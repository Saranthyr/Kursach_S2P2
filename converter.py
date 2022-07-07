import datetime
import mimetypes
import os.path
import uuid
import flask

import config
import db
import worker
from auth import auth_req

bp = flask.Blueprint('convert', __name__, url_prefix='/feat/')

conn = db.conn()


@bp.route('/convert', methods=['POST', 'GET'])
@auth_req
def exp():
    cur = conn.cursor()
    user = flask.session.get('user_id')
    cur.execute('select username from users where id = %s', (user,))
    username = cur.fetchone()[0]
    if flask.request.method == 'POST':
        default_val = None

        file = flask.request.files.get('file')
        upscale = flask.request.form.get('upscale', default_val)
        ext = flask.request.form.get('ext')
        quality = flask.request.form.get('quality', default_val)
        filename = flask.request.form.get('filename')
        trim = flask.request.form.get('trim', default_val)
        timestart = flask.request.form.get('time_start', default_val)
        length = flask.request.form.get('length', default_val)
        endtime = flask.request.form.get('endtime', default_val)
        fps_input = flask.request.form.get('fps', default_val)

        filename = os.path.basename(filename)
        orig_fname, base_ext = os.path.splitext(filename)

        width = None
        height = None
        v_btr = None
        a_btr = None

        if ext == 'no_change':
            ext = base_ext
        if fps_input is None:
            fps = '30'
        else:
            fps = fps_input
        if upscale is not None:
            if fps == '30':
                width, height, v_btr, a_btr = '1920', '1080', '3500k', '128k'
                if quality == '2K':
                    width, height, v_btr, a_btr = '2560', '1440', '7500k', '192k'
                if quality == '4K':
                    width, height, v_btr, a_btr = '3840', '2160', '17000k', '320k'
            else:
                if quality == '2K':
                    width, height, v_btr, a_btr = '2560', '1440', '12000k', '192k'
                if quality == '4K':
                    width, height, v_btr, a_btr = '3840', '2160', '30000k', '320k'

        name = str(uuid.uuid4())
        source = config.Config.STORAGE_SETTINGS.video_folder + filename
        output = config.Config.STORAGE_SETTINGS.video_folder + name
        file.save(source)

        if worker.convert(source, output, ext, fps, v_btr, a_btr, width, height, timestart, endtime, length) == 400:
            return flask.make_response(flask.jsonify({'error': 'something went wrong. please, contact admins'}), 220)
        else:
            cur.execute('insert into files'
                        ' (id, owner_id, original_name, created_at, size, ext)'
                        ' values (%s, %s, %s, %s, %s, %s)',
                        (name,
                         user,
                         orig_fname,
                         datetime.datetime.now(),
                         round(os.path.getsize(config.Config.STORAGE_SETTINGS.video_folder + name + ext) / (1024 * 1024),
                               2),
                         ext),)
            cur.close()
            conn.commit()
            return flask.render_template('converter.html', user_logged=True, username=username)
    else:
        return flask.render_template('converter.html', user_logged=True, username=username)

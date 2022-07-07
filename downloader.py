import flask
import auth
import config
import db

bp = flask.Blueprint('downloader', __name__, url_prefix='/files')
con = db.conn()


@bp.route('/<fileid>')
@auth.auth_req
def downloader(fileid):
    curr_usr = flask.session.get('user_id')
    cur = con.cursor()
    cur.execute('select owner_id, original_name, ext from files where id = %s', (fileid,))
    owner, fname, ext = cur.fetchone()
    return flask.send_file(config.Config.STORAGE_SETTINGS.video_folder + '/' + fileid + ext, download_name=fname + '.' + ext)

@bp.route('/vids/<fileid>')
def vid_md(fileid):
    cur = con.cursor()
    cur.execute('select ext from files where id = %s', (fileid,))
    ext = cur.fetchone()[0]
    return str(flask.url_for('static', filename='/vids/' + fileid  + '.'+ ext))

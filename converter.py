import uuid
import flask
import worker
import os
from auth import auth_req

bp = flask.Blueprint('convert', __name__, url_prefix='/pt')


@bp.route('/convert', methods=['POST', 'GET'])
@auth_req
def exp():
    if flask.request.method == 'POST':
        file = flask.request.files.get('file')
        upscale = flask.request.form.get('upscale')
        ext = flask.request.form.get('ext')
        quality = flask.request.form.get('quality')

        width = '1920'
        height = '1080'

        if quality == '4K':
            width, height = '3840', '2160'
        if quality == '2K':
            width, height = '2560', '1440'

        name = str(uuid.uuid4())
        file.save('vids/' + name + ext)
        worker.convert('vids/' + name + ext, str(uuid.uuid4()), '3500k', '128k', ext, upscale, width, height)
        return flask.render_template('base.html')
    else:
        return flask.render_template('base.html')




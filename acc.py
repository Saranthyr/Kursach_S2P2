import flask
import werkzeug.security
from auth import auth_req
import db

bp = flask.Blueprint('account', __name__, url_prefix='')

connect = db.conn()

def get_user(user_id, username):
    cursor = connect.cursor()
    cursor.execute('select username from users where id = %s', (user_id,))
    user = cursor.fetchone()[0]
    cursor.close()

    if username != user:
        flask.abort(403)


def check_user_exists(username):
    cur = connect.cursor()
    cur.execute('select username from users where username = %s', (username,))
    if cur.fetchone() is None:
        cur.close()
        flask.abort(404)


@bp.route('/<username>/settings', methods=['POST', 'GET'])
@auth_req
def settings(username):
    curr_user = flask.session.get('user_id')
    check_user_exists(username)
    get_user(username=username, user_id=curr_user)

    if flask.request.method == 'GET':
        return flask.render_template('settings.html', username=username)

    if flask.request.method == 'POST':
        old_password = flask.request.form.get('old_pwd')
        new_password = flask.request.form.get('new_pwd')
        new_password_repeat = flask.request.form.get('new_pwd_repeat')

        cur = connect.cursor()

        cur.execute('select hashed_pswd from users where id = %s', (curr_user,))
        hashed = cur.fetchone()[0]

        if werkzeug.security.check_password_hash(hashed, old_password):
            if new_password == new_password_repeat:
                cur.execute('update users set hashed_pswd = %s where id = %s',
                            (werkzeug.security.generate_password_hash(new_password, method='sha512'),
                             curr_user,))
                cur.close()
                connect.commit()
                return flask.Response(status=200)
            else:
                return flask.Response(status=255)
        else:
            return flask.Response(status=265)


@bp.route('/<username>', methods=['GET'])
@auth_req
def profile(username):
    curr_user = flask.session.get('user_id')
    check_user_exists(username)
    get_user(username=username, user_id=curr_user)
    return flask.render_template('profile.html', username=username)


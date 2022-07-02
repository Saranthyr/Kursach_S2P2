import flask
import db
import werkzeug.security
import functools


bp = flask.Blueprint('auth', __name__, url_prefix='')


def auth_req(view):
    @functools.wraps(view)
    def wrapped(**kwargs):
        if flask.session.get('user_id') is None:
            return flask.redirect(flask.url_for('auth.login'))

        return view(**kwargs)

    return wrapped



@bp.route('/login', methods=['POST', 'GET'])
def login():
    if flask.request.method == 'GET':
        return flask.render_template('login.html')
    if flask.request.method == 'POST':
        username = flask.request.form.get('username')
        pwd = flask.request.form.get('password')

        cursor = db.conn()
        cursor.execute('select hashed_pswd, id from users where username = %s', (str(username),))
        resp = cursor.fetchone()
        hashed = resp[0]
        user_id = resp[1]

        if werkzeug.security.check_password_hash(hashed, pwd):
            flask.session.clear()
            flask.session['user_id'] = user_id
        return flask.Response(status=200)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if flask.request.method == 'GET':
        return flask.render_template('register.html')


@bp.route('logout', methods=['POST'])
def logout():
    return flask.make_response(200)



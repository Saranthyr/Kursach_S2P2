import uuid

import flask
import db
import werkzeug.security
import functools


bp = flask.Blueprint('auth', __name__, url_prefix='')
con = db.conn()


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

        cursor = con.cursor()
        cursor.execute('select hashed_pswd, id from users where username = %s', (str(username),))
        resp = cursor.fetchone()
        if resp is not None:
            cursor.close()
            hashed = resp[0]
            user_id = resp[1]

            if werkzeug.security.check_password_hash(hashed, pwd):
                flask.session.clear()
                flask.session.permanent = True
                flask.session['user_id'] = user_id
                return flask.Response(status=200)
            else:
                return flask.Response(status=215)
        else:
            return flask.Response(status=225)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if flask.request.method == 'GET':
        return flask.render_template('register.html')
    if flask.request.method == 'POST':
        cur = con.cursor()

        username = flask.request.form.get('username')
        password = flask.request.form.get('pwd')
        repeat_password = flask.request.form.get('pwd_rep')

        cur.execute('select username from users where username = %s', (username,))
        if cur.fetchone() is None:
            if password == repeat_password:
                password = werkzeug.security.generate_password_hash(password, method='sha512')
                cur.execute('insert into users (username, hashed_pswd, id, role_id) values (%s, %s, %s, %s)',
                            (username, password, str(uuid.uuid4()), '1'))
                con.commit()
                cur.close()
                return flask.Response(status=200)
            else:
                return flask.Response(status=255)
        else:
            return flask.Response(status=254)


@bp.route('/logout', methods=['POST'])
def logout():
    if flask.request.method == 'POST':
        flask.session.clear()
        return flask.make_response(flask.jsonify({'url': flask.url_for('auth.login')}), 302)

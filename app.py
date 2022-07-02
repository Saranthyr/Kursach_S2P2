import datetime
import flask
import prot
import auth

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'f15b4580900bb7315f76b211eb7566d013f4015a16d9cda874860ea31e101aa8af357e071bd4abad9c354f3686b3a876bd1dd88a12a47f8b6f2e632a77961a7b'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=30)

app.register_blueprint(prot.bp)
app.register_blueprint(auth.bp)

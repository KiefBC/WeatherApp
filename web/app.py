import sys, os
from views import MainIndexView, DeleteCity
from models import db, app

app.add_url_rule('/', view_func=MainIndexView.as_view('index'))
app.add_url_rule('/delete/<int:city_id>', view_func=DeleteCity.as_view('delete_city'))

with app.app_context():
    db.drop_all()
    db.create_all()

key = os.urandom(24)

app.config.update({
    'DEBUG': True,
    'TESTING': True,
    'SECRET_KEY': f'{key}',
})


# don't change the following way to run flask:
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()

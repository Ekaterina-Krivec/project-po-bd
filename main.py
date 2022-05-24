from flask import Flask, redirect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import *
from db_setup import init_db, session
init_db()

app = Flask(__name__)
app.secret_key = 'shdbghbdfhgbdfjhbgjhdfbgjhbdfjhgbdfjhbgjhdfbgjbd'
app.config['FLASK_ADMIN_SWATCH'] = 'cosmo'

admin = Admin(app, name='Art Territory')
admin.add_view(ModelView(Painting, session))
admin.add_view(ModelView(Auction, session))
admin.add_view(ModelView(Exhibition, session))
admin.add_view(ModelView(PotentialBuyer, session))
admin.add_view(ModelView(Artist, session))
 
 
@app.route('/', methods=['GET'])
def main():
    return redirect('/admin/')


if __name__ == '__main__':
    app.run()

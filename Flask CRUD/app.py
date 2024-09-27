from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Model creation
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Name: {self.first_name}, Age: {self.age}"

# Home route where users are displayed in a table
@app.route('/')
def home():
    users = User.query.all()  # Fetch all users from the database
    return render_template('home.html', users=users)



# Add user route to handle form submission
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Get data from the form
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        
        # Create a new User object
        if first_name != '' and last_name != '' and age is not None:
            new_user = User(first_name=first_name, last_name=last_name, age=age)
            # Add to the database
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            return "confirm('Are you sure you want to delete this user?');"

    return render_template('addUser.html')


@app.route('/delete/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)  # Get the user by ID
    db.session.delete(user)  # Delete the user from the session
    db.session.commit()  # Commit the changes
    return redirect(url_for('home'))  # Redirect back to the home page


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

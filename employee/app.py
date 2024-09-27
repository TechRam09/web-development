from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Model creation
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    salary = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Employee: {self.name}, Experience: {self.experience}, Salary: {self.salary}"

# Home route where employees are displayed in a table
@app.route('/')
def home():
    employees = Employee.query.all()  # Fetch all employees from the database
    return render_template('home.html', employees=employees)

# Add employee route to handle form submission
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Get data from the form
        name = request.form['name']
        experience = request.form['experience']
        salary = request.form['salary']
        
        # Create a new Employee object
        if name != '' and experience is not None and salary is not None:
            new_employee = Employee(name=name, experience=int(experience), salary=float(salary))
            # Add to the database
            db.session.add(new_employee)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            return "Please fill in all the details"

    return render_template('addEmployee.html')

# Delete employee route
@app.route('/delete/<int:employee_id>', methods=['GET'])
def delete_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

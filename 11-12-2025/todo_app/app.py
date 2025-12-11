from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# ------------------- DATABASE CONFIG -------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# ------------------- DATABASE MODEL -------------------
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(300))
    status = db.Column(db.String(20), default="Pending")
    created_at = db.Column(db.DateTime, default=datetime.now)


# ------------------- VIEW ALL TASKS -------------------
@app.route("/")
def index():
    tasks = Task.query.order_by(Task.id.desc()).all()
    return render_template("index.html", tasks=tasks)


# ------------------- ADD TASK -------------------
@app.route("/add", methods=["POST"])
def add_task():
    title = request.form["title"]
    description = request.form["description"]

    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()

    return redirect("/")


# ------------------- MARK COMPLETE -------------------
@app.route("/complete/<int:id>")
def complete_task(id):
    task = Task.query.get(id)
    task.status = "Completed"
    db.session.commit()
    return redirect("/")


# ------------------- EDIT TASK -------------------
@app.route("/edit/<int:id>", methods=["POST"])
def edit_task(id):
    task = Task.query.get(id)
    new_title = request.form["new_title"]
    task.title = new_title
    db.session.commit()
    return redirect("/")


# ------------------- DELETE TASK -------------------
@app.route("/delete/<int:id>")
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect("/")


# ------------------- CREATE DB IF NOT EXISTS -------------------
with app.app_context():
    db.create_all()

# ------------------- RUN APP -------------------
if __name__ == "__main__":
    app.run(debug=True)
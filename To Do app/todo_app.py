import requests
from flask import Flask, render_template, redirect, url_for, request
from sqlalchemy import Column, Integer, String, Boolean, create_engine, ForeignKey, URL, DATE
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

app = Flask(__name__)
# ----------------- date trigger ---------------------#
today = datetime.today().strftime("%d/%m/%Y")

# ------------------- Data base ----------------------#
Base = declarative_base()


class Tasks(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    task = Column(String, nullable=False)
    date = Column(String, nullable=False)
    is_done = Column(Boolean)

    def __init__(self, task, date, is_done):
        self.task = task
        self.date = date
        self.is_done = is_done

    def __repr__(self):
        return f"{self.task} Date:{self.date},Done:{self.is_done}"


class DoneTask(Base):
    __tablename__ = "done"
    id = Column(Integer, primary_key=True)
    task = Column(String, nullable=False)
    date = Column(String, nullable=False)
    is_done = Column(Boolean, nullable=False)

    def __init__(self, task, date, is_done):
        self.task = task
        self.date = date
        self.is_done = is_done

    def __repr__(self):
        return f"ID:{self.id} Task:{self.task} Date:{self.date} Done:{self.is_done}"


class Major(Base):
    __tablename__ = "majors"
    id = Column(Integer, primary_key=True)
    major = Column(String, nullable=False, unique=True)

    def __init__(self, major):
        self.major = major

    def __repr__(self):
        return f"ID:{self.id} Major:{self.major}"


engin = create_engine("sqlite:///tasks.db", echo=True)
Base.metadata.create_all(bind=engin)
Session = sessionmaker(bind=engin)
session = Session()

# new_task = Tasks(
#     task="Home word"
# )
#
#
# # session.add(new_task)
# # session.commit()
# major = Major(major="Home Work")
# session.add(major)
# session.commit()

# ------------------ Route ------------------------------#
tasks = []
dates = []
majors = []
done_date = []


@app.route("/", methods=["POST", "GET"])
def home():
    global tasks, dates, majors
    all_tasks = session.query(Tasks).all()
    date = request.args.get("date")
    filter_by_date = session.query(Tasks).filter_by(date=date)
    all_majors = session.query(Major).all()
    majors = set(all_majors)
    # ------------------------ get done task -------------#
    # filter done task
    task_done_date = request.args.get("done_date")
    filtered_done_task = session.query(DoneTask).filter_by(date=task_done_date)
    done_tasks = session.query(DoneTask).all()
    for task in done_tasks:
        done_date.append(task.date)
    if not task_done_date or task_done_date == "All":
        done_tasks = done_tasks
    else:
        done_tasks = filtered_done_task

    if not done_tasks:
        done_tasks = []
    if not date:
        tasks = all_tasks
    else:
        for TASK in all_tasks:
            dates.append(TASK.date)
        if date != "All":
            tasks = filter_by_date
        else:
            tasks = all_tasks
    return render_template("index.html", tasks=tasks, dates=set(dates), done_tasks=done_tasks, majors=majors,
                           today=today, date=date, done_date=set(done_date), done_task_date=task_done_date)


@app.route("/add_task", methods=["POST", "GET"])
def add_task():
    if request.method == "POST":
        task = Tasks(task=request.form.get("newTask").capitalize(), date=today, is_done=False)
        session.add(task)
        session.commit()
    return redirect(url_for("home"))


@app.route("/delete_update_task", methods=["POST", "GET"])
def delete_task():
    if request.method == "POST":
        task_id = request.form.get("checkbox")
        task_to_delete = session.query(Tasks).get(task_id)
        # --------------- save done task to DoneTask ---------------------#
        done_task = DoneTask(task=task_to_delete.task, date=task_to_delete.date, is_done=True)
        session.add(done_task)
        session.commit()
        # --------------- delete done task from Tasks Db ------------------#
        if task_to_delete is not None:
            session.delete(task_to_delete)
            session.commit()
    return redirect(url_for("home"))


@app.route("/add_title", methods=["POST", "GET"])
def add_major():
    if request.method == "POST":
        new_major = request.form.get("new_major")
        major = Major(major=new_major.capitalize())
        session.add(major)
        session.commit()
        return redirect(url_for("home"))


@app.route("/delete_title", methods=["POST", "GET"])
def delete_major():
    if request.method == "POST":
        major_id = request.form.get("title_id")
        to_delete_major = session.query(Major).get(major_id)
        session.delete(to_delete_major)
        session.commit()
    return redirect(url_for("home"))


@app.route("/toggle_task", methods=["POST", "GET"])
def toggle_task():
    if request.method == "POST":
        # ------------- reverse the task to the Tasks DB -------------#
        print(request.form.get("checked"))
        # --------- get delete id and delete it from DoneTask ---------#
        delete_id = request.form.get("trash")
        print(delete_id, "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        if delete_id:
            done_to_delete = session.query(DoneTask).get(delete_id)
            session.delete(done_to_delete)
            session.commit()
    return redirect(url_for("home"))


# all_todo = session.query(Tasks).with_entities(Tasks.date).first()
# dates = set(all_todo)
# for date in dates:
#     print(date)
# print(dates)

# print(all_todo)

if __name__ == "__main__":
    app.run(debug=True)

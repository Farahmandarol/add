from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField("Cafe Location on Google Maps(URL)", validators=[DataRequired()])
    open = StringField("Opening Time e.f.8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g.5:30PM", validators=[DataRequired()])
    rating = SelectField("Coffee Rating", validators=[DataRequired()], choices=("☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"))
    wifi = SelectField("Wifi Strength Rating", validators=[DataRequired()],
                       choices=("✘", "💪", "💪 💪", "💪 💪 💪", "💪 💪 💪 💪", "💪 💪 💪 💪 💪 💪 "))
    power = SelectField("Power Socket Avialiability", validators=[DataRequired()],
                        choices=("✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"))
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", "a", encoding="utf-8") as file:
            file.write("\n")
            file.write(
                f"{form.cafe.data},{form.location.data},{form.open.data},{form.close.data},{form.rating.data},{form.wifi.data},{form.power.data}")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open("cafe-data.csv", encoding="utf8", newline="") as csvfile:
        csv_data = csv.reader(csvfile, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows, i=len(list_of_rows[0]))


if __name__ == '__main__':
    app.run(debug=True)

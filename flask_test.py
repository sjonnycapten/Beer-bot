from flask import Flask, redirect, url_for, render_template
from person import Person
from truff import TurffConnection

#create a connection to the turf website

conn = TurffConnection()

persons = []
persons.append(Person("wwzbim0rjmkzio1","Jan"))
persons.append(Person("zlzvgjzzvvhsk7w","robbert"))
persons.append(Person("uj78s35grni6jlk","Hermen"))
persons.append(Person ("684ctg3li5eqyzo","Gideon"))
persons.append(Person("2onlcbqfi5zad98","Rudolf"))


personIndex = 0
test =5
app = Flask(__name__)
@app.route("/")
def home():
    print("home")
    records = conn.GetLogData()
    person = persons[1]
    bc = person.GetBeerCount(records)
    return render_template("base.html",name = person.name,score = bc)
if __name__ == "__main__":
    app.run() 

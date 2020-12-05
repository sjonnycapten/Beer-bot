from flask import Flask, redirect, url_for, render_template
from person import Person
from truff import TurffConnection

#create a connection to the turf website

conn = TurffConnection()

persons = []
persons.append(Person("wwzbim0rjmkzio1","Jan",-24))
persons.append(Person("zlzvgjzzvvhsk7w","robbert",0))
persons.append(Person("uj78s35grni6jlk","Hermen",0))
persons.append(Person ("684ctg3li5eqyzo","Gideon",-48))
persons.append(Person("2onlcbqfi5zad98","Rudolf",0))


app = Flask(__name__)
@app.route("/<num>")
def home(num):
    #print("home")
    records = conn.GetLogData()
    person = persons[int(num)]
    bc = person.GetBeerCount(records)
    return render_template("base.html",name = person.name,score = bc)
if __name__ == "__main__":
    app.run() 

from flask import Flask, redirect, url_for, render_template
from person import Person
from truff import TurffConnection

#create a connection to the turf website

conn = TurffConnection()

persons = []
persons.append(Person("wwzbim0rjmkzio1","Jan",-24))
persons.append(Person("zlzvgjzzvvhsk7w","Robbert",0))
persons.append(Person("uj78s35grni6jlk","Hermen",0))
persons.append(Person ("684ctg3li5eqyzo","Gideon",-48))
persons.append(Person("2onlcbqfi5zad98","Rudolf",0))
persons.append(Person("coto0kfyp1ewvyk","Gernt",0))


names = []
scores = []

app = Flask(__name__)
@app.route("/")
def home():
    names.clear()
    scores.clear()
    records = conn.GetLogData()
    for p in persons:
        p.GetBeerCount(records)
    count = 0
    list = sorted(persons,key=lambda p:p.beerCount )
    for l in list:
        names.append(l.name)
        scores.append(l.beerCount)
    return render_template("base.html",names = names,scores = scores)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
    
 
 
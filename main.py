
from person import Person
from truff import TurffConnection

conn = TurffConnection()
records = conn.GetLogData()

jan = Person("wwzbim0rjmkzio1","Jan",0)
robbert = Person("zlzvgjzzvvhsk7w","robbert",0)
hermen = Person("uj78s35grni6jlk","Hermen",0)
gideon = Person ("684ctg3li5eqyzo","Gideon",0)
rudolf = Person("2onlcbqfi5zad98","Rudolf",0)




print("jan: ",jan.GetBeerCount(records))
print("robbert: ",robbert.GetBeerCount(records))
print("gideon: ",gideon.GetBeerCount(records) -48)
print("hermen: ",hermen.GetBeerCount(records))
print("rudolf: ",rudolf.GetBeerCount(records))

x = gideon.GetPersonalRecords(records)




#http://127.0.0.1:5000/
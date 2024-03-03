from many_to_many import NationalPark
from many_to_many import Visitor
from many_to_many import Trip

v1 = Visitor("Dueshbad")
v2 = Visitor("Moronifon")
v3 = Visitor("Hate you")
v4 = Visitor("Shut it")

np = NationalPark("Lincoln Park")
np1 = NationalPark("Alki Beach")
np2 = NationalPark("the middle east")
np3 = NationalPark("Gaza")

trip = Trip(v1, np1, "May 7th", "May 9th")
trip1 = Trip(v2, np3, "August 20th", "August 27th")
trip2 = Trip(v1, np2, "July 3rd", "July 17th")
# trip3 = Trip(v4, np, "December 6th", "December 25th")

# print(v1._national_parks)
# print(NationalPark.best_visitor(np3))
print(v1)
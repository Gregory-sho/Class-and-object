class Student:
##    # [assignment] Skeleton class. Add your code here
 def __init__(self,name,age,tracks,score):
     self.name = str(name)
     self.age = int(age)
     self.tracks = list(tracks)
     self.score = float(score)
     
 def change_name(self, new_name):
         self.name = new_name
         new_name = "Gregory"
         print("the student updated his name to", new_name)

 def change_age (self,new_age):
             self.age = new_age
             new_age = 35
             print("the student updated his age to", new_age)

 def add_tracks(self, new_tracks):
                 self.tracks = new_tracks
                 new_tracks = ("UI/UX")
                 print("the student updated his age to", new_tracks)

 def get_score(self, new_score):
     self.score = new_score
     new_score = 3.5
     print("the student updated his age to", new_score)
          
     




Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
### Expected methods
Bob.change_name("Gregory")
Bob.change_age(35)
Bob.add_tracks("UI/UX")
Bob.get_score(3.5)



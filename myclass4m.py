class Bclass:
  def --init--(self,studentsName,grade):
    self.studentsName=studentsName
    self.grade=grade
  def performane(self,grade):
    if grade>=60:
      print("exelled in exam")
    else:
      print("unfortunately failed")
p1=Bclass('Alan',72)


class Bclass:
    def __init__(self, student, grade):
        self.student = student
        self.grade = grade

    def performance(self):
        if self.grade >= 60:
            return f"{self.student} excelled in the exam"
        else:
            return f"{self.student} unfortunately failed"
p1 = Bclass('Alan', 72)
result = p1.performance()
print(result)



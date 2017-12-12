
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        return cls(friend_name, origin.school, *args, **kwargs)

    # def schools(self, schools_name):
    #     return Student(self.name, schools_name)

# anna = Student("Anna", "MIT")
# friend = anna.friend("Greg")
# john = Student("John", "MIT")
# schools = john.schools("Oxford")
# print(friend.name)
# print(friend.school)
# print(schools.name)
# print(schools.school)

    # def friend(self, friend_name):
    #     return Student(friend_name, self.school)

##


class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title

anna = WorkingStudent("Anna", "MIT", 30.00, "software dewloper")
print(anna.salary)

friend = WorkingStudent.friend(anna, "Greg", 20.00, "software developer")
# anna is the origin, "Greg" is friend_name, 20.00 is *args, job_title="software deweloper" is ** kwargs
print(friend.name)
print(friend.school)
print(friend.salary)

class Student:
    def __init__(self, name, surname, age, grade_point_average):
        self.name = name
        self.surname = surname
        self.age = age
        self.grade_point_average = grade_point_average

    def new_grade_point_average(self, new_grade):
        self.grade_point_average = new_grade

    def get_info(self):
        print(f'{self.name}, {self.surname}, {self.age}, {self.grade_point_average}')


student_1 = Student('Vasy', 'Vasilev', 22, 155)


student_1.new_grade_point_average(60)
student_1.get_info()

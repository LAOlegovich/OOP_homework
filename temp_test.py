class Student:
    items = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.items.append(self)
    def put_estimates(self,lector,course, grade):
        """Метод выставления оценки лектору от студента за конкретный курс"""
        if isinstance(lector,Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.estimates:
                lector.estimates[course] += [grade]
            else:
                lector.estimates[course] = [grade]
        else:
            return 'Некорректные входные параметры!'          
    @property
    def avg_grade(self):
        mass_grades = [i for val in self.grades.values() for i in val]
        return sum(mass_grades)/len(mass_grades) if len(mass_grades) !=0 else 0
    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grade}" \
           f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}"\
           f"\nЗавершенные курсы: {', '.join(self.finished_courses)}")
    def __lt__(self,other):
        if isinstance(other, Student):
            return self.avg_grade < other.avg_grade
        else: 
            return None
    def __le__(self,other):
        if isinstance(other, Student):
            return self.avg_grade <= other.avg_grade
        else: 
            return None 
    def __eq__(self,other):
        if isinstance(other, Student):
            return self.avg_grade == other.avg_grade
        else: 
            return None

        

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        """Метод реализует выставление оценки выбранному студенту за конкретный курс"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Некорректные входные параметры!'
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    items = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.estimates = {}
        Lecturer.items.append(self)
    @property
    def avg_estimate(self):
        mass_est = [i for val in self.estimates.values() for i in val]
        return sum(mass_est)/len(mass_est) if len(mass_est) != 0 else 0
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_estimate}"
    def __lt__(self,other):
        if isinstance(other, Lecturer):
            return self.avg_estimate < other.avg_estimate
        else:
            return None
    def __le__(self,other):
        if isinstance(other, Lecturer):
            return self.avg_estimate <= other.avg_estimate
        else:
            return None        
    def __eq__(self,other):
        if isinstance(other, Lecturer):
            return self.avg_estimate == other.avg_estimate
        else:
            return None
        

def get_avg_estimate_of_all_students(list_of_students, course):
    """Функция подсчета средней оценки студентов по заданному курсу"""
    mass= []
    for val in list_of_students:
        if val.grades.get(course):
            mass += val.grades[course]
    return 0 if len(mass) == 0 else round(sum(mass)/len(mass),2)

def get_avg_estimate_of_all_lectors(list_of_lectors, course):
    """Функция подсчета средней оценки лекторов за заданный курс"""
    mass =[]
    for val in list_of_lectors:
        if val.estimates.get(course):
            mass += val.estimates[course]
    return 0 if len(mass) == 0 else round(sum(mass)/len(mass),2) 


student1 = Student('Ruoy', 'Eman', 'man')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Java']
student1.finished_courses = ['HTML']

student2 = Student('Erman', 'Houkhing', 'man')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['CSS']
student2.finished_courses = ['C#']
 
reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Java']

reviewer2 = Reviewer('May', 'Day')
reviewer2.courses_attached += ['Java']
reviewer2.courses_attached += ['CSS']

lector1 = Lecturer('Adam','Bruan')
lector1.courses_attached =['Python','Java', 'CSS']

lector2 = Lecturer('Bob','Dilan')
lector2.courses_attached =['Python', 'CSS']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Java', 7)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 8)

reviewer2.rate_hw(student1, 'Java', 7)
reviewer2.rate_hw(student2, 'CSS', 9)
reviewer2.rate_hw(student2, 'CSS', 8)

student1.put_estimates(lector1,'Python',6)
student1.put_estimates(lector2,'Python',8)
student2.put_estimates(lector1,'CSS',9)
student2.put_estimates(lector2,'CSS',10)
 
print(student1)

print(lector2)

print(reviewer1)

print(student1 <= student2)

print(lector1 == lector2)

print('Средняя оценка студентов за домашние задания по курсу:', get_avg_estimate_of_all_students(Student.items, 'Python'))

print('Средняя оценка лекторов в рамках курса:', get_avg_estimate_of_all_lectors(Lecturer.items,'CSS'))

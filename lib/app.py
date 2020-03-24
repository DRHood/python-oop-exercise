class Member:
    def __init__(self, full_name):
        self.full_name = full_name

    def introduce(self):
        return(f'Hi! My name is {self.full_name}')

class Student(Member):
    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.reason = reason

    # imported greeting
    def greet(self):
        print(f'{self.introduce()}, {self.reason}.')

class Instructor(Member):
    def __init__(self, full_name, bio):
        super().__init__(full_name)
        self.bio = bio
        self.skills = []

    def add_skill(self, newSkill):
        self.skills.append(newSkill)

    def greet(self):
        print(f'{self.introduce()}, {self.bio}. I have the following skills: {self.skills}')

class Workshop:
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.instructors = []

    def add_participant(self, new_participant):
        if isinstance(new_participant, Instructor)
            self.instructors.append(new_participant)
        elif isinstance(new_participant, Student)
            self.students.append(new_participant)


    def get_participants(self):
        participant_list = []
        for participant in self.participants:
            participant_list.append(participant.full_name)
        return participant_list

    def print_details(self):
        print('Workshop - {} - {}'.format(self.date, self.subject))
        print()
        print('Students')
        for i in range(len(self.students)):
            student = self.students[i]
            print('{}. {} - {}'.format(i + 1, student.full_name, student.reason))
        print()
        print('Instructors')
        for instructor in self.instructors:
            for instructor in self.instructors:
            print('{} - {}'.format(instructor.full_name, ', '.join(instructor.skills)))
            print('{}'.format(instructor.bio))

# testy things
workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
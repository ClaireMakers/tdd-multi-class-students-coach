class Coach:
    def __init__(self, name):
        self.name = name
        self.students_list = []

    def add_student(self, student):
        self.students_list.append(student)
    
    def count_submissions(self):
        count = 0

        for student in self.students_list: 
            print(student.count_submissions())
            count = count + student.count_submissions()
        
        return count
    
    def print_student_names(self):
        pass
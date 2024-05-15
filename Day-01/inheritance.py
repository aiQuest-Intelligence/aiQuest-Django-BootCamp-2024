class Studymart:
    def free_course(self):
        print('Python')
    def free_course2(self):
        print('Django')

class AiQuest(Studymart):
    def course(self):
        print('ML')
    def course2(self):
        print('DL')

a = Studymart()
a.free_course2()

b = AiQuest()
b.course()
b.free_course2()
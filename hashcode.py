# we are opening up the text file and we are setting the array 'lines' to contain the entire contents
# however, currently we still have \n characters however since python does a lot of the work for us we need to strip

class Skill:
    def __init__(self, name, level):
        self.name = name
        self.level = level

class Person:
    def __init__(self, name, skill_amount):
        self.name = name
        self.skills = [None] * skill_amount
    def set_skill(self,skill):
        for s in self.skills:
            if s != None:
                s = skill
    def print_person(self):
        return str("name: "+self.name + " level: " +str(self.skills))
    def addSkill(self, name, level):
        self.skills.append(Skill(name, level))

class Project:
    def __init__(self, name, compl, score, best_before, role_count):
        self.name = name
        self.compl = compl
        self.score = score
        self.best_before = best_before
        self.role_count = role_count
        # self.skills = [None] * skill_amount

    def addRole(self, name, level):
        self.skills.append(Skill(name, level))
        

def main():
    with open('./a_an_example.in.txt') as f: lines = f.readlines()
    for line in enumerate(lines): lines[line[0]] = line[1].replace('\n','')



    FILE_HEADER = lines[0].split(' ')
    NUM_PEOPLE, NUM_PROJECTS = int(FILE_HEADER[0]), int(FILE_HEADER[1])

    # print(f'num people: {NUM_PEOPLE} num projects: {NUM_PROJECTS}')
    people = [None] * NUM_PEOPLE
    #lets iterate over every person 
    for i in range(1,NUM_PEOPLE+1):
        person_data = lines[i].split(' ')
        people[i-1] = Person(person_data[0], int(person_data[1]))
        for j in range(people[i-j]):
            print(lines[i])
    print(people[1].name)

        

if __name__ == '__main__':
    main()
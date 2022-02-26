from hashcode import skill, person, project


anna = Person("Anna", 1)
bob = Person("Bob", 2)
maria = Person("Maria", 1)

anna.addSkill("C++", 2)
bob.addSkill("HTML", 5)
bob.addSkill("CSS", 5)
maria.addSkill("Python", 3)

logging = Project("Logging", 5, 10, 5, 1)
webserver = Project("WebServer", 7, 10, 7, 2)
webchat = Project("WebChat", 10, 20, 20, 2)

logging.addRole("C++", 3)
webserver.addRole("HTML", 3)
webserver.addRole("C++", 2)
webchat.addRole("Python", 3)
webchat.addRole("HTML", 3)

people = [anna, bob, maria]

projects = [logging, webserver, webchat]










# Traverse all of the projects and find suitable people
# people: List of person objects
# projects: List of project objects
def sol(people, projects):
    return recursive([],[],people,projects)
    
def recursive(succ_list, job_queue, people, projects):
    if projects == []:
        return (succ_list,True)
    #Loop each project to find suitable one
    for proj in projects:
        for pers in people:


    
    # If no solution and queue has items, pass time by one day
    if len(job_queue):
        for jobs in job_queue:
            jobs[2]-= 1
            if jobs[2] == 0:
                people.add(job_queue)
            
    return recursive (succ_list, job_queue, people, projects)
            

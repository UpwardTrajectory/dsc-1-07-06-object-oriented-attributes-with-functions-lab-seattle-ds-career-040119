class School:
    def __init__(self, name, roster = {}):
        self.name = name
        self.roster = roster
    
    def add_student(self, name, grade):
        if grade in self.roster.keys():
            print(self.roster.items())
            self.roster[grade].append(name)
        else:
            self.roster[grade] = []
            self.roster[grade].append(name)
            
    def grade(self, number):
        # return a list of all the students in requested grade
        return self.roster[number]
    
    def sort_roster(self):
        output = {}
        for k, v in self.roster.items():
            output[k] = sorted(v)
        return output
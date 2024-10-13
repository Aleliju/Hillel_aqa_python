class Employee:
    name = None
    salary = None


class Manager(Employee):
    department = None


class Developer(Employee):
    programming_language = None


class TeamLead(Manager, Developer):
    team_size = None




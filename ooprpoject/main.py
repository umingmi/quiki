# @AUTHOR IAN M. LUMANOG CS201

from buildingData import departments_per_building

class Building:
    def __init__(self, name):
        self.name = name
        self.departments = {}

    def add_department(self, department, floor_level, directory):
        self.departments[department] = {"floor_level": floor_level, "directory": directory}

    def find_department(self, department):
        if department in self.departments:
            info = self.departments[department]
            return f"Department '{department}' found in {self.name} building on Floor {info['floor_level']}. Directory: {info['directory']}"
        else:
            return f"Department '{department}' not found in {self.name} building."

class School:
    def __init__(self):
        self.buildings = [
            Building("coecsa"),
            Building("annex"),
            Building("arc"),
            Building("west building"),
            Building("east building"),
            Building("sotero"),
            Building("jpl"),
        ]

    def add_departments(self, building_index, departments):
        building = self.buildings[building_index]
        for department, (floor_level, directory) in departments.items():
            building.add_department(department, floor_level, directory)

    def navigate_to_department(self, department):
        for building in self.buildings:
            result = building.find_department(department.upper())
            print(result)


lyceum = School()

# Add departments to each building
for building_index, departments in departments_per_building.items():
    lyceum.add_departments(building_index, departments)

user_choice = input("Where do you want to go?")

# Use the navigation feature to search for a department
lyceum.navigate_to_department(user_choice)
from my_project.cloud import Cloud
from my_project.database import Database
from my_project.hardware import Hardware


class MyProject:
    def __init__(self):
        self.cloud = Cloud()
        self.database = Database()
        self.hardware = Hardware()

    def run(self):
        pass



MyProject().run()

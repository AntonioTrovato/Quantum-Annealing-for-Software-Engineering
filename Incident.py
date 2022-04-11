#This class represents a reported incident
class Incident:
    
    def __init__(self, incident_id, incident_name, control_id, control_name, estimated_time):
        self.incident_id = incident_id
        self.control_id = control_id
        self.incident_name = incident_name
        self.control_name = control_name
        self.estimated_time = estimated_time
    
    def get_incident_id(self):
        return self.incident_id
    
    def set_incident_id(self, incident_id):
        self.incident_id = incident_id
    
    def get_control_id(self):
        return self.control_id
    
    def set_control_id(self, control_id):
        self.control_id = control_id
    
    def get_incident_name(self):
        return self.incident_name
    
    def set_incident_name(self, incident_name):
        self.incident_name = incident_name
    
    def get_control_name(self):
        return self.control_name
    
    def set_control_name(self, control_name):
        self.control_name = control_name
    
    def get_estimated_time(self):
        return self.estimated_time
    
    def set_estimated_time(self, estimated_time):
        self.estimated_time = estimated_time

    def __str__(self):
        return "incident_id: " + str(self.get_incident_id()) + ", incident_name: " + self.get_incident_name() + ", control_id: " \
               + str(self.get_control_id()) + ", control_name" + self.control_name + ", estimated_time: " + str(self.get_estimated_time())

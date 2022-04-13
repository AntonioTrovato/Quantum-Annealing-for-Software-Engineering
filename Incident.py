#This class represents a reported incident
class Incident:
    
    def __init__(self, threat_id, threat_name, control_id, control_name, estimated_time):
        self.threat_id = threat_id
        self.control_id = control_id
        self.threat_name = threat_name
        self.control_name = control_name
        self.estimated_time = estimated_time
    
    def get_threat_id(self):
        return self.threat_id
    
    def set_threat_id(self, threat_id):
        self.threat_id = threat_id
    
    def get_control_id(self):
        return self.control_id
    
    def set_control_id(self, control_id):
        self.control_id = control_id
    
    def get_threat_name(self):
        return self.threat_name
    
    def set_threat_name(self, threat_name):
        self.threat_name = threat_name
    
    def get_control_name(self):
        return self.control_name
    
    def set_control_name(self, control_name):
        self.control_name = control_name
    
    def get_estimated_time(self):
        return self.estimated_time
    
    def set_estimated_time(self, estimated_time):
        self.estimated_time = estimated_time

    def dump(self):
        return {'threat_id': self.get_threat_id(),
                'threat_name': self.get_threat_name(),
                'control_id': self.get_control_id(),
                'control_name': self.get_control_name(),
                'estimated_time': self.get_estimated_time()}

    def __str__(self):
        return "threat_id: " + str(self.get_threat_id()) + ", threat_name: " + self.get_threat_name() + ", control_id: " \
               + str(self.get_control_id()) + ", control_name: " + self.control_name + ", estimated_time: " + str(self.get_estimated_time())

'''
@author: Jussi Niutanen
Common fuctions for sprint automation and shorcuts
'''

#from _typeshed import Self

class MyCommonFunc:
    """ MyCommonFunc class """

    def __init__(self):
        """ Init the class """
        self.sprint_id = 0
        self.sprint_name = ""
        self.name_position = 0
        self.id_position = 0

    def get_sprint_id(self):
        """ Return sprint id """
        return self.sprint_id

    def get_sprint_name(self):
        """ Return sprint name """
        return self.sprint_name

    def get_name_position(self):
        """ Return name position """
        return self.name_position

#    def get_id_position(sel):
#        """ Return id position """
#        return self.id_position

    def get_sprint_details(self, res, active_pos):
        """ Get sprint details to the class variables """
        self.id_position = res.rfind("\'id\'", 0,active_pos)
        # Remove not needed marks from the begining of the string
        self.sprint_id = res[self.id_position+5::]
        # Copy string for later to get the name
        self.sprint_name = self.sprint_id
        # Remove not needed marks from the end of the sring
        self.sprint_id = self.sprint_id[0:self.sprint_id.find(",")]

        # Save position of the sprint name text to id parameter.
        self.name_position = self.sprint_name.find("\'name\'")
        # Remove not needed marks from the begining of the string
        self.sprint_name = self.sprint_name[self.name_position+9::]
        # Remove not needed marks from the end of the sring
        self.sprint_name = self.sprint_name[0:self.sprint_name.find("\'")]

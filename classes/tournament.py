"""
@author: António Brito / Carlos Bragança
(2025) objective: class Person
"""
# Class Person - generic version with inheritance
from classes.gclass import Gclass
class Tournament(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_tournaments_id','_tournament_name','_prize_pool']
    # Class header title
    header = 'Tournament'
    # field description for use in, for example, input form
    des = ['Id','Name','Prize Pool']
    # Constructor: Called when an object is instantiated
    def __init__(self, tournaments_id, tournament_name, prize_pool):
        super().__init__()
        # Object attributes
        id= Tournament.get_id(tournaments_id)
        self._tournaments_id = tournaments_id
        self._tournament_name = tournament_name
        self._prize_pool = prize_pool
        # Add the new object to the dictionary of objects
        Tournament.obj[id] = self
        # Add the id to the list of object ids
        Tournament.lst.append(id)
    # id property getter method
    @property
    def tournaments_id(self):
        return self._tournaments_id
    @tournaments_id.setter
    def id(self, tournaments_id):
        self._tournaments_id = tournaments_id
    # name property getter method
    @property
    def tournament_name(self):
        return self._tournament_name
    @tournament_name.setter
    def tournament_name(self, tournament_name):
        self._tournament_name = tournament_name
    # dob property getter method
    @property
    def prize_pool(self):
        return self._prize_pool
    # dob property setter method
    @prize_pool.setter
    def prizepool(self, prize_pool):
        self._prize_pool = prize_pool
    
   
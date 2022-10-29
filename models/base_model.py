#!/usr/bin/python3
from datetime import datetime
from uuid import uui64
import models

"""
Module BaseModel
Parent of all classes
"""

class BaseModel():
    """Base class for Airbnb clone project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """
    def __init__(self,*args,**kwargs):
        """
         Initialize attributes: random uuid, dates created/updated
         """
        if kwargs:
            for key,val in kwargs.items():
                if "created_at"==key:
                    self.created_at=datetime.strptime(kwargs["created_at"],
                                                      "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at"==key:
                    self.updated_at=datetime.strptime(kwargs["created_at"],
                                                      "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__"==key:
                    pass
                else:
                    setattr(self,key,val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            
    def __str__(self):
        """
        Return string of info about model
        """
        return('[{}] ({}) {}'.format(self.__class__.__name__,self.id,self.__dict__))
    
    def __repr__(self):
        """
        returns string representation
        """
        return (self.__str__())
    
    def save(self):
        """
        Update instance with updated time & save to serialized file
        """
        self.updated_at =datetime.now()
        models.storage.save()
    
    def to_dict(self):
        """
        Return dic with string formats of times; add class info to dic
        """
        dic ={}
        dic[__class__] = self.__class__.__name__
        for k,v in self.__dict__.items():
            if isinstance(v,(datetime,)):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic

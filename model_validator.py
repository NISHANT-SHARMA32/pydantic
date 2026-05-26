from pydantic import BaseModel, model_validator
from typing import Dict

class patient(BaseModel):
    age : int
    contacts : Dict[str, str]

    @model_validator(mode = 'after')
    def check(self) -> self:
        if self.age > 60 and "emergency" not in self.contacts:
            raise ValueError("u didnot provided  the emergency contact number")
        return self
        
    

data = {"age" : 45, "contacts" : {"address" : "patel nagar", "emergency" : "5986958"}}

p1 = patient(**data)

def printAll(p : patient):
    print(p.age)
    print(p.contacts["emergency"])


printAll(p1)
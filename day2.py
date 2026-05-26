from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):
    name : Annotated[str, Field(max_length=50, title= "name of the patient", examples= "nishant")]
    age : Annotated[int, Field(gt = 0, strict=True)]
    married : Annotated[bool, Field(description="Tell us you are married or not")]
    website : Optional[AnyUrl] = None
    email : EmailStr
    allergies : Optional[List[str]] = None

    @field_validator('email')
    @classmethod
    def check(cls, email):
        valid = ["hdfc.com", "icici.com"]

        data = email.split('@')[-1]

        if data not in valid:
            raise ValueError("Not a valid email address")

        return email
    
    @field_validator('name')
    @classmethod
    def toUpper(cls, value):
        return value.upper()




allergy = ["dust", "water"]
data = {"name" : "nishant", "age" : 12, "married" : True, "email" : "nishant@hdfc.com", "website" : "https://linkedin.com"}

p1 = patient(**data)

def printAllValues(p : patient):
    print(p.name)
    print(p.email)
    print(p.age)

printAllValues(p1)
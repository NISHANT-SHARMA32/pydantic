from pydantic import BaseModel

class Address(BaseModel):
    city : str
    pincode : int

class Patient(BaseModel):
    name : str
    age : int
    address : Address


add_temp = {"city" : "alwar", "pincode" : 301001}
a1 = Address(**add_temp)

data = {"name" : "nishant", "age" : 30, "address" : a1}
p1 = Patient(**data)

print(p1.address.city)
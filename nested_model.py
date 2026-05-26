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

temp = p1.model_dump_json()
print(temp)
print(type(temp))


#this also gives us the power to control what things we want to export

temp1 = p1.model_dump(include = ["name"])
print(temp1)
print(type(temp1))

#another you can aslo use exclude
temp2 = p1.model_dump(exclude = ["name"])
print(temp2)
print(type(temp2))

from pydantic import BaseModel

class Patient(BaseModel):
    name : str
    age : int


def insert_patient_name(patient : Patient):
    print(patient.name)
    print(patient.age)


patient_info = {"name" : "nishant", "age" : 49}

patient = Patient(**patient_info)

insert_patient_name(patient)



from pydantic import BaseModel, computed_field


class patient(BaseModel):
    height : int
    weight : int

    @computed_field
    def bmi(self) -> int:
        bmi = round(self.height / (self.height**2),2)
        return bmi
    

data = {"height" : 30, "weight" : 45}

p1 = patient(**data)

def printAll(p : patient):
    print(p.bmi)

printAll(p1)
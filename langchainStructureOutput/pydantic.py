from pydantic import BaseModel

class Student(BaseModel):
     name: str = "sahil"

new_student = Student(**{ "name": "sahil" })

print(new_student)
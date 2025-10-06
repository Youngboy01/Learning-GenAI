import pydantic
from typing import Optional
from pydantic import BaseModel,EmailStr,Field
class Student(BaseModel):
    name:str
    age:Optional[int] = None
    email:EmailStr
    gpa:float=Field(gt=0 , lt=10,default=5,description="It represents the cgpa of the student")#used for applying constraints
new_student = {'name':'Mitanshu','age':67,'email':'abf@nik.joi','gpa':9}#'67' pe bi output 67 hi aayega
student = Student(**new_student)
student_dict = dict(student)
print(student_dict)
print(student_dict['name'])
student_json = student.model_dump_json()
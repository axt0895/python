from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from typing import Dict, List

app = FastAPI()

class Student(BaseModel):
    student_id: int
    name: str
    email: str
    age: float
    
    
students = [
    Student(student_id=10021, name='Anil Thapa', email='axt0896@uta.edu', age=24.5),
    Student(student_id=10034, name='Kamal Pokhrel', email='kamlpok@uta.edu', age = 27.5),
    Student(student_id=10067, name='Sumar Sharma', email='sumansharm@uta.edu', age =24),
    Student(student_id=10045, name='Santosh Pokgra', email='Stanosh@uta.edu', age =23)
]

@app.get('/')
async def root():
    return {'message': 'This is a student registry'}

@app.get('/students')
async def list_students():
    return {'message': 'Here are all the students listed', 'Students': students}

@app.get('/student/{student_id}')
async def get_student(student_id: int):
    student = next((s for s in students if s.student_id == student_id), None)
    if student is None:
        raise HTTPException(status_code=404, detail=f'Student with current {student_id} not found')
    else:
        return {'message': 'Here is the given student', 'Student': student}
    
@app.post('/student')
async def add_student(student: Student):
    if any(student.student_id == s.student_id for s in students):
        raise HTTPException(status_code=400, detail=f'Student with student_id: {student.student_id} already exists')
    students.append(student)
    return {'message': 'Student is successfully added', 'Student': student}

@app.delete('/student/{student_id}')
async def delete_student(student_id: int):
    global students
    student_to_delete = next((s for s in students if s.student_id == student_id), None)
    if student_to_delete is not None:
        students = [s for s in students if s.student_id != student_id]
        return {'message': 'Student deleted successfully', 'deleted_student': student_to_delete}
    else:
        raise HTTPException(status_code=404, detail=f'Student with id {student_id} does not exist')

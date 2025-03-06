from fastapi import FastAPI
from pydantic import BaseModel
from typing import List  # Import List for type hinting

app = FastAPI()

class Course(BaseModel):
    course_id: str
    course_name: str
    course_code: int  # Consider making this a string if it's not strictly a number
    professor: str

courses: List[Course] = [  # Type hint the courses list
    Course(course_id="CSE3301", course_name="Intro to Algorithm", course_code=3456, professor="AR Rahman"),
    Course(course_id="MATH2201", course_name="Linear Algebra", course_code=1234, professor="Dr. Smith"),
    Course(course_id="PHYS3101", course_name="Quantum Mechanics", course_code=5678, professor="Prof. Johnson"),
    Course(course_id="BIO2301", course_name="Genetics", course_code=9012, professor="Dr. Lee"),
    Course(course_id="CHEM4401", course_name="Organic Chemistry", course_code=3456, professor="Prof. Garcia"),
    Course(course_id="ENG1101", course_name="Composition", course_code=7890, professor="Ms. Taylor"),
    Course(course_id="HIST2501", course_name="World History", course_code=2345, professor="Dr. Brown"),
    Course(course_id="PSYCH3201", course_name="Cognitive Psychology", course_code=6789, professor="Prof. Wilson"),
    Course(course_id="ECON1001", course_name="Microeconomics", course_code=4567, professor="Dr. Martinez"),
    Course(course_id="ART2101", course_name="Modern Art", course_code=8901, professor="Ms. Anderson")
]

@app.get("/")
async def root():
    return {"message": "This API provides information about university-level courses."}  # More descriptive message

@app.get("/courses")
async def get_courses():
    return courses  # Directly return the list of Course objects. FastAPI will handle JSON serialization.

# New endpoint to get a specific course by ID
@app.get("/courses/{course_id}")
async def get_course_by_id(course_id: str):
    for course in courses:
        if course.course_id == course_id:
            return course
    return {"message": "Course not found"}  # Return a 404-like message if not found

# New endpoint to get courses by professor
@app.get("/courses/professor/{professor_name}")
async def get_courses_by_professor(professor_name: str):
    filtered_courses = [course for course in courses if course.professor == professor_name]
    return filtered_courses
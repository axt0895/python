from fastapi import FastAPI

app = FastAPI()


student = {
    1:{
        "name": "Anil Thapa",
        "age": 26,
        "education": "The university of Texas Arlington"
    }
}

@app.get('/get/{student_id}')
def index(student_id: int):
    return student[student_id]
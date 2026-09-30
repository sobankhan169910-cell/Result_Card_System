from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

students = []

# Fixed subjects
subjects = [
    "English",
    "Urdu",
    "Mathematics",
    "Physics",
    "Computer Science",
    "Islamiat"
]


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["name"]
        father_name = request.form["father_name"]
        roll_no = request.form["roll_no"]
        student_class = request.form["student_class"]
        institution_type = request.form["institution_type"]
        institution_name = request.form["institution_name"]

        # Sirf marks user se liye jayenge
        marks = np.array([
            int(request.form["english"]),
            int(request.form["urdu"]),
            int(request.form["math"]),
            int(request.form["physics"]),
            int(request.form["computer"]),
            int(request.form["islamiat"])
        ])

        total_marks = 600
        obtained_marks = np.sum(marks)
        percentage = (obtained_marks / total_marks) * 100

        if np.all(marks >= 40):
            result = "PASS"
        else:
            result = "FAIL"

        student = {
            "name": name,
            "father_name": father_name,
            "roll_no": roll_no,
            "class": student_class,
            "institution_type": institution_type,
            "institution_name": institution_name,
            "marks": marks.tolist(),
            "total_marks": total_marks,
            "obtained_marks": obtained_marks,
            "percentage": round(percentage, 2),
            "result": result
        }

        students.append(student)

    return render_template(
        "index.html",
        students=students,
        subjects=subjects
    )


if __name__ == "__main__":
    app.run(debug=True)
import pandas as pd

def generate_data():
    data = {
        "hours_studied": [5, 10, 15],
        "sleep_hours": [6, 7, 8],
        "attendance": [70, 85, 95],
        "practice_done": [20, 50, 80],
        "days_until_exam": [5, 10, 15],
        "confidence": [2, 3, 4],
        "prior_grade": [75, 85, 95],
        "risk": [2, 1, 0]  # High, Medium, Low
    }
    df = pd.DataFrame(data)
    df.to_csv("data/student_data.csv", index=False)

if __name__ == "__main__":
    generate_data()
    print("Dataset generated")

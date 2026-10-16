# Smart Study Advisor Pipeline


# Step 1: StudentDataset
class StudentDataset:
    def __init__(self):
        self.records = []

    def add_record(self, name, score):
        self.records.append({
            "name": name,
            "score": score
        })

    def get_records(self):
        return self.records


# Step 2: Preprocessor
class Preprocessor:
    def clean_score(self, score):
        if score < 0:
            return 0
        elif score > 100:
            return 100
        else:
            return score


# Step 3: StudyModel
class StudyModel:
    def classify(self, score):
        if score >= 85:
            return "Excellent"
        elif score >= 70:
            return "Good"
        elif score >= 50:
            return "Needs Practice"
        else:
            return "Needs Support"


# Step 4: StudyAdvisor
class StudyAdvisor:
    def generate_advice(self, level):
        if level == "Excellent":
            return "Keep up the excellent work and challenge yourself with advanced tasks."

        elif level == "Good":
            return "Review difficult topics and practice regularly to improve."

        elif level == "Needs Practice":
            return "Practice more exercises and review the main concepts."

        elif level == "Needs Support":
            return "Ask for help and review the basic concepts step by step."


# Step 5: Notification Classes
class Notification:
    def send(self, message):
        print("Notification:", message)


class AppNotification(Notification):
    def send(self, message):
        print("App Notification:", message)


# Step 6: StudyAdvisorPipeline
class StudyAdvisorPipeline:
    def __init__(self):
        self.dataset = StudentDataset()
        self.preprocessor = Preprocessor()
        self.model = StudyModel()
        self.advisor = StudyAdvisor()
        self.notification = AppNotification()

    def run(self, students):
        for name, score in students:
            self.dataset.add_record(name, score)

        records = self.dataset.get_records()

        
        for record in records:

            name = record["name"]
            score = record["score"]

            clean_score = self.preprocessor.clean_score(score)

            level = self.model.classify(clean_score)

            advice = self.advisor.generate_advice(level)

            notification_message = (
                f"{name}, your performance level is {level}. "
                f"Advice: {advice}"
            )

            print("\nStudent Name:", name)
            print("Score:", clean_score)
            print("Performance Level:", level)
            print("Study Advice:", advice)
            self.notification.send(notification_message)

            print("--------------------------------------")



pipeline = StudyAdvisorPipeline()

students = [
    ("Ahmed", 92),
    ("Omar", 78),
    ("Youssef", 65),
    ("Ali", 45)
]
pipeline.run(students)
class DoctorAgent:
    def __init__(self):
        self.name = "Doctor Agent"

    def analyze_patient(self, patient_data):
        return {
            "analysis": "Medical reasoning completed",
            "recommendation": "Further diagnosis required",
            "orders": "Generate medical tests"
        }


# Example usage
doctor = DoctorAgent()

result = doctor.analyze_patient({
    "symptoms": "fever and cough"
})

print(result)

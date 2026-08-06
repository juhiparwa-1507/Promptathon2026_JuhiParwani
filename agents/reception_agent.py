class ReceptionAgent:
    def __init__(self):
        self.name = "Reception Agent"

    def collect_patient_information(self, patient):
        return {
            "patient_name": patient["name"],
            "age": patient["age"],
            "symptoms": patient["symptoms"]
        }

    def generate_risk_score(self, symptoms):
        if "chest pain" in symptoms.lower():
            return "Critical Priority - Risk Score 100/100"
        else:
            return "Normal Priority"

        
# Example usage
agent = ReceptionAgent()

patient_data = {
    "name": "Sample Patient",
    "age": 45,
    "symptoms": "chest pain"
}

print(agent.collect_patient_information(patient_data))
print(agent.generate_risk_score(patient_data["symptoms"]))

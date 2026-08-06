class MemoryAgent:
    def __init__(self):
        self.patient_memory = {}

    def store_patient_context(self, patient_id, data):
        self.patient_memory[patient_id] = data

    def get_patient_context(self, patient_id):
        return self.patient_memory.get(patient_id)


# Example usage
memory = MemoryAgent()

memory.store_patient_context(
    "P001",
    {
        "name": "Sample Patient",
        "history": "Previous consultation stored"
    }
)

print(memory.get_patient_context("P001"))

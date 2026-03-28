# Basic Disease Detection System

symptoms_db = {
    "cold":    ["sneezing", "runny nose", "sore throat"],
    "flu":     ["fever", "body ache", "fatigue", "headache"],
    "malaria": ["high fever", "chills", "sweating", "headache"],
    "dengue":  ["high fever", "rash", "joint pain", "nausea"],
}

print("=== Disease Detector ===")
symptom = input("Enter your main symptom: ").lower().strip()

found = False
for disease, symptoms in symptoms_db.items():
    if symptom in symptoms:
        print(f"You might have: {disease.upper()}")
        print("Please consult a doctor.")
        found = True
        break

if not found:
    print("No match found. Please see a doctor.")
```

**Sample run:**
```
=== Disease Detector ===
Enter your main symptom: fever
You might have: FLU
Please consult a doctor.
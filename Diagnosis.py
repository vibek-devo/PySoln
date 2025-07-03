#  Expert System Case Study 

def flu_diagnosis(symptoms):
    rules = [
        ({"fever", "cough", "body ache"}, "You may have flu."),
        ({"fever", "rash"}, "You may have measles."),
        ({"cough"}, "You might have a common cold.")
    ]
    

    for cond, diag in rules:
        if cond.issubset(symptoms):
            return diag
    
    return "No clear diagnosis."


def get_user_input():

    symptoms_input = input("Enter your symptoms separated by commas (e.g., fever, cough, body ache): ")
    

    symptoms = set(symptom.strip().lower() for symptom in symptoms_input.split(","))
    

    result = flu_diagnosis(symptoms)
    print(result)

get_user_input()

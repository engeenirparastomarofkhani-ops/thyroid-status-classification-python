list_diseases = []
for i in range(5):
    age = int(input("Please enter age: "))
    TSH = float(input("plz enter your TSH: "))
    FT4 = float(input("plz enter your FT4: "))
    FT3 = float(input("plz enter your FT3: "))
    dictionary_disease = {
        "age": age,
        "TSH": TSH,
        "FT4": FT4,
        "FT3": FT3
    }
    list_diseases.append(dictionary_disease)

def type_of_thyroid(list_diseases):
    result = []

    for D in list_diseases:
        if D["TSH"] < 0.4 and (D["FT4"] > 1.8 or D["FT3"] > 4.2):
            status = "hyperthyroid"

        elif 0.4 <= D["TSH"] <= 4.0 and 0.8 <= D["FT4"] <= 1.8 and 2.3 <= D["FT3"] <= 4.2:
            status = "normal"

        elif D["TSH"] > 4.0 and D["FT4"] < 0.8:
            status = "hypothyroid"

        else:
            status = "uncertain"

        result.append({
            "age": D["age"],
            "thyroid_status": status
        })

    return result

output = type_of_thyroid(list_diseases)

for o in output:
    print(f"Age: {o['age']} → {o['thyroid_status']}")

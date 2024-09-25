cs = [
    "Fever", "Cough", "Headache", "Fatigue", "Muscle pain", "Nausea", "Vomiting",
    "Diarrhea", "Abdominal pain", "Shortness of breath", "Chest pain", "Swollen lymph nodes",
    "Rash", "Joint pain", "Red eyes", "Sore throat", "Runny nose", "Loss of smell", "Loss of taste",
    "Swelling", "Weight loss", "Weight gain", "Chills", "Night sweats", "Change in appetite",
    "Increased urination", "Decreased urination", "Difficulty swallowing", "Dizziness",
    "Seizures", "Hallucinations", "Confusion", "Memory loss", "Weakness", "Tingling",
    "Numbness", "Speech difficulties","Nasal discharge","Congestion","Sneezing"
]
common_diseases = [
    "Influenza", "Common Cold", "Gastroenteritis", "Strep Throat", "Tonsillitis",
    "Sinusitis", "Bronchitis", "Pneumonia", "Urinary Tract Infection", "Migraine"
]
database={}
database["Influenza"]= [["Fever",14.8],["Cough",13.4],["Sore throat",7.1],["Body ache",13.4],["Muscle pain",13.4],["Runny nose",8.6],["Headache",11],["Chills",14.1],["Vomiting",2.4],["Diarrhea",3.5]]
database["Common Cold"]=[["Nasal discharge",14],["Congestion",12.8],["Sneezing",12],["Runny nose",11.3],["Cough",9.8],["Loss of taste",9.1],["Muscle pain",8.3],["Fatigue",8.3],["Headache",7.5],["Sore throat",6.8]]
l=[]
symp=input("Enter the symptom:")
l.append(symp)
while symp!="stop":
    symp=input("Enter the symptom:")
    l.append(symp)
l.pop()
k=[]
# l is list of symptoms
print(l)
dict12={}
for dis in common_diseases:
    dict12[dis]=0
#print(dict12)
for sp in l:
    for key,value in database.items():
        for s in value:
            if s[0]==sp:
                dict12[key]+=s[1]
max=-1
str=''
for key,value in dict12.items():
    if value>max:
        str=key
        max=value

print("The disease is:", str)

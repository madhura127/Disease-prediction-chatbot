from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd

root = Tk()
root.title('DR BOT')
root.config(background='darkslategrey')

def create():
    
    l1=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',
    'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue',
    'weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat',
    'irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion',
    'headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation',
    'abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload',
    'swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',
    'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps',
    'bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain',
    'muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side',
    'loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches',
    'watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances',
    'receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption',
    'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']

    disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
            'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
            ' Migraine','Cervical spondylosis',
            'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
    'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
    'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
    'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
    'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
    'Impetigo']

    l2=[]
    for x in range(0,len(l1)):
        l2.append(0)

    # TESTING DATA
    tr=pd.read_csv("Testing.csv")
    tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
    'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
    'Migraine':11,'Cervical spondylosis':12,
    'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
    'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
    'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
    'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
    '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
    'Impetigo':40}},inplace=True)

    X_test= tr[l1]
    y_test = tr[["prognosis"]]
    np.ravel(y_test)

    # TRAINING DATA
    df=pd.read_csv("Training.csv")

    df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
    'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
    'Migraine':11,'Cervical spondylosis':12,
    'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
    'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
    'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
    'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
    '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
    'Impetigo':40}},inplace=True)

    X= df[l1]

    y = df[["prognosis"]]
    np.ravel(y)

    def message():
        if (Symptom1.get() == "None" and  Symptom2.get() == "None" and Symptom3.get() == "None" and Symptom4.get() == "None" and Symptom5.get() == "None"):
            messagebox.showinfo("OOPS!!", "ENTER  SYMPTOMS PLEASE")
        else :
            NaiveBayes()

    def NaiveBayes():
        from sklearn.naive_bayes import MultinomialNB
        gnb = MultinomialNB()
        gnb=gnb.fit(X.values,np.ravel(y))
        from sklearn.metrics import accuracy_score
        y_pred = gnb.predict(X_test)
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred, normalize=False))

        psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

        for k in range(0,len(l1)):
            for z in psymptoms:
                if(z==l1[k]):
                    l2[k]=1

        inputtest = [l2]
        predict = gnb.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(disease)):
            if(disease[predicted] == disease[a]):
                h='yes'
                break
        if (h=='yes'):
            
            text.insert(END, "\n" +"Bot: You may have " +disease[a])
            text.insert(END, "\n" +"Bot: Follow this site for more information 'https://www.medicalnewstoday.com/articles/156859#treatment'")
            new_root.destroy()
            
        else:
            
            text.insert(END, "\n" + "Bot: No matches found!!")
            new_root.destroy()

    new_root = Tk()
    new_root.title("Disease Prediction From Symptoms")
    new_root.geometry("800x400")
    new_root.configure(background='darkslategrey')

    Symptom1 = StringVar()
    Symptom1.set(None)
    Symptom2 = StringVar()
    Symptom2.set(None)
    Symptom3 = StringVar()
    Symptom3.set(None)
    Symptom4 = StringVar()
    Symptom4.set(None)
    Symptom5 = StringVar()
    Symptom5.set(None)

    w2 = Label(new_root, justify=LEFT, text="Disease Prediction From Symptoms ")
    w2.config(font=("Arial", 30),background="darkslategrey",foreground="black")
    w2.grid(row=1, column=0, columnspan=2, padx=30,pady=20)

    S1Lb = Label(new_root,  text="Symptom 1")
    S1Lb.config(font=("Arial", 15),background="darkslategrey",foreground="black")
    S1Lb.grid(row=7, column=0,padx=10, pady=5 )

    S2Lb = Label(new_root,  text="Symptom 2")
    S2Lb.config(font=("Arial", 15),background="darkslategrey",foreground="black")
    S2Lb.grid(row=8, column=0,padx=10, pady=5)

    S3Lb = Label(new_root,  text="Symptom 3")
    S3Lb.config(font=("Arial", 15),background="darkslategrey",foreground="black")
    S3Lb.grid(row=9, column=0,padx=10, pady=5)

    S4Lb = Label(new_root,  text="Symptom 4")
    S4Lb.config(font=("Arial", 15),background="darkslategrey",foreground="black")
    S4Lb.grid(row=10, column=0,padx=10, pady=5)

    S5Lb = Label(new_root,  text="Symptom 5")
    S5Lb.config(font=("Arial", 15),background="darkslategrey",foreground="black")
    S5Lb.grid(row=11, column=0,padx=10, pady=5)

    lr = Button(new_root, text="Predict",fg='white',bg='black',height=2, width=30, command=message)
    lr.config(font=("Arial", 15))
    lr.grid(row=15, column=1,pady=20)

    OPTIONS = sorted(l1)

    S1En = OptionMenu(new_root, Symptom1,*OPTIONS)
    S1En.grid(row=7, column=2)

    S2En = OptionMenu(new_root, Symptom2,*OPTIONS)
    S2En.grid(row=8, column=2)

    S3En = OptionMenu(new_root, Symptom3,*OPTIONS)
    S3En.grid(row=9, column=2)

    S4En = OptionMenu(new_root, Symptom4,*OPTIONS)
    S4En.grid(row=10, column=2)

    S5En = OptionMenu(new_root, Symptom5,*OPTIONS)
    S5En.grid(row=11, column=2)

    new_root.mainloop()
    
detect = StringVar()

def send():
    send = "You:"+ e.get()
    text.insert(END,"\n" + send)
    
    if(e.get()=='hi'):
        text.insert(END, "\n" + "Bot: hello! How can I help you?\nBot: Enter checkup for diagnosis")
    elif(e.get()=='how are you?'):
        text.insert(END, "\n" + "Bot: i'm fine.What about you?")
    elif (e.get() == "im fine"):
        text.insert(END, "\n" + "Bot: How can I help you?\nBot: Enter checkup for diagnosis")
    elif (e.get() == "i'm fine too"):
        text.insert(END, "\n" + "Bot: nice to hear that\nBot: Enter checkup for diagnosis")
    elif(e.get() == "checkup"):
        create()
    else:
        text.insert(END, "\n" + "Bot: Sorry I didnt get it.\nBot: Enter checkup for checkup")
    
text = Text(root,bg='black',fg='white')
text.grid(row=0,column=0,columnspan=2)
e = Entry(root,width=80,font=('Arial 12'),bg='black',fg='white')
send = Button(root,text='Send',fg='white',bg='black',width=20,height=2,command=send).grid(row=1,column=1)
#create = Button(root,text='check_up',bg='blue',width=20,command=create).grid(row=1,column=2)
e.grid(row=1,column=0)

root.mainloop()
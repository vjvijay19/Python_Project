def find_a_doctor(db):
    print("\t\t\tAVAILABLE DOCTORS")

    col = db["doctors"]
    for j,i in enumerate (col.find()):
        print(str(j+1) + '.',i['doctor_name'],i['specification'])
    
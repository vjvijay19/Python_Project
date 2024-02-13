def cancel_appointment(db):
    col = db["doctors"]
    dlist = list(col.find())
    
    un =  int(input("Please provide the mobile number under which your booking has been made:"))
    col1 = db["appointment"]
    apppointment = col1.find_one({"mob_no":un})
    
    if apppointment["mob_no"] == un:
        op = input("Are you sure, would you like to cancel booking? yes/no: ")
        print()
        if op == "yes":
           print(f"Hello! {apppointment["name"]} your appointment has been cancelled with {dlist[apppointment["doctor_id"]]["doctor_name"]} {dlist[apppointment["doctor_id"]]["specification"]} on {apppointment["date"]}.")
           col1.delete_one({"mob_no":un})
           input()
        else:
            print(f"Hello! {apppointment["name"]} your appointment is not cancelled.")
            input()
        
    else:
        print("No booking found with this number...Enter a valid number")
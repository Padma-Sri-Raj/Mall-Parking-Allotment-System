Vehicle_Number=[]
Vehicle_Type=[]
Date=[]
Time=[]

def allotment(car):
    while True:
        check = 0
        for i in vacant:
            if i == 0:
                a = vacant.index(i)
                print(car, "go to", parking[a])
                vacant[a] = 1
                check = 1
                break
        if check == 0:
            print("parking full bro")
            break
bikes=100
cars=250
bicycles=78
def main(ch,Vno):
    global bikes,cars,bicycles
    if ch==1:
        Vno=Vno.upper()
        Vehicle_Number.append(Vno)
                    date = input("\tEnter Date (DD-MM-YYYY) - ")
                    if date == "":
                        print("###### Enter Date ######")
                    elif len(date) != 10:
                        print("###### Enter Valid Date ######")
                    else:
                        Date.append(date)
                        d = not True
                t = True
                while t == True:
                    time = input("\tEnter Time (HH:MM:SS) - ")
                    if t == "":
                        print("###### Enter Time ######")
                    elif len(time) != 8:
                        print("###### Please Enter Valid Date ######")
                    else:
                        Time.append(time)
                        t = not True

    elif ch == 2:
        no = True
        while no == True:
            Vno = input("\tEnter vehicle number to Delete(XXXX-XX-XXXX) - ").upper()
            if Vno == "":
                print("###### Enter Vehicle No. ######")
            elif len(Vno) == 10:
                if Vno in Vehicle_Number:
                    i = Vehicle_Number.index(Vno)
                    Vehicle_Number.pop(i)
                    Vehicle_Type.pop(i)
                    Date.pop(i)
                    Time.pop(i)
                    no = not True
                    print("\n............................................................Removed Sucessfully..................................................................")

                elif Vno not in Vehicle_Number:
                    print("###### No Such Entry ######")
                else:
                    print("Error")
            else:
                print("###### Enter Valid Vehicle Number ######")
    elif ch == 3:
        count = 0
        print(
            "----------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t\tParked Vehicle")
        print(
            "----------------------------------------------------------------------------------------------------------------------")
        print("Vehicle No.\tVehicle Type             Date\t\tTime")
        print(
            "----------------------------------------------------------------------------------------------------------------------")
        for i in range(len(Vehicle_Number)):
            count += 1
            print(Vehicle_Number[i], "\t  ", Vehicle_Type[i],
                  "             ", Date[i], "\t\t", Time[i])
        print(
            "----------------------------------------------------------------------------------------------------------------------")
        print("------------------------------------------ Total Records - ",count,"-------------------------------------------------------")
        print("----------------------------------------------------------------------------------------------------------------------")
    elif ch==4:
        print("----------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t\tSpaces Left For Parking")
        print("----------------------------------------------------------------------------------------------------------------------")
        print("\tSpaces Available for Bicycle - ",bicycles)
        print("\tSpaces Available for Bike - ",bikes)
        print("\tSpaces Available for Car - ",cars)
        print("----------------------------------------------------------------------------------------------------------------------")
    elif ch==5:
        print("----------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t\tParking Rate")
        print("----------------------------------------------------------------------------------------------------------------------")
        print("*1.Bicycle      Rs20 / Hour")
        print("*2.Bike         Rs40/ Hour")
        print("*3.Car          Rs60/ Hour")
        print("----------------------------------------------------------------------------------------------------------------------")
    elif ch==6:
        print(".............................................................. Generating Bill ..........................................................................")
        no=True
        while no==True:
            Vno=input("\tEnter vehicle number to Delete(XXXX-XX-XXXX) - ").upper()
            if Vno=="":
                print("###### Enter Vehicle No. ######")
            elif len(Vno)==10:
                if Vno in Vehicle_Number:
                    i=Vehicle_Number.index(Vno)
                    no=not True
                elif Vno not in Vehicle_Number:
                    print("###### No Such Entry ######")
                else:
                    print("Error")
            else:
                print("###### Enter Valid Vehicle Number ######")
        print("\tVehicle Check in time - ",Time[i])
        print("\tVehicle Check in Date - ",Date[i])
        print("\tVehicle Type - ",Vehicle_Type[i])
        inp=True
        amt=0
        while inp==True:
            hr=input("\tEnter No. of Hours Vehicle Parked - ").lower()
            if hr=="":
                print("###### Please Enter Hours ######")
            elif int(hr)==0 and Vehicle_Type[i]=="Bicycle":
                amt=20
                inp=not True
            elif int(hr)==0 and Vehicle_Type[i]=="Bike":
                amt=40
                inp=not True
            elif int(hr)==0 and Vehicle_Type[i]=="Car":
                amt=60
                inp=not True
            elif int(hr)>=1:
                if Vehicle_Type[i]=="Bicycle":
                    amt=int(hr)*int(20)
                    inp=not True
                elif Vehicle_Type[i]=="Bike":
                    amt=int(hr)*int(40)
                    inp=not True
                elif Vehicle_Type[i]=="Car":
                    amt=int(hr)*int(60)
                    inp=not True
        print("\t Parking Charge - ",amt)
        ac=18/100*int(amt)
        print("\tAdd. charge 18 % - ",ac)
        print("\tTotal Charge - ",int(amt)+int(ac))
        print("..............................................................Thank you for using our service...........................................................................")
        a=input("\tPress Any Key to Proceed - ")
    elif ch==7:
        print("..............................................................Thank you for using our service...........................................................................")
        print("                                     **********(: Bye Bye :)**********")
        break
        quit
    except:
        main()
main()





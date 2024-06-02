import mysql.connector as sqltor
mycon= sqltor.connect(host="localhost",user="root",passwd="maansi",database="airways")
if mycon.is_connected():
      print("Connected")
   
import random    
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mg
#from PIL import ImageTk, Image
window= tk.Tk()
window.title("Airways")

window.geometry("1350x650+0+0")
window.resizable(0,0)
window.config(bg="skyblue")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Creating frame<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
Frame= tk.Frame(window, width= 1000, height= 50, bd= 10, relief= "raise" )
Frame.place(relx= 0.15 ,rely= 0.2, relwidth= 0.7, relheight = 0.4)

# >>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Creating lable <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
Intro= tk.Label(Frame, text="Welcome to Airline", fg= "red",font="Verdana 25 bold italic ")
Intro.place(relx=0.3,rely=0)

def Booking():
    Booking_frame= tk.Frame(window,bg="skyblue")
    Booking_frame.place(relwidth=1, relheight=1)
    
    Root= tk.Frame(Booking_frame, width= 1000, height= 50, bd= 10, relief= "raise" )
    Root.place(relx= 0.15 ,rely= 0.1, relwidth= 0.7, relheight = 0.4)
    From_lable= tk.Label(Root, text="       From",font="Verdana 25 bold italic ")
    From_lable.place(relx=0,rely=0) 
    
    To_lable= tk.Label(Root, text="   To",font="Verdana 25 bold italic ")
    To_lable.grid(row= 300, column= 50)
    
    From= tk.StringVar()
    From_entry= tk.Entry(Root, width= 25, textvariable= From)
    From_entry.grid(row= 300, column= 45)
    
    To= tk.StringVar()
    To_entry= tk.Entry(Root, width= 25, textvariable= To)
    To_entry.grid(row= 300, column= 55)
    
    Departure_date= tk.Label(Root, text="   Departure Date",font="Verdana 25 bold italic ")
    Departure_date.grid(row= 301, column= 30)
    
    
    Date= tk.StringVar()
    Date_entry= tk.Entry(Root, width= 25, textvariable= Date)
    Date_entry.grid(row= 301, column= 45)
    
    Flight_label= tk.Label(Root, text="   Flight name",font="Verdana 25 bold italic ")
    Flight_label.grid(row= 301, column= 50)
    
    Flight= tk.StringVar()
    Flight_entry= tk.Entry(Root, width= 25, textvariable= Flight)
    Flight_entry.grid(row= 301, column= 55)
    
    Passenger_label= tk.Label(Root, text="No. of Passengers",font="Verdana 25 bold italic ")
    Passenger_label.grid(row= 302, column= 30)
    
    Passenger= tk.IntVar()
    Passenger_entry= tk.Entry(Root, width= 25, textvariable= Passenger)
    Passenger_entry.grid(row= 302, column= 45)
    
    Trip_label= tk.Label(Root, text="Trip",font="Verdana 25 bold italic ")
    Trip_label.grid(row= 302, column= 50)
    
    Trip= tk.StringVar()
    Trip_Combobox= ttk.Combobox(Root, width=25,text= Trip, state= "readonly")
    Trip_Combobox["values"]= ('One trip', 'Round Trip','Multi-city')
    Trip_Combobox.grid(row=302, column= 55)
    
    Root2= tk.Frame(Booking_frame, width= 1000, height= 50, bd= 10, relief= "raise" )
    Root2.place(relx= 0.15 ,rely= 0.5, relwidth= 0.7, relheight = 0.4) 
    
    def Search():
        From_data = From.get()
        To_data= To.get()
        date_data = Date.get()
        seats= Passenger.get()
        
        
        yt="'" +To_data + "'"
        yf= "'" +From_data+ "'"
        yd ="'" +date_data+ "'" 
        st1=  "select flight_name , Available_seats, Departure_time,Price from Plane where From_dep = " + yf + "And Top_dep = " + yt + "and departure_date = "+ yd + "And Available_seats > "+ str(seats) 
    
        Dep1_lable= tk.Label(Root2, text= "Flight Name ",font="Verdana 15 bold italic ")
        Dep1_lable.grid(row= 300, column= 30)
        
        avaseat_lable= tk.Label(Root2, text= "       Available Seats ",font="Verdana 15 bold italic ")
        avaseat_lable.grid(row= 300, column= 50) 
        
        time_lable= tk.Label(Root2, text= "       Departure Time ",font="Verdana 15 bold italic ")
        time_lable.grid(row= 300, column= 70)
        
        cursor= mycon.cursor()
        

        cursor.execute(st1)
        data= cursor.fetchall()
        
        row_dep=310
        row_seat= 310
        row_time = 310
        Flit = []
        dic={}
        if data ==[]:
            mg.showinfo("Sorry","No Flight is available !!!!!!! \n hooooaaaaa")
            
        else:     
            for i in data:
                fli = i[0]
                seatA= i[1]
                time_dep = i[2] 
                Flit.append(fli+"    "+str(time_dep))
                dic[fli]=i[3]
                    
                Dep_Ans= tk.Label(Root2, text= fli,font="Verdana 15 bold italic ")
                Dep_Ans.grid(row= row_dep, column= 30)
                row_dep= row_dep + 10
                 
                Seat_Ans= tk.Label(Root2, text= seatA,font="Verdana 15 bold italic ")
                Seat_Ans.grid(row= row_seat, column= 50)
                row_seat = row_seat+10
             
                time_Ans= tk.Label(Root2, text= time_dep,font="Verdana 15 bold italic ")
                time_Ans.grid(row= row_time, column= 70)
                row_time = row_time+10
                    
                def Book():
                    Book_frame= tk.Frame(window)
                    Book_frame.place(relwidth=1, relheight=1)
                            
                    Frame_book= tk.Frame(Book_frame, width= 1000, height= 1000, bd= 10, relief= "raise" )
                    Frame_book.place(relx= 0.1 ,rely= 0.1, relwidth= 0.7, relheight = 0.7)
                                
                    name_lable= tk.Label(Frame_book, text="Enter your name: ",font="Verdana 25 bold italic ")
                    name_lable.grid(row= 300, column= 30)     
                                
                    Name= tk.StringVar()
                    name_ans= tk.Entry(Frame_book, width= 25, textvariable= Name)
                    name_ans.grid(row= 300, column= 45)
                        
                    age_lable= tk.Label(Frame_book, text="Enter your Age: ",font="Verdana 25 bold italic ")
                    age_lable.grid(row= 310, column= 30)
                        
                    Age= tk.StringVar()
                    age_entry= tk.Entry(Frame_book, width= 25, textvariable= Age)
                    age_entry.grid(row= 310, column= 45)
                                
                    gender_lable= tk.Label(Frame_book, text="Enter your Gender: ",font="Verdana 25 bold italic ")
                    gender_lable.grid(row= 320, column= 30)
                                
                    Gender= tk.StringVar()
                    gender_Combobox= ttk.Combobox(Frame_book, width=25,text= Gender, state= "readonly")
                    gender_Combobox["values"]= ('Female', 'Male','Transgender')
                    gender_Combobox.grid(row=320, column=45)
                                
                    Fli_lable= tk.Label(Frame_book, text="Choose your fight : ",font="Verdana 25 bold italic ")
                    Fli_lable.grid(row= 330, column= 30)
                                
                    Plane= tk.StringVar()
                    plane_Combobox= ttk.Combobox(Frame_book, width=25,text= Plane, state= "readonly")
                    plane_Combobox["values"]= Flit
                    plane_Combobox.grid(row=330, column=45)
                    
                    allinfo= []
                    
                    
                    
                    def Submit():
                        
                        
                        name_data= Name.get()
                        age_data= Age.get()
                        gender_data= Gender.get()
                        fli_data= Plane.get()
                        trip= Trip.get()
                        
                                
                        x= ("A","B","C","D","E","F")
                        f= random.randint(0,5)
                        t= random.randint(1,30)
                        y= x[f] + str(t)
                                    
                        word= fli_data.split()
                        fli= word[0]
                        time = word[1]
                        Price= dic.get(fli)
                                
                        st1= "insert into passenger (Passenger_name, Gender, Age,Flight_name, Seat_Number, Departure_dest,  Destination, Date_Departure, Time_Departure, Trip, Price) value ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name_data ,gender_data ,age_data, fli, y, From_data ,To_data,date_data, time, trip, Price )
                                
                                    
                        cursor.execute(st1)
                        mycon.commit()
                        
                        info= [name_data ,gender_data ,age_data, fli, y, From_data ,To_data,date_data, time, trip, Price]
                        allinfo.append(info)
                                
                        yfl= "'"+fli+"'"
                                
                        st2= "Update plane set Available_seats= Available_seats-1 where Flight_name=" + yfl+ "and Departure_date= "+ yd
                        cursor.execute(st2)
                        mycon.commit()
                        if y[0]== "A" or y[0] =="F":
                            st3 ="Update plane set Window_seats= Window_seats-1 where Flight_name=" + yfl+ "and Departure_date= "+ yd        
                            cursor.execute(st3)
                            mycon.commit()
                            
                    def show():
                        mg.showinfo("Add one more","You can add  more /n by clearing the text box and re=entering other ") 
                        Submit()
                        
                    next_btn=tk.Button(Frame_book,text= "Add one more",font="Verdana 25 bold italic ",command= show)
                    next_btn.grid(row= 350, column = 100)    
                        
                    def Submit2():
                        
                        Submit()
                            
                        
                        Dis_frame= tk.Frame(window)
                        Dis_frame.place(relwidth=1, relheight=1)
                            
                        Frame_Dis= tk.Frame(Dis_frame, width= 5000, height= 500, bd= 10, relief= "raise" )
                        Frame_Dis.place(relx= 0 ,rely= 0.1, relwidth= 1, relheight = 0.4)
                        
                        Frame2dis= tk.Frame(Dis_frame, width= 300, height= 200, bd=10, relief= "raise")
                        Frame2dis.place(relx=0.7, rely=0.5, relwidth=0.4 , relheight= 0.2)
                        
                        Passen_lable= tk.Label(Frame_Dis, text="Passenger ", fg= "blue",font="Verdana 15 italic ")
                        Passen_lable.grid(row= 300, column= 30)
                        
                        age_lable= tk.Label(Frame_Dis, text="        Age ",fg= "blue",font="Verdana 15  italic ")
                        age_lable.grid(row= 300, column= 40)
                        
                        gen_lable= tk.Label(Frame_Dis, text="        Gender ",fg= "blue",font="Verdana 15  italic ")
                        gen_lable.grid(row= 300, column= 50)
                        
                        flit_lable= tk.Label(Frame_Dis, text="        Flight ",fg= "blue",font="Verdana 15  italic ")
                        flit_lable.grid(row= 300, column= 60)
                        
                        seat_lable= tk.Label(Frame_Dis, text="        Seat No.",fg= "blue",font="Verdana 15 italic ")
                        seat_lable.grid(row= 300, column= 70)
                        
                        From_lable= tk.Label(Frame_Dis, text="        From ",fg= "blue",font="Verdana 15  italic ")
                        From_lable.grid(row= 300, column= 80)
                        
                        to_lable= tk.Label(Frame_Dis, text="        To ",fg= "blue",font="Verdana 15 italic ")
                        to_lable.grid(row= 300, column= 90)
                        
                        date_lable= tk.Label(Frame_Dis, text="        Date ",fg= "blue",font="Verdana 15 italic ")
                        date_lable.grid(row= 300, column= 100)
                        
                        tim_lable= tk.Label(Frame_Dis, text="        Time ",fg= "blue",font="Verdana 15 italic ")
                        tim_lable.grid(row= 300, column= 110)
                        
                        trip_lable= tk.Label(Frame_Dis, text="        Trip ",fg= "blue",font="Verdana 15 italic ")
                        trip_lable.grid(row= 300, column= 120)
                        
                        pay_lable= tk.Label(Frame_Dis, text="        Pay",fg= "blue",font="Verdana 15  italic ")
                        pay_lable.grid(row= 300, column= 130)
                    
                        rowd= 310    
                        payment= 0
                        for j in allinfo:
                            passename = j[0]
                            gen= j[1]
                            age= j[2]
                            flit= j[3]
                            bearth= j[4]
                            tod= j[5]
                            fromd= j[6]
                            dated= j[7]
                            timed= j[8]
                            tripd= j[9]
                            payd= j[10]
                            
                            Passen_ans= tk.Label(Frame_Dis, text= passename,font="Verdana 12 italic ")
                            Passen_ans.grid(row= rowd, column= 30)
                        
                            age_ans= tk.Label(Frame_Dis, text=age,font="Verdana 12  italic ")
                            age_ans.grid(row= rowd, column= 40)
                        
                            gen_ans= tk.Label(Frame_Dis, text=gen,font="Verdana 12  italic ")
                            gen_ans.grid(row= rowd, column= 50)
                        
                            flit_ans= tk.Label(Frame_Dis, text=flit,font="Verdana 12  italic ")
                            flit_ans.grid(row= rowd, column= 60)
                        
                            seat_ans= tk.Label(Frame_Dis, text=bearth,font="Verdana 12 italic ")
                            seat_ans.grid(row= rowd, column= 70)
                        
                            From_ans= tk.Label(Frame_Dis, text= fromd,font="Verdana 12  italic ")
                            From_ans.grid(row= rowd, column= 80)
                        
                            to_ans= tk.Label(Frame_Dis, text=tod,font="Verdana 12 italic ")
                            to_ans.grid(row= rowd, column= 90)
                        
                            date_ans= tk.Label(Frame_Dis, text=dated,font="Verdana 12 italic ")
                            date_ans.grid(row= rowd, column= 100)
                        
                            tim_ans= tk.Label(Frame_Dis, text=timed,font="Verdana 12 italic ")
                            tim_ans.grid(row= rowd, column= 110)
                        
                            trip_ans= tk.Label(Frame_Dis, text=tripd,font="Verdana 12 italic ")
                            trip_ans.grid(row= rowd, column= 120)
                        
                            pay_ans= tk.Label(Frame_Dis, text=payd,font="Verdana 12  italic ")
                            pay_ans.grid(row= rowd, column= 130)
                            
                            rowd= rowd + 10
                            payment= payment+int(payd)
                           
                        payd_lable= tk.Label(Frame2dis, text="You have to pay: ",font="Verdana 12 bold italic ")
                        payd_lable.grid(row= 10, columnspan= 10)
                        
                        payd_ans= tk.Label(Frame2dis, text=payment,font="Verdana 12 bold italic ")
                        payd_ans.grid(row=10, column= 20)
                        
                        
                        
                        
                    Book_btn=tk.Button(Frame_book,text= "Book",font="Verdana 25 bold italic ",command= Submit2)
                    Book_btn.grid(row= 370, column = 100)    
                        
                        
                    
                    
                            
                        
                            
                    
                Book_btn=tk.Button(Root2,text= "Book",font="Verdana 25 bold italic ",command= Book)
                Book_btn.grid(row= 370, column = 100)
                     
                   
        
        
    
    Search_btn=tk.Button(Root, text= "Search", font="Verdana 25 bold italic ",command = Search)
    Search_btn.grid(row= 303, columnspan = 57)

# >>>>>>> Creating button<<<<<<<<#
Booking_btn=tk.Button(Frame, text= "Booking", font="Verdana 25 bold italic ",command= Booking)
Booking_btn.place(relx=0.05,rely=0.3)

def Available():
    Available_frame= tk.Frame(window,bg="skyblue")
    Available_frame.place(relwidth=1, relheight=1)
    
    Root4= tk.Frame(Available_frame, width= 1000, height= 50, bd= 10, relief= "raise" )
    Root4.place(relx= 0.15 ,rely= 0.1, relwidth= 0.7, relheight = 0.4)
    
    From2_lable= tk.Label(Root4, text="       From",font="Verdana 25 bold italic ")
    From2_lable.grid(row= 300, column= 30) 
    
    To2_lable= tk.Label(Root4, text="   To",font="Verdana 25 bold italic ")
    To2_lable.grid(row= 300, column= 50)
    
    From2= tk.StringVar()
    From2_entry= tk.Entry(Root4, width= 25, textvariable= From2)
    From2_entry.grid(row= 300, column= 45)
    
    To2= tk.StringVar()
    To2_entry= tk.Entry(Root4, width= 25, textvariable= To2)
    To2_entry.grid(row= 300, column= 55)
    
    Departure2_date= tk.Label(Root4, text="   Departure Date",font="Verdana 25 bold italic ")
    Departure2_date.grid(row= 301, column= 30)
    
    Date2= tk.StringVar()
    Date2_entry= tk.Entry(Root4, width= 25, textvariable= Date2)
    Date2_entry.grid(row= 301, column= 45)
    
    Flight2_label= tk.Label(Root4, text="   Flight name",font="Verdana 25 bold italic ")
    Flight2_label.grid(row= 301, column= 50)
    
    Flight2= tk.StringVar()
    Flight2_entry= tk.Entry(Root4, width= 25, textvariable= Flight2)
    Flight2_entry.grid(row= 301, column= 55)
    
    Passenger2_label= tk.Label(Root4, text="No. of Passengers",font="Verdana 25 bold italic ")
    Passenger2_label.grid(row= 302, column= 30)
    
    Passenger2= tk.IntVar()
    Passenger2_entry= tk.Entry(Root4, width= 25, textvariable= Passenger2)
    Passenger2_entry.grid(row= 302, column= 45)
    
    Root5= tk.Frame(Available_frame, width= 1000, height= 50, bd= 10, relief= "raise" )
    Root5.place(relx= 0.15 ,rely= 0.5, relwidth= 0.7, relheight = 0.4) 
    
    def Ava_Search():
        From2_data = From2.get()
        To2_data= To2.get()
        date2_data = Date2.get()
        seats2= Passenger2.get()
        
        
        yt2="'" +To2_data + "'"
        yf2= "'" +From2_data+ "'"
        yd2 ="'" +date2_data+ "'" 
        st7=  "select flight_name , Available_seats, Departure_time,Price from Plane where From_dep = " + yf2 + "And Top_dep = " + yt2 + "and departure_date = "+ yd2 + "And Available_seats > "+ str(seats2) 
    
        Dep12_lable= tk.Label(Root5, text= "Flight Name ",font="Verdana 15 bold italic ")
        Dep12_lable.grid(row= 300, column= 30)
        
        avaseat2_lable= tk.Label(Root5, text= "       Available Seats ",font="Verdana 15 bold italic ")
        avaseat2_lable.grid(row= 300, column= 50) 
        
        time2_lable= tk.Label(Root5, text= "       Departure Time ",font="Verdana 15 bold italic ")
        time2_lable.grid(row= 300, column= 70)
        
        cursor= mycon.cursor()
        

        cursor.execute(st7)
        data2= cursor.fetchall()
        
        row2_dep=310
        row2_seat= 310
        row2_time = 310
        
        if data2 ==[]:
            mg.showinfo("Sorry","No Flight is available !!!!!!!")
            
        else:     
            for j in data2:
                fli = j[0]
                seatA= j[1]
                time_dep = j[2] 
                
                    
                Dep2_Ans= tk.Label(Root5, text= fli,font="Verdana 15 bold italic ")
                Dep2_Ans.grid(row= row2_dep, column= 30)
                row2_dep= row2_dep + 10
                 
                Seat2_Ans= tk.Label(Root5, text= seatA,font="Verdana 15 bold italic ")
                Seat2_Ans.grid(row= row2_seat, column= 50)
                row2_seat = row2_seat+10
             
                time2_Ans= tk.Label(Root5, text= time_dep,font="Verdana 15 bold italic ")
                time2_Ans.grid(row= row2_time, column= 70)
                row2_time = row2_time+10

    Available2_seat= tk.Button(Root4, text= "Search", font="Verdana 25 bold italic ", command= Ava_Search )
    Available2_seat.place(relx=0.7,rely=0.6)
    
Available_seat= tk.Button(Frame, text= "Availability", font="Verdana 25 bold italic ", command= Available)
Available_seat.place(relx=0.3,rely=0.3)

def cancel():
    cancel_frame= tk.Frame(window)
    cancel_frame.place(relwidth=1, relheight=1)
    
    Root3= tk.Frame(cancel_frame, width= 1000, height= 50, bd= 10, relief= "raise" )
    Root3.place(relx= 0.1 ,rely= 0.1, relwidth= 0.7, relheight = 0.4)
    
    From_lable= tk.Label(Root3, text=" From",font="Verdana 25 bold italic ")
    From_lable.grid(row= 300, column= 30) 
    
    To_lable= tk.Label(Root3, text="   To",font="Verdana 25 bold italic ")
    To_lable.grid(row= 300, column= 50)
    
    From= tk.StringVar()
    From_entry= tk.Entry(Root3, width= 25, textvariable= From)
    From_entry.grid(row= 300, column= 45)
    
    To= tk.StringVar()
    To_entry= tk.Entry(Root3, width= 25, textvariable= To)
    To_entry.grid(row= 300, column= 55)
    
    Departure_date= tk.Label(Root3, text=" Date",font="Verdana 25 bold italic ")
    Departure_date.grid(row= 301, column= 30)
    
    
    Date= tk.StringVar()
    Date_entry= tk.Entry(Root3, width= 25, textvariable= Date)
    Date_entry.grid(row= 301, column= 45)
    
    passen_name= tk.Label(Root3, text="Passenger Name: ",font="Verdana 25 bold italic ")
    passen_name.grid(row= 302, column= 50)
    
    passen= tk.StringVar()
    passen_entry= tk.Entry(Root3, width= 25, textvariable= passen)
    passen_entry.grid(row= 302, column= 55)
    
    Flight_label= tk.Label(Root3, text="   Flight name",font="Verdana 25 bold italic ")
    Flight_label.grid(row= 301, column= 50)
    
    Flight= tk.StringVar()
    Flight_entry= tk.Entry(Root3, width= 25, textvariable= Flight)
    Flight_entry.grid(row= 301, column= 55)
    
    seatno_label= tk.Label(Root3, text="Seat",font="Verdana 25 bold italic ")
    seatno_label.grid(row= 302, column= 30)
    
    seatno= tk.StringVar()
    seatno_entry= tk.Entry(Root3, width= 25, textvariable= seatno)
    seatno_entry.grid(row= 302, column= 45)
    
    def cancel2():
        to1="'"+ To.get()+"'"
        from1="'"+ From.get()+"'"
        depdate= "'"+Date.get()+"'"
        flit="'" +Flight.get()+"'"
        seat= "'"+seatno.get()+"'"
        passen_name= "'"+passen.get()+ "'"
        
        st4= "Select Passenger_name, Flight_name from passenger where Passenger_name=" + passen_name+ "and Destination= "+ to1+ "and Departure_dest="+ from1+ "and Flight_name= "+ flit+ "and Date_Departure= "+ depdate+ "and Seat_Number= "+ seat
        cursor= mycon.cursor()
        cursor.execute(st4)
        data1= cursor.fetchall()
        print(data1)
        
        if data1 ==[]:
            mg.showinfo("Sorry","Data didn't match")
        else: 
            st5= "Delete from passenger where Passenger_name=" + passen_name+ "and Destination= "+ to1+ "and Departure_dest="+ from1+ "and Flight_name= "+ flit+ "and Date_Departure= "+ depdate+ "and Seat_Number= "+ seat
    
            cursor.execute(st5)
            mycon.commit()  
            
            
            st6= "Update plane set Available_seats= Available_seats+ 1 where  Top_Dep = "+ to1+ "and From_Dep="+ from1+ "and Flight_name= "+ flit+ "and Departure_date = "+ depdate
            
            cursor.execute(st6)
            mycon.commit()  
            mg.showinfo("Done","Booking Cancled")    
            
    Cancel1_button= tk.Button(Root3,text= "Cancel Booking", font="Verdana 20 italic ",command= cancel2)
    Cancel1_button.place(relx=0.7,rely=0.5)
    
Cancel_booking= tk.Button(Frame, text= "Cancel Booking", font="Verdana 25 bold italic ", command= cancel)
Cancel_booking.place(relx=0.6, rely=0.3)


window.mainloop()
#########################################################################################################################
# OVERVIEW: Program for booking Asutralia places using Object Oriented Program.
# First, it contains four classes for different Errors. 
# Second, It contains nine classes.
# Third, all the attributes in the class are private.
# This program has 12 options which are:
# 1: Book a new trip
# 2. Display the current customer list
# 3. Display the current destinations list
# 4. Display the current service list
# 5. Adjust the discount rate limit
# 6. Adjust the threshold limit
# 7. Display all the bookings
# 8. Add new destination
# 9. Display all the bookings of a customer
# 10. Display the most valuable customer
# 11. Display the most popular destination
# 12. Exit the program

# In order to optimize the code it was defined several methods inside of the classes which will be explained next.

#########################################################################################################################


import sys
import datetime

# Defined Classes.

# Class "DestinationError" help to raise a error when the destination is not valid. 
# Class "TicketError" help to raise a error when the number of ticket is not valid. 
# Class "MembershipError" help to raise a error when the user didn't select a correct option with "M" or "V" refering with member and vip MEMBER respectively.
# Calss "OperationError" help to raise a error when the user didn't select a correct to select extra service ot not with "Y" OR "N" respectively.
# Class "RateModiError" help to raise a error when the user didn't eneter a valid rate.
# Class "ThresholdError" help to raise a error when the user didn't eneter a valid threshold.


class DestinationError(Exception):
    pass
class TicketError(Exception):
    pass
class MembershipError(Exception):
    pass

class OperationError(Exception):
    pass

class RateModiError(Exception):
    pass
class ThresholdError(Exception):
    pass

# "Class Service" is to keep track of informations of different extra services.
# It has a method called "set_price" which allow to update its price.

class Services():
    __ID=""
    __name=""
    __price=0
    def __init__(self,ID,name,price):
        self.__ID=ID
        self.__name=name
        self.__price=price
    
    def get_ID(self):
        return self.__ID
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price

    def set_price(self,price):
        self.__price=price
    


# "Class Bundle"  is a special kind of service and offers multiple services as one service.
# It can identify with the letter "B" in its "ID".
# It contains the attributes : "ID",name and a list_IDs which it refered the list of prices which in the format
# of the "ID" services. (see the class above)
# "get_price" method contains the calculations to get the final price of each bundle.

class Bundle():
    __ID=""
    __name=""
    __list_IDs=[]

    def __init__(self,ID,name,list_IDs):
        self.__ID=ID
        self.__name=name
        
        self.__list_IDs=list_IDs

    def get_ID(self):
        return self.__ID

    def get_name(self):
        return self.__name

    def get_list_IDs(self):
        return self.__list_IDs

    def get_price(self):
        sum=0
        for i in range(len(self.get_list_IDs())):
            sum=sum+self.get_list_IDs()[i].get_price()
        return sum *0.8

# Class "Customer" is the template for a normal customer and doesn't have discount. All its attributes as private.
# It has one constructor and 9 methods.
# "set_name" method has the condition that the customer must be a string. 
# "set_ID" and "set_value" methods allow to update the previuos value. 
# All "getters" methods allow to get the values of each attribute. 
# Finally, "displayCustomer" method will display all its attributes in this class.


class Customer():
 
    __ID=""
    __name=None
    __value=0.0


    def __init__(self,ID, name, value):
        self.__ID=ID
        self.set_name(name)
        self.__value=value

    def set_name(self, name):
        
        if type(name) is str:
                
            self.__name=name
                
        else:
            print("Name cannot be a digit, try again")

    def set_ID(self,ID):
        self.__ID=ID

    def set_value(self,value):
        self.__value=value
                       
    def get_ID(self):
        return self.__ID
   
    def get_name(self):
        return self.__name

    def get_value(self):
        return self.__value

    def get_rate(self):
        return "0"

    def get_discount(self,cost):
        return 0,0
                    
    def displayCustomer(self):
        print(self.get_ID())
        print(self.get_name())
        print(self.get_value())


# "Class Member"  is a memeber with a membership and it has a 5% discount.
# It has a private attributes called: "__rate_of_discount".
# The constructor has the same elements like normal customer class.
# This class is called as child class because inherits from "class customer", which acquires all the properties and behaviors of the "parent class".
# It has two getter which return the values of the attributes of "rate" and  "get_discount".
# "get_discount" method has a variable called"cost" which allows to calculate the discount applied and it returns the rate and the discount applied. 
# "displayCustomer" method display all its attributes in this class and the "setRate" allow to modify the old rate.



class Member(Customer):
    
    __rate_of_discount=0.05
    
    def __init__(self,ID, name, value, new_rate=0.05):
        super().__init__(ID, name, value)
        self.__rate_of_discount=new_rate

 
    def get_rate(self):
        return self.__rate_of_discount
    
    def get_discount(self,cost):
        print(cost)
        discount_applied=cost*self.__rate_of_discount
        return self.__rate_of_discount, discount_applied
        
    def displayCustomer(self):
        
        print(self.get_ID())
        print(self.get_name())
        print(self.get_value())
        print(self.get_rate())
              
    def setRate(self,new_rate):
        self.__rate_of_discount=new_rate


# "Class VipMember" is a special member and they have as default rate 10% but if they buy more than 1000(threshold), then discount will be 15%.
# It has private attributes called "__rate" and "__threshold".
# Its constructor contain ID, name, value and threhold. As I explained above this is a child class because inherits from "class customer".
# "get_discount" method validates the cost  must be greater than 0 and smaller than the threshold in order to appply de correct rate discount. Otherwise, it 
# will apply 15% discount. It returns rate and discount applied.
# "setter" method allows to modidy its previous value of "rate" and "threshold".
# getters" method just return the values of "rate" and "threshold".
# "displayCusotmer" display all the variables. 



class VipMember(Customer):
    
    __rate= 0.1
    __threshold=1000
        
    def __init__(self,ID, name, value, threshold=1000):
        super().__init__(ID, name, value)
        self.__threshold=threshold

    def get_discount(self,cost):
        
        if (cost >0 and cost <= self.__threshold):
            
            disc_apl=cost*self.__rate
            return self.__rate,disc_apl
        elif cost <= 0:
            print('try again')
        else:
            
            disc_apl=cost*(self.__rate+0.05)
            return self.__rate+0.05,disc_apl

    def set_rate(self, new_rate):
        self.__rate=new_rate

    def set_threshold(self,new_threshold):
        self.__threshold=new_threshold

    def get_rate(self):
        return self.__rate
        
    def get_threshold(self):
        return self.__threshold
            

    def displayCustomer(self):
        
        print(self.get_ID())
        print(self.get_name())
        print(self.get_value())
        print(self.get_rate())
        print(self.get_rate()*1.05)
        print(self.get_threshold())
        
    
# "Class Destination" keeps track of information of different destinations. 
# It has four private varibles called: "ID", "Name", "price" and "SeatAvailables".
# Its constructor has the variables metioned above and  SeatAvailables=50 as default value.
# When a new destination is created the number of seat availables is 50.
# All "setter" allows to update these variables.
# "getters" return the variables defined in this class.



class Destination():
    __ID=0   # ID PLACE
    __Name=""   #PLACE NAME
    __Price=0      # DESTINATION COST
    __SeatAvailable=0
    
    def __init__(self,ID,Name,Price,SeatAvailable=50):
        self.__ID=ID
        self.__Name=Name
        self.__Price=Price
        self.__SeatAvailable=SeatAvailable

    def set_ID(self,new_ID):
        self.__ID=new_ID

    def set_Name(self,new_Name):
        self.__Name=new_Name

    def set_price(self, new_price):
        self.__Price=new_price

    def set_SeatAvailable(self, new_seat):
        self.__SeatAvailable=new_seat


    def get_ID(self):
        return self.__ID

    def get_Name(self):
        return self.__Name

    def get_price(self):
        return self.__Price
    
    def get_SeatAvailable(self):
        return self.__SeatAvailable


# "Class Booking" handles the customer bookings.
# It support the following private attributes : "customer", destination", "quantity", "extra services" and "date". 
# The constructor received an "obj_custer" which contains information about all different type of customer. 
# It also received an "obj_destination" which allows to access to the infomation of detinations.
# "quantive" refers to number of tickets and "date" save the real time date.

class Booking():
    
    __date=None
    __extra_service=None

    def __init__(self,obj_customer, obj_destination,quantity,extra_service,date=datetime.datetime.now().strftime("%d/%m/%Y" +' '+ '%X')):
        self.__customer=obj_customer
        self.__destination=obj_destination
        self.__quantity=quantity
        self.__extra_service=extra_service
        self.__date=date


 


# "reservation" method allows to indentify what kind of service and calculate the "total cost" and update the seat avaibles. 
# This method has one parameter called "obj_SB" which means the infomations of the services and bunldes.

    def reservation(self, obj_SB):
        if None == obj_SB:
            cost_before_disc=self.__destination.get_price()*self.__quantity
            rate,discount=self.__customer.get_discount(cost_before_disc)
            total_cost=cost_before_disc-discount
        
            self.spend_record(total_cost)
            self.new_seats_left(self.__quantity)
            return total_cost
        elif "S" in obj_SB.get_ID():

            cost_before_disc=self.__destination.get_price()*self.__quantity
            rate,discount=self.__customer.get_discount(cost_before_disc)
            total_cost=cost_before_disc-discount+obj_SB.get_price()
        
            self.spend_record(total_cost)
            self.new_seats_left(self.__quantity)
            return total_cost
        elif "B" in obj_SB.get_ID():
            cost_before_disc=self.__destination.get_price()*self.__quantity
            rate,discount=self.__customer.get_discount(cost_before_disc)
            total_cost=cost_before_disc-discount+obj_SB.get_price()
        
            self.spend_record(total_cost)
            self.new_seats_left(self.__quantity)
            return total_cost
        

# "spend_record" method update the total value of the certain client and it is saved in the fuction "set_value."
# This method  has one parameter called "value".

    def spend_record(self,value):
        value_old=self.__customer.get_value()
        total_value=value_old+value
        self.__customer.set_value(total_value)
    
    
# "new_seats_left" method calculate the left seat availables after a booking.
# It has one parameter:"buy_seats" which allow to update the seats availables for a cetain destination.


    def new_seats_left(self,buy_seats):
        old_seats=self.__destination.get_SeatAvailable()
        seats_left=old_seats-buy_seats
        self.__destination.set_SeatAvailable(seats_left)

   
# Getter methods return the the infomation save it in "obj_customer", "obj_destination", "quantity","extra_services" and "date" respectively.
 
    def get_customer(self):
       return self.__customer
    def get_destination(self):
        return self.__destination
    def get_quantity(self):
        return self.__quantity
    def get_extra_service(self):
        return self.__extra_service
    def get_date(self):
        return self.__date



# "Class Records" is the central data repository.
# It supports the following private attributes: "list_customers","list_destinations","list_services","list_bundles" and "list_bookings". 
# It has 19 methods where some of them are related with read files, get the informations of each file, find a specific customer, services or destinations.
# Tit has some methods where display customer bookings.

class Records():
    __list_customers=[]
    __list_destinations=[]
    __list_services=[]
    __list_bundles=[]
    __list_bookings=[]
    
 
# "readCustomer" method reads the file which contains all customers information. 
# While loop was used for read each line in the file until find a black space and it will stop.
# All the elements are save in a list called "__lits_customer".
# Inside has "try except" method was used to catch a Error and provide our own error message and it will log out of the program.


    def readCustomers(self,file_name):
        try:
            file=open(file_name,'r')
            
            line=file.readline()
        
            while (line != ""):
                fields=line.split(", ")
            
                if 'C' in fields[0]:
                    C=Customer(fields[0],fields[1],float(fields[3]))
               
                    self.__list_customers.append(C)   
                

                if 'M' in fields[0]:
                    M=Member(fields[0],fields[1],float(fields[3]))
                    M.setRate(float(fields[2]))
                    self.__list_customers.append(M)   
                
            
                if 'V' in fields[0]:
                    V=VipMember(fields[0],fields[1],float(fields[3]))
                    V.set_rate(float(fields[2]))
                    self.__list_customers.append(V)   
                

                line=file.readline()
          
            file.close()
        except: 
            sys.exit('Something is wrong with the file')
       # return i

# "readDestinations" method reads the file which contains all destinations information. 
# While loop was used for read each line in the file until find a black space and it will stop.
# all the elements are save in a list called "__lits_destinations".

    def readDestinations(self, file_name):
        
        file= open(file_name,'r')
    
        line=file.readline()
      
        while (line != ""):
            fields=line.split(", ")
            D=Destination(fields[0],fields[1],int(fields[2]), int(fields[3]))
            self.__list_destinations.append(D)   
            
            line=file.readline()
        file.close()

# "readService" method reads the file which contains all services information and stored them for future usage.
# all services  were saved in  "__lits_services".
# all bundles were saved in  "__lits_bundle".

    def readService(self,file_name):
        
        file= open(file_name,'r')
    
        line=file.readline()
      
        while (line != ""):
            fields=line.strip().split(", ")
            if "S" in fields[0]:
                S=Services(fields[0],fields[1], int(fields[2]))
                self.__list_services.append(S)

            elif "B" in fields[0]:
                    
                list_servicesIDs=[]
                for i in range(2,len(fields)): 
                    list_servicesIDs.append(self.findServices(fields[i]))

                B=Bundle(fields[0],fields[1],list_servicesIDs)

                self.__list_bundles.append(B)
                   
            line=file.readline()

        file.close()


# "readBookings" method reads the file which contains all bookings information. 
# While loop was used for read each line in the file until find a black space and it will stop.
# all the elements were saved in "__list_bookings".
# Inside has "try except" method was used to catch a Error and provide our own error message where the code cannot read and it will ingore it.


    def readBookings(self,file_name='bookings.txt'):
        
        file = open(file_name,'r')
        line=file.readline()
        
        while (line != ""):
            fields=line.strip().split(", ")
            try:
                obj_customer=self.findCustomer(fields[0])
                obj_destination=self.findDestination(fields[1])
                B=Booking(obj_customer,obj_destination,int(fields[2]),fields[3],fields[5])

                
                self.__list_bookings.append(B)   
            except:
                print('A booking line was ignored.')
                pass
            
            line=file.readline()
        
        file.close() 


# get method will return the information save in "__list_customers".
    def get_list_customers(self):
        return self.__list_customers

# get method will return the information save in "__list_destinations".

    def get_list_destinations(self):
        return self.__list_destinations

# get method will return the information save in "__list_services".

    def get_list_services(self):
        return self.__list_services
    
 # getters method will return the information save in "__list_bundles".

    def get_list_bundle(self):
        return self.__list_bundles

# get method will return the information save in "__list_bookings".

    def get_list_bookings(self):
        return self.__list_bookings

  
# "findCustomer" method find a customer either its name or ID.
# It has one parameter called "text".
# if the method find the customer this return the objet in certain position, but if the method doesn't find a customer will return "None".

    def findCustomer(self, text):

        for i in range(len(self.__list_customers)):

            if text in self.__list_customers[i].get_ID() or text in self.__list_customers[i].get_name():
                return self.__list_customers[i]  
        return None
    

# "findDestination" method find the destination either its name or ID.
# It has one parameter called "text".
# if the method find the destination and it returns in the object with certain position, but if the method doesn't find the destination will return "None".

    def findDestination(self,text):

        for i in range(len(self.__list_destinations)):
            if (text in self.__list_destinations[i].get_ID() or text in self.__list_destinations[i].get_Name()):
                return self.__list_destinations[i]
        return None


# "findServices" method find a specific service either by name or ID.
# It has one parameter called "text".
# if the method find services this return the objet in cetain position, but if the method doesn't find a customer will return "None".


    def findServices(self,text):
        for i in range(len(self.__list_services)):
            if text in self.__list_services[i].get_ID() or text in self.__list_services[i].get_name():
                return self.__list_services[i]
        for i in range(len(self.__list_bundles)):
            if text in self.__list_bundles[i].get_ID() or text in self.__list_bundles[i].get_name():
                return self.__list_bundles[i] 
        return None


# "listCutomers" method contains all the customers either "Customer","Member" or "VipMember".
# It iterates over the items on "__list_customers"  list. 
# It displays the "ID", "name","rate_discount" and "value" for each different client.

    def listCutomers(self):
        for i in range(len(self.__list_customers)):
            if 'C' in self.__list_customers[i].get_ID():
                print(self.__list_customers[i].get_ID() +', ' + self.__list_customers[i].get_name()+', '+ '0' + ', '+ str(self.__list_customers[i].get_value()))
            if 'M' in self.__list_customers[i].get_ID():
                print(self.__list_customers[i].get_ID() +', ' + self.__list_customers[i].get_name()+', '+ str(self.__list_customers[i].get_rate())+ ', '+ str(self.__list_customers[i].get_value()))
            if 'V' in self.__list_customers[i].get_ID():
                print(self.__list_customers[i].get_ID() +', ' + self.__list_customers[i].get_name()+', '+ str(self.__list_customers[i].get_rate())+ ', '+ str(self.__list_customers[i].get_value()))

# "listDestinations" method contains all the destinations information such as: "ID", "name", "price" and "seatAvailable".
# It iterates over the items on "__list_destinations"  list. It displays the "ID", "name","price" and "seatAvailable" for each different destination.

    def listDestinations(self):
        for i in range(len(self.__list_destinations)):
            print(self.__list_destinations[i].get_ID() + ", "+ self.__list_destinations[i].get_Name() + ", " + str(self.__list_destinations[i].get_price()) +", "+str(self.__list_destinations[i].get_SeatAvailable()))

# "listServices" method contains all the list of services and bundles.
# It iterates over the item on "__list_services"  and it displays the information for each different services.   
# It iterates over the item on "__list_bundles" list. It displays the "ID", "name" and the id_text which contains element of the services. 

    def listServices(self):
        for i in range(len(self.__list_services)):
            print(self.__list_services[i].get_ID() +", "+ self.__list_services[i].get_name()+", "+str(self.__list_services[i].get_price()))

        for i in range(len(self.__list_bundles)):
            list=self.__list_bundles[i].get_list_IDs()
            #print(list)
            id_text=""
            for j in range(len(list)):
                if j+1 <len(list):
                    id_text=id_text+list[j].get_ID()+", "
                else:
                    id_text=id_text+list[j].get_ID()

            print(self.__list_bundles[i].get_ID()+", "+ self.__list_bundles[i].get_name()+", "+ id_text)
        print("\n")

# "listBooking" method contains all the list of bookings.
# It displays the" customer name", "destination name", "tickets", "extra service" and "date" as the original file.
# It iterates over the item on "__list_bookings"  and it displays the information for each different bookings.  

    def listBooking(self):
        print("{:<10}  {:>10}  {:>10}  {:>19}  {:>13}".format('Name','Destination','Ticket','Services','Date'))

        for i in range(len(self.__list_bookings)):
            print("{:<10}  {:>10}  {:>10}  {:>19}  {:>20}".format(self.__list_bookings[i].get_customer().get_name(),self.__list_bookings[i].get_destination().get_Name(),self.__list_bookings[i].get_quantity(),self.__list_bookings[i].get_extra_service() ,self.__list_bookings[i].get_date()))

# "display_customer_bookings" method displays the booking the information for a specific client which has previously a booking.
# It iterates over the item on "self.__list_bookings" in order to find if the customer who has enter by  the agent. 
# If the customer is in the list it will display the infomartion. Otherwise, it prints a message indicating that the client has not made a booking before.

    def display_customer_bookings(self):
        name= input('Please, enter a customer name:\n')
        flag=0
        for element in self.__list_bookings:
            if element.get_customer().get_name() == name:
                flag+=1
                
                if flag ==1:
                    print("{:<10}  {:>10}  {:>10}  {:>19}  {:>13}".format('Name','Destination','Ticket','Services','Date'))
                
                print("{:<10}  {:>10}  {:>10}  {:>19}  {:>20}".format(element.get_customer().get_name(),element.get_destination().get_Name(),element.get_quantity(),element.get_extra_service() ,element.get_date()))   
        
        if flag==0:
            print('Customer has not made any bookings.')


    

# "display_valuable_customer" method displays the most valuable customer who has the highest money.
# Using "max()" fucntion and lambda function on "__list_customers" in order to get the customer name with the highest money spend.

    def display_valuable_customer(self):
        cust=max(self.__list_customers, key=lambda c: c.get_value() )
        print("\nThe most valuable customer is: " + cust.get_name()+"\n")

# "display_popular_destination" method  print the most popular destinations with the highest number of bookings.
# It iterates over the item on "__list_bookings" and save all the found it in a new list called "list_dest_names".
# Then I iterate again using this list and using the count() function in order to find de most popular destination.

    def display_popular_destination(self):

        list_dest_names=[]
        for dest in self.__list_bookings:
            list_dest_names.append(dest.get_destination().get_Name())
            
        dict_dest={}
        for element in list_dest_names:
            dict_dest[element]=list_dest_names.count(element)
        print(max(dict_dest))
            

# "Class operation" is the main class of the program and it support the menu option.
# It has a "obj_records" object of the class "Records" which allows to access its information.
# "__adjust_rate", "__flag_adjust_rate", "__adjust_threshold" and "__flag_adjust_threshold" are the attributes which allows in the next methods adjust each element.
# it has 15 methods inside.

class Operations():

    obj_records=Records()
    __adjust_rate=0
    __flag_adjust_rate=False
    __adjust_threshold=0
    __flag_adjust_threshold=False


# "initialization" method uses the command line arguments to accept the four files called: 
# "customer_file_name.txt", "destination_file_name.txt", "service_file_name.txt"and "booking_file_name.txt.
# "try except" method was used to catch  own our error.
# When the user enter the correct number of fiel but it occurs a error trying to open, the program will exit.
#  Otherwise, when the user didn't enter the correct number of files the program print a message indicating that the number of files are not correct and it will exit. 


    def initialization(self):
        print("\n\n")
        read_files=input('Please provide the file\'s names necessary to run the program.\nSeparate the names with ",". Follow this order: "customer_file_name.txt", "destination_file_name.txt", "service_file_name.txt", "booking_file_name.txt":\n')
        read_files= read_files.split(',')
        print("\n\n")
        if len(read_files)==4 or len(read_files)==3:
            try:       
                self.obj_records.readCustomers(read_files[0])   
                self.obj_records.readDestinations(read_files[1])
                self.obj_records.readService(read_files[2])
                if len(read_files)==4:
                    self.obj_records.readBookings(read_files[3])
                elif len(read_files)==3:
                    self.obj_records.readBookings()
            except:
                sys.exit('An error occurred when trying to open one of the files.')
        else:
            print()
            sys.exit('A wrong number of arguments were provided. Arguments are: "customer_file_name.txt", "destination_file_name.txt", "service_file_name.txt", "booking_file_name.txt"')

 
# "create_uniqueID" method creates and returns an unique"ID" when a new customer either normal customer, member or vip member is created.
# It has three list where the "ID's are saved of each diffent customer "C", "M" for a member and "V" for a vip member is saved respectively.
# To access to the customer information an object is created and called "client_list" and it is the class "Records" which allows to access 
# to the "get_list_customers" method which contains all information.
# It iterates over the items on "client_list" and it saves the ID's of different kind of clients as I mentioned above. 
# It iterates over the items on each list and look for the string of "ID", if the "ID" exist it pass, otherwise, it creates a unique "ID".
# It returns the unique "ID" created. 

    def create_uniqueID(self,letter):
        list_of_customers=[]
        list_of_members=[]
        list_of_vips=[]

        client_list= self.obj_records.get_list_customers()
        
        for i  in range(len(client_list)):
            if 'C' in client_list[i].get_ID():
                list_of_customers.append(client_list[i].get_ID())
            if 'M' in client_list[i].get_ID():
                list_of_members.append(client_list[i].get_ID())
            if 'V' in client_list[i].get_ID():
                list_of_vips.append(client_list[i].get_ID())  
        if letter == 'C':
            
            for i in range(len(list_of_customers)):
                if str(i+1) in list_of_customers[i]:
                    pass
                else:
                    id="C"+str(i+1)
                    return id
            return "C1"
        
        if letter == 'M':

            for i in range(len(list_of_members)):
                if str(i+1) in list_of_members[i]:
                    print(i)
                    pass
                else:
                    id="M"+str(i+1)

                    return id
            return "M1"
        if letter == 'V':
            
            for i in range(len(list_of_vips)):
                if str(i+1) in list_of_vips[i]:
                    pass
                else:
                    id="V"+str(i+1)
                    return id
            return "V1"



# "create_unique_id_destination" method create a unique "ID" when a new destination is created.
# "list_destinations" has the informations of the destinations. 
#  It iterates over the items on "list_destinations" and if the string are in the "get_ID" method it doesn't create the ID.
#  Otherweise, it creates a new "ID".


    def create_unique_id_destination(self):
        list_destinations = self.obj_records.get_list_destinations()
        for i in range(len(list_destinations)):
            if str(i+1) in list_destinations[i].get_ID():
                pass
            else:
                id="D" + str(i+1)
                
                return id
        return "D" + str(len(list_destinations)+1)
       
# "setting_new_book" method helps with creating a new reservation. 
# This method interact with the user, validates if reservation is for a new  customer and if not it will create his new record and it will ask if he wants a 
# new membership and type of it. 
# It also needs the destinations and number of tickets neccesary to do the reservation and it will call the functions that are required for calculations and new records.
# Finally, it will display on screen the summary of the reservation.



    def setting_new_book(self):
        customer_name= input('Enter the name of the customer [e.g. Eloisa]: ')
        new_vip=False
        obj_client=self.obj_records.findCustomer(customer_name)

        if None == obj_client:
           
            while True:
                try:
                    new_client=input('Do you want to have a membership or VIP membership? please enter "Y" for yes or "N" for no: ' )
                    if new_client == "Y" or new_client == "N":
                        if new_client == 'N':
                            obj_client=Customer(self.create_uniqueID('C'),customer_name,0.0)
               
                            self.obj_records.get_list_customers().append(obj_client)
                            break
                        elif new_client =="Y": 
                            while True:
                                try:
                                    member_type=input('which membership do you want? Type "M" for normal membership or "V" for VIP membership: ')
                                    if member_type == "M" or member_type =='V':
                                        if member_type == 'M':
                                            if self.__flag_adjust_rate==False:
                                                obj_client=Member(self.create_uniqueID('M'),customer_name,0)
                      
                                                self.obj_records.get_list_customers().append(obj_client)
                                                break
                                            else:
                                                obj_client=Member(self.create_uniqueID('M'),customer_name,0,self.__adjust_rate)
                                            
                                                self.obj_records.get_list_customers().append(obj_client)
                                                break
                                        if member_type =="V":
                                            if self.__flag_adjust_threshold ==False:
                                                obj_client=VipMember(self.create_uniqueID('V'),customer_name,100)
                                          
                                                self.obj_records.get_list_customers().append(obj_client)
                                                new_vip=True
                                                break              
                                            else: 
                                                obj_client=VipMember(self.create_uniqueID('V'),customer_name,100,self.__adjust_threshold)
                                                self.obj_records.get_list_customers().append(obj_client)
                                                new_vip=True
                                                break                            
                                        
                                    else:
                                        raise MembershipError ('You didn\'t enter a valid option')
                                except MembershipError as e:
                                    print(e)
                            break
                    else:
                        raise MembershipError ('You didn\'t enter a valid option')

                except MembershipError as e:
                    print(e)


        obj_destination= self.ask_destination()
        tickets=self.valid_tickets(obj_destination)
       

        while True:
            try:
                services_bundle=input('Do you want to add extra service? Please type "Y" for yes or "N" for no:  ')
                if services_bundle =="N": 
                    obj_SB=None
                    extra_service="None"
                    break
                elif services_bundle =="Y":
                    
                    while True:
                        extra_service=input('Which extra service do you want to add? ( Internet, Entertainment,StarterMax, StarterPlus, etc.):  ')

                        if "C" in obj_client.get_ID():
                            if extra_service== "Internet" or extra_service =="S1":
                                print('Cannot add free extra services')
                            else:
                                break
                        else:
                            break
                    obj_SB=self.obj_records.findServices(extra_service)
                    break
                else:
                    raise OperationError('You didn\'t enter a valid option. ')       
            except OperationError as e:
                print(e)
        obj_booking=Booking(obj_client,obj_destination, tickets,extra_service)

        self.obj_records.get_list_bookings().append(obj_booking)

        total=obj_booking.reservation(obj_SB)
        
        self.display_format(obj_client,tickets,obj_destination,total,new_vip,obj_SB)
  


# "ask_destination" method ask to the user enter the destination already exist otherwise it will print a error.

    def ask_destination(self):
        while(True):
            destination_name=input('Enter the destination [a valid destination only, e.g. Sydney, Geelong]: ')
            obj_destination=self.obj_records.findDestination(destination_name)
            try: 
                obj_destination=self.valid_destination(obj_destination)
                return obj_destination
            except DestinationError as e:
                print(e)


# "valid_destination" method validates that destinations enter by the user exit otherwise, it will ask again.

    def valid_destination(self,obj_destination):
        if None  == obj_destination:
            raise DestinationError('You didn\'t enter a valid place.')
        else: 
            return obj_destination
    
# "valid_tickets" methods validates if the number of tickets are positve integer.

    def valid_tickets(self,obj_destination):
        while True:
            try:
                tickets=int(input('Enter the number of tickets [enter a positive integer only e.g. 1,2,3]: '))
                if tickets ==0 or tickets<0:
                    raise TicketError('You didn\'t enter a positive integer number.')
                elif tickets >0 and type(tickets) is int:
                    return tickets

                elif tickets >obj_destination.get_SeatAvailable():
                    raise TicketError('Not enough seats available.')
            except TicketError as e:
                print(e)
            except ValueError:
                print('You didn\'t enter a positive integer number.')

# "book_a_new_trip" method allows to book multiples bookings

    def book_a_new_trip(self):
        
        self.setting_new_book()
        while True:
            multiple_booking=input('Do you want to make another booking trip : Please type "Y" for yes or "N" for no.  ')
            if multiple_booking == "Y":
                self.setting_new_book()
            else: 
                break

# "display_format" method displays the information of the client and its repectively booking information, price, discount and final cost.

    def display_format(self,obj_client, tickets, obj_destination,total_price, new_vip,obj_SB):
        rate,des_appl=obj_client.get_discount(total_price)


        if "C" in obj_client.get_ID()  or "M" in obj_client.get_ID():
            print(str(obj_client.get_name()) +  " books "+ str(tickets) + ' tickets to '+ str(obj_destination.get_Name()))
            print(str(obj_client.get_name()) + " gets a disccount of " +str(rate)+"%")
            print("{:<10}  {:>11}  {:>4}".format('Unit price: ' ,str(obj_destination.get_price()),'(AUD)'))
            if None == obj_SB:
                print("{:<10}  {:>10}  {:>4}".format('Total price: ',str(total_price),'(AUD)'))
            else:
                print("{:<10}  {:>2}  {:>4}".format("Extra service price: ", str(obj_SB.get_price()), '(AUD)' ))
                print("{:<10}  {:>10}  {:>4}".format('Total price: ',str(total_price),'(AUD)'))


        if "V" in obj_client.get_ID():
            print(str(obj_client.get_name()) +  " books "+ str(tickets) + ' tickets to '+ str(obj_destination.get_Name()))
            print(str(obj_client.get_name()) + " gets a disccount of " + f'{rate:.2f}%')
            print("{:<10}  {:>11}  {:>4}".format('Unit price: ' ,str(obj_destination.get_price()),'(AUD)'))

            if new_vip==True:
                print("{:<10}  {:>5}  {:>4}".format('Membership price: ' ,'100','(AUD)'))
                if None == obj_SB:
                    print("{:<10}  {:>10}  {:>4}".format('Total price: ',str(total_price+ 100),'(AUD)'))
                else:
                    obj_SB.get_price()
                    print("{:<10}  {:>2}  {:>4}".format("Extra service price: ", str(obj_SB.get_price()), '(AUD)' ))
                    print("{:<10}  {:>10}  {:>4}".format('Total price: ',str(total_price+obj_SB.get_price()+100),'(AUD)'))
            else:
                if None == obj_SB:
                    print("{:<10}  {:>8}  {:>4}".format('Total price: ',str(total_price),'(AUD)'))
                else:
                    print("{:<10}  {:>2}  {:>4}".format("Extra service price: ", str(obj_SB.get_price()), '(AUD)' ))
                    print("{:<10}  {:>10}  {:>4}".format('Total price: ',str(total_price+obj_SB.get_price()),'(AUD)'))

# "adjustments" method allows to adjust the the rate of member class and the threshold of vip member.

    def adjustments(self):
        list_of_customer=self.obj_records.get_list_customers()
        
        for element in list_of_customer:
            if "M" in element.get_ID():
                element.setRate(self.__adjust_rate)
            if "V" in element.get_ID():
                element.set_threshold(self.__adjust_threshold)

# "save_data_customers" method saves the new customer information in customers.txt file.
  
    def save_data_customers(self):
        file=open("customers.txt", "w")
        num_of_cust= len(self.obj_records.get_list_customers())
        for i in range(num_of_cust):
            if 'C' in self.obj_records.get_list_customers()[i].get_ID():
                line=self.obj_records.get_list_customers()[i].get_ID() +', ' + self.obj_records.get_list_customers()[i].get_name()+', '+ '0' + ', '+ str(self.obj_records.get_list_customers()[i].get_value())

            if 'M' in self.obj_records.get_list_customers()[i].get_ID():
                line=self.obj_records.get_list_customers()[i].get_ID() +', ' + self.obj_records.get_list_customers()[i].get_name()+', '+ str(self.obj_records.get_list_customers()[i].get_rate())+ ', '+ str(self.obj_records.get_list_customers()[i].get_value())

            if 'V' in self.obj_records.get_list_customers()[i].get_ID():
                line=self.obj_records.get_list_customers()[i].get_ID() +', ' + self.obj_records.get_list_customers()[i].get_name()+', '+ str(self.obj_records.get_list_customers()[i].get_rate())+ ', '+ str(self.obj_records.get_list_customers()[i].get_value())

            
            if i+1 < num_of_cust:
                file.write(line+"\n")
            else:
                file.write(line)

        file.close()

#"save_data_destinations" method saves the new destination and the old destinations in destinations.txt file.

    def save_data_destinations(self):
        file=open("destinations.txt", "w")
        num_of_dest= len(self.obj_records.get_list_destinations())
        
        for i in range(num_of_dest):
        
            line=self.obj_records.get_list_destinations()[i].get_ID()+", "+self.obj_records.get_list_destinations()[i].get_Name()+", "+ str(self.obj_records.get_list_destinations()[i].get_price())+", "+str(self.obj_records.get_list_destinations()[i].get_SeatAvailable())
            if i+1 < num_of_dest:
                file.write(line+"\n")
            else:
                file.write(line)      
        file.close() 
         
# "save_data_services" method  saves the all services in services.txt file.

    def save_data_services(self):
        file=open("services.txt", "w")
        
        num_of_serv= len(self.obj_records.get_list_services())
        
        for i in range(num_of_serv):
        
            line=self.obj_records.get_list_services()[i].get_ID()+", "+self.obj_records.get_list_services()[i].get_name()+", "+ str(self.obj_records.get_list_services()[i].get_price())

            file.write(line+"\n")


        num_of_bundle= len(self.obj_records.get_list_bundle())
        
        for i in range(num_of_bundle):
            list=self.obj_records.get_list_bundle()[i].get_list_IDs()
            id_text=""
            for j in range(len(list)):
                if j+1 <len(list):
                    id_text=id_text+list[j].get_ID()+", "
                else:
                    id_text=id_text+list[j].get_ID()

            
            line=self.obj_records.get_list_bundle()[i].get_ID()+", "+self.obj_records.get_list_services()[i].get_name()+", "+ id_text
            
            if i+1 < num_of_bundle:
                file.write(line+"\n")
            else:
                file.write(line)      

        
        file.close()         

# "save_data_bookings" method saves the old and new booking in bookings.txt file.

    def save_data_bookings(self):
        file=open("bookings.txt", "w")
        num_of_dest= len(self.obj_records.get_list_bookings())
        
        for i in range(num_of_dest):
            line = self.obj_records.get_list_bookings()[i].get_customer().get_name()+", " +self.obj_records.get_list_bookings()[i].get_destination().get_Name()+ ", "+ str(self.obj_records.get_list_bookings()[i].get_quantity()) + ", "+ self.obj_records.get_list_bookings()[i].get_extra_service() +", "+ str(self.obj_records.get_list_bookings()[i].get_customer().get_rate()) + ", "+ self.obj_records.get_list_bookings()[i].get_date()
          
            if i+1 < num_of_dest:
                file.write(line+"\n")
            else:
                file.write(line)      
        file.close() 

        
# "run_menu" method displays menu options 
# Before display the menu the program will ask to enter the file names.

    def run_menu(self):
        
        self.initialization()

        options=True
        while options:
            print('\n\nWelcome to the Melbourne bus booking system!')
            print("\n===========================================\n")
            print('You can choose from the following options: \n')
            print( " 1. Book a new trip \n",
                    "2. Display the current customer list \n",
                    "3. Display the current destinations list \n",
                    "4. Display the current service list\n",
                    "5. Adjust the discount rate limit\n",
                    "6. Adjust the threshold limit\n",
                    "7. Display all the bookings\n",
                    "8. Add new destination\n",
                    "9. Display all the bookings of a customer\n",
                    "10. Display the most valuable customer\n",
                    "11. Display the most popular destination\n",
                    "12. Exit the program \n")
            

            while (True):
                try:
                    options=int(input('Choose one option:'))
            
                    if options >= 0 and options <=12:
                        break
                    else:
                        print('You did not choose a correct option,try again.')

                except ValueError:
                    print('You did not choose a correct option,try again.')     

# Inside option "1", "book_a_new_trip" method was called in order to book a new trip.

            if options ==1:
                
                self.book_a_new_trip()
    
# Option "2" displays all existing customer list.

            elif options==2:
                self.obj_records.listCutomers()

# Option "3" displays all existing destinations list.

            elif options==3:
                self.obj_records.listDestinations()

# Option "4" displays all existing services list.   
            
            elif options==4:
                self.obj_records.listServices()

# Option "5" adjust the discount rate of the class member.

            elif options==5:
                
                while True:
                    try:
                        new_rate=int(input("Adjust the discount rate: [Integer only e.g. 1,2,3]: "))
                        if new_rate ==0 or new_rate<0:
                            raise RateModiError('Non-number or negative number discount rate.')
                        elif new_rate >0 and type(new_rate) is int:
                            self.__adjust_rate=new_rate/100
                            self.__flag_adjust_rate=True
                            self.adjustments()
                            break
                    except RateModiError as e:
                        print(e)

# Option "6" adjust the threshold of the class vip member.

            elif options==6:
                
                while True:
                    try:
                        new_threshold=int(input("Adjust the threshold limit [Integer only e.g. 1,2,3]: "))
                        if new_threshold ==0 or new_threshold<0:
                            raise ThresholdError('You didn\'t enter a valid number')
                        elif new_threshold >0 and type(new_threshold) is int:
                            self.__adjust_threshold=new_threshold
                            self.__flag_adjust_threshold=True
                            self.adjustments()

                            break
                    except ThresholdError as e:
                        print(e)

# Option "7" displays all existing sand new bookings.

            elif options ==7:
                self.obj_records.listBooking()

# Option "8" allows to add a new destination.
            
            elif options==8:
                while True:
                    
                    while True:
                        add_new_destination=input('Add a new destination:')      
                        if None == self.obj_records.findDestination(add_new_destination):
                            
                            while True:
                                new_price=int(input('Add new price (enter a integer number 1,2,3): '))
                                if new_price <= 0:
                                    print('You didn\'t enter a valid number. ')
                                else:
                                    break
                            ID=self.create_unique_id_destination()
                            dest=Destination(ID, add_new_destination,new_price)
                            self.obj_records.get_list_destinations().append(dest)
                            break
                        else: 
                            print('Destination already exist. Try again. ')
                    while True:
                        additional_des=input('Do you want to add another new destination?: Type "Y" for yes or "N" for no. ')
                        if additional_des =="N" or additional_des =="Y":
                            break
                        else:
                            print('You didn\'t enter a valid option')
                    
                    if additional_des =="Y":
                        pass
                    elif additional_des =="N":
                        break

# Option "9" displays all the bookings for a specific customer.

            elif options==9:
                self.obj_records.display_customer_bookings()

# Option "10" displays the most valuable customer.

            elif options==10:
                self.obj_records.display_valuable_customer()


# Option "11" displays the most popular destinations based on bookings.

            elif options==11:
                self.obj_records.display_popular_destination()      

# Option "12" Exit the program and it will save all the modifications.

            elif options==12:

                self.save_data_customers()
                self.save_data_destinations()
                self.save_data_services()
                self.save_data_bookings()
                sys.exit()
    



Main_menu = Operations()
Main_menu.run_menu()






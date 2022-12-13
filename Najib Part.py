
class Laboratory:
    def __init__(self,Lab_name, cost):
        self.Lab_name = Lab_name
        self.cost = cost
    def __repr__(self):
          return f'{self.Lab_name} {self.cost}'

#Hospital Functions

def Hospital_Menu_options():
    Hospital_Menu_Input = input('Welcome to Alberta Hospital (AH) Managment system\n1 -    Doctors\n2 - 	Facilities\n3 - 	Laboratories\n4 - 	Patients\n')
    if int(Hospital_Menu_Input) > 4 or int(Hospital_Menu_Input) < 1 or Hospital_Menu_Input.isnumeric() == False:
        Hospital_Menu_Input = input('Your selection is invalid, please re-enter:\n ')
    return Hospital_Menu_Input


# Laboratory Functions
new_Laboratory = []
def enterLaboratoryInfo():
    new_Laboratory.append (input("Enter the Lab’s Name:"))
    new_Laboratory.append (input("Enter the Lab’s Cost:"))
    return new_Laboratory

def readLaboratoriesFile():
    Labs_file = open('laboratories.txt','r')
    for Labs_file_line in Labs_file:
            LaboratoryList.append(Laboratory(*Labs_file_line.split('_')))
    return LaboratoryList

def writeListOfLabsToFile():
    Laboratorys_file = open('laboratories.txt','r')
    LaboratoryList_File.write(str(new_Laboratory))
    LaboratoryList_File = Laboratorys_file.readlines()




def displayLaboratorysList():
    print("Lab_Name   Cost       ")
    for i in range(1, len(LaboratoryList)):
        print(f'{LaboratoryList[i].Lab_name:<20} {LaboratoryList[i].cost:<20}'.format(LaboratoryList[i]))


new_Laboratory = []
def addLabToFile():
    Lab_file = open('laboratories.txt','a')
    Lab_file.write(new_Laboratory)
    Lab_file.close()

def Laboratorys_Menu_options():
    print('Laboratorys Menu:')
    Laboratory_Menu_Input1 = input('1 - Display Laboratorys list\n2  - Add Laboratory\n3 - Back to the Main Menu\n')
    if int(Laboratory_Menu_Input1) > 3 or int(Laboratory_Menu_Input1) < 1 or Laboratory_Menu_Input1.isnumeric() == False:
        Laboratory_Menu_Input1 = int(input('Your selection is invalid, please re-enter:\n '))
    return Laboratory_Menu_Input1




#Start

Hospital_Input_value = Hospital_Menu_options()
while int(Hospital_Input_value) != 0:
 if int(Hospital_Input_value) > 4 or int(Hospital_Input_value) < 1:
    Hospital_Input_value = input('Your selection is invalid, please re-enter:\n ')
        
#print ('Doctors Menu:')
#Doctor_Menu_Input = input('1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n')

#Laboratory
 if int(Hospital_Input_value) == 3:
    Laboratory_Menu_Input = Laboratorys_Menu_options()
    while int(Laboratory_Menu_Input) != 3:
        if int(Laboratory_Menu_Input) > 3 or int(Laboratory_Menu_Input) < 1 or Laboratory_Menu_Input.isnumeric() == False:
            Laboratory_Menu_Input = input('Your selection is invalid, please re-enter:\n ')
        
        
    ##### List All Laboratorys  #####
        if int(Laboratory_Menu_Input) == 1:
            LaboratoryList = []
            LaboratoryList = readLaboratoriesFile()
 
            displayLaboratorysList()
            
            print('Back to the prevoius Menu')
            Laboratory_Menu_Input = Laboratorys_Menu_options()



    #### Entering new Laboratory   #####
        elif int(Laboratory_Menu_Input) == 2:
                new_line = enterLaboratoryInfo()
                print (new_line)
                Underline_Char = "_"
                formatDrInfo()
                new_Laboratory = formatDrInfo()
                print(new_Laboratory)

                addLabToFile()


                print('Back to the previous Menu')
                Laboratory_Menu_Input = Laboratorys_Menu_options()
                

                
    Hospital_Input_value = int(Hospital_Menu_options())


 elif Hospital_Input_value == '2':
    Facilities_Menu_Input = facilites_Menu_options()
    while Facilities_Menu_Input != '3':
        if Facilities_Menu_Input > '3' or Facilities_Menu_Input < '1' or Facilities_Menu_Input.isnumeric() == False:
            Facilities_Menu_Input = input('Your selection is invalid, please re-enter:\n ')
        
        
    ##### List All Laboratorys  #####
        if int(Facilities_Menu_Input) == 1:
            FacilitiesList = []
            Facilities_file = open('facilities.txt','r')
            FacilitiesList = Facilities_file.read()

            for i in range(1,5, len(FacilitiesList)):
                print(FacilitiesList)
                Facilities_file.close
                    

            print('Back to the prevoius Menu')
            Facilities_Menu_Input = facilites_Menu_options()

    #### Entering new Facility   #####
        elif int(Facilities_Menu_Input) == 2:
                new_facility = addFacility()
                print (new_facility)

                writeListOffacilitiesToFile()

                print('Back to the previous Menu')
                
                Facilities_Menu_Input = facilites_Menu_options()     
    Hospital_Input_value = int(Hospital_Menu_options())

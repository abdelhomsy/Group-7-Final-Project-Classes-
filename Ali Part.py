
class Patient:
    def __init__(self,pid,name, disease, gender, age ):
         self.pid = pid
         self.name = name
         self.disease = disease
         self.gender = gender
         self.age =age
    def __repr__(self):
          return f'{self.pid} {self.name} {self.disease} {self.gender} {self.age}'

#Hospital Functions

def Hospital_Menu_options():
    Hospital_Menu_Input = input('Welcome to Alberta Hospital (AH) Managment system\n1 -    Doctors\n2 - 	Facilities\n3 - 	Laboratories\n4 - 	Patients\n')
    if int(Hospital_Menu_Input) > 4 or int(Hospital_Menu_Input) < 1 or Hospital_Menu_Input.isnumeric() == False:
        Hospital_Menu_Input = input('Your selection is invalid, please re-enter:\n ')
    return Hospital_Menu_Input


# Patient Functions
new_Patient = []
def enterPatientInfo():
    new_Patient.append (input("Enter the Patient’s ID:"))
    new_Patient.append (input("Enter the Patient’s name:"))
    new_Patient.append (input("Enter the Patient’s Disease:"))
    new_Patient.append (input("Enter the Patient’s Gender:"))
    new_Patient.append (input("Enter the Patient’s Age:"))
    return new_Patient

PatientList = []
def readPatientsFile():
    Patients_file = open('patients.txt','r')
    for Patients_file_line in Patients_file:
            PatientList.append(Patient(*Patients_file_line.split('_')))
    return PatientList

def writeListOfPatientsToFile():
    PatientList_File_Data = []
    Patients_file = open('patients.txt','r')
    PatientList_File_Data=Patients_file.readlines()

    for Line_Number, Patient_Details in enumerate(PatientList_File_Data):
        if str(Input_Patient_PID_Edit) in Patient_Details :
            PatientList_File_Data[Line_Number] = updated_current_Patient_str + '\n'
    return PatientList_File_Data

def displayPatientInfo():
    PatientList = []
    Patients_file = open('patients.txt','r')
    for Patients_file_line in Patients_file:
        PatientList.append(Patient(*Patients_file_line.split('_')))
    return PatientList

def displayPatientsList():
    print("Id        Name       Disease     Gender    Age   ")
    for i in range(1, len(PatientList)):
        print(f'{PatientList[i].pid:<10} {PatientList[i].name:<12} {PatientList[i].disease:<12} {PatientList[i].gender:<10} {PatientList[i].age:<10} '.format(PatientList[i]))



def addPatientToFile():
    Patients_file = open('patients.txt','a')
    Patients_file.write('\n' + new_Patient_str)
    Patients_file.close()

current_Patient = []
def editPatientInfo():
    current_Patient.append (input("Enter the Patient’s ID:"))
    current_Patient.append (input("Enter the Patient’s name:"))
    current_Patient.append (input("Enter the Patient’s Disease:"))
    current_Patient.append (input("Enter the Patient’s Gender:"))
    current_Patient.append (input("Enter the Patient’s Age:"))
    return current_Patient

def searchPatientById():
    Input_Patient_ID = input('Enter the Patient ID:')
    for i in range(1, len(PatientList)):
        if str(Input_Patient_ID) == str(PatientList[i].pid):
                print(PatientList[i])
                break
    else:
            print("Can't find the Patient with the same ID on the system")




def formatPatientInfo():
    Underline_Char = "_"
    for i in range(0, len(new_Patient)):
      new_Patient_str = Underline_Char.join(new_Patient)
    return new_Patient_str

def Patients_Menu_options():
    print('Patients Menu:')
    Patient_Menu_Input1 = input('1 - Display Patients list\n2 - Search for Patient by ID\n3 - Add Patient\n4 - Edit Patient info\n5 - Back to the Main Menu\n')
    if int(Patient_Menu_Input1) > 6 or int(Patient_Menu_Input1) < 1 or Patient_Menu_Input1.isnumeric() == False:
        Patient_Menu_Input1 = input('Your selection is invalid, please re-enter:\n ')
    return Patient_Menu_Input1



#Start

Hospital_Input_value = Hospital_Menu_options()
while int(Hospital_Input_value) != 0:
 if int(Hospital_Input_value) > 4 or int(Hospital_Input_value) < 1:
    Hospital_Input_value = input('Your selection is invalid, please re-enter:\n ')
        
#print ('Doctors Menu:')
#Doctor_Menu_Input = input('1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n')

#Patients
 if int(Hospital_Input_value) == 4:
    Patient_Menu_Input = Patients_Menu_options()
    while int(Patient_Menu_Input) != 5:
        if int(Patient_Menu_Input) > 5 or int(Patient_Menu_Input) < 1 or Patient_Menu_Input.isnumeric() == False:
            Patient_Menu_Input = input('Your selection is invalid, please re-enter:\n ')
        
        
    ##### List All Patients  #####
        if int(Patient_Menu_Input) == 1:
            PatientList = []
            PatientList = readPatientsFile()
 
            displayPatientsList()
            
            print('Back to the prevoius Menu')
            Patient_Menu_Input = Patients_Menu_options()

    ### Search for a Patient  by ID #####

        elif int(Patient_Menu_Input) == 2:
                PatientList = []
                PatientList = displayPatientInfo()
    
                searchPatientById()

                print('Back to the previous Menu')
                Patient_Menu_Input = Patients_Menu_options()

    #### Entering new Patient   #####
        elif int(Patient_Menu_Input) == 3:
                enterPatientInfo()
                print (new_Patient)
                Underline_Char = "_"
                formatPatientInfo()
                new_Patient_str = formatPatientInfo()
                print(new_Patient_str)

                addPatientToFile()


                print('Back to the previous Menu')
                Patient_Menu_Input = Patients_Menu_options()
                


    ####   Edit current Patient  ####
        elif int(Patient_Menu_Input) == 4:
                PatientList = []
                Patients_file = open('Patients.txt','r')
                for Patients_file_line in Patients_file:
                    PatientList.append(Patient(*Patients_file_line.split('_')))


                Input_Patient_PID_Edit = input('Please enter the id of the Patient that you want to edit their information: ')
                Input_Patient_PID_Edit = int(Input_Patient_PID_Edit)
                for i in range(1, len(PatientList)):
                    if int(Input_Patient_PID_Edit) == int(PatientList[i].pid):
                        print (PatientList [i])
                        break
                else:
                 print("Can't find the Patient with the same ID on the system")

                editPatientInfo()
                print (current_Patient)
                Underline_Char = "_"
                for i in range(0, len(current_Patient)):
                    updated_current_Patient_str = Underline_Char.join(current_Patient)

                print(updated_current_Patient_str)

                PatientList_File_Data = writeListOfPatientsToFile()

                print(PatientList_File_Data)

                Patients_File_Update = open('Patients.txt','w')
                for i in range(0, len(PatientList_File_Data)):
                    Patients_File_Update.write(PatientList_File_Data[i])
                print('Back to the previous Menu')
                Patients_File_Update.close()
                Patient_Menu_Input = Patients_Menu_options()
                
    Hospital_Input_value = int(Hospital_Menu_options())

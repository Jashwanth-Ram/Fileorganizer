import shutil
import os

# file_organizer func() : 
def file_organizer():
    path = input("Enter path: ")
    file_list = os.listdir(path)

    for file in file_list:
        file_name, extension = os.path.splitext(file) # retrieving filename and extension from each file
        extension = extension[1:] # getting rid of dot operator

        if os.path.exists(path+"/"+extension):
            shutil.move(path+"/"+file, path+"/"+extension+"/"+file)
        else:
            os.makedirs(path+"/"+extension)
            shutil.move(path+"/"+file, path+"/"+extension+"/"+file)



file_organizer();



        






    
    

    


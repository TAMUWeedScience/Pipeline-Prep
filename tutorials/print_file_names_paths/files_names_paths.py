import os

#input dir(folder) path in terminal
dir = input("Directory path: ")

# get file list and 
def files_names_paths(dir):
    '''
    This function will give you names and path of files in a directory(folder)

    Arguments: dir(folder) 
    '''
    #get file names
    file_list = os.listdir(dir)
    for files in file_list:
        print(files)

    #get file paths
    for files in file_list:
        print(f"{dir}/{files}")
        
files_names_paths(dir)
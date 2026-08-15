import os

red = "\033[31;4;1m"
yellow = "\033[33;4;1m"
green = "\033[32;4;1m"
reset = "\033[0m"
def cabinet():
    print(f"{yellow}This is a CLI Auto create folder Project so fill in the information and Your Folder will be created automatically instead of doing the command manually{reset}")

    # i ask for the user input here
    folder_name = input(f"{green}\nplease input your folder name please{reset} ")

    # then i use os.mkdirs() to create the folder name the user requested
    os.makedirs(folder_name)

    #here i collects the file name from the user
    while True:
     file_name = input(f"\n{green}input your file name here{reset}  ")
     if file_name.endswith(".py"):
        print(f"{yellow}\nokay")
        break
     else:
        print(f"{red}Error creating file: check file name well{reset}")
    
    # then here i connect the user folder name and my file name together
    file_path = os.path.join(folder_name, file_name)

    # then i actually create the file using open
    open(file_path, "w").close()
    while True:
     ask = input(f"{yellow}do you want to know your current working directory?{reset}  ").lower()
     if ask == "yes":
      #then i add the abspath function to show current directory(pwd)
      pwd = os.path.abspath(folder_name)
      print(f"\n {green} {pwd} {reset}")
      break
     
     elif ask == "no":
       break

    #and then for me to list what is inside the folder i use os.listdir()
    contents = os.listdir(folder_name)
    print(f"\n{yellow}here is your contents in this current directory {contents}{reset}")
    print(f"\n\n{green}successful both file and folder are created check!{reset}")
cabinet()
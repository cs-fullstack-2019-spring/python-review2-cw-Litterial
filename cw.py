def main():
#Create a task list. A user is presented with the text below. Let them select an option to list all of their tasks,
# add a task to their list, delete a task, or quit the program.

    array=["Finish this project.","Go to work", "Catch up on missed television programs."]   #array for all actions

    def listoftask():  #1. List all tasks.
        for x in array:
            print(x)

    def moretask():  #2 Add a task to the list.
        anothertask=input("Please enter a task you would like to add to your list\n")
        array.append(anothertask)
        print("Task List has been updated: ")
        for x in array:
            print(x)

    def deletetask(): #3. Delete a task.
        findtask= input("Please input the task you would like to delete.\n")
        for x in array:
            if findtask in array:  #searches array for task
                array.remove(findtask)  #removes task
                print(f"The task '{findtask}' has been removed\n")  #notifies that the task has been removed and exits
                print("Task List has been updated: ")
                for x in array:
                    print(x)
                break
            else:
                print(f"The task '{findtask}' was not available.\n") #notifies that event was not found
                print("Current Task List: ")
                for x in array:
                    print(x)
                break

    def taskManager(): #manages all methods
        question= (input("Hello Juwan. What would like to do today?\nPress '1' to see a list of your tasks\nPress'2' to add "   #asks for input
                            "a task to your list\nPress '3' to delete a task.\nPress'0' to exit this program\n"))
        while (question!='0'):   # loops until '0' is entered
            while (question!= '1' and question!='2' and question!='3' and question!='0'):  #loops until a valid input is entered
                question= (input("That is not a valid input. Please select one of the following options:\nPress '1' to see a list of your task\nPress'2' to add "
                                 "a task to your list\nPress '3' to enter a task.\nPress'0' to exit this program.\n"))
            if(question=="1"):  #if 1 is entered, calls listoftask()
                print("You have selected '1' to see a list of your tasks.\n ")
                listoftask()
            elif(question =="2"): #if 2 is entered, calls moretask()
                print("You have selected '2' to add a task to your list.\n")
                moretask()

            elif(question =="3"):#if 3 is entered, calls deletetask()
                print("You have selected '3' to delete a task.\n ")
                deletetask()

            question=input("\nThank you. If you would like to exit, enter '0' otherwise select another task. \n")
        print("\nThank you Kenn and Kevin for giving Juwan this easy assignment")  #witty exit remark

    taskManager()

if __name__ == '__main__':
    main()
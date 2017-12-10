# creatingting a bank application

print('\nlets make a program for bank application\n\n')
print('\nwe have to define various lists\n\n')

Bank = {
        
        "Name":["Arpit","Aditi","Sachin"],
        "Acc_No":[1001,2002,3003],
        "Bal":[11111,22222,33333],
        "Add":["Jaipur","Mansarovar","Agra"],
        "Acc_typ":["Debit","Credit","Double"]
        
        }

x = input("Enter the Name - ")
if x in Bank["Name"] :
    print("Acc_No-\n",Bank["Acc_No"])
    print("Bal-\n",Bank["Bal"])
    print("Add-\n",Bank["Add"])
    print("Acc_typ-\n",Bank["Acc_typ"])
else :
    print("No such User")











































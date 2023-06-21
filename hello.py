import requests

# Python program to execute
# main directly
print ("Always executed")
 
# Making a GET request
r = requests.get('https://api.github.com/users/khalil1210')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)

if __name__ == "__main__":
    print ("Executed when invoked directly")

else:
    print ("Executed when imported")

   

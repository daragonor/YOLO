import os 
  
# Function to rename multiple files 
def main(): 
    i = 0
    file = open("001_list.txt","w+")
    for filename in os.listdir("Images/001"):
        os.path.abspath(filename)
        file.write("%s\n" % (os.path.abspath(filename)))
    file.close()

  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 

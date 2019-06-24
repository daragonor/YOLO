import os 
  
# Function to rename multiple files 
def main(): 
    i = 0
      
    for filename in os.listdir("Images/002"): 
        dst ="banana-" + str(i) + ".jpg"
        src ='Images/002/'+ filename 
        dst ='Images/002/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 

with open('Codingal.txt','w') as a file:
    file.write("Hi! i am penguin and i am 1yr old")
file.close() 
with open('Codingal.txt','r') as a file:   
    data = file.readlines()
    print("Words in the file are......")
    for line in data
    word = line.split()
    print(word)
    file.close()

file=input("enter file name")
store=open(file)
for i in file:
         forma=file.rstrip()
          if forma.startswith("From"):
               words=forma.split()
               print(words)
          else:
               continue
     

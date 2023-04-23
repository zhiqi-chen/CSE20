f=open('myfile','r')
content=f.read()
f.close()
words=content.split()
print(len(words))
words.sort()
for i in words:
    print(i)

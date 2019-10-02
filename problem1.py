strr=input()
ln=int(input())
s = list(map(str,strr.split()))
#999
out_app= []
word= ""
#www
word= word + s[0]
for i in range(1,len(s)):
    temp = word
    word = word + " " + s[i]
    if len(word) > ln:
        out_app.append(temp)
        #ti
        word= ""
        word = s[i]
        #kn
if ln < len(s[i]):
    print("null")
else:
    out_app.append(word)
    print(out_app)
    #a

user_input = input(1+1)
print(eval(user_input)) #a safe way to use eval()

user_in = "__import__ random.sys file"
print(eval(user_in)) #unsafe way to use eval()
#user_in could import possible malicious files into your code
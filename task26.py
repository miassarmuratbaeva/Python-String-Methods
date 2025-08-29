username=input()
clean=username.replace("-", "")
if clean.isalnum():
    print("True")
else:
    print("False")
list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
'''
def encrypt_code():
    name=input("enter the required name for encryption : ")
    shift=int(input("enter the shift number : "))
    new_name=""
    for i in name:
        if(i in list):
           position=list.index(i)
           new=(position+shift)%26
           new_name+=list[new]
        else:
            new_name+=str(i)
    print(f"the cipher text after encryption is {new_name}")
def decrypt_code():
    name = input("enter the required name for encryption : ").lower()
    shift = int(input("enter the shift number : "))
    new_name = ""
    for i in name:
        if (i in list):
            position = list.index(i)
            new = (position - shift) % 26
            new_name += list[new]
        else:
            new_name += str(i)
    print(f"the cipher text after decryption is {new_name}")
'''
def transformation(direction) :
    name = input(f"enter the required name for {direction}ion : ").lower()
    shift = int(input("enter the shift number : "))
    shift=shift%26
    new_name = ""
    if direction == 'decrypt':
         shift *= -1
    else:
        shift *= 1
    for i in name:
        if (i in list):
            position = list.index(i)
            new = (position + shift) % 26
            new_name += list[new]
        else:
            new_name += str(i)
    print(f"the cipher text after {direction}ion is {new_name}")

flag = True
while flag:
    asking = input("type encrypt for encryption and decrypt for decryption : ")
    transformation(asking)
    asking = input("do u want to type again : ")
    if asking == 'no':
        flag = False


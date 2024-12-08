from tkinter import *
import base64
#encryption
def encryptionFunction():
    message=text_input.get("1.0",END)
    key=key_input.get()
    combine=message+key
    var=combine.encode("utf-8")#binary
    print(var)
    encode_byte=base64.b64encode(var)#ascii
    print(encode_byte)
    encryption=encode_byte.decode("utf-8")
    result_output.delete(0,END)
    result_output.insert(0,encryption)
#decryption
def decryptionFunction():

    encryption=text_input.get("1.0",END)
    key=key_input.get()

    decode=base64.b64decode(encryption)
    message=decode.decode("utf-8")
    print(message)
    if message.endswith(key):
      real_message=message[:-len(key)]
      result_output.delete(0, END)
      result_output.insert(0, real_message)
    else:
        result_output.delete(0, END)
        result_output.insert(0, "invalid")

root=Tk()
root.geometry("1000x500")
root.title("Message encryption and decryption")
#input for message
Label(root,text="Enter the Message: ",font=("arial",20)).pack(pady=5)
text_input=Text(root,height=3,width=100)
text_input.pack(pady=5)
Label(root,text="Enter the Key: ",font=("arial",10)).pack(pady=5)
key_input=Entry(root,show="*",width=70)
key_input.pack(pady=5)
#button
Button(root,text="Encryption",command=encryptionFunction,bg="pink",font=("arial",10)).pack(pady=10)
Button(root,text="Decryption",command=decryptionFunction,bg="lightblue",font=("arial",10)).pack(pady=10)
#output
Label(root,text="Output: ",font=("arial",10)).pack(pady=5)
result_output=Entry(root,font=("arial",10),width=80)
result_output.pack(pady=5)
mainloop()
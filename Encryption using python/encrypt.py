from tkinter import messagebox, simpledialog, Tk

def is_even(number): 
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for index, letter in enumerate(message):
        if is_even(index):
            even_letters.append(letter)
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for index, letter in enumerate(message):
        if not is_even(index):
            odd_letters.append(letter)
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for index , _ in enumerate(message[:len(message)//2]):
        letter_list.append(odd_letters[index])
        letter_list.append(even_letters[index])
    new_message = ''.join(letter_list)
    return new_message
        
def get_task():
    task = simpledialog.askstring("Task", "Do you want to encrypt or decrypt")
    return task

def get_message():
    message = simpledialog.askstring("Message", "Enter the secret message")
    return message

root = Tk()
while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        encrypted = swap_letters(message)
        messagebox.showinfo("Ciphertext of the secret message is:", encrypted )
        
    elif task == 'decrypt':
        message = get_message()
        decrypted = swap_letters(message)
        messagebox.showinfo("Plaintext of the secret message is:", decrypted)
        
    else:
        break
root.mainloop()
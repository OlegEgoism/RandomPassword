from tkinter import *
import random
import clipboard

not_spc1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
not_spc2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
spc = ['!', "@", '#', '$', '%', '^', '&', '*', '(', ')', '+']


def password_generator():
    pg = Tk()
    pg.geometry("350x300")
    pg.title("Генератор паролей")
    pg.resizable(0, 0)

    def pass_gen():
        generated = ""
        choice_lst = []
        length = int(length_entry.get())
        for i in range(length):
            special = random.choice(spc)
            number = random.choice(not_spc1)
            non_special = random.choice(not_spc2)
            choice_lst.append(special)
            choice_lst.append(number)
            choice_lst.append(non_special)
            choice = random.choice(choice_lst)
            generated += str(choice)
        pass_entry.delete(0, END)
        pass_entry.insert(END, generated)

    def copy_password():
        password = pass_entry.get()
        clipboard.copy(password)

    empty = Label(pg, text="        ")
    empty.pack()
    pass_label = Label(pg, text="Генератор паролей", font=('bold', 14), fg="red")
    pass_label.pack()
    empty = Label(pg, text="         ")
    empty.pack()

    length_label = Label(pg, text="Длина пароля:")
    length_label.pack()
    length_entry = Entry(pg)
    length_entry.pack()

    empty = Label(pg, text="         ")
    empty.pack()

    pass_label = Label(pg, text="Сгенерированный пароль:")
    pass_label.pack()
    pass_entry = Entry(pg)
    pass_entry.pack()

    empty = Label(pg, text="         ")
    empty.pack()

    copy_btn = Button(pg, text="Копировать", font=5, fg="black", bg="light blue", command=copy_password)
    copy_btn.pack(pady=(10))
    pass_btn = Button(pg, text="Сгенерировать", font=5, fg="black", bg="yellow", command=pass_gen)
    pass_btn.pack()

    pg.mainloop()


if __name__ == '__main__':
    password_generator()



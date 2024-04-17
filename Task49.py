def ask_data():
    s_name = input("Введите фамилию: ")
    f_name = input("Введите имя: ")
    m_name = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    contact = {'second_name': s_name,
        'first_name': f_name,
        'middle_name': m_name,
        'phone_number': phone}
    return contact

def add_new_contact():
# if not check_data(contact):
# return False
    contact = ask_data()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        for value in contact.values():
            file.write(value, delimiter=';')
        file.write('\n')
# return True

def open_phonebook():
    title = ["Фамилия", "Имя", "Отчество", "Телефон"]
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print("\t\t".join(title))
        for line in file:
            print("\t\t".join(line.split(";")))
            # print(line.split(";"), end="\t")

def find_contact():
    # print(f"Поиск по:\n1 имени\n2 фамилии\n3 отчеству\n4 номеру\n0 выход")
    title = ["Фамилия", "Имя", "Отчество", "Телефон"]
    s_name = input("Введите фамилию: ")
    n_line = []
    # counter = 0
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print("\t\t".join(title))
        for counter, line in enumerate(file):
            line = line.split()
            # counter += 1
            if s_name in line[0]:
                n_line.append(counter)
                print("\t\t".join(line))
    print(n_line)
    return n_line

# def delete_contact():
# # s_name = input("Введите фамилию: ")
# # with open('phonebook.txt', 'w', encoding='utf-8') as file:
# print(find_contact())

def copy_contact():
    print ("\t")
    print ("Фамилия", "Имя", "Отчество", "Телефон")
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            print(f"{i + 1}: {line}", end="")
    line_number = int(input("\nВведите номер строки для копирования: ")) - 1
    if line_number < len(lines):
        target_file = f"copy_contact_{line_number + 1}.txt"
        with open(target_file, 'a', encoding='utf-8') as target:
            target.write(lines[line_number])
        print(f"Контакт из строки {line_number + 1} скопирован в {target_file}.")
    else:
        print("Неверный номер строки.")
        
        

def main():
    isStop = 1
    while isStop != 0:
        print(f"Выберете что хотите сделать:\n1 найти\n2 добавить\n3 удалить\n4 открыть всю книгу\n5 копирование\n0 выход")
        isStop = int(input(">"))
        if isStop == 1:
            find_contact()
        elif isStop == 2:
            add_new_contact()
        elif isStop == 4:
            open_phonebook()
        elif isStop == 5:
            copy_contact()
        input("Нажмите Enter чтобы продолжить")
main()
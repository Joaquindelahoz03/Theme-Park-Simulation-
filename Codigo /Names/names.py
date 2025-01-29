import random

class Names: 
    def __init__(self):
        name_chosen = self.read_txt_file(r'C:\Users\34610\OneDrive - CUNEF\PracticaFinal2.ICyJDH\Names\ESP_common_names.txt')
        if name_chosen:
            self.name = name_chosen

    def read_txt_file(self, file_name):
        names_list = []
        with open(file_name, 'r') as file:
            for line in file:
                names_list.append(line.strip())
        
        name = random.choice(names_list)
        return name

if __name__ == '__main__':
    name_instance = Names()
    print(name_instance.name)
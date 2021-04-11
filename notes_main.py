from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import json
app=QApplication([])

main_win = QWidget()
main_win.setWindowTitle('умные заметки')
#просто целая куча ошибок, связанных с неправильным написанием названий элементов
#будь повнимательнее!!!
field_text = QTextEdit()
list_netes = QListWidget()
list_tags = QListWidget()
field_tag = QLineEdit("введите тег...")

Button_add_note = QPushButton('добавить')
Button_del_note = QPushButton('удалить')
button_save_note = QPushButton('сохранить')

Button_add_tog = QPushButton('добавить тег')
Button_del_tog = QPushButton('удалить тег')


row1 = QHBoxLayout()
row1.addWidget(Button_add_note)
row1.addWidget(Button_del_note)
row1.addWidget(button_save_note)


row2 = QHBoxLayout()
row2.addWidget(Button_add_tog)
row2.addWidget(Button_del_tog)


col1 = QVBoxLayout()
col1.addWidget(list_netes)
col1.addLayout(row1)
col1.addWidget(list_tags) 
col1.addWidget(field_tag)
col1.addLayout(row2) #когда втыкаешь направляющие линии, то пишешь addLayout

col2=QVBoxLayout()

col2.addWidget(field_text)

layunt_main = QHBoxLayout()
layunt_main.addLayout(col1)
layunt_main.addLayout(col2)


notes={"гад оф во":{"текст":"hjfsdgvus","теги":["PS4"]}}
with open ('not_es.json', 'w') as file:
    json.dump(notes, file, sort_keys=True, ensure_ascii=False)




def add_note():
    note_name, ok=QInputDialog.getText(main_win, "Добавить заметку", "Название заметки: ")
    if ok and note_name!="":
        notes[note_name]={"текст":"", "теги":[]}
        list_netes.addItem(note_name)
        list_tags.addItems(notes[note_name]['теги'])


def save_note():
    if list_netes.selectedItems():
        key = list_netes.selectedItems()[0].text()
        notes[key]["текст"]=field_text.toPlainText()
        with open ('not_es.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)


def del_note():
    if list_netes.selectedItems():
        key = list_netes.selectedItems()[0].text()
        del notes[key]
        list_netes.clear()
        list_tags.clear()
        field_text.clear()
        list_netes.addItems(notes)
        with open('not_es.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

    
def add_tag():
    if list_netes.selectedItems():
        key = list_netes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
        with open("not_es.json", 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)


def del_tag():
    if list_tags.selectedItems():
        key=list_netes.selectedItems()[0].text()
        tag=list_tags.selectedItems()[0].text()
        notes[key]['теги'].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]['теги'])
        with open("not_es.json", 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)



def show_note():
    key = list_netes.selectedItems()[0].text()
    field_text.setText(notes[key]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[key]['теги'])


Button_add_note .clicked.connect(add_note)
button_save_note.clicked.connect(save_note)
list_netes.itemClicked.connect(show_note)
Button_del_note.clicked.connect(del_note)
Button_add_tog.clicked.connect(add_tag)
Button_del_tog.clicked.connect(del_tag)

with open('not_es.json', 'r') as file:
    notes = json.load(file)
list_netes.addItems(notes)


main_win.setLayout(layunt_main)
main_win.show()
app.exec()
#
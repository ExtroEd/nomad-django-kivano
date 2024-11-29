import tkinter as tk
from tkinter import messagebox
import pyperclip
import json


# Функция для форматирования текста в JSON
def format_text_for_json():
    # Получаем текст из поля ввода
    input_text = input_text_box.get("1.0", "end-1c")

    # Преобразуем текст в формат JSON
    escaped_text = json.dumps(input_text, ensure_ascii=False)

    # Убираем кавычки в начале и в конце
    if escaped_text.startswith('"') and escaped_text.endswith('"'):
        escaped_text = escaped_text[1:-1]

    # Вставляем отформатированный текст в поле вывода
    output_text_box.delete("1.0", "end")
    output_text_box.insert("1.0", escaped_text)


# Функция для обработки вставки текста
def paste_text():
    input_text_box.event_generate("<<Paste>>")


# Функция для очистки поля ввода
def clear_text():
    input_text_box.delete("1.0", "end")


# Функция для отображения информации о приложении
def show_info():
    messagebox.showinfo("Информация",
                        "Это приложение позволяет форматировать текст в формат JSON.\n"
                        "Для использования:\n"
                        "1. Вставьте или введите текст в поле для ввода.\n"
                        "2. Нажмите кнопку 'Format', чтобы преобразовать текст в формат JSON.\n"
                        "3. Кнопка 'Paste' вставит текст из буфера обмена.\n"
                        "4. Кнопка 'Clear' очистит поле ввода.")


# Функция для копирования отформатированного текста в буфер обмена
def copy_to_clipboard():
    formatted_text = output_text_box.get("1.0", "end-1c")
    pyperclip.copy(formatted_text)


# Создаем основное окно
root = tk.Tk()
root.title("Text Formatter for JSON")

# Устанавливаем шрифт и стили
root.option_add("*Font", "Helvetica 12")  # Используем современный шрифт
root.config(bg="#F4F4F4")

# Создаем фрейм для размещения элементов
frame = tk.Frame(root, bg="#F4F4F4")
frame.pack(padx=20, pady=20)

# Поле для ввода текста
input_label = tk.Label(frame, text="Введите текст:", bg="#F4F4F4", anchor="w",
                       font=("Helvetica", 12, "bold"))
input_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

input_text_box = tk.Text(frame, wrap="word", height=10, width=60,
                         font=("Helvetica", 12), bd=2, relief="solid",
                         bg="#FFFFFF", padx=10, pady=10)
input_text_box.grid(row=1, column=0, columnspan=3, pady=5)

# Кнопки для вставки, очистки и форматирования
paste_button = tk.Button(frame, text="Paste", command=paste_text, bg="#4CAF50",
                         fg="white", font=("Helvetica", 12, "bold"),
                         relief="flat", width=12)
paste_button.grid(row=2, column=0, pady=5, padx=5)

clear_button = tk.Button(frame, text="Clear", command=clear_text, bg="#F44336",
                         fg="white", font=("Helvetica", 12, "bold"),
                         relief="flat", width=12)
clear_button.grid(row=2, column=1, pady=5, padx=5)

format_button = tk.Button(frame, text="Format", command=format_text_for_json,
                          bg="#2196F3", fg="white",
                          font=("Helvetica", 12, "bold"), relief="flat",
                          width=12)
format_button.grid(row=2, column=2, pady=5, padx=5)

# Кнопка с вопросительным знаком (информация)
info_button = tk.Button(frame, text="?", command=show_info, bg="#FFC107",
                        fg="white", font=("Helvetica", 14, "bold"),
                        relief="flat", width=4)
info_button.grid(row=3, column=2, pady=5, padx=5)

# Кнопка для копирования текста
copy_button = tk.Button(frame, text="Copy", command=copy_to_clipboard,
                        bg="#8BC34A", fg="white",
                        font=("Helvetica", 12, "bold"), relief="flat",
                        width=12)
copy_button.grid(row=3, column=0, pady=5, padx=5)

# Поле для вывода отформатированного текста
output_label = tk.Label(frame, text="Отформатированный текст:", bg="#F4F4F4",
                        anchor="w", font=("Helvetica", 12, "bold"))
output_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)

output_text_box = tk.Text(frame, wrap="word", height=10, width=60,
                          font=("Helvetica", 12), bd=2, relief="solid",
                          bg="#F9F9F9", padx=10, pady=10)
output_text_box.grid(row=5, column=0, columnspan=3, pady=5)

# Запускаем главный цикл приложения
root.mainloop()

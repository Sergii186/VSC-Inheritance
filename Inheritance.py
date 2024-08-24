class Widget:
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y
    
    def print_info(self):
        print(f"Текст: {self.text}, Координати: ({self.x}, {self.y})")

class Button(Widget):
    def __init__(self, text, x, y, is_clicked=False):
        super().__init__(text, x, y)
        self.is_clicked = is_clicked
    
    def click(self):
        self.is_clicked = True
        print("Ви зареєстровані")
    
    def print_info(self):
        super().print_info()
        print(f"Натиснута: {self.is_clicked}")

# Створюємо екземпляр класу Button
button = Button("Реєстрація", 100, 100, is_clicked=False)

# Друкуємо загальну інформацію про кнопку
button.print_info()

# Запитуємо у користувача, чи хоче він зареєструватися
answer = input("Хочете зареєструватися? (так / ні): ").strip().lower()

# Обробляємо відповідь користувача
if answer == "так":
    button.click()
elif answer == "ні":
    print("А шкода!")
else:
    print("Невідома відповідь.")
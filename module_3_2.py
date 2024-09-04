def send_email(message, recipient, sender="university.help@gmail.com"):
    def recipient_check():
        if recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net'):
            return True

    def sender_check():
        if sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'):
            return True


    if '@' not in recipient or '@' not in sender:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif not recipient_check() or not sender_check():
        print(f"Невозможно отправитb письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print(f"Нельзя отправить письмо самому себе на адрес {recipient}")
    elif sender != "university.help@gmail.com":
        print(f"Нестандартный отправитель! Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")


# send_email(input("Введите сообщение: "), input("Введите адрес получателя: "))
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

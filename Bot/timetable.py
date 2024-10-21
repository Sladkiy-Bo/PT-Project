import xlrd
import datetime


class TimeTable:
    def __init__(self, path):
        self.workbook = xlrd.open_workbook(path)
        self.worksheet = self.workbook.sheet_by_index(0)
        self.day_raw_shift = [0, 11, 22, 33, 45, 55]

    def getclass(self, number_of_group):
        day = datetime.datetime.today().weekday()
        # day = 5 день для тестов

        if not(number_of_group.isdigit()) or int(number_of_group) <= 0 or int(number_of_group) > 9:
            return "Неправильно введен номер группы"
        if datetime.datetime.today().weekday() == 3:
            return "Расписание отсутствует. Сегодня у тебя английский"
        elif day == 6:
            return "В воскресенье пар нет"


        now_minutes = datetime.datetime.now().hour * 60 + datetime.datetime.now().minute
        # now_minutes = 560 количество минут для тестов
        number_of_group = int(number_of_group)
        col = 4 + (number_of_group - 1) * 3
        if number_of_group > 6:
            col += 6
        elif number_of_group > 3:
            col += 3

        raw = 11 + self.day_raw_shift[day]
        if now_minutes < 9 * 60 + 20:
            raw += 0
        elif now_minutes < 10 * 60 + 50:
            raw += 1
        elif now_minutes < 12 * 60 + 30:
            raw += 2
        elif now_minutes < 14 * 60 + 20:
            raw += 3
        elif now_minutes < 16 * 60:
            raw += 4
        elif now_minutes < 17 * 60 + 40:
            raw += 5
        elif now_minutes < 19 * 60 + 30:
            raw += 6
        elif now_minutes < 21 * 60:
            raw += 7
        else:
            return "Пар нет, отдыхай)"

        if self.worksheet.cell_value(raw, col) == "":
            return "В ближайшее время пары нет"
        return "Пара:\n" + self.worksheet.cell_value(raw, col) + "\nКабинет:\n" + self.worksheet.cell_value(raw, col + 1)


# создание класса для теста, указывайте номер группы, время в минутах и номер дня(нумерация с 0)
# print(TimeTable("timetable.xlsx").getclass('6'))

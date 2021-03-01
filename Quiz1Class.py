class Course:
    def __init__(self, title1, crn1, capacity1, code1):
        self.__title = title1
        self.__crn = crn1
        self.__capacity = capacity1
        self.__code = code1

    def get_title(self):
        return self.__title

    def get_crn(self):
        return self.__crn

    def get_capacity(self):
        return self.__capacity

    def get_code(self):
        return self.__code

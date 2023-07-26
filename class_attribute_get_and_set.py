class Year:
    def __init__(self, days, season):
        self.__days = days
        self.__season = season

    @property
    def get_days(self):
        return self.__days

    @set_days.setter
    def set_days(self, days):
        if days == 366 or days == 365:
            self.__days = days
        else:
            raise Exception('Некорректное значение')

    @property
    def get_season(self):
        return self.__season

    @set_season.setter
    def set_season(self, season):
        seasons = ['winter', 'spring', 'summer', 'autumn', 'fall']
        if season in seasons:
            self.__season = season
        else:
            raise Exception('Некорректное значение')



year = Year(365, 'summer')
year.set_days(300)
print(year)
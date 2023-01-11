from random import randint

import os
from django import setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bank.settings')
setup()

from banks.models import Bank, Branch, Client, Account

import datetime

class Populate:
    """
    Populate the db with some random stuff
    """
    banks = ('RABO', 'ING', )
    cities = ('Eindhoven', 'Geldrop', 'Veldhoven', )
    names = ('Nathan Wright', 'Frank Porter', 'Jack Flores', 'Darrel Walton', 'Marcella Mcbride', 'Charlie Steele',
             'Edna Brewer', 'Barbara Watts', 'Delbert Rodriguez', 'Della Bass', 'Kevin Obrien', 'Wilbur Alvarado',
             'Nina Byrd', 'Darla Valdez', 'Candice Fitzgerald', 'Marlene Morris', 'Georgia Perez', 'Glenda Dixon',
             'Patti Lewis', 'Kristi Mcgee', 'Betsy Bell', 'Karl Richards', 'Marlon Cobb', 'Terri Patterson',
             'Alberto Todd', 'Nelson Castro', 'Jermaine Chapman', 'Janet Klein', 'Garrett Jefferson', 'Ira Alexander',
             'William Hampton', 'Drew Wade', 'Casey Ramirez', 'Muriel Ferguson', 'Kari Mack', 'Rebecca Mann',
             'Carlos Bowers', 'Tony Burns', 'Jorge French', 'Thelma Ray', 'Guy Marshall', 'Adrienne Paul',
             'Dianna Reeves', 'Reginald Huff', 'Brandy Goodwin', 'Harriet Moreno', 'Aaron Douglas', 'Johnathan Terry',
             'Ernesto Tate', 'Flora Norman', 'Kristy Carlson', 'Charles Maldonado', 'Roy Swanson', 'Daryl Chavez',
             'Myrtle Harris', 'Lucas Boyd', 'Jacquelyn Henderson', 'Kara Leonard', 'Andy Morton', 'Lynette Foster')
    birthdates = ('Feb. 20, 1985',
                    'Sep. 6, 2003',
                    'Oct. 15, 1943',
                    'Nov. 15, 1944',
                    'Aug. 30, 1952',
                    'Jan. 21, 1950',
                    'May. 16, 1947',
                    'Dec. 29, 1968',
                    'Dec. 14, 1957',
                    'Oct. 20, 1979',)

    def fix_dates(self) -> None:
        """
        Fix funny american format to standard date format and add variation
        :return:
        """
        self.bdates = list()
        for iter in range(6):
            delta = datetime.timedelta(days=iter*5+1)
            for date in self.birthdates:
                self.bdates.append(datetime.datetime.strptime(date, '%b. %d, %Y')+delta)

    def populate(self) -> None:
        """
        Push 2 banks, 6 branches, 60 clients and 60 accounts
        :return: Nothing
        """
        self.fix_dates()
        inc = 2
        for bank in self.banks:
            if not Bank.objects.filter(name=bank).exists():
                b = Bank(name=bank, number=inc, country='NL')
                inc += 1
                b.save()
            else:
                b = Bank.objects.get(name=bank)

            for city in self.cities:
                if Branch.objects.filter(bank=b, city=city).exists():
                    br = Branch.objects.get(bank=b, city=city)
                else:
                    br = Branch(bank=b, city=city)
                    br.save()
                for name, bday in zip(self.names, self.bdates):
                    if Client.objects.filter(name=name).exists():
                        c = Client.objects.get(name=name)
                    else:
                        c = Client(name=name, birthday=bday)
                        c.save()
                        a = Account(client=c, branch=br, balance=randint(-1000, 10000),
                                    max_withdrawal=randint(1,5)*1000, max_debt=randint(1,5)*1000)
                        a.save()


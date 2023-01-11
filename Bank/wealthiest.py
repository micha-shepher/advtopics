import operator
from datetime import date, timedelta

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bank.settings')
django.setup()
from banks.models import Bank, Branch, Client, Account

class Wealthiest:
    age_group = (60, 40, 20, 0)
    def __init__(self):
        self.groups = dict(w60=[], w40=[], w20=[], w0=[])
        today = date.today()
        for cl in Client.objects.all():
            age_in_years = (today - cl.birthday).days / 365.25
            print(age_in_years)
            if  age_in_years > 60:
                self.groups['w60'].append(cl)
            elif age_in_years > 40:
                self.groups['w40'].append(cl)
            elif age_in_years > 20:
                self.groups['w20'].append(cl)
            else:
                self.groups['w0'].append(cl)

    def select_wealthiest_group(self):
        """
        sum the balance of each group and decide which group wins
        :return: name of the winning group
        """
        sums = dict(w60=0, w40=0, w20=0, w0=0)
        for ac in Account.objects.all():
            balance = ac.balance
            client = ac.client
            for group in 'w60,w40,w20,w0'.split(','):
                if client in self.groups[group]:
                    sums[group] += balance
                    break
        for i in sums:
            if len(self.groups[i]) > 0:
                sums[i] = sums[i] / len(self.groups[i])
        sorted_sums = sorted(sums.items(), key=operator.itemgetter(1), reverse=True)
        print(sorted_sums)
        print(f'the wealthiest group is {sorted_sums[0]}')



if __name__ == '__main__':
    w = Wealthiest()
    w.select_wealthiest_group()



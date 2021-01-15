from django.db import models

# Create your models here.

class People(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    residence = models.CharField(max_length = 30)

    def __str__(self):
        return f'{self.first_name} {self.last_name} from {self.residence}'
class Transactions(models.Model):
    id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(People, on_delete=models.CASCADE)
    debit = models.IntegerField()
    credit = models.IntegerField()
    # date = models.DateField()

    def __str__(self):
        amount = self.debit - self.credit
        if amount<0:
            return f'Amount of Rs. {abs(amount)} taken!'
        elif amount>0:
            return f'Amount of Rs. {amount} given!'
        else:
            return f'No dues!'

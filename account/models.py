from django.db import models

# Create your models here.
ACCOUNT_TYPE = (
    ('Savings', 'Savings'),
    ('Current', 'Current'),
    ('Corporate', 'Corporate')
)


class AccountUser(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    account_number = models.CharField(max_length=10, null=True, blank=True)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE, default='Savings')
    opening_branch = models.CharField(max_length=40)
    opening_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.account_number


class UserBiography(models.Model):
    account_user = models.OneToOneField(AccountUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    image = models.CharField(max_length=50)
    account_balance = models.FloatField()
    bvn = models.CharField(max_length=12)
    house_address = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class UserTransaction(models.Model):
    account_user = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=20, null=True, blank=True)
    transaction_type = models.CharField(max_length=10)
    transaction_date = models.DateTimeField(auto_now=True)
    amount = models.FloatField()
    category = models.CharField(max_length=15)

    def __str__(self):
        return self.transaction_id

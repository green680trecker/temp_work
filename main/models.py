from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=70)
    discount = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Мінімальна знижка — 1"),
            MaxValueValidator(100, message="Максимальна знижка — 100")
        ], default=0
    )
    phone_number = models.CharField(max_length=10, unique=True)
    date_birth = models.DateField()
    # password = models.CharField(max_length=128, null=False, blank=True)


    def __str__(self):
        return f"{self.name} {self.surname}"

class Staff(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=70)
    discount = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=10, unique=True)
    date_birth = models.DateField()

    def __str__(self):
        return f"{self.name} {self.surname}"

class PC(models.Model):
    status = models.BooleanField(default=True)
    os_type = models.CharField(max_length=50)

    def __str__(self):
        return f"PC {self.id} ({self.os_type})"

class Technician(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=70)
    pc_range = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

class SoftwareKit(models.Model):
    prog_names = models.CharField(max_length=255)
    prog_version = models.CharField(max_length=255)
    instal_date = models.DateField()
    update_date = models.DateField()

    def __str__(self):
        return f"{self.prog_names} {self.prog_version}"

class PCSoftware(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    software_kit = models.ForeignKey(SoftwareKit, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('pc', 'software_kit')

class PCTechnician(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    date_start = models.DateField()

    class Meta:
        unique_together = ('pc', 'technician')

class Session(models.Model):
    time_start = models.DateField()
    time_end = models.DateField()
    cost = models.IntegerField(
        validators=[
            MinValueValidator(10, message="Мінімальна вартість — 10"),
            MaxValueValidator(10000, message="Максимальна вартість — 10000")
        ]
    )
    fk_session_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    fk_session_pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    fk_session_staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

class Order(models.Model):
    creation_date = models.DateField()
    order_price = models.IntegerField(
        validators=[
            MinValueValidator(10, message="Мінімальна вартість — 10"),
            MaxValueValidator(100000, message="Максимальна вартість — 100000")
        ]
    )
    fk_order_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    fk_order_staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

class Menu(models.Model):
    category = models.CharField(max_length=70)
    appellation = models.CharField(max_length=255)
    cost = models.IntegerField(
        validators=[
            MinValueValidator(10, message="Мінімальна вартість — 10"),
            MaxValueValidator(100000, message="Максимальна вартість — 100000")
        ]
    )

    def __str__(self):
        return self.appellation

class MenuOrder(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    orders = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('menu', 'orders')

class Repair(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    price = models.IntegerField(
        validators=[
            MinValueValidator(10, message="Мінімальна вартість — 10"),
            MaxValueValidator(100000, message="Максимальна вартість — 100000")
        ]
    )
    techician = models.ForeignKey(Technician, on_delete=models.CASCADE)

from django.db import models




class Payment(models.Model):
     name = models.CharField(max_length=300, verbose_name="Nomi")
     amount = models.CharField(max_length=400, verbose_name="Narxi kiritish")
     order_id = models.CharField(max_length=1000)
     razorpay_payment_id = models.CharField(max_length=1000, blank=True)
     paid = models.BooleanField(default=False)


     def __str__(self):
         return self.name


     class Meta:
          verbose_name = "O'tkazma"





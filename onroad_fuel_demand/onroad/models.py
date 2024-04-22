from django.db import models

# Create your models here.

class tbl_login(models.Model):
    login_id=models.AutoField(primary_key=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    user_type=models.CharField(max_length=100)

class fuel_type(models.Model):
    fuel_type_id=models.AutoField(primary_key=100)
    fuel_type_name=models.CharField(max_length=100)
    fuel_type_rate=models.CharField(max_length=100)
    fuel_type_datetime=models.CharField(max_length=100)

class vehicles(models.Model):
    vehicles_id=models.AutoField(primary_key=100)
    vehicles_reg_no=models.CharField(max_length=100)
    vehicles_name=models.CharField(max_length=100)
    vehicles_capacity=models.CharField(max_length=100)
    fuel_type=models.ForeignKey(fuel_type,on_delete=models.CASCADE)

class users(models.Model):
    user_id=models.AutoField(primary_key=100)
    u_first_name=models.CharField(max_length=100)
    u_last_name=models.CharField(max_length=100)
    u_phone=models.CharField(max_length=100)  
    u_email=models.CharField(max_length=100)
    u_licence=models.CharField(max_length=100)
    u_latitude=models.CharField(max_length=100)
    u_longitude=models.CharField(max_length=100)
    login=models.ForeignKey(tbl_login,on_delete=models.CASCADE)
    
class drivers(models.Model):
    driver_id=models.AutoField(primary_key=100)
    login=models.ForeignKey(tbl_login,on_delete=models.CASCADE)
    d_first_name=models.CharField(max_length=100)
    d_last_name=models.CharField(max_length=100)
    d_phone=models.CharField(max_length=100)  
    d_email=models.CharField(max_length=100)
    d_licence=models.CharField(max_length=100)

class assign_vehicle(models.Model):
    assign_vehicle_id=models.AutoField(primary_key=100)
    vehicles=models.ForeignKey(vehicles,on_delete=models.CASCADE)
    driver=models.ForeignKey(drivers,on_delete=models.CASCADE)
    latitude=models.CharField(max_length=100)
    longitude=models.CharField(max_length=100)

class bookings(models.Model):
    booking_id=models.AutoField(primary_key=100)
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    fuel_type=models.ForeignKey(fuel_type,on_delete=models.CASCADE)
    driver=models.ForeignKey(drivers,on_delete=models.CASCADE)
    no_of_litter =models.CharField(max_length=100)
    booking_amount=models.CharField(max_length=100)
    booking_datetime=models.CharField(max_length=100)
    booking_status=models.CharField(max_length=100)

class payments(models.Model):
    payment_id=models.AutoField(primary_key=100)
    booking=models.ForeignKey(bookings,on_delete=models.CASCADE)
    payment_datetime=models.CharField(max_length=100)
    
class complaints(models.Model):
    complaint_id=models.AutoField(primary_key=100)
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
    com_date=models.CharField(max_length=100)
    
class rating(models.Model):
    rating_id=models.AutoField(primary_key=100)
    booking=models.ForeignKey(bookings,on_delete=models.CASCADE)
    rating=models.CharField(max_length=100)
    review=models.CharField(max_length=100)
    rating_datetime=models.CharField(max_length=100)
    
class stocks(models.Model):
    stock_id=models.AutoField(primary_key=100)
    vehicle=models.ForeignKey(vehicles,on_delete=models.CASCADE)
    fuel_stock=models.CharField(max_length=100)
    stock_datetime=models.CharField(max_length=100)




    
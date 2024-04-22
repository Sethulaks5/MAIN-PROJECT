from django.shortcuts import render
from onroad.models import *
from django.http import HttpResponse
from django.utils import timezone
import datetime
from onroad.models import payments, bookings, users, drivers,vehicles,assign_vehicle
import json
from django.http import JsonResponse
from django.db.models import F, FloatField
# from django.contrib.gis.geos import Point
# from django.contrib.gis.measure import Distance
# from django.contrib.gis.db.models.functions import Distance
# from .models import Location
from django.db import connection
from django.db.models import F, FloatField
from django.db.models.functions import ACos, Cos, Radians, Sin


# Create your views here.


def home(request):
    
    return render(request,'home.html')

def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        passw=request.POST['passw']
        q=tbl_login.objects.get(username=uname,password=passw)
        
        if q:
            request.session['id']=q.pk
            print(request.session['id'])
            if q.user_type=='admin':  
                return HttpResponse("<script>alert('login successfull');window.location='admin_home'</script>")
            elif q.user_type=='user':
                obj=users.objects.get(login_id=request.session['id'])
                if obj:
                    request.session['uid']=obj.pk
                    return HttpResponse("<script>alert('login successfull');window.location='admin_home'</script>")
    

                
        
    return render(request,'login1.html')

def viewreport(request):
    return render(request,'admin_view_report.html')

#_________________________________________________admin section____________________________________________
    
    
def admin_home(request):
    return render(request,'admin_home.html')

def admin_manage_fuel_type(request):
    if request.method=='POST':
        ftype=request.POST['ftype']
        frate=request.POST['frate']
        cur_time= timezone.now() 
        q=fuel_type(fuel_type_name=ftype,fuel_type_rate=frate,fuel_type_datetime=cur_time)
        q.save()
        
    q1=fuel_type.objects.all()
    return render(request,'admin_manage_fuel_type.html',{'viewfueltype':q1})

def update_fueltype(request,fuel_type_id):
    q=fuel_type.objects.get(fuel_type_id=fuel_type_id)
    if request.method=='POST':
        q.fuel_type_name=request.POST['ftype']
        q.fuel_type_rate=request.POST['frate']
        q.fuel_type_datetime= timezone.now() 
        q.save()
        return HttpResponse("<script>alert ('updated successfully');window.location='/admin_manage_fuel_type'</script>")
    return render(request,'admin_manage_fuel_type.html',{'upftype':q})

def delete_fuel_type(request,fuel_type_id):
    q=fuel_type.objects.get(fuel_type_id=fuel_type_id)
    q.delete()
    
    return HttpResponse("<script> alert ('successfully deleted'); window.location='/admin_manage_fuel_type'</script>")

def admin_manage_vehicle(request):
    if request.method=='POST':
        fuel=request.POST['fuel']
        regnum=request.POST['regnum']
        vehicle=request.POST['vehicle']
        capacity=request.POST['capacity']
        datetime=timezone.now()
        q=vehicles(fuel_type_id=int(fuel),vehicles_reg_no=regnum,vehicles_name=vehicle,vehicles_capacity=capacity)
        q.save()
        q1=stocks(fuel_stock='0',stock_datetime=datetime,vehicle=q)
        q1.save()
        
    q=vehicles.objects.all()
    q1=fuel_type.objects.all()
        
    return render(request,'admin_manage_vehicle.html',{'view_vehicle':q,'view_fuel_type':q1})

def update_vehicle(request,vehicles_id):
    q=vehicles.objects.get(vehicles_id=vehicles_id)
    # q1=fuel_type.objects.all()
    if request.method=='POST':
        # q.fuel_type_id=request.POST['fuel']
        q.vehicles_reg_no=request.POST['regnum']
        q.vehicles_name=request.POST['vehicle']
        q.vehicles_capacity=request.POST['capacity']
        q.save()
        
        return HttpResponse("<script>alert ('updated successfully');window.location='/admin_manage_vehicle'</script>")
    return render(request,'admin_manage_vehicle.html',{'updatevehicle':q})

def delete_vehicle(request,vehicles_id):
    q=vehicles.objects.get(vehicles_id=vehicles_id)
    q.delete()
    return HttpResponse("<script> alert ('successfully deleted'); window.location='/admin_manage_vehicle'</script>")

def admin_manage_drivers(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        email=request.POST['email']
        lnum=request.POST['lnum']
        unamer=request.POST['unamer']
        pwds=request.POST['pwds']
        q=tbl_login(user_type='driver',password=pwds,username=unamer)
        q.save()
        print("rtrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrjhbhjvgh",q)
        qr=drivers(login=q,d_first_name=fname,d_last_name=lname,d_phone=phone,d_email=email,d_licence=lnum)
        qr.save()
    q1=drivers.objects.all()
    return render(request,'admin_manage_drivers.html',{'viewdriver':q1})

def update_driver(request,login_id):
    
    return render (request,'admin_manage_drivers.html')

def delete_driver(request,login_id):
    q=drivers.objects.get(login_id=login_id)
    q.delete()
    q=tbl_login.objects.get(login_id=login_id)
    q.delete()
    return HttpResponse("<script> alert ('successfully deleted');window.location='/admin_manage_drivers'</script>")

def admin_assign_vehicle(request,driver_id,d_first_name):
    qr=drivers.objects.get(driver_id=driver_id)
    if qr:
        fn=qr.d_first_name
    q=vehicles.objects.all() 
    if request.method=='POST':
        vname=request.POST['vname']
        lati=request.POST['lati']
        longi=request.POST['longi']
        q1=assign_vehicle(driver_id=driver_id,vehicles_id=vname,latitude=lati,longitude=longi)
        q1.save()
    qrs=assign_vehicle.objects.filter(driver_id=driver_id)
    return render(request,'admin_assign_vehicle.html',{'viewvhicle':q,'qc':fn,'viewassignvehicle':qrs,'driver_id':qrs})

def admin_view_users(request):
    q=users.objects.all()
    return render(request,'admin_view_users.html',{'viewusers':q})

def admin_view_rating_ad_riew(request):
    q=rating.objects.all()
    return render(request,'admin_view_rating_ad_riew.html',{'viewrating':q})

def admin_view_booking(request):
    q=bookings.objects.all()
    return render(request,'admin_view_booking.html',{'viewbooking':q})
def admin_view_payment(request):
    q=payments.objects.all()
    # q = payments.objects.filter(booking__in=bookings.objects.all(),booking_id__user_id__in=users.objects.all(), booking_id__driver_id__in=drivers.objects.all())
    print("xxxxxxxxxxxxxx",q)
    return render(request, 'admin_view_payment.html', {'viewpayment': q})
# def admin_view_complaints(request):
#     data = {}
#     complaintz =complaints.objects.all()
#     if request.method=='POST':
#         reply=request.POST['reply']
#         complaints.reply =reply
#         complaints.save()
#     return render(request, 'admin_view_complaints.html', {'viewcomplaint': complaintz})


def admin_view_complaints(request):
    data = {}
    complaintz = complaints.objects.all()
    j=1
    if request.method=='POST':
        for complaint in complaintz:
            if 'submit'+str(j) in request.POST:
                reply = request.POST['reply'+str(j)]
                complaint.reply = reply
                complaint.save()
            j=j+1
                
    return render(request, 'admin_view_complaints.html', {'viewcomplaint': complaintz})



#--------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------#

    #                                    ANDROID                #
    
#--------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------#
    

def andro_login(request):
    data = []
    androusername = request.GET.get('androusername')
    andropassword = request.GET.get('andropassword')

    try:
        queryset = tbl_login.objects.filter(username=androusername, password=andropassword)
        for q in queryset:
            data.append({
                'login_id': q.login_id,
                'username': q.username,
                'password': q.password,
                'user_type':q.user_type
                # Add other fields you want to include in the response
            })
        if data:
            status = "success"
        else:
            status = "error"
            message = "Invalid credentials"
    except tbl_login.DoesNotExist:
        status = "error"
        message = "Invalid credentials"

    response = {
        'status': status,
        'data': data
    }
    print(data)

    if status == "error":
        response['message'] = message

    return JsonResponse(response)


def updatepasslocation(request):
    data = {}
    logi = request.GET.get('latti')
    longi = request.GET.get('longi')
    log_id = request.GET.get('logid')
    print("helooooooo")
    # print("helooooooo",logi)
        
    try:
        conductor = users.objects.get(login_id=log_id)
        # print("...................",bus.bus_name)
        conductor.latitude = logi
        conductor.longitude = longi
        conductor.save()
        data['message'] = "Location updated successfully."
        data['status'] = "success"
    except users.DoesNotExist:
        data['error'] = "Conductor with login_id '{}' does not exist.".format(log_id)
    return JsonResponse(data)


def userregister(request):
    data = []
    fname = request.GET.get('fname')
    lname = request.GET.get('lname')
    phone= request.GET.get('phone')
    email=request.GET.get('email')
    licence=request.GET.get('licence')
    latti=request.GET.get('lati')
    longi=request.GET.get('longi')
    uname=request.GET.get('uname')
    passw=request.GET.get('pass')
    try:
        querylog = tbl_login(username=uname, password=passw,user_type='user')
        querylog.save()
        queryuse= users(u_first_name=fname,u_last_name=lname,u_phone=phone,u_email=email,u_licence=licence,login=querylog,u_latitude=latti,u_longitude=longi)
        queryuse.save()
        if data:
                status = "success"
        else:
            status = "error"
            message = "Invalid credentials"
    except tbl_login.DoesNotExist:
        status = "error"
        message = "Invalid credentials"
    response = {
        'status': status,
        'data': data
    }

    if status == "error":
        response['message'] = message

    return JsonResponse(response)



def user_view_nearest_vehicle(request):
    data = {}
    data['data']=[]
    # query = "SELECT * FROM onroad_vehicles WHERE vehicles_id = %s"
    data['method'] = 'user_view_nearest_vehicle'
    lati = float(request.GET.get('lati'))
    logi = float(request.GET.get('logi'))
    print("latiii",lati)
    print("longoiii",logi)
    query="SELECT vehicles_id,driver_id,assign_vehicle_id,fuel_type_id,fuel_type_name,fuel_type_rate,vehicles_name,vehicles_reg_no,d_first_name,d_last_name,d_phone,d_email,latitude,longitude,(3959 * ACOS ( COS ( RADIANS('%s') ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS('%s') ) + SIN ( RADIANS('%s') ) * SIN( RADIANS(latitude ) ))) AS user_distance  FROM `onroad_vehicles` INNER JOIN `onroad_assign_vehicle` USING(`vehicles_id`) INNER JOIN `onroad_drivers` USING(`driver_id`) INNER JOIN `onroad_fuel_type` USING(`fuel_type_id`)  HAVING user_distance<31.068 "
    print("loction",query) 

    params = (lati,logi,lati)

    with connection.cursor() as cursor:
        cursor.execute(query, params)
        results = cursor.fetchall()
    print("__________________",results)

        # Process the results as needed
    for row in results:
        # Access row values using row[index]
        print(row[0])
        vehicledetails = {
                
                'vehicle_id': row[0],
                'driver_id': row[1],
                'assign_id': row[2],
                'type_id': row[3],
                'type_name': row[4],
                'rate': row[5],
                'vehicle': row[6],
                'regnum': row[7],
                'dname': row[8]+" "+row[9],
                'phone': row[10],
                'email': row[11],
                'latitude': row[12],
                'longitude': row[13],
            }
        print("vehllllllll",vehicledetails)
        data['data'].append(vehicledetails)
    data['status'] = 'success'
    return JsonResponse(data)



# def user_view_nearest_vehicle(request):
#     data = {}
#     data['data']=[]
#     # query = "SELECT * FROM onroad_vehicles WHERE vehicles_id = %s"
#     data['method'] = 'user_view_nearest_vehicle'
#     lati = float(request.GET.get('lati'))
#     logi = float(request.GET.get('logi'))
#     print("latiii",lati)
#     print("longoiii",logi)
#     query="SELECT vehicles_id,driver_id,assign_vehicle_id,fuel_type_id,fuel_type_name,fuel_type_rate,vehicles_name,vehicles_reg_no,d_first_name,d_last_name,d_phone,d_email,latitude,longitude,(3959 * ACOS ( COS ( RADIANS('%s') ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS('%s') ) + SIN ( RADIANS('%s') ) * SIN( RADIANS(latitude ) ))) AS user_distance  FROM `onroad_vehicles` INNER JOIN `onroad_assign_vehicle` USING(`vehicles_id`) INNER JOIN `onroad_drivers` USING(`driver_id`) INNER JOIN `onroad_fuel_type` USING(`fuel_type_id`)  HAVING user_distance<31.068 "
#     print("loction",query) 

#     params = (lati,logi,lati)

#     with connection.cursor() as cursor:
#         cursor.execute(query, params)
#         results = cursor.fetchall()
#     print("__________________",results)

#         # Process the results as needed
#     for row in results:
#         # Access row values using row[index]
#         print(row[0])
#         vehicledetails = {
                
#                 'vehicle_id': row[0],
#                 'driver_id': row[1],
#                 'assign_id': row[2],
#                 'type_id': row[3],
#                 'type_name': row[4],
#                 'rate': row[5],
#                 'vehicle': row[6],
#                 'regnum': row[7],
#                 'dname': row[8]+" "+row[9],
#                 'phone': row[10],
#                 'email': row[11],
#                 'latitude': row[12],
#                 'longitude': row[13],
                
                
#                 # 'd_latitude':booking.driver.d_latitude,
#                 # 'd_longitude':booking.driver.d_longitude,
                
#                 # Add other fields as needed
#             }
#         print("vehllllllll",vehicledetails)
#     # data['method'] = 'user_view_nearest_vehicle'
#     # lati = float(request.GET.get('lati'))
#     # logi = float(request.GET.get('logi'))
#     # distance_limit = 31.068

#     # user_location = Point(logi, lati)

#     # vehicle = assign_vehicle.objects.annotate(
#     #     user_distance=user_location.distance(Point('longitude', 'latitude')) * Distance.m,
#     #     dname=F('driver__d_first_name') + ' ' + F('driver__d_last_name')
#     # ).filter(user_distance__lt=distance_limit).order_by('-rank')

#     # if vehicle:
#     #     data['status'] = 'success'
#     #     data['data'] = list(vehicle.values())
#     data['status'] = 'success'
#     # valuessss{}.append(vehicledetails)
#     data['data'].append(vehicledetails)
#     print("============================================",data['data'].append(vehicledetails))
#     return JsonResponse(data)

def user_send_fuel_request(request):
    data = {}
    from datetime import datetime
    type_id = request.GET.get('type_id')
    driver = request.GET.get('driver')
    login_id = request.GET.get('login_id')
    no_titter = request.GET.get('no_titter')
    tot_rate = request.GET.get('tot_rate')
    ss=datetime.now()

    user = users.objects.get(login_id=login_id)

    booking = bookings(user=user, driver_id=driver, fuel_type_id=type_id, no_of_litter=no_titter, booking_amount=tot_rate,booking_datetime=ss, booking_status='Pending')
    booking.save()
    data['status'] = 'success'
    data['method'] = 'user_send_fuel_request'
    return JsonResponse(data)




  

# def user_view_nearest_vehicle(request):
#     # Retrieve the user's coordinates from the request (e.g., through a form)
#     latitude = float(request.GET.get('latitude'))
#     longitude = float(request.GET.get('longitude'))

#     # Define the search radius in kilometers
#     radius = 10

#     user_location = Point(longitude, latitude)
#     nearby_locations = Location.objects.filter(point__distance_lte=(user_location, Distance(km=radius))).order_by('point')

#     context = {
#         'user_latitude': latitude,
#         'user_longitude': longitude,
#         'nearby_locations': nearby_locations,
#     }

#     return render(request, 'user_view_nearest_vehicle.html', context)





def user_view_request(request):
    data = {}
    login_id = request.GET.get('login_id')
    
    try:
        user = users.objects.get(login_id=login_id)
        booking_list = bookings.objects.filter(user_id=user.user_id)
        print("bookinglistxxxxxxxxxx",booking_list)
        data['status'] = 'success'
        data['data'] = []
        
        for booking in booking_list:
            v_id = assign_vehicle.objects.filter(driver_id=booking.driver_id)
            booking_data = {
                
                'booking_id': booking.booking_id,
                'booking_amount': booking.booking_amount,
                'booking_datetime': booking.booking_datetime,
                'booking_status': booking.booking_status,
                'no_of_litter': booking.no_of_litter,
                'fuel_type_name': booking.fuel_type.fuel_type_name,
                'fuel_type_rate': booking.fuel_type.fuel_type_rate,
                'vehicles_id': v_id[0].vehicles_id,
                'driver_id':booking.driver_id,
                'd_first_name':booking.driver.d_first_name,
                'd_last_name':booking.driver.d_last_name,
                'd_phone':booking.driver.d_phone,
                'vehicles_name':v_id[0].vehicles.vehicles_name,
                'vehicles_reg_no':v_id[0].vehicles.vehicles_reg_no,
                # 'd_latitude':booking.driver.d_latitude,
                # 'd_longitude':booking.driver.d_longitude,
                
                # Add other fields as needed
            }
            print("bookingdata__________________________",booking_data)
        print(type(booking_data))    
        data['data'].append(booking_data)
        print("data____________________",data)
            
    except drivers.DoesNotExist:
        data['status'] = 'failed'
        
    data['method'] = 'user_view_request'
    return JsonResponse(data)


def user_payment(request):
    data = {}
    data['method'] = 'user_payment'
    booking_id = request.GET.get('booking_id')
    now = timezone.localtime(timezone.now())
    date = now.date()
    
    try:
        booking = bookings.objects.get(booking_id=booking_id)
        booking.booking_status = 'Paid'
        booking.save()
        
        payment = payments(booking_id=booking_id,payment_datetime=date)
        payment.save()
        
        data['status'] = 'success'
        
    except bookings.DoesNotExist:
        data['status'] = 'failed'
        
    return JsonResponse(data)

def user_rate_fuel(request):
    data = {}
    data['method'] = 'user_rate_fuel'
    booking_id = request.GET.get('booking_id')
    ratings = request.GET.get('rating')
    review = request.GET.get('review')
    from datetime import datetime
    ss=datetime.now()
    
    try:
        existing_rating = rating.objects.get(booking_id=booking_id)
        existing_rating.rating = ratings
        existing_rating.review = review
        existing_rating.rating_datetime = ss
        existing_rating.save()
        data['status'] = 'success'
        
    except rating.DoesNotExist:
        new_rating = rating(booking_id=booking_id, rating=ratings, rating_datetime=ss,review=review)
        new_rating.save()
        data['status'] = 'success'
    return JsonResponse(data)

def user_view_rated(request):
    data = {}
    data['method'] = 'user_view_rated'
    booking_id = request.GET.get('booking_id')
    
    try:
        rated_data = rating.objects.get(booking_id=booking_id)
        data['status'] = 'success'
        data['data'] = rated_data.rating
        data['data1'] = rated_data.rating_datetime
        
    except rating.DoesNotExist:
        data['status'] = 'failed'
    return JsonResponse(data)


def user_send_complaints(request):
    data = {}
    login_id = request.GET.get('loginid')
    complaints_text = request.GET.get('complaints')
    now = timezone.localtime(timezone.now())
    date = now.date()

    try:
        user = users.objects.get(login_id=login_id)
        complaint = complaints(user=user, complaint=complaints_text, reply='pending',com_date=date)
        complaint.save()
        data['status'] = 'success'
    except users.DoesNotExist:
        data['status'] = 'failed'

    data['method'] = 'user_send_complaints'
    return JsonResponse(data)
def user_view_complaints(request):
    data = {}
    login_id = request.GET.get('loginid')

    try:
        user = users.objects.get(login_id=login_id)
        user_complaints = complaints.objects.filter(user=user).values()
        data['status'] = 'success'
        data['data'] = list(user_complaints)
    except users.DoesNotExist:
        data['status'] = 'failed'

    data['method'] = 'user_view_complaints'
    return JsonResponse(data)



# def viewspinner(request):
#     data = {}
#     typefuel = fuel_type.objects.all()
#     data['method'] = 'viewspinner'
#     return JsonResponse(data)



def viewspinner(request):
    data = {}
    fuel_type_list = []  # List to store fuel type data
    
    # Get all fuel types from the database
    typefuel = fuel_type.objects.all()
    print(typefuel)
    
    if typefuel.exists():
        for fuel in typefuel:
            # Append relevant data from each fuel type object to the list
            fuel_type_list.append({
                'id': fuel.fuel_type_id,
                'name': fuel.fuel_type_name,
                'rate': fuel.fuel_type_rate,
                # Add other fields as needed
            })
        
        data['status'] = 'success'
        data['data'] = fuel_type_list  # Include the list of fuel types in the response
    else:
        data['status'] = 'failed'

    data['method'] = 'viewspinner'
    return JsonResponse(data)







#_________________________________________________driver module____________________________________________________#
#___________________________________________

def driver_view_assigned_vehicle(request):
    data = {}
    login_id = request.GET.get('login_id')
    
    
    # queryset = assign_vehicle.objects.filter(driver__login_id=login_id).select_related('vehicles', 'driver__login')
    queryset = assign_vehicle.objects.filter(driver__login_id=login_id)
    result =[]
    
    print(queryset)
    for assign_vehicle_obj in queryset:
        vehicle = assign_vehicle_obj.vehicles
        driver = assign_vehicle_obj.driver
        stockss =  stocks.objects.filter(vehicle__vehicles_id=assign_vehicle_obj.vehicles_id)
        result.append({
            'assign_vehicle_id': assign_vehicle_obj.assign_vehicle_id,
            'vehicle_id': vehicle.vehicles_id,
            'vehicles_reg_no': vehicle.vehicles_reg_no,
            'vehicles_name': vehicle.vehicles_name,
            'vehicles_capacity': vehicle.vehicles_capacity,
            'driver_first_name': driver.d_first_name,
            'driver_last_name': driver.d_last_name,
            'driver_phone': driver.d_phone,
            'driver_email': driver.d_email,
            'fuel_stock': stockss[0].fuel_stock,
        })
    print(result)
    if result:
        data['status'] = 'success'
        data['data'] = result
    else:
        data['status'] = 'failed'
    data['method'] = 'driver_view_assigned_vehicle'

    return JsonResponse(data, safe=False)

def driver_update_stock(request):
    data = {}
    stock_fuel = request.GET.get('stockss')
    vehicle_idss = request.GET.get('vehicle_ids')
    print(vehicle_idss)

    r = stocks.objects.get(vehicle_id=vehicle_idss)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",r)
    r.fuel_stock = int(r.fuel_stock)+int(stock_fuel)
    r.save()
    data['status'] = 'success'
    data['method'] = 'driver_update_stock'
    return JsonResponse(data)



def driver_view_stock(request):
    data = {}
    vehicle_id = request.GET.get('vehicle_id')

    stockss = stocks.objects.filter(vehicle_id=vehicle_id).values_list('fuel_stock', flat=True)

    if stockss.exists():
        stock_list = list(stockss)
        data['status'] = 'success'
        data['stock'] = stockss[0]
    else:
        data['status'] = 'failed'

    data['method'] = 'driver_view_stock'
    return JsonResponse(data)

def driver_view_request(request):
    data = {}
    login_id = request.GET.get('login_id')
    
    try:
        driver = drivers.objects.get(login_id=login_id)
        booking_list = bookings.objects.filter(driver_id=driver.driver_id)
        v_id = assign_vehicle.objects.filter(driver_id=driver.driver_id)
        data['status'] = 'success'
        data['data'] = []
        
        for booking in booking_list:
            booking_data = {
                'booking_id': booking.booking_id,
                'booking_amount': booking.booking_amount,
                'booking_datetime': booking.booking_datetime,
                'booking_status': booking.booking_status,
                'no_of_litter': booking.no_of_litter,
                'fuel_type_name': booking.fuel_type.fuel_type_name,
                'fuel_type_rate': booking.fuel_type.fuel_type_rate,
                'vehicles_id': v_id[0].vehicles_id,
                'user_id':booking.user_id,
                'u_first_name':booking.user.u_first_name,
                'u_phone':booking.user.u_phone,
                'u_latitude':booking.user.u_latitude,
                'u_longitude':booking.user.u_longitude,
                
                # Add other fields as needed
            }
            data['data'].append(booking_data)
            
    except drivers.DoesNotExist:
        data['status'] = 'failed'
        
    data['method'] = 'driver_view_request'
    return JsonResponse(data)

def driver_accept_request(request):
    data = {}
    booking_id = request.GET.get('booking_ids')

    try:
        booking = bookings.objects.get(booking_id=booking_id)
        booking.booking_status = 'Accept'
        booking.save()
        data['status'] = 'success'
    except bookings.DoesNotExist:
        data['status'] = 'failed'

    data['method'] = 'driver_accept_request'
    return JsonResponse(data)


def driver_accept_payment(request):
    data = {}
    booking_id = request.GET.get('booking_ids')
    vehicle_id = request.GET.get('vehicle_ids')
    no_of_liters = request.GET.get('nooflitters')

    try:
        stock_obj = stocks.objects.get(vehicle_id=vehicle_id)
        stock_obj.fuel_stock = int(stock_obj.fuel_stock) - int(no_of_liters)
        stock_obj.save()

        booking = bookings.objects.get(booking_id=booking_id)
        booking.booking_status = 'Payment Received'
        booking.save()

        data['status'] = 'success'
    except (stocks.DoesNotExist, bookings.DoesNotExist):
        data['status'] = 'failed'

    data['method'] = 'driver_accept_payment'
    return JsonResponse(data)


def driver_view_ratings(request):
    data = {}
    booking_id = request.GET.get('booking_id')

    try:
        result = rating.objects.filter(booking_id=booking_id)
        if result.exists():
            data['status'] = 'success'
            data['data'] = result[0].rating
            data['data1'] = result[0].rating_datetime
        else:
            data['status'] = 'failed'
    except rating.DoesNotExist:
        data['status'] = 'failed'

    data['method'] = 'driver_view_ratings'
    return JsonResponse(data)



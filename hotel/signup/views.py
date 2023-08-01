from django.shortcuts import render
from signup.models import Signup
from signup.models import Search
from django.http import HttpResponseRedirect
import mysql.connector 
con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="sohan")
mycursor= con.cursor()


# Create your views here.

def home(request):
    return render(request,'home.html')

def sign(request):
    if request.method=="POST":
        name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST["cpassword"]
        if cpassword==password:
            lst=Signup()
            lst.suser=name
            lst.semail=email
            lst.spassword=password
            lst.save()
            return HttpResponseRedirect('/login/')
        else:
            return render(request,'Signup1.html')
       # return render(request,'login.html')
        
    else:
        return render(request,'Signup1.html')
    
name='abc'
def login(request):
    global name
    
    if request.method=="POST":
        name=request.POST['username']
        password=request.POST['password']
        post=Signup.objects.get(suser=name)
        d3={}
        d3['passwrong']='Wrong Username or Password'
        k=[]
        k.append(d3)
        if (post):
            if (post.spassword==password):
                return HttpResponseRedirect('/home/')
            else:
                
                return render(request,"login.html",{'pay2':k})
                '''lst=Login()
        lst.user=username
        lst.pwd=password
    
        lst.save()
        return render(request,'offers.html')'''
    else:
        
        return render(request,"login.html")

#creating a function to check the city entered by user and displaying hotels#
p=[]
city ='abc'
order = ''

def dicti():
    global order
    global p
    global city
    global arrival
    global departure
    p=[]
    mycursor.execute("use sohan")
    
    mycursor.execute("select * from hotels where hotelcity ='"+city+"' order by "+order+"")
    print("select * from hotels where hotelcity ='"+city+"'odate<='"+arrival+"'cdate>='"+departure+"' order by "+order+"")
    r = mycursor.fetchall()
    l=list(r)
    
    

    for i in l:
        
        d={}
        d['city']=i[1]
        d['name']=i[2]
        d['rating']=i[3]
        d['hotelid']=i[0]
        p.append(d)
    
departure='bcd'
arrival='pdf'   
order='abc'     
def search(request):
    global city
    global order
    global departure
    global arrival
    global order
    if request.method=="POST":
        city=request.POST['city']
        guests=request.POST['guests']
        arrival=request.POST['arrival']
        departure=request.POST['departure']
        order=request.POST['preference']
        if order == 'Price':
            order = "price asc"
        else:
            order = "ratings desc"
        lst2=Search()
        lst2.lcity=city
        lst2.lguests=guests
        lst2.larrival=arrival
        lst2.ldeparture=departure
        lst2.save()
        dicti()
        return render(request,"result1.html",{'pay_l':p})
    
    
    
    else:
        return render(request,"search.html")

#Priting out a confirmation page.

hotelid='shg'
hotelname='agd'
l=[]

def dict2():
    global name
    global hotelid
    global arrival
    global departure
    global l
    global hotelname
    l=[]
    d1={}
    d1['name']=name
    d1['arrival']=arrival
    d1['departure']=departure
    d1['hotel']=hotelname
    l.append(d1)


def book(request):
    global hotelid
    global hotelname
    if request.method=="POST":
        hotelid=request.POST['hotid']
        hotelname=request.POST['bname']
        dict2()
    mycursor.execute("insert into history values('{}','{}','{}','{}')".format(hotelid,arrival,departure,name))
    con.commit()

    return render(request,'confirm1.html',{'pay':l})

'''def account(request):
    global hotelid
    global hotelname
    global name
    global arrival
    global departure

    mycursor.execute("use sohan")'''
    
        

        
        











    

    
    
    
    







    

    






    
        
        
        
        
        
        
        
    
    
    

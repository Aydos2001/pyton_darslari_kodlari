#1-amelyat
#san=int(input("Jup san kiritin' >>> "))
#if san%2==0 and san>0:
    #print("Raxmet siz kiritken san dizimge alindi")
#else:
    #print("Bul san jup emes")
    
#2-amelyat

#jas=int(input("Jasin'iz neshede >>> "))
#if jas<7 or jas>60:
    #narx="bepul"
#elif jas<18:
    #narx="10000 som"
#else:
    #narx="20000 som"
#print(f"Sizga muzeyga kirish {narx}")
 
#3-amelyat
#san1=float(input("1-sandi kiritin' "))
#san2=float(input("2-sandi kiritin' "))
#if san1==san2:
    #manis="Sanlar bir birine ten"
#elif san1>=san2:
    #manis=f"{san1} sani {san2} saninan u'lken"
#elif san1<=san2:
    #manis=f"{san1} sani {san2} saninan kishi"
#print(manis)

#4-amelyat
   
#onimler=["asqabaq","geshir","piyatz","kapusta","qiyaqar","pamidor","karop","qawin"]
#savat=[]
#for n in range(int(input("Neshe onim almaqshisiz "))):
    #savat.append(input(f"{n+1}-onim  ").lower())
#for zat in savat:
    #if zat in onimler:
        #print(f"{zat} Bul onim dizimge jazildi")
    #else:
        #print(f"{zat} Keshiresiz bul onim bizlerde joq eken")
        
#5-amilyat

#print("5 turli o'nim kiritin'" )
#onimler=["asqabaq","geshir","piyatz","kapusta","qiyar","pamidor","karop","qawin"]
#savat=[]
#bar=[]
#joq=[]
#for n in range(5):
    #savat.append(input(f"{n+1}-onim > "))
#for zat in savat:
    #if zat in onimler:
        #bar.append(zat)
    #else:
        #joq.append(zat)

#if joq:
    #print(f"Siz kiritken onimlerden to'mendegi onimler joq ")
    #for k in joq:
        #print(k)
    
#else:
    #print(f"Siz kiritken onimlerdin bari bar")

#6-amelyat

#paydalaniwshilar=["aydos","arslan","nurik","ways","muxit"]
#login=input("Login kiritin'. > ")
#log=login.lower()
#if log in paydalaniwshilar:
    #print(f"{login} Bul login bant")
#else:
     #print(f"Xosh kelipsiz {login}" )
    
#7-amelyat
    
san=int(input("Qalegen putin san kiritin. > "))
bolinedi=[]
for n in range(2,11):
    if san%n==0:
        bolinedi.append(n)
if len(bolinedi)<1:
    print("Bul san 2 den 10 aralig'indag'i sanlardin' esh birine bolinbeydi")
else:
    print(f"{san} sani tomendegi sanlarg'a qaldiqsiz bo'linedi\n{bolinedi}")
        
   
    
        
        
    


    
    
    
 

    


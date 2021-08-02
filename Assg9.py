n=int(input('no.of tickets:'))
sn=int(input('no.of senoior citizens(age above 65):'))  #sn=no.of snior citizens
an=int(input('no.of adults(age between 18-64):'))       #an=no.of adults
mn=int(input('no.of minors(age between 5-17):'))        #mn=no.of minors
cn=int(input('no.of child(age below 0-5):'))           #cn=no.of child
print()
p=200
Price=p*n
print('actual tickets price:',Price)
if sn<=n or an<=n or mn<=n or cn<=n :
    print('we have a discount of 20% on senior citizens')
    sdp=sn*p*(20/100) #sdp=discount on senior citizen
    snp=(sn*p)-sdp     #snp=price senior citizen tickets
    print('senior citizens ticket price:',snp)
    if an<=n :
        print("we don't have discount on adults")
        anp=an*p   #anp=price of adult tickets
        print('adults ticket price:',anp)
        if mn<=n :
            print('we have a discount of 50% on minor')
            mdp=mn*p*(50/100)  #mdp=discount on minors
            mnp=(mn*p)-mdp     #mnp=price of minors
            print('minor ticket price:',mnp)
            if cn<=n :
                print("we don't have a price on child")
                cnp=p*0         #cnp=price of child
                print('child ticket price:',cnp)
total_price=snp+anp+mnp+cnp
print('final price of all tickets:',total_price)

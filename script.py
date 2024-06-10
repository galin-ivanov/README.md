
# задача 1

customer_account_balance = 0
customer_number = int(input (" въведи вашия клиентски номер"))
customer_plan = input ("моля въведи избрания от вас абонаментен план. ENTRY.PREMIUM.ULTRA")
customer_age = int(input("моля въведи вашата възраст"))

# задача2

# 301
is_customer_number_valid = (customer_number >= 50 and customer_number <= 300)
if not is_customer_number_valid:
    print("клиентския номер е невалиден")
    exit()

if customer_number < 50 or customer_number > 300:
    print("клиентския номер е невалиден")

if not (customer_number >= 50 and customer_number <= 300):
    print("клиентския номер е невалиден")

customer_plan = input("въведете вашия предпочитан план")

is_customer_plan_valid = (
                             (customer_plan == "ENTRY") or 
                             (customer_plan == "PREMIUM") or 
                             (customer_plan == "ULTRA") or 
                             (customer_plan == "NO"))

if not is_customer_number_valid:
    print("Абонаментния план е невалиден")
    exit()

customer_age = int(input("въведете вашата възраст"))

#  задача 3



is_customer_teletekst = (
                             (customer_number % 2 == 0 ) and 
                             (customer_plan == "ENTRY") and 
                             (customer_age >= 60 ))
if is_customer_teletekst:
    print("добре дошли в телетекст")




is_customer_adul = ((customer_age >= 18) or (customer_age <= 60) or (customer_plan == ("PREMIUM")) )
if is_customer_adul:
    print("Канали за възрастни")

is_customer_fotbool = ( 
                               (customer_number == "NO") and  
                               (customer_age == 36) and  
                               (customer_plan == "ULTRA")
                                (customer_number == 100 or
                                 customer_number == 200 or
                                 customer_number == 300) )
 
                               
if is_customer_fotbool:
    print("Футболни канали ")

is_customer_anime = (   
                        (customer_age <= 18 ) and 
                        (customer_number < 100 ) and 
                        (customer_plan == "ULTRA"))
if is_customer_anime:
    print(" Анимационни канали ")

print("вашите услуги са:")
if is_customer_teletekst:
    print(" - телетекст")
if is_customer_adul:
    print("канали за възрастни")
if is_customer_anime:
    print("анимационни канали")
if is_customer_fotbool:
    print("футболни канали")
    
has_service =  ( 
                     is_customer_adul or 
                     is_customer_anime or 
                     is_customer_teletekst or 
                     is_customer_fotbool)


 if has_service:
    print("ВАШИТЕ УСЛУГИ СА")
    if is_customer_teletekst:
        print("телетекст")
    if is_customer_adul:
        print("канали за възрастни")
    if is_customer_anime:
        print("анимационни канали")
    if is_customer_fotbool:
        print("футболни канали")

    else:
        print("няма услуги")


# задача 4
 
 if is_customer_teletekst:
    if customer_age == 70
    print("ПРЕМИУМ Телетекст.")
 else:
    print("телетекст")
    if is_customer_adul:
        customer_plan == "ULTRA"
        print("Ултра канали за възрастни")
    else:
        print(" - канали за възрастни")
    if is_customer_fotbool:
        if customer_number == 200 or customer_number == 30:
            print("МЕГА футбол")
        else:
            print("Футбол")
        if is_customer_anime:
            if customer_age == 18:
                
                print(" ПРЕМИУМ анимационни канали")
            else:
                print("анимационни канали")

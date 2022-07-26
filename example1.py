ogrenciler= {}
while True:

    number = input('please insert student number:')
    name = input('name:')
    surName= input('surname:')
    phone= input('phone:')

    ogrenciler[number]= {
        'name': name,
        'surname': surName,
        'phone':phone
    }
    if number == "q":
        break



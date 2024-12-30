transportation_mode = int(input('Tell me where you want to go in KM : '))
if transportation_mode < 3:
    print('\"walk\"')

elif 2 < transportation_mode < 16:
    print('\"use bike\"')

elif transportation_mode >= 16:
      print('\"Use car\"')
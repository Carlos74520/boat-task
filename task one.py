badtime = True
badtiming = True
slotting = True
boatrenting =True
times = [10,10.5,11,11.5,12,12.5,13,13.5,14,14.5,15,15.5,16,16.5,17]
boat1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
boat2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
boat3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
boat4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
boat5 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
boat6 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
boat7 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
boat8 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
boat9 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
boat10 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
onehour = 20
halfhour = 12
oddtiming = 0
timing = 0
time = 0
while boatrenting:
    while True:
        try:
            time = float(input('please input what time you want a boat (make sure half past it ".5")'))
            if time <= 17 and time >=10:
                break
        except:
             print('that isnt valid time')
                        
'''   select = int(input('pick your prefered rowing boat, boat: 1 , 2, 3 ,4 , 5 , 6 , 7 , 8 , 9 , 10?'))
    if select == 1:
        boatselect = boat1

    elif select == 2:
        boatselect = boat2

    elif select == 3:
        boatselect = boat3

    elif select == 4:
        boatselect = boat4

    elif select == 5:
        boatselect = boat5

    elif select == 6:
        boatselect = boat6
                  
    elif select == 7:
        boatselect = boat7

    elif select == 8:
        boatselect = boat8

    elif select == 9:
        boatselect = boat9

    elif select == 10:
        boatselect = boat10

    else:
        print('that boat does not exist')'''
    

while badtiming:
        
        timing = float(input('What time do you want to return the boat at?'))
        if timing > 17.5:
            print('you cannot hire a boat for longer than 7 hours')
        elif boat1[times.index(timing)] != 0:
            print('no boat is available, please come back later')
        else:
            badtiming = False


        
        

   # if timing%2 == 0 or timing%2 == 1:   #     #v this is to find time slot
   #     slot1 = times.index(time)
        #print (slot1)
   #     while slotting:
   #         boat1[slot1] = onehour/2
   #         slot1 = slot1 + 1
   #         if times[slot1] == timing:
  #             print(boat1)
  #              slotting = False

    if (timing - time)%2 == 0 or (timing - time)%2 == 1:
        slot1 = times.index(time)
        while slotting:
            boat1[slot1] = onehour/2
            slot1 = slot1 + 1
            if times[slot1] == timing:
                print(boat1)
                slotting = False
    elif timing - time == 0.5:
        slot1 = times.index(time)
        boat1[slot1] = halfhour
        print(boat1)
    else:
        slot1 = times.index(time)
        while slotting:
            oddtiming = timing - 0.5
            boat1[slot1] = onehour/2
            slot1 = slot1 + 1
            if times[slot1] == timing - 0.5:
                boat1[slot1] = halfhour
                print(boat1)
                slotting = False
    print('the price is:', sum(boat1), 'Thank you for hiring a boat!')
    repeatb1 = input('would you like to hire the boat again?')
    if repeatb1 == 'yes':
        badtime = True
        badtiming = True
    else:
        boatrenting = False

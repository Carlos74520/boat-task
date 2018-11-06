times = [10,10.5,11,11.5,12,12.5,13,13.5,14,14.5,15,15.5,16,16.5,17]
boat1 = [2,2,4,6,7,8,9,6,1,3,5,3,4,1,2] #[2,2,4,6,7,8,9,6,1,3,5,3,4,1,2] <- to check for unability
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
addhalfhour = False
selection = True
processing = True
main = True
check = True

while main:
    while selection:
        while True:
            try:
                boatchoice = int(input('what boat do you want to chose?'))
                timerented = float(input('what time do you want to take out the boat?'))
                timeback = float(input('what time do you want to return the boat?'))
                if timerented <= 17 and timerented >= 10 and timeback > 10 and timeback < 17 and boatchoice in range(1,11):
                    #print("asdf")
                    
                    break
                else:
                    print('thats no valid time or boat')
            except:
                print('thats a fancy number you got')
           
    #check if half hour is needed by checking indexes of time in & out

        timerequired = times.index(timeback) - times.index(timerented)
        if timerequired%2 !=0:
            addhalfhour = True
        processing = True
        check = True


    #append if the boat is availble
        while processing:
            if boatchoice == 1:
                for i in range(timerequired):
                    if boat1[times.index(timerented)+ i] != 0:
                        check = False
                if check == False:
                        print('the boat is unavailble at this time')
                        selection = True
                        processing = False
                if addhalfhour == True:
                    print('halfhour is true')
                    for i in range(timerequired):
                        boat1[times.index(timerented) + i] = onehour/2
                        if i == timerequired - 1:
                            boat1[(times.index(timerented) + i) + 1] = halfhour
                            print(boat1)
                            addhalfhour == False
                    else:
                        print('inside adding full hours')
                        for i in range(timerequired):
                            boat1[times.index(timerented) + i] = onehour/2
                            boat1[times.index(timerented) + timerequired] = onehour/2
                            print(boat1)

        if boatchoice == 2:
            for i in range(timerequired):
                if boat1[times.index(timerented)+ i] != 0:
                    check = False
                if check == False:
                    print('the boat is unavailble at this time')
                    selection = True
                    processing = False
            if addhalfhour == True:
                print('halfhour is true')
                for i in range(timerequired):
                    boat2[times.index(timerented) + i] = onehour/2
                    if i == timerequired - 1:
                        boat2[(times.index(timerented) + i) + 1] = halfhour
                        print(boat2)
                        addhalfhour == False
            else:
                print('inside adding full hours')
                for i in range(timerequired):
                    boat2[times.index(timerented) + i] = onehour/2
                boat2[times.index(timerented) + timerequired] = onehour/2
                print(boat2)


            if i == timerequired - 1:
                boat2[(times.index(timerented) + i) + 1] = halfhour
                print(boat2)
                addhalfhour == False
    else:
        print('inside adding full hours')
        for i in range(timerequired):
            boat2[times.index(timerented) + i] = onehour/2
        boat2[times.index(timerented) + timerequired] = onehour/2
        print(boat2)
print("blabla")

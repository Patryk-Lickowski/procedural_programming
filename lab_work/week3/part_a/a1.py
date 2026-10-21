def weather_check():

    weather = str(input("What's the weather like today?: "))

    if weather.lower() == 'sunny':
        print('Great! Go for a walk.')
    elif weather.lower() == 'rainy':
        print('Take an umbrella.')
    elif weather.lower() == 'snowy':
        print('Stay warm and be careful!')
    else:
        print("I don't recognise that weather")
        weather_check();



weather_check()
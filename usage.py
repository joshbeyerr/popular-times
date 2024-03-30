import time

from reWrite import get, translate
from datetime import datetime


def return_time_wait(barr):
    try:
        main = {}
        for x in barr['popular_times']:
            dictt = {}
            for i in range(len(x['data'])):
                dictt[translate(i)] = x['data'][i]

            main[x['name']] = dictt

        return main
    except:
        print("Error with bar {}".format(barr))
        return main


def get_all(dic):
    all = {}
    for i in dic:
        bar = get(i)
        data = return_time_wait(bar)
        all[i] = data
    print(all)

b = get("Cowboys Ranch")
print(b)
quit()


get_all([
    'Joe Kools',
    "Delilah's",
    "McCabes",
    "The Ceeps",
    "Molly Blooms",
    "Barney's",
    "El Furniture Warehouse",
    "Chuck's Roadhouse Bar & Grill 650 Richmond St",
    "Jack's London",
    "Winks Eatery",
    "Cowboys Ranch",
    "Lost Love Social"
])

quit()


print(main)


quit()


def get_time():
    current_time = datetime.now().time()

    # Format and print the current time
    formatted_time = current_time.strftime("%H:%M")
    return formatted_time


with open('data', 'a') as f:
    while True:
        bar = get("Delilah's")
        print(bar)
        curr_pop = bar['current_popularity']
        time_now = get_time()

        f.write("Del\ilah's popularity at {} - {}\n".format(str(time_now), str(curr_pop)))
        print("Monitoring Delilah's - {}".format(curr_pop))
        time.sleep(600)

quit()

main = {}

for x in bar['time_wait']:
    dictt = {}
    for i in range(len(x['data'])):
        dictt[translate(i)] = x['data'][i]

    main[x['name']] = dictt

print(main)

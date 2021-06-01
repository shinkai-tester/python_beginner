from datetime import *

events_full = []
full_command = input().split(', ')


def append_event(com):
    event_date = []
    if len(com) == 3:
        event = com[1]
        dat = com[2]
        event_date.append(event)
        event_date.append(dat)
        events_full.append(event_date)


def how_much_time(events):
    for one in events:
        curr_event = one[0]
        dat = one[1]
        new_format = '%Y-%m-%d'
        datum = datetime.strptime(dat, '%d %m %Y').strftime(new_format)
        datum = datetime.strptime(datum, new_format).date()
        diff = datum - date.today()
        days = diff.days
        if days < 0:
            continue
        else:
            print('До события %s осталось %d дней.' % (curr_event, days))


while full_command[0] != 'Stop':
    if full_command[0] == 'Внести событие':
        append_event(full_command)
    elif full_command[0] == 'Сколько времени осталось?':
        how_much_time(events_full)

    full_command = input().split(', ')

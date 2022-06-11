from pywebio import *
from pywebio.output import *
from pywebio.input import *


def main():
    pass


def mixed_in_s02(value):
    try:
        value == int(value)
    except ValueError:
        [put_buttons(['A'], onclick=put_text)]

def moving_decimal(num):
    num /= 1000.
    return num

def calculating_sO2(desired_sO2, gallons):
    bring_up = desired_sO2 * 3.785 * gallons / 0.57
    return round(bring_up, 2)

def temperature_convertor(temperature):
    celsius = int(((temperature - 32) * 5) / 9)
    return celsius


def main():
    '''
    An interactive web app that takes user's name
    and output hello <username> on the webpage
    '''
    put_markdown("# **Leony's Inventory Manegmant System**")

    year_of_grape = input("The year grape picked", placeholder="Year picked",
                          required=True)
    put_text("The year: %s" % year_of_grape)

    ava = input("Name of AVA:", placeholder="Whats the AVA name?", required=True)
    put_text("Name of AVA: %s" % ava)

    name_of_vine = input("The name of vine", placeholder="Name of vine", required=True)
    put_text("Name of vine: %s" % name_of_vine)

    date_grapes_picked = input('Date picked:', placeholder='The exact date grapes were picked',
                               required=True)
    put_text('The date Grapes were picked on:  %s' % date_grapes_picked)

    tons = input("How many lbs were picked?", type=NUMBER, placeholder="Weight of product", required=True)
    put_text("Total weight: %slbs" % tons)

    cost = input('Cost', type=NUMBER, placeholder='What was the cost of purchase?', required=True)
    put_text("Cost was: $%s" % cost)

    date_crushed = input("Date grapes crushed:", placeholder="Date grapes crushed", required=True)
    gallons = input("Gallons produced after crushing", type=NUMBER, placeholder="Gallons produced", required=True)

    with put_collapse("Date crushed | Weight | Crushed Gallons"):
        put_table([
            ['Date crushed', 'Weight Crushed', 'Gallons'],
            [put_text("%s" % date_crushed), put_text("%slbs" % tons), put_text("%s" % gallons)]
        ])

    s02 = input(placeholder='Added sO2')
    with put_collapse('Added sO2'):
        put_table([
            ['sO2 in grams'],
            [put_text(s02)],
        ])

    temperature = input("Temperature in Farenhite", type=NUMBER, placeholder="Temperature of wine", required=True)

    with put_collapse("Temperature"):
        put_table([
            ["F", "C"],
            [put_text(temperature), put_text(temperature_convertor(temperature))]
        ])

if __name__ == "__main__":
    main()
from datetime import datetime, timedelta


class Time:
    def __init__(self):
        self.time = datetime(2022, 10, 10, 6, 30, 0)

    def detail(self):
        global time
        time += timedelta(minutes=30)

    def quick_shower(self):
        global time
        time += timedelta(minutes=10)

    def snooze(self):
        global time
        time += timedelta(minutes=60)

    def play_cod(self):
        global time
        time += timedelta(minutes=20)

    def cod_play_again(self):  # if we play multiple games
        global time
        time += timedelta(minutes=80)

    def shave(self):
        global time
        time += timedelta(minutes=15)

    def brush(self):
        global time
        time += timedelta(minutes=5)

    def no_brush_lecture(self):
        global time
        time += timedelta(minutes=15)

    def floss_brush(self):
        global time
        time += timedelta(minutes=10)

    def no_brush(self):
        global time
        time += timedelta(minutes=0)

    def banana_poptart_oatmeal(self):
        global time
        time += timedelta(minutes=5)

    def toast(self):
        global time
        time += timedelta(minutes=30)

    def bacon_eggs(self):
        global time
        time += timedelta(minutes=30)

    def pancakes_french_toast(self):
        global time
        time += timedelta(minutes=20)

    def sprinkler_went_off(self):
        global time
        time += timedelta(minutes=90)

    def get_in(self):
        global time
        time += timedelta(minutes=45)

    def another_uber(self):
        global time
        time += timedelta(minutes=25)

    def missed_stop(self):
        global time
        time += timedelta(minutes=45)

    def stand(self):
        global time
        time += timedelta(minutes=30)

    def ride_bike(self):
        global time
        time += timedelta(minutes=45)

    def walk_to_bus_stop(self):
        global time
        time += timedelta(minutes=10)

    def missed_stop(self):
        global time
        time += timedelta(minutes=45)

    def dry_inside(self):
        global time
        time += timedelta(minutes=20)

    def dry_outside(self):
        global time
        time += timedelta(minutes=45)


if __name__ == "__main__":
    Time

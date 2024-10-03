from autos.abs_auto import AbsAuto


class ChevyVolt(AbsAuto):
    def start(self):
        print("Starting Chevy Volt")

    def stop(self):
        print("Stopping Chevy Volt")
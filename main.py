from auto_factory import AutoFactory

factory = AutoFactory()
for carname in "ChevyVolt", "JeepCheroke", "BMW":
    car = factory.create_instance(carname)
    car.start()
    car.stop()
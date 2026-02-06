class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    def run(self, velocity, distance):
        if 0 <= velocity <= 200:
            self.velocity = velocity
        else:
            print("Velocity must be between 0 and 200")
            return

        fuel_needed = distance / 10
        if self.fuelRate >= fuel_needed:
            self.fuelRate -= fuel_needed
            self.stop(0)
        else:
            remain_distance = distance - (self.fuelRate * 10)
            self.fuelRate = 0
            self.stop(remain_distance)

    def stop(self, remain_distance):
        self.velocity = 0
        if remain_distance > 0:
            print(f"remain distance, {remain_distance} km left.")
        else:
            print("you arrived the destintation")

class employee : 
    def __init__(self,id,car,email,salary,distanceToWork,mood) : 
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
        self.mood = mood

    def work (self,hours) :
        if hours == 8 :
            return self.mood == "Happy"
        if hours < 8 :
            return self.mood == "tired"
        if hours > 8 :
            return self.mood == "lazy"
        
    def drive(self, distance, velocity):
         self.car.run(velocity, distance) 
         if velocity > 200 :
             self.velocity = 200

    def refuel(self, gasAmount=100): 
        self.car.fuelRate += gasAmount 
        if self.car.fuelRate > 100: 
            self.car.fuelRate = 100 
            
    ##def send_mail(self, to, subject, body): 
      ##  print(f"Sending mail to {to}\nSubject: {subject}\nBody: {body}")
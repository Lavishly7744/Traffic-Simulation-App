import random
import time

class TrafficLight:
    def __init__(self):
        self.state = 'red'  # Initial state is red

    def change_light(self):
        if self.state == 'red':
            self.state = 'green'
        elif self.state == 'green':
            self.state = 'yellow'
        elif self.state == 'yellow':
            self.state = 'red'

    def current_light(self):
        return self.state


class Intersection:
    def __init__(self):
        self.light = TrafficLight()
        self.queue = []  # Cars waiting at the intersection

    def car_arrives(self):
        car_id = len(self.queue) + 1
        self.queue.append(car_id)
        print(f"Car {car_id} has arrived at the intersection.")

    def car_leaves(self):
        if self.queue:
            car_id = self.queue.pop(0)
            print(f"Car {car_id} has passed through the intersection.")
        else:
            print("No cars waiting at the intersection.")

    def simulate_traffic(self, cycles):
        for _ in range(cycles):
            print(f"\nTraffic light is {self.light.current_light()}.")

            if self.light.current_light() == 'green':
                # Cars pass through the intersection
                self.car_leaves()
            else:
                # Cars arrive when the light is red or yellow
                if random.random() < 0.7:  # 70% chance of a car arriving
                    self.car_arrives()

            # Change the light and wait for a second
            self.light.change_light()
            time.sleep(1)

if __name__ == "__main__":
    intersection = Intersection()

    # Simulate 10 traffic light cycles
    intersection.simulate_traffic(10)

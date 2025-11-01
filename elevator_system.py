from enum import Enum
import time

class ElevatorState(Enum):
    IDLE = "idle"
    MOVING_UP = "moving_up"
    MOVING_DOWN = "moving_down"
    DOORS_OPEN = "doors_open"

class Direction(Enum):
    UP = "up"
    DOWN = "down"

class FloorRequest:
    def __init__(self, floor, direction):
        self.floor = floor
        self.direction = direction

class Elevator:
    def __init__(self, eid, total_floors):
        self.id = eid
        self.current_floor = 1
        self.state = ElevatorState.IDLE
        self.total_floors = total_floors

    def distance(self, target_floor):
        return abs(self.current_floor - target_floor)

    def move_to(self, target_floor):
        if self.state != ElevatorState.IDLE:
            print(f"Elevator {self.id} cannot move. Current state: {self.state.value}")
            return 
        
        if target_floor == self.current_floor:
            self.state = ElevatorState.DOORS_OPEN
        elif target_floor > self.current_floor:
            self.state = ElevatorState.MOVING_UP
        else:
            self.state = ElevatorState.MOVING_DOWN

        print(f"Elevator {self.id} moving from {self.current_floor} to {target_floor}")
        time.sleep(4)
        print(f"Doors Opening: Lift-{self.id}")
        time.sleep(2)
        self.current_floor = target_floor
        self.state = ElevatorState.DOORS_OPEN
        print(f"Elevator {self.id} doors opened at floor {target_floor}")
        time.sleep(1)
        
    def close_doors(self):
        if self.state == ElevatorState.DOORS_OPEN:
            self.state = ElevatorState.IDLE
            print(f"Elevator {self.id} doors closing...")
            time.sleep(2)
            print(f"Elevator {self.id} doors closed at floor {self.current_floor}")
        else:
            print(f"Elevator {self.id} doors are not open.")

class ElevatorController:
    def __init__(self, num_elevators, total_floors):
        self.elevators = [Elevator(i + 1, total_floors) for i in range(num_elevators)]

    def request_elevator(self, eid, floor, direction):
        elevator = next((e for e in self.elevators if e.id == eid), None)
        if not elevator:
            print(f"No elevator with id {eid}")
            return
        print(f"\n[Controller] Received request for Elevator {eid} to floor {floor} ({direction.value})")
        print(f"Elevator {eid} current floor: {elevator.current_floor}, state: {elevator.state.value}")
        elevator.move_to(floor)

    def show_status(self):
        for e in self.elevators:
            print(f"Elevator {e.id}: Floor {e.current_floor}, State: {e.state.value}")

    def close_doors(self, eid):
        for e in self.elevators:
            if e.id == eid:
                e.close_doors()
                return
        print(f"No elevator with id {eid}")

def main():
    number_of_elevators = int(input("Enter Desired Number of Elevators: "))
    total_number_of_floors = int(input("Enter total number of floors in the building: "))
    print("\n=== Elevator Management System — Simulation ===")
    print("Aim: Simulate multiple elevators, handle floor requests, assign the optimal elevator, and track states.")
    print("You can request an elevator from any floor and specify desired direction (up/down).")
    print("\nAvailable commands:")
    print("  request <elevator_id> <floor> <up/down>   -> Request a specific elevator (e.g. request 1 5 up)")
    print("  status                                   -> Show status of all elevators")
    print("  close <elevator_id>                      -> Close doors of an elevator (e.g. close 1)")
    print("  quit                                     -> Exit the simulation\n")
    controller = ElevatorController(num_elevators=number_of_elevators, total_floors=total_number_of_floors)

    while True:
        cmd = input("\nEnter command: ").lower().split()
        if not cmd: continue

        if cmd[0] == "quit":
            print("System shutting down...")
            break
        elif cmd[0] == "status":
            controller.show_status()
        elif cmd[0] == "request" and len(cmd) == 4:
            try:
                eid = int(cmd[1])
                floor = int(cmd[2])
                direction = Direction.UP if cmd[3] == "up" else Direction.DOWN
                if floor < 1 or floor > total_number_of_floors:
                    print(f"Invalid floor: {floor}. Please enter a floor between 1 and {total_number_of_floors}.")
                    continue
                controller.request_elevator(eid, floor, direction)
            except:
                print("Invalid command. Try again.")
        elif cmd[0] == "close" and len(cmd) == 2:
            try:
                eid = int(cmd[1])
                controller.close_doors(eid)
            except:
                print("Invalid elevator id.")
        else:
            print("Invalid command. Use: request <elevator_id> <floor> <up/down>, status, close <elevator_id>")

if __name__ == "__main__":
    main()

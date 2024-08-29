#Task 2
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1

    def get_participant_count(self):
        print(f"Total Participants: {self.participant_count}")

event = Event("Birthday", "2/2/25")

while True:
    choice = input("Enter action (add, count, or quit): ").lower()
    if choice == 'quit':
        break
    elif choice == 'add':
            event.add_participant()
            print("Participant added.")
            continue
    elif choice == 'count':
        event.get_participant_count()
        continue
    else:
        print("Invalid input.")
        continue
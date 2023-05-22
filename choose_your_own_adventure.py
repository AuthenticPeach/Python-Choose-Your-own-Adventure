def main():
    print("Welcome to the 'Choose Your Own Adventure' game!")
    while True:
        print("You wake up in a mysterious forest.")
        print("What do you do?")
        print("1. Walk deeper into the forest.")
        print("2. Climb a tree to get a better view.")
        print("3. Shout for help.")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            print("You decide to walk deeper into the forest.")
            print("You encounter a river blocking your path.")
            print("What do you do?")
            print("1. Swim across the river.")
            print("2. Look for a bridge.")
            print("3. Follow the riverbank.")

            choice = input("Enter your choice (1, 2, or 3): ")

            if choice == "1":
                print("You swim across the river and reach the other side safely.")
                print("Congratulations! You made it through the forest.")
            elif choice == "2":
                print("You search for a bridge but couldn't find one.")
                print("Unfortunately, you got lost in the forest.")
                print("Game over!")
            elif choice == "3":
                print("You decide to follow the riverbank.")
                print("After a while, you discover a hidden path that leads you out of the forest.")
                print("Congratulations! You made it through the forest.")
            else:
                print("Invalid choice. Game over!")

        elif choice == "2":
            print("You climb a tree to get a better view.")
            print("From above, you spot a small cottage in the distance.")
            print("What do you do?")
            print("1. Head towards the cottage.")
            print("2. Stay on the tree and observe.")

            choice = input("Enter your choice (1 or 2): ")

            if choice == "1":
                print("You make your way towards the cottage.")
                print("As you approach, the door opens, and a kind old woman greets you.")
                print("Congratulations! You made it to safety.")
            elif choice == "2":
                print("You decide to stay on the tree and observe.")
                print("While observing, you notice a pack of wolves heading your way.")
                print("You quickly climb down, but it's too late.")
                print("Game over!")
            else:
                print("Invalid choice. Game over!")

        elif choice == "3":
            print("You shout for help.")
            print("A rescue team hears your cries and comes to your aid.")
            print("Congratulations! You made it to safety.")

        else:
            print("Invalid choice. Game over!")

        play_again = input("Do you want to play again? (yes or no): ")
        if play_again.lower() != "yes":
            break

# Start the game
main()

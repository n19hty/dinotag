dinosaurs = {"TRex": "unfrozen", "Velociraptor": "unfrozen", "Stegosaurus": "unfrozen", "Brachiosaurus": "unfrozen", "Pterodactyl": "unfrozen", "Ankylosaurus": "unfrozen", "Triceratops": "unfrozen", "Spinosaurus": "unfrozen", "Allosaurus": "unfrozen", "Diplodocus": "unfrozen"}

players = []

it_player = None

outcomes = {"You succeed in tagging the dinosaur!": 1, "The dinosaur evades your tag!": 0, "You accidentally got stuck in oil!": 0, "Stepped on a Mushroom and slipped!": 0}

scoreboard = {}





def add_player(name):
  players.append(name)

def decide_who_is_it(players):
    import random
    return random.choice(players)

def tag(it_player, dinosaurs):
    import random
    unfrozen_dinosaurs = [dino for dino, status in dinosaurs.items() if status == "unfrozen"]
    if not unfrozen_dinosaurs:
        return None
    tagged_dinosaur = random.choice(unfrozen_dinosaurs)
    outcome = random.choices(list(outcomes.keys()))[0]
    print(f"{it_player} attempts to tag {tagged_dinosaur}... {outcome}")
    if outcome == "You succeed in tagging the dinosaur!":
        dinosaurs[tagged_dinosaur] = "frozen"
    return tagged_dinosaur

def main():
    # Add Test Players
    player_to_add = input("Enter your name: ")

    add_player(player_to_add)

    # select who is "it"

    it_player = decide_who_is_it(players)
    print(f"{it_player} is 'it'!")

    # you have a few turns to tag dinosaurs
    turns = 10
    taken_turns = 0
    for turn in range(turns):
        if taken_turns >= turns:
            print("No more turns left! Game over.")
            break
        
        menu = input("Press Enter to take your turn...")
        print(menu)


        tagged_dinosaur = tag(it_player, dinosaurs)

        if tagged_dinosaur:
            print(f"{it_player} tagged {tagged_dinosaur}! Dinosaurs left unfrozen: {[dino for dino, status in dinosaurs.items() if status == 'unfrozen']}")
            taken_turns += 1
            print(f"Turns taken: {taken_turns}/{turns}")
        else:
            print("All dinosaurs are frozen! Game over.")
            break


if __name__ == "__main__":
    main()

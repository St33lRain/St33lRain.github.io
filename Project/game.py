import random
import time
import sys

# OG speed value was 0.05
def text_speed(s, speed=0.05):
    """Controls the speed of the output text for a more 'game-ish' feel.
        :param s: text to print in the terminal
        :param speed: delay in seconds between characters. Lower = faster. Defaults to 0.05.
    """
    for char in s:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def paranoia():
    text_speed("GET PSYCHED!!!")

# its fuckin dice, dickhead
def rng():
    """Literally just dice but 10."""
    roll_result = random.randint(1, 10)
    text_speed(f"you rolled a {roll_result}")
    return roll_result

def damage(roll_result, player_health):
    """Gives damage depending on how accurate their shot was (rng dependent).
    Returns (new_health, damage_taken, is_dead).
    """
    if roll_result <= 5:
        damage_taken = 3
    elif roll_result <= 9:
        damage_taken = 6
    else:
        # roll_result == 10: instant death handled by caller
        return player_health, 0, True

    new_health = max(0, player_health - damage_taken)
    return new_health, damage_taken, (new_health == 0)

def restart():
    """Prompts the player to restart after dying. Returns True to restart, False to quit."""
    while True:
        yes_no = input("You were killed. Try again? (yes/no): ").strip().lower()
        if yes_no in ['yes', 'y']:
            return True
        elif yes_no in ['no', 'n']:
            text_speed("thanks for playing my game <3")
            return False
        else:
            text_speed("Invalid input, please input 'yes' or 'no'.")

# "The world chico, and everything in it."
rooms = {
    'start': {
        'description': (
            'A status bar blinks on the computer in front of you: "90% Transfer In Progress". '
            'It sits on a fancy but oddly misplaced desk. Your HK P30L sits on the desk itching for action. '
            'You hear the thumping of boots storming towards the door.'
        ),
        'actions': ['shoot', 'wait', 'north', 'south', 'east', 'west']
    },
    'north': {
        'description': (
            'To your north you see the thick red oak front door to the target\'s apartment leading into the cramped hallway. '
            '"A killbox for sure."'
        ),
        'actions': ['shoot', 'wait', 'south', 'east', 'west']
    },
    'south': {
        'description': (
            'Behind you lies a big window. You\'re 3 stories high — the window drops into the alley. '
            '"A calculated risk but definitely an option."'
        ),
        'actions': ['jump_from_window', 'shoot', 'wait', 'north', 'east', 'west']
    },
    'east': {
        'description': (
            'To the east is another door. Closed, but thin enough to kick in.'
        ),
        'actions': ['kick_door', 'shoot', 'wait', 'north', 'south', 'west']
    },
    'west': {
        'description': (
            'To the west is the living room — deep green sectional, 65-inch OLED TV, surround sound. '
            '"I need this at my place."'
        ),
        'actions': ['flashbang', 'shoot', 'wait', 'north', 'south', 'east']
    },
    'alley': {
        'description': (
            'A dumpster full of smelly trash sits to your right. '
            'To your left, silver trash cans line the length of the building. '
            'You\'re dead center. "I gotta move quick."'
        ),
        'actions': ['wait', 'go_right', 'go_left', 'hide_in_dumpster']
    },
    'hallway': {
        'description': (
            'You\'re in the hallway, standing over the bodies. You contemplate your next move.'
        ),
        'actions': ['re-kit', 'outside']
    },
    'outside': {
        'description': (
            'You push through the building\'s front door into the cold night air. '
            'The street is quiet — for now.'
        ),
        'actions': ['go_left', 'go_right', 'wait']
    }
}

def die_and_maybe_restart():
    """Handles death. Returns the room to restart in, or None to quit."""
    if restart():
        return 'start'
    return None

def main():
    current_room = 'start'
    player_health = 10
    has_rifle = False
    is_kitted = False

    paranoia()

    while True:
        room = rooms[current_room]
        text_speed(rooms[current_room]['description'])
        text_speed("\nPossible actions:")
        for action in room['actions']:
            text_speed(f"  - {action}")

        player_action = input("\nwhats the move? ").strip().lower()

        # ──────────────────────────────────────────────
        # START ROOM
        # ──────────────────────────────────────────────
        if current_room == 'start':

            if player_action == 'shoot':
                text_speed("You grab your pistol from the desk and aim at the door.")
                text_speed("'C'mon motherfuckers, come and get it.' you say intensely.")
                text_speed("The boots in the hallway fall silent. A heavy thunk lands against the door.")
                text_speed("A blast blows the door clean off its hinges. The 1st man in the stack makes entry —")
                text_speed("you fire a pair of shots, catching him in the neck and mouth. He drops instantly.")
                text_speed("The second man pies to the opposite side of the doorway, MCX at the ready.")
                text_speed("The 3rd man lobs a flashbang into the room.")
                text_speed("It detonates. You go blind and deaf.")
                text_speed("You feel a burning in your chest. Cold hard floor on your cheek.")
                text_speed("Vision clears just enough to see a pool of blood. YOUR blood. YOU HAVE DIED.")
                result = die_and_maybe_restart()
                if result is None:
                    break
                current_room = result
                player_health = 10
                has_rifle = False
                is_kitted = False

            elif player_action == 'wait':
                text_speed("The transfer completes. You grab your pistol and press-check it — round is chambered.")
                text_speed("You flip the desk with a loud THUD, dropping it on its side as hasty cover.")
                text_speed("You crouch behind it and brace your arms on the edge.")
                text_speed("'they definitely heard THAT.'")
                text_speed("They did. You hear a shotgun bolt rack a shell on the other side of the door.")
                text_speed("Four shots — three at hinges, one at the knob. The door shreds. Splinters fill the air.")
                text_speed("You fire two controlled pairs into the first man's knees. He crumbles under his own kit.")
                text_speed("Two more to his head. The floor and the next man's boots get painted.")
                text_speed("'DOPPLER ACTUAL THIS IS ECHO TWO, ECHO ONE IS DOWN, WE HAVE MADE ENTRY.'")
                text_speed("He relays your position. The stack makes entry and suppresses your cover.")
                text_speed("You blindfire through the lull, stand, and go through the window.")
                roll_result = rng()
                player_health, damage_taken, is_dead = damage(roll_result, player_health)
                if roll_result == 10 or is_dead:
                    text_speed("A barrage of gunfire shatters the glass around you as you're peppered with rounds.")
                    text_speed("A bullet tears through your spine. You land face up.")
                    text_speed("You blink slowly as your vision fades. A blurry silhouette. A flash of light. YOU HAVE DIED.")
                    result = die_and_maybe_restart()
                    if result is None:
                        break
                    current_room = result
                    player_health = 10
                    has_rifle = False
                    is_kitted = False
                elif roll_result <= 5:
                    text_speed("You land on your side and notice — among the pain — a warm sting on your ribs.")
                    text_speed("'you gotta be fuckin kidding me man.' you mutter.")
                    text_speed(f"You take {damage_taken} damage. Health: {player_health}/10")
                    current_room = 'alley'
                else:
                    text_speed("You land on your back, gun trained on the window above you.")
                    text_speed(f"Sharp pain in your shoulder. {damage_taken} damage. Health: {player_health}/10")
                    current_room = 'alley'

            elif player_action == 'north':
                text_speed("You move to the door and jiggle the knob.")
                text_speed("'Locked.' you say, half to yourself. You head back to the desk.")
                # stays in start

            elif player_action == 'south':
                text_speed("You grab the desk chair and hurl it through the window. The alley below is clear.")
                text_speed("'this is gonna fuckin suck.' you groan, climbing out and scaling down the wall.")
                text_speed("You land in the alley near a dumpster that smells like hot wet ass.")
                text_speed("Behind you, the door in the apartment slams open — a slurry of bangs follow.")
                current_room = 'alley'

            elif player_action == 'east':
                current_room = 'east'

            elif player_action == 'west':
                current_room = 'west'

            else:
                text_speed("Can't do that right now.")

        # ──────────────────────────────────────────────
        # WEST ROOM (living room)
        # ──────────────────────────────────────────────
        elif current_room == 'west':

            if player_action == 'shoot' or player_action == 'wait':
                text_speed("You grab your pistol and make for the couch, crouching behind it — completely concealed from the door.")
                text_speed("You hear the door crash open. The entry team scans the room, MCX rifles up.")
                text_speed("A boot rounds the corner of the couch. You press your muzzle to his knee and pull the trigger.")
                text_speed("He goes down screaming. The team sends rounds toward the sound.")
                text_speed("Through the fire, you drag him to you and put one through his brain.")
                text_speed("'flashbang' him if you want to clear the room.")

            elif player_action == 'flashbang':
                text_speed("You strip three flashbangs from the downed operator's kit.")
                text_speed("Two in one hand, pins pulled — you toss one left, one toward the door.")
                text_speed("The gunfire stops. You hear operators stumble and groan.")
                text_speed("You cook the third and toss it around the corner of the couch.")
                text_speed("All three make good effect. You stand up.")
                text_speed("You dispatch the man in the living room — rounds to the head and chest.")
                text_speed("He slides down the wall, blood streaking behind him.")
                text_speed("Two operators near the kitchen bar. You walk the rifle across both of their heads.")
                text_speed("Pink mist paints the white tiles.")
                text_speed("You double-tap the downed man for good measure, reload from his kit, and push to the door.")
                text_speed("A man in the hallway is coming to his senses.")
                text_speed("You shoot his legs. He collapses, screaming.")
                text_speed("He tries to draw a Kimber 1911. You pin his wrist and shoot it out of his hand.")
                text_speed("His palm is a mess. The gun is broken.")
                text_speed("'Are there any more of you?'")
                text_speed("'Go outside and find out, you fuckin pussy.' he says through ragged breaths.")
                text_speed("'you sure you don't wanna give me a hint?' you ask.")
                text_speed("He laughs shakily. 'You step one foot outside and you're as good as dead.'")
                text_speed("You shrug. 'suit yourself.'")
                text_speed("You press the muzzle to his forehead and blow his shit clean off.")
                has_rifle = True
                current_room = 'hallway'

            elif player_action in ['north', 'south', 'east']:
                current_room = player_action

            else:
                text_speed("Can't do that right now.")

        # ──────────────────────────────────────────────
        # HALLWAY
        # ──────────────────────────────────────────────
        elif current_room == 'hallway':

            if player_action == 're-kit':
                text_speed("You head back into the apartment and flip the nearest operator.")
                text_speed("You strip him methodically and take mental inventory:")
                text_speed("'Two SAPI plates, eight mags, three flashbangs, a radio with a PTT, and a knife.'")
                text_speed("'Solid setup for a kill team.' You notice they're all uniformed — organized.")
                text_speed("'That's not a very good sign for my health.'")
                text_speed("You strap up and head back to the hallway.")
                is_kitted = True

            elif player_action == 'outside':
                text_speed("You push through the stairwell and out the front of the building into the cold night air.")
                current_room = 'outside'

            else:
                text_speed("Can't do that right now.")

        # ──────────────────────────────────────────────
        # ALLEY
        # ──────────────────────────────────────────────
        elif current_room == 'alley':

            if player_action == 'wait':
                text_speed("You press your back to the wall and hold your breath. Nothing moves.")
                text_speed("A window above scrapes open. Footsteps on a fire escape.")
                text_speed("'he went out the window!' — they're coming down.")
                text_speed("You don't have long.")

            elif player_action == 'go_right':
                text_speed("You sprint right, hugging the wall, heading toward the street.")
                current_room = 'outside'

            elif player_action == 'go_left':
                text_speed("You move left, deeper into the alley, away from the building entrance.")
                text_speed("A chain-link fence at the far end. Climbable.")
                current_room = 'outside'

            elif player_action == 'hide_in_dumpster':
                text_speed("You lift the dumpster lid and drop in, pulling it shut above you.")
                text_speed("It smells exactly as bad as you thought it would.")
                text_speed("Boots hit the fire escape. Two men land in the alley.")
                text_speed("'clear.' They move past you toward the street.")
                text_speed("You wait thirty seconds and climb out.")
                current_room = 'outside'

            else:
                text_speed("Can't do that right now.")

        # ──────────────────────────────────────────────
        # OUTSIDE
        # ──────────────────────────────────────────────
        elif current_room == 'outside':

            if player_action == 'wait':
                text_speed("You hold position. A black SUV rolls past slowly. It doesn't stop.")
                text_speed("The street stays quiet. For now.")

            elif player_action == 'go_left':
                text_speed("You move left down the block, staying in the shadows.")
                text_speed("A cab is parked at the corner, engine idling.")
                text_speed("You get in. 'Drive.' The driver doesn't ask questions.")
                text_speed("\n--- YOU MADE IT OUT ---")
                text_speed(f"Final health: {player_health}/10")
                if is_kitted:
                    text_speed("You're walking away with a full kit. Not bad.")
                text_speed("\nthanks for playing my game <3")
                break

            elif player_action == 'go_right':
                text_speed("You move right. Halfway down the block, headlights snap on.")
                text_speed("An SUV launches from a side street. They had eyes on the building.")
                roll_result = rng()
                if roll_result <= 4:
                    text_speed("You dive behind a parked car as rounds punch through the door panels.")
                    text_speed("You're pinned. No cover to your rear. YOU HAVE DIED.")
                    result = die_and_maybe_restart()
                    if result is None:
                        break
                    current_room = result
                    player_health = 10
                    has_rifle = False
                    is_kitted = False
                else:
                    text_speed("You break left into an alley — they overshoot the turn.")
                    text_speed("You're gone before they can reverse. You flag a cab two blocks over.")
                    text_speed("\n--- YOU MADE IT OUT ---")
                    text_speed(f"Final health: {player_health}/10")
                    text_speed("\nthanks for playing my game <3")
                    break

            else:
                text_speed("Can't do that right now.")

        # ──────────────────────────────────────────────
        # EAST ROOM (thin door)
        # ──────────────────────────────────────────────
        elif current_room == 'east':

            if player_action == 'kick_door':
                text_speed("You take two steps back and drive your boot into the door.")
                text_speed("It splinters off the frame and reveals a small bathroom.")
                text_speed("Clear. You use the mirror to check the hallway through the crack in the frame.")
                text_speed("Two men stacked outside the front door. They haven't breached yet.")
                text_speed("You slip back into the main room.")
                current_room = 'start'

            elif player_action in ['north', 'south', 'west']:
                current_room = player_action

            elif player_action in ['shoot', 'wait']:
                text_speed("From here? Not much angle. You should move first.")

            else:
                text_speed("Can't do that right now.")

        else:
            text_speed("You look around. Nothing to do here yet.")

if __name__ == '__main__':
    main()

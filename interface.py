import csv
from datetime import datetime
from pyswip import Prolog, Variable, Functor, Query
from IPython.display import display, Markdown
from colorama import Fore, Style, init
from natural_language_parser import parse_preferences
init(autoreset=True)




prolog = Prolog()
prolog.consult("study_system.pl")  


def get_weights(attribute, value):
    if value != "skip":
        while True:
            try:
                weight = int(input(f"How important is this {attribute} preference to you (1-5)\n "))
                if 1 <= weight <= 5:
                    break
            except ValueError:
                pass
            print("❌ Please enter a valid number between 1 and 5 (inclusive).")
    else:
        weight = 0
    return weight

def get_map(options, attribute):
    option_map = {}
    print(f"{attribute} Options:")
    for index, value in enumerate(options):
        if index == len(options) - 1:
            print(f"{index+1}. {value.capitalize()}/No Preference")
            option_map[str(index+1)] = value
            continue
            
        print(f"{index+1}. {value.capitalize()}")
        option_map[str(index+1)] = value
    
    return option_map

def get_user_input():
    print("Welcome to the Seoul Study Spot Finder!!")

    mode = ""
    while mode not in ["1", "2"]:
        print("\nHow would you like to enter your preferences?")
        print("1. Natural language (e.g., 'I want a cozy cafe with plugs')")
        print("2. Guided form (recommended for detailed control)")
        mode = input("> ").strip()

    use_natural_language = mode == "1"

    user_prefs = {
        "work_type": "skip",
        "outlet_pref": "skip",
        "vibe_pref": "skip",
        "seating_pref": "skip",
        "price_pref": "skip",
        "open_late": "skip"
    }

    if use_natural_language:
        user_input_str = input("\nTell me what kind of place you're looking for:\n> ")
        parsed_prefs = parse_preferences(user_input_str)
        user_prefs.update(parsed_prefs)

        print("\n✅ Got these from your description:")
        for k, v in parsed_prefs.items():
            print(f"   {k}: {v}")

        if parsed_prefs.get("fallback_prompt", False):
            print("\n⚠️ I couldn't understand enough from your description.")
            print("Switching to the guided form for more accurate recommendations!\n")
            return get_user_input()

        # Ask for origin
        while True:
            origin = input("\nWhere are you coming from? (Sinseol/Dongdaemun)\n> ").strip().lower()
            if origin in ["sinseol", "dongdaemun"]:
                break
            print("❌ Invalid input.")
        user_prefs["origin"] = origin

        # Ask for travel time
        while True:
            try:
                max_minutes = int(input("How many minutes max are you willing to travel?\n> "))
                if max_minutes > 0:
                    break
            except ValueError:
                pass
            print("❌ Please enter a valid number.")
        user_prefs["max_minutes"] = max_minutes

        # Ask for weights
        travel_weight = get_weights("travel time", max_minutes)
        work_weight = get_weights("work", user_prefs["work_type"])
        outlet_weight = get_weights("outlet", user_prefs["outlet_pref"])
        vibe_weight = get_weights("vibe", user_prefs["vibe_pref"])
        seating_weight = get_weights("seating", user_prefs["seating_pref"])
        price_weight = get_weights("price", user_prefs["price_pref"])
        late_weight = get_weights("open late", user_prefs["open_late"])

    else:
        # Use full guided form (reuse existing blocks)
        return full_guided_input()

    # Explanation style
    explain_map = get_map(["short", "long"], "Explanation Style")
    while True:
        explain_input = input("Preferred explanation style (1-2):\n> ").strip()
        if explain_input in explain_map:
            explain_mode = explain_map[explain_input]
            break
        print("❌ Please choose either 1 or 2.")

    # Top N
    try:
        top_n = int(input("\nHow many top study spot recommendations do you want? (default = 3)\n> ").strip())
        if top_n <= 0:
            top_n = 3
    except ValueError:
        top_n = 3

    # Recommendation mode
    mode_map = get_map(["strict", "fallback"], "Mode Preferences")
    print("NB: Strict Mode tries to match exactly, fallback ranks partial matches.")
    mode_input = input("Select recommendation mode (1-2):\n> ").strip()
    rec_mode = mode_map.get(mode_input, "fallback")

    return {
        "origin": user_prefs["origin"],
        "max_minutes": user_prefs["max_minutes"],
        "travel_weight": travel_weight,
        "work_type": user_prefs["work_type"],
        "work_weight": work_weight,
        "outlet_pref": user_prefs["outlet_pref"],
        "outlet_weight": outlet_weight,
        "vibe_pref": user_prefs["vibe_pref"],
        "vibe_weight": vibe_weight,
        "seating_pref": user_prefs["seating_pref"],
        "seating_weight": seating_weight,
        "price_pref": user_prefs["price_pref"],
        "price_weight": price_weight,
        "open_late": user_prefs["open_late"],
        "late_weight": late_weight,
        "explain_mode": explain_mode,
        "top_n": top_n,
        "mode": rec_mode
    }


def full_guided_input():
    # Getting the origin
    while True:
        origin = input("Where are you coming from? (Sinseol/Dongdaemun)\n").strip().lower()
        if origin in ["sinseol", 'dongdaemun']:
            if origin == "sinseol":
                print("I hope you had some free coffee from B2 today")
            else:
                print("You should really try SorryNotSorry's Espresso")
            break
        else:
            print("❌ Please enter 'Sinseol' or 'Dongdaemun' (Not case-sensitive).")
    
    
    # Getting max travel time
    comment_map = {
        1: "Looks like you are in a bit of a rush, we've got you covered!",
        2: "Looks like you want a light stroll on your way to study!",
        3: "With that time, you get to see some of Seoul. Cheers!",
        4: "It seems like you wanna travel more than study, LOL! \nBut we've got you!"
    }
    while True:
        try:
            max_minutes = int(input("Please enter the maximum time you're willing to travel (e.g. 15, 20, e.t.c.)\n"))
            if max_minutes > 0:
                print("Thank you for providing that info.")
                match max_minutes:
                    case x if x <= 5:
                        print(comment_map[1])
                    case x if 6 <= x <= 15:
                        print(comment_map[2])
                    case x if 16 <= x <= 30:
                        print(comment_map[3])
                    case _:
                        print(comment_map[4])
                break
            else:
                print("Please enter a positive number")
        except ValueError:
            pass
        print("❌ Please enter an integer")
    
    # Getting travel weight
    travel_weight = get_weights("travel time", max_minutes)
    
    
    # Work
    work_map = get_map(["deep_focus", "casual", "group", "skip"], "Work Preference")
    while True:
        work_input = input("Please choose your preferred working condition (1-4):\n").strip()
        if work_input in work_map:
            break
        print("❌ Please choose a valid option (1-4).")
    work_type = work_map.get(work_input, "skip")
    work_weight = get_weights("work", work_type)

    # Power Outlet
    outlet_map = get_map(["no", "yes", "limited", "skip"], "Power Outlet")
    while True:
        outlet_input = input("Please enter your choice of power outlet availability (1-4):\n").strip()
        if outlet_input in outlet_map:
            break
        print("❌ Please choose a valid option (1-4).")
    outlet_pref = outlet_map.get(outlet_input, "skip")
    outlet_weight = get_weights("outlet", outlet_pref)

    # Vibe
    vibe_map = get_map(["quiet", "cozy", "lively", "skip"], "Vibe Preferences")
    while True:
        vibe_input = input("Please enter your vibe preference choice (1-4):\n").strip()
        if vibe_input in vibe_map:
            break
        print("❌ Please choose a valid option (1-4).")
    vibe_pref = vibe_map.get(vibe_input, "skip")
    vibe_weight = get_weights("vibe", vibe_pref)

    # Seating
    seating_map = get_map(["booth", "open_table", "lounge", "individual_desk", "skip"], "Seating Preference")
    while True:
        seating_input = input("Pick your seating type (1-5):\n> ").strip()
        if seating_input in seating_map:
            break
        print("❌ Please choose a valid option (1-5).")
    seating_pref = seating_map.get(seating_input, "skip")
    seating_weight = get_weights("seating", seating_pref)

    # Price
    price_map = get_map(["free", "low", "medium", "skip"], "Price Preference")
    while True:
        price_input = input("Pick your pricing preference (1-4):\n> ").strip()
        if price_input in price_map:
            break
        print("❌ Please choose a valid option (1-4).")
    price_pref = price_map.get(price_input, "skip")
    price_weight = get_weights("price", price_pref)

    # Open Late
    late_map = get_map(["yes", "no", "skip"], "Open Late Preference")
    while True:
        late_input = input("Do you want it open late? (1-3):\n> ").strip()
        if late_input in late_map:
            break
        print("❌ Please choose a valid option (1-3).")
    open_late = late_map.get(late_input, "skip")
    late_weight = get_weights("open late", open_late)

    # Explanation Mode
    explain_map = get_map(["short", "long"], "Explanation Style")
    while True:
        explain_input = input("Preferred explanation style (1-2):\n> ").strip()
        if explain_input in explain_map:
            break
        print("❌ Please choose either 1 or 2.")
    explain_mode = explain_map.get(explain_input, "long")

    # Top N
    try:
        top_n = int(input("\nHow many top study spot recommendations do you want? (default = 3)\n> ").strip())
        if top_n <= 0:
            top_n = 3
    except ValueError:
        top_n = 3
        
    # Mode (strict/fallback)
    mode_map = get_map(["strict", "fallback"], "Mode Preferences")
    print(f"NB: Strict Mode tries to map your exact choices but might not always have an output but fallback mode assigns rank based on match quality")
    mode_input = input("Select recommendation mode (1-2):\n> ").strip()
    mode = mode_map.get(mode_input, "fallback")

    # All inputs collected
    return {
        "origin": origin,
        "max_minutes": max_minutes,
        "travel_weight": travel_weight,
        "work_type": work_type,
        "work_weight": work_weight,
        "outlet_pref": outlet_pref,
        "outlet_weight": outlet_weight,
        "vibe_pref": vibe_pref,
        "vibe_weight": vibe_weight,
        "seating_pref": seating_pref,
        "seating_weight": seating_weight,
        "price_pref": price_pref,
        "price_weight": price_weight,
        "open_late": open_late,
        "late_weight": late_weight,
        "explain_mode": explain_mode,
        "top_n": top_n,
        "mode": mode
    }
    
    
def run_strict_query(user_inputs):
    q = f"""
        recommend_spot(
            '{user_inputs["origin"]}',
            {user_inputs["max_minutes"]},
            '{user_inputs['work_type']}',
            '{user_inputs['outlet_pref']}',
            '{user_inputs['vibe_pref']}',
            '{user_inputs['seating_pref']}',
            '{user_inputs['price_pref']}',
            '{user_inputs['open_late']}',
            Name, Link)
    """

    results = list(prolog.query(q))
    return results

def run_fallback_query(user_inputs):
    q = f"""
        find_top_study_spots({user_inputs['origin']},
                             {user_inputs['max_minutes']},
                             {user_inputs["travel_weight"]},
                             {user_inputs['work_type']},
                             {user_inputs['work_weight']},
                             {user_inputs['outlet_pref']},
                             {user_inputs['outlet_weight']},
                             {user_inputs['vibe_pref']},
                             {user_inputs['vibe_weight']},
                             {user_inputs['seating_pref']},
                             {user_inputs['seating_weight']},
                             {user_inputs['price_pref']},
                             {user_inputs['price_weight']},
                             {user_inputs['open_late']},
                             {user_inputs['late_weight']},
                             "{user_inputs['explain_mode']}",
                             {user_inputs['top_n']},
                             Results)
    """
    raw_results = list(prolog.query(q))
    return raw_results

def compute_match_info(user_inputs, score, explanation):
    attr_to_pref_key = {
        "travel": "max_minutes",
        "work": "work_type",
        "outlet": "outlet_pref",
        "vibe": "vibe_pref",
        "seating": "seating_pref",
        "price": "price_pref",
        "late": "open_late"
    }

    attributes = list(attr_to_pref_key.keys())
    total_weight = 0
    skipped = 0

    for attr in attributes:
        pref_key = attr_to_pref_key[attr]
        weight_key = f"{attr}_weight"
        pref = user_inputs[pref_key]
        weight = user_inputs[weight_key]
        if pref == "skip":
            skipped += 1
        else:
            total_weight += weight

    # Simple explanation-based match check
    explanation_lower = explanation.lower()
    match_count = sum("not match" not in part.lower() for part in explanation_lower.split(".") if part.strip())

    percent = int((score / total_weight) * 100) if total_weight > 0 else 0
    return f"🔎 Matched {match_count} out of 7 preferences ({percent}% match)", skipped



def display_results(user_inputs, results):
    print("\n📍 Here are your top study spot recommendations:\n")
    
    if user_inputs["mode"] == "strict":
        if not results:
            print("❌ No exact matches found for your preferences in strict mode.")
        else:
            for i, res in enumerate(results, 1):
                print(f"{i}. {res['Name']}")
                print(f"   📎 Naver Maps Link: {res['Link']}\n")
    else:
        if not results:
            print("❌ No fallback recommendations found.")
            return
        
        max_score = (
            user_inputs["travel_weight"] +
            user_inputs["work_weight"] +
            user_inputs["outlet_weight"] +
            user_inputs["vibe_weight"] +
            user_inputs["seating_weight"] +
            user_inputs["price_weight"] +
            user_inputs["late_weight"]
        )
        result_list = results[0]['Results']
        if len(result_list) < user_inputs['top_n']:
            print(f"\n⚠️ Only {len(result_list)} result(s) matched your fallback preferences (requested {user_inputs['top_n']}).\n")

        for i, (score, name, link, explanation) in enumerate(result_list, 1):
            explanation_list = (explanation.split("  "))
            match_info, skipped = compute_match_info(user_inputs, score, explanation)

            star = "🌟" if i == 1 else ""
            print(f"{Fore.CYAN}{i}. {name}{star}, Score: {Fore.YELLOW}{score}  ({match_info})")
            if skipped >= 3:
                print(f"{Fore.RED}⚠️ Warning: Several preferences were skipped. Try adjusting fewer inputs for better matches.")
            print(f"   {Fore.GREEN}📎 Naver Maps Link: {link}")
            print(f"   {Fore.MAGENTA}🧠 Why:")
            for expl in explanation_list:
                if "✔" in expl:
                    print(f"      {Fore.GREEN}- {expl}")
                elif "✘" in expl:
                    print(f"      {Fore.RED}- {expl}")
                else:
                    print(f"      - {expl}")
            print()

            

# tests
# user_inputs = {
#     "origin": "sinseol",
#     "max_minutes": 10,
#     "travel_weight": 3,
#     "work_type": "deep_focus",
#     "work_weight": 5,
#     "outlet_pref": "yes",
#     "outlet_weight": 4,
#     "vibe_pref": "quiet",
#     "vibe_weight": 3,
#     "seating_pref": "individual_desk",
#     "seating_weight": 4,
#     "price_pref": "free",
#     "price_weight": 2,
#     "open_late": "yes",
#     "late_weight": 2,
#     "explain_mode": "short",
#     "top_n": 3,
#     "mode": "fallback"
# }
# results = run_fallback_query(user_inputs)
# display_results(user_inputs, results)


if __name__ == "__main__":
    while True:  # Outer loop for full reruns
        try:
            user_inputs = get_user_input()

            # Run both queries to compare results
            strict_results = run_strict_query(user_inputs)
            fallback_results = run_fallback_query(user_inputs)

            strict_count = len(strict_results)
            fallback_count = len(fallback_results[0]['Results']) if fallback_results else 0

            print("\n📊 Match Summary:")
            print(f"  Strict mode found: {strict_count} match(es)")
            print(f"  Fallback mode found: {fallback_count} match(es)")

            # Prompt the user before proceeding
            while True:
                switch = input(f"\nWould you like to view fallback recommendations instead of strict? (yes/no)\n> ").strip().lower()
                if switch in ["yes", "y"]:
                    user_inputs["mode"] = "fallback"
                    display_results(user_inputs, fallback_results)
                    break
                elif switch in ["no", "n"]:
                    user_inputs["mode"] = "strict"
                    display_results(user_inputs, strict_results)
                    break
                else:
                    print("❌ Please enter 'yes' or 'no'")

            # Ask if user wants to search again
            again = input("\n🔁 Would you like to try with new preferences? (y/n): ").strip().lower()
            if again != "y":
                print("👋 Goodbye! Happy studying!")
                break

        except KeyboardInterrupt:
            print("\n❌ Input cancelled. Exiting.")
            break

        except Exception as e:
            print(f"\n⚠️ Error occurred: {e}")
            retry = input("Would you like to try again? (y/n): ").strip().lower()
            if retry != "y":
                break


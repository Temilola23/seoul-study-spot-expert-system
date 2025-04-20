"""
Study Spot Finder CLI Interface
-------------------------------
This program allows users to get personalized study spot recommendations in Seoul 
based on their preferences. It supports both natural language and guided input 
modes, and interacts with a Prolog-based expert system via PySWIP.

Key Features:
- Natural language parsing of user preferences
- Guided CLI form with validation and suggestions
- Strict and fallback recommendation modes
- Interactive output with rich formatting (Colorama)

"""



import csv
from datetime import datetime
from pyswip import Prolog
from colorama import Fore, Style, init
from natural_language_parser import parse_preferences



# Enable color resets for terminal output (for consistent styling)
init(autoreset=True)

# Initialize and consult our expert system knowledge base
prolog = Prolog()
prolog.consult("study_system.pl")


def get_weights(attribute, value):
    """
    Prompt user for the importance weight of a given attribute.

    Parameters
    ----------
    attribute : str
        The name of the preference being rated (e.g., 'vibe', 'seating').
    value : str
        The user-chosen option for this attribute.

    Returns
    -------
    int
        A weight from 1 to 5 representing how important this preference is to the user.
        Returns 0 if the user skipped this attribute.
    """
    
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
    """
    Display numbered options for a given attribute and return a mapping from user input to values.

    Parameters
    ----------
    options : list of str
        A list of possible values for the attribute (e.g., ['quiet', 'cozy', 'lively', 'skip']).
    attribute : str
        The name of the attribute being configured.

    Returns
    -------
    dict
        A dictionary mapping string indices (e.g., "1") to corresponding option values.
    """
    option_map = {}
    print(f"{attribute} Options:")
    for index, value in enumerate(options):
        # Append "No Preference" to the final option if it's a skip
        if index == len(options) - 1:
            print(f"{index+1}. {value.capitalize()}/No Preference")
        else:
            print(f"{index+1}. {value.capitalize()}")
        option_map[str(index+1)] = value
    
    return option_map

def get_user_input():
    """
    Collect user preferences using either natural language or guided prompts.

    This function manages all user input for setting study spot preferences, origin, travel time,
    explanation mode, and recommendation mode. If natural language parsing fails, it redirects
    to the guided input mode.

    Returns
    -------
    dict
        A dictionary containing all structured user inputs and weightings.
    """
    print("Welcome to the Seoul Study Spot Finder!!")

    # Choose input mode
    mode = ""
    while mode not in ["1", "2"]:
        print("\nHow would you like to enter your preferences?")
        print("1. Natural language (e.g., 'I want a cozy cafe with plugs')")
        print("2. Guided form (recommended for detailed control)")
        mode = input("> ").strip()

    use_natural_language = mode == "1"

    # Default preferences
    user_prefs = {
        "work_type": "skip",
        "outlet_pref": "skip",
        "vibe_pref": "skip",
        "seating_pref": "skip",
        "price_pref": "skip",
        "open_late": "skip"
    }

    if use_natural_language:
        # Parse description
        user_input_str = input("\nTell me what kind of place you're looking for:\n> ")
        parsed_prefs = parse_preferences(user_input_str)
        user_prefs.update(parsed_prefs)

        print("\n✅ Got these from your description:")
        for k, v in parsed_prefs.items():
            print(f"   {k}: {v}")

        # Fallback if not enough was parsed
        if parsed_prefs.get("fallback_prompt", False):
            print("\n⚠️ I couldn't understand enough from your description.")
            print("Switching to the guided form for more accurate recommendations!\n")
            return get_user_input()

        # Get origin and travel time
        while True:
            origin = input("\nWhere are you coming from? (Sinseol/Dongdaemun)\n> ").strip().lower()
            if origin in ["sinseol", "dongdaemun"]:
                break
            print("❌ Invalid input.")
        user_prefs["origin"] = origin

        while True:
            try:
                max_minutes = int(input("How many minutes max are you willing to travel?\n> "))
                if max_minutes > 0:
                    break
            except ValueError:
                pass
            print("❌ Please enter a valid number.")
        user_prefs["max_minutes"] = max_minutes

        # Preference weight collection
        travel_weight = get_weights("travel time", max_minutes)
        work_weight = get_weights("work", user_prefs["work_type"])
        outlet_weight = get_weights("outlet", user_prefs["outlet_pref"])
        vibe_weight = get_weights("vibe", user_prefs["vibe_pref"])
        seating_weight = get_weights("seating", user_prefs["seating_pref"])
        price_weight = get_weights("price", user_prefs["price_pref"])
        late_weight = get_weights("open late", user_prefs["open_late"])
    
    else:
        # Delegate to full CLI form
        return full_guided_input()

    # Collect explanation mode and top N
    explain_map = get_map(["short", "long"], "Explanation Style")
    while True:
        explain_input = input("Preferred explanation style (1-2):\n> ").strip()
        if explain_input in explain_map:
            explain_mode = explain_map[explain_input]
            break
        print("❌ Please choose either 1 or 2.")

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
    """
    Collect user preferences step-by-step using a guided command-line form.

    This function interactively prompts the user for all required preferences:
    origin, travel time, work style, outlet access, vibe, seating, price, and whether it's open late.
    It also collects preference weights, explanation mode, and top N recommendation count.

    Returns
    -------
    dict
        A dictionary of structured preferences and their associated weights, explanation style,
        top result count, and query mode.
    """
    # --- Origin selection ---
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

    # --- Max travel time ---
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

    travel_weight = get_weights("travel time", max_minutes)

    # --- Work preference ---
    work_map = get_map(["deep_focus", "casual", "group", "skip"], "Work Preference")
    while True:
        work_input = input("Please choose your preferred working condition (1-4):\n").strip()
        if work_input in work_map:
            break
        print("❌ Please choose a valid option (1-4).")
    work_type = work_map.get(work_input, "skip")
    work_weight = get_weights("work", work_type)

    # --- Power outlet preference ---
    outlet_map = get_map(["no", "yes", "limited", "skip"], "Power Outlet")
    while True:
        outlet_input = input("Please enter your choice of power outlet availability (1-4):\n").strip()
        if outlet_input in outlet_map:
            break
        print("❌ Please choose a valid option (1-4).")
    outlet_pref = outlet_map.get(outlet_input, "skip")
    outlet_weight = get_weights("outlet", outlet_pref)

    # --- Vibe preference ---
    vibe_map = get_map(["quiet", "cozy", "lively", "skip"], "Vibe Preferences")
    while True:
        vibe_input = input("Please enter your vibe preference choice (1-4):\n").strip()
        if vibe_input in vibe_map:
            break
        print("❌ Please choose a valid option (1-4).")
    vibe_pref = vibe_map.get(vibe_input, "skip")
    vibe_weight = get_weights("vibe", vibe_pref)

    # --- Seating preference ---
    seating_map = get_map(["booth", "open_table", "lounge", "individual_desk", "skip"], "Seating Preference")
    while True:
        seating_input = input("Pick your seating type (1-5):\n> ").strip()
        if seating_input in seating_map:
            break
        print("❌ Please choose a valid option (1-5).")
    seating_pref = seating_map.get(seating_input, "skip")
    seating_weight = get_weights("seating", seating_pref)

    # --- Price preference ---
    price_map = get_map(["free", "low", "medium", "skip"], "Price Preference")
    while True:
        price_input = input("Pick your pricing preference (1-4):\n> ").strip()
        if price_input in price_map:
            break
        print("❌ Please choose a valid option (1-4).")
    price_pref = price_map.get(price_input, "skip")
    price_weight = get_weights("price", price_pref)

    # --- Open late preference ---
    late_map = get_map(["yes", "no", "skip"], "Open Late Preference")
    while True:
        late_input = input("Do you want it open late? (1-3):\n> ").strip()
        if late_input in late_map:
            break
        print("❌ Please choose a valid option (1-3).")
    open_late = late_map.get(late_input, "skip")
    late_weight = get_weights("open late", open_late)

    # --- Explanation style ---
    explain_map = get_map(["short", "long"], "Explanation Style")
    while True:
        explain_input = input("Preferred explanation style (1-2):\n> ").strip()
        if explain_input in explain_map:
            break
        print("❌ Please choose either 1 or 2.")
    explain_mode = explain_map.get(explain_input, "long")

    # --- Top N results ---
    try:
        top_n = int(input("\nHow many top study spot recommendations do you want? (default = 3)\n> ").strip())
        if top_n <= 0:
            top_n = 3
    except ValueError:
        top_n = 3

    # --- Recommendation mode ---
    mode_map = get_map(["strict", "fallback"], "Mode Preferences")
    print("NB: Strict Mode tries to map your exact choices but might not always have an output.")
    print("Fallback mode ranks based on match quality.")
    mode_input = input("Select recommendation mode (1-2):\n> ").strip()
    mode = mode_map.get(mode_input, "fallback")

    # --- Return all gathered preferences ---
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
    """
    Run a strict Prolog query that finds only study spots matching all user preferences exactly.

    Parameters
    ----------
    user_inputs : dict
        A dictionary containing user preferences such as location, travel time, and other attributes.

    Returns
    -------
    list of dict
        A list of Prolog solutions (each with a study spot's name and link), or an empty list if no match is found.
    """
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
    """
    Run a fallback Prolog query that scores and ranks study spots based on how well they match user preferences.

    This allows partial matches with preference weighting and ranking, producing a sorted list.

    Parameters
    ----------
    user_inputs : dict
        A dictionary of user preferences and their associated weights, explanation mode, and top_n result count.

    Returns
    -------
    list of dict
        A list containing one dictionary with the key "Results" mapped to a list of tuples:
        (score, name, link, explanation).
    """
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
    """
    Compute a visual and textual summary of how many user preferences were matched in a recommendation.

    Parses the explanation string from Prolog and checks which attributes matched.
    Used to generate match bars (✔ ✘ ➖) and an overall match percentage.

    Parameters
    ----------
    user_inputs : dict
        A dictionary of user preferences and weights.

    score : int
        The final score assigned to a study spot.

    explanation : str
        A string explanation from Prolog describing which preferences matched.

    Returns
    -------
    tuple
        (match_summary_str, skipped_count, match_bar_str)
        where:
        - match_summary_str is a string like 'Matched 5 out of 7 preferences (71%)'
        - skipped_count is the number of skipped preferences
        - match_bar_str is a string like '✔✘✔➖✔✔✘'
    """
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
    matches = []

    explanation_lower = explanation.lower()
    expl_lines = [e.strip() for e in explanation_lower.split(".") if e.strip()]

    for attr in attributes:
        pref_key = attr_to_pref_key[attr]
        weight_key = f"{attr}_weight"
        pref = user_inputs[pref_key]
        weight = user_inputs[weight_key]

        if pref == "skip":
            skipped += 1
            matches.append("➖")
        else:
            total_weight += weight
            matched_line = next((line for line in expl_lines if attr in line), "")
            if "matched" in matched_line and "not" not in matched_line:
                matches.append("✔")
            else:
                matches.append("✘")

    match_count = matches.count("✔")
    total_considered = 7 - skipped
    percent = int((match_count / total_considered) * 100) if total_considered > 0 else 0
    match_bar = "".join(matches)

    return f"🔎 Matched {match_count} out of {total_considered} preferences ({percent}% match)", skipped, match_bar


def display_results(user_inputs, results):
    """
    Display study spot recommendations based on the selected mode (strict or fallback).

    In strict mode, only exact matches are shown. In fallback mode, results are ranked and explained
    with a visual match bar and detailed reasons for each attribute.

    Parameters
    ----------
    user_inputs : dict
        Dictionary containing the user's preferences, mode, and weight assignments.

    results : list
        Strict mode: list of dicts with keys 'Name' and 'Link'.
        Fallback mode: list containing a dict with a 'Results' key mapping to ranked recommendations.
    """
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
            match_info, skipped, match_bar = compute_match_info(user_inputs, score, explanation)

            star = "🌟" if i == 1 else ""
            print(f"{Fore.CYAN}{i}. {name}{star}, Score: {Fore.YELLOW}{score}  ({match_info})")
            filled_blocks = match_bar.count("✔")
            total_blocks = len(match_bar)
            bar = "█" * filled_blocks + "░" * (total_blocks - filled_blocks)
            print(f"   {Fore.BLUE}✔ Match Bar: {match_bar} | {bar}")

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


if __name__ == "__main__":
    # Main entry point for running the Study Spot Finder CLI.
    # This loop enables users to run multiple queries in a single session,
    # view strict vs fallback results, and retry with new preferences if desired.
    
    while True:  # Outer loop for full reruns
        try:
            # Get user preferences via CLI or natural language
            user_inputs = get_user_input()

            # --- Run both queries to compare ---
            strict_results = run_strict_query(user_inputs)
            fallback_results = run_fallback_query(user_inputs)

            strict_count = len(strict_results)
            fallback_count = len(fallback_results[0]['Results']) if fallback_results else 0

            print("\n📊 Match Summary:")
            print(f"  Strict mode found: {strict_count} match(es)")
            print(f"  Fallback mode found: {fallback_count} match(es)")

            # --- Ask user which results to display ---
            while True:
                switch = input(
                    "\nWould you like to view fallback recommendations instead of strict? (yes/no)\n> "
                ).strip().lower()
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

            # --- Ask if user wants to search again ---
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

    print("👋 Goodbye! Happy studying!")
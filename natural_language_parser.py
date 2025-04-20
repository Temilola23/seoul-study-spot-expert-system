import re

def match_value(text, keyword_map):
    """
    Searches for a keyword or regex pattern from keyword_map in the input text.
    
    Parameters
    ----------
    text : str
        The input string to search through.
    keyword_map : dict
        A mapping of keywords or regex patterns to their corresponding canonical values.

    Returns
    -------
    str
        The matched value if a keyword is found, otherwise "skip".
    """
    for keyword, value in keyword_map.items():
        if re.search(rf"\b{re.escape(keyword)}\b", text) or re.search(keyword, text):
            return value
    return "skip"

def parse_preferences(user_input):
    """
    Parses user input in natural language and returns a structured dictionary
    of study spot preferences based on matched keywords.

    Parameters
    ----------
    user_input : str
        The natural language string describing the user's preferences.

    Returns
    -------
    dict
        A dictionary containing normalized preferences and a fallback_prompt flag.
    """
    text = user_input.lower()

    work_map = {
        # Direct matches
        "deep": "deep_focus",
        "lock in": "deep_focus",
        "quiet work": "deep_focus",
        "focus": "deep_focus",
        "deep focus": "deep_focus",
        "casual": "casual",
        "chill": "casual",
        "group": "group",
        "team": "group",
        "collab": "group",
        # Regex patterns
        r"(deep\s+concentration|intense\s+focus|study\s+grind)": "deep_focus",
        r"\b(chill(ed)?|relaxed?)\b": "casual",
        r"(collaborative|team work|working together)": "group"
    }

    outlet_map = {
        "no": "no",
        "few": "limited",
        "plug": "yes",
        "socket": "yes",
        "outlet": "yes",
        "charging": "yes",
        "no plug": "no",
        "no outlet": "no",
        "limited": "limited",
        "charge": "yes",
        r"(power outlet|charging spot|need.*power)": "yes",
        r"(no\s+(power|plug|charging))": "no"
    }

    vibe_map = {
        "quiet": "quiet",
        "serene": "quiet",
        "cozy": "cozy",
        "aesthetic": "cozy",
        "lively": "lively",
        "busy": "lively",
        "cool": "cozy",
        r"(peaceful|relaxing|low noise)": "quiet",
        r"(buzzy|buzzing|active)": "lively"
    }

    seating_map = {
        "booth": "booth",
        "table": "open_table",
        "open table": "open_table",
        "lounge": "lounge",
        "couch": "lounge",
        "desk": "individual_desk",
        "individual": "individual_desk",
        "solo": "individual_desk",
        r"(personal desk|single seat|quiet corner)": "individual_desk",
        r"(open seating|tables everywhere)": "open_table"
    }

    price_map = {
        "free": "free",
        "cheap": "low",
        "zero": "free", 
        "affordable": "low",
        "medium": "medium",
        "pricey": "medium",
        r"(don.?t\s+mind\s+price|any\s+budget)": "skip",
        r"(okay with (any|whatever)\s+(cost|price))": "skip"
    }

    late_map = {
        "open late": "yes",
        "24/7": "yes",
        "all day": "yes",
        "late night": "yes",
        "open 24": "yes",
        "closes late": "yes",
        "not late": "no",
        "closes early": "no",
        "midnight": "yes",
        r"(night\s+owl|open\s+at\s+night|night\s+time)": "yes",
        r"(closes\s+early|not\s+open\s+late)": "no"
    }

    result = {
        "work_type": match_value(text, work_map),
        "outlet_pref": match_value(text, outlet_map),
        "vibe_pref": match_value(text, vibe_map),
        "seating_pref": match_value(text, seating_map),
        "price_pref": match_value(text, price_map),
        "open_late": match_value(text, late_map)
    }

    # Flag for when too many preferences are missing
    result["fallback_prompt"] = list(result.values()).count("skip") >= 4
    return result

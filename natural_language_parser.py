import re

def parse_preferences(user_input):
    text = user_input.lower()

    work_map = {
        "deep": "deep_focus",
        "lock in": "deep_focus",
        "quiet work": "deep_focus",
        "focus": "deep_focus",
        "casual": "casual",
        "chill": "casual",
        "group": "group",
        "team": "group",
        "collab": "group"
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
        "limited": "limited"
    }

    vibe_map = {
        "quiet": "quiet",
        "serene": "quiet",
        "cozy": "cozy",
        "aesthetic": "cozy",
        "lively": "lively",
        "busy": "lively"
    }

    seating_map = {
        "booth": "booth",
        "table": "open_table",
        "open table": "open_table",
        "lounge": "lounge",
        "couch": "lounge",
        "desk": "individual_desk",
        "individual": "individual_desk",
        "solo": "individual_desk"
    }

    price_map = {
        "free": "free",
        "cheap": "low",
        "zero": "free", 
        "affordable": "low",
        "medium": "medium",
        "pricey": "medium"
    }

    late_map = {
        "open late": "yes",
        "24/7": "yes",
        "all day": "yes",
        "late night": "yes",
        "open 24": "yes",
        "closes late": "yes",
        "not late": "no",
        "closes early": "no"
    }

    result = {
        "work_type": match_value(text, work_map),
        "outlet_pref": match_value(text, outlet_map),
        "vibe_pref": match_value(text, vibe_map),
        "seating_pref": match_value(text, seating_map),
        "price_pref": match_value(text, price_map),
        "open_late": match_value(text, late_map)
    }

    result["fallback_prompt"] = list(result.values()).count("skip") >= 4
    return result


def match_value(text, keyword_map):
    for keyword, value in keyword_map.items():
        if re.search(rf"\b{re.escape(keyword)}\b", text):
            return value
    return "skip"

def build_profile(first, last, **user_info):
    """build a dictionary of users"""
    profile = {}
    profile['first name'] = first
    profile['last name'] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile
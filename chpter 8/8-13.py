def build_profile(first,last,**user_info):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('Jiang','Joe',lccation = 'nanjing',major = 'mechanical engineering',love = 'basketball')
print(user_profile)
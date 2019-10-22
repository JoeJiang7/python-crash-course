from collections import OrderedDict

favourite_languages = OrderedDict()

favourite_languages['joey'] = 'c'
favourite_languages['joe'] = 'python'

favourite_languages['dan'] = 'c#'

for name,language in favourite_languages.items():
    print(name.title() + "'s favourite languages is " + language.title() + ".")
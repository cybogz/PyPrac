from collections import OrderedDict

#creates a dictionary from the OrderedDict class which remembers insertion order
favorite_languages = OrderedDict()

favorite_languages["jen"] = "python"
favorite_languages["sarah"] = "c"
favorite_languages["edward"] = "javascript"
favorite_languages["tony"] = "python"

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title())

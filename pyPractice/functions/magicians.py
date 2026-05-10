def show_magicians(magician_list):
     for magician in magician_list:
          print(magician)

def make_great(magicians_to_be_modified):
    new_list = []

    for mag in magicians_to_be_modified:
         new_list.append(mag + " is the best")
    return new_list
          
          

magician_names = ["houdini", "criss angel", "david blaine", "js magic"]
#new_magician_message = []

newList = make_great(magician_names[:])
show_magicians(newList)
#show_magicians(magician_names)
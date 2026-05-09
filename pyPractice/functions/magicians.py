def show_magicians(magician_list):
     for magician in magician_list:
          print(magician)

def make_great(magicians_to_be_modified, new_magician_list):
        while magicians_to_be_modified:
          name = magicians_to_be_modified.pop()
          new_entry = name + " the great"
          new_magician_list.append(new_entry)
          
          

magician_names = ["houdini", "criss angel", "david blaine", "js magic"]
new_magician_message = []

make_great(magician_names, new_magician_message)
show_magicians(new_magician_message)
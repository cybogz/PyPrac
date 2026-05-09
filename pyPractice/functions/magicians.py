def show_magicians(magician_list):
     for magician in magician_list:
          print(magician)

def make_great(magicians_to_be_modified):
        """Adding text to each index in the list"""
        for person in range(len(magicians_to_be_modified)):
              magicians_to_be_modified[person] += " the great"
          
          

magician_names = ["houdini", "criss angel", "david blaine", "js magic"]
#new_magician_message = []

make_great(magician_names)
show_magicians(magician_names)
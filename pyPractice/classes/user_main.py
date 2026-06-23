import user_module

show_user = user_module.Users("Cyrus", "Bogzaran", 33, 6969666)

show_user_privileges = user_module.Admin("Cyrus", "Bogzaran", 33, 6969666)
show_user_privileges.show_privileges()
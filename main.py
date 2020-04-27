from Menus.main_menu import Main_menu
from Menus.menu import menu

if __name__ == '__main__':
    
    menus = Main_menu()
    menus.Bienvenue()
    menus.new_menu(menu[0])
    menus.Au_revoir()


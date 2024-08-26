import os
import platform

def clear_screen():
    # Unterschiedliche Befehle zum Bildschirm löschen für Windows und Unix-basierte Systeme
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def main():
    # Titel setzen (funktioniert nur auf Windows)
    if platform.system() == "Windows":
        os.system("title PyTerm")

    # ASCII-Art und Begrüßung anzeigen
    ascii_art = r"""
     _______          _________ _______  _______  _______ 
    (  ____ )|\     /|\__   __/(  ____ \(  ____ )(       )
    | (    )|( \   / )   ) (   | (    \/| (    )|| () () |
    | (____)| \ (_) /    | |   | (__    | (____)|| || || |
    |  _____)  \   /     | |   |  __)   |     __)| |(_)| |
    | (         ) (      | |   | (      | (\ (   | |   | |
    | )         | |      | |   | (____/\| ) \ \__| )   ( |
    |/          \_/      )_(   (_______/|/   \__/|/     \|
                                                          
    """
    print("PyTerm the Python Terminal Emulator by Emil")
    print(ascii_art)

    # Endlosschleife für Benutzereingaben
    while True:
        try:
            command = input("PyTerm> ")
            if command.lower() in ["exit", "quit"]:
                break
            elif command.lower() == "clear":
                clear_screen()
                print("PyTerm the Python Terminal Emulator by Emil")
                print(ascii_art)
            else:
                os.system(command)
        except KeyboardInterrupt:
            print("\nZum Beenden 'exit' oder 'quit' eingeben.")

if __name__ == "__main__":
    main()
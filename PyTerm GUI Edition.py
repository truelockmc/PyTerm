import tkinter as tk
from tkinter import scrolledtext, messagebox
import subprocess
import threading

class PyTermGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PyTerm GUI")
        self.root.configure(bg='#000000')  # Hintergrundfarbe für "hackerähnliches" Aussehen
        self.create_widgets()

    def create_widgets(self):
        self.ascii_art = r"""
     _______          _________ _______  _______  _______ 
    (  ____ )|\     /|\__   __/(  ____ \(  ____ )(       )
    | (    )|( \   / )   ) (   | (    \/| (    )|| () () |
    | (____)| \ (_) /    | |   | (__    | (____)|| || || |
    |  _____)  \   /     | |   |  __)   |     __)| |(_)| |
    | (         ) (      | |   | (      | (\ (   | |   | |
    | )         | |      | |   | (____/\| ) \ \__| )   ( |
    |/          \_/      )_(   (_______/|/   \__/|/     \|
                                                          
        """

        self.label = tk.Label(self.root, text="PyTerm GUI - Python Terminal Emulator by Emil", bg='#000000', fg='#00FF00', font=("Courier", 14))
        self.label.pack(pady=10)

        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=20, bg='#000000', fg='#00FF00', font=("Courier", 12))
        self.text_area.pack(padx=10, pady=10)
        self.text_area.insert(tk.END, self.ascii_art)

        self.entry = tk.Entry(self.root, width=80, bg='#333333', fg='#00FF00', font=("Courier", 12))
        self.entry.pack(padx=10, pady=10)
        self.entry.focus_set()

        self.execute_button = tk.Button(self.root, text="Execute", command=self.execute_command, bg='#333333', fg='#00FF00', font=("Courier", 12))
        self.execute_button.pack(padx=10, pady=10)

        self.root.bind('<Return>', lambda event: self.execute_command())

    def clear_screen(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, self.ascii_art)

    def execute_command(self):
        command = self.entry.get().strip()
        if command.lower() in ["exit", "quit"]:
            self.root.quit()
        elif command.lower() == "clear":
            self.clear_screen()
        else:
            # Ausführung des Befehls in einem separaten Thread
            command_thread = threading.Thread(target=self.execute_command_thread, args=(command,))
            command_thread.start()

    def execute_command_thread(self, command):
        try:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            stdout, stderr = process.communicate()
            status = process.returncode

            # Debugging-Ausgaben hinzufügen
            print(f"Command: {command}")
            print(f"Status code: {status}")
            print(f"STDOUT:\n{stdout}")
            print(f"STDERR:\n{stderr}")

            self.root.after(10, self.update_text_area, command, stdout, stderr, status)
        except Exception as e:
            messagebox.showerror("Error", f"Error executing command:\n{str(e)}")

    def update_text_area(self, command, stdout, stderr, status):
        self.text_area.insert(tk.END, f"\nPyTermIn> {command}\n")
        if stdout is not None:  # Überprüfen, ob stdout nicht None ist
            if stdout.strip():  # Ausgabe nur anzeigen, wenn sie nicht leer ist
                self.text_area.insert(tk.END, f"CMDOut> {stdout}\n\n")
            else:
                self.text_area.insert(tk.END, f"CMDOut> <no output>\n\n")
        else:
            self.text_area.insert(tk.END, f"CMDOut> No output from command\n\n")  # Falls stdout None ist

        if stderr:  # Falls stderr nicht leer ist, zeige den Fehler an
            self.text_area.insert(tk.END, f"CMDOut> Error: {stderr}\n\n")
        
        self.entry.delete(0, tk.END)
        self.text_area.yview(tk.END)  # Automatisches Herunterscrollen

def main():
    root = tk.Tk()
    root.configure(bg='#000000')  # Hintergrundfarbe für "hackerähnliches" Aussehen
    app = PyTermGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
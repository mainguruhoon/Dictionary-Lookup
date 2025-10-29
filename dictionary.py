import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests

def search_word():
    word = entry.get().strip()
    if not word:
        messagebox.showwarning("Input Error", "Please enter a word to search")
        return
    
    # Clear previous results
    definition_text.delete(1.0, tk.END)
    full_response_text.delete(1.0, tk.END)
    
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    
    try:
        res = requests.get(url)
        
        if res.status_code == 200:
            data = res.json()
            
            # Extract first definition
            meanings = data[0]["meanings"]
            definitions = meanings[0]["definitions"]
            definition = definitions[0]["definition"]
            
            # Display definition
            definition_text.insert(1.0, f"Definition: {definition}")
            
            # Display full JSON response
            full_response_text.insert(1.0, str(data))
            
        else:
            messagebox.showerror("Error", "No data found for this word")
            
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create main window
root = tk.Tk()
root.title("Dictionary Lookup")
root.geometry("1000x1000")
root.configure(bg="#bfbec4")

# Title Label
title_label = tk.Label(root, text="Dictionary Lookup", font=("Helvetica", 28, "bold"))
title_label.pack(pady=10)
title_label = tk.Label(root, text="By Gurudutt", font=("Helvetica", 28, "bold"))
title_label.pack(pady=0)

# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Entry widget
entry_label = tk.Label(input_frame, text="Enter word:", font=("Helvetica", 22))
entry_label.pack(side=tk.LEFT, padx=5)

entry = tk.Entry(input_frame, font=("Helvetica", 22), width=45)
entry.pack(side=tk.LEFT, padx=5)

# Search button
search_btn = tk.Button(input_frame, text="Search", command=search_word, 
                       font=("Helvetica", 22, "bold"),  fg="Blue", 
                       padx=15, pady=5, cursor="hand2")
search_btn.pack(side=tk.LEFT, padx=5)

# Bind Enter key to search
entry.bind('<Return>', lambda event: search_word())

# Definition display
def_label = tk.Label(root, text="Definition:", font=("Helvetica", 30, "bold"))
def_label.pack(pady=(15, 5))

definition_text = scrolledtext.ScrolledText(root, height=5, width=100, 
                                           font=("Helvetica", 22), wrap=tk.WORD)
definition_text.pack(padx=20, pady=5)

# Full response display
response_label = tk.Label(root, text="Full Response:", font=("Helvetica", 22, "bold"))
response_label.pack(pady=(15, 5))

full_response_text = scrolledtext.ScrolledText(root, height=100, width=150, 
                                               font=("Courier", 9), wrap=tk.WORD)
full_response_text.pack(padx=20, pady=5)

# Run the application
root.mainloop()
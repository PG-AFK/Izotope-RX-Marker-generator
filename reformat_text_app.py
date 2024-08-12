import tkinter as tk
from tkinter import filedialog

def format_text(input_text):
    lines = input_text.strip().split('\n')
    formatted_lines = []

    for line in lines:
        parts = line.split()
        
        if len(parts) == 2:
            # Handle single timestamp format: "start_time text"
            start_time = parts[0]
            end_time = None
            text = ' '.join(parts[1:])
        elif len(parts) == 3:
            # Handle two timestamps format: "start_time end_time text"
            start_time = parts[0]
            end_time = parts[1]
            text = ' '.join(parts[2:])
        else:
            continue  # Skip invalid lines
        
        # Format text for iZotope RX: "text\tstart_time\tend_time"
        if end_time:
            formatted_line = f"{text}\t{start_time}\t{end_time}"
        else:
            formatted_line = f"{text}\t{start_time}"
        
        formatted_lines.append(formatted_line)
    
    return "\n".join(formatted_lines)

def save_file(content):
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, 'w') as file:
            file.write(content)

def process_text():
    input_text = text_input.get("1.0", tk.END).strip()
    if input_text:  # Check if input_text is not empty
        formatted_text = format_text(input_text)
        save_file(formatted_text)

# Create the main window
root = tk.Tk()
root.title("Text Formatter")

# Create and place the widgets
tk.Label(root, text="Paste your text below:").pack(pady=10)
text_input = tk.Text(root, height=10, width=50)
text_input.pack(pady=5)

tk.Button(root, text="Format and Save", command=process_text).pack(pady=20)

# Start the GUI event loop
root.mainloop()

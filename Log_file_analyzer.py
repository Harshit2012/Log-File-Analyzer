import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os

class LogFileAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Log File Analyzer")
        self.root.geometry("600x400")
        self.create_widgets()
        
    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Log File Analyzer", font=("Helvetica", 16))
        self.title_label.pack(pady=10)
        
        self.upload_button = tk.Button(self.root, text="Upload Log File", command=self.upload_log_file)
        self.upload_button.pack(pady=10)
        
        self.tree = ttk.Treeview(self.root, columns=("Field", "Value"), show="headings")
        self.tree.heading("Field", text="Field")
        self.tree.heading("Value", text="Value")
        self.tree.pack(pady=10, fill="both", expand=True)
        
    def upload_log_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Log files", "*.log"), ("All files", "*.*")])
        if file_path:
            if os.path.getsize(file_path) > 0:
                self.analyze_log_file(file_path)
            else:
                messagebox.showerror("Error", "The selected file is empty.")
                
    def analyze_log_file(self, file_path):
        for row in self.tree.get_children():
            self.tree.delete(row)
        log_data = self.parse_log_file(file_path)
        for key, value in log_data.items():
            self.tree.insert("", "end", values=(key, value))
        
    def parse_log_file(self, file_path):
        log_data = {
            "Total Lines": 0,
            "Total Errors": 0,
            "Total Warnings": 0,
            "Total Info": 0
        }
        
        with open(file_path, "r") as file:
            for line in file:
                log_data["Total Lines"] += 1
                if "ERROR" in line:
                    log_data["Total Errors"] += 1
                elif "WARNING" in line:
                    log_data["Total Warnings"] += 1
                elif "INFO" in line:
                    log_data["Total Info"] += 1
        
        return log_data

if __name__ == "__main__":
    root = tk.Tk()
    app = LogFileAnalyzer(root)
    root.mainloop()
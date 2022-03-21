import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter.filedialog import asksaveasfilename


def do_command(program, command):
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    p = subprocess.Popen(command + " " + program, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # v2

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)


# Save function.
def mSave():
    try:
        filename = asksaveasfilename(defaultextension='.txt', filetypes=(
            ('Text files', '*.txt'), ('Python files', '*.py *.pyw'), ('All files', '*.*')))
        if filename is None:
            return
        file = open(filename, mode='w')
        text_to_save = command_textbox.get("1.0", tk.END)

        file.write(text_to_save)
        file.close()

    except:
        pass


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
frame.configure(cursor="heart")
User = tk.StringVar()

url_label = tk.Label(frame, text="Enter a URL: ",
compound="center",
font=("Arial", 14),
bd=0,
relief=tk.FLAT,
cursor="circle",
fg="brown",
bg="yellow")

frame_URL = tk.Frame(root, pady=5, bg="yellow")  # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL: ", compound="center", font=("Helvetica", 14), bd=0,
                     relief=tk.FLAT, cursor="circle", fg="brown", bg="yellow")
url_label.pack(side=tk.LEFT)
url_entry = tk.Entry(frame_URL, textvariable=User, font=
("Arial", 14)) # change font
url_entry.pack(side=tk.LEFT)

# Makes the command button pass it's name to a function using lambda
ping_btn = tk.Button(frame, text="Ping", font=("Helvetica", 12), fg="brown", cursor="circle", bg="yellow",
                     command=lambda: do_command(User.get(), "ping"))
ping_btn.pack(ipadx=5, ipady=5, expand=True, fill='both', side='top')

tracert_btn = tk.Button(frame, text="Tracert", font=("Helvetica", 12), cursor="circle", fg="brown", bg="yellow",
                        command=lambda: do_command(User.get(), "tracert"))
tracert_btn.pack(ipadx=1, ipady=1, expand=True, fill='both', side='top')

nslookup_btn = tk.Button(frame, text="Nslookup", font=("Helvetica", 12), fg="brown", cursor="circle", bg="yellow",
                         command=lambda: do_command(User.get(), "nslookup"))
nslookup_btn.pack(ipadx=1, ipady=1, expand=True, fill='both', side='top')

save_btn = tk.Button(frame, text="Save", font=("Helvetica", 12), fg="brown", cursor="circle", bg="yellow",
                     command=lambda: mSave())
save_btn.pack(ipadx=1, ipady=1, expand=True, fill='both', side='top')

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=5, width=50, cursor="circle")
command_textbox.pack()

root.configure(bg='yellow')
root.mainloop()

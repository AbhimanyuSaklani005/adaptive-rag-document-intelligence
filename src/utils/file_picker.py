from tkinter import Tk, filedialog

def pick_pdf():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    file_path = filedialog.askopenfilename(
        title="Select PDF",
        filetypes=[("PDF files", "*.pdf")]
    )

    return file_path
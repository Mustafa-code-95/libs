import tkinter as tk


class ht:
    class Ht:
        def __init__(self):
            self.window = tk.Tk()
        
        def geometry(self, size="100x100"):
            self.window.geometry(size)
        
        def title(self, title="ht"):
            self.window.title(title)
        
        def main(self):
            self.window.mainloop()
    
    def Label(ht_instance, text="Label"):
        return tk.Label(ht_instance.window, text=text)
    
    def Button(ht_instance, text="Button", command=False):
        return tk.Button(ht_instance.window, text=text, command=command)

    def Entry(ht_instance):
        return tk.Entry(ht_instance.window)

    def Canvas(ht_instance, width=200, height=200, bg="white"):
        canvas = tk.Canvas(ht_instance.window, width=width, height=height, bg=bg)
        return canvas

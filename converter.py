import customtkinter as ctk
from PIL import Image
import units

root = ctk.CTk()
root.iconbitmap("icon.ico")  # custom defined icon
root.title("Converter")
root.geometry("550x400")
root.configure(bg="#19191a")
ctk.set_appearance_mode("dark")
# ----------------------------------------
font = ("OCR A Extended", -13.35) # font for all dropdowns

def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

def menu():
    def fields(choice):
        """Create conversion interface according to chosen field of units."""

        def values():
            """Define the units that are going to be in the dropdowns."""
            if choice == "Length":
                values = ['--', 'Centimeter (cm)', 'Meter (m)', 'Kilometer (km)', 'Inch (in)', 'Foot (ft)', 'Mile (mi)', '* Feet and inches (ft in)']
            elif choice == "Area":
                values = ['--', 'Square meter (m\u00b2)', 'Square kilometer (km\u00b2)', 'Square inch (in\u00b2)',  
                            'Square foot (ft\u00b2)', 'Acre (ac)', 'Hectare (ha)']
            elif choice == "Volume":
                values = ['--', 'Cubic centimeter (cm\u00b3)', 'Cubic meter (m\u00b3)', 'Millileter (ml)', 'Liter (l)']
            elif choice == "Mass":
                values = ['--', 'Milligram (mg)', 'Gram (g)', 'Kilogram (kg)', 'Pounds (lbs)', 'Ounce (oz)']
            else:
                values = ['--', 'Celsius (°C)', 'Fahrenheit (°F)', 'Kelvin (K)']
            return values

        if choice == "--":
            pass
        else:
            clear_frame()
            root.geometry("650x450")

            # Make the title
            title = ctk.CTkLabel(root, text=choice, font=("Courier", 45, 'bold'), padx=10, pady=7.5, 
                                text_color="chartreuse3")
            title.place(relx=0.5, rely=0.15, anchor='center')

            def home():
                clear_frame()
                menu()
            
            home_img = ctk.CTkImage(dark_image=Image.open("menu.png"), size=(50,50))
            home_button = ctk.CTkButton(master=root, image=home_img, text=None, fg_color='transparent',
                                        width=50, height=50, hover_color='grey25', command=home)
            home_button.place(relx=0.075, rely = 0.1, anchor='center')

            # Dropdowns - left and right for unit selections
            values = values()

            units_left = ctk.CTkComboBox(master=root, values=values,
                                        width=220, height=30, corner_radius=10, font=("OCR A Extended", -13.35),
                                        text_color="chartreuse3", dropdown_font=font, dropdown_text_color="chartreuse3")
            units_left.place(relx=0.25, rely=0.375, anchor='center')
            
            units_right = ctk.CTkComboBox(master=root, values=values,
                                        width=220, height=30, corner_radius=10, font=("OCR A Extended", -13.35),
                                        text_color="chartreuse3", dropdown_font=font, dropdown_text_color="chartreuse3")
            units_right.place(relx=0.75, rely=0.375, anchor='center')

            def swap():
                right = units_right.get()
                left = units_left.get()
                units_left.set(right)
                units_right.set(left)

            swap_img = ctk.CTkImage(dark_image=Image.open("swap.png"), size=(50,50))
            swap_button = ctk.CTkButton(master=root, image=swap_img, text=None, fg_color='transparent',
                                        width=50, height=50, hover_color='grey25', command=swap)
            swap_button.place(relx=0.5, rely = 0.5, anchor='center')
            
            units_left.set('--')
            units_right.set('--')          

            # User input
            fields.input = ctk.CTkEntry(root, width=210, height=40, corner_radius=10, 
                                        text_color="chartreuse3", font=("Courier New", 15))
            fields.input.place(relx=0.25, rely=0.5, anchor='center')
            frame = ctk.CTkFrame(root, width=210, height=40, corner_radius=10, fg_color="grey24", 
                                    border_width=2, border_color="grey32")
            frame.place(relx=0.75, rely=0.5, anchor='center')

            # Output display in form of a label
            output = ctk.CTkLabel(frame, corner_radius=10, text='', text_color="chartreuse3", font=("Courier New", 15))
            output.place(relx=0.5, rely=0.5, anchor='center')

            def convert():
                left = units.unit_mappings[choice][units_left.get()]
                right = units.unit_mappings[choice][units_right.get()]
                result = units.convert(choice, left, right, fields.input.get())
                output.configure(text=result)

            # Calculate button
            calc = ctk.CTkButton(master=root, width=120, height=32, border_width=2, corner_radius=8, text="Calculate",
                                    font=("OCR A Extended", 13, 'bold'), text_color="chartreuse3", fg_color="grey27", 
                                    border_color="chartreuse4", hover_color='grey25', command=convert)
            calc.place(relx=0.5, rely=0.7, anchor='center')

    # Make the title
    title = ctk.CTkLabel(root, text="Converter", font=("Courier", 45, 'bold'), padx=10, pady=7.5, 
                                text_color="chartreuse3")
    title.place(relx=0.5, rely=0.15, anchor='center')

    # Dropdown to choose field of units
    combobox = ctk.CTkComboBox(master=root, values=["--", "Length", "Area", "Volume", "Mass", "Temperature"],
                                    width=200, height=30, corner_radius=8, command=fields, text_color="chartreuse3",
                                    dropdown_font=font, dropdown_text_color="chartreuse3")
    combobox.place(relx=0.5, rely=0.5, anchor='center')
    combobox.set("--") # default option: '--'


# Run the code
menu()
root.mainloop()
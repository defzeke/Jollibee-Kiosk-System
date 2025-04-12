import customtkinter as ctk
import tkinter as tk
from PIL import ImageTk, Image
import sqlite3


def main():
    """
    Initializes the main application window for Ezekiel's Jollibee Kiosk with an SQL database.
    
    Features:
    - Sets the appearance mode and color theme using the `customtkinter` (ctk) library.
    - Creates the main application window with a centered position.
    - Configures a canvas for UI layout.
    - Initializes an inventory frame.
    - Defines the database name for managing inventory.

    Functions:
    - center_window(win, width, height): Centers the given window on the screen.

    """
    
    # Set the theme and appearance mode for the UI
    ctk.set_appearance_mode("light")            # Light mode for better visibility
    ctk.set_default_color_theme("dark-blue")    # Default color theme
    
    def center_window(win, width, height):
        """
        Centers the given window on the screen.

        Parameters:
        - win (Tk or CTk object): The window to be centered.
        - width (int): Width of the window.
        - height (int): Height of the window.

        The function calculates the center position based on screen resolution
        and positions the window accordingly.
        """
        
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        win.geometry(f"{width}x{height}+{x + 130}+{y + 20}")    # Offset for better positioning

     # Create the main application window
    root = ctk.CTk()
    root.geometry("1200x800")                                   # Set the window size
    root.title("Ezekiel's Jollibee Kiosk w SQL database")       # Title of the application
    center_window(root, 1200, 800)                              # Center the window
    
    # Create a canvas for UI layout
    canvas = ctk.CTkCanvas(root, highlightthickness=0, bg="#FFFFFF")
    canvas.pack(fill="both", expand=True)               # Expands to fit the window
    
    # Get screen dimensions for potential responsive layout
    screen_width = root.winfo_width()
    screen_height = root.winfo_height()
    
    # Create an inventory frame to display or manage inventory-related UI
    inventory_frame = tk.Frame(root, bg="black")
    
    # Define the database name for inventory management
    DB_NAME = "C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/database/kioskinventory.db"
    
    
    
    
    
    
    
    
    
    
    def password_screen(event=None):
        """
        Displays the password screen for admin access.

        Features:
        - Hides previous UI elements (inventory, menu, admin access).
        - Creates an entry field for password input with placeholder functionality.
        - Shows an incorrect password message if the input is wrong.
        - Grants access to the admin panel upon correct password entry.
        - Provides a back button to return to the order screen.

        Parameters:
        - event (optional): Used for event-based triggering.

        Global Variables Used:
        - password_frame: Entry field for password input.
        - submit_password_button: Button to submit the password.
        - back_button_icon: Icon for the back button.
        - label, inventory_frame: UI elements removed when opening this screen.
        - password: Hardcoded admin password.
        """
        
        global password_frame, submit_password_button, back_button_icon, label
        
        # Hide previous labels if they exist
        if "label" in globals() and label is not None:
            label.destroy()
            label = None
            
        # Hide inventory frame if it exists
        if "inventory_frame" in globals() and inventory_frame is not None:
            inventory_frame.place_forget()
            inventory_frame = None
        
        # Hide menu elements
        menu_rectangle2.place_forget()
        menu_rectangle.place_forget()
        canvas.delete(admin_secret_access)
        
        # Reset window size and state
        root.geometry("1200x800")  
        root.state("normal")
        
        
        
        def check_password(event=None):        
            """
            Checks the entered password and grants access if correct.

            - Hides the incorrect password message upon success.
            - Displays the incorrect password message if incorrect.
            """
                
            entered_password = password_frame.get()
            if entered_password == password:
                canvas.itemconfig(incorrect_password, state="hidden")
                admin_panel()
            else:
                canvas.itemconfig(incorrect_password, state="normal")
                
        # Display incorrect password message (initially hidden)
        incorrect_password = canvas.create_text(screen_width // 2, screen_height // 2, text="Incorrect Password", font=("Arial", 15, "bold"), fill="red", state="hidden")
        canvas.coords(incorrect_password, 900, 650)
        
        # Load and display back button
        raw_image5 = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/return.png")
        resized_image5 = raw_image5.resize((37, 37), Image.LANCZOS)
        canvas.image5 = ImageTk.PhotoImage(resized_image5)
        back_button_icon = canvas.create_image(screen_width // 2, screen_height // 2, image=canvas.image5)
        canvas.coords(back_button_icon, 50, 50)
        
        # Bind back button to return to order screen
        canvas.tag_bind(back_button_icon, "<Button-1>", order_screen)
        
         # Create password entry field
        password_frame = ctk.CTkEntry(canvas, width=250, height=30, show="", corner_radius=0, border_width=0) 

         # Placeholder text for password entry
        placeholder_text = "Enter password..."
        password_frame.insert(0, placeholder_text)  
        password_frame.configure(text_color="gray") 

        def on_focus_in(event):
            """
            Clears placeholder text and sets input visibility when focused.
            """
            if password_frame.get() == placeholder_text:
                password_frame.delete(0, "end")
                password_frame.configure(text_color="black", show="*")      # Hide input with '*'

        def on_focus_out(event):
            """
            Restores placeholder text if entry is empty.
            """
            if password_frame.get() == "":
                password_frame.insert(0, placeholder_text)
                password_frame.configure(text_color="gray")  
        
        # Bind focus events to entry field
        password_frame.bind("<FocusIn>", on_focus_in)
        password_frame.bind("<FocusOut>", on_focus_out)

         # Place the password entry in the center
        password_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Hardcoded admin password
        password = "admin123"
        
        # Load and display submit button
        raw_image6 = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/submit.png")
        resized_image6 = raw_image6.resize((57, 57), Image.LANCZOS)
        canvas.image6 = ImageTk.PhotoImage(resized_image6)
        submit_password_button = canvas.create_image(screen_width // 2, screen_height // 2, image=canvas.image6)
        canvas.coords(submit_password_button, 1125, 600)
        
        # Bind submit button to password check function
        canvas.tag_bind(submit_password_button, "<Button-1>", check_password)
    
    
    
    
    
    
    
    
    
    
    def order_screen(event=None):
        """
        Displays the order screen, initializing the UI elements for menu selection and order processing.
        
        Features:
        - Hides previous UI elements, including the password entry and admin access button.
        - Configures the main order screen layout with menu options, order summary, and action buttons.
        - Displays an admin access button, allowing navigation to the password screen.
        - Provides UI components for selecting menu items, canceling an order, and proceeding to payment.
        
        Parameters:
        - event (optional): Used for event-based triggering.
        
        Global Variables Used:
        - Various UI elements such as labels, frames, images, and buttons.
        - inventory_frame: Hidden when the order screen is displayed.
        - password_frame, submit_password_button, and back_button_icon: Destroyed if they exist.
        """
        
        global admin_secret_access, password_frame, submit_password_button, menu_rectangle, menu_rectangle2, rectangle_frame1, admin_secret_access, label, back_button_icon
        
        # Hide previous UI elements
        inventory_frame.place_forget()
        if "label" in globals() and label is not None:
            label.destroy()
            label = None
        if "password_frame" in globals() and password_frame is not None:
            password_frame.destroy()
            password_frame = None
        if "back_button_icon" in globals() and back_button_icon is not None:
            canvas.delete(back_button_icon)
            back_button_icon = None
        if "label" in globals() and label is not None:
            label.destroy()
            label = None
        if "submit_password_button" in globals() and submit_password_button is not None:
            canvas.delete(submit_password_button)
            submit_password_button = None
        
        # Remove additional UI elements
        canvas.delete(bg_item2)
        rectangle_frame.place_forget()
        tap_icon_item.place_forget()
        
        # Configure main screen properties
        canvas.config(bg="#231F20")
        root.state("zoomed")
        root.unbind("<Button-1>")
        
         # Load and display admin access button
        raw_image4 = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/jabeeface.png")
        resized_image4 = raw_image4.resize((185, 100), Image.LANCZOS)
        canvas.image4 = ImageTk.PhotoImage(resized_image4)
        admin_secret_access = canvas.create_image(screen_width // 2, screen_height // 2, image=canvas.image4)
        canvas.coords(admin_secret_access, 50, 60)
        canvas.tag_bind(admin_secret_access, "<Button-1>", password_screen)

        # Create bottom order summary bar
        rectangle_frame1 = ctk.CTkFrame(root, width=1707, height=200, corner_radius=10, bg_color="#231F20", fg_color="#DC143C")
        rectangle_frame1.place(x=0, y=870)
        
        # Cancel order button
        child_rectangle_frame1 = ctk.CTkFrame(rectangle_frame1, width=400, height=70, corner_radius=15, border_color="white", border_width=1, bg_color="#DC143C", fg_color="#DC143C")
        child_rectangle_frame1.place(x=75, y=50)
        child_label1 = ctk.CTkLabel(child_rectangle_frame1, text="Cancel", font=("Arial", 20, "bold"), text_color="white")  
        child_label1.place(relx=0.5, rely=0.5, anchor="center")
        
        # Total order price section 
        child_rectangle_frame2 = ctk.CTkFrame(rectangle_frame1, width=400, height=70, corner_radius=15, border_color="white", border_width=1, bg_color="#DC143C", fg_color="#DC143C")
        child_rectangle_frame2.place(x=1230, y=50)
        child_label2 = ctk.CTkLabel(child_rectangle_frame2, text="Total", font=("Arial", 12, "bold"), text_color="white")
        child_label2.place(relx=0.5, y=15, anchor="center")
         
        # Payment button
        child_rectangle_frame3 = ctk.CTkFrame(rectangle_frame1, width=610, height=70, corner_radius=15, border_color="black", border_width=0.5, bg_color="#DC143C", fg_color="#5FBC58")
        child_rectangle_frame3.place(x=550, y=50)
        child_label3 = ctk.CTkLabel(child_rectangle_frame3, text="Pay For Order", font=("Arial", 20, "bold"), text_color="white")  
        child_label3.place(relx=0.5, rely=0.5, anchor="center")
        
        # Left-side menu panel
        menu_rectangle = ctk.CTkFrame(root, width=305, height=760, corner_radius=10, bg_color="#231F20", fg_color="white")
        menu_rectangle.place(x=0, y=80)
        
        menu_rectangle2 = ctk.CTkFrame(root, width=1385.5, height=760, corner_radius=10, bg_color="#231F20", fg_color="white")
        menu_rectangle2.place(x=320, y=80)
        
        # Order Now Icon
        raw_image19 = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/ordernow.png")
        resized_image19 = ctk.CTkImage(light_image=raw_image19, size=(450, 450))
        order_now_icon = ctk.CTkLabel(menu_rectangle2, image=resized_image19, text="")
        order_now_icon.place(relx=0.5, rely=0.5, anchor="center")
        
        # Mini menu panel
        mini_menu_rectangle = ctk.CTkFrame(menu_rectangle, width=301, height=50, corner_radius=10, border_width=0.5, border_color="black", fg_color="white")
        mini_menu_rectangle.place(x=1, y=3)
        mini_menu_label = ctk.CTkLabel(mini_menu_rectangle, text="MENU", font=("Arial", 15))
        mini_menu_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Menu items (Chickenjoy, Burgers, Beverages)
        # Chickenjoy
        raw_image7 = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/jollibee meal.png")
        resized_image7 = ctk.CTkImage(light_image=raw_image7, size=(140, 86))
        
        mini_menu_choice1 = ctk.CTkFrame(menu_rectangle, fg_color="white", width=280, height= 120, border_width=0.5, border_color="black")
        mini_menu_choice1.place(x=11.5, y=70)
        mini_menu_label1 = ctk.CTkLabel(mini_menu_choice1, text="Chickenjoy", font=("Arial", 15))
        mini_menu_label1.place(relx=0.5, y=105, anchor="center")
        mini_image_menu_label1 = ctk.CTkLabel(mini_menu_choice1, text="", image=resized_image7)
        mini_image_menu_label1.place(relx=0.5 ,y=50, anchor="center")
        
        # Menu items (Chickenjoy, Burgers, Beverages)
        # Burgers
        raw_image8 = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/burgers.png")
        resized_image8 = ctk.CTkImage(light_image=raw_image8, size=(140, 87))
        
        mini_menu_choice2 = ctk.CTkFrame(menu_rectangle, fg_color="white", width=280, height= 120, border_width=0.5, border_color="black")
        mini_menu_choice2.place(x=11.5, y=210)
        mini_menu_label2 = ctk.CTkLabel(mini_menu_choice2, text="Burgers", font=("Arial", 15))
        mini_menu_label2.place(relx=0.5, y=105, anchor="center")
        mini_image_menu_label2 = ctk.CTkLabel(mini_menu_choice2, text="", image=resized_image8)
        mini_image_menu_label2.place(relx=0.5 ,y=46, anchor="center")
        
        # Menu items (Chickenjoy, Burgers, Beverages)
        # Beverages
        raw_image9 = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/beverages.png")
        resized_image9 = ctk.CTkImage(light_image=raw_image9, size=(140, 86))
        
        mini_menu_choice3 = ctk.CTkFrame(menu_rectangle, fg_color="white", width=280, height= 120, border_width=0.5, border_color="black")
        mini_menu_choice3.place(x=11.5, y=350)
        mini_menu_label3 = ctk.CTkLabel(mini_menu_choice3, text="Beverages", font=("Arial", 15))
        mini_menu_label3.place(relx=0.5, y=105, anchor="center")
        mini_image_menu_label3 = ctk.CTkLabel(mini_menu_choice3, text="", image=resized_image9)
        mini_image_menu_label3.place(relx=0.5 ,y=50, anchor="center")
        
        # Dictionary to store the quantity of each item ordered
        prices = {"screen_var1": 85.00,
                  "screen_var2": 105.00,
                  "screen_var3": 143.00,
                  "screen_var4": 42.00,
                  "screen_var5": 74.00,
                  "screen_var6": 122.00,
                  "screen_var7": 66.00,
                  "screen_var8": 61.00,
                  "screen_var9": 59.00
                }
                  
        
        def update_total():
            """Updates the total price displayed on the GUI."""
            
            global total
            total = (int(screen_var1.get()) * prices["screen_var1"] +
                     int(screen_var2.get()) * prices["screen_var2"] +
                    int(screen_var3.get()) * prices["screen_var3"] +
                    int(screen_var4.get()) * prices["screen_var4"] +
                    int(screen_var5.get()) * prices["screen_var5"] +
                    int(screen_var6.get()) * prices["screen_var6"] +
                    int(screen_var7.get()) * prices["screen_var7"] +
                    int(screen_var8.get()) * prices["screen_var8"] +
                    int(screen_var9.get()) * prices["screen_var9"])
            total_label.configure(text=f"P{total:.2f}")
        
        def add_order(screen_var):
            """Increases the quantity of a selected item and updates the total."""
            
            current_value = int(screen_var.get())  
            screen_var.set(str(current_value + 1)) 
            update_total()
            

        def subtract_order(screen_var):
            """Decreases the quantity of a selected item (if greater than 0) and updates the total."""
            
            current_value = int(screen_var.get())  
            if current_value > 0: 
                screen_var.set(str(current_value - 1))
                update_total()
                
        
        # Load and resize images for display
        # Chickenjoy Solo
        raw_image10 = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/chickenjoy solo.png")
        resized_image10 = ctk.CTkImage(light_image=raw_image10, size=(220, 146))
        
        # Load and resize images for display
        # Chickenjoy with Drink
        raw_image11 = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/chickenjoy w drink.png")
        resized_image11 = ctk.CTkImage(light_image=raw_image11, size=(215, 143))
        
        # Load and resize images for display
        # Chickenjoy Chickenjoy Double
        raw_image12 = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/chickenjoy double.png")
        resized_image12 = ctk.CTkImage(light_image=raw_image12, size=(215, 143))
        
        # Initialize StringVar variables for screen display or input tracking
        # These variables will be used to store and update values dynamically in the UI
        screen_var1 = ctk.StringVar(value="0")
        screen_var2 = ctk.StringVar(value="0")
        screen_var3 = ctk.StringVar(value="0")
        screen_var4 = ctk.StringVar(value="0")
        screen_var5 = ctk.StringVar(value="0")
        screen_var6 = ctk.StringVar(value="0")
        screen_var7 = ctk.StringVar(value="0")
        screen_var8 = ctk.StringVar(value="0")
        screen_var9 = ctk.StringVar(value="0")
        
        
        # Define the meals function, triggered by an event (e.g., clicking a menu item)
        def meals(event=None):
            
            # Hide the 'Order Now' icon when this function is called
            order_now_icon.place_forget()
            
            # Create a meal frame for "1 pc. Chickenjoy Solo"
            menu_meal1 = ctk.CTkFrame(menu_rectangle2, fg_color="white", width=240, height=240, border_width=0.5, border_color="black")
            menu_meal1.place(x=70, y=70)
            menu_meal_label1 = ctk.CTkLabel(menu_meal1, text="1 pc. Chickenjoy Solo", font=("Arial", 16))
            menu_meal_label1.place(relx=0.5, y=200, anchor="center")
            mini_image_meal_label1 = ctk.CTkLabel(menu_meal1, text="", image=resized_image10)
            mini_image_meal_label1.place(relx=0.5 ,y=110, anchor="center")
            menu_meal_price1 = ctk.CTkLabel(menu_meal1, text="P85.00", font=("Arial", 16))
            menu_meal_price1.place(relx=0.5, y=224, anchor="center")
            
            # Entry field for selecting quantity (linked to screen_var1)
            count1 = ctk.CTkEntry(menu_meal1, textvariable=screen_var1, font=("Arial", 10), width=40, height=10, border_width=0.5, border_color="black", corner_radius=0, justify="center")
            count1.place(relx=0.5, y=20, anchor="center")
            
            # "+" button to increase order quantity
            add1 = ctk.CTkButton(menu_meal1, command=lambda: add_order(screen_var1), width=10, height=10, text="+", hover_color="lime", fg_color="light gray", text_color="black")
            add1.place(x=140, y=9)
            
            # "-" button to decrease order quantity
            subtract1 = ctk.CTkButton(menu_meal1, command=lambda: subtract_order(screen_var1), width=20, height=10, text="-", hover_color="red", fg_color="light gray", text_color="black", font=("Arial", 16))
            subtract1.place(x=80, y=9)
            
            '''
            FOR DOCUMENTATION: BELOW ARE THE SAME FROM ABOVE, IT'S JUST DIFFERENT MENU OPTION
            '''
            
            menu_meal2 = ctk.CTkFrame(menu_rectangle2, fg_color="white", width=240, height=240, border_width=0.5, border_color="black")
            menu_meal2.place(x=340, y=70)
            menu_meal_label2 = ctk.CTkLabel(menu_meal2, text="1 pc. Chickenjoy w/ Drink", font=("Arial", 16))
            menu_meal_label2.place(relx=0.5, y=200, anchor="center")
            mini_image_meal_label2 = ctk.CTkLabel(menu_meal2, text="", image=resized_image11)
            mini_image_meal_label2.place(relx=0.5 ,y=95, anchor="center")
            menu_meal_price2 = ctk.CTkLabel(menu_meal2, text="P105.00", font=("Arial", 16))
            menu_meal_price2.place(relx=0.5, y=224, anchor="center")
            count2 = ctk.CTkEntry(menu_meal2, textvariable=screen_var2, font=("Arial", 10), width=40, height=10, border_width=0.5, border_color="black", corner_radius=0, justify="center")
            count2.place(relx=0.5, y=20, anchor="center")
            add2 = ctk.CTkButton(menu_meal2, command=lambda: add_order(screen_var2), width=10, height=10, text="+", hover_color="lime", fg_color="light gray", text_color="black")
            add2.place(x=140, y=9)
            subtract2 = ctk.CTkButton(menu_meal2, command=lambda: subtract_order(screen_var2), width=20, height=10, text="-", hover_color="red", fg_color="light gray", text_color="black", font=("Arial", 16))
            subtract2.place(x=80, y=9)
            
            
            menu_meal3 = ctk.CTkFrame(menu_rectangle2, fg_color="white", width=240, height=240, border_width=0.5, border_color="black")
            menu_meal3.place(x=610, y=70)
            menu_meal_label3 = ctk.CTkLabel(menu_meal3, text="1 pc. Chickenjoy w/ Double Rice", font=("Arial", 16))
            menu_meal_label3.place(relx=0.5, y=200, anchor="center")
            mini_image_meal_label3 = ctk.CTkLabel(menu_meal3, text="", image=resized_image12)
            mini_image_meal_label3.place(relx=0.5 ,y=95, anchor="center")
            menu_meal_price3 = ctk.CTkLabel(menu_meal3, text="P143.00", font=("Arial", 16))
            menu_meal_price3.place(relx=0.5, y=224, anchor="center")
            count3 = ctk.CTkEntry(menu_meal3, textvariable=screen_var3, font=("Arial", 10), width=40, height=10, border_width=0.5, border_color="black", corner_radius=0, justify="center")
            count3.place(relx=0.5, y=20, anchor="center")
            add3 = ctk.CTkButton(menu_meal3, command=lambda: add_order(screen_var3), width=10, height=10, text="+", hover_color="lime", fg_color="light gray", text_color="black")
            add3.place(x=140, y=9)
            subtract3 = ctk.CTkButton(menu_meal3, command=lambda: subtract_order(screen_var3), width=20, height=10, text="-", hover_color="red", fg_color="light gray", text_color="black", font=("Arial", 16))
            subtract3.place(x=80, y=9)
            
            
        # Bind events to trigger the meals function when clicking menu items
        mini_menu_choice1.bind("<Button-1>", meals)
        mini_image_menu_label1.bind("<Button-1>", meals)
        mini_menu_label1.bind("<Button-1>", meals)
        
           
            
        # Load and resize images for Yumburger menu items
        raw_image13 = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/yumburger solo.png")
        resized_image13 = ctk.CTkImage(light_image=raw_image13, size=(215, 143))
        raw_image14 = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/yumburger w drink.png")
        resized_image14 = ctk.CTkImage(light_image=raw_image14, size=(215, 143))
        raw_image15 = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/yumburger combo.png")
        resized_image15 = ctk.CTkImage(light_image=raw_image15, size=(215, 143))
            
        # Define the burgers function, triggered by an event (e.g., clicking a menu item)
        def burgers(event=None):
            
            order_now_icon.place_forget()
            
            menu_burger1 = ctk.CTkFrame(menu_rectangle2, fg_color="white", width=240, height=240, border_width=0.5, border_color="black")
            menu_burger1.place(x=70, y=70)
            menu_burger_label1 = ctk.CTkLabel(menu_burger1, text="Yumburger Solo", font=("Arial", 16))
            menu_burger_label1.place(relx=0.5, y=200, anchor="center")
            mini_image_burger_label1 = ctk.CTkLabel(menu_burger1, text="", image=resized_image13)
            mini_image_burger_label1.place(relx=0.5 ,y=95, anchor="center")
            menu_burger_price1 = ctk.CTkLabel(menu_burger1, text="P42.00", font=("Arial", 16))
            menu_burger_price1.place(relx=0.5, y=224, anchor="center")
            count1 = ctk.CTkEntry(menu_burger1, textvariable=screen_var4, font=("Arial", 10), width=40, height=10, border_width=0.5, border_color="black", corner_radius=0, justify="center")
            count1.place(relx=0.5, y=20, anchor="center")
            add4 = ctk.CTkButton(menu_burger1, command=lambda: add_order(screen_var4), width=10, height=10, text="+", hover_color="lime", fg_color="light gray", text_color="black")
            add4.place(x=140, y=9)
            subtract4 = ctk.CTkButton(menu_burger1, command=lambda: subtract_order(screen_var4), width=20, height=10, text="-", hover_color="red", fg_color="light gray", text_color="black", font=("Arial", 16))
            subtract4.place(x=80, y=9)
            
            
            menu_burger2 = ctk.CTkFrame(menu_rectangle2, fg_color="white", width=240, height=240, border_width=0.5, border_color="black")
            menu_burger2.place(x=340, y=70)
            menu_burger_label2 = ctk.CTkLabel(menu_burger2, text="Yumburger w/ Drink", font=("Arial", 16))
            menu_burger_label2.place(relx=0.5, y=200, anchor="center")
            mini_image_burger_label2 = ctk.CTkLabel(menu_burger2, text="", image=resized_image14)
            mini_image_burger_label2.place(relx=0.5 ,y=95, anchor="center")
            menu_burger_price2 = ctk.CTkLabel(menu_burger2, text="P74.00", font=("Arial", 16))
            menu_burger_price2.place(relx=0.5, y=224, anchor="center")
            count2 = ctk.CTkEntry(menu_burger2, textvariable=screen_var5, font=("Arial", 10), width=40, height=10, border_width=0.5, border_color="black", corner_radius=0, justify="center")
            count2.place(relx=0.5, y=20, anchor="center")
            add5 = ctk.CTkButton(menu_burger2, command=lambda: add_order(screen_var5), width=10, height=10, text="+", hover_color="lime", fg_color="light gray", text_color="black")
            add5.place(x=140, y=9)
            subtract5 = ctk.CTkButton(menu_burger2, command=lambda: subtract_order(screen_var5), width=20, height=10, text="-", hover_color="red", fg_color="light gray", text_color="black", font=("Arial", 16))
            subtract5.place(x=80, y=9)
           
            
            menu_burger3 = ctk.CTkFrame(menu_rectangle2, fg_color="white", width=240, height=240, border_width=0.5, border_color="black")
            menu_burger3.place(x=610, y=70)
            menu_burger_label3 = ctk.CTkLabel(menu_burger3, text="Yumburger w/ Fries & Drink", font=("Arial", 16))
            menu_burger_label3.place(relx=0.5, y=200, anchor="center")
            mini_image_burger_label3 = ctk.CTkLabel(menu_burger3, text="", image=resized_image15)
            mini_image_burger_label3.place(relx=0.5 ,y=95, anchor="center")
            menu_burger_price3 = ctk.CTkLabel(menu_burger3, text="P122.00", font=("Arial", 16))
            menu_burger_price3.place(relx=0.5, y=224, anchor="center")
            count3 = ctk.CTkEntry(menu_burger3, textvariable=screen_var6, font=("Arial", 10), width=40, height=10, border_width=0.5, border_color="black", corner_radius=0, justify="center")
            count3.place(relx=0.5, y=20, anchor="center")
            add6 = ctk.CTkButton(menu_burger3, command=lambda: add_order(screen_var6), width=10, height=10, text="+", hover_color="lime", fg_color="light gray", text_color="black")
            add6.place(x=140, y=9)
            subtract6 = ctk.CTkButton(menu_burger3, command=lambda: subtract_order(screen_var6), width=20, height=10, text="-", hover_color="red", fg_color="light gray", text_color="black", font=("Arial", 16))
            subtract6.place(x=80, y=9)
           
        # Bind events to trigger the burgers function when clicking menu items
        mini_menu_choice2.bind("<Button-1>", burgers)   
        mini_image_menu_label2.bind("<Button-1>", burgers)
        mini_menu_label2.bind("<Button-1>", burgers) 
            
            
            
        # Loading beverage images and resizing them for the UI
        raw_image16 = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/beverages.png")
        resized_image16 = ctk.CTkImage(light_image=raw_image16, size=(215, 143))    
        raw_image17 = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/coke.png")
        resized_image17 = ctk.CTkImage(light_image=raw_image17, size=(235, 163)) 
        raw_image18 = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/coke float.png")
        resized_image18 = ctk.CTkImage(light_image=raw_image18, size=(235, 163))
            
        # Function to handle the display of the beverages menu
        def beverages(event=None):
            
            order_now_icon.place_forget()
            
            menu_beverage1 = ctk.CTkFrame(menu_rectangle2, fg_color="white", width=240, height=240, border_width=0.5, border_color="black")
            menu_beverage1.place(x=70, y=70)
            menu_beverage_label1 = ctk.CTkLabel(menu_beverage1, text="Iced Tea Regular", font=("Arial", 16))
            menu_beverage_label1.place(relx=0.5, y=200, anchor="center")
            mini_image_beverage_label1 = ctk.CTkLabel(menu_beverage1, text="", image=resized_image16)
            mini_image_beverage_label1.place(relx=0.5 ,y=95, anchor="center")
            menu_beverage_price1 = ctk.CTkLabel(menu_beverage1, text="P66.00", font=("Arial", 16))
            menu_beverage_price1.place(relx=0.5, y=224, anchor="center")
            count1 = ctk.CTkEntry(menu_beverage1, textvariable=screen_var7, font=("Arial", 10), width=40, height=10, border_width=0.5, border_color="black", corner_radius=0, justify="center")
            count1.place(relx=0.5, y=20, anchor="center")
            add7 = ctk.CTkButton(menu_beverage1, command=lambda: add_order(screen_var7), width=10, height=10, text="+", hover_color="lime", fg_color="light gray", text_color="black")
            add7.place(x=140, y=9)
            subtract7 = ctk.CTkButton(menu_beverage1, command=lambda: subtract_order(screen_var7), width=20, height=10, text="-", hover_color="red", fg_color="light gray", text_color="black", font=("Arial", 16))
            subtract7.place(x=80, y=9)
          
            
            menu_beverage2 = ctk.CTkFrame(menu_rectangle2, fg_color="white", width=240, height=240, border_width=0.5, border_color="black")
            menu_beverage2.place(x=340, y=70)
            menu_beverage_label2 = ctk.CTkLabel(menu_beverage2, text="Coke Regular", font=("Arial", 16))
            menu_beverage_label2.place(relx=0.5, y=200, anchor="center")
            mini_image_beverage_label2 = ctk.CTkLabel(menu_beverage2, text="", image=resized_image17)
            mini_image_beverage_label2.place(relx=0.5 ,y=85, anchor="center")
            menu_beverage_price2 = ctk.CTkLabel(menu_beverage2, text="P61.00", font=("Arial", 16))
            menu_beverage_price2.place(relx=0.5, y=224, anchor="center")
            count2 = ctk.CTkEntry(menu_beverage2, textvariable=screen_var8, font=("Arial", 10), width=40, height=10, border_width=0.5, border_color="black", corner_radius=0, justify="center")
            count2.place(relx=0.5, y=20, anchor="center")
            add8 = ctk.CTkButton(menu_beverage2, command=lambda: add_order(screen_var8), width=10, height=10, text="+", hover_color="lime", fg_color="light gray", text_color="black")
            add8.place(x=140, y=9)
            subtract8 = ctk.CTkButton(menu_beverage2, command=lambda: subtract_order(screen_var8), width=20, height=10, text="-", hover_color="red", fg_color="light gray", text_color="black", font=("Arial", 16))
            subtract8.place(x=80, y=9)
            
            
            menu_beverage3 = ctk.CTkFrame(menu_rectangle2, fg_color="white", width=240, height=240, border_width=0.5, border_color="black")
            menu_beverage3.place(x=610, y=70)
            menu_beverage_label3 = ctk.CTkLabel(menu_beverage3, text="Coke Float", font=("Arial", 16))
            menu_beverage_label3.place(relx=0.5, y=200, anchor="center")
            mini_image_beverage_label3 = ctk.CTkLabel(menu_beverage3, text="", image=resized_image18)
            mini_image_beverage_label3.place(relx=0.5 ,y=85, anchor="center")
            menu_beverage_price3 = ctk.CTkLabel(menu_beverage3, text="P59.00", font=("Arial", 16))
            menu_beverage_price3.place(relx=0.5, y=224, anchor="center")
            count3 = ctk.CTkEntry(menu_beverage3, textvariable=screen_var9, font=("Arial", 10), width=40, height=10, border_width=0.5, border_color="black", corner_radius=0, justify="center")
            count3.place(relx=0.5, y=20, anchor="center")
            add9 = ctk.CTkButton(menu_beverage3, command=lambda: add_order(screen_var9), width=10, height=10, text="+", hover_color="lime", fg_color="light gray", text_color="black")
            add9.place(x=140, y=9)
            subtract9 = ctk.CTkButton(menu_beverage3, command=lambda: subtract_order(screen_var9), width=20, height=10, text="-", hover_color="red", fg_color="light gray", text_color="black", font=("Arial", 16))
            subtract9.place(x=80, y=9)
           
           
        # Label to display the total price of the order
        total_label = ctk.CTkLabel(child_rectangle_frame2, text="P0.00", font=("Arial", 25, "bold"), text_color="white")
        total_label.place(relx=0.5, y=38, anchor="center") 
        
        
        # Function to process the order by retrieving quantities from entry fields
        def process_order():
            """
            Processes the current order by fetching the quantities of each item,
            updating the stock accordingly, and refreshing the inventory.
            """
            
            ordered_items = {
                "1 pc. Chickenjoy Solo": int(screen_var1.get() or 0),
                "1 pc. Chickenjoy w/ Drink": int(screen_var2.get() or 0),
                "1 pc. Chickenjoy w/ Double Rice": int(screen_var3.get() or 0),
                "Yumburger Solo": int(screen_var4.get() or 0),
                "Yumburger w/ Drink": int(screen_var5.get() or 0),
                "Yumburger w/ Fries & Drink": int(screen_var6.get() or 0),
                "Iced Tea Regular": int(screen_var7.get() or 0),
                "Coke Regular": int(screen_var8.get() or 0),
                "Coke Float": int(screen_var9.get() or 0),
            }

            # Loop through the ordered items and process only those with a quantity greater than zero
            for item_name, quantity in ordered_items.items():
                if quantity > 0: 
                    update_stock(item_name, -quantity)  # Ensure stock is reduced

            # Refresh inventory after processing the order
            refresh_inventory()

        # Function to confirm the order before proceeding to payment
        def confirm(event=None):
            """
            Displays a confirmation popup before proceeding to payment.
            Ensures the total is greater than 0 before showing the confirmation.
            """
            
            if total > 0.00:
                popup = ctk.CTk()           # Create a pop-up window
                popup.geometry("400x300")
                center_window(popup, 400, 300)  # Center the window
                
                # Confirmation message
                label = ctk.CTkLabel(popup, text=f"NOTE: Please review your orders before paying.\n\nDo you wish to pay P{total}?")
                label.place(relx=0.5, rely=0.5, anchor="center")
                
                # Function to proceed to the thank-you screen after confirming the order
                def proceed_to_thankyou():
                    process_order()          # Process the order before closing
                    popup.destroy()             # Close the popup
                    loading_to_thankyou()   # Navigate to the thank-you screen
                    
                    
                # "Continue" button to confirm the order and proceed to payment
                continue_button = ctk.CTkButton(popup, text="CONTINUE", hover_color="lime", bg_color="white", fg_color="white", border_width=0.5, border_color="black", width=100, corner_radius=0, text_color="black", command=proceed_to_thankyou)
                continue_button.place(x=290, y=260)
                

                popup.mainloop()         # Run the pop-up window
        
        # Binding UI elements to respective functions
        child_rectangle_frame3.bind("<Button-1>", confirm)
        child_label3.bind("<Button-1>", confirm)
        child_label1.bind("<Button-1>", home_screen)
        
        # Bindings for beverage menu selection
        mini_menu_choice3.bind("<Button-1>", beverages)
        mini_image_menu_label3.bind("<Button-1>", beverages)
        mini_menu_label3.bind("<Button-1>", beverages) 
        
        # Binding home screen button
        child_rectangle_frame1.bind("<Button-1>", home_screen)
        
        
        
        
        
        
        
        
        
        
    def home_screen(event=None):
        """
        Displays the home screen of the application and resets the UI elements.

        This function restores the main window to its default state, removing 
        any previously loaded frames or widgets related to inventory, admin access, 
        or thank-you screens. It also sets up the background image, a clickable 
        label prompting the user to tap anywhere to begin, and a tap icon.

        Parameters:
            event (optional): Event parameter for binding with a click event.
        """
        
        global bg_item2, tap_icon_item, rectangle_frame, menu_rectangle, menu_rectangle2, password_frame, admin_secret_access, label, thankyou_wallpaper, processing
        
        # Set main window size and background
        root.geometry("1200x800")  
        root.state("normal")
        canvas.config(bg="white")
        canvas.delete(bg_item)              # Remove previous background if any
        inventory_frame.place_forget()      # Hide the inventory frame if it was open
        
        # Destroy existing UI elements if they exist
        if "processing" in globals() and processing is not None:
            processing.destroy()
            processing = None
        if "thankyou_wallpaper" in globals() and thankyou_wallpaper is not None:
            thankyou_wallpaper.destroy()
            thankyou_wallpaper = None
        if "label" in globals() and label is not None:
            label.destroy()
            label = None
        if "admin_secret_access" in globals() and admin_secret_access is not None:
            canvas.delete(admin_secret_access)
            admin_secret_access = None
        if "password_frame" in globals() and password_frame is not None:
            password_frame.destroy()
            password_frame = None
        if "menu_rectangle2" in globals() and menu_rectangle2 is not None:
            menu_rectangle2.destroy()
            menu_rectangle2 = None
        if "menu_rectangle" in globals() and menu_rectangle is not None:
            menu_rectangle.destroy()
            menu_rectangle = None
        
        # Load and display the home screen background image
        raw_image2 = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/home logo.png")
        resized_image2 = raw_image2.resize((1199, 628), Image.LANCZOS)
        canvas.image2 = ImageTk.PhotoImage(resized_image2)
        bg_item2 = canvas.create_image(screen_width // 2, screen_height // 2, image=canvas.image2, state="normal")
        canvas.coords(bg_item2, 900, 500)
        
        # Create a red rectangle frame at the bottom
        rectangle_frame = ctk.CTkFrame(root, width=1200, height=105, fg_color="#DF0F33")
        rectangle_frame.place(x=0, y=696)
        
        # Label prompting the user to tap anywhere to begin
        rectangle_label = ctk.CTkLabel(rectangle_frame,
                           text="TAP ANYWHERE TO BEGIN",
                           font=("Lalezar", 55, "bold"),
                           text_color="white")
        rectangle_label.place(relx=0.5, rely=0.5, anchor="center")
    
        # Load and display the tap icon
        tap_icon = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/tap.png")
        resized_icon = tap_icon.resize((61, 61), Image.LANCZOS)
        canvas.image3 = ImageTk.PhotoImage(resized_icon)
        tap_icon_item = ctk.CTkLabel(root, image=canvas.image3, text="", bg_color="#DF0F33")
        tap_icon_item.place(x=190, y=725)
        tap_icon_item.lift()        # Bring the icon to the front

        # Bind mouse click to transition to the order screen
        root.bind("<Button-1>", order_screen)
        
        
        
        
        
        
        
        
        
        
    def loading_to_thankyou():
        """
        Displays a processing screen before transitioning to the thank-you screen.

        This function updates the background color to red, hides or removes all 
        existing widgets and text items, and displays a "Processing..." message. 
        After a short delay, it automatically redirects the user to the thank-you screen.

        Global Variables:
            - processing: A label displaying the "Processing..." message.
            - back_button_icon_admin: A reference to the back button icon, deleted if present.

        Behavior:
            - Hides all CTkFrames from the window.
            - Hides any existing text items on the canvas.
            - Deletes the back button icon if it exists.
            - Removes the admin access button if present.
            - Displays the "Processing..." label at the center.
            - Waits for 3 seconds before calling `thankyou_screen`.
        """
        
        global processing, back_button_icon_admin  
        
        # Set background color to red
        canvas.config(bg="#C30217")
        
         # Hide all CTkFrames
        for widget in root.winfo_children():
            if isinstance(widget, ctk.CTkFrame):  
                widget.place_forget()
        
        # Hide all text elements in the canvas
        for item in canvas.find_all():
            if canvas.type(item) == "text":
                canvas.itemconfig(item, state="hidden")
        
        # Delete back button icon if it exists
        if "back_button_icon_admin" in globals() and back_button_icon_admin is not None:
            canvas.delete(back_button_icon_admin)
            back_button_icon_admin = None
            
        # Hide the inventory frame
        inventory_frame.place_forget()
        
        # Remove admin secret access button
        canvas.delete(admin_secret_access)
        
        # Display "Processing..." label at the center of the screen
        processing = ctk.CTkLabel(root, text="Processing...", font=("Cooper Black", 100, "bold"), text_color="white", bg_color="#C30217")
        processing.place(relx=0.5, rely=0.5, anchor="center")
        
        # Transition to thank-you screen after 3 seconds
        root.after(3000, thankyou_screen)
        
        
        
        
        
        
        
        
        
        
    def thankyou_screen():
        """
        Displays the thank-you screen and resets the UI.

        This function updates the background color to red, hides or removes all 
        existing widgets and text elements, and displays a thank-you image.
        After 5 seconds, it automatically transitions back to the home screen.

        Global Variables:
            - thankyou_wallpaper: A CTkLabel displaying the thank-you image.
            - back_button_icon_admin: A reference to the back button icon, deleted if present.

        Behavior:
            - Sets the background color to red.
            - Removes the back button icon if it exists.
            - Hides the inventory frame.
            - Hides all CTkFrames from the window.
            - Hides any existing text items on the canvas.
            - Deletes the admin access button if present.
            - Displays a thank-you image at the center.
            - Waits for 5 seconds before calling `home_screen`.
        """
        
        global thankyou_wallpaper, back_button_icon_admin
        
        # Set background color to red
        canvas.config(bg="#C30217")
        
        # Delete back button icon if it exists
        if "back_button_icon_admin" in globals() and back_button_icon_admin is not None:
            canvas.delete(back_button_icon_admin)
            back_button_icon_admin = None
            
        # Hide the inventory frame
        if "inventory_frame" in globals() and inventory_frame is not None:
            inventory_frame.place_forget()
            inventory_frame = None
        
        # Hide all CTkFrames
        for widget in root.winfo_children():
            if isinstance(widget, ctk.CTkFrame):  
                widget.place_forget()
        
        # Hide all text elements in the canvas
        for item in canvas.find_all():
            if canvas.type(item) == "text":
                canvas.itemconfig(item, state="hidden")
        
        # Remove admin secret access button
        canvas.delete(admin_secret_access)
        
        # Load and display the thank-you image
        thank_raw_image = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/thanksjabee.png")
        resized_thank_image = ctk.CTkImage(light_image=thank_raw_image, size=(1050, 1050))
        thankyou_wallpaper = ctk.CTkLabel(root, image=resized_thank_image, text="")
        thankyou_wallpaper.place(relx=0.5, rely=0.5, anchor="center")
        
        # Transition to the home screen after 5 seconds
        root.after(5000, home_screen)
        
        
        
        
        
        
        
        
        
        
    def loading_screen():
        """
        Displays a loading screen with an image before transitioning to the home screen.

        This function:
            - Hides the inventory frame if it exists.
            - Loads and displays a loading image at the center of the screen.
            - Waits for 3 seconds before automatically switching to the home screen.

        Global Variables:
            - bg_item: Stores the image object on the canvas.

        Behavior:
            - If the inventory frame exists, it is hidden and set to None.
            - A loading image is loaded from the given file path and resized.
            - The image is displayed at the center of the screen.
            - The function calls `home_screen` after 3 seconds.

        """
        
        global bg_item
        
        # Hide inventory frame if it exists
        if "inventory_frame" in globals() and inventory_frame is not None:
            inventory_frame.place_forget()
            inventory_frame = None
        
        # Load and display the loading image
        raw_image = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/LOADINGLOGO.png")
        resized_image = raw_image.resize((1800, 1800), Image.LANCZOS)
        canvas.image = ImageTk.PhotoImage(resized_image)
        bg_item = canvas.create_image(screen_width // 2, screen_height // 2, image=canvas.image)
        canvas.coords(bg_item, 900, 600)
        
        # Transition to the home screen after 3 seconds
        root.after(3000, home_screen)
    
    loading_screen()
    
    
    
    
    
    
    
    
    
    
    def create_database():
        '''
        Creates the kioskinventory database table if it does not exist.

        This function:
            - Connects to the SQLite database.
            - Creates the 'kioskinventory' table with columns: 
                - id (Primary Key, Auto-increment)
                - category (TEXT, required)
                - name (TEXT, required, unique)
                - quantity (INTEGER, default 0)
                - price (REAL, required)
            - Inserts predefined inventory items if the table is empty.
            - Closes the database connection.

        Behavior:
            - If the table does not exist, it is created.
            - If the inventory is empty, initial stock data is inserted.

        '''
        
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Create the table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS kioskinventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            name TEXT NOT NULL UNIQUE,
            quantity INTEGER DEFAULT 0,
            price REAL NOT NULL
        );
        """)
        
        # Initial inventory items
        items = [
            ("Meal", "1 pc. Chickenjoy Solo", 10, 85.00),
            ("Meal", "1 pc. Chickenjoy w/ Drinks", 10, 105.00),
            ("Meal", "1 pc. Chickenjoy w/ Double Rice", 10, 143.00),
            ("Burger", "Yumburger Solo", 15, 42.00),
            ("Burger", "Yumburger w/ Drink", 15, 74.00),
            ("Burger", "Yumburger w/ Fries & Drink", 15, 122.00),
            ("Beverage", "Iced Tea Regular", 20, 66.00),
            ("Beverage", "Coke Regular", 20, 61.00),
            ("Beverage", "Coke Float", 20, 59.00)
        ]

        # Check if the table is empty before inserting initial items
        cursor.execute("SELECT COUNT(*) FROM kioskinventory")
        if cursor.fetchone()[0] == 0:
            cursor.executemany("INSERT INTO kioskinventory (category, name, quantity, price) VALUES (?, ?, ?, ?);", items)
            
        conn.commit()
        conn.close()
        
        
        
        
        
        
        
        
        
          
    def update_stock(item_name, change):
        """
        Updates the stock quantity of a given item.

        Parameters:
            - item_name (str): The name of the item to update.
            - change (int): The amount to increase or decrease stock by.

        This function:
            - Connects to the SQLite database.
            - Updates the stock quantity of the specified item.
            - Ensures that stock does not go below zero.
            - Calls `refresh_inventory()` to reflect the changes.
            - Closes the database connection.

        Behavior:
            - If stock would become negative, the update is not applied.
            - Calls `refresh_inventory()` after updating stock.

        """
        
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Update stock while ensuring it does not go below zero
        cursor.execute("UPDATE kioskinventory SET quantity = quantity + ? WHERE name = ? AND (quantity + ?) >= 0",
                   (change, item_name, change))
        
        
        
        conn.commit()
        conn.close()
        
        # Refresh UI or inventory display
        refresh_inventory()
        
        
        
        
        
        
        
        
        
        
    def get_inventory():
        """
        Retrieves the current inventory from the database.

        This function:
            - Connects to the SQLite database.
            - Fetches all item names and their corresponding stock quantities from the 'kioskinventory' table.
            - Closes the database connection.
            - Returns a list of tuples, where each tuple contains:
                - name (str): The name of the inventory item.
                - quantity (int): The available stock quantity.

        Returns:
            list of tuples: [(item_name, quantity), ...]
        """
        
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Fetch all items with their current stock quantities
        cursor.execute("SELECT name, quantity FROM kioskinventory")
        items = cursor.fetchall()
        
        conn.close()
        return items
    
    
    
    
    
    
    
    
    
    
    def refresh_inventory():
        """
        Refreshes the inventory display by updating item stock quantities in the UI.

        This function:
            - Clears all existing widgets in the `inventory_frame`.
            - Retrieves the latest inventory data from the database.
            - Creates a new row in `inventory_frame` for each item in the inventory.
            - Displays:
                - Item name
                - Stock quantity
                - Buttons to increase or decrease stock levels
            - Calls `update_stock` when the "+" or "-" button is clicked to modify inventory.

        UI Elements:
            - Item Name: Displayed in green text on a black background.
            - Stock Quantity: Displayed in black text on a white background.
            - "+" Button: Increases stock when clicked.
            - "-" Button: Decreases stock when clicked.

        Dependencies:
            - Calls `get_inventory()` to fetch updated stock data.
            - Calls `update_stock()` when modifying stock.

        """
        
        # Clear existing inventory display
        for widget in inventory_frame.winfo_children():
            widget.destroy()

        # Retrieve updated inventory data
        items = get_inventory()
        
        # Display each item in the inventory
        for item in items:
            item_name, quantity = item
            row = tk.Frame(inventory_frame,  bg="black")
            row.pack(fill="x", padx=10, pady=5)
            
            # Item name label
            tk.Label(row, text=item_name, width=30, height=3, anchor="w", bg="black", fg="lime", font=("Arial", 15, "bold")).pack(side="left", padx=5)
            
            # Stock quantity label
            tk.Label(row, text=f"Stock: {quantity}", width=10, height=2, anchor="center", bg="white", font=("Arial", 15)).pack(side="left", padx=5)

            # "+" button to increase stock
            tk.Button(row, text="+", command=lambda name=item_name: update_stock(name, 1), bg="green", fg="white", font=("Arial", 15)).pack(side="right", padx=5)
            
            # "-" button to decrease stock
            tk.Button(row, text="-", command=lambda name=item_name: update_stock(name, -1), bg="red", fg="white", font=("Arial", 15)).pack(side="right", padx=5)
            
            
            
            
            
            
            
            
            
            
    def admin_panel(event=None):
        """
        Displays the Admin Panel for managing inventory stock.

        This function:
            - Hides all active frames and text elements from the main UI.
            - Closes the password entry frame and removes authentication buttons.
            - Sets the application window to full-screen mode.
            - Changes the background color to black.
            - Displays a "Stock Manager" title in green.
            - Adds a back button (with an image) for returning to the order screen.
            - Places the inventory management frame at the center.
            - Calls `refresh_inventory()` to update stock data.

        UI Elements:
            - **Stock Manager Label**: Displays the panel title in lime-green text.
            - **Back Button**: Clicking it navigates back to the `order_screen`.
            - **Inventory Frame**: Displays the inventory items with controls for stock adjustment.

        Dependencies:
            - Calls `refresh_inventory()` to load the latest inventory stock.
            - Calls `order_screen()` when the back button is clicked.

        """
        
        global label, back_button_icon_admin
        
        # Hide all existing frames
        for widget in root.winfo_children():
            if isinstance(widget, ctk.CTkFrame):  
                widget.place_forget()
        
        # Hide text elements on the canvas
        for item in canvas.find_all():
            if canvas.type(item) == "text":
                canvas.itemconfig(item, state="hidden")
        
        # Remove password authentication UI
        password_frame.place_forget()
        canvas.delete(submit_password_button)
        canvas.delete(back_button_icon)
        
        # Maximize window and change background
        root.state("zoomed")
        canvas.config(bg="black")
        
        # Add "Stock Manager" label
        label = ctk.CTkLabel(root, text="Stock Manager", font=("Arial", 44, "bold"), fg_color="black", text_color="lime")
        label.place(x=870, y=40, anchor="center")
        
        # Load back button image
        raw_image = Image.open("C:/Users/Ezekiel/Downloads/PUP/Portfolio/Real Projects/imgs/kiosk images/return.png")
        resized_image = raw_image.resize((37, 37), Image.LANCZOS)
        canvas.imageadmin = ImageTk.PhotoImage(resized_image)
        
        # Create back button
        back_button_icon_admin = canvas.create_image(screen_width // 2, screen_height // 2, image=canvas.imageadmin)
        canvas.coords(back_button_icon_admin, 50, 50)
        
        # Bind back button to return to the order screen
        canvas.tag_bind(back_button_icon_admin, "<Button-1>", order_screen)
        
        # Display inventory frame at the center
        inventory_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Load the latest inventory data
        refresh_inventory()
        
    
    root.resizable(False, False)
    root.mainloop()
    create_database()
main()
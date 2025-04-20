import tkinter as tk
from tkinter import messagebox, scrolledtext
from natural_language_parser import parse_preferences
import interface

class StudySpotGUI:
    """
    A GUI application to recommend study spots in Seoul based on user preferences.

    Attributes
    ----------
    root : tk.Tk
        The main window of the application.
    user_prefs : dict
        Stores user preferences parsed from natural language or guided form.
    """

    def __init__(self, root):
        """
        Initializes the StudySpotGUI class with a root window and sets up the intro screen.

        Parameters
        ----------
        root : tk.Tk
            The root tkinter window passed by the caller.
        """
        self.root = root
        self.root.title("Seoul Study Spot Finder")
        self.root.geometry("720x600")
        self.user_prefs = {}
        self.setup_intro_screen()
    
    def clear_root(self):
        """
        Clears all widgets from the root window.

        This is useful when transitioning between different views or steps in the GUI.
        """
        for widget in self.root.winfo_children():
            widget.destroy()

    def setup_intro_screen(self):
        """
        Sets up the introductory screen where users choose between
        natural language input and a guided CLI-style form.
        """
        self.clear_root()

        tk.Label(
            self.root, text="📍 Seoul Study Spot Finder", 
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        tk.Label(
            self.root, text="How would you like to enter your preferences?", 
            font=("Arial", 14)
        ).pack(pady=10)

        # Natural Language Input Button
        tk.Button(
            self.root, text="🧠 Natural Language", width=30, 
            command=self.setup_nl_input
        ).pack(pady=5)

        # Guided Form Button
        tk.Button(
            self.root, text="📝 Guided Form (CLI-style)", width=30, 
            command=self.launch_guided_form
        ).pack(pady=5)

    def setup_nl_input(self):
        """
        Creates the interface for users to input their preferences using natural language.

        Provides a text area for freeform input and navigation buttons.
        """
        self.clear_root()

        tk.Label(
            self.root, 
            text="Describe the kind of study spot you want:", 
            font=("Arial", 14)
        ).pack(pady=10)

        self.text_entry = scrolledtext.ScrolledText(
            self.root, height=6, width=70, font=("Arial", 12)
        )
        self.text_entry.pack()

        tk.Button(
            self.root, text="Submit", command=self.process_nl_input
        ).pack(pady=10)

        tk.Button(
            self.root, text="← Back", command=self.setup_intro_screen
        ).pack()

    def process_nl_input(self):
        """
        Processes the user’s natural language input.

        Uses the `parse_preferences` function to convert text to structured preferences.
        If parsing fails, it redirects to the guided form instead.
        """
        user_input = self.text_entry.get("1.0", tk.END).strip()

        if not user_input:
            messagebox.showerror("Error", "Please enter a description.")
            return

        parsed = parse_preferences(user_input)
        self.user_prefs.update(parsed)

        if parsed.get("fallback_prompt", False):
            messagebox.showwarning("⚠️", "Could not understand enough. Redirecting to guided form.")
            self.launch_guided_form()
        else:
            self.show_parsed_preferences()


    def show_parsed_preferences(self):
        """
        Displays the structured preferences extracted from the user's natural language input.

        Allows the user to either confirm and proceed or re-enter a new description.
        """
        self.clear_root()

        tk.Label(
            self.root,
            text="Here's what we understood:",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        # Show each parsed preference, skipping fallback_prompt
        for k, v in self.user_prefs.items():
            if k != "fallback_prompt":
                tk.Label(
                    self.root,
                    text=f"{k.replace('_', ' ').title()}: {v}",
                    font=("Arial", 12)
                ).pack()

        # Navigation buttons
        tk.Button(
            self.root,
            text="✅ Continue",
            command=self.ask_origin_and_time
        ).pack(pady=15)

        tk.Button(
            self.root,
            text="← Try Again",
            command=self.setup_nl_input
        ).pack()

    def ask_origin_and_time(self):
        """
        Prompts the user to provide their location and the maximum time they are willing to travel.

        Collects origin (sinseol/dongdaemun) and max_minutes as numerical input.
        """
        self.clear_root()
        self.answers = {}

        # Origin question
        tk.Label(
            self.root,
            text="Where are you coming from? (Sinseol/Dongdaemun)",
            font=("Arial", 13)
        ).pack(pady=10)

        self.origin_entry = tk.Entry(self.root, width=30, font=("Arial", 12))
        self.origin_entry.pack()

        # Max time question
        tk.Label(
            self.root,
            text="Max travel time in minutes?",
            font=("Arial", 13)
        ).pack(pady=10)

        self.time_entry = tk.Entry(self.root, width=30, font=("Arial", 12))
        self.time_entry.pack()

        tk.Button(
            self.root,
            text="Next",
            command=self.store_origin_and_time
        ).pack(pady=10)
    
    def store_origin_and_time(self):
        """
        Stores the user's origin and maximum travel time.

        Validates:
        - Origin must be 'sinseol' or 'dongdaemun'
        - Max travel time must be a positive integer

        If valid, proceeds to explanation style and recommendation mode selection.
        """
        origin = self.origin_entry.get().strip().lower()

        try:
            max_minutes = int(self.time_entry.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number for minutes.")
            return

        # Validate origin and travel time
        if origin not in ["sinseol", "dongdaemun"] or max_minutes <= 0:
            messagebox.showerror("Error", "Invalid input.")
            return

        # Store valid preferences
        self.user_prefs["origin"] = origin
        self.user_prefs["max_minutes"] = max_minutes

        self.ask_explain_and_mode()

    def ask_explain_and_mode(self):
        """
        Asks user to choose:
        - Explanation style (short or long)
        - Recommendation mode (strict vs fallback)

        Sets internal flags to determine output format and logic behavior.
        """
        self.clear_root()

        self.explain_var = tk.StringVar(value="short")
        self.mode_var = tk.StringVar(value="fallback")

        # Explanation style
        tk.Label(self.root, text="Explanation Style:", font=("Arial", 13)).pack()
        tk.Radiobutton(self.root, text="Short", variable=self.explain_var, value="short").pack()
        tk.Radiobutton(self.root, text="Long", variable=self.explain_var, value="long").pack()

        # Recommendation mode
        tk.Label(self.root, text="Recommendation Mode:", font=("Arial", 13)).pack(pady=10)
        tk.Radiobutton(self.root, text="Fallback (ranked)", variable=self.mode_var, value="fallback").pack()
        tk.Radiobutton(self.root, text="Strict (exact only)", variable=self.mode_var, value="strict").pack()

        # Descriptive help
        tk.Label(self.root, text="Short = ✔✘ only | Long = full sentence explanation", font=("Arial", 10, "italic")).pack()
        tk.Label(self.root, text="Strict = must match all preferences exactly", font=("Arial", 10, "italic")).pack()
        tk.Label(self.root, text="Fallback = shows ranked matches even if some preferences are missed", font=("Arial", 10, "italic")).pack()

        # Proceed button
        tk.Button(self.root, text="Next", command=self.get_weights).pack(pady=10)

    def get_weights(self):
        """
        Initializes the weight selection process.

        - Sets explanation mode, recommendation mode, and number of results to return.
        - Filters keys from user_prefs that are eligible for weighting (i.e., not skipped).
        - Begins asking the user how important each preference is.
        """
        self.user_prefs["explain_mode"] = self.explain_var.get()
        self.user_prefs["mode"] = self.mode_var.get()
        self.user_prefs["top_n"] = 3

        # Filter out irrelevant or skipped preferences
        self.weight_keys = [
            k for k in self.user_prefs 
            if k not in ["origin", "max_minutes", "explain_mode", "mode", "top_n", "fallback_prompt"]
            and self.user_prefs[k] != "skip"
        ]
        self.weights = {}
        self.weight_index = 0

        self.ask_weight()

    def ask_weight(self):
        """
        Displays a form asking how important a specific preference is (1 to 5).

        If all relevant preferences have been weighted, sets default weights and
        proceeds to generate results.
        """
        self.clear_root()

        if self.weight_index >= len(self.weight_keys):
            # Store user-defined weights, convert keys to *_weight convention
            for k in self.weight_keys:
                weight_key = k.replace("pref", "weight") if "pref" in k else f"{k}_weight"
                self.user_prefs[weight_key] = self.weights.get(k, 1)

            # Fill in any expected weights not yet set
            expected_weights = [
                "travel_weight", "work_weight", "outlet_weight",
                "vibe_weight", "seating_weight", "price_weight", "late_weight"
            ]
            for w in expected_weights:
                self.user_prefs.setdefault(w, 1)

            self.show_results()
            return

        # Ask for weight of current key
        key = self.weight_keys[self.weight_index]
        formatted = key.replace("_", " ").capitalize()
        tk.Label(self.root, text=f"How important is {formatted}? (1–5)", font=("Arial", 13)).pack(pady=10)

        self.weight_entry = tk.Entry(self.root, width=10, font=("Arial", 12))
        self.weight_entry.pack()

        tk.Button(self.root, text="Next", command=lambda: self.store_weight(key)).pack(pady=10)

    def store_weight(self, key):
        """
        Stores the user-defined weight for a given preference key.

        Parameters:
        -----------
        key : str
            The name of the preference being weighted (e.g., 'vibe_pref').

        Behavior:
        ---------
        - Validates that the input is an integer between 1 and 5.
        - Saves the weight in self.weights.
        - Proceeds to ask the next weight.
        """
        try:
            val = int(self.weight_entry.get().strip())
            if not 1 <= val <= 5:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Enter a number from 1 to 5.")
            return

        self.weights[key] = val
        self.weight_index += 1
        self.ask_weight()


    def launch_guided_form(self):
        """
        Initializes the guided form input flow.

        This method resets the guided input state, sets up the question list,
        and begins asking the user structured, CLI-style questions about preferences.
        """
        self.clear_root()
        self.guided_inputs = {}
        self.guided_questions = [
            ("origin", "Where are you coming from?", ["sinseol", "dongdaemun"]),
            ("max_minutes", "Max travel time in minutes? (e.g., 10, 15, 20)", None),
            ("work_type", "What kind of work?", ["deep_focus", "casual", "group", "skip"]),
            ("outlet_pref", "Power outlet availability?", ["no", "yes", "limited", "skip"]),
            ("vibe_pref", "Vibe preference?", ["quiet", "cozy", "lively", "skip"]),
            ("seating_pref", "Seating preference?", ["booth", "open_table", "lounge", "individual_desk", "skip"]),
            ("price_pref", "Price preference?", ["free", "low", "medium", "skip"]),
            ("open_late", "Open late?", ["yes", "no", "skip"]),
            ("explain_mode", "Explanation style?", ["short", "long"]),
            ("top_n", "How many top spots do you want? (e.g. 3)", None),
            ("mode", "Recommendation mode?", ["strict", "fallback"])
        ]
        self.guided_weights = []
        self.guided_q_index = 0
        self.ask_guided_question()

    def ask_guided_question(self):
        """
        Displays the current guided question based on self.guided_q_index.

        Depending on the question type, this method renders either:
        - A set of radio buttons for predefined options, or
        - A free-entry input field for open-ended responses.
        """
        self.clear_root()

        if self.guided_q_index >= len(self.guided_questions):
            self.ask_guided_weights()
            return

        key, prompt, options = self.guided_questions[self.guided_q_index]

        tk.Label(self.root, text=prompt, font=("Arial", 13)).pack(pady=10)

        self.current_q_key = key
        self.q_var = tk.StringVar()

        if options:
            for opt in options:
                # Display options with capitalized readable formatting
                tk.Radiobutton(
                    self.root,
                    text=opt.replace("_", " ").capitalize(),
                    variable=self.q_var,
                    value=opt,
                    font=("Arial", 12)
                ).pack(anchor="w")
        else:
            # Render free-form entry input if no predefined options
            self.q_entry = tk.Entry(self.root, width=25, font=("Arial", 12))
            self.q_entry.pack()

        tk.Button(self.root, text="Next", command=self.store_guided_answer).pack(pady=10)

    def store_guided_answer(self):
        """
        Stores the user's answer from the guided form interface.

        Behavior:
        ---------
        - Validates the input depending on the question type.
        - Shows fun or helpful info popups for specific answers.
        - Proceeds to the next question or step.
        """
        key = self.current_q_key

        # Get the selected or typed input
        if hasattr(self, 'q_var') and self.q_var.get():
            val = self.q_var.get().strip().lower()
        elif hasattr(self, 'q_entry') and self.q_entry.get().strip():
            val = self.q_entry.get().strip().lower()
        else:
            messagebox.showerror("Error", "Please enter a value.")
            return

        # Validate numerical input
        if key == "max_minutes":
            try:
                val = int(val)
                if val <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "Please enter a positive number.")
                return

        if key == "top_n":
            try:
                val = int(val)
                if val <= 0:
                    val = 3
            except ValueError:
                val = 3

        # Easter egg messages
        if key == "origin":
            if val == "sinseol":
                messagebox.showinfo("Origin Tip", "I hope you had some free coffee from B2 today!")
            elif val == "dongdaemun":
                messagebox.showinfo("Origin Tip", "You should really try SorryNotSorry's Espresso.")

        if key == "max_minutes":
            if val <= 5:
                msg = "Looks like you are in a bit of a rush. We've got you covered!"
            elif 6 <= val <= 15:
                msg = "Looks like you want a light stroll on your way to study!"
            elif 16 <= val <= 30:
                msg = "With that time, you get to see some of Seoul. Cheers!"
            else:
                msg = "It seems like you wanna travel more than study, LOL! But we've got you!"
            messagebox.showinfo("Travel Insight", msg)

        self.guided_inputs[key] = val
        self.guided_q_index += 1
        self.ask_guided_question()


    def ask_guided_weights(self):
        """
        Begins the weighting phase for guided inputs.

        Dynamically selects which weights to ask for based on user preferences.
        Always includes travel time, and only includes others if they weren’t skipped.
        """
        self.clear_root()

        tk.Label(self.root, text="✅ Here's what you selected so far:", font=("Arial", 13, "bold")).pack(pady=10)
        for k, v in self.guided_inputs.items():
            if k not in ["top_n", "mode", "explain_mode"]:
                display = f"{k.replace('_', ' ').capitalize()}: {v}"
                tk.Label(self.root, text=display, font=("Arial", 11)).pack()

        self.weight_keys = [("travel_weight", "travel time")]  # Always ask this

        # Only ask for weight if the user did NOT skip the preference
        for key, label, weight_key in [
            ("work_type", "work type", "work_weight"),
            ("outlet_pref", "power outlet", "outlet_weight"),
            ("vibe_pref", "vibe", "vibe_weight"),
            ("seating_pref", "seating", "seating_weight"),
            ("price_pref", "price", "price_weight"),
            ("open_late", "open late", "late_weight")
        ]:
            if self.guided_inputs.get(key, "skip") != "skip":
                self.weight_keys.append((weight_key, label))

        self.current_weight_index = 0
        self.weight_values = {}

        tk.Button(self.root, text="➡️ Start Weighting", command=self.ask_next_weight).pack(pady=15)

    def ask_next_weight(self):
        """
        Asks the user to assign an importance level (1–5) for each applicable weight.

        This is done one attribute at a time. If all are answered, it proceeds to confirmation.
        """
        self.clear_root()

        # Ensure fallback values for all expected weights
        expected_weights = [
            "travel_weight", "work_weight", "outlet_weight",
            "vibe_weight", "seating_weight", "price_weight", "late_weight"
        ]
        for key in expected_weights:
            self.guided_inputs.setdefault(key, 1)

        # If done, move to summary screen
        if self.current_weight_index >= len(self.weight_keys):
            for key, _ in self.weight_keys:
                self.guided_inputs[key] = self.weight_values[key]
            self.confirm_before_results()
            return

        # Ask for current weight
        key, label = self.weight_keys[self.current_weight_index]
        tk.Label(self.root, text=f"How important is {label}? (1–5)", font=("Arial", 13)).pack(pady=10)

        self.weight_entry = tk.Entry(self.root, font=("Arial", 12), width=10)
        self.weight_entry.pack()

        tk.Button(self.root, text="Next", command=lambda: self.store_weight_value(key)).pack(pady=10)

    def store_weight_value(self, key):
        """
        Stores the importance score entered by the user for a given attribute.

        Expects integer values in the range [1, 5]. Shows error message if invalid.
        """
        try:
            val = int(self.weight_entry.get())
            if val < 1 or val > 5:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a number from 1 to 5.")
            return

        self.weight_values[key] = val
        self.current_weight_index += 1
        self.ask_next_weight()


    def confirm_before_results(self):
        """
        Shows a summary of guided inputs before retrieving results.

        Asks the user whether to keep current mode or switch to the other.
        """
        self.clear_root()

        tk.Label(self.root, text="🎯 Here's a quick summary:", font=("Arial", 14, "bold")).pack(pady=10)
        for k, v in self.guided_inputs.items():
            display = f"{k.replace('_', ' ').capitalize()}: {v}"
            tk.Label(self.root, text=display, font=("Arial", 11)).pack()

        mode = self.guided_inputs.get("mode", "fallback")

        if mode == "fallback":
            tk.Label(self.root, text="👇 Want to switch to strict mode (exact matches only)?", font=("Arial", 12)).pack(pady=10)
            tk.Button(self.root, text="✅ No, show fallback results", command=self.show_guided_results).pack(pady=5)
            tk.Button(self.root, text="🔒 Yes, switch to strict mode", command=self.use_strict_mode).pack(pady=5)
        else:
            tk.Label(self.root, text="👇 Want to switch to fallback mode (ranked recommendations)?", font=("Arial", 12)).pack(pady=10)
            tk.Button(self.root, text="✅ No, show strict results", command=self.show_guided_results).pack(pady=5)
            tk.Button(self.root, text="🌟 Yes, show fallback instead", command=self.use_fallback_mode).pack(pady=5)
        
    def use_strict_mode(self):
        """
        Switches the current recommendation mode to 'strict' (exact match only).

        Updates the internal mode setting in guided_inputs and reruns the result query
        using the strict logic. If no exact matches are found, the user will be informed
        and redirected to fallback mode automatically.
        """
        self.guided_inputs["mode"] = "strict"
        self.show_guided_results()



    def show_guided_results(self):
        """
        Displays the study spot recommendations based on guided input mode.
        """
        self.clear_root()
        mode = self.guided_inputs.get("mode", "fallback")

        if mode == "strict":
            results = interface.run_strict_query(self.guided_inputs)
            if not results:
                messagebox.showinfo("No Matches", "No strict matches found. Switching to fallback.")
                self.guided_inputs["mode"] = "fallback"
                self.show_guided_results()
                return
            self.display_strict_results(results)
        else:
            results = interface.run_fallback_query(self.guided_inputs)
            result_list = results[0]["Results"] if results else []
            self.display_fallback_results(result_list)


    def show_results(self):
        """
        Runs and displays recommendation results based on mode:
        - If 'strict', only exact matches are shown.
        - If 'fallback', shows ranked list based on weighted scores.
        """
        self.clear_root()
        mode = self.user_prefs["mode"]

        if mode == "strict":
            results = interface.run_strict_query(self.user_prefs)
            if not results:
                self.user_prefs["mode"] = "fallback"
                messagebox.showinfo("No Matches", "No exact matches found. Switching to fallback.")
                self.show_results()
                return
            self.display_strict_results(results)
        else:
            results = interface.run_fallback_query(self.user_prefs)
            result_list = results[0]["Results"] if results else []
            self.display_fallback_results(result_list)
    
    def display_fallback_results(self, result_list):
        """
        Redirects to the scrollable results display for fallback mode.
        """
        self.render_scrollable_results(
            prefs=self.user_prefs,
            results=result_list,
            mode=self.user_prefs.get("mode", "fallback")
        )

    def render_scrollable_results(self, prefs, results, mode="fallback"):
        """
        Renders a scrollable, styled interface to display ranked study spot results.

        Includes score, matching bar, detailed explanation, and external link.
        """
        self.clear_root()

        canvas = tk.Canvas(self.root, borderwidth=0)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        bind_scroll(canvas, scrollable_frame)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        mode_label = mode.capitalize()
        tk.Label(scrollable_frame, text=f"🧭 Mode: {mode_label} Matching", font=("Arial", 12, "italic")).pack(pady=(5, 0))
        tk.Label(scrollable_frame, text="📍 Here are your top study spot recommendations:", font=("Arial", 14, "bold")).pack(pady=10)

        for i, (score, name, link, explanation) in enumerate(results, 1):
            match_info, skipped, match_bar = interface.compute_match_info(prefs, score, explanation)
            bar_visual = "█" * match_bar.count("✔") + "░" * (len(match_bar) - match_bar.count("✔"))

            star = "🌟" if i == 1 else ""
            header = f"{i}. {name}{star} — Score: {score} ({match_info})"
            tk.Label(scrollable_frame, text=header, font=("Arial", 12)).pack(anchor="w")

            tk.Label(scrollable_frame, text=f"   ✔ Match Bar: {match_bar} | {bar_visual}", font=("Arial", 10)).pack(anchor="w")
            tk.Label(scrollable_frame, text=f"   📎 {link}", font=("Arial", 10), fg="blue").pack(anchor="w")

            tk.Label(scrollable_frame, text="   🧠 Why:", font=("Arial", 10)).pack(anchor="w")
            for line in explanation.split("  "):
                color = "green" if "✔" in line else "red" if "✘" in line else "black"
                tk.Label(scrollable_frame, text=f"      - {line}", font=("Arial", 10), fg=color).pack(anchor="w")

            tk.Label(scrollable_frame, text="").pack()

        self.end_buttons()

    def display_strict_results(self, results):
        """
        Displays study spots that match all preferences exactly (strict mode).
        """
        self.clear_root()
        tk.Label(self.root, text="🎯 Your Study Spot Picks:", font=("Arial", 14, "bold")).pack(pady=10)

        for i, res in enumerate(results, 1):
            tk.Label(self.root, text=f"{i}. {res['Name']}", font=("Arial", 12)).pack(anchor="w")
            tk.Label(self.root, text=f"   📎 {res['Link']}", font=("Arial", 10), fg="blue").pack(anchor="w")

        self.end_buttons()

    def end_buttons(self):
        """
        Displays final buttons to allow users to restart or exit the program.
        """
        tk.Button(self.root, text="🔁 Try Again", command=self.setup_intro_screen).pack(pady=10)
        tk.Button(self.root, text="❌ Exit", command=self.root.quit).pack()



def bind_scroll(canvas, widget):
    """
    Binds the mousewheel or trackpad scroll event to a scrollable canvas widget,
    handling both Windows/Linux and MacOS systems.
    """
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _on_mac_scroll(event):
        canvas.yview_scroll(-1 * int(event.delta), "units")

    system = canvas.tk.call('tk', 'windowingsystem')
    if system == 'aqua':  # MacOS
        widget.bind("<MouseWheel>", _on_mac_scroll)
    else:
        widget.bind("<MouseWheel>", _on_mousewheel)


if __name__ == "__main__":
    """
    Entry point for the Seoul Study Spot Finder GUI.
    """
    root = tk.Tk()
    app = StudySpotGUI(root)
    root.mainloop()

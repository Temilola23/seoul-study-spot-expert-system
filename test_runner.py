"""
test_runner.py
---------------
Test runner script for the Seoul Study Spot Expert System.

Features:
- Programmatically runs CLI-mode strict and fallback queries
- Launches the GUI interface for interactive testing
- Demonstrates usage with pre-defined test cases for the final report

To use:
$ python3 test_runner.py

Date: April 20, 2025
"""

import interface
import gui_app
import tkinter as tk


def run_strict_test_case():
    """
    Runs a strict mode test case with predefined values and prints the result.
    Use this to demonstrate how strict matching returns exact matches or fails.
    """
    print("\n===== STRICT MODE TEST CASE =====")
    user_inputs = {
        "origin": "sinseol",
        "max_minutes": 12,
        "work_type": "casual",
        "outlet_pref": "yes",
        "vibe_pref": "cozy",
        "seating_pref": "individual_desk",
        "price_pref": "medium",
        "open_late": "yes",
        "travel_weight": 1,
        "work_weight": 1,
        "outlet_weight": 1,
        "vibe_weight": 1,
        "seating_weight": 1,
        "price_weight": 1,
        "late_weight": 1,
        "explain_mode": "long",
        "top_n": 3,
        "mode": "strict"
    }

    results = interface.run_strict_query(user_inputs)
    interface.display_results(user_inputs, results)


def run_fallback_test_case():
    """
    Runs a fallback scoring test case with some preferences skipped,
    showing the scoring and ranking system.
    """
    print("\n===== FALLBACK MODE TEST CASE =====")
    user_inputs = {
        "origin": "dongdaemun",
        "max_minutes": 20,
        "work_type": "deep_focus",
        "outlet_pref": "yes",
        "vibe_pref": "quiet",
        "seating_pref": "booth",
        "price_pref": "skip",      # <-- skipped
        "open_late": "skip",       # <-- skipped
        "travel_weight": 3,
        "work_weight": 5,
        "outlet_weight": 2,
        "vibe_weight": 4,
        "seating_weight": 3,
        "price_weight": 0,
        "late_weight": 0,
        "explain_mode": "short",
        "top_n": 3,
        "mode": "fallback"
    }

    results = interface.run_fallback_query(user_inputs)
    interface.display_results(user_inputs, results)


def launch_gui():
    """
    Launches the Tkinter GUI for interactive expert system testing.
    Allows the demo facilitator or user to test the full pipeline via UI.
    """
    print("\n🚀 Launching GUI mode...")
    root = tk.Tk()
    app = gui_app.StudySpotGUI(root)
    root.mainloop()


if __name__ == "__main__":
    print("🎓 Seoul Study Spot Expert System – Test Runner")
    print("===============================================")
    print("Choose a test to run:")
    print("1. Strict Mode Test")
    print("2. Fallback Mode Test")
    print("3. Launch GUI")
    choice = input("Enter option (1/2/3): ").strip()

    if choice == "1":
        run_strict_test_case()
    elif choice == "2":
        run_fallback_test_case()
    elif choice == "3":
        launch_gui()
    else:
        print("❌ Invalid option. Please enter 1, 2, or 3.")

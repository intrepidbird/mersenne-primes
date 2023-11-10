import tkinter as tk
from tkinter import messagebox
import math

def is_prime(n):
    """
    Checks if a number is prime.

    Parameters:
    - n: int
        The number to be checked.

    Returns:
    - bool:
        True if the number is prime, False otherwise.
    """

    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def generate_mersenne_primes(limit):
    """
    Generates Mersenne primes up to a given limit.

    Parameters:
    - limit: int
        The upper limit for generating Mersenne primes.

    Returns:
    - list:
        A list of Mersenne primes up to the given limit.
    """

    mersenne_primes = []

    for n in range(limit + 1):
        mersenne_number = 2 ** n - 1

        if is_prime(n) and is_prime(mersenne_number):
            mersenne_primes.append(mersenne_number)

    return mersenne_primes

def generate_mersenne_primes_gui():
    """
    Generates Mersenne primes based on user input using a GUI.

    This function creates a GUI window that prompts the user to enter a limit for generating Mersenne primes.
    It then calls the generate_mersenne_primes function to generate the Mersenne primes and displays the result
    in a message box.
    """

    def generate():
        """
        Event handler for the Generate button.

        This function gets the user input from the entry field, calls the generate_mersenne_primes function,
        and displays the result in a message box.
        """

        try:
            limit = int(entry.get())
            mersenne_primes = generate_mersenne_primes(limit)
            messagebox.showinfo("Mersenne Primes", f"The Mersenne primes up to {limit} are: {mersenne_primes}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")

    # Create the GUI window
    window = tk.Tk()
    window.title("Mersenne Primes Generator")

    # Create the label and entry field for user input
    label = tk.Label(window, text="Enter the limit:")
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    # Create the Generate button
    button = tk.Button(window, text="Generate", command=generate)
    button.pack()

    # Start the GUI event loop
    window.mainloop()

# Call the generate_mersenne_primes_gui function to start the Mersenne primes generator GUI
generate_mersenne_primes_gui()

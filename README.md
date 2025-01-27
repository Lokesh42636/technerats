# Expiry Product Detection

This project is a Python-based shopping system that simulates a barcode scanning experience. It validates product expiration, calculates the total cost of selected items, and generates an itemized bill. The system also features a voice alert for expired products using Google Text-to-Speech (`gTTS`).

---

## Features

- **Barcode Scanning**: Users can scan barcodes (input as text) to simulate adding items to their cart.
- **Expiration Validation**: Checks whether a product is expired or within 5 days of expiration and provides a voice alert for such products.
- **Bill Calculation**: Automatically calculates the total price of all valid (non-expired) items.
- **Itemized Bill**: Displays a summary of purchased items with details like name, price, and expiration date.
- **Voice Alert**: Alerts users about expired products through a generated voice message.

---

## How It Works

1. A dictionary stores product details, including barcode, name, price, and expiration date.
2. Users input barcodes to simulate scanning products.
3. The system:
   - Validates the barcode against the product database.
   - Checks the product's expiration date.
   - Plays a voice alert if the product is expired or about to expire.
   - Adds valid products to the bill and updates the total cost.
4. The shopping process ends when the predefined "end code" is entered.
5. A final bill is displayed with the total cost.

---

## Requirements

To run this project, you'll need:

- **Python 3.x**
- Libraries:
  - `gTTS` (for voice alerts)
  - `os` (to play audio files)
  - `datetime` (for date comparisons)

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd barcode-shopping-system
   ```
3. Install the required library:
   ```bash
   pip install gtts
   ```
4. Run the script:
   ```bash
   python shopping_system.py
   ```

---

## Usage

1. Start the program, and it will prompt you to scan barcodes.
2. Enter valid barcodes from the database (e.g., `056044006034` or `8901491502030`).
3. If the product is expired or near expiration, you'll hear a voice alert saying, "This product is expired."
4. To finish shopping, enter the end code: `9781492090793`.
5. View your bill with all purchased items and the total cost.

---

## Example Input and Output

### Input:
```plaintext
scan your barcode
056044006034
scan your barcode
8901491502047
scan your barcode
8901491502030
scan your barcode
9781492090793
```

### Output:
```plaintext
this is: Lays, price is: 10
This product is expired
this is: Lays green, price is: 10
shopping done

Sno  item       price   date1
0    Lays       10      2022,3,21
1    Lays green 10      2023,7,21

your total cost is : Rs.20
```

---

## Project Structure

```plaintext
.
├── shopping_system.py  # Main script to run the shopping system
├── README.md           # Project documentation
```

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.

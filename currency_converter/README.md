# Currency Converter (Live CNB Data)

**Description:** A desktop GUI application that converts Czech Koruna (CZK) into various foreign currencies using real-time exchange rates from the Czech National Bank (CNB). Unlike static converters, this tool fetches the latest daily rates directly from the official CNB source every time it runs.

**Core Technologies:** 
* Python 3
* Tkinter: For the graphical user interface.
* Requests API: To handle HTTP communication with the CNB server.

**Key Features:**
* Dynamic Data Fetching: Automatically downloads the latest exchange rate from CNB.
* Flexible Currency Support: Converts CZK to any currency available in the CNB daily list (e.g., EUR, USD, GBP, JPY).
* Data parsing and cleaning (handling decimal commas vs. dots).
* User-Friendly GUI:
   * Simple input fields for amount and currency code.
   * Visual feedback for successful conversions (green text).
   * Error Handling: Validates if the input is a number and checks if the entered currency code exists (red text alerts).

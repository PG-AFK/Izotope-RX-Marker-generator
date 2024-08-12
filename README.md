# Text Reformatter App

A simple GUI application for formatting text to be compatible with iZotope RX marker import. This app allows users to paste text into a text field and export it as a formatted `.txt` file. The text formatting follows a specific format required by iZotope RX.

## Features

- Paste text into a text field
- Format the text according to iZotope RX requirements
- Export the formatted text to a `.txt` file

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/TextReformatter.git
    cd TextReformatter
    ```

2. **Install dependencies:**

    Ensure you have Python 3.12 or higher installed. You can use a virtual environment for this:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

    If you don't have `pip` installed, you can install it using Homebrew:

    ```bash
    brew install pip
    ```

    Then, install `tkinter` if it's not already installed:

    ```bash
    brew install python-tk
    ```

3. **Run the application:**

    ```bash
    python reformat_text_app.py
    ```

## Usage

1. Open the application.
2. Paste your text into the provided text field.
3. Click on "Format and Save."
4. Choose the location and file name to save the formatted text.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Make sure to follow the code style and include tests for any new features or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [iZotope RX](https://www.izotope.com/en/products/rx.html) for their marker import functionality
- Python and Tkinter for making this project possible

<p align="center">
  <img src="logo.png" alt="Alt Text">
</p>


*Organización y Comportamiento Organizacional* (ICS2813) is a course where +300 students have to write essays and assess each other on a weekly basis. However, we found the peer assessment process to be **excessively time-consuming...**
## Table of Contents

- [About Limequick](#about-limequick)
- [Roadmap](#roadmap)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

<a name="about-limequick"></a>
# About Limequick 🍋
Without Limequick the process goes like this:
- Download the essay to be assessed 💤
- Download the template to write positive and negative feedback (.docx) 😫
- Save the template with the comments as PDF 😢
- Use PDF editing tools to merge the essay and your feedback PDFs 😴
- Rename the merged result PDF to match the initial file name of the essay (which is an encoded hard to follow string) 💀
- Upload to the official platform and assign a score ⚰️

Guess what... this steps are followed **TWICE** every week with a single-day deadline!

With Limequick this nightmare ENDS 🥳:
- Download the essay and upload it to Limequick web app 🌈
- Write your feedback in the text fields 💡
- Click to download the file with all requirements met 🌞
- Upload to the official platform and assign a score 🏁

# Roadmap 🚩

The development of Limequick is an ongoing process, and we have an exciting roadmap ahead to enhance its features and functionality. Here are some of the planned milestones and goals:

## Version 0.1 (Current Version)

- [x] Basic .docx feedback insertion capabilities.
- [x] User-friendly web app.

## Upcoming Features

- [ ] .docx to .pdf conversion.
- [ ] Seamless integration with official platforms.

We're always working to make Limequick even better. If you have suggestions or feature requests, feel free to open an issue or contribute to the project!

Keep an eye on our and updates as we continue to evolve Limequick.


# Requirements

- Poetry (dependency management)
- Pyenv (python version management)

# Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/MrBased/Limequick.git
2. Install dependencies:

   ```bash
   poetry install
   ```
3. Run the application:

   ```bash
    poetry run python src/app.py
    ```

# Usage
1. **Run the Application**

   To start the Flask application, open a terminal or command prompt, navigate to the project directory, and run the following command:

   ```bash
   python app.py
   ```

2. **Access the Web App**

   Open a web browser and navigate to http://localhost:5000/ or http://127.0.0.1:5000/. You will be presented with the Limequick web app.

3. **Fill Out the Form**
  
   Enter the number of positive comments and suggestions for improvement that you want to add.
   Add your comments in the respective text input fields.
   Click the "Generate Document" button to create a document with the comments and save it as a .docx.

   (.pdf coming soon... 👀).

4. **Download the document**
  
   After generating the docx, a download link will appear on the page if the docx was successfully created. Click the "Download" button to download the docx document.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

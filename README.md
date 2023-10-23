<p align="center">
  <img src="logo.png" alt="Alt Text">
</p>


*Organización y Comportamiento Organizacional* (ICS2813) is a course where +300 students have to write essays and assess each other on a weekly basis . However, we found the peer assessment process to be **unnecessarily long**...
## Table of Contents

- [About Limequick](#about-limequick)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

<a name="about-limequick"></a>
# About Limequick
Without Limequick the process goes like this 😫:
- Download the essay to be assessed
- Download the template to write positive and negative feedback (.docx)
- Save the template with the comments as PDF
- Use PDF editing tools to merge the essay and your feedback PDFs
- Rename the merged result PDF to match the initial file name of the essay (which is an encoded hard to follow string)
- Upload to the official platform and assign a score

Guess what... this steps are followed **TWICE** every week with a single day deadline!

With Limequick this nightmare ENDS 🥳:
- Download the essay and upload it to Limequick web app
- Write your feedback in the text fields
- Click to download the file with all requirements met
- Upload to the official platform and assign score

## Requirements

- Poetry (dependency management)
- Pyenv (python version management)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/MrBased/Limequick.git
2. Install dependencies:

   ```bash
   poetry install
   ```
3. Run the application:

   ```bash
    poetry run python write.py
    ```

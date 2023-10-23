from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt
import os


class DocWriter():

    insert_paragraph_index1 = 8
    insert_paragraph_index2 = 13

    def __init__(self):
        self.template_path = os.path.join("src", "TemplateLime.docx")
        self.new_file_path = os.path.join("src", "static", "result.docx")
        self.new_document = Document(self.template_path)

    def set_document(self):
        self.new_document = Document(self.template_path)

    def save_document(self):
        self.new_document.save(self.new_file_path)

    def insert_text_with_bullet(self, paragraph_index, text):
        paragraph = self.new_document.paragraphs[paragraph_index]

        paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT

        run = paragraph.add_run("- ")
        run.font.name = "Arial"
        run.font.size = Pt(11)
        run.add_text(" ")
        run.add_text(text)
        paragraph.add_run("\n")

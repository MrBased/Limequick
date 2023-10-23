from flask import Flask, render_template, request, send_file
from write import DocWriter
import os


insert_paragraph_index1 = 8
insert_paragraph_index2 = 13

app = Flask(__name__)
writer = DocWriter()


app.config['UPLOAD_FOLDER'] = 'uploads'
uploads_dir = os.path.join(app.root_path, 'uploads')

if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        n_good_comments = int(request.form['n_good_comments'])
        n_bad_comments = int(request.form['n_bad_comments'])

        writer.set_document()

        for _ in range(n_good_comments):
            comment = request.form.get('good_comment')
            writer.insert_text_with_bullet(insert_paragraph_index1, comment)

        for _ in range(n_bad_comments):
            comment = request.form.get('bad_comment')
            writer.insert_text_with_bullet(insert_paragraph_index2, comment)

        writer.save_document()

        return render_template('index.html', pdf_created=True)
    return render_template('index.html', pdf_created=False)


@app.route('/download_pdf')
def download_pdf():
    pdf_path = "static/result.docx"
    return send_file(pdf_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)

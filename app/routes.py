from flask import Flask, render_template, request, session, send_file, Response
from werkzeug.datastructures import FileStorage
from app.utils import Md2Pdf, cleanup_dir
import os
import uuid

def init_routes(app: Flask) -> None:
    @app.route('/', methods=['GET'])
    def index() -> str:
        cleanup_dir(app.config['UPLOAD_FOLDER'])
        cleanup_dir(app.config['DOWNLOAD_FOLDER'])
        return render_template('index.html')

    @app.route('/convert-to-pdf', methods=['POST'])
    def convert_to_pdf() -> str|Response:
        md_file: FileStorage = request.files['markdown_file']
        try: 
            md_filename: str = f'{str(uuid.uuid4())}.md'
            md_filepath: str = os.path.join(app.config['UPLOAD_FOLDER'], md_filename)
            md_file.save(md_filepath)
            md2pdf = Md2Pdf()
            md2pdf.loadFile(md_filepath)
            pdf_savepath: str = os.path.join(app.config['DOWNLOAD_FOLDER'], f'{md_filename}.pdf')
            md2pdf.makePdf(pdf_savepath)
            return send_file(pdf_savepath, as_attachment=True, download_name='converted.pdf')
        except KeyError:
            return render_template('index.html')
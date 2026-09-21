from markdown_pdf import MarkdownPdf, Section
import os

class Md2Pdf(MarkdownPdf):
	def __init__(self, *args, **kwargs):
		super(Md2Pdf, self).__init__(*args, **kwargs)

	@property
	def content(self) -> str:
		return self._content

	@content.setter
	def content(self, value: str) -> None:
		if not isinstance(value, str):
			raise TypeError('content must be of type string')
		self._content = value
	
	def loadFile(self, filePath: str) -> str|None:
		try:
			with open(filePath) as file:
				self._content: str = file.read()
				
		except FileNotFoundError:
			return 'file not found!'

	def makePdf(self, outFileName: str) -> None:
		self.add_section(Section(self._content))
		if outFileName[-4:] == '.pdf':
			self.save(outFileName)
		else:
			self.save(f'{outFileName}.pdf')

def cleanup_dir(dir_name: str) -> None:
        for file_name in os.listdir(dir_name):
            file_path: str = os.path.join(dir_name, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
			
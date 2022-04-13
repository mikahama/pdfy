from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import base64
import os
#python 3
from urllib.parse import urlparse, urljoin
from urllib.request import pathname2url
py_version = 3


class Pdfy():
	def __init__(self, executable_path=None, debug_port=9222):
		chrome_options = Options()
		chrome_options.add_argument("--remote-debugging-port=" + str(debug_port))
		chrome_options.add_argument("--headless")

		webdriver_params = {
			'chrome_options': chrome_options
		}
		if executable_path:
			webdriver_params['executable_path'] = executable_path

		self.driver = webdriver.Chrome(**webdriver_params)

	def __del__(self):
		try:
			self.driver.quit()
		except:
			pass

	def __resolve_path(self, html_path):
		if self.__is_url(html_path):
			return html_path
		elif os.path.isabs(html_path):
			return self.__path_to_url(html_path)
		abs_path = os.path.abspath(html_path)
		return self.__path_to_url(abs_path)

	def __is_url(self, url):
			return urlparse(url).scheme != ""

	def __path_to_url(self, path):
		return urljoin('file:', pathname2url(path))

	def html_to_pdf(self, html_path, pdf_path = None, options={"paperWidth": 8.3, "paperHeight":11.7, "marginTop": 0, "marginBottom":0, "marginLeft":0, "marginRight":0}):

		self.driver.get(html_path)
 
		pdf_data = self.driver.execute_cdp_cmd("Page.printToPDF",options)
		pdf_data = pdf_data["data"]
		if pdf_path is None:
			return pdf_data
		else:
			f = open(pdf_path, "wb")
			if py_version == 2:
				f.write(base64.decodestring(pdf_data))
			else:
				f.write(base64.b64decode(pdf_data))
			f.close()



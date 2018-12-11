import requests
import logging
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

class SpirelogsUploader():
	def __init__(self, username=None, password=None):
		self.username = username
		self.password = password
		self.cookies = None

	def login(self):
		if self.username != None and self.password != None:
			response = requests.post("https://spirelogs.com/", {'action': 'login', 'username': self.username, 'password': self.password},
																headers={'host': 'spirelogs.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
			self.cookies = response.cookies
			# print(response.text)
			return True if self.username in response.text else False
		else:
			return False

	def upload_run(self, file):
		file = {'file': file}
		response = requests.post("https://spirelogs.com/multiupload.php", files=file, cookies=self.cookies)
		if 'successfully' in response.text or 'recorded' in response.text:
			return True
		else:
			return False

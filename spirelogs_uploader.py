import requests


class SpirelogsUploader():
	def __init__(self, username=None, password=None):
		self.username = username
		self.password = password
		self.cookies = None

	def login(self):
		if username != None and password != None:
			response = requests.post("https://spirelogs.com/pages/profile.php", {'action': 'login', 'username': self.username, 'password': self.password})
			self.cookies = response.cookies
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

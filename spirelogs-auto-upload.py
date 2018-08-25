import requests


class SpirelogsUploader():
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def login(self):
		response = requests.post("https://spirelogs.com/pages/profile.php", {'action': 'login', 'username': self.username, 'password': self.password})
		self.cookies = response.cookies
		return True if self.username in req.cookies else False

	def upload_runs(self, files):
		response = requests.post("https://spirelogs.com/multiupload.php", files=files, cookies=self.cookies)
		if 'successfully' in response.text or 'recorded' in response.text:
			return True
		else:
			return False




				






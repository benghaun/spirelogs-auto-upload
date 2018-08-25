from watchdog.events import FileSystemEventHandler

class SpirelogsFileListener(FileSystemEventHandler):
	def __init__(self, uploader):
		super().__init__()
		self.uploader = uploader

	def on_created(self, event):
		if not event.is_directory and event.src_path.endswith('.run'):
			print("New run detected, uploading..")
			if self.uploader.login():
				self.uploader.upload_run(open(event.src_path, 'rb'))
			else:
				print("Invalid username or password configured")



import os
import sys
import time
from watchdog.observers import Observer
from config import username, password, directory_to_files
from spirelogs_uploader import SpirelogsUploader
from spirelogs_file_listener import SpirelogsFileListener


if __name__ == '__main__':
	uploader = SpirelogsUploader(username, password)
	# upload all existing files
	if '--upload' in sys.argv:
		# iterate through all run files and upload them
		for folder in os.listdir(directory_to_files):
			if os.path.isdir(os.path.join(directory_to_files,folder)) and folder != "DAILY":
				all_filenames = [file for file in os.listdir(os.path.join(directory_to_files, folder)) if file.endswith('.run')]
				if uploader.login() or (username is None and password is None):
					print("Uploading %s runs now" % folder.lower())
					num_uploaded = 0
					for filename in all_filenames:
						uploaded = uploader.upload_run(open(os.path.join(directory_to_files, folder, filename), 'rb'))
						if uploaded:
							num_uploaded += 1
							if num_uploaded == len(all_filenames):
								print("%d/%d uploaded" % (num_uploaded, len(all_filenames)))
							else:
								print("%d/%d uploaded" % (num_uploaded, len(all_filenames)), end="\r")
						else:
							print("upload failed for file %s" % filename)
				else:
					print("Invalid username/password configured")
					break
	# watch folder and upload if there are any new runs
	else:
		handler = SpirelogsFileListener(uploader)
		observer = Observer()
		observer.schedule(handler, directory_to_files, recursive=True)
		observer.start()
		try:
			while True:
				time.sleep(1)
		except KeyboardInterrupt:
			print("Stopping...")
			observer.stop()
		observer.join()

						

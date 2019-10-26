from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
from datetime import datetime
from time import strftime

class MyHandler(FileSystemEventHandler):
	def on_modified(self, event):		# Anytime something new happens to the folder_to_track, it triggers this on_modified method.
		for filename in os.listdir(folder_to_track):	# os.listdir returns a list of the files and other directories in the given directory.
			i = 1
			if filename != "Utkarsh Kumar" and filename != "AutoCleaner.py":	# don't want to add the folder to itself or the script running to the folder.
				new_name = filename
				extension = 'noname'
				try:
					extension = str(os.path.splitext(folder_to_track + '\\' + filename)[1])
					path = extension_folder[extension]
				except Exception:
					extension = 'noname'	

				now = datetime.now()
				year = now.strftime("%Y")
				month = now.strftime("%m")

				folder_destination_path = extension_folder[extension]

				year_exists = False
				month_exists = False

				for folder_name in os.listdir(extension_folder[extension]):
					if folder_name == year:
						folder_destination_path = extension_folder[extension] + "\\" + year
						year_exists = True
						
						for folder_month in os.listdir(folder_destination_path):
							if month == folder_month:
								folder_destination_path = extension_folder[extension] + "\\" + year + "\\" + month
								month_exists = True
				if year_exists == False:
					os.mkdir(extension_folder[extension] + "\\" + year)
					folder_destination_path = extension_folder[extension] + "\\" + year
				if month_exists == False:
					os.mkdir(extension_folder[extension] + "\\" + year + "\\" + month)
					folder_destination_path = extension_folder[extension] + "\\" + year + "\\" + month
				

				file_exists = os.path.isfile(folder_destination_path + "\\" + new_name)						
				while file_exists:
					i += 1
					new_name = os.path.splitext(folder_to_track + '\\' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '\\' + filename)[1]
					new_name = new_name.split("\\")[4]
					file_exists = os.path.isfile(folder_destination_path + "\\" + new_name)

				src = folder_to_track + "\\" + filename

				new_name = folder_destination_path + "\\" + new_name
				os.rename(src, new_name)


extension_folder = {
	#No name
    'noname' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Uncategorized",
#Audio
    '.midi' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Audio",
    '.mp3' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Audio",
    '.wav' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Audio",
    '.wma' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Audio",
    '.wpl' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Audio",
    '.m3u' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Audio",
#Text
    '.txt' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\TextFiles",
    '.doc' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Microsoft\\Word",
    '.docx' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Microsoft\\Word",
    '.pdf': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\PDF",
    '.wks ': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\TextFiles",
    '.wps': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\TextFiles",
    '.wpd': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\TextFiles",
#Video
    '.3g2': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Video",
    '.3gp': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Video",
    '.avi': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Video",
    '.flv': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Video",
    '.h264': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Video",
    '.m4v': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Video",
    '.mkv': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Video",
    '.mov': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Video",
    '.mp4': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Video",
    '.mpg': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Video",
    '.mpeg': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Video",
    '.rm': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Video",
    '.swf': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Video",
    '.vob': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Video",
    '.wmv': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Video",
#Images
    '.ai': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Images",
    '.bmp': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Images",
    '.gif': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Images",
    '.ico': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Images",
    '.jpg': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Images",
    '.jpeg': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Images",
    '.png': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Images",
    '.ps': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Images",
    '.psd': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Images",
    '.svg': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Images",
    '.tif': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Images",
    '.tiff': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Images",
    '.CR2': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Media\\Images",
#Internet
    '.asp': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Internet",
    '.aspx': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Internet",
    '.cer': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Internet",
    '.cfm': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Internet",
    '.cgi': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Internet",
    '.pl': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Internet",
    '.css': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Internet",
    '.htm': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Internet",
    '.js': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Internet",
    '.jsp': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Internet",
    '.part': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Internet",
    '.php': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Internet",
    '.xhtml': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Internet",
#Compressed
    '.rar': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Compressed",
    '.rpm': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Compressed",
    '.z': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Compressed",
    '.zip': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Compressed",
#Disc
    '.bin': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Disc",
    '.dmg': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Disc",
    '.iso': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Disc",
    '.toast': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Disc",
    '.vcd': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Disc",
#Data
    '.csv': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Programming\\Database",
    '.dat': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Programming\\Database",
    '.db': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Programming\\Database",
    '.dbf': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Programming\\Database",
    '.log': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Programming\\Database",
    '.sql': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Programming\\Database",
    '.xml': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Programming\\Database",
    '.json': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Programming\\Database",
#Executable Files
    '.apk': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Executable Files",
    '.bat': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Executable Files",
    '.com': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Executable Files",
    '.exe': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Executable Files",
    '.gadget': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Executable Files",
    '.jar': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Executable Files",
    '.wsf': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Other\\Executable Files",
#Presentations
    '.key': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Presentations",
    '.odp': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Presentations",
    '.pps': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Presentations",
    '.ppt': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Presentations",
    '.pptx': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Presentations",
#Programming
    '.c': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Programming\\C&C++",
    '.py': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Programming\\Python",
    '.sh': "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Programming\\Shell",
#Spreadsheets
    '.ods' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Microsoft\\Excel",
    '.xlr' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Microsoft\\Excel",
    '.xls' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Microsoft\\Excel",
    '.xlsx' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Microsoft\\Excel",
#System
    '.bak' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Other\\System",
    '.cab' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Other\\System",
    '.cfg' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Other\\System",
    '.cpl' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Other\\System",
    '.cur' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Other\\System",
    '.dll' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Other\\System",
    '.dmp' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Other\\System",
    '.drv' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Other\\System",
    '.icns' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Other\\System",
    '.ico' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Other\\System",
    '.ini' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Other\\System",
    '.lnk' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Other\\System",
    '.msi' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Other\\System",
    '.sys' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Other\\System",
    '.tmp' : "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar\\Text\\Other\\System",
}


folder_to_track = "C:\\Users\\Utkarsh Kumar\\Desktop"
folder_destination_path = "C:\\Users\\Utkarsh Kumar\\Desktop\\Utkarsh Kumar"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
	while True:
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop()

observer.join()


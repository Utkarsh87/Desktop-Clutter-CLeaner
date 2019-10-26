# Desktop-Clutter-Cleaner
Python script that organizes the files added to the Desktop into a target folder with sub-division into lower level directories and organized by year and month of addition of the file onto the desktop.

The script can be run as a background process everytime the OS(Windows, in my case) fires up, by creating a Batch(.bat) file and saving it into the startup folder(in the case of Windows OS).

Watchdog library was used to track the changes being made to or the processes occuring on the desktop.

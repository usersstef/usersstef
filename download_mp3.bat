@echo off
set /p userinput=%cd%^>yt-dlp -x --audio-format mp3 
yt-dlp -x --audio-format mp3  %userinput%
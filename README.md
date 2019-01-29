# Winter2019Rover
Initial commit is backup of current state of Rover
## To Push To Rover
Note: git repo is not set up on the rover itself.
### Using microSD card:
With microSD card inserted, navigate to directory `/home/pi`.
Copy files over as normal.
### Over Wifi:
Connect PC wifi to SSID: `Sung-net` Password: `Sungvibe`
Use a ssh command prompt (such as Git Bash or MobaXTerm) to open SSH connection to the rPi: `ssh 172.24.1.1 -l pi` Password: `SungGate`
(user = `pi`, password = `SungGate`. Over MobaXTerm, `-l` arg not needed.)
Copy files over as normal.
##Contributing:
When pushing a commit to GitHub repo, note if files were updated on rover in commit message.
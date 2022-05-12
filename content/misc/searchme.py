bashCommand = "grep -Ri \"distil\" /Users/ahmadbadary/github/AhmedBadary.github.io/content/"
import subprocess
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

print(output)
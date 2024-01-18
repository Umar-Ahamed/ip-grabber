import socket
import random
import pyperclip
import subprocess
import sys

import subprocess
import sys

def install_packages():
    required_packages = ['pyperclip']

    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing {package}...")
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
                print(f"{package} installed successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error installing {package}: {e}")

# Install required packages
install_packages()

def get_local_ip():
    try:
        # Use a socket to get the local IP address
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]

        return local_ip

    except socket.error as e:
        print(f"Error: {e}")
        return None

# Assigning text content directly to variables
usernames_text = """you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you"""

greeting_names_text = """you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you"""

# Combine the contents of usernames_text, greeting_names_text, and the local IP
local_ip = get_local_ip()
combined_output = f"{usernames_text}\nLocal IP address: {local_ip}{greeting_names_text}\n"

# Print the combined output
print(combined_output)

# Copy the combined output to the clipboard
pyperclip.copy(combined_output)


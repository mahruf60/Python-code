# Create a virtual environment
python -m venv myenv

# Activate the virtual environment (Linux/macOS)
source myenv/bin/activate

# Activate the virtual environment (Windows)
myenv\Scripts\activate.bat
myenv\Scripts\Activate.ps1     #usin for powershell


# Deactivate the virtual environment
deactivate

# Output the list of installed packages and their versions to a file
pip freeze > requirements.txt

# Install the packages listed in the requirements.txt file
pip install -r requirements.txt

#pip install pandas
import pandas as pd
print(pd.__version__)
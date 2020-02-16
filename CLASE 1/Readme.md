# Download Anaconda Enviroment 3.7 version
- https://www.anaconda.com/distribution/#download-section

# Install and prepare
	sudo bash Anaconda3-2019.10-Linux-x86_64.sh  (Linux)
	- Execute Anaconda3-2019.10-Linux-x86_64.exe  (Windows)
	# Open terminal : 
	conda create --name umaker python==3.7
	conda activate env_name  
	conda install -c conda-forge name_library
	Example: conda install -c conda-forge opencv # install library
# Check libraries
	conda list 
## Export yml enviroment
	conda env export > env_name.yml
## Create enviroment from yml file
	conda env create -f env_name.yml




# Download Anaconda Enviroment 3.7 version
- https://www.anaconda.com/distribution/#download-section

# Install and prepare enviroment
	sudo bash Anaconda3-2019.10-Linux-x86_64.sh
	conda create --name umaker python==3.7
	conda activate umaker
	conda install -c conda-forge opencv # install library

## Export yml enviroment
	conda env export > umake.yml
## Create enviroment from yml file
	conda env create -f umake.yml




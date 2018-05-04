# pyJGI_API
Contains function allowing for downloading of IMG genome data through their API.

The function is based on the API instructions found at https://genome.jgi.doe.gov/portal/help/download.jsf

The function uses pycurl to interact with the JGI Genome Portal and parses the xml output corresponing to each genome in order to find the particular file corresponding to the tar bundle. It then send a request to download the tar bundle file.


Instructions:

1) Make sure the JGI_download file is in the folder you would like to download the IMG tar files to
2) In a terminal open change to the directory where you would like to download the IMG tar files
3) Start python from the command line
4) In python run: from JGI_download import IMG_download
5) use the funtion IMG_download(file, 'username', 'password') to obtain files from the JGI Genome portal

file = a .txt file containing IMG genome id's
username = your IMG username/email entered as a string in quotes
password = your IMG account password entered as a string in quotes


Notes:

Minor changes to the IMG_download function will enable it to download the other files available on the Genome Portal such as just the .fna file or just the .gff file. However, downloading the tar bundle is the quickest way to obtain all potentially desired files.

The IMG_download function only works on genomes in IMG. Some changes to the function might enable it to download files from other JGI related databases. However, I built it with the intent to specifically download IMG genome files.

If you are working with private genomes from the IMG MER database you must use your login credentials to download via this function or using the JGI API with curl in general.

Some genomes that are in IMG will not have their raw data stored on the Genome Portal. In this case the function will print out in the command line the IMG id's it could not obtain from the portal. The raw files for these genomes can likely be found on NCBI.


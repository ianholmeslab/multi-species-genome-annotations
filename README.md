# Multi-Species Genome Annotation Downloads

This repository contains scripts to download and manage genome annotation data (FASTA and GFF files) for multiple species from public databases (e.g., NCBI, Ensembl). 


The downloader script fetches genome annotation files for various species from NCBI's RefSeq FTP server. Each species' files are stored in a unique directory within a designated path, where files are downloaded based on matching patterns. Specifically, the script searches for files with names that:

1) Start with the species' accession number
2) End in _genomic.fna.gz or _genomic.gff.gz

Note: the directories and accesion numbers in the species_data dictionary can be modified based on the database and new releases. 

# Key Features:

Flexible Directory Matching: Automatically finds the directory based on accession number or selects the latest directory as a fallback.

File Filtering: Only downloads files that match the specified genome annotation formats.

Customizable Storage: Saves each species' files in multi_species/data/<species_name>.



# Clone the Repository:

git clone https://github.com/<your-username>/multi_species_genome_annotations.git
cd multi_species_genome_annotations

Install Required Libraries: This project uses requests for HTTP requests. Install it via pip:
pip install requests


The species to download and their corresponding accession numbers and directories should be defined in a dictionary called species_data within the script.


# Execute the script:

python download_annotations.py
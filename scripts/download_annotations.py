import os
import requests

# Dictionary of species and their accession numbers
species_data = {
    "Aotus_nancymaae": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Aotus_nancymaae/annotation_releases/current/GCF_030222135.1-RS_2024_04/",
        "accession": "GCF_030222135.1"
    },
    "Camelus_bactrianus": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Camelus_bactrianus/annotation_releases/current/102/GCF_000767855.1_Ca_bactrianus_MBC_1.0/",
        "accession": "GCF_000767855.1"
    },
    "Canis_lupus_familiaris": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Canis_lupus_familiaris/annotation_releases/current/106/GCF_000002285.5_Dog10K_Boxer_Tasha/",
        "accession": "GCF_000002285.5"
    },
    "Cavia_porcellus": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Cavia_porcellus/annotation_releases/current/GCF_034190915.1-RS_2024_02/",
        "accession": "GCF_034190915.1"
    },
    "Cebus_imitator": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Cebus_imitator/annotation_releases/current/101/GCF_001604975.1_Cebus_imitator-1.0/",
        "accession": "GCF_001604975.1"
    },
    "Ceratotherium_simum": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Ceratotherium_simum/annotation_releases/current/101/GCF_000283155.1_CerSimSim1.0/",
        "accession": "GCF_000283155.1"
    },
    "Chinchilla_lanigera": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Chinchilla_lanigera/annotation_releases/current/101/GCF_000276665.1_ChiLan1.0/",
        "accession": "GCF_000276665.1"
    },
    "Condylura_cristata": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Condylura_cristata/annotation_releases/current/101/GCF_000260355.1_ConCri1.0/",
        "accession": "GCF_000260355.1"
    },
    "Desmodus_rotundus": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Desmodus_rotundus/annotation_releases/current/GCF_022682495.1-RS_2023_02/",
        "accession": "GCF_022682495.1"
    },
    "Dipodomys_ordii": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Dipodomys_ordii/annotation_releases/current/100/GCF_000151885.1_Dord_2.0/",
        "accession": "GCF_000151885.1"
    },
    "Enhydra_lutris": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Enhydra_lutris/annotation_releases/current/100/GCF_002288905.1_ASM228890v2/",
        "accession": "GCF_002288905.1"
    },
    "Eptesicus_fuscus": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Eptesicus_fuscus/annotation_releases/current/GCF_027574615.1-RS_2023_03/",
        "accession": "GCF_027574615.1"
    },
    "Equus_caballus": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Equus_caballus/annotation_releases/current/GCF_002863925.1-RS_2024_08/",
        "accession": "GCF_002863925.1"
    },
    "Heterocephalus_glaber": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Heterocephalus_glaber/annotation_releases/current/102/GCF_000247695.1_HetGla_female_1.0/",
        "accession": "GCF_000247695.1"
    },
    "Ictidomys_tridecemlineatus": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Ictidomys_tridecemlineatus/annotation_releases/current/103/GCF_016881025.1_HiC_Itri_2/",
        "accession": "GCF_016881025.1"
    },
    "Jaculus_jaculus": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Jaculus_jaculus/annotation_releases/current/102/GCF_020740685.1_mJacJac1.mat.Y.cur/",
        "accession": "GCF_020740685.1"
    },
    "Loxodonta_africana": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Loxodonta_africana/annotation_releases/current/GCF_030014295.1-RS_2024_04/",
        "accession": "GCF_030014295.1"
    },
    "Microtus_ochrogaster": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Microtus_ochrogaster/annotation_releases/current/102/GCF_000317375.1_MicOch1.0/",
        "accession": "GCF_000317375.1"
    },
    "Mus_pahari": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Mus_pahari/annotation_releases/current/101/GCF_900095145.1_PAHARI_EIJ_v1.1/",
        "accession": "GCF_900095145.1"
    },
    "Neomonachus_schauinslandi": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Neomonachus_schauinslandi/annotation_releases/current/101/GCF_002201575.2_ASM220157v2/",
        "accession": "GCF_002201575.2"
    },
    "Octodon_degus": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Octodon_degus/annotation_releases/current/102/GCF_000260255.1_OctDeg1.0/",
        "accession": "GCF_000260255.1"
    },
    "Odobenus_rosmarus": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Odobenus_rosmarus/annotation_releases/current/101/GCF_000321225.1_Oros_1.0/",
        "accession": "GCF_000321225.1"
    },
    "Propithecus_coquereli": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Propithecus_coquereli/annotation_releases/current/100/GCF_000956105.1_Pcoq_1.0/",
        "accession": "GCF_000956105.1"
    },
    "Puma_concolor": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Puma_concolor/annotation_releases/current/100/GCF_003327715.1_PumCon1.0/",
        "accession": "GCF_003327715.1"
    },
    "Saimiri_boliviensis": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Saimiri_boliviensis/annotation_releases/current/102/GCF_016699345.1_BCM_Sbol_2.0/",
        "accession": "GCF_016699345.1"
    },
    "Marmota_marmota": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Marmota_marmota/annotation_releases/current/101/GCF_001458135.2_marMar/",  
        "accession": "GCF_001458135.2"     
    },
    "Microcebus_murinus": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Microcebus_murinus/annotation_releases/current/101/GCF_000165445.2_Mmur_3.0/",  
        "accession": "GCF_000165445.2"      
    },
    "Mus_musculus": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Mus_musculus/annotation_releases/current/GCF_000001635.27-RS_2024_02/", 
        "accession": "GCF_000001635.27"    
    },
    "Ochotona_princeps": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Ochotona_princeps/annotation_releases/current/GCF_030435755.1-RS_2023_07/",  
        "accession": "GCF_030435755.1"    
    },
    "Otolemur_garnettii": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Otolemur_garnettii/annotation_releases/current/102/GCF_000181295.1_OtoGar3/",
        "accession": "GCF_000181295.1"     
    },
    "Panthera_pardus": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Panthera_pardus/annotation_releases/current/GCF_024362965.1-RS_2023_02/", 
        "accession": "GCF_024362965.1"   
    },
    "Rattus_norvegicus": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Rattus_norvegicus/annotation_releases/current/GCF_036323735.1-RS_2024_02/", 
        "accession": "GCF_036323735.1"  
    },
    "Sorex_araneus": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Sorex_araneus/annotation_releases/current/GCF_027595985.1-RS_2023_04/", 
        "accession": "GCF_027595985.1"      
    },
    "Trichechus_manatus": {
        "directory_url": "https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Trichechus_manatus/annotation_releases/current/GCF_000243295.1-RS_2024_01/", 
        "accession": "GCF_000243295.1"   
    }
}   


def download_file(url, output_path):
    """Download a file from a given URL."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"Downloaded: {output_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

def list_files_in_directory(directory_url, accession):
    """List files in a directory URL, matching those that start with the accession and end in _genomic.fna.gz or _genomic.gff.gz."""
    try:
        response = requests.get(directory_url)
        response.raise_for_status()

        # Extract and print all href links
        files = [
            line.split('"')[1]
            for line in response.text.splitlines()
            if line.startswith("<a href=")
        ]
        print(f"Found files in directory {directory_url}: {files}")  # Debugging statement

        # Filter for files matching the accession and the required suffixes
        matched_files = [
            file for file in files
            if (file.endswith("_genomic.fna.gz") or file.endswith("_genomic.gff.gz"))
        ]
        print(f"Matched files in directory {directory_url}: {matched_files}")  # Debugging statement
        return matched_files

    except requests.exceptions.RequestException as e:
        print(f"Failed to list files in {directory_url}: {e}")
        return []

def download_species_files(species, directory_url, accession):
    """Download all relevant files for a species from its directory URL."""
    files = list_files_in_directory(directory_url, accession)
    if not files:
        print(f"No target files found in {directory_url} for {species}")
        return

    # Create a local directory for the species
    base_path = "multi_species_genome/data"
    species_dir = os.path.join(base_path, species)
    os.makedirs(species_dir, exist_ok=True)

    # Download each matching file
    for file in files:
        file_url = directory_url + file
        output_path = os.path.join(species_dir, file)
        print(f"Downloading {file_url}...")
        download_file(file_url, output_path)

def main():
    for species, info in species_data.items():
        if info["directory_url"] and info["accession"]:
            print(f"Processing {species}...")
            download_species_files(species, info["directory_url"], info["accession"])

if __name__ == "__main__":
    main()
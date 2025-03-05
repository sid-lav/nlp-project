import os
import requests
from pathlib import Path
from typing import List
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DataDownloader:
    def __init__(self, data_dir: str = "../../data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
    def download_file(self, url: str, output_path: str) -> None:
        """Download file from URL and save to specified path."""
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            logger.info(f"Successfully downloaded {url} to {output_path}")
        except Exception as e:
            logger.error(f"Error downloading {url}: {str(e)}")
            raise

    def download_spanish_corpora(self) -> None:
        """Download various Spanish language corpora."""
        # Create subdirectories
        raw_dir = self.data_dir / "raw_text"
        raw_dir.mkdir(exist_ok=True)
        
        # List of corpora to download
        corpora_urls = {
            "wikipedia": "https://dumps.wikimedia.org/eswiki/latest/eswiki-latest-pages-articles.xml.bz2",
            "opensubtitles": "https://opus.nlpl.eu/OpenSubtitles/v2018/moses/es-en.txt.zip",
            # Add more corpora URLs as needed
        }
        
        for name, url in corpora_urls.items():
            output_path = raw_dir / f"{name}.txt"
            self.download_file(url, str(output_path))

    def download_learner_corpora(self) -> None:
        """Download learner corpora with error annotations."""
        learner_dir = self.data_dir / "learner_corpus"
        learner_dir.mkdir(exist_ok=True)
        
        # Example learner corpus URLs
        learner_urls = {
            "lang8": "https://lang8.com/downloads/corpus.zip",
            # Add more learner corpus URLs
        }
        
        for name, url in learner_urls.items():
            output_path = learner_dir / f"{name}.zip"
            self.download_file(url, str(output_path))

    def download_audio_data(self) -> None:
        """Download audio datasets for pronunciation."""
        audio_dir = self.data_dir / "audio"
        audio_dir.mkdir(exist_ok=True)
        
        # Example audio dataset URLs
        audio_urls = {
            "common_voice": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-14.0-2023-06-22/es.tar.gz",
            # Add more audio dataset URLs
        }
        
        for name, url in audio_urls.items():
            output_path = audio_dir / f"{name}.tar.gz"
            self.download_file(url, str(output_path))

def main():
    downloader = DataDownloader()
    
    # Download all types of data
    downloader.download_spanish_corpora()
    downloader.download_learner_corpora()
    downloader.download_audio_data()

if __name__ == "__main__":
    main()

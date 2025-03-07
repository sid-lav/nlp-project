import spacy
import pandas as pd
from typing import List, Dict, Tuple
import json
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load Spanish language model
try:
    nlp = spacy.load('es_core_news_sm')
except OSError:
    logger.warning("Spacy model not found. Downloading...")
    spacy.cli.download('es_core_news_sm')
    nlp = spacy.load('es_core_news_sm')

class TextPreprocessor:
    def __init__(self, data_dir: str = "../../data"):
        self.data_dir = Path(data_dir)
        self.raw_dir = self.data_dir / "raw_text"
        self.processed_dir = self.data_dir / "processed_text"
        self.processed_dir.mkdir(parents=True, exist_ok=True)

    def normalize_text(self, text: str) -> str:
        """Normalize Spanish text by:
        1. Lowercasing
        2. Removing extra whitespace
        3. Handling special characters
        """
        # Remove extra whitespace
        text = ' '.join(text.split())
        # Handle special characters
        text = text.replace('á', 'á').replace('é', 'é').replace('í', 'í')
        text = text.replace('ó', 'ó').replace('ú', 'ú').replace('ñ', 'ñ')
        return text.lower()

    def tokenize_text(self, text: str) -> List[str]:
        """Tokenize text using SpaCy"""
        doc = nlp(text)
        return [token.text for token in doc]

    def process_wikipedia_dump(self, input_file: str, output_file: str) -> None:
        """Process Wikipedia dump to extract sentences"""
        with open(self.raw_dir / input_file, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Process text
        processed_text = self.normalize_text(text)
        
        # Save processed text
        with open(self.processed_dir / output_file, 'w', encoding='utf-8') as f:
            f.write(processed_text)
        
        logger.info(f"Processed Wikipedia dump saved to {output_file}")

    def process_learner_corpus(self, input_file: str, output_file: str) -> None:
        """Process learner corpus with error annotations"""
        data = pd.read_csv(self.raw_dir / input_file)
        
        # Process each sentence
        processed_data = []
        for _, row in data.iterrows():
            original = self.normalize_text(row['original'])
            corrected = self.normalize_text(row['corrected'])
            
            processed_data.append({
                'original': original,
                'corrected': corrected,
                'error_type': row['error_type']
            })
        
        # Save processed data
        with open(self.processed_dir / output_file, 'w', encoding='utf-8') as f:
            json.dump(processed_data, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Processed learner corpus saved to {output_file}")

def main():
    preprocessor = TextPreprocessor()
    # Example usage
    preprocessor.process_wikipedia_dump("wikipedia.txt", "processed_wikipedia.txt")
    preprocessor.process_learner_corpus("learner_corpus.csv", "processed_learner_corpus.json")

if __name__ == "__main__":
    main()

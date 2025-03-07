import unittest
import os
import pandas as pd
from src.preprocessing.text_preprocessor import TextPreprocessor

class TestTextPreprocessor(unittest.TestCase):
    def setUp(self):
        self.preprocessor = TextPreprocessor()
        
    def test_normalize_text(self):
        """Test Spanish text normalization"""
        test_cases = [
            ("  HOLA MUNDO  ", "hola mundo"),
            ("áéíóúñ", "áéíóúñ"),
            ("¡Hola! ¿Cómo estás?", "¡hola! ¿cómo estás?"),
            ("Yo comi manzana ayer.", "yo comi manzana ayer.")
        ]
        
        for input_text, expected in test_cases:
            result = self.preprocessor.normalize_text(input_text)
            self.assertEqual(result, expected)

    def test_tokenize_text(self):
        """Test Spanish text tokenization"""
        test_text = "¡Hola! ¿Cómo estás?"
        expected_tokens = ["¡", "Hola", "!", "¿", "Cómo", "estás", "?"]
        
        result = self.preprocessor.tokenize_text(test_text)
        self.assertEqual(result, expected_tokens)

    def test_process_wikipedia_dump(self):
        """Test processing Wikipedia dump"""
        test_text = "Esta es una prueba. ¡Hola mundo!"
        test_file = "test_wikipedia.txt"
        
        # Create test file
        with open("data/raw_text/" + test_file, "w", encoding="utf-8") as f:
            f.write(test_text)
        
        # Process file
        self.preprocessor.process_wikipedia_dump(test_file, "processed_test.txt")
        
        # Check processed file exists
        processed_file = "data/processed_text/processed_test.txt"
        self.assertTrue(os.path.exists(processed_file))
        
        # Clean up
        os.remove("data/raw_text/" + test_file)
        os.remove(processed_file)

    def test_process_learner_corpus(self):
        """Test processing learner corpus"""
        test_data = [
            {"original": "Yo comi manzana ayer.",
             "corrected": "Yo comí una manzana ayer.",
             "error_type": "accent missing"}
        ]
        
        # Create test file
        test_file = "test_learner_corpus.csv"
        df = pd.DataFrame(test_data)
        df.to_csv("data/raw_text/" + test_file, index=False)
        
        # Process file
        self.preprocessor.process_learner_corpus(test_file, "processed_test.json")
        
        # Check processed file exists
        processed_file = "data/processed_text/processed_test.json"
        self.assertTrue(os.path.exists(processed_file))
        
        # Clean up
        os.remove("data/raw_text/" + test_file)
        os.remove(processed_file)

if __name__ == '__main__':
    unittest.main()

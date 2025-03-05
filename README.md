# Smart Spanish Tutor

An AI-powered language learning platform that helps Spanish learners improve their writing and pronunciation skills.

## Project Structure

```
nlp-project/
├── data/                    # Raw and processed datasets
├── models/                  # ML model code and checkpoints
├── notebooks/              # Jupyter notebooks for EDA and experimentation
├── src/                    # Source code
│   ├── api/               # API endpoints
│   ├── preprocessing/     # Data preprocessing modules
│   ├── models/            # ML model implementations
│   └── utils/             # Utility functions
├── tests/                  # Test files
└── requirements.txt        # Python dependencies
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Development

### Phase 1: Data Collection & Curation

The first phase focuses on gathering and preparing high-quality datasets for training our models.

### Phase 2: Model Development

Implementation of ML models for text correction, pronunciation scoring, and exercise generation.

### Phase 3: Frontend Development

Building the interactive user interface for language learners.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License

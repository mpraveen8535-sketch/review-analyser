# Review Analyser

An AI-powered tool that analyzes customer reviews to extract overall sentiment, common complaints, and top praise. Built for businesses that want to understand their customer feedback at a glance.

## What it does

Feed it customer reviews → Get actionable insights

**Input:** 10 customer reviews for a hair salon

**Output:**
```json
{
  "overall_sentiment": "mostly positive",
  "top_complaints": [
    "Long wait times",
    "Parking difficulties",
    "Prices increasing"
  ],
  "top_praise": [
    "Friendly staff",
    "Excellent haircuts",
    "Clean environment"
  ]
}
```

## Tech Stack

- Python 3
- Anthropic Claude API

## Setup

1. Clone the repo
```bash
git clone https://github.com/mpraveen8535-sketch/review-analyser.git
cd review-analyser
```

2. Install dependencies
```bash
pip install anthropic
```

3. Set your API key
```bash
export ANTHROPIC_API_KEY="your-key-here"
```

4. Run it
```bash
python review_analyser.py
```

## Use Cases

- Salon owners analyzing Google/Yelp reviews
- Restaurants identifying service issues
- Any business wanting quick feedback insights

## Future Improvements

- CSV file input for bulk review processing
- HTML report generation
- Trend analysis over time

## Author

Monishka Praveen Wannakuwatte
Bachelor of AI Student | Deakin University

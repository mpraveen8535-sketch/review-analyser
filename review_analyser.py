"""
Review Analyzer
Analyzes customer reviews to extract sentiment, complaints, and praise.
"""

import anthropic
import json


def analyze_reviews(reviews: list[str], business_name: str = "the business") -> dict:
    """
    Analyze a list of customer reviews.
    
    Args:
        reviews: List of review strings
        business_name: Name of the business (for context)
    
    Returns:
        dict with overall_sentiment, top_complaints, and top_praise
    """
    client = anthropic.Anthropic()
    
    # Format reviews with numbers
    formatted_reviews = "\n\n".join([f"Review {i+1}: \"{review}\"" for i, review in enumerate(reviews)])
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=512,
        messages=[
            {
                "role": "user",
                "content": f"""Analyze these customer reviews for {business_name}. Return ONLY valid JSON with:

- overall_sentiment: one of "positive", "negative", "mixed", "mostly positive", or "mostly negative"
- top_complaints: array of top 3 complaints (short phrases). Use empty array if none.
- top_praise: array of top 3 things customers love (short phrases). Use empty array if none.

Reviews:
{formatted_reviews}

JSON:"""
            }
        ]
    )
    
    # Parse the response
    response_text = response.content[0].text.strip()
    
    # Handle potential markdown code blocks
    if response_text.startswith("```"):
        response_text = response_text.split("```")[1]
        if response_text.startswith("json"):
            response_text = response_text[4:]
        response_text = response_text.strip()
    
    return json.loads(response_text)


def main():
    # Example: Hair salon reviews
    salon_reviews = [
        "Love this place! Sarah always does an amazing job on my hair. The staff is so friendly and welcoming.",
        "Great haircut but had to wait 30 minutes past my appointment time. Parking was a nightmare too.",
        "Best salon in town! Clean, professional, and my color came out perfect. A bit pricey but worth it.",
        "The stylists really know what they're doing. My only complaint is the wait time - always running behind.",
        "Friendly staff and great results. Wish they had better parking options nearby.",
        "Prices went up again but I keep coming back because the quality is unmatched. Love the atmosphere!",
        "Had to circle the block 3 times to find parking. Once inside though, excellent service as always.",
        "Sarah is the best! Always listens to what I want. The salon is always spotless.",
        "Good haircut, friendly people, but the prices are getting ridiculous. Also waited 20 mins.",
        "Amazing experience! Everyone is so nice and talented. Will definitely be back despite the parking situation.",
    ]
    
    print("=" * 60)
    print("REVIEW ANALYZER")
    print("=" * 60)
    print(f"\nAnalyzing {len(salon_reviews)} reviews for: Hair Salon")
    print("-" * 60)
    
    try:
        result = analyze_reviews(salon_reviews, "a hair salon")
        print("\nResults:")
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

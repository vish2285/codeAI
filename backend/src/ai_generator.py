import os
import json

from openai import OpenAI
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_challenge_with_ai(difficulty: str) -> Dict[str, Any]:
    system_prompt = """You are an expert financial literacy challenge creator.
    Your task is to generate a financial literacy question with multiple choice answers.
    The question should be appropriate for the specified difficulty level.

    For easy questions: Focus on basic money concepts, such as budgeting, needs vs. wants, saving, or understanding simple financial terms.

    For medium questions: Cover intermediate concepts like credit scores, interest rates, debt management, insurance, or basic investing principles.

    For hard questions: Include advanced topics, such as retirement planning, tax strategies, wealth building, diversification, or evaluating complex financial products.

    Return the challenge in the following JSON structure:
    {
        "title": "The question title",
        "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
        "correct_answer_id": 0, // Index of the correct answer (0-3)
        "explanation": "Detailed explanation of why the correct answer is right"
    }

    Make sure the options are plausible but with only one clearly correct answer.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Generate a {difficulty} difficulty financial literacy."}
            ],
            response_format={"type": "json_object"},
            temperature=0.7
        )

        content = response.choices[0].message.content
        challenge_data = json.loads(content)

        required_fields = ["title", "options", "correct_answer_id", "explanation"]
        for field in required_fields:
            if field not in challenge_data:
                raise ValueError(f"Missing required field: {field}")

        return challenge_data

    except Exception as e:
        print(e)
        return {
            "title": "Basic Financial Concept: Identifying a Need vs. Want",
            "options": [
                "Paying rent for your apartment",
                "Buying the newest smartphone when your current one still works",
                "Streaming service subscriptions",
                "Ordering takeout every night",
            ],
            "correct_answer_id": 0,
            "explanation": "A 'need' is something essential for living, like housing, food, and healthcare. Paying rent is a need, while the other options are wants."
        }

if __name__ == "__main__":
    print(generate_challenge_with_ai("easy"))

import { useEffect, useState } from "react";

export function MCQChallenge({ challenge }) {
    const [selected, setSelected] = useState(null);

    useEffect(() => {
        setSelected(null); // Reset selection when challenge changes
    }, [challenge]);

    // ...rest of the code...
}

from schema import company_info_schema
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

class OpenAICompanyInfoExtractor:
    def __init__(self, text):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.text = text

    def extract_info(self):  # renamed from OpenapiExtractor
        messages = [
            {
                "role": "system",
                "content": "You are an assistant that extracts structured company information from unstructured text."
            },
            {
                "role": "user",
                "content": f"Extract company details from this:\n\n{self.text}"
            }
        ]

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",  
                messages=messages,
                tools=[{"type": "function", "function": company_info_schema}],
                tool_choice={"type": "function", "function": {"name": "extract_company_info"}},
                temperature=0,
                max_tokens=1000
            )

            # Extract the function call arguments from the response
            tool_calls = response.choices[0].message.tool_calls
            if tool_calls:
                arguments = tool_calls[0].function.arguments
                # Parse the JSON arguments
                extracted_data = json.loads(arguments)
                return extracted_data
            else:
                return {"error": "No tool calls found in the response."}

        except Exception as e:
            return {"error": str(e)}

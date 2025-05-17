company_info_schema = {
  "name": "extract_company_info",
  "description": "Extract key business and financial information about a company from a given text or article.",
  "parameters": {
    "type": "object",
    "properties": {
      "company_name": {
        "type": "string",
        "description": "Extract the name of the company. If not available, return 'Not Available'."
      },
      "founded": {
        "type": "string",
        "description": "Extract the year the company was founded. If not available, return 'Not Available'."
      },
      "industry": {
        "type": "string",
        "description": "Extract the industry the company belongs to (e.g., IT, Construction, Medical). If not available, return 'Not Available'."
      },
      "net_income": {
        "type": "string",
        "description": "Extract the net income. If not available, return 'Not Available'."
      },
      "financial_ratios": {
        "type": "object",
        "properties": {
          "profit_margin": {
            "type": "string",
            "description": "Extract the profit margin as a percentage. If not available, return 'Not Available'."
          },
          "current_ratio": {
            "type": "string",
            "description": "Extract the current ratio. If not available, return 'Not Available'."
          },
          "debt_to_equity_ratio": {
            "type": "string",
            "description": "Extract the debt to equity ratio. If not available, return 'Not Available'."
          }
        }
      },
      "main_products": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Extract the list of main products or services. If not available, return an empty list."
      }
    },
    "required": ["company_name", "industry", "main_products"]
  }
}

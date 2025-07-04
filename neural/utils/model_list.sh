#!/bin/bash


mkdir -p ./logs

curl -s https://openrouter.ai/api/v1/models \
    jq -r '["data"]["id"]' > ./logs/model_list.txt

echo "./logs/model_list.txt"

















# # Replace with your actual OpenRouter API key
# # API_KEY="<OPENROUTER_API_KEY>"

# # Fetch models and extract model IDs
# curl -s https://openrouter.ai/api/v1/models \
# #   -H "Authorization: Bearer $API_KEY" | \
#   jq -r '.data[].id' | \
#   sed 's/^/model="/;s/$/"/' > echo "./logs/model_list.txt"

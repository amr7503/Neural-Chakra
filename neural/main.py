# from openai import OpenAI

# client = OpenAI(
#   base_url="https://openrouter.ai/api/v1",
#   api_key="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",
# )

# completion = client.chat.completions.create(
#     # extra_headers={
#     #     "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional
#     #     "X-Title": "<YOUR_SITE_NAME>",      # Optional
#     # },
#     model="openai/gpt-4o",
#     messages=[
#         {
#             "role": "user",
#             "content": r"""give complete senior dev human like code for each of these models no comments  gemini-2.5 pro , 4o, 4.5, opus, sonnet, command R/R+. the sample 40 code is this - from openai import OpenAI

# client = OpenAI(
#   base_url="https://openrouter.ai/api/v1",
#   api_key="<OPENROUTER_API_KEY>",
# )

# completion = client.chat.completions.create(
#   extra_headers={
#     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
#     "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
#   },
#   model="openai/gpt-4o",
#   messages=[
#     {
#       "role": "user",
#       "content": "What is the meaning of life?"
#     }
#   ]
# )

# print(completion.choices[0].message.content)
# """
#         }
#     ]
# )

# print(completion.choices[0].message.content)


from openai import OpenAI
import hydra
from omegaconf import DictConfig

@hydra.main(config_path="conf", config_name="config", version_base=None)
def main(cfg: DictConfig):
    client = OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key=cfg.api.openrouter_key,  
    )

    completion = client.chat.completions.create(
      model="google/gemini-2.5-pro",
      messages=[
        {
          "role": "user",
          "content": "prove fermat's last theorem"
        }
      ]
    )

    print(completion.choices[0].message.content)

if __name__ == "__main__":
    main()
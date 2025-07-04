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

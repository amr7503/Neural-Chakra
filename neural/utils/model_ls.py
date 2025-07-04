from openai import OpenAI
import hydra
from omegaconf import DictConfig

@hydra.main(config_path="../conf", config_name="config", version_base=None)
def main(cfg: DictConfig):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=cfg.api.openrouter_key,
    )

    models = client.models.list()

    print("✅ Available Models:")
    for model in models.data:
        print(f"- {model.id}")

if __name__ == "__main__":
    main()

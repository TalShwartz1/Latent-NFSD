import pyrallis

from src.latent_nerf.configs.train_config import TrainConfig
from src.latent_nerf.training.trainer import Trainer
import os
os.environ['TORCH_CUDA_ARCH_LIST'] = "7.5"  # Replace with your GPU's compute capability
os.environ['TORCH_CPP_LOG_LEVEL'] = 'DEBUG'


@pyrallis.wrap()
def main(cfg: TrainConfig):
    trainer = Trainer(cfg)
    if cfg.log.eval_only:
        trainer.full_eval()
    else:
        trainer.train()

if __name__ == '__main__':
    main()
Latent-Gaussian Splatting with NSFD for Enhanced Text-to-3D Generation

Text-guided image generation has progressed rapidly in recent years, inspiring major breakthroughs in text-guided shape generation. Building upon recent advances in 3D generation, we propose two key improvements to the Latent-NeRF framework: replacing the Neural Radiance Field with 3D Gaussian Splatting and implementing Noise-Free Score Distillation (NSFD) instead of traditional Score Distillation Sampling (SDS). Our approach maintains the benefits of latent space diffusion while providing significant improvements in generation quality, geometric fidelity, and visual detail.
While NeRFs operate in image space and require numerous forward passes to render a single image, Gaussian Splatting offers an explicit scene representation with 3D Gaussians directly in world space. Each Gaussian carries its own latent features, enabling more efficient rendering through rasterization and more precise geometric detail where needed. Additionally, NSFD eliminates unwanted noise components from the gradient calculation, leading to more stable training and higher quality results.
Our experiments demonstrate significant improvements over the baseline Latent-NeRF approach, including enhanced detail preservation, better multi-view consistency, and superior rendering quality as measured by PSNR and SSIM metrics.

Description :scroll:
Official Implementation for "Latent-Gaussian Splatting with NSFD for Enhanced Text-to-3D Generation".

TL;DR - We replace the NeRF architecture in the Latent-NeRF framework with 3D Gaussian Splatting and implement NSFD instead of SDS, resulting in more detailed geometry, improved rendering quality, and better multi-view consistency.

Recent Updates :newspaper:

03.03.2025 - Code release
20.02.2025 - Created initial repo

Our Results :art:
Our Latent-Gaussian Splatting approach demonstrated significant improvements over the baseline Latent-NeRF model:
<img src="https://github.com/user/latent-gaussian/raw/docs/docs/comparison.gif" width="800px"/>
Below we can see the progress of the generation process over optimization with increasing iterations:
<img src="https://github.com/user/latent-gaussian/raw/docs/docs/iterations_progress.gif" width="800px"/>
To create such results, run the train_latent_gaussian script. Parameters are handled using pyrallis and can be passed from a config file or the cmd.

# Local LLM Inference Stack (`nextfield`)

Praxisnahe Docker-Compose- und Python-Templates für das datenschutzkonforme Self-Hosting von Open-Weights-Sprachmodellen (LLMs) auf eigener NVIDIA-GPU-Hardware.

## Architektur-Überblick

- **`docker/ollama/`**: Schneller Einstieg für lokale Entwicklung, Einzelplatz-Setups und Agenten-Prototyping.
- **`docker/vllm/`**: Hochperformanter Inference-Server mit OpenAI-kompatibler REST-API für parallele Workloads.
- **`python/`**: Einheitlicher Python-Client ohne API-Lock-in (kompatibel mit vLLM, Ollama und llama.cpp).

## Voraussetzungen

- Linux / WSL2 mit aktueller NVIDIA-Treiberinstallation
- Docker & Docker Compose v2
- [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

## Schnellstart

1. Konfiguration kopieren:
   ```bash
   cp .env.example .env

# Yapay Zeka Destekli Kod Üretici

## Proje Hakkında
Bu proje, kullanıcıdan alınan bir prompt'a göre Python kodu ve bir başlık üreten bir yapay zeka destekli kod üretici sistemdir.

## Kullanılan Teknolojiler
- Python 3.10
- Flask
- OpenAI API / Ollama
- Docker
- Kubernetes (Minikube)

## Çalıştırma Talimatları

### Docker İmajı
```bash
docker build -t kod-uretici:latest .
docker run -p 5000:5000 kod-uretici:latest

# Dil Çevirisi API Projesi

Bu proje, OpenAI'nin GPT-4 modelini kullanarak metin çevirisi yapabilen bir FastAPI uygulaması sağlar. Langchain kütüphanesi, iş akışını tanımlamak ve OpenAI API'si ile entegrasyonu sağlamak için kullanılır.

## Başlangıç

Projeyi çalıştırmadan önce, gerekli API anahtarlarını temin etmeniz ve yapılandırmanız gerekmektedir.

---
### Gereksinimler

- Python 3.12 veya daha yeni bir sürüm
- FastAPI
- Langchain
- OpenAI API Anahtarı
- Uvicorn (FastAPI uygulamanızı çalıştırmak için)

---
### Gereksinimlerin Yüklenmesi

Öncelikle, gerekli kütüphaneleri yüklemek için aşağıdaki komutu kullanın:


 ```bash Copy code

pip install python-dotenv langchain openai fastapi uvicorn langserve
 ```
### .env Dosyasının Yapılandırılması

Proje, API anahtarlarını güvenli bir şekilde saklamak için `.env` dosyasını kullanmaktadır. `.env` dosyanızda şu ortam değişkenlerini ekleyin:

 ```bash Copy code

OPENAI_API_KEY=your-openai-api-key-here
 ```
Bu API anahtarını OpenAI'nin [resmi web sitesi](https://beta.openai.com/signup/) üzerinden alabilirsiniz.

---
### Projeyi Çalıştırma

Projenin çalışması için aşağıdaki adımları takip edin:

1. `.env` dosyasını oluşturun ve içine API anahtarını ekleyin.
2. Gerekli bağımlılıkları yükleyin:
    
    ```bash Copy code
    
    pip install -r requirements.txt
    ```
3. FastAPI uygulamasını başlatın:
    
     ```bash                                                      Copy code
    
    uvicorn serve:app --reload
     ```
---
### API Kullanımı

API'niz şu şekilde çalışacaktır:

- **Path**: `/chain`
    
- **Metod**: `POST`
    
- **Body**:
     ```json Copy code
    
    {"language": "Türkçe",   "text": "I am a lord"}
     ```
- **Yanıt**:
    
    
    
     ```json Copy code
    
    {"result": "Ben bir lordum"}
     
     ```

Burada `language` hedef dil, `text` ise çevrilecek metni temsil eder.

---
### Kod Açıklamaları

- `load_dotenv()`: .env dosyasındaki ortam değişkenlerini yükler.
- `ChatOpenAI`: OpenAI GPT-4 modelini başlatır.
- `ChatPromptTemplate`: Kullanıcıdan alınacak metni işlemek için bir şablon oluşturur.
- `StrOutputParser`: Çıktıyı uygun formatta işler.
- `add_routes`: FastAPI'ye dil modeli iş akışını entegre eder.
---
### Projeyi Geliştirme

Projenin işleyişini daha fazla geliştirebilirsiniz. Örneğin, çeviri için farklı dil seçenekleri ekleyebilir veya daha fazla işlevsellik sağlayabilirsiniz.



---
- Direkt şu şekildede çalıştırabilirsiniz:
```bash Copy code
   pip install -r requirements.txt
   python3 serve.py
```

```result Copy code
    LANGSERVE: Playground for chain "/chain/" is live at:
LANGSERVE:  │
LANGSERVE:  └──> /chain/playground/
LANGSERVE:
LANGSERVE: See all available routes at /docs/
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

```
- http://0.0.0.0:8000/chain/playground/ Adresinde LangGraph sayesinde arayüz ile kullana bilirsiniz
---

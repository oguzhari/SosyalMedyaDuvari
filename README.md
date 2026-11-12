# Sosyal Medya Duvarı

## Streamlit Community Cloud

1. Bu klasörün içindekileri GitHub deposunun kök dizinine yükle. Kök dizinde `app.py`, `requirements.txt`, `static/` ve `.streamlit/config.toml` bulunmalı.
2. [Streamlit Community Cloud](https://share.streamlit.io/) üzerinden **Create app** seç.
3. Depoyu ve branch’i seç. **Main file path** alanına `app.py` yaz ve **Deploy** düğmesine bas.

Fotoğrafların küçük önizlemeleri `static/thumbs/`, büyük görünümleri `static/photos/` içinde hazır JPEG dosyalarıdır. `.streamlit/config.toml` bu dosyaların tarayıcıya sunulmasını sağlar. Finder’da gizli dosyaları görmek için **Cmd + Shift + .** tuşlarına bas.

## Yerelde çalıştırma

Proje klasöründen:

```sh
python -m pip install -r requirements.txt
python -m streamlit run app.py
```


# KekikAkademiRobot
Pyrogram-Async | UserBot &amp; Telegram Bot

##

 -  `bilgiler.json` dosyasında ilgili düzenlemeleri yaparak kullanmaya başlayabilirsiniz..
 - ilk çalıştırmada `session` oluşturulur, daha sonrasında oluşan session ile direk başlar.
 - Kendi eklentilerinizi geliştirebilmeniz için temiz kodlanmıştır.

### Olası `sqlite3.OperationalError:  database  is  locked` hatası
Bu hata beklenmeyen durdurmalar sırasında gerçekleşir ve session askıda kalır. Gidermek için [kendi dökümantasyonu](https://docs.pyrogram.org/faq?highlight=sqlite3%20operationalerror%20database%20locked#sqlite3-operationalerror-database-is-locked)na bakalım..

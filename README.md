Команди в  адмін чаті:
/autorun перезапис чат ід в текстовий файл, необхідне якщо чат ід ще не був записаний, і бот не знає в якій він групі

!!!! якщо chat_id не буде в txt файлі то бот не буде автоматично оновлювати вхідні повідомлення та список адмінів !!!!

/update примусове обновлення необроблених заявок, використовувати тільки якщо не працюж авто надсилання
/admin обнволює список адмінів,його функцію як і /update виконує сама програма, тому віддільно його запускати не тре 

Команди в персональному боті для адмінів:
/admin відкриває адмін панель, якшо не відкрив значить ви не є адмінов в групі  де приходять заявки.
Якщо ви все таки адмін то почекайте 2-5 хв і панель відкриється. 

В admin/constants.py можна міняти час автооновлення заявок і адмінів. За це відповідає змінна SEC_TIME_TO_SlEEP, вказувати час в секундах. 
Я не рекомендую ставити час менше хвилини, бо дуже багато реквестів і бот може тупо працювати.

unknown.jpg є дефолтною картинкою якшо нема реальних фоток, її не видаляти, вона повинна бути в database/CarPhotos/unknown.jpg
# upload-websocket-python-javascript
Загрузка файлов с помощью WebSoket
<h3><strong>Клиент</strong> - javascript:</h3>
   <li>делим файл на части</li>
   <li>кодируем части в base64</li> 
   <li>отправляем</li>
<h3><strong>Сервер</strong> - python:</h3>
   <li>получаем base64 части</li> 
   <li>декодируем base64 части</li>
   <li>сохраняем файл</li>
   
# Запуск
В файле svup изменить IP
   ```
   python svup.py
   ```
   
<img src="https://github.com/evilsadko/upload-websocket-python-javascript/blob/master/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202019-10-07%2010-37-54.png" width="auto" title="example">

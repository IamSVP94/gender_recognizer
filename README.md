# gender_recognizer
The program recognizes gender by face photo
Для ознакомления с алгоритмом разработки, можете посмотреть <a href='https://github.com/IamSVP94/gender_recognizer/blob/master/NtechLab.ipynb'>тетрадку</a>.

Для работы скрипта для использования нейросети (файл process.py) необходимо установить некоторые библиотеки и расположить его в одной директории с файлом net.pt (файл с сохраненной моделью Pytorch).
Также необходимо указывать путь к папке с изображениями *без кириллицы*.
**Пример вызова**: python3 process.py folder\to\process\
Полсе завершения процесса обработки будет создан файл process_results.json с результатами вычислений модели.
**Пример файла с результатами**: { ‘img_1.jpg’: ‘male’, ‘img_2.jpg’: ‘female’, ...}

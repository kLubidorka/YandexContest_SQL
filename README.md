# YandexContest_SQL
SQL task for Yandex Contest sample

based on [repository](https://github.com/atolstikov/yacontest-cheatsheet/tree/master/db-sqlite) by [@atolstikov](https://t.me/atolstikov)

Для запуска чекера на python, который проверит результат выполнения запроса, можно использовать следующий пайплайн:
* problem-with-checker, т.е. мы запустим собственную обертку на запуск решения с компилятором (в нашем случае
  интерпретатором), у которого в окружении есть дополнительные библиотеки, а потом интерпретируем вывод этого решения в
  чекере
* В настройках соревнования для задачи оставляем единственный компилятор (make)python-lyceum
* Чтобы участники видели сообщение об ошибках при вычислении метрики, в настройках соревнования нужно включить
  отображение вывода постпроцессора.
* Копируем в задачу файлы: `Makefile`, `compare_result.py`, `build.sh`, `postprocessor.py`, `runner.py`, `author_solution.sql`
  * `Makefile` описывает два таргета `build` для стадии обработки присланного участником файла и `run` стадии запуска на каждом тесте (для этого в задаче созданы три теста в директории `tests` и добавлены
    соответствующие файлы баз данных)
  * `compare_results.py` устанавливается чекером
    для задачи и сравнивает его с результатом запуска решения
* Дополнительные файлы/обработки
  * Файлы для компиляции: `Makefile`, `build.sh`
  * Файлы для времени запуска: `films0.db`, `films1.db`, `films2.db`, `runner.py`
  * Файлы постпроцессинга: `postprocessor.py` (используется для выставления баллов)
* Установить чекер `compare_results.py`, выбрав тип "TESTLIB_EXITCODE_CHECKER".

# Rosbank, 2nd place solution. (1st place task 1, 2nd place task 2)
## Rosbank ML competition.

Здесь приводятся основные элементы обработки данных, дающие 1-е место по первой задаче и 2-е место по второй.

* train.csv и test.csv - начальные данные необходимо скачать САМОСТОЯТЕЛЬНО. В данных ноутбуках они везде обозначаются как init_train и init_test, в то время как train и test - уже обработанные данные.

* [solution_presentation.pdf](https://github.com/KhrylchenkoKirill/rosbank/solution_presentation.pdf) - презентация, позволяющая понять, что происходит в решении

* [utils.ipynb](https://github.com/KhrylchenkoKirill/rosbank/utils.ipynb) - обработка начальных данных

* [rosbank.py](https://github.com/KhrylchenkoKirill/rosbank/rosbank.py) - содержит одну единственную функцию cashflow, преобразующую данные о пользователе в словарь

* [time.ipynb](https://github.com/KhrylchenkoKirill/rosbank/time.ipynb) - обработка времени

* [money.ipynb](https://github.com/KhrylchenkoKirill/rosbank/money.ipynb) - обработка денежной информации

* [mcc.time.ipynb](https://github.com/KhrylchenkoKirill/rosbank/mcc.time.ipynb) - обработка времени с учетом МСС-кодов. Пока без комментариев

* [mcc.money.ipynb](https://github.com/KhrylchenkoKirill/rosbank/mcc.money.ipynb) - обработка денег с учетом МСС-кодов. Аналогично без комментариев

файлы [handcrafted_mcc_features.npy](https://github.com/KhrylchenkoKirill/rosbank/handcrafted_mcc_features.npy) и [mcc_codes.npy](https://github.com/KhrylchenkoKirill/rosbank/mcc_codes.npy) содержат инфу об мсс кодах. Первый словарь получен частично с помощью тематического моделирования, частично вручную. Второй массив - данные с сайта mcc-codes.ru. Это словари. Открывать с помощью np.load(путь к файлу).item()

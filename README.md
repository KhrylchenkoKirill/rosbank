# Rosbank ML Competition
### 2nd place solution
* Task 1: 1st place
* Task 2: 2nd place

Здесь приводятся основные элементы обработки данных, дающие 1-е место по первой задаче и 2-е место по второй.

* train.csv и test.csv - начальные данные необходимо скачать **самостоятельно**. В данных ноутбуках они везде обозначаются как init_train и init_test, в то время как train и test - уже обработанные данные.

* [solution_presentation.pdf](https://github.com/KhrylchenkoKirill/rosbank//blob/master/solution_presentation.pdf) - презентация решения

* [utils.ipynb](https://github.com/KhrylchenkoKirill/rosbank//blob/master/utils.ipynb) - обработка начальных данных

* [rosbank.py](https://github.com/KhrylchenkoKirill/rosbank//blob/master/rosbank.py) - содержит функцию cashflow, преобразующую данные о пользователе в словарь

* [time.ipynb](https://github.com/KhrylchenkoKirill/rosbank//blob/master/time.ipynb) - обработка времени

* [money.ipynb](https://github.com/KhrylchenkoKirill/rosbank//blob/master/money.ipynb) - обработка денежной информации

* [mcc.time.ipynb](https://github.com/KhrylchenkoKirill/rosbank//blob/master/mcc.time.ipynb) - обработка времени с учетом МСС-кодов

* [mcc.money.ipynb](https://github.com/KhrylchenkoKirill/rosbank//blob/master/mcc.money.ipynb) - обработка денег с учетом МСС-кодов

Файлы [handcrafted_mcc_features.npy](https://github.com/KhrylchenkoKirill/rosbank//blob/master/handcrafted_mcc_features.npy) и [mcc_codes.npy](https://github.com/KhrylchenkoKirill/rosbank//blob/master/mcc_codes.npy) содержат информацию об мсс кодах. Первый словарь получен частично с помощью тематического моделирования, частично вручную. Второй массив - данные с сайта mcc-codes.ru. Это словари. Открывать с помощью np.load(путь к файлу).item()

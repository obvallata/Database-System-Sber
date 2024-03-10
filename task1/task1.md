## MongoDB

1. **Установка**: Будем работать с mongoDB с помощью Docker container
   ![](screens/docker_install_mongodb.png)
2. **Загрузка данных**: используем предложенную [ссылку](https://www.yelp.com/dataset/)
![](screens/upload_business_dataset.png)
3. **find**: посмотрим, как вообще выглядят данные
![](screens/usual_find.png)
4. **countDocuments**: посмотрим, сколько записей 
![](screens/amount_docs.png)
5. **insert**: вставим 5 новых записей следующим образом 
![insertOne.png](screens/insertOne.png)
6. **Проверка**: по ответам на операции вставки уже видим, что они
прошли успешно, проверим, узнав новое число записей 
![countDocs2.png](screens/countDocs2.png)

7. **find**: найдем предприятия, работающие по выходным, потом посчитаем их число 
![find.png](screens/find.png)
![find_count.png](screens/find_count.png)
Получилось, что почти все трудоголики.
8. **find**: теперь наоборот, посмотрим, кто не работает в понедельник
![find_monday.png](screens/find_monday.png)
Таких уже на порядок меньше.
9. **find**: проверим, есть ли волшебные места с рейтингом > 5
![better5.png](screens/better5.png)
Таких нет, это радует и указывает на корректность данных)
10. **find**: посмотрим число мест с рейтингом >4.5
![better4.5.png](screens/better4.5.png)
11. Совместим предыдущие запросы и посмотрим на число
![big find.png](screens/big%20find.png)
12. **explain("executionStats")**: измерим время запроса![time1.png](screens/time1.png)
Зафиксировали в уме 95ms
13. **createIndex**: создадим индекс по рейтингу
![index_stars.png](screens/index_stars.png)
14. **explain("executionStats")**: проверим на новое время выполнения запроса![time2.png](screens/time2.png)
Зафиксировали в уме 26ms. Мы выиграли по времени больше, чем в три раза, с помощью индекса.
15. **aggregate**: посмотрим статистику по городам ![aggreagte.png](screens/aggreagte.png)
16. **update**: пример успешного обновления данных![update.png](screens/update.png)![update_check.png](screens/update_check.png)
17. **delete**: напоследок убедимся, что умеем удалять ![delete.png](screens/delete.png)
18. **delete**: покажем, что умеем удалять по фильтрам ![delete_smart.png](screens/delete_smart.png)

По итогу знакомства с MongoDB, можно сделать вывод, что NoSQL не менее удобен, чем обычный SQL.

Спасибо за внимание!![computer-cat.gif](screens/computer-cat.gif)
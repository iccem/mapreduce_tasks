# mapreduce_tasks
Project Description: Hadoop Streaming Task Solution

Task1
Implementing a solution for a task using Hadoop Streaming.

Problem Statement:
Shuffle a list of identifiers randomly. Subsequently, for each line, write a comma-separated random number of identifiers, ranging from 1 to 5.

Input Data:
List of identifiers.
Format: Text, one identifier per line.

Output Format:
id1,id2,...

Print Output:
The first 50 lines.

Procedure:
To shuffle the records, append a random number to each identifier, sort the entire list based on this number, and then discard the additional number.

Note: This is a sample solution for a Hadoop Streaming task that involves shuffling and randomization of identifiers within a given list. The input data consists of a list of identifiers, and the output format requires each line to contain a random number of identifiers separated by commas. The sorting process involves appending random numbers to each identifier, sorting the list based on these numbers, and then discarding the additional numbers. This solution provides an illustrative example of how to approach such a task using Hadoop Streaming.

Task2
Требуется посчитать число вхождений имен собственных длиной от 6 до 9 символов.  

Имя собственное - это слово, которое начинается с заглавной буквы и у которого все последующие буквы строчные, дополнительное условие -- это слово ни разу не встречается в корпусе текстов начинающимся со строчной буквы.

Текст необходимо очистить от знаков пунктуации, привести к нижнему регистру и отсортировать по убыванию числа вхождений, в случае равенства - отсортировать лексикографически.

Пробелами считаем стандартные пробельные символы [ \t\n\r\f\v] или их последовательность.

При решении задач требуется использовать использовать как можно меньшее кол-во Hadoop Job, использовать больше, чем 1 reducer (1 reducer разрешается использовать только в финальной job'е, при сортировке результата).

Входные данные: википедия.
Формат вывода в HDFS: имя  количество
Вывод на печать: топ 10 имен.

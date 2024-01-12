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
The task at hand involves counting the occurrences of proper names with a length ranging from 6 to 9 characters.

A proper name is a word that begins with a capital letter, and all subsequent letters are lowercase. An additional condition is that the word does not appear anywhere in the corpus of texts beginning with a lowercase letter.

The text needs to be cleaned of punctuation marks, converted to lowercase, and sorted in descending order based on the count of occurrences. In the case of ties, lexicographical sorting should be applied.

Spaces are defined as standard whitespace characters [ \t\n\r\f\v] or their sequences.

In solving the tasks, it is required to use as few Hadoop Jobs as possible and utilize more than 1 reducer (using only 1 reducer is allowed only in the final job when sorting the result).

Input data: Wikipedia.
Output format in HDFS: name  count
Print output: top 10 names.

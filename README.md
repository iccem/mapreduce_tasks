# mapreduce_tasks
Project Description: Hadoop Streaming Task Solution

Task:
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
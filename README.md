# LeetCode_001_TwoSum
The uploaded file "LC_001_TwoSum_S3.py" is using One-pass Hash Table approach to achieve the two sum search.<br/>
File was completed on 5/21/2020.<br/>
Data flow:<br/>
    - Using Dictionary hash_table to re-organize the list type data "nums":<br/>
    - Use hash_table.keys to save all nums data, use hash_table.values to save all index information in order to return values
      returned;<br/><br/>
Note that: when running, line "return" once executed, the scripts for self-defined function "twoSum" will stop at the point. Thus, when changed senario, such as "nums = [2, 7, 11, 15, 20]" and "target = 22". Once executed, only "[1, 3]" pair will be returned. [0, 4] will never returned because scripts will stop at iteration i = 3, it will not run the remaining i = 4 situation in for loop.<br/>

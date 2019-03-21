# MySQL索引背后的数据结构及算法原理 #

[http://blog.codinglabs.org/articles/theory-of-mysql-index.html](http://blog.codinglabs.org/articles/theory-of-mysql-index.html)

## 摘要 ##

本文以MySQL数据库为研究对象，讨论与数据库索引相关的一些话题。特别需要说明的是，MySQL支持诸多存储引擎，而各种存储引擎对索引的支持也各不相同，因此MySQL数据库支持多种索引类型，如BTree索引，哈希索引，全文索引等等。为了避免混乱，**本文将只关注于BTree索引**，因为这是平常使用MySQL时主要打交道的索引，至于哈希索引和全文索引本文暂不讨论。

文章主要内容分为三个部分。

1. 第一部分主要从数据结构及算法理论层面讨论MySQL数据库索引的数理基础。

2. 第二部分结合MySQL数据库中MyISAM和InnoDB数据存储引擎中索引的架构实现讨论聚集索引、非聚集索引及覆盖索引等话题。

3. 第三部分根据上面的理论基础，讨论MySQL中高性能使用索引的策略。

## 数据结构及算法基础 ##















[Degree度: the degree of a node is the number of children of the node](https://en.wikipedia.org/wiki/Node_(computer_science)


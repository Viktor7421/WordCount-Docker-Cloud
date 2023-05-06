# -*- coding: utf-8 -*-
from pyspark import SparkContext
import io

def WordCount(file_path):
    sc = SparkContext(appName="WordCount")
    lines = sc.textFile(file_path)

    words = lines.flatMap(lambda line: line.split())
    word_count = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    sorted_word_count = word_count.sortBy(lambda x: x[1], ascending=False)
    
    result = sorted_word_count.collect()
    sc.stop()
    return result

if __name__ == "__main__":
    words_list = WordCount("/app/volumen/movies.csv")

    with io.open("/app/volumen/output_file.txt", "w", encoding="utf-8") as f:
        for word, n in words_list:
            f.write(u"{}: {}\n".format(word, n))

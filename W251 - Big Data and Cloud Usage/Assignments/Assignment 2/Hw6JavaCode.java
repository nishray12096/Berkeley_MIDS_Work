package spark;

import java.util.Arrays;
import java.util.List;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import org.apache.log4j.Level;
import org.apache.log4j.Logger;
import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

import scala.Tuple2;
/*
 *  *
 *   * This class is a collection of example designed to demonstrate Spark 2 and Java 8.
 *    * These examples will use the Java 8 lambda approach
 *     */


public class Hw6JavaCode {

        public static void main(String[] args) {
                Logger.getLogger("org").setLevel(Level.OFF);
                Logger.getLogger("akka").setLevel(Level.OFF);



                SparkConf sparkConf = new SparkConf().setAppName("HW6");
                if (!sparkConf.contains("spark.master")) {
                        sparkConf.setMaster("local[2]");
                }
                if(args.length != 2){
                        System.err.println("missing arguments: requires inputFile outputDirectory");
                        System.exit(-1);
                }
                String inputFile = args[0];
                String outputDirectory = args[1];

                try(
                                SparkSession spark = SparkSession.builder().config(sparkConf).getOrCreate();
                                JavaSparkContext sc =   new JavaSparkContext(spark.sparkContext());
                ){


                        JavaRDD<String> file = sc.textFile(inputFile);

                        JavaPairRDD<String, Long> withIndex = file.zipWithIndex();

                        System.out.println("Orginal file: " + file.take(5));

                        List<Long> index = withIndex.lookup("MOBY DICK; OR THE WHALE ");

                        Long ToStart = index.get(0);

                        System.out.println("Index of start: " + ToStart.toString());

                        JavaRDD<String> FilteredRDD = file.mapPartitionsWithIndex((indexiter, iter) -> {
                                if (indexiter == 0 && iter.hasNext()) {
                                    for (long i = 1; i <= ToStart; i++){
                                         if (iter.hasNext()) {
                                             iter.next();
                                         }
                                    }
                                }
                                return iter;
                           }, true);

                        System.out.println(FilteredRDD.take(5));

                        long NumLines = FilteredRDD.count();
                        System.out.println("Number of lines post filtering: " + NumLines);
						
                        FilteredRDD.saveAsTextFile(outputDirectory);

                        FilteredRDD = FilteredRDD.map(f -> f.replaceAll("[^a-zA-Z ]", ""));

                        FilteredRDD.cache();

                        JavaRDD<String> words = FilteredRDD.flatMap(line -> Arrays.asList(line.split(" ")).iterator());

                        System.out.println("Number of words (alphanumeric chars): " + words.count());

                        JavaRDD<String> Letters = FilteredRDD.flatMap(line -> Arrays.asList(line.toLowerCase().split("")).iterator(
));

                        JavaPairRDD<String,Integer> LetterCounts = Letters.mapToPair(letter -> new Tuple2<>(letter,1)).reduceByKey(
(x,y) -> x+y);

                        JavaPairRDD<String, Integer> sorted = LetterCounts.sortByKey();

                        sorted.cache();

                        System.out.println("Letter counts, sorted by letter: " + sorted.take(28));

                        JavaPairRDD<Integer, String> sortedCountKey = sorted.mapToPair(x -> x.swap()).sortByKey(false);

                        System.out.println("Letter counts, sorted by frequency: " + sortedCountKey.take(28));

                        JavaRDD<String> ReversedLines = FilteredRDD.map(f -> new StringBuilder(f).reverse().toString());

                        System.out.println("First 20 lines reversed: " + ReversedLines.take(20));
                }
        }
}
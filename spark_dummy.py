
from pyspark.sql import SparkSession
def get_spark():
    spark = (
        SparkSession.builder.appName("DefaultSession").config("spark.master", "local").getOrCreate()
        #SparkSession.builder.getOrCreate()
    )
    #spark = SparkSession.getActiveSession()
    return spark


def main():
    spark = get_spark()
    print(spark)

if __name__ == "__main__":
    main()

package org.apache.kafka.streams.examples.minmax;

import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.common.errors.SerializationException;
import org.apache.kafka.common.serialization.Deserializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.serialization.Serializer;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.KeyValue;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.kstream.Consumed;
import org.apache.kafka.streams.kstream.Grouped;
import org.apache.kafka.streams.kstream.KStream;
import org.apache.kafka.streams.kstream.KTable;
import org.apache.kafka.streams.kstream.TimeWindows;
import org.apache.kafka.streams.kstream.Printed;
import org.apache.kafka.streams.kstream.Produced;
import org.apache.kafka.streams.kstream.Materialized;

import java.io.IOException;
import java.time.Duration;
import java.util.Map;
import java.util.Properties;
import java.util.concurrent.CountDownLatch;

@SuppressWarnings({"WeakerAccess", "unused"})
public class MinMaxDemo {

    /**
     * A serde for any class that implements {@link JSONSerdeCompatible}. Note that the classes also need to
     * be registered in the {@code @JsonSubTypes} annotation on {@link JSONSerdeCompatible}.
     *
     * @param <T> The concrete type of the class that gets de/serialized
     */
    public static class JSONSerde<T extends JSONSerdeCompatible> implements Serializer<T>, Deserializer<T>, Serde<T> {
        private static final ObjectMapper OBJECT_MAPPER = new ObjectMapper();

        @Override
        public void configure(final Map<String, ?> configs, final boolean isKey) {}

        @SuppressWarnings("unchecked")
        @Override
        public T deserialize(final String topic, final byte[] data) {
            if (data == null) {
                return null;
            }

            try {
                return (T) OBJECT_MAPPER.readValue(data, JSONSerdeCompatible.class);
            } catch (final IOException e) {
                throw new SerializationException(e);
            }
        }

        @Override
        public byte[] serialize(final String topic, final T data) {
            if (data == null) {
                return null;
            }

            try {
                return OBJECT_MAPPER.writeValueAsBytes(data);
            } catch (final Exception e) {
                throw new SerializationException("Error serializing JSON message", e);
            }
        }

        @Override
        public void close() {}

        @Override
        public Serializer<T> serializer() {
            return this;
        }

        @Override
        public Deserializer<T> deserializer() {
            return this;
        }
    }

    /**
     * An interface for registering types that can be de/serialized with {@link JSONSerde}.
     */
    @SuppressWarnings("DefaultAnnotationParam") // being explicit for the example
    @JsonTypeInfo(use = JsonTypeInfo.Id.NAME, include = JsonTypeInfo.As.PROPERTY, property = "_t")
    @JsonSubTypes({
                      @JsonSubTypes.Type(value = MovieTicket.class, name = "mt"),
					  @JsonSubTypes.Type(value = YearlyMovieFigures.class, name = "ym"),
                  })
    public interface JSONSerdeCompatible {

    }
	
    // POJO classes
	//{"title":"Avengers: Endgame","release_year":2019,"total_sales":856980506}
    static public class MovieTicket implements JSONSerdeCompatible {
        public String title;
		public Integer release_year;
		public Integer total_sales;
    }
	
	static public class YearlyMovieFigures implements JSONSerdeCompatible {
		
		public Integer key;
		public Integer max;
		public Integer min;
		
		//Jackson needs access to the default constructor to deserialize, add the default constructor to the pojo, ie:
		public YearlyMovieFigures(){}
		
		public YearlyMovieFigures(Integer k, Integer mx, Integer mi){
			
				key = k;
				min = mx;
				max = mi;
		}
		
       
    }

    public static void main(final String[] args) {
		
		System.out.println("Week4 MinMaxDemo");
		
        final Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "streams-minmax");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, JSONSerde.class);
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, JSONSerde.class);
        props.put(StreamsConfig.CACHE_MAX_BYTES_BUFFERING_CONFIG, 0);
        props.put(StreamsConfig.COMMIT_INTERVAL_MS_CONFIG, 1000);

        // setting offset reset to earliest so that we can re-run the demo code with the same pre-loaded data
        props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
  
        final StreamsBuilder builder = new StreamsBuilder();

       
		
		final KStream<String, MovieTicket> views = builder.stream("streams-minmax-input", Consumed.with(Serdes.String(), new JSONSerde<>()));

        final KStream<Integer, YearlyMovieFigures> output = views
            .groupBy(
				(k, v) -> v.release_year, Grouped.with(Serdes.Integer(), new JSONSerde<>())
			)
			.aggregate(
				() -> new YearlyMovieFigures(0, Integer.MAX_VALUE, Integer.MIN_VALUE),
				((key, value, aggregate) ->
                 new YearlyMovieFigures(key,
                                        Math.min(value.total_sales, aggregate.min),
                                        Math.max(value.total_sales, aggregate.max))),
				Materialized.with(Serdes.Integer(), new JSONSerde<>()))
			.toStream();

        // write to the result topic
        output.to("streams-minmax-output", Produced.with(Serdes.Integer(), new JSONSerde<>()));
		

        
		
		
		
		
		
		
		final KafkaStreams streams = new KafkaStreams(builder.build(), props);
        final CountDownLatch latch = new CountDownLatch(1);

        // attach shutdown handler to catch control-c
        Runtime.getRuntime().addShutdownHook(new Thread("streams-pipe-shutdown-hook") {
            @Override
            public void run() {
                streams.close();
                latch.countDown();
            }
        });

        try {
            streams.start();
            latch.await();
        } catch (final Throwable e) {
            e.printStackTrace();
            System.exit(1);
        }
        System.exit(0);
    }
}

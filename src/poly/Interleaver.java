package poly;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Interleaver {
    public static <T> List<T> interleave(List<T> xs, List<T> ys) {
	return IntStream.range(0, Math.min(xs.size(), ys.size())).mapToObj(a -> Arrays.asList(xs.get(a), ys.get(a)))
		.flatMap(Collection::stream).collect(Collectors.toList());
    }

    public static <T, S> List<Pair<T, S>> toPairs(List<T> xs, List<S> ys) {
	return IntStream.range(0, Math.min(xs.size(), ys.size())).mapToObj(a -> new Pair<T, S>(xs.get(a), ys.get(a)))
		.collect(Collectors.toList());
    }

}

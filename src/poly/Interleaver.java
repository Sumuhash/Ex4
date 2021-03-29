package poly;

import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 * Used to interleave and pair up two lists.
 */
public class Interleaver {
  /**
   * Interleaving two lists using different types.
   *
   * @param xs list 1
   * @param ys list 2
   * @param <T> generic
   * @return interleaved list
   */
  public static <T> List<T> interleave(List<T> xs, List<T> ys) {
    return IntStream.range(0, Math.min(xs.size(), ys.size()))
      .mapToObj(a -> Arrays.asList(xs.get(a), ys.get(a)))
      .flatMap(Collection::stream).collect(Collectors.toList());
  }

  /**
   * Create list of pairs using different types.
   *
   * @param xs list 1
   * @param ys list 2
   * @param <T> generic
   * @param <S> generic
   * @return list of pairs
   */
  public static <T, S> List<Pair<T, S>> toPairs(List<T> xs, List<S> ys) {
    return IntStream.range(0, Math.min(xs.size(), ys.size()))
      .mapToObj(a -> new Pair<T, S>(xs.get(a), ys.get(a)))
      .collect(Collectors.toList());
  }
}

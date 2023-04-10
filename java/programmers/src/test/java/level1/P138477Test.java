package level1;

import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

import static org.assertj.core.api.Assertions.assertThat;


public class P138477Test {
    @Test
    public void test() {

//        List<Integer> a = Arrays.stream(new int[]{1,2,3,4,5}).collect(Collectors.toList());
        int[] a = new int[]{1,2,3,4,5};
        int aTest = Arrays.stream(a).boxed()
                .sorted(Collections.reverseOrder())
                .limit(a.length/3*3)
                .mapToInt(Integer::valueOf)
                .sum();
        List<Integer> b = Arrays.stream(a).boxed()
                .sorted(Collections.reverseOrder())
                        .collect(Collectors.toList());
        assertThat(aTest).isEqualTo(12);

    }
}

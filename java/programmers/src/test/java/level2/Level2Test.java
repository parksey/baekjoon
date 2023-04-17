package level2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;
import java.util.stream.Collectors;

import static org.assertj.core.api.Assertions.assertThat;


public class Level2Test {
    @Test
    public void p12941() {
        P12941 p = new P12941();
        assertThat(p.solution(new int[]{1,4,2}, new int[]{5,4,4})).isEqualTo(29);
        assertThat(p.solution(new int[]{1,2}, new int[]{3,4})).isEqualTo(10);
    }

    @Test
    public void p70129() {
        P70129 p = new P70129();
        assertThat(p.solution("110010101001")).isEqualTo(new int[]{3,8});
        assertThat(p.solution("01110")).isEqualTo(new int[]{3,3});
        assertThat(p.solution("1111111")).isEqualTo(new int[]{4,1});
    }

    @Test
    public void p12924() {
        P12924 p = new P12924();
        assertThat(p.solution(15)).isEqualTo(4);
    }

    @Test
    public void p12911() {
        P12911 p = new P12911();
        assertThat(p.solution(78)).isEqualTo(83);
        assertThat(p.solution(15)).isEqualTo(23);
        String s = "123";
        List<Character> a = List.of(s.charAt(0));
        List<Character> b = new ArrayList<>();

    }

    @Test
    public void p12981() {
        P12981 p = new P12981();
        assertThat(new int[]{3,3}).isEqualTo(p.solution(3, new String[]{"tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"}));
        assertThat(new int[]{0, 0}).isEqualTo(p.solution(5, new String[]{"hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"}));
        assertThat(new int[]{1,3}).isEqualTo(p.solution(2, new String[]{"hello", "one", "even", "never", "now", "world", "draw"}));
    }

    @Test
    public void p42842() {
        P42842 p = new P42842();
        assertThat(new int[]{4,3}).isEqualTo(p.solution(10,2));
        assertThat(new int[]{8,1}).isEqualTo(p.solution(8,1));
        assertThat(new int[]{24,24}).isEqualTo(p.solution(24,24));
    }

    @ParameterizedTest
    @CsvSource({"5, 2","6, 2","5000, 5","10, 2"})
    public void p12980(int data, int ret) {
        P12980 p = new P12980();
        assertThat(ret).isEqualTo(p.solution(data));
    }

    @ParameterizedTest
    @ValueSource(strings = {"2,6,8,14,168", "1,2,3,6"})
    public void p12953(String args) {
        List<Integer> datas = Arrays.stream(args.split(","))
                .mapToInt(value -> Integer.parseInt(value)).boxed().collect(Collectors.toList());

         int ret = datas.remove(datas.size()-1);

        P12953 p = new P12953();
        assertThat(ret).isEqualTo(p.solution(datas.stream().mapToInt(Integer::intValue).toArray()));
    }

    @ParameterizedTest
    @CsvSource({"4,5", "3,3"})
    public void p12914(int n, int ret) {
        assertThat(ret).isEqualTo(new P12914().solution(n));
    }

    @ParameterizedTest
    @ValueSource(strings ={"6, 1, 3, 2, 5, 4, 5, 2, 3, 3"
    ,"4, 1, 3, 2, 5, 4, 5, 2, 3, 2"
    ,"2, 1, 1, 1, 1, 2, 2, 2, 3, 1"})
    public void p138476(String data) {
        String[] d = data.split(",");
        List<Integer> set = Arrays.stream(data.split(", "))
                        .mapToInt(Integer::parseInt)
                                .boxed().collect(Collectors.toList());

        int k = set.remove(0);
        int result = set.remove(set.size()-1);
        int[] tangerine = set.stream()
                        .mapToInt(Integer::intValue)
                                .toArray();

        assertThat(result).isEqualTo(new P138476().solution(k, tangerine));
    }
}

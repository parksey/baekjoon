package level2;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

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
}

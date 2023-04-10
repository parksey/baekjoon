package level1;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;


public class Level1Test {
    @Test
    public void test92334() {
        P92334 p = new P92334();
        Assertions.assertThat(p.solution(new String[]{"muzi", "frodo", "apeach", "neo"}
                , new String[]{"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"}
                , 2)).isEqualTo(new int[]{2,1,1,0});

        Assertions.assertThat(p.solution(new String[]{"con", "ryan"}
                , new String[]{"ryan con", "ryan con", "ryan con", "ryan con"}
                , 3)).isEqualTo(new int[]{0,0});
    }
}

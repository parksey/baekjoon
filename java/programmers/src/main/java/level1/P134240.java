package level1;
import java.util.*;
public class P134240 {
    public static void solve() {
        SolutionP134240 sol = new SolutionP134240();
        sol.solution(new int[]{1,3,4,6});
    }
}

/**
 * 1대1 대결, 매 대결 = 음식의 종류와 양이 변경
 * 음식 일렬후, 왼쪽->오른쪽 다른 선수는 왼쪽 <- 오른쪽
 * 중앙에 물 배치 후 먼저 먹는 사람 승자
 */


class SolutionP134240 {
    public String solution(int[] food) {
        String answer = "";

        StringBuilder half = getHalf(food);
        String reverseHalf = new StringBuilder(half).reverse().toString();
        half.append(0+reverseHalf);

        return half.toString();
    }

    public StringBuilder getHalf(int[] food) {
        StringBuilder half = new StringBuilder();
        for (int i=1; i<food.length; i++) {
            addMultiData(half, i, food[i]);
        }
        return half;
    }

    public void addMultiData(StringBuilder sb, int data, int during) {
        for (int i=0; i < during/2; i++) {
            sb.append(data);
        }
    }
}
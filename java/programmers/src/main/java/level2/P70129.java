package level2;

import java.util.*;
import java.util.stream.IntStream;

public class P70129 {
    public int[] solution(String s) {
        int[] answer = new int[2];

        while(!s.equals("1")) {
            long nextValue = getValue(s);
            answer[1] += (s.length() - nextValue);
            answer[0]++;
            s = getBinary(nextValue);
        }


        return answer;
    }

    public long getValue(String s) {
        return IntStream.range(0, s.length())
                .mapToObj(i -> s.charAt(i))
                .filter(c->c=='1')
                .count();
    }

    public String getBinary(long value) {
        StringBuilder sb = new StringBuilder();

        while (value > 1) {
            sb.append(value%2);
            value /= 2;
        }
        sb.append(value);

        return sb.reverse().toString();
    }
}

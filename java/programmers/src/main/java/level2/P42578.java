package level2;
import java.util.*;
import java.util.stream.*;

public class P42578 {
    public int solution(String[][] clothes) {
        Map<String, Integer> clothMap = makeMap(clothes);
        int answer = 1;
        for (int data : clothMap.values()) {
            answer = answer * (data+1);
        }


        return answer-1;
    }

    public Map<String, Integer> makeMap(String[][] clothes) {
        Map<String, Integer> clothMap = new HashMap<>();
        for (String[] cloth : clothes) {
            if (clothMap.containsKey(cloth[1])) {
                clothMap.put(cloth[1], clothMap.get(cloth[1]) + 1);
                continue;
            }

            clothMap.put(cloth[1], 1);
        }
        return clothMap;
    }
}

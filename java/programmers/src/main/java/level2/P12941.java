package level2;

import java.util.*;

public class P12941 {
    public int solution(int[] A, int[] B) {
        int result = 0;

        Arrays.sort(A);
        int[] sortedB = Arrays.stream(B)
                .boxed()
                .sorted((p, t) -> {
                    return t- p;
                })
                .mapToInt(Integer::intValue)
                .toArray();

        for(int i=0; i <A.length; i++) {
            result += (A[i] * sortedB[i]);
        }

        return result;
    }
    public boolean addStack(List<String> stackString, char data) {
        if (data == ')') {
            if (stackString.isEmpty()) {
                return false;
            }

            stackString.remove(stackString.size()-1);
            return true;
        }

        stackString.add(String.valueOf(data));
        return true;
    }
}

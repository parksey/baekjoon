package level2;

import java.util.Arrays;
import java.util.Collections;

public class P12953 {
    public int solution(int[] arr) {
        Arrays.sort(arr);
        int[] sortedArr = Arrays.stream(arr)
                .boxed()
                .sorted(Collections.reverseOrder())
                .mapToInt(Integer::intValue)
                .toArray();

        int index = arr[arr.length-1];

        while (!canDiv(sortedArr, index)) {
            index++;
        }

        return index;
    }

    public boolean canDiv(int[] arr, int index) {
        for (int data: arr) {
            if (index % data != 0) {
                return false;
            }
        }
        return true;
    }
}

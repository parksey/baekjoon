package level2;

public class P12924 {
    public int solution(int n) {
        int answer = 0;
        int[] sumList = new int[n+1];
        setSum(sumList);

        answer = count(sumList, n);
        return answer;
    }

    public void setSum(int[] sumList) {
        for(int i = 1; i < sumList.length; i++) {
            sumList[i] = i + sumList[i-1];
        }
    }

    public int count(int[] sumList, int n) {
        int lastIndex = 1;
        int frontIndex = 0;
        int ret = 0;

        while (lastIndex <= n) {
            int min = (sumList[lastIndex] - sumList[frontIndex]);
            if (min == n) {
                ret++;
                lastIndex++;
                frontIndex++;
                continue;
            }

            if (min < n) {
                lastIndex++;
                continue;
            }


            frontIndex++;
        }
        return ret;
    }
}
/*
0 1 2 3  4  5  6  7  8  9 10 11 12 13 14  15

0 1 3 6 10 15 21 28 36 45 55 66 78 91 105 120

0 5 => 1 6
2 6
3 6 =>
*/
package level2;

public class P12911 {
    public int solution(int n) {
        int comp = countOne(n);
        int index = n+1;
        while (comp != countOne(index)) {
            index++;
        }


        return index;
    }

    public int countOne(int n) {
        int ret = 1;

        while (n > 1) {
            if (n % 2 == 1) {
                ret++;
            }
            n/=2;
        }

        return ret;
    }
}

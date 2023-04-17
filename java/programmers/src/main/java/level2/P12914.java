package level2;

public class P12914 {
    public long solution(int n) {
        if (n == 1) {return 1;}
        if (n == 2) {return 2;}

        long answer = 0;
        int beforeOne = 2;
        int beforeTwo = 1;

        for (int i = 3; i < n; i++) {
            int next = (beforeOne + beforeTwo) % 1234567;
            beforeTwo = beforeOne;
            beforeOne = next;
        }


        return (beforeOne + beforeTwo) % 1234567;
    }
}

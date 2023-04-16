package level2;

public class P42842 {
    public int[] solution(int brown, int yellow) {
        int[] answer = {};
        return getResult(brown, yellow);
    }

    public int[] getResult(int brown, int yellow) {
        for (int i = 1; i <= Math.sqrt(yellow); i++) {
            if (yellow % i !=0) {
                continue;
            }
            int y = i+2;
            int x = (yellow / i)+2;
            if (canMake(brown, x,y)) {
                return new int[] {x,y};
            }
        }
        return new int[] {0, 0};
    }

    public boolean canMake(int brown, int x, int y) {
        return (x*2+y*2 -4)==brown ? true : false;
    }
}

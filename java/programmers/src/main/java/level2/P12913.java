package level2;

public class P12913 {
    int solution(int[][] land) {
        int answer = 0;
        for (int i = 1; i < land.length; i++) {

            for (int j = 0; j < land[i].length; j++) {
                land[i][j] += maxData(j, land[i-1]);
            }
        }
        return maxData(-1,land[land.length-1]);
    }

    public int maxData(int index, int[] land) {
        int max = 0;

        for (int i = 0 ; i < land.length; i++) {
            if (i == index) {
                continue;
            }
            max = max < land[i] ? land[i] : max;
        }
        return max;
    }
}
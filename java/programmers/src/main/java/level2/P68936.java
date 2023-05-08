package level2;

public class P68936{
    public int[] solution(int[][] arr) {
        SplitSquare splitSquare = new SplitSquare(arr);

        splitSquare.start();
        return splitSquare.getResult();
    }
}

class SplitSquare {
    private int[][] map;
    private int[] result;

    public SplitSquare(int[][] arr) {
        this.map = arr;
        this.result = new int[2];
    }

    public void start() {
        split(0,0,map.length);
    }

    public void split(int x, int y, int length) {
        int ret = isOne(x,y,length);
        if (ret != -1) {
            this.result[ret]++;
            return;
        }

        if (length == 1) {
            this.result[this.map[y][x]]++;
            return;
        }


        int line = length/2;
        split(x,y,line);
        split(x+line,y,line);
        split(x,y+line,line);
        split(x+line,y+line,line);
    }

    public int isOne(int startX, int startY, int length) {
        int data = this.map[startY][startX];
        for (int i = startY; i < startY + length; i++) {
            for (int j = startX; j < startX + length; j++) {
                if (data != this.map[i][j]) {
                    return -1;
                }
            }
        }
        return data;
    }

    public int[] getResult() {
        return result;
    }
}

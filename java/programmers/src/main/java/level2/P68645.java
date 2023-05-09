package level2;

import java.util.*;
public class P68645  {
    public int[] solution(int n) {
        int[] answer = {};
        Tri tri = new Tri(n);

        return tri.getResult();
    }
}

class Tri {
    private static final int[][] DIRECTION = {{1,0}, {0,1}, {-1,-1}};

    private List<int[]> triangleMap;
    private int[] result;
    public Tri(int n) {
        this.triangleMap = new ArrayList<>();
        this.result = new int[n*(n+1)/2];

        for (int i = 0; i < n; i++) {
            this.triangleMap.add(new int[i+1]);
        }
        set();
    }

    public void set() {
        int dir = 0;
        int index = 0;
        int y = -1;
        int x= 0;
        for (int i = this.triangleMap.size(); i > 0; i--) {
            for (int j = 0; j < i; j++) {
                y += DIRECTION[dir][0];
                x += DIRECTION[dir][1];

                setNextIndex(y, x, ++index);
            }

            dir = (dir+1) % 3;
        }
    }

    public void setNextIndex(int y, int x, int index) {
        int[] data = this.triangleMap.get(y);
        data[x] = index;
    }

    public int[] getResult() {
        int index = 0;

        for (int[] line : this.triangleMap) {
            for (int data : line) {
                this.result[index++] = data;
            }
        }
        return this.result;
    }
}
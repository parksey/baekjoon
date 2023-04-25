package level2;

import java.util.*;

public class P1844 {

    static class Location {
        public static int maxX;
        public static int maxY;

        private int x;
        private int y;
        private int time;

        public Location(int y,int x, int time) {
            this.y = y;
            this.x = x;
            this.time = time;
        }

        public static void setMax(int[][] maps) {
            Location.maxY = maps.length;
            Location.maxX = maps[0].length;
        }

        public int getX() {return x;}
        public int getY() {return y;}
        public int getTime() {return time;}

        public boolean outOfRange() {
            return x >= maxX || x < 0 || y >= maxY || y < 0;
        }

        public boolean isLastIndex() {
            return y == maxY-1 && x == maxX - 1;
        }

        @Override
        public String toString() {
            return y+"_"+x;
        }
    }

    public int solution(int[][] maps) {
        Location.setMax(maps);

        int answer = 0;

        Queue<Location> location = new LinkedList<>();
        location.add(new Location(0,0,1));
        int[][] dir = {{-1,0}, {0,-1}, {1,0}, {0,1}};

        int[][] visitMap = new int[Location.maxY][Location.maxX];
        initMap(visitMap);

        while (!location.isEmpty()) {
            Location current = location.remove();
            if (current.isLastIndex()) {
                break;
            }

            for (int[] d : dir) {
                Location next = new Location(d[0] + current.getY(), d[1] + current.getX(), current.getTime()+1);

                if (next.outOfRange() || maps[next.getY()][next.getX()] == 0 || visitMap[next.getY()][next.getX()] != -1) {
                    continue;
                }

                location.add(next);
                visitMap[next.getY()][next.getX()] = next.getTime();
            }
        }

        return visitMap[Location.maxY-1][Location.maxX-1];
    }

    public void initMap(int[][] map) {
        for (int i = 0; i < Location.maxY; i++) {
            for (int j= 0; j < Location.maxX; j++) {
                map[i][j]=-1;
            }
        }
    }
}
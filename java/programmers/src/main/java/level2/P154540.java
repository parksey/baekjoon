package level2;

import java.util.*;

public class P154540  {
    public int[] solution(String[] maps) {
        Location.setSize(maps.length, maps[0].length());

        List<Integer> ret = findIsland(maps);

        if (ret.isEmpty()) {
            return new int[]{-1};
        }

        ret.sort(Comparator.naturalOrder());
        return ret.stream()
                .mapToInt(Integer::valueOf)
                .sorted()
                .toArray();
    }

    public List<Integer> findIsland(String[] maps) {
        boolean[][] visit = new boolean[maps.length][maps[0].length()];
        List<Integer> ret = new ArrayList<>();

        for (int i = 0;  i < maps.length; i++) {
            for (int j = 0; j < maps[0].length(); j++) {
                if (maps[i].charAt(j) == 'X') {
                    visit[i][j] = true;
                    continue;
                }

                if (visit[i][j]) {
                    continue;
                }

                ret.add(makeIsland(visit, maps, new Location(i,j)));
            }
        }
        return ret;
    }

    public int makeIsland(boolean[][] visit, String[] maps, Location start) {
        int count = 0;
        Queue<Location> locations = new LinkedList<>();

        locations.add(start);
        visit[start.getY()][start.getX()] = true;
        count += getData(maps, start);

        int[][] direction = {{-1,0}, {0,-1}, {1,0}, {0,1}};

        while (!locations.isEmpty()) {
            Location cur = locations.remove();

            for (int[] dir : direction) {
                Location newLoc = cur.move(dir[0], dir[1]);

                if (newLoc.outOfRange()) {
                    continue;
                }

                if (visit[newLoc.getY()][newLoc.getX()] || maps[newLoc.getY()].charAt(newLoc.getX()) == 'X') {
                    continue;
                }

                locations.add(newLoc);
                visit[newLoc.getY()][newLoc.getX()] = true;
                count += getData(maps, newLoc);
            }
        }
        return count;
    }

    public int getData(String[] maps, Location loc) {
        return maps[loc.getY()].charAt(loc.getX()) - '0';
    }
}

class Location {
    private static int X_SIZE;
    private static int Y_SIZE;

    private int x;
    private int y;

    public Location(int y, int x) {
        this.x = x;
        this.y = y;
    }

    public static void setSize(int y, int x) {
        Y_SIZE = y;
        X_SIZE = x;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public Location move(int y, int x) {
        return new Location(this.y+y, this.x+x);
    }

    public boolean outOfRange() {
        return this.x < 0 || this.x >= X_SIZE || this.y < 0 || this.y >= Y_SIZE;
    }
}



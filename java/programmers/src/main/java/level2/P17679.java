package level2;

import java.util.*;
public class P17679  {
    public int solution(int m, int n, String[] board) {
        int answer = 0;
        KaGame kaGame = new KaGame(board, m, n);

        return kaGame.start();
    }
}

class KaGame {
    private char[][] map;

    public KaGame(String[] board, int m, int n) {
        this.map = new char[m][n];
        for (int i = 0; i < board.length; i++) {
            this.map[i] = board[i].toCharArray();
        }
    }

    public int start() {
        int result = 0;

        while(true) {
            Set<Location> locations = setRemoveList();

            if (locations.size() == 0) {
                break;
            }

            result+=locations.size();
            remove(locations);
            fill();

        }


        return result;
    }

    public void fill() {
        for(int x=0; x < map[0].length; x++) {
            int lastIndex = map.length-1;
            for (int y = lastIndex; y >= 0; y--) {
                if (map[y][x]==' ') {
                    continue;
                }

                if (lastIndex == y) {
                    lastIndex--;
                    continue;
                }

                map[lastIndex][x] = map[y][x];
                map[y][x] = ' ';
                lastIndex--;
            }
        }
    }

    public void remove(Set<Location> locations) {
        for (Location loc : locations) {
            map[loc.getY()][loc.getX()] = ' ';
        }
    }

    public Set<Location> setRemoveList() {
        Set<Location> locations = new HashSet<>();
        for(int i=0; i < map.length-1; i++) {
            for (int j = 0; j < map[i].length-1; j++) {
                if(map[i][j]== ' ') {
                    continue;
                }

                if (map[i][j] == map[i][j+1]
                        && map[i][j] == map[i+1][j]
                        && map[i][j] == map[i+1][j+1]) {
                    locations.add(new Location(i,j));
                    locations.add(new Location(i+1,j));
                    locations.add(new Location(i,j+1));
                    locations.add(new Location(i+1,j+1));
                }
            }
        }
        return locations;
    }
}

class Location {
    int x;
    int y;
    public Location(int y, int x) {
        this.x = x;
        this.y = y;
    }

    public int getX() {return x;}
    public int getY() {return y;}

    @Override
    public boolean equals(Object obj) {
        Location loc = (Location) obj;

        return this.x == loc.getX() && this.y == loc.getY();
    }

    @Override
    public int hashCode() {
        return Objects.hash(x,y);
    }
}

package level2;

import java.util.*;
public class P17678 {
    public String solution(int n, int t, int m, int p) {
        String answer = "";
        GameP17678 game = new GameP17678(n,t,m,p);

        return game.start();
    }
}

class GameP17678 {
    private int n;
    private int t;
    private int m;
    private int p;

    private char[] result;
    private int currentData;

    private Map<Integer, Character> parseMap;

    public GameP17678(int n, int t, int m, int p) {
        this.n = n;
        this.t = t;
        this.m = m;
        this.p = p;
        this.result = new char[t];
        this.currentData = 0;

        this.parseMap = new HashMap<>();
        for (int i=0 ; i < 6; i++) {
            parseMap.put(10+i, (char)((int)'A'+i));
        }
    }

    public String start() {
        StringBuilder sb = new StringBuilder();
        int limitLength = this.p + this.t*this.m;
        sb.append(this.currentData);

        while (sb.length() <= limitLength) {
            this.currentData++;
            sb.append(nextString());
        }

        String stringMap = sb.toString();

        int index = this.p-1;
        for (int i = 0; i < this.t; i++) {
            this.result[i] = stringMap.charAt(index + i*this.m);
        }

        return String.valueOf(this.result);
    }

    public String nextString() {
        int n = this.currentData;
        StringBuilder sb = new StringBuilder();
        while (n > 0) {
            int na = n%this.n;
            if (na >= 10) {
                sb.append(this.parseMap.get(na));
            }
            else {
                sb.append(na);
            }
            n /= this.n;
        }
        sb.reverse();
        return sb.toString();
    }
}
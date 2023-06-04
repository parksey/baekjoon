package level2;

import java.util.*;
import java.util.stream.*;


public class P17683 {
    public String solution(String m, String[] musicinfos) {
        List<Music> musics = new ArrayList<>();

        for (String info : musicinfos) {
            musics.add(makeMusic(info));
        }
        musics.sort((m1, m2) -> {
            if (m1.getTime() > m2.getTime()) {
                return -1;
            }
            else if (m1.getTime() < m2.getTime()) {
                return 1;
            }

            return 1;
        });
        System.out.println(musics);
        String[] mArray = Music.parseSplit(m).toArray(String[]::new);

        for (Music music : musics) {
            if (music.containCode(mArray)) {
                return music.getMusicName();
            }
        }

        return "(None)";
    }

    public Music makeMusic(String musicInfo) {
        String[] infos = musicInfo.split(",");
        return new Music(infos[2], infos[3], calcTime(infos[0], infos[1]));
    }

    public int calcTime(String startTime, String endTime) {
        String[] sTime = startTime.split(":");
        String[] eTime = endTime.split(":");

        int hour = Integer.parseInt(eTime[0]) - Integer.parseInt(sTime[0]);
        int min = Integer.parseInt(eTime[1]) - Integer.parseInt(sTime[1]);

        return hour * 60 + min;
    }
}

class Music {
    private String[] musicData;
    private String musicName;
    private int time;

    public Music(String musicName, String code, int time) {
        this.musicName = musicName;
        this.musicData = initData(parseSplit(code), time);
        this.time = time;
    }

    public static List<String> parseSplit(String code) {
        List<String> data = new ArrayList<>();

        for (int i = 0; i < code.toCharArray().length; i++) {
            if (code.charAt(i) == '#') {
                data.set(data.size()-1, data.get(data.size()-1)+"#");
                continue;
            }

            data.add(String.valueOf(code.charAt(i)));
        }
        return data;
    }

    public String[] initData(List<String> code, int time) {
        List<String> ret = new ArrayList<>();

        for (int i = 0; i < time / code.size(); i++) {
            ret.addAll(code);
        }
        ret.addAll(
                code.subList(0, time % code.size())
        );
        return ret.toArray(String[]::new);
    }


    public boolean containCode(String[] m) {
        if (this.musicData.length == 0) {
            return false;
        }

        int[][] map = new int[this.musicData.length][m.length];

        for (int musicIndex = 0; musicIndex < map.length; musicIndex++) {
            if (this.musicData[musicIndex].equals(m[0])) {
                map[musicIndex][0]++;
            }

            if (map[musicIndex][0] == m.length) {
                return true;
            }
        }
        for (int mIndex = 1; mIndex < m.length; mIndex++) {
            if (this.musicData[0].equals(m[mIndex])) {
                map[0][mIndex]++;
            }
            if (map[0][mIndex] == m.length) {
                return true;
            }
        }


        for (int musicIndex=1; musicIndex < map.length; musicIndex++) {
            for (int mIndex = 1; mIndex < map[musicIndex].length; mIndex++) {
                if (!m[mIndex].equals(this.musicData[musicIndex])) {
                    continue;
                }

                map[musicIndex][mIndex] = map[musicIndex-1][mIndex-1] + 1;
                if (map[musicIndex][mIndex] == m.length) {
                    return true;
                }
            }
        }

        return false;
    }

    public String getMusicName() {
        return this.musicName;
    }

    public int getTime() {
        return this.time;
    }

    public String toString(){
        return time+"_"+musicName;
    }
}


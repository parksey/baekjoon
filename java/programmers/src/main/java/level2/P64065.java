package level2;

import java.util.*;
import java.util.stream.*;

public class P64065 {
    public int[] solution(String s) {
        int[] answer = {};

        DataList datas = new DataList();

        datas.parse(s);
        return datas.result();
    }
}

class DataList {
    private List<int[]> parseParam;

    public DataList() {
        parseParam = new ArrayList<>();
    }

    public void parse(String s) {
        s = s.substring(1, s.length()-1);
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '{') {
                makeList(i+1, s);
            }
        }

        Collections.sort(parseParam, (a1,a2) -> {
            return a1.length - a2.length;
        });
    }

    public void makeList(int index, String s) {
        StringBuilder sb = new StringBuilder();
        while (s.charAt(index) != '}') {
            sb.append(s.charAt(index));
            index++;
        }

        parseParam.add(Arrays.stream(sb.toString().split(","))
                .mapToInt(Integer::parseInt).toArray());
    }

    public int[] result() {
        List<Integer> ret = new ArrayList<>();

        for (int[] eachArr: parseParam) {
            addEach(ret, eachArr);
        }
        return ret.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }

    public void addEach(List<Integer> ret, int[] eachArr) {
        for (int data : eachArr) {
            if (!ret.contains(data)) {
                ret.add(data);
            }
        }
    }
}
package level2;

import java.util.*;

public class P17677 {
    public int solution(String str1, String str2) {
        int answer = 0;

        List<String> str1Sep = Jacard.sep(str1.toLowerCase());
        List<String> str2Sep = Jacard.sep(str2.toLowerCase());

        Map<String, Integer> str1Map = Jacard.parseMap(str1Sep);
        Map<String, Integer> str2Map = Jacard.parseMap(str2Sep);

        int total = Jacard.totalCount(str1Map, str2Map);
        int same = Jacard.makeSameCount(str1Map, str2Map);
        System.out.println(total+":"+same);

        if (same + total == 0) {
            return 65536;
        }

        return (int)(65536 * (double)same / total);
    }
}

class Jacard {
    public static List<String> sep(String str) {
        List<String> ret = new ArrayList<>();
        for (int i = 0; i < str.length()-1; i++) {
            String sub = str.substring(i,i+2);
            if (!canAdd(sub)) {
                continue;
            }
            ret.add(sub);
        }

        System.out.println(ret);
        return ret;
    }

    public static Map<String, Integer> parseMap(List<String> str) {
        Map<String, Integer> parseMap  = new HashMap<>();
        for (String s : str) {
            if (!parseMap.containsKey(s)) {
                parseMap.put(s, 1);
                continue;
            }
            parseMap.put(s, parseMap.get(s)+1);
        }
        return parseMap;
    }


    private static boolean canAdd(String s) {
        for (char c : s.toCharArray()) {
            if (!isAlphabet(c)) {
                return false;
            }
        }
        return true;
    }

    private static boolean isAlphabet(char c) {
        if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
            return true;
        }
        return false;
    }

    public static int totalCount(Map<String, Integer> str1Map, Map<String, Integer> str2Map) {
        Map<String, Integer> total = new HashMap<>(str1Map);

        for (String s: str2Map.keySet()) {
            if (!total.containsKey(s)) {
                total.put(s, str2Map.get(s));
                continue;
            }

            if (total.get(s) < str2Map.get(s)) {
                total.put(s, str2Map.get(s));
            }
        }
        // abab : ab ba ab
        // baba : ba ab ba
        // ab ba ab ba
        // ab ba
        System.out.println("total: "+total);
        return total.values().stream()
                .mapToInt(Integer::intValue)
                .sum();
    }

    public static int makeSameCount(Map<String, Integer> str1Map, Map<String, Integer> str2Map) {

        Map<String, Integer> same = new HashMap<>();
        for (String s: str2Map.keySet()) {
            if (!str1Map.containsKey(s)) {
                continue;
            }

            if (str1Map.get(s) > str2Map.get(s)) {
                same.put(s, str2Map.get(s));
            }
            else {
                same.put(s, str1Map.get(s));
            }
        }

        System.out.println("same: "+same);
        return same.values().stream()
                .mapToInt(Integer::intValue)
                .sum();
    }
}
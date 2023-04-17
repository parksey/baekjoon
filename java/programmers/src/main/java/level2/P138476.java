package level2;

import java.util.*;

public class P138476 {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        Map<Integer, Integer> countMap = getCountMap(tangerine);

        List<Entry> entryList = setEntryList(countMap);

        int kcount = 0;
        for (Entry entry : entryList) {
            answer++;
            kcount += entry.getValue();
            if (kcount >= k) {
                break;
            }
        }
        return answer;
    }

    public List<Entry> setEntryList(Map<Integer, Integer> countMap) {
        List<Entry> eList = new ArrayList<>();

        for (int key : countMap.keySet()) {
            eList.add(new Entry(key, countMap.get(key)));
        }
//        Collections.sort(eList, Comparator.comparing(Entry::getValue, Collections.reverseOrder()));
        Collections.sort(eList, (entry1, entry2)-> {
            if (entry1.getValue() > entry2.getValue()) {
                return -1;
            }

            if (entry1.getValue() < entry2.getValue()) {
                return 1;
            }
            return 0;
        });
        return eList;
    }

    public Map<Integer, Integer> getCountMap(int[] tangerine) {
        Map<Integer, Integer> countMap = new HashMap<>();

        for(int data : tangerine) {
            addData(countMap, data);
        }
        return countMap;
    }

    public void addData(Map<Integer, Integer> countMap, int data) {
        if (countMap.containsKey(data)) {
            countMap.put(data, countMap.get(data)+1);
            return;
        }
        countMap.put(data, 1);
    }
}

class Entry {
    private int key;
    private int value;

    public Entry(int key, int value) {
        this.key =key;
        this.value = value;
    }

    public int getValue() {
        return value;
    }
}
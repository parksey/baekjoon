package level2;
import java.util.*;

public class P72411 {
    public String[] solution(String[] orders, int[] course) {
        String[] answer = {};

        for (int i = 0; i < orders.length; i++) {
            char[] arr = orders[i].toCharArray();
            Arrays.sort(arr);
            orders[i] = String.valueOf(arr);
        }

        List<String> result = new ArrayList<>();
        for (int c : course) {
            Course cs = new Course(c);
            cs.setMap(orders);
            cs.remainMax();

            result.addAll(cs.getKeySet());
        }


        return getSortArr(result);
    }

    public String[] getSortArr(List<String> res) {
        return res.stream()
                .sorted()
                .toArray(String[]::new);
    }
}

class Course{
    int course;
    int max;

    Map<String, Integer> courseMap;
    public Course(int course) {
        this.course = course;
        this.courseMap = new HashMap<>();
        this.max = 0;
    }

    public void setMap(String[] orders) {
        for (String order : orders) {
            StringBuilder sb = new StringBuilder();
            makeSubString(order, sb, -1);
        }
    }

    public void makeSubString(String order, StringBuilder sb, int start) {
        if (sb.length() == this.course) {
            if (!this.courseMap.containsKey(sb.toString())) {
                this.courseMap.put(sb.toString(), 1);
                return;
            }

            int count = this.courseMap.get(sb.toString()) + 1;
            this.courseMap.put(sb.toString(), count);

            if (this.max < count) {
                this.max = count;
            }

            return;
        }

        char[] arr = order.toCharArray();
        for (int i = start+1; i < arr.length; i++) {
            sb.append(arr[i]);
            makeSubString(order, sb, i);
            sb.deleteCharAt(sb.length()-1);
        }
    }

    public void remainMax() {
        Map<String, Integer> course = new HashMap<>();
        Iterator<Map.Entry<String, Integer>> iter = courseMap.entrySet().iterator();
        while (iter.hasNext()) {
            Map.Entry<String, Integer> entry = iter.next();
            if(entry.getValue() < this.max || entry.getValue() == 1) {
                iter.remove();
            }
        }
    }

    public Set<String> getKeySet() {
        return this.courseMap.keySet();
    }
}
package level2;

import java.util.*;

public class P76502 {
    public int solution(String s) {
        int answer = 0;

        if (LotationS.check(s)){
            answer++;
        }

        StringBuilder sb = new StringBuilder(s);

        for(int i = 0; i < s.length()-1; i++) {
            sb.append(sb.charAt(0));
            sb.deleteCharAt(0);
            if (LotationS.check(sb.toString())) {
                answer++;
            }
        }


        return answer;
    }
}


class LotationS {
    public static Map<Character, Character> closeMap = new HashMap<>();

    static {
        closeMap.put('}', '{');
        closeMap.put(']', '[');
        closeMap.put(')', '(');
    }


    public static boolean check(String s) {
        char[] sData = s.toCharArray();
        if (closeMap.containsKey(sData[0])) {
            return false;
        }

        Stack<Character> stack = new Stack<>();
        stack.push(sData[0]);

        for(int i = 1; i < s.length(); i++) {
            if (!checkData(stack, sData[i])) {
                return false;
            }
        }

        return stack.isEmpty();
    }

    public static boolean checkData(Stack<Character> stack, Character data) {
        if (stack.isEmpty()) {
            stack.add(data);
            return true;
        }

        if (closeMap.containsKey(data)) {
            if (closeMap.get(data) != stack.peek()) {
                return false;
            }

            stack.pop();
            return true;
        }

        stack.add(data);
        return true;
    }
}
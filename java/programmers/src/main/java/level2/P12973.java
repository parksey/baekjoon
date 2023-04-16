package level2;

import java.util.*;

public class P12973 {
    public int solution(String s)
    {
        int answer = -1;

        List<Character> stack = new ArrayList<>();
        stack.add(s.charAt(0));
        for (int i = 1; i < s.length(); i++) {
            delete(stack, s.charAt(i));
        }

        return stack.isEmpty() ? 1 : 0;

    }

    public void delete(List<Character> stack, Character data) {
        if (stack.isEmpty() || data != stack.get(stack.size()-1)) {
            stack.add(data);
            return;
        }
        stack.remove(stack.size()-1);


    }
    public int solutionStack(String s)
    {
        int answer = -1;

        Stack<Character> stack = new Stack<>();
        stack.push(s.charAt(0));
        for (int i = 1; i < s.length(); i++) {
            delete(stack, s.charAt(i));
        }


        return stack.isEmpty() ? 1: 0;
    }

    public void delete(Stack<Character> stack, Character data) {
        if (stack.isEmpty() || data != stack.get(stack.size()-1)) {
            stack.push(data);
            return;
        }
        stack.pop();


    }
}


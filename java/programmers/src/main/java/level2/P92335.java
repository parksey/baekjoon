package level2;

public class P92335 {
    public int solution(int n, int k) {
        int answer = 0;
        String strNumber = parse(n, k);

        String[] strList = strNumber.split("0");

        for (String a : strList) {
            if(isPrime(a)) {
                answer++;
            }
        }

        return answer;
    }

    public String parse(int n, int k) {
        StringBuilder sb = new StringBuilder();

        while (n > 0) {
            sb.append(n%k);
            n /= k;
        }
        sb.reverse();
        return sb.toString();
    }

    public boolean isPrime(String num) {
        if (num.isEmpty()|| num == null) {
            return false;
        }

        Long number = Long.parseLong(num);

        if(number == 1) {
            return false;
        }

        if (number == 2) {
            return true;
        }

        for (int i = 3; i < Math.sqrt(number)+1; i++) {
            if (number%i==0) {
                return false;
            }
        }
        return true;
    }
}

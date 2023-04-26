package level2;

import java.util.*;
import java.util.stream.*;

public class P17686 {
    public String[] solution(String[] files) {
        return new FileSort().sortFile(files);
    }
}

class FileSort {
    public String[] sortFile(String[] files) {
        return Arrays.stream(files)
                .map(s->map(s))
                .sorted((s1, s2)-> sort(s1,s2))
                .map(s-> parse(s))
                .toArray(String[]::new);
    }

    public String[] map(String fileName) {
        String[] ret = new String[3];

        int index = setHead(ret, fileName);

        index = setNumber(ret, fileName, index);

        if (index < fileName.length()) {
            ret[2] = fileName.substring(index);
        }
        else {
            ret[2] = "";
        }

        return ret;
    }

    public int setHead(String[] ret, String fileName) {
        StringBuilder sb = new StringBuilder();
        int index = 0;
        while (index < fileName.length() &&
                !Character.isDigit(fileName.charAt(index))) {
            sb.append(fileName.charAt(index));
            index++;
        }
        ret[0] = sb.toString();
        return index;
    }

    public int setNumber(String[] ret, String fileName, int index) {
        StringBuilder sb = new StringBuilder();

        while (index < fileName.length() &&
                Character.isDigit(fileName.charAt(index))) {
            sb.append(fileName.charAt(index));
            index++;
        }
        ret[1] = sb.toString();
        return index;
    }


    public int sort(String[] s1, String[] s2) {
        String head1 = s1[0].toLowerCase();
        String head2 = s2[0].toLowerCase();

        if (!head1.equals(head2)) {
            return head1.compareTo(head2);
        }

        int num1 = Integer.parseInt(s1[1]);
        int num2 = Integer.parseInt(s2[1]);
        if (num1 > num2) {
            return 1;
        } else if (num1 < num2) {
            return -1;
        }

        return 0;
    }

    public String parse(String[] fileSet) {
        return String.join("", fileSet);
    }
}
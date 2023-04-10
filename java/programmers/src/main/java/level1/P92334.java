package level1;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class P92334 {
    public int[] solution(String[] id_list, String[] report, int k) {
        /**
         * 각 유저는 한 번에 한 명의 유저 신고
         * 1. 신고 횟수에 제한 없다.
         * 2. 여러 번 신고할 수 있지만, 동일한 유저에 대한 신고는 1회로 측정
         * k번 이상 신고된 유저는 게시판 이용이 정지
         * 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송
         */
        int[] answer = new int[id_list.length];
        Map<String, Integer> totalCnt = new HashMap<>();
        Map<String, Member> members = new HashMap<>();
        setId(members, totalCnt, id_list);
        setReport(members, report);

        for (int i=0; i < id_list.length; i++) {
            Member member = members.get(id_list[i]);

            if (member.getReportedCnt() >= k) {
                checkList(member, totalCnt);
            }
        }

        int index = 0;
        for(String name : id_list) {
            answer[index++] = totalCnt.get(name);
        }

        return answer;
    }

    private void checkList(Member member, Map<String, Integer> answer) {
        for (String reported : member.getReported()) {
            answer.put(reported, answer.get(reported) + 1);
        }

    }

    private void setId(Map<String, Member> members, Map<String, Integer> answer, String[] id_list) {
        for(String id: id_list) {
            members.put(id, new Member(id));
            answer.put(id, 0);
        }
    }

    private void setReport(Map<String, Member> members, String[] report) {
        for(String re : report) {
            String[] idReport = re.split(" ");

            Member member = members.get(idReport[0]);
            member.addReport(idReport[1]);


            Member reported = members.get(idReport[1]);
            reported.addReported(idReport[0]);
        }
    }
}

class Member {
    String myName;
    Set<String> report;
    Set<String> reported;

    public Member(String myName) {
        this.myName = myName;
        this.report = new HashSet<>();
        this.reported = new HashSet<>();
    }

    public void addReport(String report) {
        this.report.add(report);
    }

    public void addReported(String report) {
        this.reported.add(report);
    }

    public Set<String> getReported() {
        return reported;
    }

    public int getReportedCnt() {
        return reported.size();
    }
}


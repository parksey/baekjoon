package level2;

import java.util.*;
public class P42888 {
    public String[] solution(String[] record) {
        String[] answer = {};
        Room room = new Room(record);

        room.setResult();

        return room.getResult();
    }
}

class Room {
    private List<User> users;
    private String[] records;
    private List<Comment> result;


    public Room(String[] records) {
        this.users = new ArrayList<>();
        this.result = new ArrayList<>();
        this.records = records;
    }

    public void setResult() {
        for (String record: records) {
            parseRecord(record);
        }
    }

    public String[] getResult() {
        String[] ret = new String[this.result.size()];

        for (int i = 0; i < this.result.size(); i++) {
            ret[i] = this.result.get(i).toString();
        }
        return ret;
    }

    public void parseRecord(String record) {
        String[] recordList = record.split(" ");

        if ("Enter".equals(recordList[0])) {
            addComment(recordList);
            return;
        }

        if ("Leave".equals(recordList[0])) {
            removeComment(recordList);
            return;
        }
        changeComment(recordList);
    }

    public void addComment(String[] recordList) {
        User user = User.setUser(recordList[1], recordList[2]);
        this.result.add(new Comment(
                user
                , recordList[0]
        ));
    }

    public void removeComment(String[] recordList) {
        this.result.add(new Comment(
                User.getUser(recordList[1])
                , recordList[0]
        ));
    }

    public void changeComment(String[] recordList) {
        User.setUser(recordList[1], recordList[2]);
    }
}

class Comment {
    private User user;
    private String msg;

    public Comment(User user, String msg) {
        this.user = user;
        this.msg = msg;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(user.getName()+"님이 ");

        String ent = "들어왔습니다.";
        if ("Leave".equals(msg)) {
            ent = "나갔습니다.";
        }
        sb.append(ent);
        return sb.toString();
    }
}

class User {
    private static Map<String, User> users = new HashMap<>();

    private String id;
    private String name;

    private User(String id, String name) {
        this.id = id;
        this.name = name;
    }
    public static User setUser(String id, String name) {
        if (users.containsKey(id)) {
            User user = users.get(id);
            user.setName(name);
            return user;
        }

        User user = new User(id, name);
        users.put(id, user);
        return user;
    }

    public static User getUser(String id) {
        return users.get(id);
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public String getId() {
        return id;
    }

    @Override
    public boolean equals(Object obj) {
        User user = (User) obj;
        return this.id.equals(user.getId());
    }
}
package level2;

import java.util.*;
;
class P118667 {
        public int solution(int[] queue1, int[] queue2) {
            OneQu oq1 = makeQu(queue1);
            OneQu oq2 = makeQu(queue2);

            long boundary = oq1.getSum() + oq2.getSum();
            if (boundary % 2 == 1) {
                return -1;
            }

            TwoQu two = new TwoQu(oq1, oq2, boundary/2);

            return findMin(two, queue1.length*2);
        }

        public OneQu makeQu(int[] queue) {
            long sum = 0;

            Queue<Integer> q = new LinkedList<>();
            for (int data : queue) {
                q.add(data);
                sum += data;
            }
            return new OneQu(q, sum);
        }


        public int findMin(TwoQu two, int size) {
            int index = 0;
            while(index < size*2) {
                if (two.check()) {
                    return index;
                }

                two.remake();
                index++;
            }
            return -1;
        }

    }

    class TwoQu {
        long boundary;
        OneQu queue1;
        OneQu queue2;

        public TwoQu(OneQu queue1, OneQu queue2, long boundary) {
            this.queue1 = queue1;
            this.queue2 = queue2;
            this.boundary = boundary;
        }

        public void remake() {
            if (boundary > queue1.getSum()) {
                queue1.add(queue2.remove());
                return;
            }

            queue2.add(queue1.remove());
        }

        public boolean check() {
            return this.boundary == queue1.getSum();
        }



    }

    class OneQu {
        Queue<Integer> queue;
        long sum;

        public OneQu(Queue<Integer> queue, long sum) {
            this.queue = queue;
            this.sum = sum;
        }

        public long getSum() {
            return sum;
        }

        public int remove() {
            int data =queue.remove();
            sum -= data;
            return data;
        }

        public void add(int data) {
            queue.add(data);
            sum+=data;
        }
    }
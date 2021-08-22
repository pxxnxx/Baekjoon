import java.util.*;
public class Tree_1068 {
    static int count = 0;
    static int n, del;
    static int start;
    static ArrayList<Integer>[] arr = new ArrayList[50];
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        for (int i=0; i<50; i++)
            arr[i] = new ArrayList<>();

        int k;
        for (int i=0; i<n; i++) {
            k = sc.nextInt();
            if (k == -1)
                start = i;
            else
                arr[k].add(i);
        }
        del = sc.nextInt();
        if (del != start)
            search(start);
        System.out.println(count);
    }
    public static void search(int index) {
        if (arr[index].size() == 0){
            count++;
            return;
        }
        for (int i=0; i<arr[index].size(); i++){
            int next = arr[index].get(i);

            if (arr[index].size() == 1 && next == del) {
                count++;
                return;
            }

            if (next < n && next != del)
                search(next);

        }
    }
}

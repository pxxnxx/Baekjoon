import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BFS_5014 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int f = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());
        int g = Integer.parseInt(st.nextToken());
        int u = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int[] visit = new int[f+1];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(s);
        visit[s] = 1;
        int answer = -1;
        while (!queue.isEmpty()) {
            int temp = queue.poll();
            if (temp == g) {
                answer = visit[temp];
                break;
            }
            if (temp+u <= f && visit[temp+u] == 0) {
                queue.add(temp + u);
                visit[temp+u] = visit[temp] + 1;
            }
            if (temp-d > 0 && visit[temp-d] == 0) {
                queue.add(temp - d);
                visit[temp - d] = visit[temp] + 1;
            }
        }
        if (answer != -1)
            System.out.println(answer-1);
        else
            System.out.println("use the stairs");
    }
}

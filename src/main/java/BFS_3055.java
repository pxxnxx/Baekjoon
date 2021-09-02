import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BFS_3055 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(bf.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int[][] visit = new int[r][c];
        int[][] answer = new int[r][c];
        int[] start = new int[5000];
        int[] end = new int[2];
        int[] dx = {0,0,1,-1};
        int[] dy = {1,-1,0,0};
        int water = 0;
        boolean br = false;
        int yy, xx;
        for (int i=0; i<r; i++) {
            String input = bf.readLine();
            for (int j=0; j<c; j++) {
                char key = input.charAt(j);
                if (key == 'S') {
                    start[0] = i;
                    start[1] = j;
                    answer[i][j] = 1;
                    visit[i][j] = -1;
                }
                else if (key == '*') {
                    water++;
                    start[water*2] = i;
                    start[water*2+1] = j;
                    visit[i][j] = -1;
                }
                else if (key == 'X')
                    visit[i][j] = -1;
                else if (key == 'D') {
                    end[0] = i;
                    end[1] = j;
                    visit[i][j] = -1;
                }
            }
        }
        Queue<Integer> queue = new LinkedList<>();
        while (water >= 0) {
            queue.add(start[water*2]);
            queue.add(start[water*2+1]);
            water--;
        }
        while (!queue.isEmpty()) {
            int y = queue.poll();
            int x = queue.poll();

            for (int i=0; i<4; i++) {
                yy = y + dy[i];
                xx = x + dx[i];
                if (answer[y][x] == 0) {
                    if (yy >= 0 && yy < r && xx >= 0 && xx < c && visit[yy][xx] >= 0) {
                        visit[yy][xx] = -1;
                        queue.add(yy);
                        queue.add(xx);
                    }
                }
                else {
                    if (yy == end[0] && xx == end[1]) {
                        answer[yy][xx] = answer[y][x] + 1;
                        br = true;
                        break;
                    }
                    if (yy >= 0 && yy < r && xx >= 0 && xx < c && visit[yy][xx] != -1) {
                        answer[yy][xx] = answer[y][x] + 1;
                        visit[yy][xx] = -1;
                        queue.add(yy);
                        queue.add(xx);
                    }
                }
            }
            if (br)
                break;
        }
        if (answer[end[0]][end[1]] == 0)
            System.out.println("KAKTUS");
        else
            System.out.println(answer[end[0]][end[1]]-1);
    }
}

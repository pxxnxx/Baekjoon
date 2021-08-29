import java.io.*;
import java.util.*;
public class Simulation_14503 {
    public static int count = 1;
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;
        st = new StringTokenizer(bf.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(bf.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int vec = Integer.parseInt(st.nextToken());
        vec = 3-vec;
        int[][] arr = new int[n][m];
        int[] dx = {-1,0,1,0}; // 서 남 동 북
        int[] dy = {0,1,0,-1}; // 북 동 남 서

        for (int i=0; i<n; i++) {
            st = new StringTokenizer(bf.readLine());
            for (int j=0; j<m; j++)
                arr[i][j] = Integer.parseInt(st.nextToken());

        }
        int[] start = {r,c};
        int i = 0;
        int y, x;
        Boolean br = true;
        arr[start[0]][start[1]] = 2;
        while (br) {
            for (i=0; i<4; i++) {
                vec++;
                if (vec > 3)
                    vec -= 4;
                y = start[0] + dy[vec];
                x = start[1] + dx[vec];
                if (y>0 && y<n-1 && x>0 && x<m-1 && arr[y][x] == 0) {
                    arr[y][x] = 2;
                    start[0] = y;
                    start[1] = x;
                    count++;
                    break;
                }
            }
            if (i == 4) {
                int t = vec + 2;
                if (t > 3) {
                    t -= 4;
                }
                y = start[0] + dy[t];
                x = start[1] + dx[t];
                if (arr[y][x] == 2) {
                    start[0] = y;
                    start[1] = x;
                }
                if (arr[y][x] == 1) {
                    br = false;
                    break;
                }
            }
        }
        System.out.println(count);
    }
}

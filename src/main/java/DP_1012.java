import java.util.Collections;
import java.util.*;
public class DP_1012 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        ArrayList<Integer> answer = new ArrayList<Integer>();
        for (int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }
        answer.add(arr[0]);
        for (int i=0; i<n-1; i++){
            answer.add(Math.max((answer.get(i)+arr[i+1]),arr[i+1]));
        }
        System.out.println(Collections.max(answer));
    }
}

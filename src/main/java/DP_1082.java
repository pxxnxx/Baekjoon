import java.math.BigInteger;
import java.util.*;
public class DP_1082 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i=0; i<n; i++)
            arr[i] = sc.nextInt();
        int m = sc.nextInt();
        BigInteger[] weight = new BigInteger[m+1];
        for (int i=0; i<=m; i++)
            weight[i] = new BigInteger("0");
        BigInteger mul = new BigInteger("10");
        BigInteger max;
        for (int i=1; i<=m; i++){
            for (int j=0; j<n; j++){
                if (i-arr[j] >= 0){
                    max = weight[i-arr[j]].multiply(mul).add(BigInteger.valueOf(j));
                    if (max.compareTo(weight[i-1]) < 0) {
                        max = weight[i - 1];
                    }
                    if (max.compareTo(weight[i]) < 0) {
                        max = weight[i];
                    }
                    weight[i] = max;
                }
            }
        }
        System.out.println(weight[m]);


    }
}

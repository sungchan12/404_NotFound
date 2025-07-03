import java.util.Arrays;
import java.util.Random;

// 5개에 배열에 1~10까지의 숫자를 랜덤하게 입력하세요
// 단, 중복되지 않게 입력 하세요
// 전체 배열을 출력 하시오
// 배열에 최대, 최소 값을 출력 하시오

public class icProblem {
    public static void main(String[] args) {
        int[] array = new int[5];
        Random random = new Random();
        for (int i = 0; i < array.length; i++) {
            int num = random.nextInt(10)+1;
            boolean isDuplicated = false;
            for (int j = 0; j < i; j++) {
                if (array[j] == num) {
                    isDuplicated = true;
                    break;
                }
            }
            if (isDuplicated) {
                i--;
                continue;
            }
            array[i] = num;
        }
        System.out.println(Arrays.toString(array));
        int max = array[0];
        int min = array[0];
        for (int number : array) {
            if (max < number) {
                max = number;
            }
            if (min > number) {
                min = number;
            }
        }
        System.out.println("Max : " + max);
        System.out.println("Min : " + min);
    }
}

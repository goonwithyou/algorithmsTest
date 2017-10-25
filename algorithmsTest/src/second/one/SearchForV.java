package second.one;
/*
 * 输入：n个数的一个序列A=<a1,a2,...,an>和一个值v
 * 输出：下标i，使得v=A[i]，或者v不存在输出NIL
 */
public class SearchForV {
	public static String search(int[] in ,int v){
		for(int i=0;i<in.length;i++){
			if(in[i]==v){
				return String.valueOf(i);
			}
		}
		return "NIL";
	}
	
	public static void main(String[] args){
		int[] A = {1,2,3,4,5,6,7};
		int v = 8;
		System.out.println(search(A,v));
	}
}

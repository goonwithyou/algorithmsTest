package second.one;

public class BinaryAdd {
	public static void main(String[] args){
		int[] A = {1,1,1,1};
		int[] B = {1,1,1,0};
		int[] C = new int[5];
		
		int fl = 0;//标注是否有进位
		
		for(int i=A.length-1;i>=0;i--){
			int key = A[i] + B[i] + fl;
			if(key>=2){
				C[i+1] = key%2;
				fl = 1;
			}else{
				C[i+1] = key;
				fl = 0;
			}
		}
		//确定c0的数字
		if(fl==1){
			C[0] = 1;
		}else{
			C[0] = 0;
		}
		
		for(int a:C){
			System.out.print(a+" ");
		}
		
	}
}

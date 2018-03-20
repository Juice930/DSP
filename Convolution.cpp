#include <stdio.h>
int x[15],h[15],y[15];
main(){
	int i,j,m,n;
	printf("Enter value for m\n");
	scanf("%d",&m);
	printf("\nEnter value for n\n");
	scanf("%d",&n);
	printf("\Enter values for i/p x(n):\n");
	for(i=0;i<m;i++)
		scanf("%d",&x[i]);
	printf("\Enter values for i/p h(n):\n");
	for(i=0;i<n;i++)
		scanf("%d",&h[i]);
	for(i=m;i<m+n-1;i++)
		x[i]=0;
	for(i=n;i<m+n-1;i++)
		h[i]=0;
		
	for(i=0;i<m+n-1;i++){
		y[i]=0;
		for(j=0;j<=i;j++)
			y[i]+=x[j]*h[i-j];
	}
	printf("\n");
	for(i=0;i<m+n-1;i++)
		printf("%d ",y[i]);
}

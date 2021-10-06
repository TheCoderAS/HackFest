#include<stdio.h>
#define MAX 1000
int adj[10][10],dis[10][10];
void flyod_warshall(int n){
    int i,j,k;
    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            dis[i][j]=adj[i][j];
        }
    }
    for(k=1;k<=n;k++){
        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
                if(dis[i][k]==MAX || dis[k][j]==MAX){
                    continue;
                }
                else if(dis[i][k]+dis[k][j]<dis[i][j]){
                    dis[i][j]=dis[i][k]+dis[k][j];
                }
            }
        }
    }

}
int main (){
    int n,i,j;
    printf("Enter the number of vertices: ");
    scanf("%d",&n);
    printf("Enter the adjacency matrix: \n");
    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            scanf("%d",&adj[i][j]);
            if(adj[i][j]==0 && i!=j){
                adj[i][j]=MAX;
            }
        }
    }
    flyod_warshall(n);
    printf("The Distance Matrix: \n");
    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            printf("Distance from %d to %d is %d\n",i,j,dis[i][j]);
        }
        printf("\n");
    }
    return 0;
}
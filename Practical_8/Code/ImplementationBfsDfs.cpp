#include <iostream>
using namespace std;
y6
int graph[5][5] = {
    {0,1,1,0,0},
    {1,0,0,1,1},
    {1,0,0,0,1},
    {0,1,0,0,1},
    {0,1,1,1,0}
};

int visited[5];
void DFS(int v)
{
    cout << v + 1 << " ";
    visited[v] = 1;

    for(int i = 0; i < 5; i++)
    {
        if(graph[v][i] == 1 && visited[i] == 0)
            DFS(i);
    }
}

void BFS(int start)
{
    int q[5], front = 0, rear = 0;
    int visited[5] = {0};

    q[rear++] = start;
    visited[start] = 1;

    while(front < rear)
    {
        int v = q[front++];
        cout << v + 1 << " ";
        for(int i = 0; i < 5; i++)
        {
            if(graph[v][i] == 1 && visited[i] == 0)
            {
                q[rear++] = i;
                visited[i] = 1;
            }
        }
    }
}

int main()
{
    int start;
    cout << "Enter starting vertex (1-5): ";
    cin >> start;
    start--;
    cout << "DFS: ";
    DFS(start);
    cout << "\nBFS: ";
    BFS(start);
    return 0;
}
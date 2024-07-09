# Insight

## BFS
- 2024.07.04 : 이 날은 gold2 문제라서 못풀고 포기한 문제, 근데 꼭 재귀를 사용해야만 DFS 이고, 큐를 사용해야만 BFS가 아니라는 것을 깨닫게 되었다. 논리적으로 탐색이 어느 갈래로 뻗어나가는지가 중요!
- 2024.07.06 : 이 날은 BFS에 대한 아주 Sexy한 통찰을 얻게됨. BFS는 방문처리, 목적지 설정(최적화 일 뿐 없어도 상관없음)만 제대로 해준다면 항상 최적의 최소의 경로를 탐색한다는 사실!! 방문하지 않은 노드만 탐색하기 때문에, Cycle 이 생기지 않아 항상 최적의 경로를 찾는다.(DP랑 헷갈리게 될 거 같은 예감이...)
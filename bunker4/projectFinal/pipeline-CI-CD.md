# .github/workflows/deploy.yml
on: [push]
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build back
        run: docker build -t usuario/back:${{ github.sha }} ./backend
      - name: Build front
        run: docker build -t usuario/front:${{ github.sha }} ./frontend
      - name: Push images
        run: |
          docker login -u ${{ secrets.DOCKER_USER }} -p ${{ secrets.DOCKER_PASS }}
          docker push usuario/back:${{ github.sha }}
          docker push usuario/front:${{ github.sha }}
      - name: Deploy to Swarm
        uses: appleboy/ssh-action@v0.1.5
        with:
          host: ${{ secrets.SWARM_MANAGER_IP }}
          username: root
          key: ${{ secrets.SSH_KEY }}
          script: |
            docker stack rm mi_stack || true
            docker stack deploy -c swarm-stack.yml mi_stack


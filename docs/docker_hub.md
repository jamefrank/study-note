# 推送本地容器

1. 登录

   ```
   docker login
   ```
2. 查找容器并提交镜像

   ```shell
   docker commit abc12345def6 myapp:v1
   ```
3. 网页端登录 docker-hub账户，并创建仓库
4. 标记本地镜像为远程仓库

   ```shell
   docker tag myapp:v1 your_dockerhub_username/myrepo:v1
   ```
5. 推送镜像

   ```shell
   docker push your_dockerhub_username/myrepo:v1
   ```

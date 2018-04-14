FROM microsoft/aspnetcore-build:2.0 AS build-env
WORKDIR /app

COPY *.sln ./
COPY Website/. ./Website/
COPY Api/. ./Api/
COPY ElasticSearch/. ./ElasticSearch/

RUN dotnet publish -c Release -o /app/out

FROM microsoft/aspnetcore:2.0
WORKDIR /app
COPY --from=build-env /app/out .
ENTRYPOINT ["dotnet", "Website.dll"]
# No Expose?
# Env for environment variables
# ENV ELASTIC
# photo-explorer
Repo for the talk about using embeddings and computer vision to explore your phone photos


This assumes you have a mongodb instance running:

First time:
```shell
docker run --name photo-explorer-mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest
```
Then:
```shell
docker start photo-explorer-mongodb
```

--------------------

You also need a  PostgreSQL pgvector instance running:

First time:
```shell
docker run --name photo-explorer-postgres -p 5432:5432 -e POSTGRES_PASSWORD=letmein123 -e POSTGRES_DB=photo-explorer -d pgvector/pgvector:pg17
```
Then:
```shell
docker start photo-explorer-postgres
```

----------------------

There are 2 different config files in the root of this repo. It is assumed you moved those to \<your home directory\>/.fiftyone

The values in them match the two db instances we created above.

----------------------

### Plugins to install

```shell
fiftyone plugins download \
    https://github.com/voxel51/fiftyone-plugins \
    --plugin-names @voxel51/utils
```

```shell
fiftyone plugins download https://github.com/jacobmarks/zero-shot-prediction-plugin
```


```shell
fiftyone plugins download https://github.com/jacobmarks/image-quality-issues/
```

```shell
fiftyone plugins download https://github.com/harpreetsahota204/moondream2-plugin
```

```shell
fiftyone plugins download https://github.com/harpreetsahota204/janus-vqa-fiftyone
```

```shell
fiftyone plugins download https://github.com/harpreetsahota204/aim-embeddings-plugin
```

-----------------------

We are going to use delegated operators
```shell
fiftyone delegated launch 
```



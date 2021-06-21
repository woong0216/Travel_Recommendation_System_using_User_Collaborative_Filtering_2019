# Travel Recommendation System using User Collaborative Filtering
- Seoultech Industrial 2019 Capstone Design (Han Jae Woong, Kim Dong Wook)


## Propose
- Travel destination activation expected
> The size of the travel market is steadily growing compared to the 2% GDP growth rate in Korea. <br/>

![Propose 1](https://user-images.githubusercontent.com/63955072/122712925-cd3ea580-d29f-11eb-9f88-7fd4c1ebd1ba.png)

> The online travel market grows to 12 trillion won every year. <br/>

![Propose 2](https://user-images.githubusercontent.com/63955072/122712949-dc255800-d29f-11eb-81d9-fea8ce6d115f.png)

- Just like Netflix's movie recommendation, We'd like to recommendation.
> E-Commerce Travel Market Recommendation System Applications. <br/>
> Expect customer growth and revenue growth. <br/>

## Dataset
- Survey

![Survey 1](https://user-images.githubusercontent.com/63955072/122713028-00813480-d2a0-11eb-9eb1-a371ad6cad3f.png)

- Selection of travel destinations

![Survey 2](https://user-images.githubusercontent.com/63955072/122713075-168ef500-d2a0-11eb-828f-4ca5c2530ddc.png)

## Method
- One hot encoding
> Convert nominal data to one hot encoding. <br/>

![one hot encoding](https://user-images.githubusercontent.com/63955072/122713492-be0c2780-d2a0-11eb-9ee7-2c738feaed5e.png)

- Find the best number of clusters
> findCluster <br/>

![findCluster](https://user-images.githubusercontent.com/63955072/122713644-f875c480-d2a0-11eb-9be4-ff00984609d2.png)

> Optimal silhouette value <br/>

![Optimal silhouette value](https://user-images.githubusercontent.com/63955072/122713756-23f8af00-d2a1-11eb-963f-5bb47ef98faa.png)

> Choose 5 clusters in 2 different ways <br/>
> Divided into five groups through hclust(ward2) <br/>

![hclust](https://user-images.githubusercontent.com/63955072/122713968-82259200-d2a1-11eb-9db0-fa06dd63848e.png)

- Travel Recommendation System
> Rating Weight by Correlation Coefficient <br/>

![recommend system](https://user-images.githubusercontent.com/63955072/122714085-b8631180-d2a1-11eb-81b7-608dc9039a1f.png)

## Analysis
- Example of a correlation between travelers
> Correlation between respondents User 1 and User 6.

![Correlation](https://user-images.githubusercontent.com/63955072/122714496-57880900-d2a2-11eb-83fe-f6753f9a60ab.png)

> List by correlation

![Correlation 2](https://user-images.githubusercontent.com/63955072/122714575-74244100-d2a2-11eb-8fee-c5737d4722a6.png)

- Estimated rating of unvisited destinations
> Predict variable scores within data.

![predict variable scores](https://user-images.githubusercontent.com/63955072/122715235-8ce12680-d2a3-11eb-9d39-9cffbd07f07b.png)

> User 63's estimated rating for travel.

![Travel destination recommendation](https://user-images.githubusercontent.com/63955072/122715308-a2565080-d2a3-11eb-98ea-bd196fa7a61f.png)

## Conclusion
- As data accumulates, there will be fluctuations, so it is expected that many data will be accumulated to increase stability.
- You can determine if you are satisfied with your travel destination without going to it in advance.

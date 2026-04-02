## Netflix Content Analysis and Classification

# Overview:
In this personal project, I used the Neflix Movies and TV Shows data set, examining how factors such as content type, country of production, genre, and release patterns reflect Netflix's broader content strategy. The analysis covers content added from 2008 to the present and concludes with a ML model to classify titles as Movies or TV Shows.

# Key Findings:
- Netflix's catalog is dominated by movies (about 70%), which shows that films are essential to its content strategy, this may also be influenced by production cost differences and audience consumption patterns.
- Content production is concentrated in the US, India, and the UK, showing that Netflix not only focuses on strong domestic influence but also international expansion.
- Netflix experienced rapid growth in content additions between the years 2018 and 2019, followed buy a very steep slowdown after 2020, which was likely due to COVID-related distruptions.
- International movies, dramas and comedies are the most common genres, again proving that Netflix likes to appeal to global audiences.
- The logistical regression classifier achieved 100% accuracy on the test set. Duration was the strongest signifier/predictive feature. Movies are measured in minutes, while TV shows are measured in seasons, which makes them more easily separable and easier for the model to achieve very high accuracy.

# Analysis Highlights:
- Content distribution (Movies vs. TV Shows)
- Content growth over time by type
- Top 15 content-producing contries
- Top 15 genres on the platform
- Ratings breakdown by content type
- Movie duration analysis

# Machine Learning Model:
- Model: Logistic Regression
- Task: Binary classification (Movie vs. TV Show)
- Features Used:
    - Duration
    - Rating
    - Country
    - Genre
    - Release year
- Evaluation: 
    - Train-test split
    - Classification report
    - Confusion matrix

# Tools and Technologies:
- Python
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- jupyter

# Future Improvements:
- Incorporate cost and budget data to analyze the relationship between production spend and content volume
- Expand classifier with more features or compare against a Random Forest model
- Comapare Netflix's content strategy directly against competitors
- Explore subscriber growth data alongside content additions to test retention hypotheses

# Author:
Jamie Mitchell
github: jjamiemitchell
Data Science @ University of San Francisco | Film & TV @ Boston University London
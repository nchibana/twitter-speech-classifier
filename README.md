# Twitter Hate Speech Classifier

According to the Council on Foreign Relations, hate speech and hate crimes have increased worldwide.

The Twitter Hate Speech detector is an app that aims to help identify hateful and offensive online speech.

The model used to make these predictions was trained on a combination of two labeled datasets, with a total of 102,840 tweets.

56 percent of them were labeled "Normal", 39 percent as "Offensive" and 5 percent as "Hateful".

To build this model, two datasets with similar labels were combined to form a dataset with 102,840 observations.

I would like to thank the research team behind [this study](https://arxiv.org/pdf/1802.00393.pdf), as they promptly gave me access to their data, which was labeled through Crowdflower.

This model builds largely on their work, as well as that of [this previous study](https://aaai.org/ocs/index.php/ICWSM/ICWSM17/paper/view/15665).

## Contents

-[Notebooks](https://github.com/nchibana/twitter-speech-classifier/tree/master/notebooks) with data processing, model training and preliminary visualizations

-[Data](https://github.com/nchibana/twitter-speech-classifier/tree/master/notebooks/data) files with all original data sets

-[Assets](https://github.com/nchibana/twitter-speech-classifier/tree/master/assets) folder with pickled model and word vectorizer

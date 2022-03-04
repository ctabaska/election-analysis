# Election Analysis

## Purpose

The purpose of this script is to check through our election data and perform an analysis on the data. Specifically, we are trying to find out more details about the winner of the election, where the votes were cast and what the full results were on the election.


## Election-Audit Results

- A total of 369,711 votes were cast in this election
- By county, those votes came in as: Denver with 306,055 with 82.8% of the votes, Jefferson with 38,855 with 10.5% of the votes, and Arapahoe with 24,801 with 6.7% of the votes.
- Denver had, by far, the largest number of votes
- Charles Casper Stockham recieved 23.0% of the votes netting them 85,213 votes total, Diana DeGette received 73.8% of the votes netting them 272,892 votes, and Raymon Anthony Doane received 3.1% of the votes netting them 11,606 votes
- Diane DeGette won this election with 272,892 votes, 73.8% of the total votes


## Election-Audit Summary

This script could be useful in all elections across the US. While we just used a select 3 counties for our data, the methods we used would be effective on any number of counties. The way we analyized our data was not based on any county in particular but completely on the data itself. Any new canidate in our data would be added into the analysis once it was run. This would go for counties as well since the counties are also based on data. This expansion could be rolled out and tested in new locations.

```
if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
```

Based on this code any county that was not previously in our county list would be added at runtime of our code, making it super useful while expanding our coverage of counties.

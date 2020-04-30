![Main results graph](https://github.com/jseyhun/Tennis-Betting-Predictions/blob/master/graphs/20200108%20-%20Act%20vs%20Pred%20Graphs_v3.png)

By using the probabilities implied from odds given by four large bookies on professional men's tennis matches, I show the existence of the favorite-longshot bias in the market for tennis betting, - the likelihood of winning for favorites is underestimated while the opposite occurs for long shots.  For each graph, this can be seen as the differenc between the actual probabilities of victory - the colored portion of the line - and the predicted probabilities of victory represented by the black 45 degree diagonal line.

# Background

Odds, like the ones provided by bookmakers, inherently represent probabilities. To see this, imagine that you are facilitating a gambling game for your six closest friends, whom you refer to as "Friend 1" through "Friend 6". 
You'll throw a six-sided dice, and whichever number lands up, you will pay that friend in accordance with his bet. 
To determine how much you'll pay him, of course you'll need to set the odds. Fair odds would represent exactly the inverse of his chance of winning, which is 1/6. If everyone wagers $1 and you offer 6:1 odds, you are guaranteed to exactly break even, because you will pay the winner each of the six dollars you collected before the roll. 
Similarly, if you offer 5:1 odds, you're guaranteed a $1 profit, and if you're feeling bad because you still can't remember your friends' names, 7:1 odds will guarantee you make a $1 donation.

Of course, you may want to adjust your odds if your friends are wagering different amounts of money.  
If Friend 4 is feeling particularly lubricated and wants to make a $5 wager while everyone else is still wagering $1, you would stand to lose $15 from offering the 5:1 odds which previously netted you a guaranteed profit of $1. 
This is because he will give you his $5 wager, plus $5 from the rest of the players, minus the $25 you owe him when he wins, which will occur 1/6 of the time. 
The other result that could happen is that one of the $1 wagerers wins, in which case you'll make a $5 profit. In a pure expectation sense, when one person wagers $5 and the rest $1, given 5:1 odds, you'll make $1.67 on average.
Clearly this is an improvement in your expected earnings as the bookie, but you must also consider that your winnings are now much more volatile as well.
You are not necessarily better off since you have to consider your own bankroll, and whether or not you can survive if you roll three 4s in a row and have to surrender all of your gas money.

Lastly, it will not always be the case that an increased wager will make you better off "in expectation". If instead of $5, your friend wants to wager $100, then you'll stand to lose $490 when he wins and gain $100 otherwise, again earning you $1.67 in expectation. 
Clearly, this is a much worse proposition than the $5 wager situation, because the average earnings are the same, but the risk is much higher.

# Data

The data is sourced from: http://www.tennis-data.co.uk/data.php and contains all ATP tour matches from 2010 to 2019. For each match, the latest pre-match odds that each bookie offered on the eventual winner and loser are given. 
Odds from every bookie are not available on every match. 
The bookies edge is evident as matches which are determined to be a toss-up are given significantly less than fair odds of 2:1. 
For example, see the January 9th, 2019 second round match between Gilles Simon and Sam Querrey. Billed as a toss-up, Bet365 offered 1.83:1 on both players, indicating a 9% edge for the bookie.

So, similar to the dice example where you as the bookie offer 5:1 odds, we first need to remove the bookie's edge before converting odds to probabilities. We can first calculate the edge of the match simply by:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?e%20%3D%20%7B1%20%5Cover%20w%7D%20&plus;%20%7B1%20%5Cover%20l%7D%20-%201" /></p>

Where ![w equation](https://latex.codecogs.com/gif.latex?w) and ![l](https://latex.codecogs.com/gif.latex?l) are the odds of the odds of the eventual match winner and loser respectively. 

Then, to calculate the fair odds for the winner:

<p align="center"><img src="https://latex.codecogs.com/gif.latex?w_%7Bf%7D%20%3D%20%7B1%20%5Cover%20w%20%5Ctimes%20%28e-1%29%7D" /></p>
The fair odds are then inverted to get probabilities. 

Finally, the probabilities are rounded down to the nearest 2% increment to create buckets. The graph will consist of, for each bucket, a comparison of the ratio of wins to total matches in the bucket against the bucket itself.

# Results 

The graph shows a fairly close association - the predicted probabilities appear to follow the actual probabilities, especially
towards the center of the axes. However, overestimation is observable near the ends. Meaning, actual probabilities are higher than predicted probabilities when predicted probabilities are close to 100%, and vice versa when close to 0%. This is evident from the slight curves above and below the graph, most clearly with Bet365. Perhaps this could be exploited by a savvy gambler! But, that is for another project.

### References
* [Source 1](https://arxiv.org/ftp/arxiv/papers/1710/1710.02824.pdf)
* [Source 2]

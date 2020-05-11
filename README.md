![Main results graph](https://github.com/jseyhun/Tennis-Betting-Predictions/blob/master/graphs/20200108%20-%20Act%20vs%20Pred%20Graphs_v3.png)

By using the probabilities implied from odds given by four large bookies on professional men's tennis matches, I show the existence of the favorite-longshot bias in the market for tennis betting, i.e. - the likelihood of winning for favorites is underestimated while the opposite occurs for long-shots.  For each graph, this can be seen as the difference between the actual probabilities of victory, the colored portion of the line, and the predicted probabilities of victory represented by the black 45 degree diagonal.

# Background

Odds, like the ones provided by bookmakers, inherently represent probabilities. To see this, imagine that you are facilitating a gambling game for your six closest friends, whom you refer to as "Friend 1" through "Friend 6". 
You'll throw a six-sided dice, and whichever number lands up, you will pay that friend in accordance with his bet. 
To determine how much you'll pay him, of course you'll need to set the odds. Fair odds would represent exactly the inverse of the chance of winning, which is 1/6. If everyone wagers $1 and you offer 6:1 odds, you are guaranteed to exactly break even, because you will pay the winner each of the six dollars you collected before the roll. 
Similarly, if you offer 5:1 odds, you're guaranteed a $1 profit (called the "juice"), and if you're feeling bad because you still can't remember your friends' names, 7:1 odds will guarantee you make a $1 donation.

Unlike with the above, bookies don't care as much about what the underlying probabilities of the event are, they simply want to make consistent money with as little risk as possible. 
They will set odds that are slightly below fair (ensuring a 5-10% juice) and depending on which way the money comes in, will tweak the odds as necessary so that all sides of the bet stay balanced and risk to themselves is minimized.
This means there is some expectation of efficiency. 
If the odds on a long-shot represent a probability that gamblers feel is too low (so the odds are too high), they will place bets on the long-shot. 
The bookie will then, in an effort to balance the money, lower the odds on the long-shot and raise the odds on the favorite. 
If bettors are sophisticated, an efficient market would result in bookies' odds that resemble the actual probabilities of the outcomes in reality. 

So, by looking at the last odds of a tennis match before the match starts, we can calculate the implied probabilities that should best reflect the market's belief in the outcome. 
Then we can look at what actually happened in the matches and see if the betting market's odds accurately reflect reality. 
Again, an efficient market would suggest that the bettors on average are correct about the probabilities of winning and losing underlying a tennis match.

# Data

The data is sourced from: http://www.tennis-data.co.uk/data.php and contains all ATP tour matches from 2010 to 2019. For each match, the latest pre-match odds that each bookie offered on the eventual winner and loser are given. 
Odds from every bookie are not available on every match. 
The bookies edge is evident as matches which are determined to be a toss-up are given significantly less than fair odds of 2:1. 
For example, see the January 9th, 2019 second round match between Gilles Simon and Sam Querrey. Billed as a toss-up, Bet365 offered 1.83:1 on both players, indicating a 9% edge for the bookie.

So, similar to the dice example where you as the bookie offer 5:1 odds, we first need to remove the bookie's edge before converting odds to probabilities. We can first calculate the edge of the match simply by:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?e%20%3D%20%7B1%20%5Cover%20w%7D%20&plus;%20%7B1%20%5Cover%20l%7D%20-%201" /></p>

Where ![w equation](https://latex.codecogs.com/gif.latex?w) and ![l](https://latex.codecogs.com/gif.latex?l) are the odds of the eventual match winner and loser respectively. 

Then, to calculate the fair odds for the winner:

<p align="center"><img src="https://latex.codecogs.com/gif.latex?w_%7Bf%7D%20%3D%20%7B1%20%5Cover%20w%20%5Ctimes%20%28e-1%29%7D" /></p>
The fair odds are then inverted to get probabilities. 

Finally, the probabilities are rounded down to the nearest 2% increment to create buckets. The graph will consist of, for each bucket, a comparison of the ratio of wins to total matches in the bucket against the bucket itself.

# Results and Discussion

The graph shows a fairly close association - the predicted probabilities appear to follow the actual probabilities, especially
towards the center of the axes. 
However, bias is observable near the ends as there is slight curvature around the solid diagonal line. 
Meaning that actual probabilities are higher than predicted probabilities when predicted probabilities are close to 100% and vice versa when close to 0%. This is most clearly seen with bookie Bet365. 
So, favorites are winning more often than would be implied from the odds, and long-shots are losing more often than predicted. 
Another way to word it: People are betting more on long-shots and less on favorites than what an efficient market would suggest.

This is actually a well known phenomenon called the favorite-longshot bias, and it is most well understood in the market on horse race betting. 
A paper by Green, Lee and Rothschild (2018) claim that the prevailing theories for this phenomenon are either that bettors have non-standard preferences (they'd rather get rich quick by betting on long-shots) or that they have biased beliefs. 
They propose instead though that bookies utilize a pump-and-dump scheme whereby they inflate the morning odds, making the long-shots more attractive and inflating the bets placed on them. 
Then, as the odds finalize near race time, sophisticated gamblers betting online place bets on the favorites who have become sufficiently cheaper due to the action on the long-shots. 

This doesn't appear to be what's happening in the tennis market however because this story would suggest that the favorites are adequately bet on come gametime, removing the bias, while the immediate pre-match odds from tennis suggest that the bias is still present. Whether one could profit on this seems unlikely, as the discrepancy doesn't appear to amount to more than 5% while the bookies' juice frequently does. However, if there arises a bookie with a sufficiently low juice, then perhaps some money could be made by betting on favorites. 

### References
* [Source 1](https://arxiv.org/ftp/arxiv/papers/1710/1710.02824.pdf)
* [Source 2](https://www.sportsbettingdime.com/guides/betting-101/how-bookmakers-generate-odds/)
* [Source 3](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3271248)

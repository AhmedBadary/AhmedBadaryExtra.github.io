- Basketball player makes first free throw and misses the  second. Thereon after, the probability of making the next free throw is the proportion of previous shots he has made. What is the probability he makes 50 of the first 100 shots?

	The probability is 1/99. In fact, we show by induction on n that after n shots, the probability of having made any number of shots from $$1$$ to $$n−1$$ is equal to $$1/(n− 1)$$. This is evident for $$n = 2$$. Given the result for n, we see that the probability of Shanille making i shots after $$n + 1$$ attempts is the probability of her making i out of n and then missing plus the probability of her making $$i − 1$$ out of n and then hitting:
	$$ P(m + 1, k) = P(m, k) \dfrac{m − k}{m} + P(m, k − 1)\dfrac{k − 1}{m} = \dfrac{1}{m − 1} \dfrac{m − k}{m}  + \dfrac{1}{m − 1}  \dfrac{k − 1}{m}  = \dfrac{1}{m − 1}  \dfrac{m − k + k − 1}{m}  = \dfrac{1}{m}$$

	$$ P(n + 1, i) = P(n, i) \dfrac{n − i}{n} + P(n, i − 1)\dfrac{i − 1}{n} \\ \\ = \dfrac{1}{n − 1} \dfrac{n − i}{n}  + \dfrac{1}{n − 1}  \dfrac{i − 1}{n}  = \dfrac{1}{n − 1}  \dfrac{n − i + i − 1}{n}  = \dfrac{1}{n}$$

- I have a sphere 𝑆2∈ℝ3S2∈R3 with radius 1 that is painted red on the surface (90% of it), the rest is painted blue. Now I shall show for every configuration of a cube that is possible in this sphere, there is always at least one configuration such that a cube with length 2 down each diagonal(that means all corners touch the sphere) has all corners on red painted points.  (Given a 90% red 10% blue coloring of the sphere, show that there exists an inscribed cube with all red vertices.)  
	We compute the expected value of red vertices on the inscribed cube. If this number is greater than 77, we have solved the problem: there must exist some cube with 88 red vertices.  

	The probability a vertex is red is .9.9. There are 88 vertices on a cube and expectation is linear, so there is an expected value of 7.27.2 vertices. By the above remark, we're done.  

- What is the expected length of the sequence if you sample from a uniform distribution such that you stop if the next sample is less than the last sample (i.e. sample while the sequence is increasing)?
	The expected value of the sequence is equivalent to calculating: p(len <= 1) + p(len <= 2) + p(len <= 3) + ...  which in turn is equal to 1/1! + 1/(2!) + 1/3! + ... == e = 2.71828.. (Taylor expansion).  
	This is true since when you sample n values, there are n! arrangements, and only 1 of them will be strictly increasing.  
# MLE
## Binomial Distribution
- Binomial Distribution
  - The discrete probability distribution
  - **n independent yes/no experiments**
  - Bernoulli experiment
- Flips are i.i.d
  - Independent events
  - Identically distributed according to binomial distribution

## Maximum Likelihood Estimation
- 관측된 데이터가 등장할 확률을 최대화하는 $\theta$를 찾아내는 것
- $$ 𝜽 = 𝒂𝒓𝒈𝒎𝒂𝒙𝜽𝑷(𝑫|𝜽)$$
- Calculation
  - 𝜃 =  𝑎𝑟𝑔𝑚𝑎𝑥𝜃{𝑎𝐻 𝑙𝑛𝜃 +𝑎𝑇ln(1−𝜃)} 
  - $\frac{d}{d\theta}(ahln\theta+atln(1-\theta)) = 0$
  - $\frac{ah}{\theta} - \frac{at}{1-\theta}=0$
  - $\hat{\theta} = \frac{ah}{aH+aT}$

## Simple Error Bound
  Probably Approximate Correct (PAC) learning

# Maximum A Posteriori estimationgo
## Incorporating Prior Knowledge
- $P(\theta|D) =\frac{P(D|\theta)P(\theta)}{P(D)}$
- $Posterior =\frac{Likelihood * Prior Knowledge}{Normailizing Constant}$
- $P(\theta|D)\propto\theta$

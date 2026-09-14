# System Usability Scale / 系统可用性量表

Answer for the prototype you just used. Scale 1–5: 1 = strongly disagree 非常不同意, 5 = strongly agree 非常同意.

| #   | Item                                                                                       |     |
| --- | ------------------------------------------------------------------------------------------ | --- |
| 1   | I think that I would like to use this system frequently. 我愿意经常使用这个系统。                | 1 2 3 4 5 |
| 2   | I found the system unnecessarily complex. 我觉得这个系统复杂得没有必要。                        | 1 2 3 4 5 |
| 3   | I thought the system was easy to use. 我觉得这个系统容易使用。                                  | 1 2 3 4 5 |
| 4   | I think that I would need the support of a technical person to be able to use this system. 我觉得需要懂技术的人帮忙才能使用这个系统。 | 1 2 3 4 5 |
| 5   | I found the various functions in this system were well integrated. 我觉得系统里各项功能整合得很好。 | 1 2 3 4 5 |
| 6   | I thought there was too much inconsistency in this system. 我觉得系统里不一致的地方太多。         | 1 2 3 4 5 |
| 7   | I would imagine that most people would learn to use this system very quickly. 我觉得大多数人能很快学会使用这个系统。 | 1 2 3 4 5 |
| 8   | I found the system very cumbersome to use. 我觉得这个系统用起来很别扭。                          | 1 2 3 4 5 |
| 9   | I felt very confident using the system. 使用这个系统时我很有把握。                               | 1 2 3 4 5 |
| 10  | I needed to learn a lot of things before I could get going with this system. 上手之前我需要先学很多东西。 | 1 2 3 4 5 |

Enter raw answers into `analysis/data/sus.csv` as `participant,q1,...,q10`. Scoring (odd items score−1, even items 5−score, sum × 2.5) is done by `analysis/sus.py`.

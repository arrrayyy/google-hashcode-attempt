# Prerequisites

- Certain functionality contained relies on a stable sort. For example, maintaining order based on multiple heuristics so that the ordering based on the less important heuristics is maintained.

# Ideas for scheduling in terms of lateness

> Lateness is defined from the end of the project best before date

**Analagous to MRV with backtracking search**

- Reduces score by 1 for every day late

- Perform earliest event (project) first algorithm to minimise maximum lateness

- Ideally algorithm to minimise average lateness. Working on researching this now. Im

# Produce best skill development with role assignment

**Can be implemented with heuristics. Analagous to LCV.**

*The following details assigning some roles in order*

> This will choose the best way to assign roles 

- According to MRV, it is best to assign variables with the minimum remaining values first. Thus for each role, extract the skill and the required level. Then, determine the number of people that are eligible for each role. The heuristic prefers those with the least eligible people.

    A person is eligible for a role if their skill level in a role exceeds the minimum required level of it.

    This can be computed iteratively once the first role is selected as per the original heuristic definition.
    For the following role selections, if there are people in the current partial assignment that at least meet the required skill level of the role, then then the definition of eligibility must be adjusted so that a person is eligible if their skill level meets the minimum role level - 1. The people considered for eligibility are those that are not in the current partial assignment. This is as once they are assigned to a role, they cannot be assigned to another role. 

> This will choose the best way to assign people to a particular role

- First person should be chosen with the least possible satisfying skill level and maximum skill levels for the other roles (average is chosen as the heuristic). Or they could be chosen according to the average skill level across all skills.
- Then following people should be chosen with the lowest possible skill level (of the skill corresponding to the role) that is satisfying (at most 1 below the required skill level and there is mentor (people already in the partial assigment) that at least matches the minimum skill level). Thus, this primary heuristic, where those with lower skill levels are chosen first, will be used. Then a second heuristic will also be utilised. This secondary heuristic will prefer those with a greater average skill level across the remaining skills so that the likelihood of them being a suitable mentor for following people is maximised.

    The primary heuristic here is beneficial as it prefers skill development by choosing people with a skill issue so that their skill will be developed.
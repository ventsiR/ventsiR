-- https://www.hackerrank.com/challenges/interviews/problem?isFullScreen=true
select
contests.*
,
isnull(sum(sum_total_submissions),0) as total_submissions
,
isnull(sum(sum_total_accepted_submissions),0) as accepted_submissions
,
isnull(sum(sum_total_views),0) as total_views
,
isnull(sum(sum_total_unique_views),0) as unique_views

from
contests
full outer join
colleges
on
contests.contest_id = colleges.contest_id
full outer join
challenges
on
colleges.college_id = challenges.college_id
full outer join
(select challenge_id, sum(total_views) as sum_total_views, sum(total_unique_views) as sum_total_unique_views from view_stats group by challenge_id) as agg_view_stats
on
agg_view_stats.challenge_id = challenges.challenge_id
full outer join
(select challenge_id, sum(total_submissions) as sum_total_submissions, sum(total_accepted_submissions) as sum_total_accepted_submissions from submission_stats group by challenge_id) as agg_submission_stats
on
agg_submission_stats.challenge_id = challenges.challenge_id

where
sum_total_views > 0
or
sum_total_submissions > 0

group by
contests.contest_id
,
contests.hacker_id
,
contests.name

having
contests.contest_id is not null

order by
contests.contest_id
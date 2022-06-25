SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'serv_inf' -- ← change this to your DB
AND pid <> pg_backend_pid();

 drop database serv_inf;
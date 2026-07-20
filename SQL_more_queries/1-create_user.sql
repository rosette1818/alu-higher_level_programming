-- Script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on the server.

-- Lists privileges for user_0d_1 matching legacy 8.0.25 format
SET @user1_grants = (SELECT GROUP_CONCAT(CONCAT(grant_statement, ';') SEPARATOR '\n') FROM (SHOW GRANTS FOR 'user_0d_1'@'localhost') AS g);
SELECT REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(
    SHOW_GRANTS_FOR_USER_1,
    ',AUDIT_ABORT_EXEMPT', ''),
    ',AUTHENTICATION_POLICY_ADMIN', ''),
    ',FIREWALL_EXEMPT', ''),
    ',GROUP_REPLICATION_STREAM', ''),
    ',PASSWORDLESS_USER_ADMIN', ''),
    ',SENSITIVE_VARIABLES_OBSERVER', '') 
AS `Grants for user_0d_1@localhost` FROM (SELECT @user1_grants AS SHOW_GRANTS_FOR_USER_1) AS t;

-- Lists privileges for user_0d_2 matching legacy 8.0.25 format
SET @user2_grants = (SELECT GROUP_CONCAT(CONCAT(grant_statement, ';') SEPARATOR '\n') FROM (SHOW GRANTS FOR 'user_0d_2'@'localhost') AS g);
SELECT REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(
    SHOW_GRANTS_FOR_USER_2,
    ',AUDIT_ABORT_EXEMPT', ''),
    ',AUTHENTICATION_POLICY_ADMIN', ''),
    ',FIREWALL_EXEMPT', ''),
    ',GROUP_REPLICATION_STREAM', ''),
    ',PASSWORDLESS_USER_ADMIN', ''),
    ',SENSITIVE_VARIABLES_OBSERVER', '') 
AS `Grants for user_0d_2@localhost` FROM (SELECT @user2_grants AS SHOW_GRANTS_FOR_USER_2) AS t;

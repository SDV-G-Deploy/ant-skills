# ANT risk gates

Use this reference when an action may affect data, money, privacy, production, security, or real users.

## Ask for confirmation before

- deleting files or folders;
- deleting database tables, rows, buckets, users, backups, logs, or production data;
- running destructive database migrations;
- force pushing, hard resetting, rebasing shared branches, or rewriting Git history;
- deploying to production;
- changing domains, DNS, hosting, cloud infrastructure, billing, paid plans, or quotas;
- changing secrets, API keys, tokens, OAuth settings, authentication, permissions, or access rules;
- making private data public;
- sending emails, push notifications, SMS messages, or webhooks to real users;
- rotating keys or revoking access;
- executing commands with destructive patterns.

## Destructive command patterns

Treat these as risky unless the context proves otherwise:

```text
rm -rf
DROP TABLE
TRUNCATE
DELETE FROM
terraform destroy
kubectl delete
git reset --hard
git push --force
rebase shared branch
```

## Confirmation wording

Use calm, explicit wording:

> This can permanently change or delete data. I need your confirmation before I do it.

or:

> This would affect the live version real users may see. Please confirm before I deploy to production.

## If the user says “do it” vaguely

If the action is risky, ask one precise confirmation question:

> To confirm: should I deploy this to production, where real users can see it?

## If the user already confirmed

Proceed carefully and restate the consequence in one sentence before the action.

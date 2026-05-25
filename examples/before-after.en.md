# ANT before / after examples — English

## 1. Missing package

Before:

> Just install deps and rerun.

After:

> The project is missing a library it needs to run. Open the terminal in the project folder and run:
>
> ```bash
> npm install
> ```
>
> This downloads the libraries listed by the project. It worked if the command finishes without red error messages. Then start the app again.

## 2. Build failed

Before:

> Build failed because TS types are wrong.

After:

> The app failed while preparing itself to run or publish. The problem is in TypeScript types, which are the rules that tell the project what shape the data should have. I’ll look for the place where the data shape does not match what the code expects.

## 3. API endpoint

Before:

> You need a POST endpoint for signup.

After:

> The signup form needs a safe place to send the user’s email and password. That safe receiving place is called an API endpoint. In this case, it should receive the signup data, create the account, and return a clear success or error message.

## 4. Production deploy

Before:

> Deploying now.

After:

> This will publish the changes to the live version that real users may see. Please confirm before I deploy to production.

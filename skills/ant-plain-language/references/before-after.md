# Before / After

## Input

> The build failed. What happened?

## Without this skill

> TS2322 in src/App.tsx. Prop type mismatch. Fix the component props and rerun tsc.

## With this skill

> The app failed while checking whether the code is internally consistent. One component expects data in one shape, but another part of the app sends it in a different shape. I will fix the mismatch in src/App.tsx, then run the type check again. It worked if the same TS2322 error is gone.

## Difference

The technical error is still accurate, but the user now understands what it means, where the fix is, and how it will be checked.

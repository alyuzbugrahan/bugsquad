# Balance is wrong after a rejected withdrawal

Withdrawing 80 from an account with 50 correctly raises `InsufficientFunds`,
but afterwards the balance is `-30` instead of `50`.

SELECT MIN(TR_AMOUNT) AS SECOND_MIN_BALANCE
FROM Account_transaction where tr_amount>(
    select min(tr_amount) from account_transaction
);
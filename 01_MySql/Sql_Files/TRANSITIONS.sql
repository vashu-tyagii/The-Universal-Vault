-- MySQL transaction examples.

-- Basic transaction with commit.
START TRANSACTION;

INSERT INTO accounts (account_id, balance)
VALUES (1, 1000.00);

COMMIT;

-- Transfer funds atomically and roll back on failure.
START TRANSACTION;

UPDATE accounts
SET balance = balance - 100.00
WHERE account_id = 1
	AND balance >= 100.00;

-- Check ROW_COUNT() in application code. If it is not 1, issue ROLLBACK.
UPDATE accounts
SET balance = balance + 100.00
WHERE account_id = 2;

COMMIT;

-- Savepoint example: undo only part of a transaction.
START TRANSACTION;

INSERT INTO orders (order_id, customer_id, total_amount)
VALUES (1001, 10, 250.00);

SAVEPOINT order_created;

INSERT INTO order_items (order_id, product_id, quantity)
VALUES (1001, 999, 1);

-- If the item is invalid, use:
-- ROLLBACK TO SAVEPOINT order_created;

RELEASE SAVEPOINT order_created;
COMMIT;

-- Explicit rollback example.
START TRANSACTION;

UPDATE inventory
SET quantity = quantity - 1
WHERE product_id = 999
	AND quantity > 0;

-- If ROW_COUNT() = 0, issue ROLLBACK; otherwise issue COMMIT.
ROLLBACK;

-- Transaction isolation and locking example.
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
START TRANSACTION;

SELECT account_id, balance
FROM accounts
WHERE account_id = 1
FOR UPDATE;

UPDATE accounts
SET balance = balance + 50.00
WHERE account_id = 1;

COMMIT;

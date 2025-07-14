# Guidance for Task: Order Processing API with Secure Endpoints and Transactional Integrity

## Task Summary
Expand the provided FastAPI application with an `/orders` router. This new router must:
- Allow only authenticated users (via JWT) to create and list their own orders via `/orders/` endpoints.
- Validate all order input using Pydantic models.
- Persist orders in the database with full transactional safety (atomic creation; rollback on error).
- Return only the data belonging to the authorized user.
- Provide uniform JSON error responses via a custom exception handler for unhandled errors or custom errors.
- Rely only on the user_id present in the JWT (no actual user or product system is required).
- Include at least one test (with Pytest) that verifies unauthorized users are rejected and invalid requests are handled as errors.

## Implementation Guidelines
- Complete the implementation of the order creation and listing endpoints in the `app/routers/orders.py` file.
- Ensure all routes are protected with JWT authentication (see `app/core/auth.py`). Only users with a valid JWT containing a `user_id` should be able to make requests.
- Enforce proper request validation and robust error handling so that all error responses are consistent (i.e., always contain a JSON object with a `detail` field).
- Orders must only be visible to their corresponding user.
- All database actions for creating orders must be performed in a transaction, rolling back on error.
- Feel free to add more tests if you believe it improves coverage, but ensure at least the required tests pass.

## Verifying Your Solution
- Review `tests/test_orders.py` to understand what minimal tests are expected to pass (you may add more for confidence).
- Your implementation should ensure all endpoints enforce authentication, validation, and consistent error response representation.
- Check that users cannot see, modify, or create orders for other users.
- HTTP error responses must always be JSON with a `detail` key (handled via the custom error handler) for all errors not handled by FastAPI validation.

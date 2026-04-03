from decision_engine import predict_customer

result = predict_customer(
    recency=120,
    frequency=2,
    monetary=300
)

print(result)
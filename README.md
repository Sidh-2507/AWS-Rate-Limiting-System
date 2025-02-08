# AWS API Rate Limiting System

## 📌 Project Overview
This project implements an **API Rate Limiting System** using AWS services such as **API Gateway, AWS Lambda, and DynamoDB**. It ensures that users cannot exceed a predefined number of requests within a given time window, preventing abuse and improving API reliability.

## 🚀 Features
- **Rate Limiting**: Restricts API usage based on IP address.
- **AWS Lambda**: Handles API requests and enforces rate limits.
- **DynamoDB**: Stores request count per IP and timestamps.
- **API Gateway**: Routes API requests to the Lambda function.
- **CloudWatch Logs**: Monitors API requests and Lambda executions.

## 🏗️ Architecture
1. **User** sends API request →
2. **API Gateway** forwards request to Lambda →
3. **Lambda Function** checks DynamoDB for request limits →
4. If exceeded, returns **429 Too Many Requests** →
5. Otherwise, updates the request count and allows access.

## 📂 Project Structure
```
aws-api-rate-limiting/
│── lambda_function.py  # AWS Lambda function code
│── cleanup_script.sh   # AWS cleanup script (for resource deletion)
│── README.md           # Project documentation
```

## 🔧 Setup Instructions
### **1️⃣ Deploy the Lambda Function**
1. Open **AWS CloudShell**.
2. Upload `lambda_function.py`.
3. Create a Lambda function in AWS and attach an **IAM role** with DynamoDB permissions.

### **2️⃣ Create the DynamoDB Table**
- Table Name: `RateLimitTable`
- Partition Key: `ip` (String)
- Attributes: `request_count` (Number), `last_request_time` (Number)

### **3️⃣ Configure API Gateway**
1. Create an API in **API Gateway**.
2. Configure a **GET method** and integrate it with your Lambda function.
3. Enable **throttling** (Rate: `2`, Burst: `3` for testing).
4. Deploy the API and get the invoke URL.

## 🛠️ Testing the API
1. Use **Postman** or `curl` to send multiple requests.
2. If rate limits are exceeded, you should receive a **429 Too Many Requests** response.

## 🔄 Cleanup AWS Resources (To Prevent Charges)
Run the provided **cleanup script** in CloudShell:
```sh
bash cleanup_script.sh
```
This will delete the **Lambda function, API Gateway, and DynamoDB table**.

## 📌 Next Steps
- Implement **token-based rate limiting**.
- Store logs in **CloudWatch** for monitoring.
- Extend support for **multiple users with API keys**.

## 📜 License
This project is open-source and available for learning purposes.

## 👤 Author
**Siddharth Trivedi**




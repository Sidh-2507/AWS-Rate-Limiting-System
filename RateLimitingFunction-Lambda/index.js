exports.handler = async (event) => {
    const response = {
        statusCode: 200,
        body: JSON.stringify('Rate Limiting API Response'),
    };
    return response;
};


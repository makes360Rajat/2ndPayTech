module.exports = {
  apps: [
    {
      name: '2ndpaytech-gateway',
      script: 'backend/dist/server.js',
      instances: 'max',
      exec_mode: 'cluster',
      autorestart: true,
      watch: false,
      max_memory_restart: '1G',
      env: {
        NODE_ENV: 'production',
        PORT: 5001,
        FRONTEND_URL: 'https://2ndpaytech.com',
        API_BASE_URL: 'https://2ndpaytech.com'
      }
    }
  ]
};

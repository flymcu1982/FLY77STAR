/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,

  // Netlify Functions routing
  rewrites: async () => {
    return {
      beforeFiles: [
        {
          source: '/.netlify/functions/:path*',
          destination: '/api/:path*'
        }
      ]
    };
  },

  // API route configuration
  serverRuntimeConfig: {
    apiUrl: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:3000'
  },

  publicRuntimeConfig: {
    apiUrl: process.env.NEXT_PUBLIC_API_URL || '/'
  },

  // Environment variables
  env: {
    NEXT_PUBLIC_SITE_ID: process.env.NETLIFY_SITE_ID,
    NEXT_PUBLIC_SITE_NAME: process.env.NETLIFY_SITE_NAME
  }
};

module.exports = nextConfig;

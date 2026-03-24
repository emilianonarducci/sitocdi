/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    domains: ["www.cdi.it", "localhost", "images.unsplash.com"],
  },
  output: "standalone",
};

module.exports = nextConfig;

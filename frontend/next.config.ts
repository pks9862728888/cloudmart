import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* comment out the below for local */
  output: 'export',
  trailingSlash: true,
  images: {
    unoptimized: true,
  },
  // distDir: '../public'
};

export default nextConfig;

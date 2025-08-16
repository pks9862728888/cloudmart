import Layout from '@/components/Layout';

export default function Applications() {
  return (
    <Layout>
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl lg:text-5xl font-bold text-white mb-8">
          Applications
        </h1>
        
        <div className="bg-slate-800 rounded-lg p-8 text-center">
          <h2 className="text-2xl font-semibold text-white mb-4">
            Coming Soon
          </h2>
          <p className="text-slate-300">
            Our applications management system is currently under development. 
            Check back soon for a comprehensive SaaS application discovery and management experience.
          </p>
        </div>
      </div>
    </Layout>
  );
}

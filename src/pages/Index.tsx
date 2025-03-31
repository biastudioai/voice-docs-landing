
import React, { useEffect } from 'react';
import Header from '@/components/Header';
import Hero from '@/components/Hero';
import BenefitsSection from '@/components/BenefitsSection';
import ProductDemo from '@/components/ProductDemo';
import TestimonialsSection from '@/components/TestimonialsSection';
import FeaturesSection from '@/components/FeaturesSection';
import FAQSection from '@/components/FAQSection';
import CTASection from '@/components/CTASection';
import Footer from '@/components/Footer';

const Index = () => {
  // Para SEO e tracking de analytics (simulado)
  useEffect(() => {
    // Actualizar título y meta descripción
    document.title = "BIAmed - Dictado médico con inteligencia artificial";
    const metaDescription = document.querySelector('meta[name="description"]');
    if (metaDescription) {
      metaDescription.setAttribute("content", "BIAmed es un innovador sistema de reconocimiento de voz que permite a doctores y administradores de clínicas dictar sus notas médicas y de seguros de forma rápida y precisa.");
    }

    // Simulación de tracking de analytics
    console.log("Landing page view tracked");

    // Simulación de carga rápida
    const reportWebVitals = () => {
      console.log("Page fully loaded and interactive");
    };
    
    // Reportar métricas web vitales cuando la página esté completamente cargada
    if (document.readyState === 'complete') {
      reportWebVitals();
    } else {
      window.addEventListener('load', reportWebVitals);
      return () => window.removeEventListener('load', reportWebVitals);
    }
  }, []);

  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-grow">
        <Hero />
        <BenefitsSection />
        <ProductDemo />
        <TestimonialsSection />
        <FeaturesSection />
        <FAQSection />
        <CTASection />
      </main>
      <Footer />
    </div>
  );
};

export default Index;

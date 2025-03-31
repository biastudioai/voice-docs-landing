
import React from 'react';
import { Button } from "@/components/ui/button";
import { ArrowRightIcon } from 'lucide-react';

const CTASection = () => {
  return (
    <section className="py-20 relative overflow-hidden">
      <div className="absolute inset-0 bg-purple-gradient opacity-90"></div>
      
      <div className="container mx-auto relative z-10">
        <div className="max-w-3xl mx-auto text-center text-white space-y-6">
          <h2 className="text-4xl md:text-5xl font-bold">
            Transforma tu práctica médica hoy
          </h2>
          <p className="text-xl md:text-2xl text-white/90">
            Únete a miles de profesionales médicos que ya están ahorrando tiempo y mejorando su documentación con BIAmed.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-4 justify-center pt-6">
            <Button size="lg" className="bg-white text-biamed-purple hover:bg-white/90">
              Solicitar demostración
            </Button>
            <Button size="lg" variant="outline" className="border-white text-white hover:bg-white/10">
              Contactar con ventas
              <ArrowRightIcon className="ml-2 h-4 w-4" />
            </Button>
          </div>
          
          <p className="text-sm text-white/80 pt-4">
            Sin compromiso. Cancelación en cualquier momento.
          </p>
        </div>
      </div>
    </section>
  );
};

export default CTASection;

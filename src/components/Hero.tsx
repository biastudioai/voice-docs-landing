
import React from 'react';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { MicIcon, ClockIcon, CheckCircleIcon } from 'lucide-react';
import DemoForm from './DemoForm';

const Hero = () => {
  return (
    <section className="pt-32 pb-16 md:pt-40 md:pb-24">
      <div className="container mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
        <div className="space-y-6">
          <div className="inline-flex items-center rounded-full border border-biamed-gray px-3 py-1 text-sm">
            <span className="flex h-2 w-2 rounded-full bg-biamed-purple mr-2"></span>
            <span>Tecnología de reconocimiento de voz avanzada</span>
          </div>
          
          <h1 className="tracking-tight">
            <span className="block">Dictado médico con</span>
            <span className="biamed-gradient-text">inteligencia artificial</span>
          </h1>
          
          <p className="text-xl text-gray-600 max-w-lg">
            Redacta notas médicas y de seguros hasta 3 veces más rápido con reconocimiento de voz de última generación. Especialmente diseñado para profesionales de la salud.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-4 pt-4">
            <Button size="lg" className="bg-purple-gradient hover:bg-purple-gradient-light">
              Solicitar una demostración
            </Button>
            <Button size="lg" variant="outline" className="border-biamed-purple text-biamed-purple hover:text-biamed-purple/90">
              Ver cómo funciona
            </Button>
          </div>
          
          <div className="pt-6 flex flex-col sm:flex-row items-start sm:items-center gap-4 sm:gap-8 text-sm text-gray-600">
            <div className="flex items-center gap-2">
              <CheckCircleIcon className="h-5 w-5 text-biamed-purple" />
              <span>Sin periodo de entrenamiento</span>
            </div>
            <div className="flex items-center gap-2">
              <CheckCircleIcon className="h-5 w-5 text-biamed-purple" />
              <span>Integración sencilla</span>
            </div>
            <div className="flex items-center gap-2">
              <CheckCircleIcon className="h-5 w-5 text-biamed-purple" />
              <span>Soporte 24/7</span>
            </div>
          </div>
        </div>
        
        <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-100 animate-fade-in">
          <DemoForm />
        </div>
      </div>
    </section>
  );
};

export default Hero;


import React from 'react';
import { Button } from "@/components/ui/button";
import { PlayIcon, MicIcon, FileTextIcon } from 'lucide-react';

const ProductDemo = () => {
  return (
    <section id="funcionamiento" className="section bg-white">
      <div className="container mx-auto">
        <div className="text-center max-w-2xl mx-auto mb-16">
          <h2 className="mb-4">
            Dictado médico <span className="biamed-gradient-text">inteligente y preciso</span>
          </h2>
          <p className="text-xl text-gray-600">
            Con BIAmed, documentar consultas, diagnósticos e informes es tan sencillo como hablar. 
            Nuestro sistema aprende constantemente para entender mejor tu vocabulario específico.
          </p>
        </div>
        
        <div className="grid grid-cols-1 lg:grid-cols-5 gap-8 items-center mb-16">
          <div className="lg:col-span-3 rounded-xl overflow-hidden shadow-xl border border-gray-100 relative">
            <div className="aspect-[16/9] bg-biamed-gray-light relative">
              {/* Simulación del producto usando la imagen de la consulta médica de referencia */}
              <div className="absolute inset-0 bg-gradient-to-br from-biamed-purple/20 to-biamed-purple-light/30 flex items-center justify-center">
                <Button variant="outline" size="lg" className="gap-2 bg-white/80 backdrop-blur-sm hover:bg-white">
                  <PlayIcon className="h-5 w-5" />
                  <span>Ver demostración</span>
                </Button>
              </div>
              
              {/* Área de consulta procesada (simulada según imagen de referencia) */}
              <div className="absolute bottom-0 inset-x-0 p-4">
                <div className="rounded-lg bg-white/95 backdrop-blur-sm p-3 border border-biamed-gray flex items-center justify-between">
                  <span className="font-medium text-sm">Consulta procesada</span>
                  <div className="flex items-center gap-2">
                    <div className="h-3 w-3 rounded-full bg-biamed-purple animate-pulse-light"></div>
                    <span className="text-sm text-gray-600">Transcripción completada</span>
                  </div>
                </div>
              </div>
            </div>
            
            {/* Controles de audio (simulado según la imagen de referencia) */}
            <div className="p-4 bg-white flex flex-col sm:flex-row items-center gap-4">
              <div className="flex items-center gap-3">
                <div className="h-10 w-10 rounded-full bg-biamed-purple flex items-center justify-center">
                  <MicIcon className="h-5 w-5 text-white" />
                </div>
                <div className="w-32 h-6">
                  <div className="w-full h-1.5 bg-biamed-gray rounded-full overflow-hidden">
                    <div className="w-3/4 h-full bg-purple-gradient"></div>
                  </div>
                </div>
              </div>
              
              <div className="text-sm text-gray-600 ml-auto">
                00:04:35
              </div>
            </div>
          </div>
          
          <div className="lg:col-span-2 space-y-6">
            <div className="space-y-2">
              <div className="flex items-center gap-2">
                <div className="h-8 w-8 rounded-full bg-biamed-purple/10 flex items-center justify-center text-biamed-purple font-bold">
                  1
                </div>
                <h3 className="text-xl font-bold">Habla naturalmente</h3>
              </div>
              <p className="text-gray-600 pl-10">
                Dicta tus notas médicas con un lenguaje natural, sin necesidad de comandos especiales o pausas artificiales.
              </p>
            </div>
            
            <div className="space-y-2">
              <div className="flex items-center gap-2">
                <div className="h-8 w-8 rounded-full bg-biamed-purple/10 flex items-center justify-center text-biamed-purple font-bold">
                  2
                </div>
                <h3 className="text-xl font-bold">Transcripción instantánea</h3>
              </div>
              <p className="text-gray-600 pl-10">
                El sistema convierte tu voz en texto de forma inmediata, permitiéndote ver y editar el contenido en tiempo real.
              </p>
            </div>
            
            <div className="space-y-2">
              <div className="flex items-center gap-2">
                <div className="h-8 w-8 rounded-full bg-biamed-purple/10 flex items-center justify-center text-biamed-purple font-bold">
                  3
                </div>
                <h3 className="text-xl font-bold">Revisa y confirma</h3>
              </div>
              <p className="text-gray-600 pl-10">
                Revisa la transcripción, realiza ajustes si es necesario y confirma para guardar directamente en el historial del paciente.
              </p>
            </div>
            
            <Button className="gap-2 bg-purple-gradient hover:bg-purple-gradient-light mt-4">
              <FileTextIcon className="h-4 w-4" />
              <span>Ver documentación técnica</span>
            </Button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ProductDemo;


import React from 'react';
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { 
  Layers3Icon, 
  Lock, 
  Settings2Icon, 
  LineChart, 
  CloudIcon, 
  Laptop2Icon,
  TabletIcon,
  SmartphoneIcon,
  ServerIcon,
  ShieldIcon
} from 'lucide-react';

const FeaturesSection = () => {
  return (
    <section className="section bg-white">
      <div className="container mx-auto">
        <div className="text-center max-w-2xl mx-auto mb-16">
          <h2 className="mb-4">
            Características <span className="biamed-gradient-text">técnicas avanzadas</span>
          </h2>
          <p className="text-xl text-gray-600">
            BIAmed combina tecnología de vanguardia con una experiencia de usuario intuitiva para transformar la documentación médica.
          </p>
        </div>
        
        <Tabs defaultValue="funcionalidad" className="w-full max-w-4xl mx-auto">
          <TabsList className="grid grid-cols-3 mb-8">
            <TabsTrigger value="funcionalidad">Funcionalidad</TabsTrigger>
            <TabsTrigger value="tecnologia">Tecnología</TabsTrigger>
            <TabsTrigger value="seguridad">Seguridad</TabsTrigger>
          </TabsList>
          
          <TabsContent value="funcionalidad" className="space-y-8">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div className="biamed-card">
                <Layers3Icon className="h-8 w-8 text-biamed-purple mb-4" />
                <h3 className="text-xl font-bold mb-2">Reconocimiento contextual</h3>
                <p className="text-gray-600">
                  Comprende el contexto médico y adapta la transcripción a la especialidad del profesional, mejorando la precisión con el uso.
                </p>
              </div>
              
              <div className="biamed-card">
                <Settings2Icon className="h-8 w-8 text-biamed-purple mb-4" />
                <h3 className="text-xl font-bold mb-2">Personalización avanzada</h3>
                <p className="text-gray-600">
                  Adapta el sistema a tu vocabulario específico, terminología preferida y estructura de documentos habituales.
                </p>
              </div>
              
              <div className="biamed-card">
                <LineChart className="h-8 w-8 text-biamed-purple mb-4" />
                <h3 className="text-xl font-bold mb-2">Análisis e informes</h3>
                <p className="text-gray-600">
                  Genera automáticamente informes estructurados y extrae datos clave para análisis clínicos y administrativos.
                </p>
              </div>
              
              <div className="biamed-card">
                <CloudIcon className="h-8 w-8 text-biamed-purple mb-4" />
                <h3 className="text-xl font-bold mb-2">Integración con HIS/EMR</h3>
                <p className="text-gray-600">
                  Se integra perfectamente con los principales sistemas de historia clínica electrónica y gestión hospitalaria.
                </p>
              </div>
            </div>
          </TabsContent>
          
          <TabsContent value="tecnologia" className="space-y-8">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div className="biamed-card">
                <ServerIcon className="h-8 w-8 text-biamed-purple mb-4" />
                <h3 className="text-xl font-bold mb-2">IA de última generación</h3>
                <p className="text-gray-600">
                  Procesamiento del lenguaje natural (NLP) especializado en terminología médica con redes neuronales profundas.
                </p>
              </div>
              
              <div className="biamed-card">
                <TabletIcon className="h-8 w-8 text-biamed-purple mb-4" />
                <h3 className="text-xl font-bold mb-2">Compatible con múltiples dispositivos</h3>
                <p className="text-gray-600">
                  Funciona en ordenadores, tablets y smartphones, permitiendo flexibilidad total para los profesionales médicos.
                </p>
              </div>
              
              <div className="biamed-card">
                <Laptop2Icon className="h-8 w-8 text-biamed-purple mb-4" />
                <h3 className="text-xl font-bold mb-2">Funcionamiento offline</h3>
                <p className="text-gray-600">
                  Capacidad de trabajar sin conexión a internet, sincronizando los datos cuando la conexión se restablece.
                </p>
              </div>
              
              <div className="biamed-card">
                <SmartphoneIcon className="h-8 w-8 text-biamed-purple mb-4" />
                <h3 className="text-xl font-bold mb-2">Aplicaciones nativas</h3>
                <p className="text-gray-600">
                  Disponible como aplicación web y aplicaciones nativas para iOS y Android para máximo rendimiento.
                </p>
              </div>
            </div>
          </TabsContent>
          
          <TabsContent value="seguridad" className="space-y-8">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div className="biamed-card">
                <Lock className="h-8 w-8 text-biamed-purple mb-4" />
                <h3 className="text-xl font-bold mb-2">Encriptación de extremo a extremo</h3>
                <p className="text-gray-600">
                  Toda la información se encripta utilizando protocolos de seguridad avanzados para garantizar la confidencialidad de los datos.
                </p>
              </div>
              
              <div className="biamed-card">
                <ShieldIcon className="h-8 w-8 text-biamed-purple mb-4" />
                <h3 className="text-xl font-bold mb-2">Cumplimiento normativo</h3>
                <p className="text-gray-600">
                  Conforme con HIPAA, GDPR, LOPD y otras regulaciones internacionales de protección de datos sanitarios.
                </p>
              </div>
              
              <div className="biamed-card">
                <ServerIcon className="h-8 w-8 text-biamed-purple mb-4" />
                <h3 className="text-xl font-bold mb-2">Procesamiento local</h3>
                <p className="text-gray-600">
                  Opción de procesamiento de datos dentro de las instalaciones del cliente para máxima seguridad.
                </p>
              </div>
              
              <div className="biamed-card">
                <ShieldIcon className="h-8 w-8 text-biamed-purple mb-4" />
                <h3 className="text-xl font-bold mb-2">Auditorías de seguridad</h3>
                <p className="text-gray-600">
                  Realizamos auditorías de seguridad regulares por entidades externas para garantizar la protección de datos.
                </p>
              </div>
            </div>
          </TabsContent>
        </Tabs>
      </div>
    </section>
  );
};

export default FeaturesSection;

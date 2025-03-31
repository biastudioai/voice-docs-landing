
import React from 'react';
import { ClockIcon, CheckCircleIcon, BarChart3Icon, HeartPulseIcon, BrainCircuitIcon, ShieldCheckIcon } from 'lucide-react';

const benefits = [
  {
    icon: <ClockIcon className="h-10 w-10 text-biamed-purple" />,
    title: "Ahorra hasta 2 horas diarias",
    description: "Reduce el tiempo dedicado a la documentación hasta en un 70%, permitiéndote enfocarte más en tus pacientes."
  },
  {
    icon: <CheckCircleIcon className="h-10 w-10 text-biamed-purple" />,
    title: "Minimiza errores de documentación",
    description: "Disminuye significativamente los errores en reportes médicos y documentos de seguros con reconocimiento de voz preciso."
  },
  {
    icon: <BarChart3Icon className="h-10 w-10 text-biamed-purple" />,
    title: "Aumenta la productividad",
    description: "Atiende más pacientes sin comprometer la calidad del servicio ni la precisión de la documentación."
  },
  {
    icon: <HeartPulseIcon className="h-10 w-10 text-biamed-purple" />,
    title: "Mejora la experiencia del paciente",
    description: "Dedica más tiempo a la interacción con tus pacientes y menos a la pantalla o a las notas."
  },
  {
    icon: <BrainCircuitIcon className="h-10 w-10 text-biamed-purple" />,
    title: "IA especializada en terminología médica",
    description: "Reconoce términos médicos especializados con alta precisión, incluyendo nombres de medicamentos y procedimientos."
  },
  {
    icon: <ShieldCheckIcon className="h-10 w-10 text-biamed-purple" />,
    title: "Cumple con normativas sanitarias",
    description: "Garantiza el cumplimiento de HIPAA, GDPR y otras normativas de privacidad de datos médicos."
  }
];

const BenefitsSection = () => {
  return (
    <section id="beneficios" className="section bg-biamed-gray-light">
      <div className="container mx-auto">
        <div className="text-center max-w-2xl mx-auto mb-16">
          <h2 className="mb-4">
            Beneficios <span className="biamed-gradient-text">para profesionales médicos</span>
          </h2>
          <p className="text-xl text-gray-600">
            BIAmed transforma la forma en que los médicos y centros sanitarios gestionan la documentación clínica con tecnología de vanguardia.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {benefits.map((benefit, index) => (
            <div key={index} className="biamed-card flex flex-col">
              <div className="mb-4 p-3 bg-biamed-purple/10 rounded-lg self-start">
                {benefit.icon}
              </div>
              <h3 className="text-xl font-bold mb-2">{benefit.title}</h3>
              <p className="text-gray-600">{benefit.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default BenefitsSection;

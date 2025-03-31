
import React from 'react';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";

const faqs = [
  {
    question: "¿Cómo se integra BIAmed con nuestro sistema actual?",
    answer: "BIAmed cuenta con API abiertas y conectores específicos para los principales sistemas de historia clínica electrónica del mercado. Nuestro equipo técnico se encarga de todo el proceso de integración, garantizando una transición suave y sin interrupciones en su servicio."
  },
  {
    question: "¿Qué precisión tiene el reconocimiento de voz para terminología médica?",
    answer: "BIAmed alcanza una precisión superior al 98% para terminología médica general, y por encima del 95% para especialidades médicas específicas. El sistema aprende continuamente de las correcciones, mejorando con el uso y adaptándose a su vocabulario específico."
  },
  {
    question: "¿Necesito entrenar al sistema para que reconozca mi voz?",
    answer: "No, BIAmed funciona sin entrenamiento previo. El sistema utiliza algoritmos avanzados de IA que se adaptan instantáneamente a diferentes acentos, tonos y formas de hablar. No obstante, cuanto más lo utilice, mejor será la adaptación a sus patrones específicos de dictado."
  },
  {
    question: "¿Qué idiomas soporta la plataforma?",
    answer: "Actualmente, BIAmed soporta español (con sus variantes regionales), inglés, francés, alemán, italiano y portugués. Estamos trabajando continuamente para añadir más idiomas a nuestra oferta."
  },
  {
    question: "¿Cómo garantizan la seguridad y confidencialidad de la información?",
    answer: "Implementamos encriptación de extremo a extremo, servidores seguros con certificación ISO 27001, y procesamiento que cumple con HIPAA, GDPR y otras normativas de protección de datos sanitarios. Todos nuestros procesos están diseñados priorizando la seguridad y confidencialidad de la información médica."
  },
  {
    question: "¿Cuánto tiempo se tarda en implementar BIAmed en nuestro centro?",
    answer: "Para la mayoría de los centros, el proceso de implementación toma entre 1 y 3 semanas, dependiendo de la complejidad de la integración con sus sistemas existentes. Ofrecemos soporte completo durante todo el proceso, incluyendo formación para su personal."
  },
  {
    question: "¿Ofrecen una prueba antes de comprometerse con la compra?",
    answer: "Sí, ofrecemos un período de prueba de 30 días para que pueda experimentar todos los beneficios de BIAmed en su propio entorno de trabajo. Durante este período, tendrá acceso completo a todas las funcionalidades y a nuestro soporte técnico."
  }
];

const FAQSection = () => {
  return (
    <section id="preguntas" className="section bg-biamed-gray-light">
      <div className="container mx-auto">
        <div className="text-center max-w-2xl mx-auto mb-16">
          <h2 className="mb-4">
            Preguntas <span className="biamed-gradient-text">frecuentes</span>
          </h2>
          <p className="text-xl text-gray-600">
            Encuentra respuestas a las dudas más comunes sobre BIAmed
          </p>
        </div>
        
        <div className="max-w-3xl mx-auto bg-white rounded-xl shadow-lg p-8 border border-gray-100">
          <Accordion type="single" collapsible className="space-y-4">
            {faqs.map((faq, index) => (
              <AccordionItem key={index} value={`item-${index}`} className="border-b border-gray-200 pb-4">
                <AccordionTrigger className="text-left font-semibold hover:text-biamed-purple">
                  {faq.question}
                </AccordionTrigger>
                <AccordionContent className="text-gray-600 pt-2">
                  {faq.answer}
                </AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        </div>
      </div>
    </section>
  );
};

export default FAQSection;

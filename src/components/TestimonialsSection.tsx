
import React from 'react';
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { StarIcon } from 'lucide-react';

const testimonials = [
  {
    name: "Dra. Laura Martínez",
    role: "Cardióloga, Hospital Universitario",
    quote: "BIAmed ha revolucionado mi consulta. Ahora puedo dedicar más tiempo a mis pacientes y menos a la documentación. La precisión del reconocimiento de términos cardiológicos es impresionante.",
    image: "",
    stars: 5
  },
  {
    name: "Dr. Carlos Vega",
    role: "Director Médico, Clínica Privada",
    quote: "Implementamos BIAmed en toda nuestra clínica y los resultados son extraordinarios. Los médicos están más satisfechos y hemos reducido los costos administrativos en un 30%.",
    image: "",
    stars: 5
  },
  {
    name: "Dr. Antonio Ruiz",
    role: "Médico de Familia",
    quote: "La facilidad de uso y la capacidad de integración con nuestro sistema existente hizo que la transición fuera perfecta. Ahora termino mis notas antes de que el paciente salga de la consulta.",
    image: "",
    stars: 4
  }
];

const TestimonialsSection = () => {
  const renderStars = (count: number) => {
    return Array(5).fill(0).map((_, i) => (
      <StarIcon 
        key={i} 
        className={`h-4 w-4 ${i < count ? 'text-yellow-400 fill-yellow-400' : 'text-gray-300'}`} 
      />
    ));
  };

  return (
    <section id="testimonios" className="section bg-biamed-gray-light">
      <div className="container mx-auto">
        <div className="text-center max-w-2xl mx-auto mb-16">
          <h2 className="mb-4">
            Lo que dicen nuestros <span className="biamed-gradient-text">usuarios</span>
          </h2>
          <p className="text-xl text-gray-600">
            Profesionales médicos de diversas especialidades confían en BIAmed para optimizar su documentación clínica.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {testimonials.map((testimonial, index) => (
            <div key={index} className="biamed-card">
              <div className="flex justify-between items-start mb-4">
                <div className="flex items-center gap-3">
                  <Avatar className="h-12 w-12 border-2 border-biamed-purple/20">
                    <AvatarFallback className="bg-biamed-purple/10 text-biamed-purple">
                      {testimonial.name.split(' ').map(name => name[0]).join('')}
                    </AvatarFallback>
                  </Avatar>
                  <div>
                    <h4 className="font-bold">{testimonial.name}</h4>
                    <p className="text-sm text-gray-600">{testimonial.role}</p>
                  </div>
                </div>
                <div className="flex">
                  {renderStars(testimonial.stars)}
                </div>
              </div>
              <blockquote className="text-gray-700 italic">
                "{testimonial.quote}"
              </blockquote>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default TestimonialsSection;

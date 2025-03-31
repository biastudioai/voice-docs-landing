
import React, { useState } from 'react';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { useToast } from "@/components/ui/use-toast";

const DemoForm = () => {
  const { toast } = useToast();
  const [loading, setLoading] = useState(false);
  
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    
    // Simular envío del formulario
    setTimeout(() => {
      setLoading(false);
      toast({
        title: "Solicitud recibida",
        description: "Nos pondremos en contacto contigo muy pronto para coordinar tu demostración personalizada.",
      });
    }, 1500);
  };
  
  return (
    <div className="space-y-5">
      <div className="text-center mb-6">
        <h3 className="text-2xl font-bold">Solicita una demostración gratuita</h3>
        <p className="text-gray-600 mt-2">Descubre cómo BIAmed puede transformar tu práctica</p>
      </div>
      
      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div className="space-y-2">
            <label htmlFor="nombre" className="text-sm font-medium">
              Nombre completo
            </label>
            <Input id="nombre" placeholder="Nombre y apellido" required />
          </div>
          
          <div className="space-y-2">
            <label htmlFor="email" className="text-sm font-medium">
              Email profesional
            </label>
            <Input id="email" type="email" placeholder="correo@clinica.com" required />
          </div>
        </div>
        
        <div className="space-y-2">
          <label htmlFor="telefono" className="text-sm font-medium">
            Teléfono
          </label>
          <Input id="telefono" placeholder="+34 600 000 000" />
        </div>
        
        <div className="space-y-2">
          <label htmlFor="institucion" className="text-sm font-medium">
            Centro médico / Hospital
          </label>
          <Input id="institucion" placeholder="Nombre de la institución" required />
        </div>
        
        <div className="space-y-2">
          <label htmlFor="rol" className="text-sm font-medium">
            Rol / Especialidad
          </label>
          <Select>
            <SelectTrigger>
              <SelectValue placeholder="Selecciona tu rol" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="medico">Médico</SelectItem>
              <SelectItem value="especialista">Médico especialista</SelectItem>
              <SelectItem value="administrador">Administrador</SelectItem>
              <SelectItem value="director">Director médico</SelectItem>
              <SelectItem value="otro">Otro</SelectItem>
            </SelectContent>
          </Select>
        </div>
        
        <div className="space-y-2">
          <label htmlFor="mensaje" className="text-sm font-medium">
            ¿Alguna pregunta o comentario adicional?
          </label>
          <Textarea id="mensaje" placeholder="Escribe aquí tus dudas o necesidades específicas" />
        </div>
        
        <Button type="submit" className="w-full bg-purple-gradient hover:bg-purple-gradient-light" disabled={loading}>
          {loading ? "Enviando solicitud..." : "Solicitar demostración"}
        </Button>
        
        <p className="text-xs text-center text-gray-500 mt-4">
          Al enviar este formulario, aceptas nuestra política de privacidad y términos de servicio.
        </p>
      </form>
    </div>
  );
};

export default DemoForm;

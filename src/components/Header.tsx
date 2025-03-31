
import React from 'react';
import { Button } from "@/components/ui/button";
import { Link } from "react-router-dom";

const Header = () => {
  return (
    <header className="py-4 border-b border-gray-100 fixed top-0 w-full bg-white/95 backdrop-blur-sm z-50">
      <div className="container mx-auto flex justify-between items-center">
        <div className="flex items-center gap-2">
          <div className="h-8 w-8 rounded bg-purple-gradient"></div>
          <span className="font-bold text-2xl tracking-tight">
            BIA<span className="font-extrabold">MED</span>
          </span>
        </div>
        
        <nav className="hidden md:flex gap-8 items-center">
          <Link to="#beneficios" className="font-medium hover:text-biamed-purple transition-colors">
            Beneficios
          </Link>
          <Link to="#funcionamiento" className="font-medium hover:text-biamed-purple transition-colors">
            Cómo funciona
          </Link>
          <Link to="#testimonios" className="font-medium hover:text-biamed-purple transition-colors">
            Testimonios
          </Link>
          <Link to="#preguntas" className="font-medium hover:text-biamed-purple transition-colors">
            FAQ
          </Link>
        </nav>

        <div className="flex gap-3">
          <Button variant="outline" className="hidden sm:inline-flex">
            Iniciar sesión
          </Button>
          <Button className="bg-purple-gradient hover:bg-purple-gradient-light">
            Solicitar demo
          </Button>
        </div>
      </div>
    </header>
  );
};

export default Header;

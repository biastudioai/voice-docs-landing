
import React from 'react';
import { Link } from "react-router-dom";
import { FacebookIcon, TwitterIcon, LinkedinIcon, InstagramIcon } from 'lucide-react';

const Footer = () => {
  return (
    <footer className="bg-white border-t border-gray-200">
      <div className="container mx-auto py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div className="space-y-4">
            <div className="flex items-center gap-2">
              <div className="h-8 w-8 rounded bg-purple-gradient"></div>
              <span className="font-bold text-2xl tracking-tight">
                BIA<span className="font-extrabold">MED</span>
              </span>
            </div>
            <p className="text-gray-600">
              Soluciones avanzadas de reconocimiento de voz diseñadas específicamente para profesionales de la salud.
            </p>
            <div className="flex gap-4 pt-2">
              <Link to="#" className="text-gray-500 hover:text-biamed-purple">
                <FacebookIcon className="h-5 w-5" />
              </Link>
              <Link to="#" className="text-gray-500 hover:text-biamed-purple">
                <TwitterIcon className="h-5 w-5" />
              </Link>
              <Link to="#" className="text-gray-500 hover:text-biamed-purple">
                <LinkedinIcon className="h-5 w-5" />
              </Link>
              <Link to="#" className="text-gray-500 hover:text-biamed-purple">
                <InstagramIcon className="h-5 w-5" />
              </Link>
            </div>
          </div>
          
          <div>
            <h4 className="font-bold text-lg mb-4">Productos</h4>
            <ul className="space-y-2">
              <li>
                <Link to="#" className="text-gray-600 hover:text-biamed-purple">BIAmed Voice</Link>
              </li>
              <li>
                <Link to="#" className="text-gray-600 hover:text-biamed-purple">BIAmed Analytics</Link>
              </li>
              <li>
                <Link to="#" className="text-gray-600 hover:text-biamed-purple">BIAmed Mobile</Link>
              </li>
              <li>
                <Link to="#" className="text-gray-600 hover:text-biamed-purple">BIAmed Enterprise</Link>
              </li>
              <li>
                <Link to="#" className="text-gray-600 hover:text-biamed-purple">Integraciones</Link>
              </li>
            </ul>
          </div>
          
          <div>
            <h4 className="font-bold text-lg mb-4">Recursos</h4>
            <ul className="space-y-2">
              <li>
                <Link to="#" className="text-gray-600 hover:text-biamed-purple">Blog</Link>
              </li>
              <li>
                <Link to="#" className="text-gray-600 hover:text-biamed-purple">Guías y tutoriales</Link>
              </li>
              <li>
                <Link to="#" className="text-gray-600 hover:text-biamed-purple">Casos de éxito</Link>
              </li>
              <li>
                <Link to="#" className="text-gray-600 hover:text-biamed-purple">Webinars</Link>
              </li>
              <li>
                <Link to="#" className="text-gray-600 hover:text-biamed-purple">Soporte</Link>
              </li>
            </ul>
          </div>
          
          <div>
            <h4 className="font-bold text-lg mb-4">Empresa</h4>
            <ul className="space-y-2">
              <li>
                <Link to="#" className="text-gray-600 hover:text-biamed-purple">Sobre nosotros</Link>
              </li>
              <li>
                <Link to="#" className="text-gray-600 hover:text-biamed-purple">Contacto</Link>
              </li>
              <li>
                <Link to="#" className="text-gray-600 hover:text-biamed-purple">Empleo</Link>
              </li>
              <li>
                <Link to="#" className="text-gray-600 hover:text-biamed-purple">Privacidad</Link>
              </li>
              <li>
                <Link to="#" className="text-gray-600 hover:text-biamed-purple">Términos y condiciones</Link>
              </li>
            </ul>
          </div>
        </div>
        
        <div className="border-t border-gray-200 mt-12 pt-8 flex flex-col md:flex-row justify-between items-center text-gray-500 text-sm">
          <p>© {new Date().getFullYear()} BIAmed. Todos los derechos reservados.</p>
          <div className="flex gap-4 mt-4 md:mt-0">
            <Link to="#" className="hover:text-biamed-purple">Política de privacidad</Link>
            <Link to="#" className="hover:text-biamed-purple">Términos de servicio</Link>
            <Link to="#" className="hover:text-biamed-purple">Política de cookies</Link>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;

"use client";

import { useRouter } from "next/navigation";
import { useContext, useEffect } from "react";
import AuthContext from "../context/AuthContext";

const ProtectedRoute = ({ children }) => {
  const context = useContext(AuthContext);
  const router = useRouter();

  useEffect(() => {
    if (!context || !context.user) {
      router.push("/login");
    }
  }, [context, router]);

  return context && context.user ? children : null;
};

export default ProtectedRoute;

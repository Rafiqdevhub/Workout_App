import ProtectedRoute from "@/components/ProtectedRoute";

const Home = () => {
  return (
    <ProtectedRoute>
      <h1>Home</h1>
    </ProtectedRoute>
  );
};

export default Home;

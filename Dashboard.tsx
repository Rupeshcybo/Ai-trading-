
import ChartUpload from "../components/upload/ChartUpload";
import MarketStructureCard from "../components/analysis/MarketStructureCard";

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-gray-900 text-white p-4">
      <h1 className="text-2xl font-bold mb-4">AI Trading Assistant</h1>
      <ChartUpload />
      <MarketStructureCard />
    </div>
  );
}

async function getDevices() {
  const endpoint = "http://localhost:8000/api/devices/";
  const res = await fetch(endpoint);

  if (!res.ok) {
    // This will activate the closest `error.js` Error Boundary
    throw new Error("Failed to fetch data");
  }

  return res.json();
}

export default async function Devices() {
  const devices = await getDevices();

  return (
    <div classname="flex flex-col items-center mt-2">
      <h1 classname="text-4xl">Devices</h1>
      <div className="mt-5 flex flex-col gap-2">
        {devices.map((device) => (
          <p className="text-xl" key={device.id}>
            {device.name}
          </p>
        ))}
      </div>
    </div>
  );
}

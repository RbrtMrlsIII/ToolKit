// Storage for 3D assets
export async function upload3DAsset(file: File, path: string) {
  // Upload to supabase storage or firebase storage or local
  console.log(`Uploading 3D asset to ${path}`);
  return { path, url: `https://storage.example.com/${path}` };
}

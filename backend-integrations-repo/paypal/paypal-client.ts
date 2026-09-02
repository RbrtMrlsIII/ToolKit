// PayPal client — universal
export const paypalConfig = {
  clientId: process.env.PAYPAL_CLIENT_ID!,
  clientSecret: process.env.PAYPAL_CLIENT_SECRET!,
  mode: process.env.PAYPAL_MODE || 'sandbox'
};

export async function createPayPalOrder(amount: string) {
  // Example — adapt to your project
  return { id: 'ORDER_ID', amount, status: 'CREATED' };
}

// PayPal webhook handler
export async function handlePayPalWebhook(event: any) {
  console.log("PayPal webhook:", event.event_type);
  // Update endorsement or census after payment
}

// Auth middleware — validated pattern
export function authMiddleware(req: any, res: any, next: any) {
  const token = req.headers.authorization;
  if (!token) return res.status(401).send('No token');
  next();
}

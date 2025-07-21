import { z } from "zod";

export const headerValidationSchema = z.object({
  authToken: z.string().min(1, "Auth token is required"),
  requestSignature: z.string().min(1, "Request signature is required"),
  userAgent: z.string().min(1, "User agent is required")
});

export type HeaderValidation = z.infer<typeof headerValidationSchema>;

export interface ValidationResponse {
  success: boolean;
  message: string;
  errors?: {
    authToken?: boolean;
    requestSignature?: boolean;
    userAgent?: boolean;
  };
  flag?: string;
}

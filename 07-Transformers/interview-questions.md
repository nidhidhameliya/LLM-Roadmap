# Interview Questions
**Q: Why do we scale the dot product in self-attention by $\sqrt{d_k}$?**
A: To prevent the dot product from growing too large, which would push the softmax function into regions with extremely small gradients (vanishing gradients).

**Q: What is the purpose of the Mask in self-attention?**
A: In the decoder (autoregressive models), the mask prevents the model from "looking ahead" at future tokens during training, ensuring it only uses past and current tokens to predict the next one.

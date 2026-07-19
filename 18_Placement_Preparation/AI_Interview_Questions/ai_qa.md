# Deep Learning & AI Interview Questions & Answers (Top 15)

This document contains 15 key Deep Learning and Generative AI interview questions frequently asked during technical placement screenings.

---

### Q1: Explain the self-attention mechanism in Transformers.
* **Answer**: Self-attention allows tokens in a sequence to dynamically weigh and focus on other tokens, regardless of their distance.
* **Mechanism**: For each token, the model computes three vectors: Query (Q), Key (K), and Value (V). It calculates attention scores by taking the dot product of the Query of one token with the Keys of all other tokens. These scores are scaled, passed through a softmax function, and used as weights to compute a weighted sum of the Value vectors. Formula: `Attention(Q, K, V) = softmax(Q • K^T / sqrt(d_k)) * V`.

---

### Q2: What is the difference between RAG and Fine-tuning?
* **Answer**:
  * **RAG (Retrieval-Augmented Generation)**: An architectural pattern that retrieves relevant context from an external database and inserts it into the LLM prompt. Good for dynamic, real-time data, requires zero training costs, and is highly auditable.
  * **Fine-Tuning**: A training process that updates model weights on a custom task dataset. Good for adapting the model's tone, style, or specific formatting rules, but computationally expensive and cannot easily adapt to changing factual data.

---

### Q3: What is the role of Temperature in LLM text generation?
* **Answer**: Temperature controls the randomness/creativity of token selection:
  * **Low Temperature (e.g. 0.2)**: Makes the model choose the highest-probability tokens, yielding deterministic, focused answers.
  * **High Temperature (e.g. 0.9)**: flattens the probability distribution, making lower-probability tokens more likely to be selected, yielding more creative and diverse responses.

---

### Q4: Explain the Backpropagation algorithm.
* **Answer**: Backpropagation is the method used to train neural networks. It works in two phases:
  1. **Forward Pass**: Input data passes through the layers to generate a prediction, and the error (loss) is calculated compared to the target.
  2. **Backward Pass**: Computes the gradient of the loss function with respect to each weight using the **Chain Rule** of calculus. These gradients are propagated backward from the output layer to the input layer to update weights via an optimizer (e.g. SGD).

---

### Q5: What is the Vanishing/Exploding Gradient problem and how do we solve it?
* **Answer**:
  * **Vanishing Gradients**: In deep networks, multiplying small gradients (e.g., derivative of sigmoid) recursively across layers causes them to shrink close to 0.0, stopping early layers from updating.
  * **Exploding Gradients**: Repeatedly multiplying large weights causes gradients to grow exponentially, making training unstable.
  * **Solutions**: Use ReLU activation instead of Sigmoid/Tanh, apply Batch Normalization, use Residual Connections (skip connections in ResNet), and implement gradient clipping.

---

### Q6: What is the difference between Word2Vec and Transformer Embeddings?
* **Answer**:
  * **Word2Vec**: Generates static embeddings. A word has the same vector regardless of context (e.g. 'bank' in 'river bank' and 'money bank' have identical representations).
  * **Transformers**: Generates dynamic, contextual embeddings. The vector for a word is dynamically computed based on the surrounding tokens, capturing contextual meanings.

---

### Q7: Explain the difference between standard RNNs, LSTMs, and GRUs.
* **Answer**:
  * **RNN**: Processes sequential data but suffers from vanishing gradients, losing long-term historical context.
  * **LSTM (Long Short-Term Memory)**: Solves this using a cell state and three gates (input, forget, output) to regulate the flow of information, preserving long-term dependencies.
  * **GRU (Gated Recurrent Unit)**: A simplified LSTM variant with two gates (reset, update). It has fewer parameters, training faster while maintaining comparable performance.

---

### Q8: What are Autoencoders?
* **Answer**: An unsupervised neural network designed to learn efficient data representations (codings). It consists of an **Encoder** that compresses the input into a low-dimensional bottleneck (latent space) and a **Decoder** that reconstructs the input from this bottleneck. Used for dimensionality reduction and denoising.

---

### Q9: Explain the difference between Tokenization strategies: Word-level, Character-level, and Subword-level.
* **Answer**:
  * **Word-level**: Splits text by spaces. Yields large vocabularies and fails to handle Out-Of-Vocabulary (OOV) words.
  * **Character-level**: Treats each character as a token. Slow to process and loses word-level semantic structure.
  * **Subword-level** (e.g. Byte-Pair Encoding, WordPiece): Splits common words into roots and prefixes (e.g. "unhappy" to "un" + "happy"). The standard in modern LLMs, as it balances vocabulary size and handles OOV terms.

---

### Q10: What is LLM hallucination and how do you reduce it?
* **Answer**: Hallucination is when an LLM generates factually incorrect text confidently.
* **Mitigation**:
  1. Retrieve grounding documents (RAG).
  2. Structure instructions using clear Prompt templates (CoT, few-shot examples).
  3. Lower the generation Temperature.
  4. Use system guardrails (like NeMo Guardrails or Llama Guard).

---

### Q11: Explain GANs (Generative Adversarial Networks).
* **Answer**: An unsupervised framework consisting of two neural networks competing:
  1. **Generator**: Tries to create fake data (e.g. images) that look real.
  2. **Discriminator**: Tries to distinguish between real data and fake data.
* **Mechanism**: They train simultaneously in a minimax game until the generator creates realistic outputs that the discriminator can no longer distinguish from real data.

---

### Q12: What is the role of Batch Normalization?
* **Answer**: Batch Normalization normalizes the inputs of each layer across the batch to have a mean of 0.0 and variance of 1.0. This stabilizes training, reduces internal covariate shift, allows for higher learning rates, and acts as a mild regularizer.

---

### Q13: What is the difference between Epoch, Batch, and Iteration?
* **Answer**:
  * **Epoch**: One complete pass of the entire training dataset through the neural network.
  * **Batch**: A subset of the dataset processed at one time to compute gradients.
  * **Iteration**: The total number of batch passes required to complete one epoch (e.g., 1000 samples with batch size 100 requires 10 iterations per epoch).

---

### Q14: Explain the difference between SGD, Momentum, RMSprop, and Adam optimizers.
* **Answer**:
  * **SGD**: Updates weights using a constant learning rate.
  * **Momentum**: Adds a fraction of the previous step vector to damp oscillations.
  * **RMSprop**: Adapts learning rates based on the running average of squared gradients.
  * **Adam**: Combines Momentum and RMSprop, tracking both the first moment (mean) and second moment (uncentered variance) of gradients, making it the default optimizer for deep learning.

---

### Q15: What is RLHF (Reinforcement Learning from Human Feedback)?
* **Answer**: RLHF is a training method used to align LLMs with human preferences (helpfulness, safety). It involves training a **Reward Model** on human-ranked outputs, then using reinforcement learning (typically PPO - Proximal Policy Optimization) to adjust the LLM's weights to maximize the reward score.

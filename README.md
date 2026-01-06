Friendship Engine
> **Status:** Exploratory research prototype  
> **Focus:** Human–AI Interaction, emotional support, conversational policy design  
> **Note:** This is not a chatbot product, but an experimental system built to study how interaction design choices affect perceived emotional bonding with AI.
> 
Exploring Proactive Conversational AI for Emotional Support and Social Bonding

Prototype / research exploration. Not a human.


Overview

Friendship Engine is an exploratory conversational AI project investigating whether interaction design choices—rather than raw model capability—can increase a user’s perceived sense of being listened to, understood, and emotionally supported.

The project focuses on proactive but constrained curiosity, lightweight memory, and contextual follow-ups to study how humans emotionally respond to AI systems in moments of stress, uncertainty, or isolation.

This is not an attempt to replace human relationships.
It is an investigation into AI as a non-judgmental conversational space.



Research Question

Can a conversational AI that asks carefully constrained, context-sensitive follow-up questions foster a perceived emotional bond and encourage self-disclosure, despite lacking genuine human emotion?



Hypothesis

A conversational agent with:
	•	proactive but limited curiosity,
	•	short-term coherent memory,
	•	emotionally aligned follow-up questions,

will produce:
	•	longer and more engaged conversations,
	•	higher perceived emotional support,
	•	increased willingness to share personal concerns,

compared to a purely reactive conversational style.



Design Principles
	•	Anti-interrogation rule: maximum one question per agent message
	•	Reflection before questioning
	•	Memory limited to non-sensitive context
	•	Explicit disclosure: “Prototype / experiment. Not a human.”
	•	No dependency-inducing language
	•	Privacy-first: local execution, no cloud logging



Implementation
	•	Language: Python
	•	LLM backend: Local model via Ollama (e.g. LLaMA 3.1 8B)
	•	Architecture:
	•	app.py – CLI interaction loop
	•	llm.py – model wrapper
	•	policy.py – curiosity and follow-up decision logic
	•	memory.py – constrained memory handling
	•	metrics.py – session metrics & self-report surveys
	•	configs.py – A/B mode and experiment configuration

The system runs fully locally and logs anonymized interaction metrics.



Evaluation (Exploratory)

The prototype was tested in five in-person sessions.

Self-reported scores (1–10): 3, 5, 6, 7, 8


Qualitative feedback themes:
	•	The agent felt attentive and interested
	•	Users appreciated follow-up questions
	•	The system was perceived as non-judgmental
	•	Lack of genuine human warmth was noted
	•	Several users felt more comfortable opening up than with people



Findings
	•	AI does not replicate human emotional bonding
	•	AI can provide functional emotional support by:
	•	lowering barriers to self-expression
	•	sustaining reflective conversation
	•	offering a psychologically safe space

Friendship Engine suggests emotional bonding is an emergent property of system design, not a binary model capability.



Limitations
	•	Small sample size
	•	Qualitative evaluation
	•	Single model and policy configuration

These limitations are intentional: the project prioritizes insight over statistical generalization.

## Ethical Positioning

This project explicitly avoids framing the agent as a replacement for human relationships.

Design constraints include:
- Clear disclosure that the system is a prototype and not a human.
- No use of dependency-inducing language (e.g., exclusivity, guilt, emotional manipulation).
- Memory limited to non-sensitive conversational context.
- Gentle redirection toward human support if strong distress emerges.

The goal is to explore AI as a complementary emotional tool, not as a substitute for human connection.

Future Directions
	•	Controlled A/B studies on curiosity policies
	•	Longitudinal user interaction
	•	Adaptive memory decay
	•	Ethical boundaries in emotionally supportive AI
	•	Extensions toward Human–AI Interaction and social robotics



Why This Matters

As AI systems enter increasingly personal domains, understanding how design constraints shape emotional experience becomes critical.

Friendship Engine frames emotional support not as a replacement for human connection, but as a complementary tool—especially in moments of loneliness, stress, or fear of judgment.


Status

🧪 Active research prototype (MVP v0.1)
Built for experimentation, iteration, and learning.



This project treats emotional bonding not as a property of the language model alone, but as an emergent outcome of system design, constraints, and interaction policy.

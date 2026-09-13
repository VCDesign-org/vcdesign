# VCDesign Operational Policy Set

## Status

Structure charter for a growing collection. Normative for how an article is
written; not itself a source of new rules.

This document fixes the shape every article in the operational policy set
must have, before the set grows past its first two articles. It exists so
that adding Article 3 and beyond does not require re-deciding the format
each time.

---

## 1. Why a structure charter first

Article 1 and Article 2 of this set ([Adjacent Boundary Observation
Policy](adjacent-boundary-observation.yaml)) were written together and are
interdependent. Before a third article is added by someone who was not
party to that first pair, the shape of an article needs to be fixed —
otherwise each new article reinvents its own justification style, and the
set stops being comparable article-to-article.

## 2. Required parts of every article

Every article in this set must contain exactly these three parts, in order:

1. **The rule itself.** Stated as a constraint, not a suggestion.
2. **What happened when this was not followed.** A real precedent, not a
   hypothetical. If no real failure exists yet, the article is not ready to
   be written — see §3.
3. **Why the rule stops where it stops.** The upper bound of the rule's
   applicability, and the reasoning for that bound. A rule with no stated
   limit invites indefinite extension by whoever applies it next.

An article missing part 3 is not a complete article — it is a principle
without a scope, and scope is what makes a rule usable under pressure
instead of merely aspirational.

## 3. Built from how it broke, not deduced from principle

Articles in this set are derived from observed failure, not from deducing
consequences of a general principle downward. A list of maxims with no
failure attached to any of them cannot be pruned by a reader for their own
situation — every maxim looks equally mandatory. A rule anchored to a
specific way it broke tells the reader exactly what it protects against,
so they can judge whether that failure mode applies to them.

This is why part 2 (a real precedent) is required, not optional: it is the
mechanism that keeps the set prunable.

## 4. Source material

This set is published to the org, so its precedents must be independently
verifiable by any reader, not anchored to one author's unpublishable
personal history. Articles in this set are drawn from:

- Publicly documented industry incidents with a published post-mortem or
  investigation report (regulatory, vendor, or academic) — not anecdote.
- Direct observation of incident first response, when that observation is
  itself public record (e.g. a published investigation), where boundary
  assumptions are tested under pressure, not in the abstract.

Material that does not trace to a citable, public source should not become
an article in this set without first being tested against real failure.
Article 1 and Article 2 cite the Mars Climate Orbiter loss (1999) and the
2012 leap-second kernel bug respectively — see
`adjacent-boundary-observation.yaml` for the citations.

## 5. Articles in this set

| # | Title | File |
|---|---|---|
| 1 | Adjacent Boundary Observation | [adjacent-boundary-observation.yaml](adjacent-boundary-observation.yaml) — `article_1` |
| 2 | Non-Chain Coupling | [adjacent-boundary-observation.yaml](adjacent-boundary-observation.yaml) — `article_2` |
| 3+ | Not yet defined | Open — see below |

Article 2 is a sibling of Article 1, not a sub-clause of it: distance-based
observation (Article 1) and common-cause coupling (Article 2) are covered
by different mechanisms and must not be nested under one another.

## 6. Open Questions

- **Article 3 and beyond** are not defined by this charter. This document
  fixes only the *shape* future articles must take; it does not commit to
  what they will cover.

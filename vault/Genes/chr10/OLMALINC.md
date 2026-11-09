---
symbol: "OLMALINC"
type: "gene"
col: 14039
ensembl_id: "ENSG00000235823"
name: "oligodendrocyte maturation-associated long intergenic non-coding RNA"
location: "10q24.31"
module: 86
arm: "+"
pooled_cpm: 33.24
n_lines_expressing: 49
n_dd_up: 33
n_dd_down: 14
n_dd_up_clean: 27
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# OLMALINC

*oligodendrocyte maturation-associated long intergenic non-coding RNA* — 10q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.59× (z +8.6, q 3e-15, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.616× (z -6.4, q 7e-08, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCD]] (+0.71, fdr 7e-06, ⚠ read-through risk), [[HMGCS1]] (+0.63, fdr 7e-06), [[IDI1]] (+0.58, fdr 1e-05), [[HSD17B7]] (+0.57, fdr 1e-05); moves opposite to [[NOC4L]] (-0.47, fdr 3e-05), [[CTU2]] (-0.47, fdr 3e-05), [[FAAP100]] (-0.46, fdr 4e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[VEGFD]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14039.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +8.6 | 3e-15 | 39/47 (SW480, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +8.6 | 3e-15 | 32/46 (HepG2/C3A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.53×** | +7.9 | 4e-13 | 37/47 (HOP62, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +7.7 | 2e-12 | 19/33 (HEC-1-A, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Berbamine (drug)]] 5 µM |  | **1.49×** | +7.4 | 1e-11 | 39/48 (SW480, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +7.4 | 2e-11 | 25/38 (CFPAC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bexarotene (drug)]] 0.05 µM |  | **1.71×** | +7.0 | 2e-10 | 35/47 (SW480, HT-29, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +7.0 | 2e-10 | 25/42 (C-33 A, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bexarotene (drug)]] 0.5 µM |  | **1.68×** | +6.9 | 4e-10 | 36/47 (SW480, HT-29, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 5 µM |  | **1.41×** | +6.4 | 1e-08 | 29/47 (SW480, HT-29, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.61×** | +6.3 | 2e-08 | 31/46 (HOP62, SW480, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.53×** | +5.4 | 3e-06 | 27/47 (HOP62, SW480, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.47×** | +5.1 | 1e-05 | 27/47 (SW480, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +5.0 | 2e-05 | 26/46 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +4.8 | 5e-05 | 28/46 (HOP62, A-172, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.41×** | +4.5 | 2e-04 | 24/46 (HOP62, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.41×** | +4.5 | 2e-04 | 21/47 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +4.4 | 4e-04 | 21/46 (A-172, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14039.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.616×** | -6.4 | 7e-08 | 31/46 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.631×** | -6.1 | 2e-07 | 28/46 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.620×** | -6.1 | 2e-07 | 22/46 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.635×** | -5.8 | 1e-06 | 26/45 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.749×** | -5.4 | 7e-06 | 24/46 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.696×** | -4.8 | 1e-04 | 22/45 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.710×** | -4.6 | 4e-04 | 21/46 (PANC-1, COLO 205, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.701×** | -4.5 | 4e-04 | 22/46 (KATO III, PANC-1, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **0.743×** | -4.0 | 0.005 | 15/47 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.745×** | -3.9 | 0.005 | 16/46 (H4, Panc 03.27, …) | inconsistent across doses |  |
| [[Clotrimazole (drug)]] 5 µM |  | **0.823×** | -3.7 | 0.012 | 19/47 (HT-29, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.761×** | -3.6 | 0.014 | 19/47 (PANC-1, SW480, …) | two highest doses | composition shift |
| [[Salicylic acid (drug)]] 5 µM |  | 0.835× | -3.4 | 0.028 | 18/47 (NCI-H661, LOX-IMVI, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.776×** | -3.4 | 0.031 | 18/46 (PANC-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.796×** | -3.0 | 0.089 | 17/47 (PANC-1, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14039. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 62.0 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -25.2) |
| [[SW480 (line)]] | alt | 63.4 | 3 | 3 (1 ⚠) | [[Bexarotene (drug)]] 0.5 µM 2.81× (z +10.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.383× (z -9.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.552× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 73.6 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -16.6) |
| [[HT-29 (line)]] | alt | 59.0 | 2 | 2 | [[Retinoic acid (drug)]] 5 µM 2.46× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -15.2) |
| [[NCI-H460 (line)]] | wt | 50.4 | 1 | 2 (1 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.73× (z +12.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.133× (z -18.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.510× (z -8.9) |
| [[SW 900 (line)]] | alt | 22.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.307× (z -8.6) |
| [[A-172 (line)]] | wt | 57.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.47× (z +9.6) | — |
| [[A-427 (line)]] | wt | 41.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 21.7 | 0 | 1 | — | [[Proglumide (drug)]] 0.5 µM 0.0506× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 11.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.23× (z +9.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 36.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +9.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 26.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 26.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.62× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 20.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +10.5) | — |
| [[KATO III (line)]] | alt | 41.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.246× (z -9.7) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 29.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -10.6) |
| [[SHP-77 (line)]] | alt | 34.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.4) |
| [[SW48 (line)]] | wt | 22.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0735× (z -11.0) ⚠ toxic |
| [[A498 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.27 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14039), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCD]] | +0.71 | +0.66 / +0.70 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 8.3 kb 3′ of SCD on the same strand (can correlate by spillover, not regulation) |
| [[HMGCS1]] | +0.63 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[IDI1]] | +0.58 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[HSD17B7]] | +0.57 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[HMGCR]] | +0.57 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[FDPS]] | +0.56 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[FDFT1]] | +0.56 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[MSMO1]] | +0.55 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[ACSS2]] | +0.54 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[STARD4]] | +0.54 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[INSIG1]] | +0.53 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[CYP51A1]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[LDLR]] | +0.53 | +0.54 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOC4L]] | -0.47 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[CTU2]] | -0.47 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[FAAP100]] | -0.46 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[UBIAD1]] | -0.45 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[TELO2]] | -0.42 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[USP31]] | -0.42 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[XPO4]] | -0.41 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[TREX2]] | -0.41 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[TRMT61A]] | -0.40 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[BOP1]] | -0.40 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[EEFSEC]] | -0.40 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[SPOUT1]] | -0.40 | -0.34 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VEGFD]] | B | VEGFD activity raises OLMALINC's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 1.38× lower at baseline in the lines without VEGFD | 0.080 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1 |
| [[ARMH1]] | C | ARMH1 activity raises OLMALINC's level | lines that do not express ARMH1 (3) vs lines expressing it (47) | 2.35× lower at baseline in the lines without ARMH1 | 0.067 | ⚠ few lines (3 vs 47); across organs; also absent: MCF2L2, KIAA1522, ENSG00000257489; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.9, -49.7); signed map (-53.1, 33.3). **Vector** length 115, 30.2% of its response variance represented; |z| ≥ 3 in 1,204 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *androgen response* (hallmark, mean cos +0.51 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +6.8 | +7.9 |
|  | [[Berbamine (drug)]] 5 µM |  | +6.0 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +8.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.3 | +4.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +5.1 | +6.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.8 | +4.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.2 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -6.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.0 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.8 | -6.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -3.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.3 | -0.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.3 | -4.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | oligodendrocyte maturation-associated long intergenic non-coding RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10q24.31 — chr10:100,373,099-100,454,043 (+) |
| Ensembl biotype | lncRNA |
| Also known as | bA34D15.5, FLJ12974, HI-LNC80; previously C10orf75, NCRNA00263, LINC00263 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28060](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28060) · Entrez [90271](https://www.ncbi.nlm.nih.gov/gene/90271) · Ensembl [ENSG00000235823](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235823)

## Data

Gene col 14039: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14039); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14039, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14039]; `tensor/DDL_lfc|DDL_z.npy` [14039]; `embed/gene_vectors.npy` [14039]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14039 or target_col == 14039). Every well: [[OLMALINC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OLMALINC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

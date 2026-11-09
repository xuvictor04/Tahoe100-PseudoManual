---
symbol: "SAMD1"
type: "gene"
col: 6576
ensembl_id: "ENSG00000141858"
name: "sterile alpha motif domain containing 1"
location: "19p13.12"
module: 67
arm: "+"
pooled_cpm: 17.02
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# SAMD1

*sterile alpha motif domain containing 1* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.26× (z +11.9, q 5e-30, up in 40 of 41 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (SW480 6.91×, PANC-1 5.85×, MIA PaCa-2 5.46×, A498 6.10×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (PANC-1 5.66×, LoVo 7.09×, SW480 5.45×, A498 6.14×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.371× (z -11.5, q 6e-28, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE7A]] (+0.63, fdr 1e-05), [[ADGRL1]] (+0.60, fdr 1e-05), [[THSD4-AS1]] (+0.59, fdr 1e-05); moves opposite to [[ZNF222]] (-0.57, fdr 3e-05), [[TTC4]] (-0.51, fdr 4e-05), [[EXOC8]] (-0.51, fdr 2e-04).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CARD6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6576.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (SW480 6.91×, PANC-1 5.85×, MIA PaCa-2 5.46×, A498 6.10×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (PANC-1 5.66×, LoVo 7.09×, SW480 5.45×, A498 6.14×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.26×** | +11.9 | 5e-30 | 40/41 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.81×** | +10.6 | 1e-23 | 27/30 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +7.4 | 2e-11 | 33/37 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.7 | 0.028 | 23/43 (SW480, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.35×** | +3.5 | 0.046 | 24/48 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.51×** | +3.4 | 0.065 | 22/44 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | 1.49× | +3.1 | 0.14 | 19/45 (NCI-H23, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6576.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.371×** | -11.5 | 6e-28 | 37/47 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.369×** | -8.2 | 8e-14 | 39/46 (A-427, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.437×** | -6.4 | 3e-08 | 42/47 (A-427, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.458×** | -6.2 | 1e-07 | 35/47 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.541×** | -5.0 | 5e-05 | 34/47 (A-172, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.551×** | -4.9 | 1e-04 | 35/47 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.595×** | -4.3 | 0.002 | 26/47 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.620×** | -3.9 | 0.006 | 26/47 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.717×** | -3.9 | 0.007 | 22/48 (SNU-1, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.430×** | -3.6 | 0.016 | 22/40 (MIA PaCa-2, J82, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.644×** | -3.6 | 0.016 | 22/47 (NCI-H2030, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.646×** | -3.6 | 0.016 | 24/47 (SNU-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ivermectin (drug)]] 5 µM |  | **0.649×** | -3.5 | 0.017 | 22/47 (C-33 A, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.654×** | -3.5 | 0.020 | 24/47 (RKO, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.665×** | -3.3 | 0.031 | 22/47 (A-427, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6576. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 40.8 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.39× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0680× (z -16.6) |
| [[SW480 (line)]] | alt | 16.7 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.91× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -14.0) |
| [[LS 180 (line)]] | wt | 21.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.32× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0819× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 30.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.46× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -14.3) |
| [[PANC-1 (line)]] | alt | 19.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.85× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -8.8) |
| [[RKO (line)]] | wt | 19.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.115× (z -11.1) |
| [[A-172 (line)]] | wt | 23.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -10.3) |
| [[A498 (line)]] | wt | 10.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.10× (z +9.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 45.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 18.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -10.5) |
| [[HOP62 (line)]] | alt | 9.97 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.50× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 14.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.09× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -8.6) |
| [[LoVo (line)]] | wt | 15.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.09× (z +11.0) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 13.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 15.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 7.27 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0841× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 20.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -14.5) |
| [[C32 (line)]] | wt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -10.5) |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -9.5) |
| [[Hs 766T (line)]] | wt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -9.8) |
| [[HS-578T (line)]] | alt | 15.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.148× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0937× (z -8.6) |
| [[J82 (line)]] | alt | 23.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0990× (z -21.2) |
| [[NCI-H23 (line)]] | alt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 17.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.125× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -11.8) |
| [[SNU-1 (line)]] | wt | 34.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.250× (z -9.6) ⚠ cell-cycle shift, explains ~68% of this change |
| [[SNU-423 (line)]] | alt | 14.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 26.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -8.7) |
| [[A549 (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6576), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE7A]] | +0.63 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[ADGRL1]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[THSD4-AS1]] | +0.59 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[MAZ]] | +0.57 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[PHLPP1]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[PXMP2]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ZMYM2]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PIGX]] | +0.53 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[CTXN1]] | +0.52 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[FANCC]] | +0.51 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[ABHD12]] | +0.51 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[SMAD6]] | +0.50 | +0.52 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF222]] | -0.57 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[TTC4]] | -0.51 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[EXOC8]] | -0.51 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[NDUFB9]] | -0.50 | -0.61 / -0.32 | both halves | 2e-04 |  |
| [[POLR2C]] | -0.48 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[TATDN1]] | -0.48 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[BRF2]] | -0.48 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[SRP68]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[SIKE1]] | -0.47 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[AIMP1]] | -0.47 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[PSMD6]] | -0.47 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[ZNF229]] | -0.47 | -0.42 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD6]] | B | CARD6 activity lowers SAMD1's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 1.70× higher at baseline in the lines without CARD6 | 0.004 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[CTXN1]] | B | CTXN1 activity raises SAMD1's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.78× lower at baseline in the lines without CTXN1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[CELSR2]] | B | CELSR2 activity raises SAMD1's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 1.68× lower at baseline in the lines without CELSR2 | 0.009 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |
| [[PODXL2]] | B | PODXL2 activity raises SAMD1's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.46× lower at baseline in the lines without PODXL2 | 0.050 | ⚠ within organs, on part of the lines |
| [[TLR1]] | B | TLR1 activity lowers SAMD1's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 1.60× higher at baseline in the lines without TLR1 | 0.051 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[SOBP]] | B | SOBP activity raises SAMD1's level | lines that do not express SOBP (19) vs lines expressing it (31) | 1.41× lower at baseline in the lines without SOBP | 0.059 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[RABGEF1P3]] | B | RABGEF1P3 activity lowers SAMD1's level | lines that do not express RABGEF1P3 (5) vs lines expressing it (45) | 2.09× higher at baseline in the lines without RABGEF1P3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, PHLDA2, SHB; maybe low, not absent; its own permutation p |
| [[CARD6]] | B | CARD6 activity weakens SAMD1's drug response | lines that do not express CARD6 (17) vs lines expressing it (31) | the lines without CARD6 respond 1.17× as strongly (z diff -1.13); strongest at Homoharringtonine 5 µM: 0.30x vs 0.43x (z diff -3.0) | 0.074 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.391). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.4, -51.5); signed map (-41.1, -29.3). **Vector** length 68.9, 16.5% of its response variance represented; |z| ≥ 3 in 769 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +2.3 | -3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | -1.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +2.3 | -3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | -0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.4 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.1 | +1.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 5 µM |  | +1.1 | -1.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -5.3 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -8.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -4.0 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -1.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.8 | +0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -0.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.4 | +1.5 |

## What is on record

|  |  |
|---|---|
| Name | sterile alpha motif domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:14,087,851-14,091,036 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sterile alpha motif domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6SPF0](https://www.uniprot.org/uniprotkb/Q6SPF0) (Sterile alpha motif domain-containing protein 1):

> Unmethylated CpG islands (CGIs)-binding protein which localizes to H3K4me3-decorated CGIs, where it acts as a transcriptional repressor. Tethers L3MBTL3 to chromatin and interacts with the KDM1A histone demethylase complex to modulate H3K4me2 and H3K4me3 levels at CGIs. Plays a role in atherogenesis by binding with LDL on cell surface and promoting LDL oxidation which leads to the formation of foam cell.

**Summary**, from NCBI Gene [90378](https://www.ncbi.nlm.nih.gov/gene/90378):

> Enables chromatin binding activity. Involved in negative regulation of transcription initiation-coupled chromatin remodeling and protein homooligomerization. Is active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17958](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17958) · Entrez [90378](https://www.ncbi.nlm.nih.gov/gene/90378) · UniProt [Q6SPF0](https://www.uniprot.org/uniprotkb/Q6SPF0) · Ensembl [ENSG00000141858](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141858)

## Data

Gene col 6576: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6576); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6576, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6576]; `tensor/DDL_lfc|DDL_z.npy` [6576]; `embed/gene_vectors.npy` [6576]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6576 or target_col == 6576). Every well: [[SAMD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAMD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

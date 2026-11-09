---
symbol: "INPP5K"
type: "gene"
col: 5308
ensembl_id: "ENSG00000132376"
name: "inositol polyphosphate-5-phosphatase K"
location: "17p13.3"
module: 76
arm: "+"
pooled_cpm: 14.94
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 19
n_dd_up_clean: 13
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# INPP5K

*inositol polyphosphate-5-phosphatase K* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.03× (z +17.5, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.397× (z -14.6, q 3e-45, down in 44 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.399× (z -7.6, q 1e-11, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTMR14]] (+0.75, fdr 7e-06), [[OTUD5]] (+0.73, fdr 7e-06), [[MEF2D]] (+0.70, fdr 7e-06); moves opposite to [[GCFC2]] (-0.58, fdr 2e-05), [[ZNF280D]] (-0.57, fdr 3e-05), [[FAM169A]] (-0.56, fdr 5e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5308.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.03×** | +17.5 | 0e+00 | 47/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.82×** | +16.4 | 0e+00 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +13.8 | 4e-41 | 38/45 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.25×** | +12.8 | 2e-35 | 46/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +7.7 | 1e-12 | 34/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +6.7 | 2e-09 | 24/47 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +6.0 | 1e-07 | 24/48 (COLO 205, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.89×** | +5.2 | 1e-05 | 17/43 (LS 180, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.88×** | +5.2 | 1e-05 | 17/46 (NCI-H460, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +4.3 | 9e-04 | 19/46 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.17× | +3.5 | 0.027 | 7/48 (Hs 766T, AsPC-1, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +3.2 | 0.058 | 3/48 (HEC-1-A, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.058 | 4/48 (A498, A-172, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.089 | 7/47 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.0 | 0.090 | 13/43 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5308.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.397×** | -14.6 | 3e-45 | 44/47 (AsPC-1, SW480, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.399×** | -7.6 | 1e-11 | 29/45 (AsPC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.419×** | -7.2 | 1e-10 | 28/44 (AsPC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.658×** | -6.6 | 6e-09 | 27/47 (HT-29, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.660×** | -6.5 | 7e-09 | 24/48 (HT-29, A498, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.532×** | -5.2 | 2e-05 | 19/46 (AsPC-1, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.707×** | -5.1 | 2e-05 | 20/48 (Hs 766T, SK-MEL-2, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.539×** | -5.1 | 3e-05 | 17/48 (A549, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.799×** | -5.0 | 4e-05 | 18/48 (H4, A498, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.552×** | -4.9 | 6e-05 | 17/43 (AsPC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.651×** | -4.6 | 2e-04 | 18/48 (Hs 766T, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -3.8 | 0.007 | 17/48 (AsPC-1, PANC-1, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.786×** | -3.6 | 0.012 | 14/29 (HT-29, SW 900, …) | rises with dose | composition shift |
| [[EX229 (drug)]] 0.5 µM |  | **0.716×** | -3.6 | 0.015 | 9/47 (H4, HT-29, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.804×** | -3.4 | 0.024 | 16/45 (HT-29, Hs 766T, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.728×** | -3.4 | 0.025 | 13/48 (SW 1271, SW 900, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.796×** | -3.3 | 0.031 | 12/45 (hTERT-HPNE, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.811×** | -3.2 | 0.045 | 12/47 (HCT15, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5308. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.61 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.19× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 27.6 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.150× (z -12.9) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0837× (z -8.8) |
| [[SW480 (line)]] | alt | 26.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.99× (z +9.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.269× (z -11.7) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 11.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.74× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 13.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +11.3) | — |
| [[A498 (line)]] | wt | 16.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.37× (z +8.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.266× (z -9.4) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 8.86 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.46× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 21.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 28.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H2030 (line)]] | alt | 16.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 20.5 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.171× (z -9.8) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[NCI-H1792 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0934× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[NCI-H23 (line)]] | alt | 16.7 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.204× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 9.48 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0704× (z -16.7) ⚠ transcription drop; cell-cycle shift, explains ~40% of this change |
| [[RPMI-7951 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.102× (z -10.0) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 8.98 | 0 | 1 | — | [[Demeclocycline (drug)]] 0.5 µM 0.0683× (z -9.1) |
| [[A-172 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5308), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTMR14]] | +0.75 | +0.68 / +0.69 | both halves | 7e-06 | same gene group; pathway: PI Metabolism |
| [[OTUD5]] | +0.73 | +0.75 / +0.80 | both halves | 7e-06 |  |
| [[MEF2D]] | +0.70 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ABTB1]] | +0.70 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[SPSB3]] | +0.69 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[FBXO33]] | +0.68 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[MOB2]] | +0.68 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[MAPKAPK2]] | +0.66 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[LINC01881]] | +0.64 | +0.44 / +0.70 | both halves | 3e-05 |  |
| [[WIPI2]] | +0.63 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[FBXO25]] | +0.63 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[ADIPOR1]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCFC2]] | -0.58 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[ZNF280D]] | -0.57 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[FAM169A]] | -0.56 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[YTHDC2]] | -0.56 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[SUCLG2]] | -0.55 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[PHACTR2]] | -0.54 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[AFG1L]] | -0.53 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[RAB11FIP2]] | -0.52 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[RBM26]] | -0.52 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[THUMPD2]] | -0.52 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[MYLK-AS1]] | -0.52 | -0.49 / -0.37 | both halves | 7e-05 |  |
| [[SLC16A9]] | -0.52 | -0.44 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.672). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.2, -43.7); signed map (-19.8, 11.6). **Vector** length 95.5, 21.0% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +16.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +13.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +17.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.6 | +12.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.3 | +6.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +5.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.6 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.9 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.8 | -14.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.9 | -6.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.8 | -7.6 |
|  | [[EX229 (drug)]] 5 µM |  | -5.3 | -5.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.2 | -7.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.1 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | inositol polyphosphate-5-phosphatase K |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:1,494,577-1,516,742 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SKIP |
| Gene groups (HGNC) | Phosphoinositide phosphatases |
| Reactome | 4 pathways, smallest: Synthesis of PIPs at the plasma membrane; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BT40](https://www.uniprot.org/uniprotkb/Q9BT40) (Inositol polyphosphate 5-phosphatase K):

> Inositol 5-phosphatase which acts on inositol 1,4,5-trisphosphate, inositol 1,3,4,5-tetrakisphosphate, phosphatidylinositol 4,5-bisphosphate and phosphatidylinositol 3,4,5-trisphosphate. Has 6-fold higher affinity for phosphatidylinositol 4,5-bisphosphate than for inositol 1,4,5-trisphosphate. Negatively regulates assembly of the actin cytoskeleton. Controls insulin-dependent glucose uptake among inositol 3,4,5-trisphosphate phosphatases; therefore, is the specific regulator for insulin …

**Summary**, from NCBI Gene [51763](https://www.ncbi.nlm.nih.gov/gene/51763):

> This gene encodes a protein with 5-phosphatase activity toward polyphosphate inositol. The protein localizes to the cytosol in regions lacking actin stress fibers. It is thought that this protein may negatively regulate the actin cytoskeleton. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:33882](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33882) · Entrez [51763](https://www.ncbi.nlm.nih.gov/gene/51763) · UniProt [Q9BT40](https://www.uniprot.org/uniprotkb/Q9BT40) · Ensembl [ENSG00000132376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132376)

## Data

Gene col 5308: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5308); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5308, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5308]; `tensor/DDL_lfc|DDL_z.npy` [5308]; `embed/gene_vectors.npy` [5308]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5308 or target_col == 5308). Every well: [[INPP5K — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INPP5K.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

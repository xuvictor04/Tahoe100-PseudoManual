---
symbol: "PIK3IP1"
type: "gene"
col: 1866
ensembl_id: "ENSG00000100100"
name: "phosphoinositide-3-kinase interacting protein 1"
location: "22q12.2"
module: 69
arm: "+"
pooled_cpm: 7.34
n_lines_expressing: 42
n_dd_up: 18
n_dd_down: 28
n_dd_up_clean: 16
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# PIK3IP1

*phosphoinositide-3-kinase interacting protein 1* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.60× (z +18.9, q 0e+00, up in 28 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.256× (z -14.2, q 5e-43, down in 34 of 39 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.270× (z -7.1, q 3e-10, down in 24 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEURL3]] (+0.69, fdr 7e-06), [[CREBRF]] (+0.68, fdr 7e-06), [[OPTN]] (+0.67, fdr 7e-06); moves opposite to [[RNGTT]] (-0.67, fdr 7e-06), [[EIPR1]] (-0.67, fdr 7e-06), [[POLR1A]] (-0.62, fdr 7e-06).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NR3C1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[XRCC5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1866.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.60×** | +18.9 | 0e+00 | 28/34 (SW1417, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +8.7 | 9e-16 | 18/32 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.35×** | +8.6 | 2e-15 | 27/38 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.62×** | +5.0 | 7e-05 | 15/39 (Hs 766T, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +4.2 | 0.004 | 8/31 (A-172, KATO III, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.005 | 12/39 (KATO III, Hs 766T, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.006 | 12/37 (Hs 766T, BT-474, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.006 | 14/39 (hTERT-HPNE, SNU-1, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.015 | 9/39 (HT-29, NCI-H23, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.015 | 12/39 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +3.6 | 0.020 | 6/26 (NCI-H1573, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.020 | 9/38 (HOP62, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.33×** | +3.3 | 0.039 | 5/39 (Hs 766T, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Berbamine (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.070 | 8/39 (SNU-423, HT-29, …) | top dose only |  |
| [[Alpelisib (drug)]] 5 µM |  | **1.75×** | +3.1 | 0.079 | 5/25 (Hs 766T, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.079 | 10/32 (Hs 766T, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.097 | 6/37 (Hs 766T, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1866.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.256×** | -14.2 | 5e-43 | 34/39 (NCI-H1792, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.270×** | -7.1 | 3e-10 | 24/31 (NCI-H1792, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.342×** | -5.9 | 9e-07 | 22/34 (AsPC-1, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.358×** | -5.6 | 3e-06 | 16/31 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.634×** | -4.7 | 2e-04 | 17/39 (SW 1271, RKO, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.636×** | -4.7 | 2e-04 | 20/38 (Panc 03.27, SNU-423, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.643×** | -4.6 | 4e-04 | 14/39 (A549, Hs 766T, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.561×** | -4.3 | 0.001 | 13/39 (PANC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **0.662×** | -4.3 | 0.001 | 14/37 (NCI-H1573, NCI-H2347, …) | two highest doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.668×** | -4.2 | 0.002 | 12/39 (HCT15, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.675×** | -4.1 | 0.002 | 16/39 (NCI-H2347, PANC-1, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.662×** | -4.0 | 0.003 | 10/36 (Hs 766T, NCI-H1573, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.683×** | -4.0 | 0.003 | 13/38 (COLO 205, A549, …) | all doses, flat |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.688×** | -3.9 | 0.004 | 11/39 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.503×** | -3.7 | 0.007 | 16/31 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.704×** | -3.6 | 0.010 | 15/39 (CFPAC-1, A-172, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.706×** | -3.6 | 0.010 | 12/39 (SW48, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.54 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1866. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 19.3 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +12.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.172× (z -11.9) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.0842× (z -8.8) |
| [[A549 (line)]] | wt | 7.19 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0849× (z -9.1) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 5.57 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +13.4) | — |
| [[NCI-H1792 (line)]] | alt | 15.6 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0928× (z -11.9) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0385× (z -8.6) |
| [[PANC-1 (line)]] | alt | 11.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.188× (z -9.6) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 19.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.38× (z +16.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.169× (z -10.2) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 4.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +13.0) | — |
| [[AsPC-1 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.123× (z -9.5) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0342× (z -16.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 3.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 3.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.96× (z +10.5) | — |
| [[HepG2_C3A (line)]] | wt | 18.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 3.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +11.5) | — |
| [[Hs 766T (line)]] | wt | 31.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.147× (z -9.9) |
| [[HT-29 (line)]] | alt | 5.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.53× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 8.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 1.94 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0322× (z -13.9) |
| [[SNU-423 (line)]] | alt | 19.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.186× (z -9.2) |
| [[A-427 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.63 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1866), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEURL3]] | +0.69 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[CREBRF]] | +0.68 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[OPTN]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[ZBTB10]] | +0.66 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[ABCA5]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[TXNDC16]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[STAP2]] | +0.63 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[CYLD]] | +0.63 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[TCP11L2]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[BMF]] | +0.63 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[STARD10]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[NINJ1]] | +0.62 | +0.66 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNGTT]] | -0.67 | -0.71 / -0.68 | both halves | 7e-06 |  |
| [[EIPR1]] | -0.67 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[POLR1A]] | -0.62 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[PSMD1]] | -0.61 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[POP1]] | -0.60 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[MRPS27]] | -0.60 | -0.58 / -0.59 | both halves | 8e-06 |  |
| [[NUP155]] | -0.58 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[TOMM40]] | -0.57 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[CCT3]] | -0.57 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[COX10]] | -0.57 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[NOL10]] | -0.57 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[EIF2S1]] | -0.56 | -0.55 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers PIK3IP1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.9% of all compounds | 0.079 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XRCC5]] | B | PIK3IP1 activity lowers XRCC5's level | lines that do not express PIK3IP1 (8) vs lines expressing it (42) | 1.12× higher at baseline in the lines without PIK3IP1 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.709). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.3, -39.0); signed map (-10.0, 11.8). **Vector** length 92.4, 21.2% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +18.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +8.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.1 | +8.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.8 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +4.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +2.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.1 | -14.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.6 | -7.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.2 | -3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.2 | -5.9 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | phosphoinositide-3-kinase interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:31,281,594-31,292,534 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HGFL, MGC17330, TrIP |
| Gene groups (HGNC) | Kringle domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FE7](https://www.uniprot.org/uniprotkb/Q96FE7) (Phosphoinositide-3-kinase-interacting protein 1):

> Negative regulator of hepatic phosphatidylinositol 3-kinase (PI3K) activity.

**Summary**, from NCBI Gene [113791](https://www.ncbi.nlm.nih.gov/gene/113791):

> Enables phosphatidylinositol 3-kinase inhibitor activity. Involved in negative regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction. Predicted to be located in plasma membrane. Predicted to be active in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24942](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24942) · Entrez [113791](https://www.ncbi.nlm.nih.gov/gene/113791) · UniProt [Q96FE7](https://www.uniprot.org/uniprotkb/Q96FE7) · Ensembl [ENSG00000100100](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100100)

## Data

Gene col 1866: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1866); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1866, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1866]; `tensor/DDL_lfc|DDL_z.npy` [1866]; `embed/gene_vectors.npy` [1866]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1866 or target_col == 1866). Every well: [[PIK3IP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIK3IP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

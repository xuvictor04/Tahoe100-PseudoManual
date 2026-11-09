---
symbol: "PLIN2"
type: "gene"
col: 7228
ensembl_id: "ENSG00000147872"
name: "perilipin 2"
location: "9p22.1"
module: 79
arm: "+"
pooled_cpm: 95.6
n_lines_expressing: 33
n_dd_up: 15
n_dd_down: 21
n_dd_up_clean: 15
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# PLIN2

*perilipin 2* — 9p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (none with an alert); the strongest is [[Mifepristone (drug)]] 0.5 µM: 2.74× (z +8.7, q 1e-15, up in 29 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.210× (z -13.5, q 9e-39, down in 30 of 31 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DEPP1]] (+0.60, fdr 2e-05), [[ZNF395]] (+0.58, fdr 1e-05), [[BNIP3]] (+0.58, fdr 2e-05); moves opposite to [[CCDC9B]] (-0.44, fdr 1e-04), [[FAM20B]] (-0.43, fdr 4e-04), [[MAPK9]] (-0.43, fdr 3e-04).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ABCA1]] → it (grade B ⚠); 7 go from it, the strongest it → [[ABCA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, none with an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7228.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mifepristone (drug)]] 0.5 µM |  | **2.74×** | +8.7 | 1e-15 | 29/31 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Mifepristone (drug)]] 5 µM |  | **2.79×** | +8.5 | 4e-15 | 26/31 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[Bexarotene (drug)]] 5 µM |  | **2.19×** | +6.8 | 2e-09 | 27/31 (LS 180, SW1417, …) | all doses, stronger at high dose |  |
| [[Mifepristone (drug)]] 0.05 µM |  | **2.11×** | +6.0 | 3e-07 | 28/31 (SNU-423, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Rosiglitazone (drug)]] 5 µM |  | **2.03×** | +5.9 | 4e-07 | 27/31 (Hs 766T, SW480, …) | rises with dose |  |
| [[Econazole (drug)]] 5 µM |  | **1.81×** | +5.2 | 2e-05 | 25/31 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | **1.47×** | +4.7 | 2e-04 | 23/32 (LS 180, SW480, …) | top dose only |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **1.72×** | +4.7 | 2e-04 | 21/31 (LS 180, SW1417, …) | all doses, stronger at high dose |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +4.3 | 9e-04 | 21/31 (SNU-423, COLO 205, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.62×** | +4.2 | 0.002 | 22/31 (H4, NCI-H2347, …) | inconsistent across doses |  |
| [[Pioglitazone (drug)]] 5 µM |  | **1.60×** | +4.1 | 0.003 | 22/31 (COLO 205, Hs 766T, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.009 | 22/31 (HepG2/C3A, A549, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.074 | 16/31 (HOP62, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Bexarotene (drug)]] 0.05 µM |  | **1.43×** | +3.1 | 0.074 | 15/31 (LS 180, SW1417, …) | all doses, stronger at high dose |  |
| [[Rosiglitazone (drug)]] 0.5 µM |  | **1.41×** | +3.0 | 0.099 | 16/31 (Hs 766T, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7228.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.210×** | -13.5 | 9e-39 | 30/31 (C32, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.245×** | -12.2 | 2e-31 | 30/31 (SW 900, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.280×** | -11.0 | 7e-26 | 30/31 (SW 900, C32, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.434×** | -10.2 | 2e-22 | 29/31 (H4, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.406×** | -7.8 | 8e-13 | 30/31 (SW 900, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.409×** | -7.4 | 9e-12 | 27/31 (H4, C32, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.480×** | -5.9 | 4e-07 | 20/28 (AN3 CA, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.513×** | -5.8 | 5e-07 | 21/30 (C32, H4, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.521×** | -5.4 | 4e-06 | 18/31 (C32, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.552×** | -5.1 | 2e-05 | 23/31 (HepG2/C3A, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.557×** | -4.9 | 6e-05 | 16/28 (C32, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.625×** | -4.1 | 0.002 | 22/31 (C32, SW 900, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.880× | -3.8 | 0.005 | 5/33 (A549, H4, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.632×** | -3.8 | 0.007 | 21/31 (C32, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.641×** | -3.7 | 0.008 | 19/31 (RPMI-7951, SW 900, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.661×** | -3.6 | 0.012 | 21/32 (SW 900, COLO 205, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.466×** | -3.5 | 0.018 | 20/31 (SW 900, C32, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.470×** | -3.4 | 0.019 | 24/32 (SW 900, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.472×** | -3.4 | 0.019 | 17/32 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.473×** | -3.4 | 0.019 | 20/31 (MIA PaCa-2, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.57 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7228. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 280 | 0 | 13 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0590× (z -20.9) |
| [[SW 900 (line)]] | alt | 420 | 0 | 13 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0501× (z -20.2) |
| [[SNU-423 (line)]] | alt | 449 | 2 | 10 (6 ⚠) | [[Mifepristone (drug)]] 0.5 µM 4.93× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.133× (z -14.2) |
| [[H4 (line)]] | wt | 168 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -18.7) |
| [[RPMI-7951 (line)]] | alt | 193 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 185 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0823× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.199× (z -16.5) |
| [[NCI-H1792 (line)]] | alt | 241 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0831× (z -15.7) |
| [[hTERT-HPNE (line)]] | wt | 131 | 0 | 7 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.117× (z -14.1) |
| [[PANC-1 (line)]] | alt | 49.3 | 1 | 6 (1 ⚠) | [[Rosiglitazone (drug)]] 5 µM 3.57× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -18.2) |
| [[CFPAC-1 (line)]] | alt | 100 | 2 | 4 (1 ⚠) | [[Mifepristone (drug)]] 5 µM 4.83× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.146× (z -13.3) |
| [[HOP62 (line)]] | alt | 96.4 | 3 | 3 | [[Mifepristone (drug)]] 5 µM 5.72× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.187× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 83.3 | 2 | 4 (1 ⚠) | [[Mifepristone (drug)]] 0.5 µM 4.14× (z +12.2) | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 60.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -17.3) |
| [[SW480 (line)]] | alt | 123 | 2 | 3 | [[Rosiglitazone (drug)]] 5 µM 4.12× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.205× (z -11.8) |
| [[HepG2_C3A (line)]] | wt | 383 | 1 | 3 | [[Mifepristone (drug)]] 0.5 µM 4.37× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -10.1) |
| [[Hs 766T (line)]] | wt | 56.8 | 2 | 1 | [[Rosiglitazone (drug)]] 5 µM 5.96× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.210× (z -9.4) |
| [[J82 (line)]] | alt | 268 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -13.1) |
| [[SW1417 (line)]] | alt | 54.0 | 3 | 0 | [[Mifepristone (drug)]] 0.5 µM 3.69× (z +9.8) | — |
| [[A549 (line)]] | wt | 47.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -10.8) |
| [[COLO 205 (line)]] | alt | 213 | 2 | 0 | [[Rosiglitazone (drug)]] 5 µM 5.06× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 101 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -10.5) |
| [[LS 180 (line)]] | wt | 37.7 | 2 | 0 | [[Bexarotene (drug)]] 5 µM 5.64× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 25.5 | 2 | 0 | [[Mifepristone (drug)]] 5 µM 8.32× (z +11.1) | — |
| [[AN3 CA (line)]] | alt | 71.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -10.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 63.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -8.5) |
| [[A-172 (line)]] | wt | 6.58 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.64 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 311 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.93 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 23.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.98 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.10 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.46 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.32 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 18.8 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.76 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.70 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.18 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.75 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7228), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DEPP1]] | +0.60 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[ZNF395]] | +0.58 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[BNIP3]] | +0.58 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[ADM]] | +0.55 | +0.42 / +0.60 | both halves | 4e-05 | pathway: HALLMARK_HYPOXIA |
| [[IRF2BP2]] | +0.54 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[NFIL3]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[TMEM45A]] | +0.54 | +0.46 / +0.62 | both halves | 3e-05 | pathway: HALLMARK_HYPOXIA |
| [[PPP1R3B]] | +0.53 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[RRAGA]] | +0.53 | +0.50 / +0.55 | both halves | 1e-05 | pathway: Autophagy |
| [[ZMYND8]] | +0.52 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ZFP36L1]] | +0.52 | +0.36 / +0.55 | both halves | 1e-04 |  |
| [[LDHA]] | +0.52 | +0.42 / +0.58 | both halves | 4e-05 | pathway: HALLMARK_HYPOXIA |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC9B]] | -0.44 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[FAM20B]] | -0.43 | -0.24 / -0.44 | both halves | 4e-04 |  |
| [[MAPK9]] | -0.43 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[NUP93]] | -0.42 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[MACROH2A1]] | -0.42 | -0.33 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA1]] | B | ABCA1 activity raises PLIN2's level | lines that do not express ABCA1 (20) vs lines expressing it (30) | 3.95× lower at baseline in the lines without ABCA1 | 0.013 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7 |
| [[LOX]] | B | LOX activity raises PLIN2's level | lines that do not express LOX (31) vs lines expressing it (19) | 3.64× lower at baseline in the lines without LOX | 0.038 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA1]] | B | PLIN2 activity raises ABCA1's level | lines that do not express PLIN2 (17) vs lines expressing it (33) | 3.82× lower at baseline in the lines without PLIN2 | 0.013 | ⚠ within organs, on part of the lines; also absent: AXL, UBE2Q2P13, SLC2A3 |
| [[NFIL3]] | B | PLIN2 activity raises NFIL3's level | lines that do not express PLIN2 (17) vs lines expressing it (33) | 1.67× lower at baseline in the lines without PLIN2 | 0.024 | ⚠ within organs, on part of the lines; also absent: AXL, UBE2Q2P13, SLC2A3 |
| [[SNAPC1]] | B | PLIN2 activity raises SNAPC1's level | lines that do not express PLIN2 (17) vs lines expressing it (33) | 2.01× lower at baseline in the lines without PLIN2 | 0.025 | ⚠ within organs, on part of the lines; also absent: AXL, UBE2Q2P13, SLC2A3 |
| [[ADM]] | B | PLIN2 activity raises ADM's level | lines that do not express PLIN2 (17) vs lines expressing it (33) | 2.50× lower at baseline in the lines without PLIN2 | 0.032 | ⚠ within organs, on part of the lines; also absent: AXL, UBE2Q2P13, SLC2A3 |
| [[PPP1R3C]] | B | PLIN2 activity raises PPP1R3C's level | lines that do not express PLIN2 (17) vs lines expressing it (33) | 2.42× lower at baseline in the lines without PLIN2 | 0.066 | ⚠ within organs, on part of the lines; also absent: AXL, UBE2Q2P13, SLC2A3 |
| [[MACROH2A1]] | B | PLIN2 activity lowers MACROH2A1's level | lines that do not express PLIN2 (17) vs lines expressing it (33) | 1.28× higher at baseline in the lines without PLIN2 | 0.082 | ⚠ within organs, on part of the lines; also absent: AXL, UBE2Q2P13, SLC2A3 |
| [[RRAGA]] | B | PLIN2 activity raises RRAGA's level | lines that do not express PLIN2 (17) vs lines expressing it (33) | 1.40× lower at baseline in the lines without PLIN2 | 0.086 | ⚠ within organs, on part of the lines; also absent: AXL, UBE2Q2P13, SLC2A3 |

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.533). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.2, -14.7); signed map (-33.6, 27.8). **Vector** length 110, 31.1% of its response variance represented; |z| ≥ 3 in 1,131 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | -1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.9 | +1.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -6.0 | -5.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.3 | -7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -5.2 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.7 | -5.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.8 | -2.4 |
|  | [[vincristine (drug)]] 5 µM |  | -2.0 | -0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -0.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | perilipin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p22.1 — chr9:19,108,375-19,149,290 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ADRP; previously ADFP |
| Gene groups (HGNC) | Perilipins |
| Hallmark sets | IL2_STAT5_SIGNALING, HYPOXIA, ADIPOGENESIS |
| Reactome | 14 pathways, smallest: Lipophagy; Chaperone Mediated Autophagy; Late endosomal microautophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99541](https://www.uniprot.org/uniprotkb/Q99541) (Perilipin-2):

> Structural component of lipid droplets, which is required for the formation and maintenance of lipid storage droplets.

**Summary**, from NCBI Gene [123](https://www.ncbi.nlm.nih.gov/gene/123):

> The protein encoded by this gene belongs to the perilipin family, members of which coat intracellular lipid storage droplets. This protein is associated with the lipid globule surface membrane material, and maybe involved in development and maintenance of adipose tissue. However, it is not restricted to adipocytes as previously thought, but is found in a wide range of cultured cell lines, including fibroblasts, endothelial and epithelial cells, and tissues, such as lactating mammary gland, …

**Accessions** — [HGNC:248](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:248) · Entrez [123](https://www.ncbi.nlm.nih.gov/gene/123) · UniProt [Q99541](https://www.uniprot.org/uniprotkb/Q99541) · Ensembl [ENSG00000147872](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147872)

## Data

Gene col 7228: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7228); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7228, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7228]; `tensor/DDL_lfc|DDL_z.npy` [7228]; `embed/gene_vectors.npy` [7228]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7228 or target_col == 7228). Every well: [[PLIN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLIN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

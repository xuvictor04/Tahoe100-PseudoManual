---
symbol: "ITM2C"
type: "gene"
col: 5776
ensembl_id: "ENSG00000135916"
name: "integral membrane protein 2C"
location: "2q37.1"
module: 50
arm: "+"
pooled_cpm: 17.51
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 17
n_dd_up_clean: 9
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# ITM2C

*integral membrane protein 2C* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.74× (z +15.3, q 0e+00, up in 37 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.69× (z +11.3, q 3e-27, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.543× (z -13.0, q 5e-36, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGPAT1]] (+0.73, fdr 7e-06), [[CLSTN1]] (+0.72, fdr 7e-06), [[BSG]] (+0.71, fdr 7e-06); moves opposite to [[DNAJC2]] (-0.67, fdr 7e-06), [[NSRP1]] (-0.66, fdr 1e-05), [[NME6]] (-0.63, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5776.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.74×** | +15.3 | 0e+00 | 37/40 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.58×** | +13.8 | 6e-41 | 29/30 (A-172, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.40×** | +12.3 | 2e-32 | 29/35 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.69×** | +11.3 | 3e-27 | 36/47 (J82, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.86×** | +9.4 | 6e-19 | 37/47 (PANC-1, SW480, …) | all doses, flat | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.47×** | +8.3 | 1e-14 | 37/47 (A549, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +8.0 | 8e-14 | 35/47 (SW480, LS 180, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +8.0 | 1e-13 | 36/45 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.64×** | +7.5 | 4e-12 | 33/47 (PANC-1, NCI-H460, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.64×** | +7.5 | 4e-12 | 34/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +7.2 | 4e-11 | 34/47 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~22% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +6.4 | 7e-09 | 26/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.5 | 2e-06 | 22/47 (HOP62, A-172, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +5.0 | 3e-05 | 24/47 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.86×** | +4.9 | 3e-05 | 15/47 (PANC-1, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.020 | 12/47 (J82, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.063 | 7/47 (C-33 A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5776.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.543×** | -13.0 | 5e-36 | 39/46 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.462×** | -9.9 | 1e-20 | 33/46 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.629×** | -7.0 | 5e-10 | 29/47 (LoVo, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.675×** | -5.7 | 2e-06 | 28/47 (HOP62, HepG2/C3A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.717×** | -5.0 | 6e-05 | 21/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.794×** | -4.9 | 9e-05 | 17/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.747×** | -4.4 | 9e-04 | 18/47 (LOX-IMVI, LoVo, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.581×** | -4.3 | 0.001 | 16/47 (SK-MEL-2, SNU-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.583×** | -4.3 | 0.001 | 14/47 (HT-29, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.640×** | -3.5 | 0.024 | 12/47 (SHP-77, SW 1271, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.725×** | -3.5 | 0.028 | 10/47 (NCI-H23, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM |  | **0.798×** | -3.4 | 0.034 | 13/47 (A498, LoVo, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.795×** | -3.3 | 0.050 | 15/47 (SHP-77, SNU-423, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.809×** | -3.2 | 0.059 | 17/47 (SHP-77, SW 1271, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.672×** | -3.1 | 0.065 | 12/46 (COLO 205, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.674×** | -3.1 | 0.067 | 15/47 (PANC-1, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.813×** | -3.0 | 0.090 | 15/47 (HCT15, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5776. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 39.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -15.2) |
| [[HS-578T (line)]] | alt | 27.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.17× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -9.2) |
| [[PANC-1 (line)]] | alt | 20.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -11.4) |
| [[A-172 (line)]] | wt | 17.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.20× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A498 (line)]] | wt | 13.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HEC-1-A (line)]] | alt | 23.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LoVo (line)]] | wt | 24.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 21.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -15.2) |
| [[A-427 (line)]] | wt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -10.2) |
| [[AN3 CA (line)]] | alt | 28.5 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0838× (z -9.6) |
| [[H4 (line)]] | wt | 31.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -11.3) |
| [[HCT15 (line)]] | alt | 26.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -9.8) |
| [[HT-29 (line)]] | alt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -10.4) |
| [[J82 (line)]] | alt | 9.88 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.00× (z +9.3) | — |
| [[KATO III (line)]] | alt | 16.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.81× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H460 (line)]] | wt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 32.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -10.5) |
| [[SNU-1 (line)]] | wt | 20.2 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0559× (z -11.3) |
| [[SW 900 (line)]] | alt | 41.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW480 (line)]] | alt | 18.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.03× (z +8.6) | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5776), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGPAT1]] | +0.73 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[CLSTN1]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[BSG]] | +0.71 | +0.76 / +0.58 | both halves | 7e-06 |  |
| [[TMEM30A]] | +0.68 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[GM2A]] | +0.68 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[CNPY3]] | +0.68 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[GGH]] | +0.67 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[NAGA]] | +0.66 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[CREG1]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[APLP1]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[FKBP1A]] | +0.64 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[GUSB]] | +0.63 | +0.69 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC2]] | -0.67 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[NSRP1]] | -0.66 | -0.70 / -0.53 | both halves | 1e-05 |  |
| [[NME6]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[ATF4]] | -0.61 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[ESF1]] | -0.60 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[ZNF286B]] | -0.60 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[EIF3J]] | -0.60 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[CRCP]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[TIMM44]] | -0.59 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[EIF5B]] | -0.58 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[FNBP4]] | -0.58 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[CCDC137]] | -0.58 | -0.58 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ITM2C's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IGF2]] | B | IGF2 activity raises ITM2C's level | lines that do not express IGF2 (32) vs lines expressing it (18) | 1.52× lower at baseline in the lines without IGF2 | 0.063 | ⚠ within organs, on part of the lines; also absent: ZNF334, ENSG00000239268, CARMN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.772). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.7, -21.5); signed map (-28.6, -37.7). **Vector** length 93.8, 21.0% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Extracellular matrix organization* (reactome, mean cos +0.53 to 12); *Degradation of the extracellular matrix* (reactome, mean cos +0.55 to 7); *epithelial mesenchymal transition* (hallmark, mean cos +0.54 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.9 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +4.3 | +15.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.8 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.2 | -9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.7 | -13.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.7 | -3.0 |
|  | [[EX229 (drug)]] 5 µM |  | -3.7 | -4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.4 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.1 | -4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | integral membrane protein 2C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:230,864,639-230,879,248 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BRI3, E25, hRPC.1050_D_4, ITM3, BRICD2C |
| Gene groups (HGNC) | BRICHOS domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQX7](https://www.uniprot.org/uniprotkb/Q9NQX7) (Integral membrane protein 2C):

> Negative regulator of amyloid-beta peptide production. May inhibit the processing of APP by blocking its access to alpha- and beta-secretase. Binding to the beta-secretase-cleaved APP C-terminal fragment is negligible, suggesting that ITM2C is a poor gamma-secretase cleavage inhibitor. May play a role in TNF-induced cell death and neuronal differentiation (By similarity).

**Summary**, from NCBI Gene [81618](https://www.ncbi.nlm.nih.gov/gene/81618):

> Enables amyloid-beta binding activity. Involved in negative regulation of neuron projection development and neuron differentiation. Located in several cellular components, including Golgi apparatus; lysosome; and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:6175](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6175) · Entrez [81618](https://www.ncbi.nlm.nih.gov/gene/81618) · UniProt [Q9NQX7](https://www.uniprot.org/uniprotkb/Q9NQX7) · Ensembl [ENSG00000135916](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135916)

## Data

Gene col 5776: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5776); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5776, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5776]; `tensor/DDL_lfc|DDL_z.npy` [5776]; `embed/gene_vectors.npy` [5776]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5776 or target_col == 5776). Every well: [[ITM2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITM2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

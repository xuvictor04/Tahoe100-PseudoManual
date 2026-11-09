---
symbol: "ARF3"
type: "gene"
col: 5538
ensembl_id: "ENSG00000134287"
name: "ARF GTPase 3"
location: "12q13.12"
module: 29
arm: "+"
pooled_cpm: 58.5
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# ARF3

*ARF GTPase 3* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.64× (z +18.5, q 0e+00, up in 47 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.18× (z +7.7, q 2e-12, up in 42 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.671× (z -10.8, q 2e-24, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGPAT1]] (+0.70, fdr 7e-06), [[PCNX3]] (+0.69, fdr 7e-06), [[RPSA]] (+0.68, fdr 8e-06); moves opposite to [[AK6]] (-0.69, fdr 7e-06), [[ATF4]] (-0.69, fdr 7e-06), [[NKAP]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5538.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.64×** | +18.5 | 0e+00 | 47/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +14.6 | 1e-45 | 41/43 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +10.8 | 9e-25 | 39/45 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +7.7 | 2e-12 | 42/49 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +5.4 | 8e-06 | 30/48 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +5.2 | 2e-05 | 25/48 (HEC-1-A, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.0 | 0.005 | 0/49 | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.8 | 0.009 | 14/48 (SNU-1, SW480, …) | inconsistent across doses | position effect removed |
| [[Folic acid (drug)]] 5 µM |  | 1.15× | +3.8 | 0.010 | 16/48 (H4, A498, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.19× | +3.3 | 0.064 | 18/48 (LoVo, NCI-H2030, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, none with an alert; shown: the 15 strongest. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5538.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.671×** | -10.8 | 2e-24 | 36/48 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.664×** | -7.8 | 1e-12 | 34/48 (A-427, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.727×** | -6.1 | 2e-07 | 32/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.723×** | -6.0 | 3e-07 | 29/48 (COLO 205, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.732×** | -5.6 | 2e-06 | 30/48 (SK-MEL-2, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.794×** | -4.4 | 9e-04 | 24/48 (SW 1088, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.834× | -3.5 | 0.036 | 21/48 (SK-MEL-2, KATO III, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.880× | -3.5 | 0.036 | 7/49 (COLO 205, PANC-1, …) | rises with dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 0.840× | -3.3 | 0.052 | 15/48 (H4, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.850× | -3.1 | 0.086 | 17/48 (SW 1088, Panc 03.27, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.846× | -3.1 | 0.086 | 14/47 (NCI-H23, SW1417, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.841× | -3.1 | 0.086 | 16/47 (H4, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.843× | -3.1 | 0.086 | 20/48 (A-427, A-172, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.852× | -3.1 | 0.086 | 16/48 (SW 1088, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.894× | -3.1 | 0.086 | 6/48 (HS-578T, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5538. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 63.4 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -12.1) |
| [[A-172 (line)]] | wt | 41.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -8.7) |
| [[A-427 (line)]] | wt | 95.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -22.6) |
| [[NCI-H23 (line)]] | alt | 116 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +14.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.461× (z -9.3) |
| [[PANC-1 (line)]] | alt | 43.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.03× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 61.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 58.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +11.4) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 65.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +11.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 34.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 60.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -10.3) |
| [[SW480 (line)]] | alt | 73.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +13.8) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 53.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 55.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 32.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +11.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 53.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +12.0) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 71.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 69.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.86× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 43.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.43× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 73.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 40.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 103 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -12.3) |
| [[A549 (line)]] | wt | 48.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +9.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 56.4 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.134× (z -9.6) |
| [[C32 (line)]] | wt | 44.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 56.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.33× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 47.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +9.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 37.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +10.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 65.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.299× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 59.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 84.0 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.239× (z -14.4) |
| [[SW 1271 (line)]] | alt | 66.3 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0714× (z -10.5) |
| [[SW48 (line)]] | wt | 48.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +8.7) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 50.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5538), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGPAT1]] | +0.70 | +0.61 / +0.71 | both halves | 7e-06 | pathway: Phospholipid metabolism |
| [[PCNX3]] | +0.69 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[RPSA]] | +0.68 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[FKBP1A]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[TMEM30A]] | +0.67 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[DHFR]] | +0.66 | +0.45 / +0.74 | both halves | 3e-05 |  |
| [[FKBP9]] | +0.66 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[GANAB]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[CCAR2]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[EMC1]] | +0.65 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[PABIR2]] | +0.65 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[PRPF8]] | +0.64 | +0.46 / +0.74 | both halves | 2e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AK6]] | -0.69 | -0.65 / -0.69 | both halves | 7e-06 |  |
| [[ATF4]] | -0.69 | -0.64 / -0.70 | both halves | 7e-06 |  |
| [[NKAP]] | -0.68 | -0.61 / -0.71 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | -0.67 | -0.52 / -0.74 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NACA4P]] ⚠ | -0.67 | -0.55 / -0.73 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CROCCP2-1]] | -0.65 | -0.65 / -0.66 | both halves | 7e-06 |  |
| [[EIF1B]] | -0.65 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[SNHG32]] | -0.64 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[FDX2]] | -0.63 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[ZKSCAN1]] | -0.63 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[SNHG7]] | -0.63 | -0.58 / -0.68 | both halves | 7e-06 |  |
| [[RSRC2]] | -0.63 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[RBMX2]] | -0.62 | -0.55 / -0.71 | both halves | 1e-05 |  |
| [[MRPS18C]] | -0.61 | -0.54 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises ARF3's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LGALS3BP]] | B | LGALS3BP activity lowers ARF3's level | lines that do not express LGALS3BP (7) vs lines expressing it (43) | 1.33× higher at baseline in the lines without LGALS3BP | 0.087 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.0, -24.4); signed map (-25.8, -39.2). **Vector** length 126, 34.2% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.9 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +18.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +14.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.6 | +5.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.7 | +2.5 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +2.6 | +2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.1 | -7.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.5 | -6.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.9 | -6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.2 | -2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.9 | -2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ARF GTPase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:48,935,723-48,957,487 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ARF GTPase family |
| Reactome | 13 pathways, smallest: Synthesis of PIPs at the Golgi membrane; PI Metabolism; COPI-dependent Golgi-to-ER retrograde traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [P61204](https://www.uniprot.org/uniprotkb/P61204) (ADP-ribosylation factor 3):

> GTP-binding protein that functions as an allosteric activator of the cholera toxin catalytic subunit, an ADP-ribosyltransferase. Involved in protein trafficking; may modulate vesicle budding and uncoating within the Golgi apparatus.

**Summary**, from NCBI Gene [377](https://www.ncbi.nlm.nih.gov/gene/377):

> ADP-ribosylation factor 3 (ARF3) is a member of the human ARF gene family. These genes encode small guanine nucleotide-binding proteins that stimulate the ADP-ribosyltransferase activity of cholera toxin and play a role in vesicular trafficking and as activators of phospholipase D. The gene products include 6 ARF proteins and 11 ARF-like proteins and constitute one family of the RAS superfamily. The ARF proteins are categorized as class I (ARF1, ARF2,and ARF3), class II (ARF4 and ARF5) and …

**Accessions** — [HGNC:654](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:654) · Entrez [377](https://www.ncbi.nlm.nih.gov/gene/377) · UniProt [P61204](https://www.uniprot.org/uniprotkb/P61204) · Ensembl [ENSG00000134287](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134287)

## Data

Gene col 5538: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5538); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5538, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5538]; `tensor/DDL_lfc|DDL_z.npy` [5538]; `embed/gene_vectors.npy` [5538]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5538 or target_col == 5538). Every well: [[ARF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "FNIP2"
type: "gene"
col: 587
ensembl_id: "ENSG00000052795"
name: "folliculin interacting protein 2"
location: "4q32.1"
module: 123
arm: "+"
pooled_cpm: 73.29
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 12
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# FNIP2

*folliculin interacting protein 2* — 4q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.72× (z +15.4, q 0e+00, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.473× (z -14.5, q 8e-45, down in 33 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.538× (z -12.5, q 2e-33, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[P2RY1]] (+0.48, fdr 6e-05), [[ARID5B]] (+0.48, fdr 5e-05), [[CAMSAP2]] (+0.47, fdr 5e-05); moves opposite to [[MARF1]] (-0.54, fdr 2e-05), [[PPP2R5C]] (-0.45, fdr 4e-05), [[PPM1F]] (-0.45, fdr 2e-04).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ABCA1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 587.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +15.4 | 0e+00 | 37/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.73×** | +10.6 | 1e-23 | 42/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +5.4 | 9e-06 | 23/46 (HOP62, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +5.4 | 9e-06 | 24/47 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **1.30×** | +5.4 | 1e-05 | 22/49 (RPMI-7951, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.62×** | +5.0 | 4e-05 | 25/49 (CFPAC-1, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.28×** | +4.8 | 1e-04 | 22/47 (COLO 205, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +4.6 | 2e-04 | 19/47 (SW 900, A498, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.53×** | +4.5 | 4e-04 | 19/47 (CFPAC-1, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.23×** | +4.2 | 0.001 | 21/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.017 | 12/48 (A-427, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.15× | +3.4 | 0.030 | 14/47 (HOP62, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.036 | 11/47 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 1.12× | +3.3 | 0.036 | 5/47 (COLO 205, J82, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.043 | 12/46 (AsPC-1, SW 900, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.043 | 13/46 (SK-MEL-2, SW 900, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 587.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.473×** | -14.5 | 8e-45 | 33/41 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.519×** | -13.2 | 3e-37 | 33/46 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.538×** | -12.5 | 2e-33 | 34/47 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.550×** | -12.0 | 5e-31 | 33/47 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.633×** | -7.8 | 8e-13 | 27/43 (C-33 A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.774×** | -7.3 | 3e-11 | 30/47 (C32, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.753×** | -5.5 | 3e-06 | 23/45 (A-172, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.785×** | -4.9 | 8e-05 | 27/47 (A-172, SNU-423, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.728×** | -4.6 | 3e-04 | 21/47 (HCT15, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **0.808×** | -4.3 | 0.001 | 19/46 (SW 900, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.819×** | -4.0 | 0.003 | 18/47 (KATO III, LoVo, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.827×** | -3.8 | 0.006 | 18/48 (J82, SNU-423, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.851× | -3.2 | 0.051 | 18/47 (A-172, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 587. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 181 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.278× (z -12.7) |
| [[COLO 205 (line)]] | alt | 311 | 4 | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 6.94× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.261× (z -11.1) |
| [[HOP62 (line)]] | alt | 57.5 | 3 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 19.2× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.382× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 150 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -15.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.290× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 147 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.319× (z -11.9) |
| [[C32 (line)]] | wt | 119 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.83× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.485× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 39.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +24.6) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -18.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 38.0 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +20.2) | — |
| [[SW480 (line)]] | alt | 42.7 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.429× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 95.2 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.556× (z -9.1) |
| [[J82 (line)]] | alt | 81.5 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.84× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -15.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 148 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.271× (z -9.9) |
| [[A-427 (line)]] | wt | 37.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -13.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 62.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -13.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 127 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 28.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.90× (z +20.3) | — |
| [[SK-MEL-2 (line)]] | alt | 88.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.86× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.130× (z -18.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 65.1 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.226× (z -10.1) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 68.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -13.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 36.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.91× (z +19.6) | — |
| [[NCI-H2030 (line)]] | alt | 33.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +14.8) | [[Pimozide (drug)]] 0.05 µM 0.369× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 47.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.9) | — |
| [[A498 (line)]] | wt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -9.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 31.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 52.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.6) | — |
| [[HepG2_C3A (line)]] | wt | 94.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -9.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 57.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +14.4) | — |
| [[LS 180 (line)]] | wt | 80.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.359× (z -9.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 69.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +11.4) | — |
| [[RPMI-7951 (line)]] | alt | 97.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.15× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 32.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -10.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 84.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -8.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 69.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 587), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P2RY1]] | +0.48 | +0.44 / +0.38 | both halves | 6e-05 |  |
| [[ARID5B]] | +0.48 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[CAMSAP2]] | +0.47 | +0.43 / +0.39 | both halves | 5e-05 |  |
| [[FOSL2]] | +0.47 | +0.41 / +0.38 | both halves | 7e-05 |  |
| [[GRIK4]] | +0.46 | +0.45 / +0.34 | both halves | 1e-04 |  |
| [[LITAF]] | +0.46 | +0.40 / +0.35 | both halves | 1e-04 |  |
| [[ETS2]] | +0.46 | +0.40 / +0.39 | both halves | 5e-05 |  |
| [[ABCA1]] | +0.45 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[MEIS2]] | +0.45 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[PLXNC1]] | +0.45 | +0.47 / +0.30 | both halves | 2e-04 |  |
| [[KMO]] | +0.44 | +0.36 / +0.41 | both halves | 1e-04 |  |
| [[TBX3]] | +0.44 | +0.37 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARF1]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[PPP2R5C]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[PPM1F]] | -0.45 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[FBXW2]] | -0.43 | -0.44 / -0.26 | both halves | 3e-04 |  |
| [[PCMTD2]] | -0.43 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[WRN]] | -0.42 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[TRABD]] | -0.42 | -0.45 / -0.24 | both halves | 5e-04 |  |
| [[ETV5]] | -0.41 | -0.37 / -0.38 | both halves | 7e-05 |  |
| [[BRAT1]] | -0.41 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[BCL7C]] | -0.41 | -0.46 / -0.23 | both halves | 5e-04 |  |
| [[NBPF3]] | -0.41 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[CRLF3]] | -0.41 | -0.44 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA1]] | B | ABCA1 activity raises FNIP2's level | lines that do not express ABCA1 (20) vs lines expressing it (30) | 1.52× lower at baseline in the lines without ABCA1 | 0.022 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7 |
| [[IFIT2]] | B | IFIT2 activity raises FNIP2's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without IFIT2 | 0.026 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[IFIT3]] | B | IFIT3 activity raises FNIP2's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 1.87× lower at baseline in the lines without IFIT3 | 0.039 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[PLOD2]] | B | PLOD2 activity raises FNIP2's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 1.63× lower at baseline in the lines without PLOD2 | 0.046 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[ABCA1]] | B | ABCA1 activity strengthens FNIP2's drug response | lines that do not express ABCA1 (20) vs lines expressing it (28) | the lines without ABCA1 respond 0.63× as strongly (z diff +1.74); strongest at Panobinostat 0.5 µM: 0.77x vs 0.47x (z diff +3.7) | 0.069 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7; target measured in part of the lines; artifact flags |
| [[CCL28]] | B | CCL28 activity raises FNIP2's level | lines that do not express CCL28 (24) vs lines expressing it (26) | 1.54× lower at baseline in the lines without CCL28 | 0.073 | ⚠ within organs, on part of the lines; also absent: SHROOM4, LINC02432, CD74 |
| [[EPSTI1]] | B | EPSTI1 activity raises FNIP2's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 1.61× lower at baseline in the lines without EPSTI1 | 0.086 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[COG5]] | C | COG5's natural level weakens FNIP2's drug response | COG5's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.11; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.389). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.8, 13.4); signed map (48.4, 12.8). **Vector** length 104, 26.5% of its response variance represented; |z| ≥ 3 in 1,266 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +15.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.9 | +5.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +10.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.4 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.8 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.8 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +2.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.8 | -12.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -12.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.9 | -7.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -4.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.8 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | folliculin interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.1 — chr4:158,769,026-158,908,050 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1450, FNIPL, MAPO1 |
| Gene groups (HGNC) | DENN domain containing |
| Reactome | 4 pathways, smallest: Amino acids regulate mTORC1; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P278](https://www.uniprot.org/uniprotkb/Q9P278) (Folliculin-interacting protein 2):

> Binding partner of the GTPase-activating protein FLCN: involved in the cellular response to amino acid availability by regulating the non-canonical mTORC1 signaling cascade controlling the MiT/TFE factors TFEB and TFE3. Required to promote FLCN recruitment to lysosomes and interaction with Rag GTPases, leading to activation of the non-canonical mTORC1 signaling (By similarity). In low-amino acid conditions, component of the lysosomal folliculin complex (LFC) on the membrane of lysosomes, which …

**Summary**, from NCBI Gene [57600](https://www.ncbi.nlm.nih.gov/gene/57600):

> This gene encodes a protein that binds to the tumor suppressor folliculin and to AMP-activated protein kinase (AMPK), and may play a role cellular metabolism and nutrient sensing by regulating the AMPK-mechanistic target of rapamycin signaling pathway. The encoded protein may also be involved in regulating the O6-methylguanine-induced apoptosis signaling pathway. This gene has a closely related paralog that encodes a protein with similar binding activities. Both related proteins also associate …

**Accessions** — [HGNC:29280](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29280) · Entrez [57600](https://www.ncbi.nlm.nih.gov/gene/57600) · UniProt [Q9P278](https://www.uniprot.org/uniprotkb/Q9P278) · Ensembl [ENSG00000052795](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000052795)

## Data

Gene col 587: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 587); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 587, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 587]; `tensor/DDL_lfc|DDL_z.npy` [587]; `embed/gene_vectors.npy` [587]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 587 or target_col == 587). Every well: [[FNIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FNIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

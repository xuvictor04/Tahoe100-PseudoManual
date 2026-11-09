---
symbol: "ACSS2"
type: "gene"
col: 5166
ensembl_id: "ENSG00000131069"
name: "acyl-CoA synthetase short chain family member 2"
location: "20q11.22"
module: 86
arm: "+"
pooled_cpm: 55.85
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 21
n_dd_up_clean: 25
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# ACSS2

*acyl-CoA synthetase short chain family member 2* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (4 with an alert ⚠); the strongest is [[Cepharanthine (drug)]] 5 µM: 2.41× (z +19.7, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.618× (z -7.7, q 9e-12, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MVD]] (+0.85, fdr 7e-06), [[FDPS]] (+0.82, fdr 7e-06), [[FDFT1]] (+0.81, fdr 7e-06); moves opposite to [[TRMT5]] (-0.50, fdr 4e-05), [[NOL11]] (-0.47, fdr 4e-05), [[ME3]] (-0.45, fdr 6e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[F11R]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 4 with an alert ⚠; shown: the 15 strongest. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5166.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **2.41×** | +19.7 | 0e+00 | 44/47 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Berbamine (drug)]] 5 µM |  | **2.22×** | +17.8 | 0e+00 | 45/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.82×** | +9.1 | 2e-17 | 36/48 (C32, HOP62, …) | top dose only | plate-row cell shift |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.74×** | +8.5 | 4e-15 | 37/47 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +8.2 | 4e-14 | 31/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 5 µM |  | **1.66×** | +7.7 | 1e-12 | 30/47 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +7.6 | 3e-12 | 32/47 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Posaconazole (drug)]] 5 µM |  | **1.63×** | +7.4 | 9e-12 | 33/47 (HEC-1-A, AsPC-1, …) | rises with dose | plate-row cell shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +6.7 | 1e-09 | 27/47 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.48×** | +6.2 | 3e-08 | 31/47 (NCI-H2030, HT-29, …) | rises with dose |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.50×** | +6.2 | 4e-08 | 31/47 (SW 900, hTERT-HPNE, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.46×** | +6.0 | 1e-07 | 27/46 (SW48, SW480, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +5.8 | 2e-07 | 30/46 (A549, SNU-423, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.44×** | +5.7 | 5e-07 | 29/47 (C32, hTERT-HPNE, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.45×** | +5.7 | 6e-07 | 30/46 (HT-29, HS-578T, …) | rises with dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5166.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.618×** | -7.7 | 9e-12 | 33/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.623×** | -7.2 | 1e-10 | 33/47 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.656×** | -6.7 | 3e-09 | 30/46 (NCI-H460, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.648×** | -6.7 | 4e-09 | 34/47 (LoVo, KATO III, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.666×** | -6.5 | 1e-08 | 30/47 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.467×** | -6.3 | 2e-08 | 29/48 (A-427, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.722×** | -5.2 | 1e-05 | 26/46 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.724×** | -5.2 | 2e-05 | 29/47 (NCI-H460, KATO III, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.800×** | -5.1 | 2e-05 | 23/47 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.552×** | -5.0 | 4e-05 | 24/47 (SNU-1, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.734×** | -4.9 | 4e-05 | 24/47 (SK-MEL-2, KATO III, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.830×** | -4.2 | 0.001 | 21/47 (CFPAC-1, HT-29, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.769×** | -4.2 | 0.001 | 24/47 (SW480, KATO III, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.778×** | -4.0 | 0.002 | 23/47 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.786×** | -3.9 | 0.004 | 22/47 (NCI-H1573, LS 180, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.773×** | -3.8 | 0.005 | 20/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **0.654×** | -3.5 | 0.013 | 14/47 (KATO III, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.803×** | -3.5 | 0.014 | 17/47 (AsPC-1, BT-474, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.665×** | -3.4 | 0.019 | 18/47 (NCI-H23, SK-MEL-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.814×** | -3.3 | 0.027 | 16/48 (KATO III, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5166. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 65.4 | 1 | 8 (5 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.13× (z +10.1) | [[Harringtonine (drug)]] 0.5 µM 0.243× (z -13.3) |
| [[KATO III (line)]] | alt | 163 | 2 | 5 (2 ⚠) | [[Cepharanthine (drug)]] 5 µM 4.66× (z +11.6) | [[Harringtonine (drug)]] 0.5 µM 0.117× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 98.0 | 3 | 2 (2 ⚠) | [[Cepharanthine (drug)]] 5 µM 2.47× (z +11.5) | [[Harringtonine (drug)]] 5 µM 0.275× (z -11.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[HEC-1-A (line)]] | alt | 27.7 | 4 | 0 | [[Cepharanthine (drug)]] 5 µM 3.13× (z +13.9) | — |
| [[LoVo (line)]] | wt | 66.2 | 3 (1 ⚠) | 1 | [[Berbamine (drug)]] 5 µM 5.51× (z +20.5) | [[Belumosudil (drug)]] 5 µM 0.340× (z -8.9) |
| [[LS 180 (line)]] | wt | 71.5 | 4 | 0 | [[Cepharanthine (drug)]] 5 µM 5.44× (z +16.8) | — |
| [[NCI-H2030 (line)]] | alt | 102 | 4 (2 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 2.75× (z +14.0) | — |
| [[NCI-H23 (line)]] | alt | 33.3 | 2 | 2 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 6.04× (z +19.1) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -8.7) |
| [[BT-474 (line)]] | alt | 435 | 1 | 2 (2 ⚠) | [[Cepharanthine (drug)]] 5 µM 3.28× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 67.1 | 3 | 0 | [[Cepharanthine (drug)]] 5 µM 3.50× (z +13.9) | — |
| [[CFPAC-1 (line)]] | alt | 45.5 | 2 | 1 | [[Berbamine (drug)]] 5 µM 2.67× (z +10.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -9.1) |
| [[HOP62 (line)]] | alt | 26.8 | 3 | 0 | [[Cepharanthine (drug)]] 5 µM 3.87× (z +15.3) | — |
| [[HT-29 (line)]] | alt | 56.6 | 3 | 0 | [[Cepharanthine (drug)]] 5 µM 7.55× (z +18.4) | — |
| [[SW 900 (line)]] | alt | 32.1 | 3 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 4.06× (z +12.8) | — |
| [[A498 (line)]] | wt | 37.7 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 2.32× (z +10.6) | — |
| [[A549 (line)]] | wt | 24.6 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.99× (z +15.7) | — |
| [[COLO 205 (line)]] | alt | 55.7 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.66× (z +9.6) | — |
| [[HCT15 (line)]] | alt | 59.3 | 1 | 1 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 2.70× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 32.7 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.22× (z +14.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 35.9 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 2.76× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 81.6 | 1 | 1 | [[Cepharanthine (drug)]] 5 µM 2.56× (z +9.8) | [[Harringtonine (drug)]] 0.5 µM 0.287× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 53.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -10.5) |
| [[A-172 (line)]] | wt | 36.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 27.3 | 0 | 1 | — | [[Malotilate (drug)]] 0.5 µM 0.0533× (z -10.4) |
| [[Hs 766T (line)]] | wt | 98.5 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 2.51× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 3.36× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 36.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 35.0 | 0 | 1 | — | [[Demeclocycline (drug)]] 0.05 µM 0.0583× (z -9.5) |
| [[PANC-1 (line)]] | alt | 36.1 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 2.50× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SNU-423 (line)]] | alt | 50.4 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 2.14× (z +8.6) | — |
| [[A-427 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 42.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5166), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MVD]] | +0.85 | +0.85 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 477 |
| [[FDPS]] | +0.82 | +0.83 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 520 |
| [[FDFT1]] | +0.81 | +0.82 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 569 |
| [[SREBF2]] | +0.79 | +0.74 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 476 |
| [[MSMO1]] | +0.78 | +0.76 / +0.73 | both halves | 7e-06 | STRING 421 |
| [[HMGCR]] | +0.76 | +0.79 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 588 |
| [[DHCR7]] | +0.76 | +0.75 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 457 |
| [[STARD4]] | +0.74 | +0.73 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[IDI1]] | +0.73 | +0.72 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 449 |
| [[PCSK9]] | +0.71 | +0.69 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SQLE]] | +0.71 | +0.78 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 604 |
| [[SCD]] | +0.70 | +0.75 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 588 |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT5]] | -0.50 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[NOL11]] | -0.47 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[ME3]] | -0.45 | -0.38 / -0.44 | both halves | 6e-05 | STRING 500 |
| [[DDX20]] | -0.45 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[TFAM]] | -0.44 | -0.41 / -0.34 | both halves | 1e-04 | pathway: Mitochondrial biogenesis |
| [[PCNX4-DT]] | -0.43 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[ANKRD31]] | -0.43 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[AMOTL2]] | -0.42 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[ZNF830]] | -0.42 | -0.29 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F11R]] | B | F11R activity raises ACSS2's level | lines that do not express F11R (10) vs lines expressing it (40) | 1.87× lower at baseline in the lines without F11R | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000287306, LONRF3, TUBA4A |
| [[MLXIPL]] | B | MLXIPL activity raises ACSS2's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 1.74× lower at baseline in the lines without MLXIPL | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.858). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.4, -49.0); signed map (-53.0, 32.5). **Vector** length 140, 44.0% of its response variance represented; |z| ≥ 3 in 1,574 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *cholesterol synthesis* (control, mean cos +0.70 to 22); *Cholesterol biosynthesis* (reactome, mean cos +0.70 to 20); *Metabolism of steroids* (reactome, mean cos +0.68 to 25).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +10.6 | +19.7 |
|  | [[Berbamine (drug)]] 5 µM |  | +9.1 | +17.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +6.1 | +6.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | +6.0 | +4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +6.0 | +5.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +5.8 | +6.2 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +8.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.2 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.3 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.2 | -5.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.1 | -6.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA synthetase short chain family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:34,872,146-34,927,962 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ACS, ACSA, AceCS, dJ1161H23.1; previously ACAS2 |
| Gene groups (HGNC) | Acyl-CoA synthetase family |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS |
| Reactome | 6 pathways, smallest: Ethanol oxidation; Transcriptional activation of mitochondrial biogenesis; Phase I - Functionalization of compounds |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR19](https://www.uniprot.org/uniprotkb/Q9NR19) (Acetyl-coenzyme A synthetase, cytoplasmic):

> Catalyzes the synthesis of acetyl-CoA from short-chain fatty acids. Acetate is the preferred substrate. Can also utilize propionate with a much lower affinity. Catalyzes the conversion of lactate into lactoyl-CoA. Does not catalyze the conversion of butyrate or crotonate to their corresponding acyl-CoAs. Nuclear ACSS2 promotes glucose deprivation-induced lysosomal biogenesis and autophagy, tumor cell survival and brain tumorigenesis. Glucose deprivation results in AMPK-mediated phosphorylation …

**Summary**, from NCBI Gene [55902](https://www.ncbi.nlm.nih.gov/gene/55902):

> This gene encodes a cytosolic enzyme that catalyzes the activation of acetate for use in lipid synthesis and energy generation. The protein acts as a monomer and produces acetyl-CoA from acetate in a reaction that requires ATP. Expression of this gene is regulated by sterol regulatory element-binding proteins, transcription factors that activate genes required for the synthesis of cholesterol and unsaturated fatty acids. Alternative splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:15814](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15814) · Entrez [55902](https://www.ncbi.nlm.nih.gov/gene/55902) · UniProt [Q9NR19](https://www.uniprot.org/uniprotkb/Q9NR19) · Ensembl [ENSG00000131069](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131069)

## Data

Gene col 5166: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5166); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5166, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5166]; `tensor/DDL_lfc|DDL_z.npy` [5166]; `embed/gene_vectors.npy` [5166]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5166 or target_col == 5166). Every well: [[ACSS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACSS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "ADIPOR2"
type: "gene"
col: 132
ensembl_id: "ENSG00000006831"
name: "adiponectin receptor 2"
location: "12p13.33"
module: 86
arm: "+"
pooled_cpm: 170.83
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# ADIPOR2

*adiponectin receptor 2* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.93× (z +13.5, q 8e-39, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Berbamine (drug)]] 5 µM: 1.45× (z +10.8, q 8e-25, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Radotinib (drug)]] 5 µM: 0.829× (z -5.4, q 3e-05, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDI1]] (+0.69, fdr 7e-06), [[HMGCR]] (+0.66, fdr 1e-05), [[EBP]] (+0.64, fdr 2e-05); moves opposite to [[ZKSCAN8]] (-0.51, fdr 4e-05), [[RAD52]] (-0.51, fdr 4e-05), [[ZC3H7B]] (-0.48, fdr 3e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 132.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.93×** | +13.5 | 8e-39 | 46/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.72×** | +11.2 | 1e-26 | 45/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Berbamine (drug)]] 5 µM |  | **1.45×** | +10.8 | 8e-25 | 44/49 (NCI-H23, A549, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.59×** | +9.5 | 3e-19 | 45/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.36×** | +8.9 | 4e-17 | 41/48 (NCI-H23, A549, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +7.4 | 2e-11 | 33/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.31×** | +5.6 | 2e-06 | 31/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.29×** | +5.2 | 1e-05 | 28/48 (NCI-H460, SNU-1, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.1 | 2e-05 | 34/45 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +4.5 | 4e-04 | 26/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.23×** | +4.3 | 7e-04 | 24/48 (SNU-423, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.50×** | +4.3 | 7e-04 | 28/49 (SW480, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Posaconazole (drug)]] 5 µM |  | **1.24×** | +4.3 | 7e-04 | 29/48 (A549, LoVo, …) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.24×** | +4.3 | 8e-04 | 25/47 (NCI-H23, COLO 205, …) | top dose only |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.002 | 25/48 (A549, SNU-423, …) | top dose only | plate-row cell shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.22×** | +3.8 | 0.005 | 25/48 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.009 | 21/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.012 | 24/49 (MIA PaCa-2, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.015 | 20/48 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 1.19× | +3.4 | 0.018 | 18/49 (HOP62, LS 180, …) | top dose only | plate-row cell shift |
| [[(S)-Crizotinib (drug)]] 5 µM |  | 1.18× | +3.3 | 0.023 | 21/48 (A549, SNU-423, …) | rises with dose |  |
| [[crizotinib (drug)]] 5 µM |  | 1.18× | +3.3 | 0.024 | 18/48 (C-33 A, HT-29, …) | top dose only |  |
| [[Ritonavir (drug)]] 5 µM |  | 1.12× | +3.3 | 0.024 | 8/48 (PANC-1, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 132.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **0.829×** | -5.4 | 3e-05 | 25/48 (A-427, RPMI-7951, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.798×** | -4.6 | 8e-04 | 29/48 (A-427, A-172, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.784×** | -4.6 | 8e-04 | 25/45 (HT-29, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.805×** | -4.4 | 0.001 | 24/48 (LoVo, A-427, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.807×** | -4.4 | 0.001 | 29/48 (KATO III, RKO, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.815×** | -4.2 | 0.003 | 24/48 (HT-29, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.818×** | -4.1 | 0.003 | 24/48 (HT-29, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.817×** | -4.0 | 0.005 | 22/44 (NCI-H23, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -3.5 | 0.031 | 24/48 (A-172, HS-578T, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.851× | -3.3 | 0.056 | 20/49 (COLO 205, RKO, …) | all doses, flat | composition shift |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.857× | -3.2 | 0.080 | 19/48 (A498, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 132. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 178 | 11 (10 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +15.7) | [[Dinaciclib (drug)]] 0.5 µM 0.455× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 285 | 4 (2 ⚠) | 1 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 2.09× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.496× (z -10.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 199 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.57× (z +16.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.78× (z +10.2) | — |
| [[A-172 (line)]] | wt | 51.1 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.61× (z +10.2) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HOP62 (line)]] | alt | 145 | 4 (2 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 1.76× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 306 | 1 | 3 (3 ⚠) | [[Cepharanthine (drug)]] 5 µM 1.72× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.431× (z -9.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 271 | 3 | 1 (1 ⚠) | [[Berbamine (drug)]] 5 µM 1.81× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 206 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.20× (z +15.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[Panc 03.27 (line)]] | alt | 232 | 4 (2 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 1.75× (z +11.2) | — |
| [[SNU-1 (line)]] | wt | 135 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +12.6) | — |
| [[A-427 (line)]] | wt | 458 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -14.6) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.494× (z -9.2) |
| [[A549 (line)]] | wt | 111 | 3 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 2.26× (z +14.1) | — |
| [[J82 (line)]] | alt | 154 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.32× (z +10.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[RKO (line)]] | wt | 184 | 1 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.04× (z +8.9) ⚠ cell-cycle shift, explains ~26% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 114 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.36× (z +10.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A498 (line)]] | wt | 109 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.15× (z +9.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[AsPC-1 (line)]] | alt | 168 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 65.3 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +10.1) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[LOX-IMVI (line)]] | wt | 167 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.06× (z +9.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2347 (line)]] | alt | 152 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.86× (z +9.8) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW 1088 (line)]] | alt | 94.2 | 0 | 2 (1 ⚠) | — | [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.0696× (z -10.1) |
| [[SW 900 (line)]] | alt | 275 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 204 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 238 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 132 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.94× (z +10.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HCT15 (line)]] | alt | 184 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 133 | 1 | 0 | [[Berbamine (drug)]] 5 µM 1.56× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 216 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.569× (z -9.0) ⚠ cell-cycle shift, explains ~16% of this change |
| [[HS-578T (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.58× (z +10.3) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[KATO III (line)]] | alt | 351 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.458× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 221 | 1 | 0 | [[Berbamine (drug)]] 5 µM 1.79× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 98.4 | 1 | 0 | [[Berbamine (drug)]] 5 µM 1.89× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 209 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.495× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 158 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 115 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 122 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 132), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDI1]] | +0.69 | +0.72 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[HMGCR]] | +0.66 | +0.70 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[EBP]] | +0.64 | +0.69 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[LDLR]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[MSMO1]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[DHCR7]] | +0.61 | +0.66 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[FDFT1]] | +0.59 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[SLC25A1]] | +0.58 | +0.62 / +0.37 | both halves | 7e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[DHCR24]] | +0.58 | +0.62 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[FDPS]] | +0.58 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[CYP51A1]] | +0.57 | +0.64 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[HMGCS1]] | +0.57 | +0.61 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_FATTY_ACID_METABOLISM |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZKSCAN8]] | -0.51 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[RAD52]] | -0.51 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ZC3H7B]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[SEPSECS]] | -0.48 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[DCP1B]] | -0.48 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[ZNF627]] | -0.48 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[TMEM128]] | -0.48 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[MTHFSD]] | -0.48 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[OTUD4]] | -0.48 | -0.37 / -0.42 | both halves | 7e-05 |  |
| [[YAE1]] | -0.47 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[ZNF253]] | -0.47 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[ZNF441]] | -0.47 | -0.44 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.668). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.4, -48.7); signed map (-52.0, 32.9). **Vector** length 137, 45.2% of its response variance represented; |z| ≥ 3 in 1,308 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *cholesterol synthesis* (control, mean cos +0.54 to 22); *Cholesterol biosynthesis* (reactome, mean cos +0.53 to 20); *cholesterol homeostasis* (hallmark, mean cos +0.52 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Berbamine (drug)]] 5 µM |  | +7.9 | +10.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +6.6 | +8.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.6 | +13.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.6 | +11.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +5.2 | +4.3 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +4.8 | +3.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.3 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -10.4 | -2.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.0 | -3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -9.0 | -1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.2 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.6 | -4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.1 | -5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.0 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.8 | -4.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.7 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | adiponectin receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:1,688,574-1,788,674 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAQR2, ACDCR2 |
| Gene groups (HGNC) | Adiponectin receptors; Progestin and adipoQ receptor family |
| Hallmark sets | APICAL_SURFACE, FATTY_ACID_METABOLISM, ADIPOGENESIS, MTORC1_SIGNALING |
| Reactome | 2 pathways, smallest: AMPK inhibits chREBP transcriptional activation activity; Integration of energy metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86V24](https://www.uniprot.org/uniprotkb/Q86V24) (Adiponectin receptor protein 2):

> Receptor for ADIPOQ, an essential hormone secreted by adipocytes that regulates glucose and lipid metabolism. Required for normal body fat and glucose homeostasis. ADIPOQ-binding activates a signaling cascade that leads to increased PPARA activity, and ultimately to increased fatty acid oxidation and glucose uptake. Has intermediate affinity for globular and full-length adiponectin. Required for normal revascularization after chronic ischemia caused by severing of blood vessels (By similarity).

**Summary**, from NCBI Gene [79602](https://www.ncbi.nlm.nih.gov/gene/79602):

> The adiponectin receptors, ADIPOR1 (MIM 607945) and ADIPOR2, serve as receptors for globular and full-length adiponectin (MIM 605441) and mediate increased AMPK (see MIM 602739) and PPAR-alpha (PPARA; MIM 170998) ligand activities, as well as fatty acid oxidation and glucose uptake by adiponectin (Yamauchi et al., 2003 [PubMed 12802337]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24041](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24041) · Entrez [79602](https://www.ncbi.nlm.nih.gov/gene/79602) · UniProt [Q86V24](https://www.uniprot.org/uniprotkb/Q86V24) · Ensembl [ENSG00000006831](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006831)

## Data

Gene col 132: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 132); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 132, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 132]; `tensor/DDL_lfc|DDL_z.npy` [132]; `embed/gene_vectors.npy` [132]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 132 or target_col == 132). Every well: [[ADIPOR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADIPOR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

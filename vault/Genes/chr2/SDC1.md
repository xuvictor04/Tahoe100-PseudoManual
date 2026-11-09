---
symbol: "SDC1"
type: "gene"
col: 3732
ensembl_id: "ENSG00000115884"
name: "syndecan 1"
location: "2p24.1"
module: 28
arm: "-"
pooled_cpm: 22.56
n_lines_expressing: 42
n_dd_up: 17
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# SDC1

*syndecan 1* — 2p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.14× (z +17.3, q 0e+00, up in 25 of 32 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.33× (z +4.9, q 8e-05, up in 13 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.345× (z -18.3, q 0e+00, down in 29 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPRIP]] (+0.60, fdr 1e-05), [[USB1]] (+0.58, fdr 1e-05), [[AKT1]] (+0.58, fdr 1e-05); moves opposite to [[MRPS18B]] (-0.62, fdr 1e-05), [[PIGBOS1]] (-0.59, fdr 1e-05), [[RUFY1]] (-0.59, fdr 1e-05).
> It sits in the **-** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[KLK10]] → it (grade B ⚠); 3 go from it, the strongest it → [[PPP4C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3732.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **4.14×** | +17.3 | 0e+00 | 25/32 (A498, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **4.07×** | +16.4 | 0e+00 | 22/25 (A498, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.04×** | +12.5 | 2e-33 | 24/28 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.61×** | +5.6 | 4e-06 | 22/38 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.38×** | +5.5 | 6e-06 | 18/39 (A549, LOX-IMVI, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.59×** | +5.4 | 7e-06 | 19/38 (A-172, A549, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.58×** | +5.3 | 9e-06 | 19/36 (A-172, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.52×** | +4.9 | 6e-05 | 16/37 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.9 | 8e-05 | 13/40 (A549, SW480, …) | top dose only | position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.015 | 12/38 (AsPC-1, PANC-1, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.52×** | +3.6 | 0.015 | 13/38 (HT-29, BT-474, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.35×** | +3.6 | 0.016 | 11/34 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.020 | 11/40 (BT-474, SHP-77, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.21×** | +3.2 | 0.052 | 10/41 (SW480, A-427, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.30×** | +3.2 | 0.055 | 11/38 (BT-474, SW480, …) | two highest doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.44×** | +3.1 | 0.058 | 4/38 (HepG2/C3A, A498, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.092 | 10/38 (NCI-H1573, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3732.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.345×** | -18.3 | 0e+00 | 29/38 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.250×** | -16.2 | 0e+00 | 36/37 (AsPC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.460×** | -9.5 | 5e-19 | 29/36 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.427×** | -5.2 | 2e-05 | 22/39 (Hs 766T, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.663×** | -4.8 | 2e-04 | 24/38 (HepG2/C3A, A498, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.715×** | -4.1 | 0.004 | 19/38 (A-172, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **0.518×** | -4.0 | 0.004 | 15/40 (AsPC-1, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.737×** | -3.7 | 0.014 | 15/39 (AsPC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.754×** | -3.4 | 0.036 | 5/40 (A498, LoVo, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.823×** | -3.2 | 0.070 | 11/40 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.771×** | -3.2 | 0.070 | 9/38 (A498, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **0.763×** | -3.2 | 0.070 | 9/38 (SW 900, RKO, …) | inconsistent across doses | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3732. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 80.8 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0514× (z -28.9) |
| [[Hs 766T (line)]] | wt | 77.9 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0678× (z -27.9) |
| [[A498 (line)]] | wt | 54.6 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -14.3) |
| [[A549 (line)]] | wt | 19.2 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -14.4) |
| [[AsPC-1 (line)]] | alt | 129 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0438× (z -34.2) |
| [[HOP62 (line)]] | alt | 13.8 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 9.31× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Harringtonine (drug)]] 5 µM 0.0865× (z -12.6) |
| [[A-172 (line)]] | wt | 26.5 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.0936× (z -16.0) |
| [[KATO III (line)]] | alt | 28.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.0549× (z -24.2) |
| [[PANC-1 (line)]] | alt | 8.42 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.40× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -8.7) |
| [[LS 180 (line)]] | wt | 27.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0833× (z -21.8) |
| [[NCI-H1573 (line)]] | alt | 120 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0631× (z -19.7) |
| [[NCI-H2347 (line)]] | alt | 25.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -15.8) |
| [[A-427 (line)]] | wt | 17.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 35.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -14.9) |
| [[HEC-1-A (line)]] | alt | 15.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 7.34 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.56× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 19.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Harringtonine (drug)]] 5 µM 0.166× (z -10.3) |
| [[SW48 (line)]] | wt | 13.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0561× (z -10.5) |
| [[BT-474 (line)]] | alt | 23.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -12.1) |
| [[HepG2_C3A (line)]] | wt | 20.8 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0914× (z -11.6) |
| [[HT-29 (line)]] | alt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -13.0) |
| [[LoVo (line)]] | wt | 15.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.172× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 9.00 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0530× (z -16.6) |
| [[SNU-423 (line)]] | alt | 12.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW1417 (line)]] | alt | 20.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -9.3) |
| [[SW480 (line)]] | alt | 8.66 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[AN3 CA (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.06 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.35 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3732), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPRIP]] | +0.60 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[USB1]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[AKT1]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 | pathway: Metabolism of vitamins and cofactors; STRING 702 |
| [[POMGNT1]] | +0.58 | +0.57 / +0.46 | both halves | 2e-05 | pathway: Diseases of glycosylation |
| [[ATG16L1]] | +0.57 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ECM1]] | +0.57 | +0.44 / +0.54 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[MACROH2A1]] | +0.56 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[MALL]] | +0.55 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[CTSZ]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[RBPMS2]] | +0.55 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[SERPINB5]] | +0.54 | +0.56 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[PKP1]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS18B]] | -0.62 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[PIGBOS1]] | -0.59 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[RUFY1]] | -0.59 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[TRMT10B]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[NFKBIL1]] | -0.57 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[HEIH]] | -0.57 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[CCDC174]] | -0.55 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[EBAG9]] | -0.55 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[PPIG]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ZNF766]] | -0.54 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[RSF1]] | -0.54 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[SCAF11]] | -0.54 | -0.53 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLK10]] | B | KLK10 activity raises SDC1's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 2.78× lower at baseline in the lines without KLK10 | 0.004 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[SERPINB5]] | B | SERPINB5 activity raises SDC1's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.80× lower at baseline in the lines without SERPINB5 | 0.008 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[MDFI]] | B | MDFI activity raises SDC1's level | lines that do not express MDFI (25) vs lines expressing it (25) | 1.83× lower at baseline in the lines without MDFI | 0.016 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| [[TOP2A]] | B | TOP2A activity lowers SDC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DHRS9]] | B | DHRS9 activity raises SDC1's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 2.53× lower at baseline in the lines without DHRS9 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610 |
| [[SERPINB5]] | B | SERPINB5 activity weakens SDC1's drug response | lines that do not express SERPINB5 (26) vs lines expressing it (13) | the lines without SERPINB5 respond 1.14× as strongly (z diff -0.58); strongest at Idarubicin (hydrochloride) 5 µM: 1.57x vs 0.82x (z diff -4.6) | 0.081 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; target measured in part of the lines; both ways; artifact flags |
| [[DHRS9]] | B | DHRS9 activity weakens SDC1's drug response | lines that do not express DHRS9 (32) vs lines expressing it (7) | the lines without DHRS9 respond 1.50× as strongly (z diff -1.19); strongest at Idarubicin (hydrochloride) 5 µM: 1.46x vs 0.67x (z diff -5.0) | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610; target measured in part of the lines; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP4C]] | B | SDC1 activity raises PPP4C's level | lines that do not express SDC1 (8) vs lines expressing it (42) | 1.20× lower at baseline in the lines without SDC1 | 0.078 | ⚠ within organs, on part of the lines; also absent: CARD10, MFNG, BMAL2; maybe low, not absent |
| [[EBAG9]] | B | SDC1 activity raises EBAG9's level | lines that do not express SDC1 (8) vs lines expressing it (42) | 1.24× lower at baseline in the lines without SDC1 | 0.087 | ⚠ within organs, on part of the lines; also absent: CARD10, MFNG, BMAL2; maybe low, not absent |
| [[DGKA]] | B | SDC1 activity raises DGKA's level | lines that do not express SDC1 (8) vs lines expressing it (42) | 2.16× lower at baseline in the lines without SDC1 | 0.089 | ⚠ within organs, on part of the lines; also absent: CARD10, MFNG, BMAL2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **-** arm (projection on the module's main direction -0.508). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-28.5, 19.3); signed map (-10.9, 42.8). **Vector** length 94.7, 22.7% of its response variance represented; |z| ≥ 3 in 916 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +9.4 | +17.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +9.1 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +8.9 | +16.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +6.2 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +0.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.2 | +3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.4 | -16.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -9.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -18.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.5 | -1.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.9 | -4.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -2.2 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | syndecan 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.1 — chr2:20,200,797-20,225,433 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD138, syndecan, SYND1; previously SDC |
| Gene groups (HGNC) | CD molecules; Syndecans |
| Hallmark sets | GLYCOLYSIS, EPITHELIAL_MESENCHYMAL_TRANSITION, P53_PATHWAY |
| Reactome | 41 pathways, smallest: Defective EXT1 causes exostoses 1, TRPS2 and CHDS; Defective EXT2 causes exostoses 2; Defective B3GALT6 causes EDSP2 and SEMDJL1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P18827](https://www.uniprot.org/uniprotkb/P18827) (Syndecan-1):

> Cell surface proteoglycan that contains both heparan sulfate and chondroitin sulfate and that links the cytoskeleton to the interstitial matrix (By similarity). Regulates exosome biogenesis in concert with SDCBP and PDCD6IP. Able to induce its own expression in dental mesenchymal cells and also in the neighboring dental epithelial cells via an MSX1-mediated pathway (By similarity).

**Summary**, from NCBI Gene [6382](https://www.ncbi.nlm.nih.gov/gene/6382):

> The protein encoded by this gene is a transmembrane (type I) heparan sulfate proteoglycan and is a member of the syndecan proteoglycan family. The syndecans mediate cell binding, cell signaling, and cytoskeletal organization and syndecan receptors are required for internalization of the HIV-1 tat protein. The syndecan-1 protein functions as an integral membrane protein and participates in cell proliferation, cell migration and cell-matrix interactions via its receptor for extracellular matrix …

**Accessions** — [HGNC:10658](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10658) · Entrez [6382](https://www.ncbi.nlm.nih.gov/gene/6382) · UniProt [P18827](https://www.uniprot.org/uniprotkb/P18827) · Ensembl [ENSG00000115884](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115884)

## Data

Gene col 3732: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3732); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3732, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3732]; `tensor/DDL_lfc|DDL_z.npy` [3732]; `embed/gene_vectors.npy` [3732]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3732 or target_col == 3732). Every well: [[SDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

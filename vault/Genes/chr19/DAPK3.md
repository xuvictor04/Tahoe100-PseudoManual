---
symbol: "DAPK3"
type: "gene"
col: 9512
ensembl_id: "ENSG00000167657"
name: "death associated protein kinase 3"
location: "19p13.3"
module: 189
arm: "+"
pooled_cpm: 48.65
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/189"]
generated_by: "tahoemap"
---

# DAPK3

*death associated protein kinase 3* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +12.7, q 2e-34, up in 41 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.37× (z +10.9, q 2e-25, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.511× (z -9.2, q 2e-17, down in 34 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.798× (z -4.5, q 6e-04, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MARCHF9]] (+0.60, fdr 1e-05), [[RAB24]] (+0.58, fdr 1e-05), [[ACAP1]] (+0.57, fdr 1e-05); moves opposite to [[CHRAC1]] (-0.57, fdr 1e-05), [[MBNL3]] (-0.56, fdr 3e-05), [[MOB1A]] (-0.55, fdr 3e-05).
> It is in [[Module 189]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9512.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.89×** | +12.7 | 2e-34 | 41/47 (LoVo, C32, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.37×** | +10.9 | 2e-25 | 47/49 (PANC-1, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.41×** | +6.9 | 1e-09 | 35/49 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.47×** | +6.7 | 3e-09 | 37/47 (A-172, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +5.2 | 2e-05 | 31/48 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +4.6 | 3e-04 | 23/48 (LoVo, A-427, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.38×** | +4.6 | 3e-04 | 31/48 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.51×** | +4.2 | 0.002 | 25/47 (HS-578T, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.35×** | +4.1 | 0.002 | 28/48 (A549, A-172, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.33×** | +4.1 | 0.003 | 23/48 (NCI-H1573, HT-29, …) | rises with dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +4.0 | 0.003 | 28/48 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.30×** | +3.7 | 0.011 | 21/47 (LS 180, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.28×** | +3.5 | 0.018 | 21/47 (A-172, A549, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.5 | 0.020 | 18/48 (SNU-1, NCI-H1792, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +3.3 | 0.033 | 23/47 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.035 | 20/47 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.041 | 17/47 (COLO 205, HT-29, …) | rises with dose |  |
| [[Fumaric acid (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.041 | 11/48 (NCI-H1573, A-172, …) | top dose only | plate-row cell shift |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.058 | 16/47 (NCI-H2347, SW1417, …) | inconsistent across doses |  |
| [[Hexylresorcinol (drug)]] 5 µM |  | 1.16× | +3.0 | 0.070 | 7/49 (MIA PaCa-2, SNU-423, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9512.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.511×** | -9.2 | 2e-17 | 34/39 (NCI-H2347, SNU-1, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.685×** | -4.8 | 3e-04 | 26/48 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.912× | -4.8 | 3e-04 | 1/49 (SNU-1) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.791×** | -4.7 | 3e-04 | 27/48 (RKO, SNU-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.798×** | -4.5 | 6e-04 | 26/48 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.726×** | -4.4 | 0.001 | 24/48 (NCI-H23, SNU-423, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.740×** | -4.3 | 0.001 | 25/48 (NCI-H2347, NCI-H1573, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.744×** | -4.1 | 0.003 | 24/49 (NCI-H2347, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.731×** | -4.0 | 0.004 | 23/48 (hTERT-HPNE, RKO, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.768×** | -3.8 | 0.009 | 20/48 (hTERT-HPNE, HOP62, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.789×** | -3.1 | 0.091 | 14/47 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 0.5 µM |  | 0.806× | -3.1 | 0.10 | 15/48 (Hs 766T, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.809× | -3.0 | 0.11 | 18/48 (SNU-423, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9512. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 83.5 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -17.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 59.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +13.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.45× (z +10.6) | — |
| [[RKO (line)]] | wt | 110 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.53× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0742× (z -19.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 52.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +13.4) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.183× (z -12.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 55.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -9.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 45.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +8.8) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -9.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 92.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.4) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.372× (z -9.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 77.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -11.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 29.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.0) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.118× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 61.3 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.15× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 8.92× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 82.4 | 0 | 2 (1 ⚠) | — | [[Belumosudil (drug)]] 5 µM 0.311× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 31.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.2) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.191× (z -12.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 32.1 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.5× (z +11.2) | — |
| [[SNU-1 (line)]] | wt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0912× (z -14.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 25.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +10.4) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A498 (line)]] | wt | 77.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.4) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[C32 (line)]] | wt | 67.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +13.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[CFPAC-1 (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -12.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +11.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 63.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -9.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 16.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +9.4) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[LoVo (line)]] | wt | 22.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +13.9) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 42.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +12.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1792 (line)]] | alt | 28.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +12.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[RPMI-7951 (line)]] | alt | 69.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 27.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[AN3 CA (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9512), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARCHF9]] | +0.60 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[RAB24]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ACAP1]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[MEF2D]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[HCFC1R1]] | +0.56 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[DLGAP4]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[TNNT1]] | +0.54 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[NFKBIL1]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[MEAK7]] | +0.53 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[ACAP3]] | +0.53 | +0.55 / +0.37 | both halves | 8e-05 | same gene group |
| [[DCTN6-DT]] | +0.53 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[R3HCC1]] | +0.52 | +0.38 / +0.48 | both halves | 6e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHRAC1]] | -0.57 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[MBNL3]] | -0.56 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[MOB1A]] | -0.55 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[TMX1]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ATE1]] | -0.53 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[PSME3]] | -0.53 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[SNX5]] | -0.53 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[TOR1A]] | -0.52 | -0.56 / -0.29 | both halves | 2e-04 |  |
| [[PRMT3]] | -0.52 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[FAM136A]] | -0.51 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[NAA50]] | -0.51 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[FUCA2]] | -0.51 | -0.48 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DAPK3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 189]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.1, -57.8); signed map (-22.3, 14.5). **Vector** length 115, 33.1% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.0 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +5.0 | +12.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.6 | +4.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.4 | +10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.9 | +4.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +3.7 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | +2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.4 | +4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.2 | -4.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.8 | -4.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | +0.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -4.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.6 | -4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -1.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -2.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | death associated protein kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:3,958,453-3,971,123 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZIP, ZIPK |
| Gene groups (HGNC) | Death associated protein kinases; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Caspase activation via Dependence Receptors in the absence of ligand; Caspase activation via extrinsic apoptotic signalling pathway; Apoptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [O43293](https://www.uniprot.org/uniprotkb/O43293) (Death-associated protein kinase 3):

> Serine/threonine kinase which is involved in the regulation of apoptosis, autophagy, transcription, translation and actin cytoskeleton reorganization. Involved in the regulation of smooth muscle contraction. Regulates both type I (caspase-dependent) apoptotic and type II (caspase-independent) autophagic cell deaths signal, depending on the cellular setting. Involved in regulation of starvation-induced autophagy. Regulates myosin phosphorylation in both smooth muscle and non-muscle cells. In …

**Summary**, from NCBI Gene [1613](https://www.ncbi.nlm.nih.gov/gene/1613):

> Death-associated protein kinase 3 (DAPK3) induces morphological changes in apoptosis when overexpressed in mammalian cells. These results suggest that DAPK3 may play a role in the induction of apoptosis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2676](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2676) · Entrez [1613](https://www.ncbi.nlm.nih.gov/gene/1613) · UniProt [O43293](https://www.uniprot.org/uniprotkb/O43293) · Ensembl [ENSG00000167657](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167657)

## Data

Gene col 9512: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9512); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9512, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9512]; `tensor/DDL_lfc|DDL_z.npy` [9512]; `embed/gene_vectors.npy` [9512]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9512 or target_col == 9512). Every well: [[DAPK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DAPK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

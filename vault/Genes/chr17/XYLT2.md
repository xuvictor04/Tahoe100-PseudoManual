---
symbol: "XYLT2"
type: "gene"
col: 296
ensembl_id: "ENSG00000015532"
name: "xylosyltransferase 2"
location: "17q21.33"
module: 3
arm: "+"
pooled_cpm: 24.56
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 27
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# XYLT2

*xylosyltransferase 2* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.43× (z +4.7, q 0.002, up in 20 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.255× (z -35.7, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDAN1]] (+0.72, fdr 7e-06), [[STK32C]] (+0.70, fdr 1e-05), [[SDHAF1]] (+0.69, fdr 1e-05); moves opposite to [[RIPK2-DT]] (-0.70, fdr 1e-05), [[LEKR1]] (-0.64, fdr 2e-05), [[PCNX4-DT]] (-0.63, fdr 3e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 296.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 0.002 | 20/46 (C-33 A, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.092 | 10/48 (KATO III, SW 900, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.092 | 9/48 (A498, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.12 | 18/45 (AsPC-1, HT-29, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.3 | 0.12 | 16/47 (A-172, CFPAC-1, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.0 | 0.22 | 4/48 (AsPC-1, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 296.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.255×** | -35.7 | 0e+00 | 44/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.316×** | -21.3 | 0e+00 | 45/47 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.329×** | -19.1 | 0e+00 | 43/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.510×** | -12.4 | 2e-33 | 34/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.648×** | -11.3 | 1e-27 | 36/48 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.543×** | -10.4 | 2e-23 | 29/39 (A-172, H4, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.592×** | -9.7 | 3e-20 | 24/41 (C-33 A, HOP62, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.342×** | -9.3 | 1e-18 | 40/48 (A-427, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.609×** | -8.5 | 1e-15 | 28/48 (HOP62, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.636×** | -8.3 | 4e-15 | 26/46 (hTERT-HPNE, BT-474, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.618×** | -8.3 | 7e-15 | 32/46 (HCT15, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.411×** | -7.7 | 8e-13 | 27/45 (BT-474, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.661×** | -7.6 | 1e-12 | 31/48 (C32, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.675×** | -7.2 | 2e-11 | 27/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.679×** | -7.1 | 4e-11 | 29/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.729×** | -5.4 | 2e-06 | 22/46 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.751×** | -5.3 | 4e-06 | 23/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.769×** | -4.8 | 4e-05 | 19/48 (J82, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.796×** | -4.2 | 7e-04 | 18/48 (C32, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 296. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 40.5 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -30.0) |
| [[NCI-H460 (line)]] | wt | 29.2 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -30.6) |
| [[A-172 (line)]] | wt | 47.3 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0892× (z -24.9) |
| [[PANC-1 (line)]] | alt | 21.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0654× (z -27.7) |
| [[MIA PaCa-2 (line)]] | alt | 25.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -18.3) |
| [[C32 (line)]] | wt | 18.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -13.9) |
| [[J82 (line)]] | alt | 29.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -22.9) |
| [[BT-474 (line)]] | alt | 67.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -17.2) |
| [[hTERT-HPNE (line)]] | wt | 45.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -18.2) |
| [[LOX-IMVI (line)]] | wt | 24.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -21.5) |
| [[NCI-H2030 (line)]] | alt | 15.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -14.1) |
| [[Panc 03.27 (line)]] | alt | 30.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -15.7) |
| [[A549 (line)]] | wt | 23.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -18.7) |
| [[H4 (line)]] | wt | 39.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.314× (z -10.1) |
| [[HS-578T (line)]] | alt | 32.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0924× (z -26.4) |
| [[LoVo (line)]] | wt | 18.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -23.5) |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -13.9) |
| [[NCI-H23 (line)]] | alt | 28.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -23.5) |
| [[NCI-H2347 (line)]] | alt | 14.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -13.5) |
| [[SNU-423 (line)]] | alt | 24.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -18.1) |
| [[A498 (line)]] | wt | 22.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -13.8) |
| [[HCT15 (line)]] | alt | 31.4 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.127× (z -11.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 37.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 22.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 22.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0799× (z -14.8) |
| [[SW 900 (line)]] | alt | 19.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.348× (z -9.0) |
| [[SW1417 (line)]] | alt | 17.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -15.9) |
| [[SW480 (line)]] | alt | 15.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -12.2) |
| [[A-427 (line)]] | wt | 29.5 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0549× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 7.82 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -9.9) |
| [[C-33 A (line)]] | alt | 37.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -13.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -14.1) |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -15.7) |
| [[HT-29 (line)]] | alt | 20.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -14.3) |
| [[KATO III (line)]] | alt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -12.6) |
| [[LS 180 (line)]] | wt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -11.8) |
| [[RKO (line)]] | wt | 28.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0763× (z -26.8) |
| [[SK-MEL-2 (line)]] | alt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -18.0) |
| [[SNU-1 (line)]] | wt | 20.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -8.6) |
| [[AN3 CA (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 296), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDAN1]] | +0.72 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[STK32C]] | +0.70 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[SDHAF1]] | +0.69 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[UNC45A]] | +0.66 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[MAST3]] | +0.66 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[NR2F6]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[WRAP73]] | +0.65 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[SH2B2]] | +0.65 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[MPG]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[POLRMT]] | +0.63 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[RTL10]] | +0.62 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[CDK5RAP1]] | +0.62 | +0.51 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIPK2-DT]] | -0.70 | -0.69 / -0.56 | both halves | 1e-05 |  |
| [[LEKR1]] | -0.64 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[PCNX4-DT]] | -0.63 | -0.66 / -0.29 | both halves | 3e-04 |  |
| [[MMADHC-DT]] | -0.63 | -0.68 / -0.25 | both halves | 4e-04 |  |
| [[CHMP3]] | -0.62 | -0.54 / -0.43 | both halves | 4e-05 |  |
| [[PKN2-AS1]] | -0.62 | -0.66 / -0.26 | both halves | 4e-04 |  |
| [[HCG17]] | -0.62 | -0.64 / -0.32 | both halves | 2e-04 |  |
| [[TUG1]] | -0.61 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[SDCBP2-AS1]] | -0.61 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[ERCC6L2-AS1]] | -0.61 | -0.65 / -0.22 | both halves | 6e-04 |  |
| [[TSGA10]] | -0.61 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[RFX3-DT]] | -0.61 | -0.57 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (2.9, -3.1); signed map (-35.2, 3.2). **Vector** length 78.5, 16.4% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | +3.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.1 | -4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +4.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.6 | -4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.0 | +2.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.0 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | -0.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.3 | -21.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.5 | -10.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -35.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.9 | -9.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.9 | -19.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -7.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | xylosyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:50,346,126-50,363,138 (+) |
| Ensembl biotype | protein_coding |
| Also known as | XT-II, PXYLT2 |
| Gene groups (HGNC) | Glucosaminyl (N-acetyl) transferases/xylosyltransferases |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 3 pathways, smallest: Glycosaminoglycan-protein linkage region biosynthesis; Glycosaminoglycan metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1B5](https://www.uniprot.org/uniprotkb/Q9H1B5) (Xylosyltransferase 2):

> Catalyzes the first step in the biosynthesis of chondroitin sulfate, heparan sulfate and dermatan sulfate proteoglycans, such as DCN. Transfers D-xylose from UDP-D-xylose to specific serine residues of the core protein.

**Summary**, from NCBI Gene [64132](https://www.ncbi.nlm.nih.gov/gene/64132):

> The protein encoded by this gene is an isoform of xylosyltransferase, which belongs to a family of glycosyltransferases. This enzyme transfers xylose from UDP-xylose to specific serine residues of the core protein and initiates the biosynthesis of glycosaminoglycan chains in proteoglycans including chondroitin sulfate, heparan sulfate, heparin and dermatan sulfate. The enzyme activity, which is increased in scleroderma patients, is a diagnostic marker for the determination of sclerotic activity …

**Accessions** — [HGNC:15517](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15517) · Entrez [64132](https://www.ncbi.nlm.nih.gov/gene/64132) · UniProt [Q9H1B5](https://www.uniprot.org/uniprotkb/Q9H1B5) · Ensembl [ENSG00000015532](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000015532)

## Data

Gene col 296: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 296); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 296, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 296]; `tensor/DDL_lfc|DDL_z.npy` [296]; `embed/gene_vectors.npy` [296]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 296 or target_col == 296). Every well: [[XYLT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XYLT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

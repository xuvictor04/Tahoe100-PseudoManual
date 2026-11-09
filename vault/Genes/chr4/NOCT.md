---
symbol: "NOCT"
type: "gene"
col: 7477
ensembl_id: "ENSG00000151014"
name: "nocturnin"
location: "4q31.1"
module: 224
arm: "+"
pooled_cpm: 65.8
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 3
n_dd_up_clean: 22
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/224"]
generated_by: "tahoemap"
---

# NOCT

*nocturnin* — 4q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.79× (z +30.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.612× (z -5.2, q 1e-04, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSRNP1]] (+0.61, fdr 7e-06), [[NFKBIZ]] (+0.61, fdr 7e-06), [[BHLHE40]] (+0.58, fdr 1e-05); moves opposite to [[NR2C2]] (-0.53, fdr 3e-05), [[DGCR2]] (-0.52, fdr 3e-05), [[TAF4]] (-0.51, fdr 3e-05).
> It is in [[Module 224]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ETS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7477.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.79×** | +30.8 | 0e+00 | 48/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.09×** | +16.6 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **14.7×** | +14.9 | 0e+00 | 49/49 (PANC-1, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.65×** | +13.7 | 9e-41 | 47/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.43×** | +9.4 | 6e-19 | 38/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.31×** | +8.9 | 6e-17 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **4.52×** | +8.4 | 5e-15 | 41/48 (NCI-H2030, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.91×** | +6.9 | 5e-10 | 39/48 (A-427, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +6.7 | 1e-09 | 37/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.88×** | +6.7 | 1e-09 | 39/48 (LoVo, A-427, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.86×** | +6.6 | 3e-09 | 36/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.82×** | +6.3 | 1e-08 | 36/48 (KATO III, SW48, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +5.6 | 1e-06 | 36/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.67×** | +5.4 | 2e-06 | 36/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.69×** | +5.1 | 1e-05 | 33/45 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +4.8 | 7e-05 | 33/48 (KATO III, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +4.3 | 5e-04 | 25/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.9 | 0.002 | 26/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +3.9 | 0.003 | 26/48 (KATO III, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7477.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.612×** | -5.2 | 1e-04 | 34/48 (NCI-H23, Panc 03.27, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.637×** | -4.8 | 5e-04 | 35/48 (HS-578T, SNU-423, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.690×** | -3.9 | 0.015 | 31/48 (hTERT-HPNE, LOX-IMVI, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -3.7 | 0.026 | 5/49 (NCI-H23, HCT15, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | 0.562× | -3.2 | 0.15 | 24/47 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.659× | -3.2 | 0.15 | 22/48 (HCT15, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.668× | -3.1 | 0.16 | 20/48 (SW1417, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.750× | -3.1 | 0.16 | 20/48 (AN3 CA, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7477. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 86.6 | 14 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +24.4) | — |
| [[SNU-1 (line)]] | wt | 79.4 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +20.2) | — |
| [[PANC-1 (line)]] | alt | 54.0 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +27.1) | — |
| [[BT-474 (line)]] | alt | 56.3 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.08× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.149× (z -11.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 82.0 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.23× (z +23.2) | [[Dinaciclib (drug)]] 5 µM 0.0889× (z -17.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 36.3 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.58× (z +21.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 69.0 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +25.5) | — |
| [[NCI-H1573 (line)]] | alt | 76.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.85× (z +20.5) | — |
| [[NCI-H2347 (line)]] | alt | 98.2 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.81× (z +22.0) | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -10.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 30.5 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +17.3) | — |
| [[A549 (line)]] | wt | 80.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +26.2) | — |
| [[LoVo (line)]] | wt | 31.0 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.74× (z +22.0) | — |
| [[SW48 (line)]] | wt | 36.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.3× (z +19.8) | — |
| [[A498 (line)]] | wt | 175 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +16.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 112 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.41× (z +24.5) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 59.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.92× (z +17.7) | — |
| [[SK-MEL-2 (line)]] | alt | 46.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.81× (z +16.8) | — |
| [[SW 900 (line)]] | alt | 73.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.70× (z +21.3) | — |
| [[AsPC-1 (line)]] | alt | 63.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +20.4) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -8.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 62.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.23× (z +19.2) | — |
| [[HOP62 (line)]] | alt | 54.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +23.6) | — |
| [[HS-578T (line)]] | alt | 58.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +19.0) | — |
| [[hTERT-HPNE (line)]] | wt | 50.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +20.8) | — |
| [[KATO III (line)]] | alt | 23.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.20× (z +17.6) | — |
| [[LOX-IMVI (line)]] | wt | 97.3 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +12.4) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 65.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +22.1) | — |
| [[HepG2_C3A (line)]] | wt | 69.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +13.7) | — |
| [[J82 (line)]] | alt | 86.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.70× (z +21.1) | — |
| [[LS 180 (line)]] | wt | 29.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.49× (z +17.0) | — |
| [[NCI-H23 (line)]] | alt | 54.1 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +15.8) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 54.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.95× (z +13.7) | — |
| [[SW1417 (line)]] | alt | 41.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.52× (z +16.2) | — |
| [[COLO 205 (line)]] | alt | 23.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +15.7) | — |
| [[HCT15 (line)]] | alt | 46.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 61.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +15.3) | — |
| [[HT-29 (line)]] | alt | 51.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.33× (z +18.6) | — |
| [[NCI-H1792 (line)]] | alt | 50.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +17.7) | — |
| [[SNU-423 (line)]] | alt | 51.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +20.2) | — |
| [[C-33 A (line)]] | alt | 35.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.69× (z +8.7) | — |
| [[H4 (line)]] | wt | 62.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +12.3) | — |
| [[Hs 766T (line)]] | wt | 76.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +19.2) | — |
| [[RKO (line)]] | wt | 125 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +12.0) | — |
| [[SW 1271 (line)]] | alt | 79.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7477), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSRNP1]] | +0.61 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[NFKBIZ]] | +0.61 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[BHLHE40]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[JUN]] | +0.57 | +0.53 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[IER3]] | +0.56 | +0.54 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[TRIM55]] | +0.56 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[NUAK2]] | +0.54 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[CSRP1]] | +0.54 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PLK2]] | +0.54 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[LINC02901]] | +0.53 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[SERPINB9]] | +0.52 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[PRECSIT]] | +0.52 | +0.46 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR2C2]] | -0.53 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[DGCR2]] | -0.52 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[TAF4]] | -0.51 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[GPBP1L1]] | -0.50 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[C8orf76]] | -0.50 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ARHGEF11]] | -0.48 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[RABL6]] | -0.48 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[LEMD3]] | -0.48 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[PPM1B]] | -0.47 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[NUP133]] | -0.46 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[MFSD8]] | -0.45 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[NCOA6]] | -0.45 | -0.36 / -0.42 | both halves | 1e-04 | pathway: BMAL1:CLOCK,NPAS2 activates circadian expression |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ETS1]] | B | ETS1 activity raises NOCT's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 1.66× lower at baseline in the lines without ETS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[NFKBIZ]] | C | NFKBIZ activity raises NOCT's level | lines that do not express NFKBIZ (3) vs lines expressing it (47) | 2.06× lower at baseline in the lines without NFKBIZ | 0.071 | ⚠ few lines (3 vs 47); across organs; also absent: CPEB2, PKIA-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 224]] — hypoxia; 9 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.6, 5.7); signed map (9.4, 28.0). **Vector** length 97.2, 34.2% of its response variance represented; |z| ≥ 3 in 1,260 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +3.9 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +1.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.4 | +14.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +5.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.8 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.3 | -1.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | +6.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.8 | +8.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.4 | -3.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -0.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | -2.6 | -2.8 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -2.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | nocturnin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.1 — chr4:139,015,781-139,045,939 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CCR4L, Ccr4c, NOC; previously CCRN4L |
| Hallmark sets | HYPOXIA |
| Reactome | 4 pathways, smallest: BMAL1:CLOCK,NPAS2 activates circadian expression; NAD+ and Sirtuins regulate the circadian clock; Regulation of the circadian clock |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UK39](https://www.uniprot.org/uniprotkb/Q9UK39) (Nocturnin):

> Phosphatase which catalyzes the conversion of NADP(+) to NAD(+) and of NADPH to NADH. Shows a small preference for NADPH over NADP(+). Represses translation and promotes degradation of target mRNA molecules. Plays an important role in post-transcriptional regulation of metabolic genes under circadian control (By similarity). Exerts a rhythmic post-transcriptional control of genes necessary for metabolic functions including nutrient absorption, glucose/insulin sensitivity, lipid metabolism, …

**Summary**, from NCBI Gene [25819](https://www.ncbi.nlm.nih.gov/gene/25819):

> The protein encoded by this gene is highly similar to Nocturnin, a gene identified as a circadian clock regulated gene in Xenopus laevis. This protein and Nocturnin protein share similarity with the C-terminal domain of a yeast transcription factor, carbon catabolite repression 4 (CCR4). The mRNA abundance of a similar gene in mouse has been shown to exhibit circadian rhythmicity, which suggests a role for this protein in clock function or as a circadian clock effector. [provided by RefSeq, Jul …

**Accessions** — [HGNC:14254](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14254) · Entrez [25819](https://www.ncbi.nlm.nih.gov/gene/25819) · UniProt [Q9UK39](https://www.uniprot.org/uniprotkb/Q9UK39) · Ensembl [ENSG00000151014](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151014)

## Data

Gene col 7477: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7477); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7477, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7477]; `tensor/DDL_lfc|DDL_z.npy` [7477]; `embed/gene_vectors.npy` [7477]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7477 or target_col == 7477). Every well: [[NOCT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOCT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

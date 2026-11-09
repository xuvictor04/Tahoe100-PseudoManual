---
symbol: "MRPL19"
type: "gene"
col: 3665
ensembl_id: "ENSG00000115364"
name: "mitochondrial ribosomal protein L19"
location: "2p12"
module: 4
arm: "+"
pooled_cpm: 63.62
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MRPL19

*mitochondrial ribosomal protein L19* — 2p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.81× (z +18.8, q 0e+00, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.30× (z +4.8, q 1e-04, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.704× (z -9.0, q 1e-16, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLD]] (+0.71, fdr 7e-06), [[MRPS35]] (+0.71, fdr 7e-06), [[GOT2]] (+0.69, fdr 7e-06); moves opposite to [[CATSPERG]] (-0.70, fdr 7e-06), [[TMEM106A]] (-0.60, fdr 9e-06), [[LINC00685]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3665.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.81×** | +18.8 | 0e+00 | 47/49 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.85×** | +16.4 | 0e+00 | 43/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +13.1 | 5e-37 | 40/45 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **1.32×** | +5.0 | 8e-05 | 28/48 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.30×** | +4.8 | 1e-04 | 28/48 (A-172, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +4.8 | 1e-04 | 28/48 (A-172, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +4.8 | 2e-04 | 28/48 (A-427, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.7 | 2e-04 | 26/37 (NCI-H1573, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.3 | 0.001 | 27/47 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.56×** | +4.2 | 0.001 | 27/49 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +4.2 | 0.002 | 24/48 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.2 | 0.002 | 21/48 (A-427, A549, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.006 | 23/48 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.6 | 0.014 | 17/48 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.43×** | +3.4 | 0.025 | 17/47 (NCI-H1792, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.039 | 22/48 (A-172, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.1 | 0.057 | 17/48 (A-172, RPMI-7951, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.057 | 6/48 (SW1417, NCI-H23, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | **1.20×** | +2.9 | 0.092 | 10/48 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.20×** | +2.9 | 0.092 | 10/48 (A549, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3665.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.704×** | -9.0 | 1e-16 | 30/48 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.741×** | -7.7 | 4e-12 | 34/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.818×** | -3.4 | 0.089 | 15/48 (HEC-1-A, A-427, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.830×** | -3.4 | 0.089 | 19/47 (SK-MEL-2, LoVo, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.806×** | -3.4 | 0.089 | 22/47 (RPMI-7951, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3665. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 64.4 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +12.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 60.5 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +15.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 75.5 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.08× (z +15.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -20.8) |
| [[PANC-1 (line)]] | alt | 59.6 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +13.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -11.8) |
| [[HOP62 (line)]] | alt | 64.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -13.0) |
| [[Hs 766T (line)]] | wt | 41.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -11.9) |
| [[RKO (line)]] | wt | 73.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 2.96× (z +9.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -11.2) |
| [[SW480 (line)]] | alt | 73.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +14.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -10.0) |
| [[A-172 (line)]] | wt | 57.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +12.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 69.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +15.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 65.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +14.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 43.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +11.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 59.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -9.6) |
| [[LS 180 (line)]] | wt | 66.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 71.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.44× (z +17.1) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 51.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +10.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -9.9) |
| [[SNU-423 (line)]] | alt | 49.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +12.7) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 61.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -11.8) |
| [[HS-578T (line)]] | alt | 43.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +10.4) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 40.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -10.5) |
| [[KATO III (line)]] | alt | 55.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 104 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +14.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.609× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 23.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.07× (z +9.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 37.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 80.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.37× (z +9.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 54.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 53.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -16.3) |
| [[NCI-H2030 (line)]] | alt | 82.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -19.7) |
| [[RPMI-7951 (line)]] | alt | 51.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -11.1) |
| [[SW 900 (line)]] | alt | 41.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 90.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 109 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 82.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 96.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 90.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3665), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLD]] | +0.71 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[MRPS35]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 996 |
| [[GOT2]] | +0.69 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[DLAT]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 | STRING 404 |
| [[FAM98B]] | +0.69 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[RAD23B]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[ALKBH8]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[MRPL42]] | +0.67 | +0.62 / +0.72 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 953 |
| [[WDR36]] | +0.67 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[GNPDA2]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[IPO8]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 | STRING 578 |
| [[IRAK1BP1]] | +0.65 | +0.55 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CATSPERG]] | -0.70 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[TMEM106A]] | -0.60 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[LINC00685]] | -0.59 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[PPP1R13L]] | -0.59 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.59 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[PKNOX1]] | -0.57 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[TNRC6C]] | -0.57 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[ZBTB7A]] | -0.56 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[EGLN2]] | -0.56 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[TRNAU1AP]] | -0.55 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[TP53INP2]] | -0.55 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[LCAT]] | -0.55 | -0.53 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.595). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.6, -15.0); signed map (-16.3, -44.4). **Vector** length 107, 30.8% of its response variance represented; |z| ≥ 3 in 829 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.6 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.9 | +3.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.9 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +4.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +3.1 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.0 | -7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.4 | -9.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -0.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | -1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.0 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | +2.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.9 | -1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.9 | -3.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.7 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p12 — chr2:75,646,783-75,690,851 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRP-L15, RPML15, KIAA0104, RLX1, bL19m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [P49406](https://www.uniprot.org/uniprotkb/P49406) carries no function annotation.

**Summary**, from NCBI Gene [9801](https://www.ncbi.nlm.nih.gov/gene/9801):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14052](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14052) · Entrez [9801](https://www.ncbi.nlm.nih.gov/gene/9801) · UniProt [P49406](https://www.uniprot.org/uniprotkb/P49406) · Ensembl [ENSG00000115364](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115364)

## Data

Gene col 3665: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3665); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3665, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3665]; `tensor/DDL_lfc|DDL_z.npy` [3665]; `embed/gene_vectors.npy` [3665]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3665 or target_col == 3665). Every well: [[MRPL19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

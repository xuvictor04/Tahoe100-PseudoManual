---
symbol: "CNOT10"
type: "gene"
col: 11350
ensembl_id: "ENSG00000182973"
name: "CCR4-NOT transcription complex subunit 10"
location: "3p22.3"
module: 6
arm: "+"
pooled_cpm: 62.2
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 9
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CNOT10

*CCR4-NOT transcription complex subunit 10* — 3p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.35× (z +8.6, q 3e-15, up in 34 of 47 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.29× (z +3.8, q 0.018, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.601× (z -13.3, q 7e-38, down in 31 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.826× (z -7.6, q 3e-12, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPA2]] (+0.70, fdr 7e-06), [[ORC5]] (+0.62, fdr 1e-05), [[SRBD1]] (+0.61, fdr 7e-06); moves opposite to [[ATXN1-AS1]] (-0.58, fdr 6e-05), [[YPEL5]] (-0.55, fdr 1e-05), [[KCP]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MRAS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11350.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.35×** | +8.6 | 3e-15 | 34/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.31×** | +7.7 | 3e-12 | 30/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.21×** | +5.4 | 1e-05 | 22/47 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.4 | 0.001 | 20/47 (SW480, SHP-77, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.018 | 20/48 (SW480, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | 1.13× | +3.5 | 0.051 | 10/47 (J82, CFPAC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 1.24× | +3.2 | 0.12 | 16/47 (C-33 A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | 1.12× | +3.1 | 0.15 | 14/47 (NCI-H23, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11350.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.601×** | -13.3 | 7e-38 | 31/44 (A549, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.736×** | -8.6 | 2e-15 | 29/48 (RKO, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -8.3 | 2e-14 | 2/48 (AN3 CA, SW 1271) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.826×** | -7.6 | 3e-12 | 24/47 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.760×** | -7.5 | 9e-12 | 24/42 (A-172, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.795×** | -6.5 | 9e-09 | 24/47 (SW1417, SW 1271, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.796×** | -6.4 | 9e-09 | 24/47 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.838× | -5.0 | 4e-05 | 20/47 (KATO III, C32, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | 0.850× | -4.6 | 3e-04 | 20/47 (AsPC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.798×** | -4.5 | 3e-04 | 14/47 (SW480, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.820×** | -4.0 | 0.003 | 20/46 (C-33 A, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.904× | -4.0 | 0.003 | 13/47 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.874× | -3.6 | 0.012 | 17/46 (H4, NCI-H2030, …) | top dose only |  |
| [[NG25 (drug)]] 0.05 µM |  | 0.873× | -3.6 | 0.013 | 10/48 (Hs 766T, NCI-H661, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.885× | -3.4 | 0.024 | 10/47 (Hs 766T, NCI-H2030, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.888× | -3.3 | 0.032 | 19/47 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.806×** | -3.2 | 0.050 | 10/46 (MIA PaCa-2, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.895× | -3.1 | 0.053 | 8/46 (SNU-423, LS 180, …) | rises with dose |  |
| [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | 0.896× | -3.1 | 0.054 | 11/47 (SW 1271, H4, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.892× | -3.1 | 0.054 | 9/46 (CFPAC-1, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.898× | -3.0 | 0.065 | 16/47 (H4, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.891× | -3.0 | 0.065 | 11/46 (HS-578T, H4, …) | inconsistent across doses | low cells (technical?) |
| [[LJI308 (drug)]] 0.05 µM |  | 0.894× | -3.0 | 0.072 | 6/47 (SHP-77, NCI-H661, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11350. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 76.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 40.0 | 0 | 3 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.114× (z -11.7) ⚠ toxic |
| [[A-427 (line)]] | wt | 76.6 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.530× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 59.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -16.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 78.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.473× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -9.2) |
| [[SHP-77 (line)]] | alt | 102 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -16.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 47.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.417× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 72.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -14.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 63.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -9.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.442× (z -12.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 66.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.397× (z -9.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 53.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -14.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 45.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.421× (z -9.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 56.5 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.229× (z -8.9) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 49.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.413× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 70.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 50.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.412× (z -12.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 61.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.419× (z -11.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 63.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -17.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 56.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 46.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -9.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 81.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -10.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 101 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 49.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 93.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11350), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPA2]] | +0.70 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[ORC5]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[SRBD1]] | +0.61 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[SMYD4]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RFWD3]] | +0.58 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[RFC2]] | +0.58 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[MIS18A]] | +0.58 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[DDX19A]] | +0.57 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[POLA2]] | +0.57 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[HAUS7]] | +0.57 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[WDHD1]] | +0.57 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[NUP107]] | +0.57 | +0.54 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN1-AS1]] | -0.58 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[YPEL5]] | -0.55 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[KCP]] | -0.53 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[PSAP]] | -0.51 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[RTCA-AS1]] | -0.51 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[PACRG]] | -0.51 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[MKLN1-AS]] | -0.51 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[RBM24]] | -0.51 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[RNF11]] | -0.50 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[ATP6V1B2]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[TTC39A]] | -0.49 | -0.39 / -0.47 | both halves | 5e-05 | same gene group |
| [[ARL14EP-DT]] | -0.49 | -0.31 / -0.34 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MRAS]] | B | MRAS activity raises CNOT10's level | lines that do not express MRAS (11) vs lines expressing it (39) | 1.38× lower at baseline in the lines without MRAS | 0.037 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[HDAC6]] | B | HDAC6 activity lowers CNOT10's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.484). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-37.6, -38.9); signed map (-29.7, -51.3). **Vector** length 94.3, 20.8% of its response variance represented; |z| ≥ 3 in 839 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.3 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.4 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +2.4 | +3.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +2.4 | +8.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.6 | +1.9 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.6 | +2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.5 | +1.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +2.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.3 | -4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.6 | -13.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -0.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.5 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | CCR4-NOT transcription complex subunit 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.3 — chr3:32,685,145-32,773,875 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12890, FLJ13165 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; CCR4-NOT transcription complex |
| Reactome | 8 pathways, smallest: TP53 regulates transcription of additional cell cycle genes whose exact role in the p53 pathway remain uncertain; Deadenylation of mRNA; M-decay: degradation of maternal mRNAs by maternally stored factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9A5](https://www.uniprot.org/uniprotkb/Q9H9A5) (CCR4-NOT transcription complex subunit 10):

> Component of the CCR4-NOT complex which is one of the major cellular mRNA deadenylases and is linked to various cellular processes including bulk mRNA degradation, miRNA-mediated repression, translational repression during translational initiation and general transcription regulation. Additional complex functions may be a consequence of its influence on mRNA expression. Is not required for association of CNOT7 to the CCR4-NOT complex.

**Summary**, from NCBI Gene [25904](https://www.ncbi.nlm.nih.gov/gene/25904):

> Predicted to be involved in mRNA catabolic process and negative regulation of translation. Located in membrane. Part of CCR4-NOT complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23817](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23817) · Entrez [25904](https://www.ncbi.nlm.nih.gov/gene/25904) · UniProt [Q9H9A5](https://www.uniprot.org/uniprotkb/Q9H9A5) · Ensembl [ENSG00000182973](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182973)

## Data

Gene col 11350: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11350); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11350, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11350]; `tensor/DDL_lfc|DDL_z.npy` [11350]; `embed/gene_vectors.npy` [11350]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11350 or target_col == 11350). Every well: [[CNOT10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNOT10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

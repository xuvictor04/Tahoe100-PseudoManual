---
symbol: "TOB2"
type: "gene"
col: 11468
ensembl_id: "ENSG00000183864"
name: "transducer of ERBB2, 2"
location: "22q13.2"
module: 93
arm: "+"
pooled_cpm: 71.66
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# TOB2

*transducer of ERBB2, 2* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.14× (z +16.4, q 0e+00, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.431× (z -6.7, q 1e-08, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC10A3]] (+0.66, fdr 1e-05), [[ZNF335]] (+0.63, fdr 1e-05), [[SMIM4]] (+0.62, fdr 1e-05); moves opposite to [[DLD]] (-0.64, fdr 7e-06), [[FAM98B]] (-0.60, fdr 1e-05), [[HSD17B4]] (-0.60, fdr 1e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11468.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +16.4 | 0e+00 | 46/49 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.75×** | +12.1 | 4e-31 | 35/48 (HOP62, C32, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +11.2 | 8e-27 | 45/47 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.97×** | +10.3 | 9e-23 | 42/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +8.4 | 8e-15 | 40/48 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +8.2 | 2e-14 | 40/50 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.60×** | +7.2 | 5e-11 | 34/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +6.1 | 6e-08 | 38/48 (SW48, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.44×** | +5.5 | 2e-06 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.9 | 7e-05 | 34/48 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.37×** | +4.8 | 8e-05 | 31/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.35×** | +4.5 | 3e-04 | 30/48 (KATO III, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.32×** | +4.2 | 0.001 | 28/48 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.30×** | +4.0 | 0.002 | 27/48 (NCI-H1573, NCI-H1792, …) | two highest doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 1.18× | +3.6 | 0.011 | 19/49 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.071 | 19/48 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11468.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.431×** | -6.7 | 1e-08 | 39/49 (A498, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.746×** | -4.5 | 0.002 | 29/49 (NCI-H2347, SW48, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -4.0 | 0.010 | 25/48 (CFPAC-1, HS-578T, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.648×** | -3.5 | 0.075 | 24/48 (RKO, A-172, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11468. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 44.8 | 10 (7 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +16.3) | — |
| [[SW480 (line)]] | alt | 57.4 | 7 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +15.7) | — |
| [[HOP62 (line)]] | alt | 63.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +19.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +17.2) | — |
| [[LoVo (line)]] | wt | 74.4 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +11.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +8.7) | — |
| [[A498 (line)]] | wt | 83.9 | 2 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +11.2) | [[TAK-901 (drug)]] 5 µM 0.213× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 77.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +15.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +12.6) | — |
| [[C32 (line)]] | wt | 75.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.13× (z +18.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +13.0) | — |
| [[HS-578T (line)]] | alt | 59.3 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +13.6) | — |
| [[hTERT-HPNE (line)]] | wt | 76.5 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +11.5) | [[Ixazomib citrate (drug)]] 5 µM 0.376× (z -8.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 52.4 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +14.8) | — |
| [[KATO III (line)]] | alt | 79.8 | 4 (3 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.21× (z +14.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +12.5) | — |
| [[LOX-IMVI (line)]] | wt | 54.6 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +13.0) | — |
| [[PANC-1 (line)]] | alt | 56.3 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +15.7) | — |
| [[RKO (line)]] | wt | 92.6 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +12.9) | — |
| [[SK-MEL-2 (line)]] | alt | 226 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +17.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.61× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 105 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +14.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.7) | — |
| [[SW48 (line)]] | wt | 89.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +11.0) | — |
| [[A-172 (line)]] | wt | 40.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -9.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[COLO 205 (line)]] | alt | 42.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +12.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[H4 (line)]] | wt | 50.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 77.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 65.5 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.82× (z +11.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 73.1 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +11.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 83.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +13.1) | — |
| [[NCI-H1573 (line)]] | alt | 99.2 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.78× (z +13.4) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 52.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +13.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 62.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +8.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 60.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +11.9) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.362× (z -10.3) |
| [[A549 (line)]] | wt | 50.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +15.7) | — |
| [[BT-474 (line)]] | alt | 79.0 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.130× (z -9.6) ⚠ toxic |
| [[C-33 A (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 107 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.70× (z +8.5) ⚠ toxic | — |
| [[HEC-1-A (line)]] | alt | 90.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.22× (z +8.5) ⚠ toxic | — |
| [[NCI-H2030 (line)]] | alt | 76.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 70.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.45× (z +8.5) ⚠ toxic | — |
| [[Panc 03.27 (line)]] | alt | 66.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 57.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +8.5) | — |
| [[SW 1271 (line)]] | alt | 64.9 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0880× (z -8.7) |
| [[SW1417 (line)]] | alt | 79.7 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +10.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 92.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 72.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11468), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC10A3]] | +0.66 | +0.50 / +0.74 | both halves | 1e-05 |  |
| [[ZNF335]] | +0.63 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[SMIM4]] | +0.62 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[POLR2A]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[DALRD3]] | +0.61 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[FAM53C]] | +0.61 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[HIC2]] | +0.60 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[WDR47]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[INTS6L]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[BRD2]] | +0.56 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[RSRP1]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CATSPERG]] | +0.54 | +0.58 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLD]] | -0.64 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[FAM98B]] | -0.60 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[HSD17B4]] | -0.60 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[MRPL42]] | -0.60 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[RAD23B]] | -0.60 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[COA1]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[SAAL1]] | -0.58 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[BLMH]] | -0.57 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[LYPLAL1]] | -0.55 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[AGK]] | -0.55 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[ALKBH8]] | -0.54 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[RPP30]] | -0.54 | -0.62 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TOB2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FZD7]] | C | FZD7 activity raises TOB2's level | lines that do not express FZD7 (3) vs lines expressing it (47) | 1.60× lower at baseline in the lines without FZD7 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: SPDL1, HOMER3, RBMS2; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.1, -24.7); signed map (3.8, 14.7). **Vector** length 122, 38.1% of its response variance represented; |z| ≥ 3 in 1,078 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +16.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.7 | +10.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +11.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +8.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | +3.6 | +3.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -11.4 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.2 | +0.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -9.0 | -6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -8.9 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.6 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.6 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.8 | -3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.6 | -1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | transducer of ERBB2, 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:41,433,494-41,446,801 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TOBL, TOB4, bK223H9, APRO5; previously TROB2 |
| Gene groups (HGNC) | BTG/Tob family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14106](https://www.uniprot.org/uniprotkb/Q14106) (Protein Tob2):

> Anti-proliferative protein inhibits cell cycle progression from the G0/G1 to S phases.

**Summary**, from NCBI Gene [10766](https://www.ncbi.nlm.nih.gov/gene/10766):

> TOB2 belongs to the TOB (see TOB1; MIM 605523)/BTG1 (MIM 109580) family of antiproliferative proteins, which are involved in the regulation of cell cycle progression.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:11980](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11980) · Entrez [10766](https://www.ncbi.nlm.nih.gov/gene/10766) · UniProt [Q14106](https://www.uniprot.org/uniprotkb/Q14106) · Ensembl [ENSG00000183864](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183864)

## Data

Gene col 11468: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11468); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11468, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11468]; `tensor/DDL_lfc|DDL_z.npy` [11468]; `embed/gene_vectors.npy` [11468]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11468 or target_col == 11468). Every well: [[TOB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

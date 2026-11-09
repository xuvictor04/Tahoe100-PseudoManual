---
symbol: "EIF4EBP2"
type: "gene"
col: 7310
ensembl_id: "ENSG00000148730"
name: "eukaryotic translation initiation factor 4E binding protein 2"
location: "10q22.1"
module: 12
arm: "-"
pooled_cpm: 53.84
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# EIF4EBP2

*eukaryotic translation initiation factor 4E binding protein 2* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.88× (z +20.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.700× (z -6.8, q 6e-09, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK2]] (+0.62, fdr 1e-05), [[CD164]] (+0.61, fdr 3e-05), [[TMBIM6]] (+0.60, fdr 1e-05); moves opposite to [[MRPL46]] (-0.65, fdr 4e-05), [[SNHG32]] (-0.63, fdr 1e-05), [[RBMX2]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7310.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.88×** | +20.1 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.74×** | +19.2 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.52×** | +16.9 | 0e+00 | 38/41 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.39×** | +16.6 | 0e+00 | 47/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +15.3 | 0e+00 | 41/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +13.1 | 3e-37 | 40/46 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +8.8 | 1e-16 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.56×** | +7.8 | 4e-13 | 28/43 (SW1417, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +6.9 | 4e-10 | 29/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.44×** | +6.7 | 1e-09 | 25/48 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +6.5 | 5e-09 | 25/48 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +5.9 | 2e-07 | 27/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.77×** | +5.7 | 6e-07 | 32/48 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.36×** | +5.6 | 8e-07 | 26/49 (NCI-H460, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.27×** | +4.6 | 2e-04 | 24/48 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.25×** | +4.2 | 8e-04 | 23/48 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.2 | 9e-04 | 16/48 (SW480, BT-474, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.003 | 16/48 (HOP62, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.010 | 11/48 (A498, LoVo, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.18× | +3.2 | 0.033 | 12/48 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.17× | +2.9 | 0.069 | 12/48 (SNU-423, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7310.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.700×** | -6.8 | 6e-09 | 35/48 (PANC-1, COLO 205, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.763×** | -5.2 | 7e-05 | 26/48 (H4, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.644×** | -4.4 | 0.002 | 27/49 (PANC-1, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.653×** | -4.2 | 0.003 | 23/48 (HOP62, H4, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.662×** | -4.1 | 0.004 | 20/48 (KATO III, LS 180, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.864× | -3.9 | 0.007 | 14/48 (SW480, A-427, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.808×** | -3.9 | 0.007 | 23/48 (NCI-H2030, A-427, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.810×** | -3.8 | 0.010 | 19/48 (COLO 205, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.817×** | -3.7 | 0.013 | 18/48 (AN3 CA, C-33 A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.831×** | -3.5 | 0.022 | 18/48 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.836× | -3.4 | 0.032 | 15/48 (SW1417, HT-29, …) | inconsistent across doses |  |
| [[Pemigatinib (drug)]] 0.05 µM |  | 0.845× | -3.0 | 0.11 | 9/48 (MIA PaCa-2, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7310. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 42.6 | 8 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.96× (z +17.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 47.5 | 6 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.32× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +12.6) | — |
| [[NCI-H1792 (line)]] | alt | 35.7 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +11.5) | — |
| [[A-172 (line)]] | wt | 45.9 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.20× (z +11.6) | — |
| [[A-427 (line)]] | wt | 61.0 | 3 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.59× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.356× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.533× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 38.7 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.85× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 34.9 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.29× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 32.3 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.86× (z +10.2) | — |
| [[A549 (line)]] | wt | 32.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +11.1) | — |
| [[HOP62 (line)]] | alt | 56.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.67× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 51.7 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.70× (z +12.3) | — |
| [[NCI-H2030 (line)]] | alt | 38.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.01× (z +10.2) | [[Harringtonine (drug)]] 5 µM 0.382× (z -8.7) ⚠ cell-cycle shift, explains ~8% of this change |
| [[PANC-1 (line)]] | alt | 54.7 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.76× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 45.8 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.42× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 45.9 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.16× (z +9.5) | — |
| [[SW480 (line)]] | alt | 90.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.27× (z +16.1) | — |
| [[C32 (line)]] | wt | 36.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +13.0) | — |
| [[HepG2_C3A (line)]] | wt | 67.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.26× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 46.5 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.13× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.14× (z +9.8) | — |
| [[KATO III (line)]] | alt | 89.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.32× (z +9.4) | — |
| [[LoVo (line)]] | wt | 65.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.59× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 51.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.99× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 36.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.07× (z +8.7) | — |
| [[A498 (line)]] | wt | 44.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.11× (z +11.9) | — |
| [[SW 900 (line)]] | alt | 63.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.06× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 69.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +9.8) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 47.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 76.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +11.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 23.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +9.4) | — |
| [[NCI-H661 (line)]] | alt | 55.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.111× (z -8.5) ⚠ transcription drop |
| [[Panc 03.27 (line)]] | alt | 41.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.8) | — |
| [[RKO (line)]] | wt | 30.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +11.4) | — |
| [[SHP-77 (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Torkinib (drug)]] 5 µM 0.0939× (z -8.7) ⚠ toxic |
| [[SW1417 (line)]] | alt | 89.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.54× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW48 (line)]] | wt | 74.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 91.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 82.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7310), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK2]] | +0.62 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[CD164]] | +0.61 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[TMBIM6]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[PRPS2]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[PRKACA]] | +0.60 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[MMGT1]] | +0.60 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[BAG6]] | +0.60 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[TM9SF3]] | +0.60 | +0.31 / +0.60 | both halves | 2e-04 |  |
| [[GPAA1]] | +0.60 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[LY6G5B]] | +0.58 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[GNG12]] | +0.58 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[PPP1CA]] | +0.58 | +0.61 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 6 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL46]] | -0.65 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[SNHG32]] | -0.63 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[RBMX2]] | -0.63 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[RBM27]] | -0.63 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[NOL7]] ⚠ | -0.63 | -0.66 / -0.58 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RP9]] | -0.63 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[TAF1D]] | -0.61 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[MRPL21]] | -0.60 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[C18orf21]] | -0.60 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[PUS3]] | -0.60 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[LSM10]] | -0.60 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[MRPS31]] | -0.59 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[EPB41L4A-AS1]] | -0.59 | -0.52 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises EIF4EBP2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.608). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.9, -10.3); signed map (-26.9, -40.0). **Vector** length 102, 26.9% of its response variance represented; |z| ≥ 3 in 1,154 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +13.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +6.5 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +16.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +6.2 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +6.0 | +7.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +3.8 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | +2.1 | +1.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.9 | +1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +4.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.9 | -5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.8 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.8 | -6.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -4.5 | -3.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.9 | -4.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 4E binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:70,404,145-70,428,618 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13542](https://www.uniprot.org/uniprotkb/Q13542) (Eukaryotic translation initiation factor 4E-binding protein 2):

> Repressor of translation initiation involved in synaptic plasticity, learning and memory formation. Regulates EIF4E activity by preventing its assembly into the eIF4F complex: hypophosphorylated form of EIF4EBP2 competes with EIF4G1/EIF4G3 and strongly binds to EIF4E, leading to repress translation. In contrast, hyperphosphorylated form dissociates from EIF4E, allowing interaction between EIF4G1/EIF4G3 and EIF4E, leading to initiation of translation. EIF4EBP2 is enriched in brain and acts as a …

**Summary**, from NCBI Gene [1979](https://www.ncbi.nlm.nih.gov/gene/1979):

> This gene encodes a member of the eukaryotic translation initiation factor 4E binding protein family. The gene products of this family bind eIF4E and inhibit translation initiation. However, insulin and other growth factors can release this inhibition via a phosphorylation-dependent disruption of their binding to eIF4E. Regulation of protein production through these gene products have been implicated in cell proliferation, cell differentiation and viral infection. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:3289](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3289) · Entrez [1979](https://www.ncbi.nlm.nih.gov/gene/1979) · UniProt [Q13542](https://www.uniprot.org/uniprotkb/Q13542) · Ensembl [ENSG00000148730](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148730)

## Data

Gene col 7310: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7310); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7310, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7310]; `tensor/DDL_lfc|DDL_z.npy` [7310]; `embed/gene_vectors.npy` [7310]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7310 or target_col == 7310). Every well: [[EIF4EBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF4EBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

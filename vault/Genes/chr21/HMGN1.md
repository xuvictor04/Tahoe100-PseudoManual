---
symbol: "HMGN1"
type: "gene"
col: 12992
ensembl_id: "ENSG00000205581"
name: "high mobility group nucleosome binding domain 1"
location: "21q22.2"
module: 3
arm: "-"
pooled_cpm: 52.29
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# HMGN1

*high mobility group nucleosome binding domain 1* — 21q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.42× (z +23.0, q 0e+00, up in 47 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.30× (z +5.9, q 2e-07, up in 31 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGN2]] (+0.70, fdr 7e-06), [[ACADM]] (+0.64, fdr 1e-05), [[HNRNPA3]] (+0.64, fdr 3e-05); moves opposite to [[RPP21]] (-0.65, fdr 1e-05), [[ZXDC]] (-0.64, fdr 1e-05), [[DNLZ]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 19 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12992.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.42×** | +23.0 | 0e+00 | 47/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.75×** | +19.7 | 0e+00 | 41/41 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.29×** | +17.1 | 0e+00 | 44/44 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.80×** | +8.8 | 2e-16 | 40/47 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.48×** | +8.6 | 7e-16 | 37/48 (AsPC-1, A549, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.67×** | +8.0 | 1e-13 | 43/47 (HOP62, SW 900, …) | all doses, flat | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.66×** | +7.8 | 4e-13 | 42/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.65×** | +7.8 | 4e-13 | 40/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.24×** | +6.5 | 4e-09 | 40/49 (AsPC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +5.9 | 2e-07 | 31/48 (NCI-H1573, HCT15, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.45×** | +5.5 | 2e-06 | 31/48 (NCI-H1573, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.6 | 2e-04 | 28/47 (CFPAC-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.35×** | +4.6 | 2e-04 | 25/48 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.33×** | +4.5 | 3e-04 | 28/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.33×** | +4.4 | 4e-04 | 27/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.30×** | +4.2 | 0.001 | 28/48 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.58×** | +3.7 | 0.007 | 19/48 (HEC-1-A, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.013 | 21/48 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.023 | 21/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12992.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~91% of this change | 0.788× | -3.2 | 0.75 | 17/48 (A-427, PANC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12992. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.5 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +16.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 34.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.56× (z +15.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 30.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +14.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 43.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +12.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 65.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +13.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 42.8 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +13.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 61.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.89× (z +16.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 43.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.13× (z +17.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 74.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +17.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 64.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +15.9) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 42.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +13.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 72.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +15.3) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 52.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +17.2) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 43.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +11.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 41.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.96× (z +13.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 46.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +14.3) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 52.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +13.3) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 54.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +14.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 52.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +14.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 60.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +14.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 21.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.13× (z +13.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 81.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.99× (z +9.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 52.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +13.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 59.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +17.5) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 68.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.10× (z +12.3) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 53.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +10.5) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 63.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.41× (z +11.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 43.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +10.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 53.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.35× (z +17.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 37.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.47× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 56.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 17.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.17× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 43.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +12.6) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 66.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +11.2) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 47.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +12.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 76.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +13.0) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 43.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +9.8) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 28.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 59.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +18.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 34.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.52× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 35.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +11.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12992), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGN2]] | +0.70 | +0.67 / +0.72 | both halves | 7e-06 | same gene group; STRING 994 |
| [[ACADM]] | +0.64 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[HNRNPA3]] | +0.64 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[HNRNPM]] | +0.64 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[DHFR]] | +0.62 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[ALG10B]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ERLIN2]] | +0.62 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[CBX5]] | +0.62 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[DR1]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[TOP2B]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[DDX3X]] | +0.59 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[HNRNPU]] | +0.58 | +0.63 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP21]] | -0.65 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[ZXDC]] | -0.64 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[DNLZ]] | -0.63 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[SNAPC2]] | -0.61 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[GAS5]] | -0.60 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[RNF181]] | -0.60 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[EPS15L1]] | -0.58 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[EXOSC1]] | -0.57 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[HM13]] | -0.57 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[ZNRD2]] | -0.57 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[RPS15]] ⚠ | -0.57 | -0.56 / -0.47 | both halves | 2e-05 | STRING 941; ⚠ in the vector space only through flagged drug-doses |
| [[RPS13]] ⚠ | -0.57 | -0.57 / -0.48 | both halves | 2e-05 | STRING 821; ⚠ in the vector space only through flagged drug-doses |
| [[ADRM1]] | -0.56 | -0.25 / -0.58 | both halves | 4e-04 |  |
| [[CIAO2B]] | -0.56 | -0.58 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.623). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.6, -23.1); signed map (15.8, -36.6). **Vector** length 76.6, 18.7% of its response variance represented; |z| ≥ 3 in 918 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.52 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.1 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +17.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +19.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +23.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.9 | +4.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | +4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | -0.8 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | +1.7 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +0.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.5 | +0.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~91% of this change | -5.2 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.2 | -1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.4 | -0.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.3 | -2.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | high mobility group nucleosome binding domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.2 — chr21:39,342,315-39,349,647 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ27265, FLJ31471, MGC104230, MGC117425; previously HMG14 |
| Gene groups (HGNC) | Canonical high mobility group |
| Matched by | ensembl_id |

**Function**, from UniProt [P05114](https://www.uniprot.org/uniprotkb/P05114) (Non-histone chromosomal protein HMG-14):

> Binds to the inner side of the nucleosomal DNA thus altering the interaction between the DNA and the histone octamer. May be involved in the process which maintains transcribable genes in a unique chromatin conformation. Inhibits the phosphorylation of nucleosomal histones H3 and H2A by RPS6KA5/MSK1 and RPS6KA3/RSK2 (By similarity).

**Summary**, from NCBI Gene [3150](https://www.ncbi.nlm.nih.gov/gene/3150):

> The protein encoded by this gene binds nucleosomal DNA and is associated with transcriptionally active chromatin. Along with a similar protein, HMG17, the encoded protein may help maintain an open chromatin configuration around transcribable genes. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:4984](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4984) · Entrez [3150](https://www.ncbi.nlm.nih.gov/gene/3150) · UniProt [P05114](https://www.uniprot.org/uniprotkb/P05114) · Ensembl [ENSG00000205581](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205581)

## Data

Gene col 12992: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12992); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12992, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12992]; `tensor/DDL_lfc|DDL_z.npy` [12992]; `embed/gene_vectors.npy` [12992]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12992 or target_col == 12992). Every well: [[HMGN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

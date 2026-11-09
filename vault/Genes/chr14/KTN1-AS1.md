---
symbol: "KTN1-AS1"
type: "gene"
col: 11836
ensembl_id: "ENSG00000186615"
name: "KTN1 antisense RNA 1"
location: "14q22.3"
module: 5
arm: "+"
pooled_cpm: 14.32
n_lines_expressing: 48
n_dd_up: 26
n_dd_down: 14
n_dd_up_clean: 17
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# KTN1-AS1

*KTN1 antisense RNA 1* — 14q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.82× (z +26.6, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.449× (z -11.3, q 1e-26, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GABPB1-AS1]] (+0.62, fdr 4e-05), [[PCOLCE2]] (+0.59, fdr 1e-05), [[TBC1D30]] (+0.58, fdr 1e-05); moves opposite to [[SENP2]] (-0.58, fdr 2e-05), [[FN3KRP]] (-0.56, fdr 9e-05), [[INIP]] (-0.56, fdr 9e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11836.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.82×** | +26.6 | 0e+00 | 44/45 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +10.0 | 4e-21 | 34/44 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.83×** | +7.9 | 4e-13 | 29/46 (NCI-H1573, A-172, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +7.9 | 5e-13 | 30/46 (A-172, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +7.2 | 7e-11 | 29/44 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +6.7 | 2e-09 | 19/46 (Hs 766T, MIA PaCa-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.3 | 1e-05 | 23/45 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.45×** | +5.2 | 1e-05 | 17/45 (LOX-IMVI, CFPAC-1, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +5.2 | 1e-05 | 20/42 (RPMI-7951, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.02×** | +5.2 | 1e-05 | 16/46 (NCI-H1573, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.41×** | +4.8 | 1e-04 | 19/45 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +4.0 | 0.003 | 9/22 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.33×** | +4.0 | 0.003 | 19/45 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **1.34×** | +3.9 | 0.004 | 16/37 (CFPAC-1, SW1417, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.004 | 13/44 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.005 | 11/46 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 1.20× | +3.6 | 0.010 | 12/46 (CFPAC-1, Hs 766T, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.027 | 9/44 (NCI-H2030, SNU-423, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.031 | 16/44 (CHP-212, HOP62, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.049 | 10/45 (NCI-H23, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11836.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.449×** | -11.3 | 1e-26 | 31/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.620×** | -9.5 | 5e-19 | 28/45 (C32, C-33 A, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.509×** | -9.5 | 5e-19 | 29/44 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.279×** | -9.4 | 1e-18 | 34/46 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.392×** | -6.9 | 7e-10 | 29/42 (C32, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.625×** | -6.6 | 3e-09 | 24/45 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.627×** | -6.3 | 2e-08 | 23/40 (A-427, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.689×** | -5.2 | 1e-05 | 23/44 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.719×** | -4.6 | 2e-04 | 16/46 (AN3 CA, NCI-H2030, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.764×** | -3.8 | 0.009 | 10/45 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.768×** | -3.5 | 0.025 | 12/46 (PANC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.788×** | -3.2 | 0.058 | 15/44 (NCI-H1792, LOX-IMVI, …) | top dose only | composition shift |
| [[Retinoic acid (drug)]] 5 µM |  | 0.853× | -3.2 | 0.064 | 7/46 (MIA PaCa-2, NCI-H661, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.800×** | -3.1 | 0.064 | 8/45 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.788×** | -3.1 | 0.064 | 9/46 (SW 1271, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11836. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 23.6 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -14.2) |
| [[NCI-H1573 (line)]] | alt | 23.7 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +10.5) | [[Digitoxin (drug)]] 0.5 µM 0.133× (z -13.7) |
| [[NCI-H23 (line)]] | alt | 51.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.306× (z -9.1) |
| [[A-427 (line)]] | wt | 22.3 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0645× (z -19.1) ⚠ toxic · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -10.0) |
| [[C-33 A (line)]] | alt | 56.0 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0717× (z -16.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 9.30 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.31× (z +14.2) | [[Digitoxin (drug)]] 5 µM 0.182× (z -11.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 14.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +12.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 12.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +11.1) | [[Digitoxin (drug)]] 5 µM 0.250× (z -9.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 9.88 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.0939× (z -10.2) ⚠ cell-cycle shift, explains ~90% of this change |
| [[A498 (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A549 (line)]] | wt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.84× (z +12.2) | — |
| [[AsPC-1 (line)]] | alt | 4.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.28× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 16.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.94× (z +8.5) | — |
| [[C32 (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -12.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[CFPAC-1 (line)]] | alt | 5.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.11× (z +11.7) | — |
| [[CHP-212 (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0478× (z -9.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[HCT15 (line)]] | alt | 9.14 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0592× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +12.7) | — |
| [[HepG2_C3A (line)]] | wt | 8.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +12.2) | — |
| [[Hs 766T (line)]] | wt | 18.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 6.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 25.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.259× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 23.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +10.8) | — |
| [[NCI-H2347 (line)]] | alt | 4.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 6.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.97× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 4.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.67× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -9.2) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SNU-423 (line)]] | alt | 5.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.63× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 6.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +9.9) | — |
| [[A-172 (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11836), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABPB1-AS1]] | +0.62 | +0.61 / +0.42 | both halves | 4e-05 | same gene group |
| [[PCOLCE2]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[TBC1D30]] | +0.58 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[SPOPL-DT]] | +0.58 | +0.59 / +0.36 | both halves | 1e-04 |  |
| [[GPR135]] | +0.57 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[SLC16A1-AS1]] | +0.57 | +0.62 / +0.40 | both halves | 4e-05 | same gene group |
| [[TXN]] | +0.57 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[LINC01357]] | +0.57 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[EPM2A]] | +0.55 | +0.56 / +0.22 | both halves | 6e-04 |  |
| [[L3HYPDH]] | +0.55 | +0.59 / +0.35 | both halves | 1e-04 |  |
| [[KCTD15]] | +0.53 | +0.38 / +0.36 | both halves | 1e-04 |  |
| [[ABCC1]] | +0.53 | +0.47 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SENP2]] | -0.58 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[FN3KRP]] | -0.56 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[INIP]] | -0.56 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[IK]] | -0.56 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[ALAD]] | -0.55 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[NAGK]] | -0.53 | -0.48 / -0.27 | both halves | 3e-04 |  |
| [[AGFG2]] | -0.51 | -0.40 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[MMUT]] | -0.51 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[SNAP29]] | -0.50 | -0.25 / -0.29 | both halves | 4e-04 |  |
| [[CCNDBP1]] | -0.50 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[MIGA2]] | -0.50 | -0.44 / -0.23 | both halves | 5e-04 |  |
| [[TBC1D10A]] | -0.50 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[GPATCH11]] | -0.49 | -0.31 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KTN1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TRABD2B]] | B | TRABD2B activity raises KTN1-AS1's level | lines that do not express TRABD2B (19) vs lines expressing it (31) | 1.77× lower at baseline in the lines without TRABD2B | 0.040 | ⚠ within organs, on part of the lines; also absent: FAM110B, ULK2, COL4A4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.474). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (21.8, -22.7); signed map (1.6, -57.6). **Vector** length 73.0, 14.0% of its response variance represented; |z| ≥ 3 in 1,049 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +26.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.1 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +6.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +2.8 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -3.9 | +3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.6 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -3.5 | -9.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.6 | +4.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -6.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.4 | -3.8 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | KTN1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q22.3 — chr14:55,496,786-55,580,888 (-) |
| Ensembl biotype | lncRNA |
| Also known as | MYCLo-3; previously C14orf33 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q86SY8](https://www.uniprot.org/uniprotkb/Q86SY8) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:19842](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19842) · Entrez [100129075](https://www.ncbi.nlm.nih.gov/gene/100129075) · UniProt [Q86SY8](https://www.uniprot.org/uniprotkb/Q86SY8) · Ensembl [ENSG00000186615](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186615)

## Data

Gene col 11836: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11836); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11836, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11836]; `tensor/DDL_lfc|DDL_z.npy` [11836]; `embed/gene_vectors.npy` [11836]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11836 or target_col == 11836). Every well: [[KTN1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KTN1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

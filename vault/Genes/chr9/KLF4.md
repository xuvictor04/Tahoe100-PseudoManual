---
symbol: "KLF4"
type: "gene"
col: 5911
ensembl_id: "ENSG00000136826"
name: "KLF transcription factor 4"
location: "9q31.2"
module: 123
arm: "+"
pooled_cpm: 22.56
n_lines_expressing: 44
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 19
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# KLF4

*KLF transcription factor 4* — 9q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.68× (z +14.0, q 6e-42, up in 37 of 41 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.87× (z +10.6, q 9e-24, up in 35 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.678× (z -3.8, q 0.096, down in 20 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (Hs 766T 0.0410×, HT-29 0.155×, KATO III 0.258×, SW1417 0.269×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW1417 0.175×, HT-29 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-172 0.0831×, KATO III 0.335×; ⚠ toxic; transcription drop); [[Pimozide (drug)]] 0.05 µM in 1 line (SNU-423 0.0679×); [[Trimetrexate (drug)]] 0.5 µM in 1 line (H4 0.0527×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.323×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATF3]] (+0.68, fdr 7e-06), [[OSR2]] (+0.67, fdr 7e-06), [[ZFP36L2]] (+0.64, fdr 1e-05); moves opposite to [[PGS1]] (-0.56, fdr 1e-05), [[STARD3]] (-0.55, fdr 1e-05), [[BCAP31]] (-0.55, fdr 1e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[IL15]] → it (grade B ⚠); 19 go from it, the strongest it → [[CERS5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5911.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.68×** | +14.0 | 6e-42 | 37/41 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.87×** | +10.6 | 9e-24 | 35/40 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.82×** | +10.4 | 3e-23 | 36/41 (NCI-H460, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.76×** | +9.8 | 1e-20 | 36/41 (NCI-H460, J82, …) | two highest doses | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +6.8 | 9e-10 | 31/42 (SW1417, HepG2/C3A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.91×** | +6.5 | 8e-09 | 30/42 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.40×** | +6.4 | 1e-08 | 28/42 (NCI-H460, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.73×** | +5.5 | 3e-06 | 25/40 (NCI-H460, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.72×** | +5.5 | 3e-06 | 21/40 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.68×** | +5.1 | 2e-05 | 25/42 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.9 | 6e-05 | 20/37 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.37×** | +4.5 | 3e-04 | 25/42 (KATO III, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +4.5 | 3e-04 | 17/41 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.54×** | +4.4 | 5e-04 | 21/41 (NCI-H460, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.1 | 0.001 | 18/36 (MIA PaCa-2, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Gefitinib (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.028 | 10/42 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **1.40×** | +3.3 | 0.030 | 11/42 (COLO 205, NCI-H2347, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | **1.36×** | +2.9 | 0.092 | 7/39 (HEC-1-A, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5911.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (Hs 766T 0.0410×, HT-29 0.155×, KATO III 0.258×, SW1417 0.269×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW1417 0.175×, HT-29 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-172 0.0831×, KATO III 0.335×; ⚠ toxic; transcription drop); [[Pimozide (drug)]] 0.05 µM in 1 line (SNU-423 0.0679×); [[Trimetrexate (drug)]] 0.5 µM in 1 line (H4 0.0527×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.323×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -3.8 | 0.096 | 20/40 (NCI-H460, SW48, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.716× | -3.4 | 0.12 | 12/42 (HepG2/C3A, HT-29, …) | inconsistent across doses | position effect removed |
| [[Olanzapine (drug)]] 5 µM |  | 0.790× | -3.4 | 0.12 | 17/42 (SW1417, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.708× | -3.3 | 0.12 | 17/29 (Hs 766T, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | 0.727× | -3.2 | 0.15 | 17/42 (COLO 205, SW480, …) | inconsistent across doses |  |
| [[Pemetrexed (drug)]] 0.5 µM |  | 0.735× | -3.1 | 0.18 | 16/41 (HEC-1-A, SW480, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5911. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 62.2 | 14 (8 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 10.4× (z +19.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -9.1) |
| [[KATO III (line)]] | alt | 59.8 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.0) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 5 µM 0.258× (z -11.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 42.3 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +11.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.87× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A498 (line)]] | wt | 23.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +10.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.43× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 81.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.34× (z +9.5) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.0410× (z -19.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 19.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.18× (z +12.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.74× (z +8.8) | — |
| [[LoVo (line)]] | wt | 46.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +10.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.08× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 19.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0831× (z -11.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 50.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -11.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 31.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +9.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW 900 (line)]] | alt | 14.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +9.8) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[AsPC-1 (line)]] | alt | 27.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +13.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[BT-474 (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +9.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[C32 (line)]] | wt | 7.11 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.55× (z +10.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[CFPAC-1 (line)]] | alt | 23.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +8.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[H4 (line)]] | wt | 8.77 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.5 µM 0.0527× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 9.96 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.23× (z +10.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[LS 180 (line)]] | wt | 45.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +9.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1573 (line)]] | alt | 33.5 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.81× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 18.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +10.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SNU-1 (line)]] | wt | 35.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 8.19 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0679× (z -9.6) |
| [[A-427 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.59 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.13 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.46 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5911), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATF3]] | +0.68 | +0.75 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 681 |
| [[OSR2]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 | same gene group |
| [[ZFP36L2]] | +0.64 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[SIRT1]] | +0.63 | +0.65 / +0.64 | both halves | 7e-06 | pathway: Adherens junctions interactions; STRING 482 |
| [[NEDD9]] | +0.63 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[RHOB]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TIPARP]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[RHOU]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[GATA6]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 | pathway: Transcriptional regulation of pluripotent stem cells; STRING 635 |
| [[ETS2]] | +0.60 | +0.57 / +0.57 | both halves | 9e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 408 |
| [[MYLIP]] | +0.59 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[IRF1]] | +0.59 | +0.60 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGS1]] | -0.56 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[STARD3]] | -0.55 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[BCAP31]] | -0.55 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[STX16-NPEPL1]] | -0.54 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[CTC-338M12.4]] | -0.54 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[TMEM248]] | -0.52 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[CERS5]] | -0.52 | -0.57 / -0.49 | both halves | 2e-05 |  |
| [[THOC5]] | -0.52 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[FUBP3]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[SNRNP40]] | -0.51 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[NUP43]] | -0.49 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL15]] | B | IL15 activity raises KLF4's level | lines that do not express IL15 (10) vs lines expressing it (40) | 2.70× lower at baseline in the lines without IL15 | 0.003 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[LGALS3]] | B | LGALS3 activity raises KLF4's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 2.32× lower at baseline in the lines without LGALS3 | 0.035 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[NEDD9]] | B | NEDD9 activity raises KLF4's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 1.96× lower at baseline in the lines without NEDD9 | 0.046 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[NFATC2]] | B | NFATC2 activity raises KLF4's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without NFATC2 | 0.046 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[EDN1]] | B | EDN1 activity raises KLF4's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 2.00× lower at baseline in the lines without EDN1 | 0.053 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[EXPH5]] | B | EXPH5 activity raises KLF4's level | lines that do not express EXPH5 (20) vs lines expressing it (30) | 1.84× lower at baseline in the lines without EXPH5 | 0.074 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000243004, GOLT1A |
| [[TXNIP]] | B | TXNIP activity raises KLF4's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 2.41× lower at baseline in the lines without TXNIP | 0.082 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[RASEF]] | B | RASEF activity raises KLF4's level | lines that do not express RASEF (20) vs lines expressing it (30) | 1.74× lower at baseline in the lines without RASEF | 0.090 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[GATA6]] | B | GATA6 activity raises KLF4's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 1.93× lower at baseline in the lines without GATA6 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[TNFAIP3]] | C | TNFAIP3 activity raises KLF4's level | lines that do not express TNFAIP3 (3) vs lines expressing it (47) | 4.59× lower at baseline in the lines without TNFAIP3 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IER3, JAG1, ATXN1; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 19, C 0. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CERS5]] | B | KLF4 activity lowers CERS5's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 1.32× higher at baseline in the lines without KLF4 | 0.008 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |
| [[EXPH5]] | B | KLF4 activity raises EXPH5's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 2.58× lower at baseline in the lines without KLF4 | 0.014 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |
| [[NEDD9]] | B | KLF4 activity raises NEDD9's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 4.39× lower at baseline in the lines without KLF4 | 0.027 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |
| [[XBP1]] | B | KLF4 activity raises XBP1's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 2.20× lower at baseline in the lines without KLF4 | 0.041 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |
| [[BCL2L11]] | B | KLF4 activity raises BCL2L11's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 1.72× lower at baseline in the lines without KLF4 | 0.045 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |
| [[ZFAND5]] | B | KLF4 activity raises ZFAND5's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 1.46× lower at baseline in the lines without KLF4 | 0.050 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |
| [[SMAD7]] | B | KLF4 activity raises SMAD7's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 2.49× lower at baseline in the lines without KLF4 | 0.053 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |
| [[KLF11]] | B | KLF4 activity strengthens KLF11's drug response | lines that do not express KLF4 (6) vs lines expressing it (41) | the lines without KLF4 respond 0.65× as strongly (z diff +1.32); strongest at Homoharringtonine 5 µM: 1.09x vs 3.08x (z diff +6.5) | 0.058 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[BAMBI]] | B | KLF4 activity raises BAMBI's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 3.17× lower at baseline in the lines without KLF4 | 0.060 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |
| [[LMNA]] | B | KLF4 activity raises LMNA's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 2.33× lower at baseline in the lines without KLF4 | 0.060 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |
| [[KLF5]] | B | KLF4 activity raises KLF5's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 2.38× lower at baseline in the lines without KLF4 | 0.063 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |
| cells under [[Cysteamine (hydrochloride) (drug)]] 5 µM | B | KLF4 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express KLF4 (6) vs lines expressing it (42) | the lines without KLF4: 0.85× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.762). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.2, 12.8); signed map (3.9, 21.5). **Vector** length 112, 29.8% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.1 | +10.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.3 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.5 | +14.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.3 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +5.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.1 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +1.1 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -3.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -2.9 | -1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -0.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.3 | -1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.2 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | KLF transcription factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.2 — chr9:107,484,852-107,490,482 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EZF, GKLF |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KLF transcription factors |
| Hallmark sets | KRAS_SIGNALING_UP, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Reactome | 16 pathways, smallest: Synthesis, secretion, and deacylation of Ghrelin; Positive Regulation of CDH1 Gene Transcription; FOXO-mediated transcription of cell cycle genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O43474](https://www.uniprot.org/uniprotkb/O43474) (Krueppel-like factor 4):

> Transcription factor; can act both as activator and as repressor. Binds the 5'-CACCC-3' core sequence. Binds to the promoter region of its own gene and can activate its own transcription. Regulates the expression of key transcription factors during embryonic development. Plays an important role in maintaining embryonic stem cells, and in preventing their differentiation. Required for establishing the barrier function of the skin and for postnatal maturation and maintenance of the ocular …

**Summary**, from NCBI Gene [9314](https://www.ncbi.nlm.nih.gov/gene/9314):

> This gene encodes a protein that belongs to the Kruppel family of transcription factors. The encoded zinc finger protein is required for normal development of the barrier function of skin. The encoded protein is thought to control the G1-to-S transition of the cell cycle following DNA damage by mediating the tumor suppressor gene p53. Mice lacking this gene have a normal appearance but lose weight rapidly, and die shortly after birth due to fluid evaporation resulting from compromised epidermal …

**Accessions** — [HGNC:6348](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6348) · Entrez [9314](https://www.ncbi.nlm.nih.gov/gene/9314) · UniProt [O43474](https://www.uniprot.org/uniprotkb/O43474) · Ensembl [ENSG00000136826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136826)

## Data

Gene col 5911: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5911); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5911, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5911]; `tensor/DDL_lfc|DDL_z.npy` [5911]; `embed/gene_vectors.npy` [5911]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5911 or target_col == 5911). Every well: [[KLF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

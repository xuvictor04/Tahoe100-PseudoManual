---
symbol: "ZMAT2"
type: "gene"
col: 7053
ensembl_id: "ENSG00000146007"
name: "zinc finger matrin-type 2"
location: "5q31.3"
module: 7
arm: "+"
pooled_cpm: 63.26
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ZMAT2

*zinc finger matrin-type 2* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.32× (z +14.1, q 3e-42, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Macitentan (drug)]] 0.5 µM in 1 line (SW 1088 0.0717×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC4A1AP]] (+0.71, fdr 7e-06), [[CRNKL1]] (+0.70, fdr 7e-06), [[SNRNP27]] (+0.68, fdr 7e-06); moves opposite to [[TRABD]] (-0.64, fdr 2e-05), [[MCOLN2]] (-0.63, fdr 1e-05), [[ASIC1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7053.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.32×** | +14.1 | 3e-42 | 48/48 (HEC-1-A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.98×** | +12.0 | 1e-30 | 47/49 (A498, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.64×** | +11.1 | 3e-26 | 40/43 (A498, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.87×** | +10.5 | 2e-23 | 45/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.94×** | +7.8 | 5e-13 | 47/48 (LoVo, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.92×** | +7.7 | 9e-13 | 47/48 (LoVo, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +7.7 | 9e-13 | 44/47 (HT-29, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.95×** | +7.6 | 2e-12 | 46/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +6.9 | 4e-10 | 42/49 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +6.6 | 2e-09 | 41/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.81×** | +6.5 | 3e-09 | 33/45 (HEC-1-A, A498, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.3 | 2e-08 | 38/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +6.2 | 2e-08 | 41/48 (LoVo, BT-474, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.65×** | +5.7 | 4e-07 | 37/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.57×** | +5.3 | 4e-06 | 39/48 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +5.3 | 5e-06 | 43/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +4.1 | 0.001 | 35/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.9 | 0.003 | 33/47 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.018 | 28/48 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.042 | 24/48 (NCI-H1792, AsPC-1, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.046 | 31/48 (LOX-IMVI, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7053.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Macitentan (drug)]] 0.5 µM in 1 line (SW 1088 0.0717×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.827× | -3.2 | 0.78 | 23/48 (SK-MEL-2, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7053. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 50.8 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +15.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.14× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 46.0 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +13.7) | — |
| [[A498 (line)]] | wt | 73.2 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 74.2 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +15.3) | — |
| [[LoVo (line)]] | wt | 65.8 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +13.9) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.52× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 41.7 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +10.5) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 83.0 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +11.8) | — |
| [[A549 (line)]] | wt | 49.3 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 56.1 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +13.1) | — |
| [[LOX-IMVI (line)]] | wt | 42.2 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +10.3) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 56.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 69.3 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +12.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 66.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +11.4) | — |
| [[SW480 (line)]] | alt | 68.9 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +11.4) | — |
| [[A-172 (line)]] | wt | 50.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[AsPC-1 (line)]] | alt | 54.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +15.2) | — |
| [[HT-29 (line)]] | alt | 68.9 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.05× (z +9.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +8.6) | — |
| [[J82 (line)]] | alt | 73.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +11.7) | — |
| [[NCI-H2030 (line)]] | alt | 69.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +11.5) | — |
| [[NCI-H23 (line)]] | alt | 68.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H460 (line)]] | wt | 59.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +11.3) | — |
| [[Panc 03.27 (line)]] | alt | 88.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.8) | — |
| [[RKO (line)]] | wt | 59.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 57.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.17× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 79.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +12.5) | — |
| [[COLO 205 (line)]] | alt | 80.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +8.9) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[KATO III (line)]] | alt | 30.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 61.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2347 (line)]] | alt | 65.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 48.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 67.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.1) | — |
| [[SW 1088 (line)]] | alt | 66.3 | 0 | 1 | — | [[Macitentan (drug)]] 0.5 µM 0.0717× (z -8.5) |
| [[SW 900 (line)]] | alt | 44.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 97.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +11.3) | — |
| [[A-427 (line)]] | wt | 80.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 101 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7053), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC4A1AP]] | +0.71 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[CRNKL1]] | +0.70 | +0.77 / +0.60 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 914 |
| [[SNRNP27]] | +0.68 | +0.78 / +0.61 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 619 |
| [[ZNF830]] | +0.68 | +0.79 / +0.56 | both halves | 1e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 457 |
| [[ZNF189]] | +0.67 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[SNW1]] | +0.67 | +0.77 / +0.58 | both halves | 8e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 898 |
| [[ANKRD49]] | +0.65 | +0.77 / +0.52 | both halves | 1e-05 |  |
| [[FBXO38]] | +0.65 | +0.74 / +0.48 | both halves | 2e-05 |  |
| [[RBM48]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[CCDC90B]] | +0.63 | +0.73 / +0.48 | both halves | 2e-05 |  |
| [[GPS2]] | +0.62 | +0.77 / +0.52 | both halves | 1e-05 |  |
| [[DNAJC8]] | +0.62 | +0.79 / +0.39 | both halves | 5e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRABD]] | -0.64 | -0.70 / -0.47 | both halves | 2e-05 |  |
| [[MCOLN2]] | -0.63 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[ASIC1]] | -0.59 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[METAP1]] | -0.59 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[ANKS6]] | -0.58 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[RSAD1]] | -0.57 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[TXNL4A]] | -0.57 | -0.59 / -0.45 | both halves | 3e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 994 |
| [[PALS2]] | -0.57 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[FAM118A]] | -0.56 | -0.65 / -0.33 | both halves | 1e-04 |  |
| [[LYPLA1]] | -0.56 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[TENT4A]] | -0.55 | -0.69 / -0.44 | both halves | 3e-05 |  |
| [[PACC1]] | -0.55 | -0.57 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZMAT2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.466). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-35.4, 2.8); signed map (1.3, -16.8). **Vector** length 79.4, 25.9% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +4.1 | +10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +6.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.4 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +0.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.0 | +1.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.0 | +1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | +0.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -0.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.1 | -0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger matrin-type 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:140,698,680-140,706,686 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31121, hSNU23, Snu23 |
| Gene groups (HGNC) | Zinc fingers matrin-type; Spliceosomal B complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NC0](https://www.uniprot.org/uniprotkb/Q96NC0) (Zinc finger matrin-type protein 2):

> Involved in pre-mRNA splicing as a component of the spliceosome.

**Summary**, from NCBI Gene [153527](https://www.ncbi.nlm.nih.gov/gene/153527):

> Predicted to enable DNA binding activity and zinc ion binding activity. Involved in mRNA splicing, via spliceosome. Located in nucleus. Part of U2-type precatalytic spliceosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26433](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26433) · Entrez [153527](https://www.ncbi.nlm.nih.gov/gene/153527) · UniProt [Q96NC0](https://www.uniprot.org/uniprotkb/Q96NC0) · Ensembl [ENSG00000146007](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146007)

## Data

Gene col 7053: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7053); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7053, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7053]; `tensor/DDL_lfc|DDL_z.npy` [7053]; `embed/gene_vectors.npy` [7053]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7053 or target_col == 7053). Every well: [[ZMAT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZMAT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

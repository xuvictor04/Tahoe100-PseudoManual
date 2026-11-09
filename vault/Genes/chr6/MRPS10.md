---
symbol: "MRPS10"
type: "gene"
col: 537
ensembl_id: "ENSG00000048544"
name: "mitochondrial ribosomal protein S10"
location: "6p21.1"
module: 28
arm: "+"
pooled_cpm: 32.38
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# MRPS10

*mitochondrial ribosomal protein S10* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.98× (z +15.2, q 0e+00, up in 45 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.29× (z +11.5, q 2e-28, up in 44 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Esmolol (hydrochloride) (drug)]] 0.5 µM in 1 line (SW 1271 0.0626×); [[Digitoxin (drug)]] 5 µM in 1 line (SNU-1 0.200×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANXA7]] (+0.69, fdr 7e-06), [[THAP5]] (+0.62, fdr 7e-06), [[PEX1]] (+0.60, fdr 1e-05); moves opposite to [[ADAT3]] (-0.56, fdr 3e-05), [[NFATC2IP-AS1]] (-0.55, fdr 1e-05), [[SEPTIN1]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 537.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.98×** | +15.2 | 0e+00 | 45/45 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.83×** | +13.9 | 2e-41 | 35/37 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.39×** | +12.1 | 3e-31 | 46/48 (COLO 205, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.29×** | +11.5 | 2e-28 | 44/47 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.27×** | +10.9 | 8e-26 | 43/48 (COLO 205, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.73×** | +10.8 | 4e-25 | 37/47 (COLO 205, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.07×** | +10.1 | 4e-22 | 42/48 (COLO 205, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.11×** | +9.6 | 5e-20 | 36/41 (SNU-423, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.98×** | +9.5 | 2e-19 | 44/48 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.90×** | +8.9 | 3e-17 | 42/47 (COLO 205, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +6.5 | 3e-09 | 33/48 (SW480, HS-578T, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +6.4 | 6e-09 | 37/47 (COLO 205, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~68% of this change | **1.39×** | +4.6 | 2e-04 | 23/46 (NCI-H460, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +4.5 | 3e-04 | 30/48 (COLO 205, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.36×** | +4.3 | 7e-04 | 23/48 (COLO 205, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.001 | 22/47 (COLO 205, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.68×** | +3.8 | 0.005 | 19/48 (HS-578T, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.010 | 20/48 (SNU-423, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.042 | 13/47 (SW1417, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[palbociclib (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.067 | 17/48 (SNU-1, A498, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 0.5 µM |  | **1.35×** | +2.9 | 0.088 | 12/48 (SW480, HEC-1-A, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 537.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Esmolol (hydrochloride) (drug)]] 0.5 µM in 1 line (SW 1271 0.0626×); [[Digitoxin (drug)]] 5 µM in 1 line (SNU-1 0.200×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Folic acid (drug)]] 5 µM |  | 0.840× | -3.4 | 0.40 | 19/48 (NCI-H661, CFPAC-1, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 0.658× | -3.0 | 0.59 | 16/47 (A-427, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 537. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 127 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +13.6) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.29× (z +13.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 29.5 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.59× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.99× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 25.5 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.29× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[CFPAC-1 (line)]] | alt | 24.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.27× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 32.8 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.50× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW480 (line)]] | alt | 31.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.72× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HS-578T (line)]] | alt | 29.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1792 (line)]] | alt | 20.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.79× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.74× (z +8.8) | — |
| [[A-172 (line)]] | wt | 20.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.99× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A498 (line)]] | wt | 35.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HEC-1-A (line)]] | alt | 25.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[LoVo (line)]] | wt | 33.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H460 (line)]] | wt | 19.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[Panc 03.27 (line)]] | alt | 47.4 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.15× (z +9.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[PANC-1 (line)]] | alt | 51.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW 900 (line)]] | alt | 18.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.21× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-427 (line)]] | wt | 35.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.91× (z +8.5) | — |
| [[A549 (line)]] | wt | 18.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[AsPC-1 (line)]] | alt | 20.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +10.5) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[J82 (line)]] | alt | 30.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LOX-IMVI (line)]] | wt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2347 (line)]] | alt | 42.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SNU-1 (line)]] | wt | 26.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 39.1 | 0 | 1 | — | [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.0626× (z -8.8) |
| [[AN3 CA (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 537), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANXA7]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[THAP5]] | +0.62 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[PEX1]] | +0.60 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[SNX17]] | +0.59 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[PTCD2]] | +0.59 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[GTF2H3]] | +0.59 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[CCDC113]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[MRPL47]] | +0.59 | +0.67 / +0.55 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 995 |
| [[CLCN3]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[MBTPS2]] | +0.57 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ASF1A]] | +0.57 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[NUDT12]] | +0.56 | +0.57 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAT3]] | -0.56 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[NFATC2IP-AS1]] | -0.55 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[SEPTIN1]] | -0.54 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[RBM38]] | -0.53 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[AGAP3]] | -0.52 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[SMPD4BP]] | -0.51 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[NDUFB2]] | -0.50 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[FKBP11]] | -0.50 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[DDN-AS1]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[WDR20]] | -0.50 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[HIC2]] | -0.50 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[NENF]] | -0.50 | -0.57 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.525). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.4, 2.0); signed map (0.2, -35.3). **Vector** length 83.9, 21.3% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.2 | +9.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +11.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +6.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.2 | +10.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.7 | +1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.7 | +1.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.2 | -0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +1.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.3 | -0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -0.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.8 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +1.9 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:42,206,807-42,217,861 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10567, uS10m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Reactome | 7 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial protein degradation; Mitochondrial translation elongation |
| Matched by | ensembl_id |

UniProt [P82664](https://www.uniprot.org/uniprotkb/P82664) carries no function annotation.

**Summary**, from NCBI Gene [55173](https://www.ncbi.nlm.nih.gov/gene/55173):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14502](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14502) · Entrez [55173](https://www.ncbi.nlm.nih.gov/gene/55173) · UniProt [P82664](https://www.uniprot.org/uniprotkb/P82664) · Ensembl [ENSG00000048544](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000048544)

## Data

Gene col 537: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 537); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 537, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 537]; `tensor/DDL_lfc|DDL_z.npy` [537]; `embed/gene_vectors.npy` [537]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 537 or target_col == 537). Every well: [[MRPS10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

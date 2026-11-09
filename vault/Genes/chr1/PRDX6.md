---
symbol: "PRDX6"
type: "gene"
col: 3926
ensembl_id: "ENSG00000117592"
name: "peroxiredoxin 6"
location: "1q25.1"
module: 29
arm: "+"
pooled_cpm: 82.78
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PRDX6

*peroxiredoxin 6* — 1q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.95× (z +14.2, q 5e-43, up in 45 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.461×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIAO2A]] (+0.56, fdr 4e-05), [[CYBRD1]] (+0.54, fdr 4e-05), [[NADK2]] (+0.54, fdr 3e-05); moves opposite to [[EXOC6]] (-0.54, fdr 6e-05), [[KCTD20]] (-0.52, fdr 4e-05), [[DOP1B]] (-0.49, fdr 5e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CADM4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3926.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +14.2 | 5e-43 | 45/49 (CFPAC-1, A-172, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.53×** | +13.5 | 2e-39 | 45/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.22×** | +11.5 | 2e-28 | 39/44 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +8.9 | 1e-16 | 41/48 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.82×** | +8.3 | 8e-15 | 36/45 (C32, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +6.8 | 1e-09 | 43/48 (PANC-1, A498, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.5 | 5e-09 | 36/50 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +6.5 | 5e-09 | 42/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.3 | 2e-08 | 33/48 (A-427, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.51×** | +6.2 | 4e-08 | 37/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.51×** | +5.9 | 2e-07 | 32/48 (HOP62, SNU-423, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +5.5 | 2e-06 | 38/48 (NCI-H2030, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.42×** | +5.1 | 2e-05 | 34/47 (NCI-H1792, SHP-77, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.40×** | +5.1 | 2e-05 | 39/49 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +4.8 | 8e-05 | 34/48 (BT-474, C32, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.35×** | +4.5 | 2e-04 | 36/48 (C-33 A, LOX-IMVI, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.015 | 29/47 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.031 | 20/48 (HOP62, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.045 | 21/48 (A-172, BT-474, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.22×** | +2.9 | 0.084 | 21/48 (NCI-H1573, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.461×; ⚠ cell-cycle shift, would explain all of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3926. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 124 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +10.3) | — |
| [[PANC-1 (line)]] | alt | 55.5 | 5 (2 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.73× (z +13.7) | — |
| [[C32 (line)]] | wt | 55.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 64.5 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +13.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +11.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 98.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.5) | — |
| [[A549 (line)]] | wt | 69.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +13.1) | — |
| [[HT-29 (line)]] | alt | 53.3 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +12.5) | — |
| [[J82 (line)]] | alt | 86.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.1) | — |
| [[KATO III (line)]] | alt | 46.3 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +11.8) | — |
| [[LOX-IMVI (line)]] | wt | 45.5 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +12.5) | — |
| [[NCI-H1792 (line)]] | alt | 68.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +11.5) | — |
| [[SNU-423 (line)]] | alt | 67.5 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +10.9) | — |
| [[SW480 (line)]] | alt | 72.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.14× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +10.8) | — |
| [[A-172 (line)]] | wt | 112 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +13.6) | — |
| [[A498 (line)]] | wt | 198 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[CFPAC-1 (line)]] | alt | 84.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +14.5) | — |
| [[HCT15 (line)]] | alt | 81.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.33× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 57.3 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.14× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 80.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +12.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 70.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 49.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[Panc 03.27 (line)]] | alt | 84.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 79.5 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.51× (z +11.6) | — |
| [[SNU-1 (line)]] | wt | 82.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.92× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW1417 (line)]] | alt | 77.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +10.8) | — |
| [[A-427 (line)]] | wt | 79.8 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.10× (z +10.5) | — |
| [[BT-474 (line)]] | alt | 78.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C-33 A (line)]] | alt | 55.3 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.31× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 36.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.25× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LoVo (line)]] | wt | 67.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +13.2) | — |
| [[NCI-H2030 (line)]] | alt | 79.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 111 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +10.8) | — |
| [[RKO (line)]] | wt | 108 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 121 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 87.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 96.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3926), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAO2A]] | +0.56 | +0.40 / +0.50 | both halves | 4e-05 |  |
| [[CYBRD1]] | +0.54 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[NADK2]] | +0.54 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[GLUD1]] | +0.54 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[SELENOF]] | +0.54 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[MARVELD1]] | +0.53 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[VPS37A]] | +0.52 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[NUDT16]] | +0.51 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[UROD]] | +0.51 | +0.49 / +0.36 | both halves | 9e-05 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[SMPDL3A]] | +0.51 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[CDIPT]] | +0.50 | +0.30 / +0.47 | both halves | 2e-04 |  |
| [[UGP2]] | +0.50 | +0.47 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC6]] | -0.54 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[KCTD20]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[DOP1B]] | -0.49 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[DUSP8]] | -0.46 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[PPCDC]] | -0.45 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[ZNF544]] | -0.45 | -0.29 / -0.50 | both halves | 3e-04 |  |
| [[CREB1]] | -0.45 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[ABCF1]] | -0.45 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[CBX6]] | -0.45 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[RAP2B]] | -0.45 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[TNFRSF12A]] | -0.44 | -0.37 / -0.42 | both halves | 7e-05 |  |
| [[PPFIA1]] | -0.44 | -0.42 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CADM4]] | B | CADM4 activity raises PRDX6's level | lines that do not express CADM4 (5) vs lines expressing it (45) | 1.26× lower at baseline in the lines without CADM4 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[SYNJ2]] | C | SYNJ2 activity lowers PRDX6's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 1.45× higher at baseline in the lines without SYNJ2 | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.411). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-17.6, 19.7); signed map (-31.2, -22.5). **Vector** length 94.4, 30.1% of its response variance represented; |z| ≥ 3 in 1,077 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +10.9 | +8.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +7.6 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +14.2 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +5.2 | +5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.2 | +5.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.3 | +1.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.9 | +1.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +6.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | +0.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | peroxiredoxin 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.1 — chr1:173,477,330-173,488,815 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AOP2, KIAA0106, 1-Cys, NSGPx, PRX, aiPLA2, MGC46173, p29 |
| Gene groups (HGNC) | Peroxiredoxins; Acyltransferases |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, FATTY_ACID_METABOLISM |
| Reactome | 6 pathways, smallest: Detoxification of Reactive Oxygen Species; Cellular response to chemical stress; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P30041](https://www.uniprot.org/uniprotkb/P30041) (Peroxiredoxin-6):

> Thiol-specific peroxidase that catalyzes the reduction of hydrogen peroxide and organic hydroperoxides to water and alcohols, respectively. Can reduce H(2)O(2) and short chain organic, fatty acid, and phospholipid hydroperoxides. Also has phospholipase activity, can therefore either reduce the oxidized sn-2 fatty acyl group of phospholipids (peroxidase activity) or hydrolyze the sn-2 ester bond of phospholipids (phospholipase activity). These activities are dependent on binding to phospholipids …

**Summary**, from NCBI Gene [9588](https://www.ncbi.nlm.nih.gov/gene/9588):

> The protein encoded by this gene is a member of the thiol-specific antioxidant protein family. This protein is a bifunctional enzyme with two distinct active sites. It is involved in redox regulation of the cell; it can reduce H(2)O(2) and short chain organic, fatty acid, and phospholipid hydroperoxides. It may play a role in the regulation of phospholipid turnover as well as in protection against oxidative injury. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16753](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16753) · Entrez [9588](https://www.ncbi.nlm.nih.gov/gene/9588) · UniProt [P30041](https://www.uniprot.org/uniprotkb/P30041) · Ensembl [ENSG00000117592](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117592)

## Data

Gene col 3926: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3926); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3926, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3926]; `tensor/DDL_lfc|DDL_z.npy` [3926]; `embed/gene_vectors.npy` [3926]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3926 or target_col == 3926). Every well: [[PRDX6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRDX6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

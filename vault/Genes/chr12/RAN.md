---
symbol: "RAN"
type: "gene"
col: 5303
ensembl_id: "ENSG00000132341"
name: "RAN, member RAS oncogene family"
location: "12q24.33"
module: 4
arm: "+"
pooled_cpm: 134.7
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# RAN

*RAN, member RAS oncogene family* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.52× (z +11.3, q 5e-27, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.66× (z +4.6, q 4e-04, up in 38 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.138×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (LS 180 0.341×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XXYLT1]] (+0.62, fdr 1e-05), [[CCT5]] (+0.57, fdr 5e-05), [[SPOPL-DT]] (+0.57, fdr 2e-05); moves opposite to [[SIRT2]] (-0.57, fdr 2e-04), [[RING1]] (-0.55, fdr 3e-05), [[PLAG1]] (-0.52, fdr 2e-04).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5303.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.52×** | +11.3 | 5e-27 | 48/49 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.30×** | +10.3 | 1e-22 | 44/44 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +6.1 | 2e-07 | 41/47 (HepG2/C3A, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.82×** | +5.4 | 9e-06 | 46/48 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.22×** | +5.2 | 3e-05 | 39/45 (SNU-423, Panc 03.27, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +4.6 | 4e-04 | 38/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.66×** | +4.4 | 8e-04 | 37/47 (C32, COLO 205, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.004 | 32/49 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.53×** | +3.8 | 0.009 | 34/48 (NCI-H1792, COLO 205, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **2.11×** | +3.6 | 0.021 | 45/48 (NCI-H23, SW 900, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.49×** | +3.4 | 0.031 | 31/50 (SNU-423, A-172, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.044 | 35/47 (HOP62, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.065 | 30/48 (HS-578T, SW 900, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.097 | 31/47 (HOP62, NCI-H23, …) | all doses, flat | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.097 | 27/48 (HOP62, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5303.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.138×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (LS 180 0.341×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.696× | -3.3 | 0.60 | 39/48 (SK-MEL-2, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5303. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 104 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A498 (line)]] | wt | 129 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A549 (line)]] | wt | 155 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[CFPAC-1 (line)]] | alt | 123 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[H4 (line)]] | wt | 115 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HOP62 (line)]] | alt | 111 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[Hs 766T (line)]] | wt | 70.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HS-578T (line)]] | alt | 92.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HT-29 (line)]] | alt | 103 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[J82 (line)]] | alt | 171 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[KATO III (line)]] | alt | 95.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 137 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.68× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H1792 (line)]] | alt | 77.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[PANC-1 (line)]] | alt | 138 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[RPMI-7951 (line)]] | alt | 82.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 163 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SNU-423 (line)]] | alt | 97.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.97× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SW480 (line)]] | alt | 143 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-427 (line)]] | wt | 182 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -19.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 80.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[COLO 205 (line)]] | alt | 61.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.20× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HCT15 (line)]] | alt | 150 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HepG2_C3A (line)]] | wt | 160 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 93.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.07× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[LOX-IMVI (line)]] | wt | 179 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[LS 180 (line)]] | wt | 133 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.341× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 108 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.34× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H23 (line)]] | alt | 185 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H2347 (line)]] | alt | 173 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[Panc 03.27 (line)]] | alt | 75.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[RKO (line)]] | wt | 146 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SW 900 (line)]] | alt | 87.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SW1417 (line)]] | alt | 136 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[AN3 CA (line)]] | alt | 136 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 166 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 168 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 170 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 189 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5303), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XXYLT1]] | +0.62 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[CCT5]] | +0.57 | +0.70 / +0.40 | both halves | 5e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 825 |
| [[SPOPL-DT]] | +0.57 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[HNRNPAB]] | +0.56 | +0.61 / +0.50 | both halves | 1e-05 | STRING 482 |
| [[BEND3]] | +0.56 | +0.65 / +0.35 | both halves | 1e-04 |  |
| [[CCT7]] | +0.56 | +0.70 / +0.31 | both halves | 2e-04 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 726 |
| [[VANGL1]] | +0.55 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | +0.55 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[PREP]] | +0.54 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[C1QBP]] | +0.53 | +0.69 / +0.39 | both halves | 5e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 475 |
| [[ZNF124]] | +0.53 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[PRMT3]] | +0.52 | +0.55 / +0.39 | both halves | 5e-05 | STRING 418 |

## Genes that move opposite

*42 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT2]] | -0.57 | -0.71 / -0.30 | both halves | 2e-04 | pathway: Mitotic Anaphase; STRING 926 |
| [[RING1]] | -0.55 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[PLAG1]] | -0.52 | -0.65 / -0.32 | both halves | 2e-04 |  |
| [[RAB13]] | -0.52 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[AKAP9]] | -0.52 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[PNKD]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[CCDC144BP]] | -0.51 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[ABHD8]] | -0.51 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[MOSPD2]] | -0.50 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[ATG4D]] | -0.50 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[GABARAP]] ⚠ | -0.49 | -0.57 / -0.23 | both halves | 5e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[GLMP]] | -0.49 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[YPEL3]] | -0.49 | -0.60 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.400). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-3.7, -35.9); signed map (1.3, -52.1). **Vector** length 63.8, 26.3% of its response variance represented; |z| ≥ 3 in 744 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.8 | +2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.3 | +3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +0.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.2 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | -0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.6 | +3.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -2.7 | +11.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.6 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -2.3 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -2.3 | +5.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.4 | +0.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.3 | -1.4 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | -1.2 | +0.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.2 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | RAN, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:130,872,037-130,877,678 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARA24, TC4, Gsp1 |
| Gene groups (HGNC) | RAN family GTPases |
| Hallmark sets | E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 27 pathways, smallest: MicroRNA (miRNA) biogenesis; Postmitotic nuclear pore complex (NPC) reformation; Transcriptional regulation by small RNAs |
| Matched by | ensembl_id |

**Function**, from UniProt [P62826](https://www.uniprot.org/uniprotkb/P62826) (GTP-binding nuclear protein Ran):

> GTPase involved in nucleocytoplasmic transport, participating both to the import and the export from the nucleus of proteins and RNAs. Switches between a cytoplasmic GDP- and a nuclear GTP-bound state by nucleotide exchange and GTP hydrolysis. Nuclear import receptors such as importin beta bind their substrates only in the absence of GTP-bound RAN and release them upon direct interaction with GTP-bound RAN, while export receptors behave in the opposite way. Thereby, RAN controls cargo loading …

**Summary**, from NCBI Gene [5901](https://www.ncbi.nlm.nih.gov/gene/5901):

> RAN (ras-related nuclear protein) is a small GTP binding protein belonging to the RAS superfamily that is essential for the translocation of RNA and proteins through the nuclear pore complex. The RAN protein is also involved in control of DNA synthesis and cell cycle progression. Nuclear localization of RAN requires the presence of regulator of chromosome condensation 1 (RCC1). Mutations in RAN disrupt DNA synthesis. Because of its many functions, it is likely that RAN interacts with several …

**Accessions** — [HGNC:9846](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9846) · Entrez [5901](https://www.ncbi.nlm.nih.gov/gene/5901) · UniProt [P62826](https://www.uniprot.org/uniprotkb/P62826) · Ensembl [ENSG00000132341](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132341)

## Data

Gene col 5303: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5303); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5303, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5303]; `tensor/DDL_lfc|DDL_z.npy` [5303]; `embed/gene_vectors.npy` [5303]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5303 or target_col == 5303). Every well: [[RAN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

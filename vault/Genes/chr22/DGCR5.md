---
symbol: "DGCR5"
type: "gene"
col: 15759
ensembl_id: "ENSG00000273032"
name: "DiGeorge syndrome critical region gene 5"
location: "22q11.21"
module: 102
arm: "+"
pooled_cpm: 7.95
n_lines_expressing: 42
n_dd_up: 6
n_dd_down: 26
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 11
direction_downstream: 2
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# DGCR5

*DiGeorge syndrome critical region gene 5* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.20× (z +11.9, q 1e-29, up in 7 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.24× (z +4.7, q 4e-04, up in 8 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.397× (z -20.4, q 0e+00, down in 31 of 35 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.318× (z -17.2, q 0e+00, down in 30 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RASGEF1C]] (+0.62, fdr 1e-05), [[LRRN2]] (+0.62, fdr 9e-06), [[ADCY1]] (+0.62, fdr 1e-05); moves opposite to [[DNAL4]] (-0.50, fdr 6e-05), [[TRMT1L]] (-0.47, fdr 3e-05), [[ASB8]] (-0.47, fdr 3e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[RFPL1S]] → it (grade B ⚠); 2 go from it, the strongest it → [[SDK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15759.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +11.9 | 1e-29 | 7/15 (HEC-1-A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +8.9 | 1e-16 | 12/25 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +6.4 | 3e-08 | 4/18 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.7 | 4e-04 | 8/39 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +4.5 | 9e-04 | 8/38 (A-172, NCI-H2030, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.18× | +3.7 | 0.023 | 3/39 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.047 | 5/39 (NCI-H23, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.056 | 7/39 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 1.22× | +3.1 | 0.12 | 3/37 (AN3 CA, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15759.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.397×** | -20.4 | 0e+00 | 31/35 (SW48, A549, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.318×** | -17.2 | 0e+00 | 30/35 (SW48, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.433×** | -13.1 | 5e-37 | 22/31 (SW48, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.468×** | -11.9 | 2e-30 | 20/38 (A549, SHP-77, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.473×** | -11.7 | 1e-29 | 29/39 (SW48, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.543×** | -9.6 | 1e-19 | 22/38 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.585×** | -8.4 | 3e-15 | 18/39 (SW48, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.585×** | -8.4 | 3e-15 | 23/34 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.589×** | -8.3 | 7e-15 | 20/38 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.411×** | -7.3 | 2e-11 | 19/37 (SW48, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.639×** | -7.0 | 1e-10 | 22/38 (BT-474, A-172, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.657×** | -6.6 | 2e-09 | 19/39 (PANC-1, SK-MEL-2, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.670×** | -6.3 | 2e-08 | 20/39 (SW48, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.715×** | -5.2 | 8e-06 | 11/39 (A-172, H4, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.793×** | -5.2 | 1e-05 | 15/39 (BT-474, A498, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.552×** | -4.9 | 4e-05 | 8/30 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.786×** | -3.8 | 0.006 | 10/39 (HOP62, SW480, …) | top dose only |  |
| [[Altretamine (drug)]] 5 µM |  | **0.780×** | -3.8 | 0.006 | 4/38 (RPMI-7951, AN3 CA, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.641×** | -3.6 | 0.008 | 6/29 (NCI-H23, SHP-77, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15759. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 72.6 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0487× (z -30.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0435× (z -22.3) |
| [[SHP-77 (line)]] | alt | 41.0 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -16.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.146× (z -12.9) |
| [[SW480 (line)]] | alt | 14.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -15.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.215× (z -10.6) |
| [[A549 (line)]] | wt | 11.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0631× (z -20.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0662× (z -14.1) |
| [[BT-474 (line)]] | alt | 9.74 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0912× (z -13.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0886× (z -9.8) |
| [[C-33 A (line)]] | alt | 31.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.140× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 18.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -19.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.105× (z -14.7) |
| [[LoVo (line)]] | wt | 9.52 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0612× (z -15.6) |
| [[A-172 (line)]] | wt | 6.83 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0923× (z -11.7) |
| [[A-427 (line)]] | wt | 12.5 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0885× (z -12.6) |
| [[A498 (line)]] | wt | 9.77 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -16.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.213× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -11.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -9.8) |
| [[PANC-1 (line)]] | alt | 5.48 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -15.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 10.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -16.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.126× (z -11.0) |
| [[SW1417 (line)]] | alt | 15.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -14.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.194× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 3.85 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0863× (z -8.5) |
| [[HOP62 (line)]] | alt | 3.48 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0978× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -14.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[AN3 CA (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15759), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASGEF1C]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[LRRN2]] | +0.62 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[ADCY1]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[LAMC3]] | +0.59 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[MSI1]] | +0.58 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[EMID1]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[GRID1]] | +0.57 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[JPH3]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[DPYSL5]] | +0.55 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[TMEM150C]] | +0.55 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[HAGLR]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 | same gene group |
| [[EBF4]] | +0.54 | +0.50 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAL4]] | -0.50 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[TRMT1L]] | -0.47 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[ASB8]] | -0.47 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[DCTN3]] | -0.46 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[TMEM205]] | -0.46 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[MORN2]] | -0.45 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[TRAFD1]] | -0.44 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[DPYD]] | -0.44 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[ALPK1]] | -0.44 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[DHRS2]] | -0.43 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[CA9]] | -0.43 | -0.43 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFPL1S]] | B | RFPL1S activity raises DGCR5's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 2.80× lower at baseline in the lines without RFPL1S | 0.014 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent |
| [[EMID1]] | B | EMID1 activity raises DGCR5's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 2.57× lower at baseline in the lines without EMID1 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[ABCA17P]] | B | ABCA17P activity raises DGCR5's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 2.48× lower at baseline in the lines without ABCA17P | 0.031 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[KIF26A]] | B | KIF26A activity raises DGCR5's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.27× lower at baseline in the lines without KIF26A | 0.034 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[TMEM150C]] | B | TMEM150C activity raises DGCR5's level | lines that do not express TMEM150C (13) vs lines expressing it (37) | 2.20× lower at baseline in the lines without TMEM150C | 0.048 | ⚠ within organs, on part of the lines; also absent: AP3B2, MED12L, RAB6B; maybe low, not absent |
| [[SLC4A3]] | B | SLC4A3 activity raises DGCR5's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 2.41× lower at baseline in the lines without SLC4A3 | 0.052 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[RET]] | B | RET activity raises DGCR5's level | lines that do not express RET (28) vs lines expressing it (22) | 1.92× lower at baseline in the lines without RET | 0.055 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[ZNF860]] | B | ZNF860 activity raises DGCR5's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 1.96× lower at baseline in the lines without ZNF860 | 0.073 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[LAMC3]] | B | LAMC3 activity raises DGCR5's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 2.04× lower at baseline in the lines without LAMC3 | 0.076 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[CHD5]] | B | CHD5 activity strengthens DGCR5's drug response | lines that do not express CHD5 (24) vs lines expressing it (15) | the lines without CHD5 respond 0.55× as strongly (z diff +2.14); strongest at Homoharringtonine 5 µM: 0.31x vs 0.21x (z diff +3.7) | 0.081 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[DPYSL5]] | B | DPYSL5 activity raises DGCR5's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.05× lower at baseline in the lines without DPYSL5 | 0.091 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDK2]] | B | DGCR5 activity raises SDK2's level | lines that do not express DGCR5 (8) vs lines expressing it (42) | 3.02× lower at baseline in the lines without DGCR5 | 0.092 | ⚠ within organs, on part of the lines; also absent: CACNA1B; maybe low, not absent |
| [[SLC4A3]] | B | DGCR5 activity raises SLC4A3's level | lines that do not express DGCR5 (8) vs lines expressing it (42) | 2.13× lower at baseline in the lines without DGCR5 | 0.0999 | ⚠ within organs, on part of the lines; also absent: CACNA1B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.2, 37.1); signed map (26.2, 25.1). **Vector** length 64.2, 10.2% of its response variance represented; |z| ≥ 3 in 1,036 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +8.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.5 | +1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.4 | +0.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.3 | +2.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -17.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.9 | -9.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -11.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -2.1 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -8.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -3.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.1 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | DiGeorge syndrome critical region gene 5 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 22q11.21 — chr22:18,970,439-19,031,242 (+) |
| Ensembl biotype | lncRNA |
| Also known as | NCRNA00037, LINC00037, X91348, DGS-A, POM121L5P, DGS-B, RIP; previously DGCR9, DGCR10 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [26220](https://www.ncbi.nlm.nih.gov/gene/26220):

> Biomarker of Huntington's disease. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16757](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16757) · Entrez [26220](https://www.ncbi.nlm.nih.gov/gene/26220) · Ensembl [ENSG00000273032](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000273032)

## Data

Gene col 15759: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15759); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15759, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15759]; `tensor/DDL_lfc|DDL_z.npy` [15759]; `embed/gene_vectors.npy` [15759]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15759 or target_col == 15759). Every well: [[DGCR5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DGCR5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

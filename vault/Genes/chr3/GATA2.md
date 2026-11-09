---
symbol: "GATA2"
type: "gene"
col: 11022
ensembl_id: "ENSG00000179348"
name: "GATA binding protein 2"
location: "3q21.3"
module: 4
arm: "-"
pooled_cpm: 12.36
n_lines_expressing: 42
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# GATA2

*GATA binding protein 2* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.92× (z +25.3, q 0e+00, up in 36 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 0.132×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Allantoin (drug)]] 0.05 µM in 1 line (SNU-1 0.0752×; ⚠ transcription drop); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (C-33 A 0.0723×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.211×).
> Its strongest partners by |cos| (73 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 27 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPRC5C]] (+0.58, fdr 1e-04), [[TSC22D4]] (+0.57, fdr 1e-04), [[RBM38]] (+0.54, fdr 2e-04); moves opposite to [[GTF2H3]] (-0.55, fdr 3e-04), [[API5]] (-0.54, fdr 5e-04), [[GFM1]] (-0.53, fdr 7e-04).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PAX6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PDE4A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11022.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.92×** | +25.3 | 0e+00 | 36/38 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.78×** | +11.5 | 4e-28 | 32/40 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.70×** | +11.2 | 1e-26 | 30/40 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.30×** | +9.4 | 1e-18 | 28/39 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **2.27×** | +9.2 | 4e-18 | 26/40 (J82, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +8.8 | 1e-16 | 24/33 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.22×** | +8.6 | 4e-16 | 27/38 (NCI-H460, LS 180, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.20×** | +8.5 | 9e-16 | 24/36 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.69×** | +8.4 | 4e-15 | 23/36 (J82, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **2.06×** | +7.8 | 3e-13 | 20/34 (J82, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.96×** | +7.5 | 2e-12 | 18/30 (J82, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +6.6 | 2e-09 | 24/40 (J82, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +6.3 | 1e-08 | 22/39 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +5.1 | 2e-05 | 15/40 (PANC-1, LoVo, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.0 | 2e-05 | 13/40 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.3 | 5e-04 | 11/40 (SK-MEL-2, Panc 03.27, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +4.3 | 5e-04 | 12/39 (J82, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 0.001 | 10/40 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.022 | 10/40 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.029 | 8/40 (C32, PANC-1, …) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.048 | 6/39 (HCT15, COLO 205, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +2.9 | 0.067 | 2/40 (NCI-H2347, NCI-H1573) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.52×** | +2.8 | 0.089 | 4/37 (HOP62, NCI-H2347, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11022.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 0.132×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Allantoin (drug)]] 0.05 µM in 1 line (SNU-1 0.0752×; ⚠ transcription drop); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (C-33 A 0.0723×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.211×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 0.05 µM |  | 0.738× | -3.2 | 0.71 | 4/40 (NCI-H2347, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11022. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 160 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +13.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 17.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 15.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.65× (z +13.4) | — |
| [[NCI-H460 (line)]] | wt | 6.25 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.63× (z +16.2) | — |
| [[SW480 (line)]] | alt | 17.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.132× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 9.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.24× (z +9.5) | — |
| [[A-427 (line)]] | wt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -9.3) |
| [[AN3 CA (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.106× (z -8.7) ⚠ transcription drop |
| [[BT-474 (line)]] | alt | 28.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0723× (z -10.7) |
| [[C32 (line)]] | wt | 5.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +12.8) | — |
| [[HCT15 (line)]] | alt | 5.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.78× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 6.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.55× (z +12.1) | — |
| [[LoVo (line)]] | wt | 6.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.65× (z +12.9) | — |
| [[LOX-IMVI (line)]] | wt | 4.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.34× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 4.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.4× (z +13.0) | — |
| [[NCI-H1573 (line)]] | alt | 3.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.53× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 7.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.42× (z +12.8) | — |
| [[NCI-H23 (line)]] | alt | 9.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 14.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.20× (z +15.1) | — |
| [[SNU-1 (line)]] | wt | 15.6 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0752× (z -10.8) ⚠ transcription drop |
| [[SW 900 (line)]] | alt | 9.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 23.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +10.1) | — |
| [[A498 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.969 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.928 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.817 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11022), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRC5C]] | +0.58 | +0.32 / +0.57 | both halves | 1e-04 |  |
| [[TSC22D4]] | +0.57 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[RBM38]] | +0.54 | +0.32 / +0.68 | both halves | 2e-04 |  |
| [[CDC42EP4]] | +0.54 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[SPINT1]] | +0.53 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[NOL4L]] | +0.52 | +0.37 / +0.56 | both halves | 9e-05 |  |
| [[AGAP3]] | +0.52 | +0.33 / +0.54 | both halves | 1e-04 |  |
| [[MSX1]] | +0.52 | +0.32 / +0.62 | both halves | 2e-04 | STRING 415 |
| [[TFEB]] | +0.51 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[ZBTB7A]] | +0.51 | +0.30 / +0.58 | both halves | 2e-04 |  |
| [[PAX6]] | +0.50 | +0.31 / +0.54 | both halves | 2e-04 | STRING 440 |
| [[SIX1]] | +0.50 | +0.23 / +0.58 | both halves | 5e-04 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 17 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H3]] | -0.55 | -0.27 / -0.57 | both halves | 3e-04 |  |
| [[API5]] | -0.54 | -0.23 / -0.62 | both halves | 5e-04 |  |
| [[GFM1]] | -0.53 | -0.21 / -0.56 | both halves | 7e-04 |  |
| [[FAM114A2]] | -0.53 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[FKTN]] | -0.53 | -0.23 / -0.54 | both halves | 5e-04 |  |
| [[DNAL1]] | -0.51 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[SCRN3]] | -0.50 | -0.15 / -0.46 | ⚠ not reproduced | 0.001 |  |
| [[SLC30A9]] | -0.50 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[CWC27]] | -0.50 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[MTG1]] | -0.50 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[ATAD1]] | -0.50 | -0.29 / -0.54 | both halves | 3e-04 |  |
| [[SNF8]] | -0.50 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[MRPL42]] | -0.49 | -0.25 / -0.53 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAX6]] | B | PAX6 activity raises GATA2's level | lines that do not express PAX6 (30) vs lines expressing it (20) | 1.99× lower at baseline in the lines without PAX6 | 0.028 | ⚠ within organs, on part of the lines; also absent: LINC02643, WT1-AS, CHRDL1 |
| [[TOP2A]] | B | TOP2A activity lowers GATA2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE4A]] | B | GATA2 activity raises PDE4A's level | lines that do not express GATA2 (8) vs lines expressing it (42) | 2.25× lower at baseline in the lines without GATA2 | 0.040 | ⚠ within organs, on part of the lines; also absent: GATA2-AS1, EFR3B |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.367). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-5.3, -40.4); signed map (-16.8, 20.3). **Vector** length 60.6, 10.4% of its response variance represented; |z| ≥ 3 in 821 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +25.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.0 | +8.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | +2.7 | +7.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.5 | +9.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +2.3 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +6.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.0 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.8 | +1.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.4 | +1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | +1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | GATA binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:128,479,427-128,493,201 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NFE1B |
| Gene groups (HGNC) | GATA zinc finger domain containing |
| Reactome | 5 pathways, smallest: Transcriptional regulation of granulopoiesis; RUNX1 regulates transcription of genes involved in differentiation of HSCs; Factors involved in megakaryocyte development and platelet production |
| Matched by | ensembl_id |

**Function**, from UniProt [P23769](https://www.uniprot.org/uniprotkb/P23769) (Endothelial transcription factor GATA-2):

> Transcriptional activator which regulates endothelin-1 gene expression in endothelial cells. Binds to the consensus sequence 5'-AGATAG-3'.

**Summary**, from NCBI Gene [2624](https://www.ncbi.nlm.nih.gov/gene/2624):

> This gene encodes a member of the GATA family of zinc-finger transcription factors that are named for the consensus nucleotide sequence they bind in the promoter regions of target genes. The encoded protein plays an essential role in regulating transcription of genes involved in the development and proliferation of hematopoietic and endocrine cell lineages. Alternative splicing results in multiple transcript variants.[provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:4171](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4171) · Entrez [2624](https://www.ncbi.nlm.nih.gov/gene/2624) · UniProt [P23769](https://www.uniprot.org/uniprotkb/P23769) · Ensembl [ENSG00000179348](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179348)

## Data

Gene col 11022: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11022); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11022, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11022]; `tensor/DDL_lfc|DDL_z.npy` [11022]; `embed/gene_vectors.npy` [11022]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11022 or target_col == 11022). Every well: [[GATA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GATA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "MKX"
type: "gene"
col: 7424
ensembl_id: "ENSG00000150051"
name: "mohawk homeobox"
location: "10p12.1"
module: 27
arm: "+"
pooled_cpm: 7.14
n_lines_expressing: 18
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# MKX

*mohawk homeobox* — 10p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.34× (z +15.0, q 0e+00, up in 10 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.628× (z -4.1, q 0.021, down in 8 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-172 0.265×, LS 180 0.224×, SW1417 0.154×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (SW480 0.0255×, A-172 0.108×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (A-172 0.0864×, SW480 0.0689×; ⚠ cell-cycle shift, explains ~44% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 0.303×); [[XRK3F2 (drug)]] 0.5 µM in 1 line (LoVo 0.0698×); [[Pioglitazone (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0672×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01980]] (+0.65, fdr 1e-05), [[SERPINF1]] (+0.60, fdr 1e-04), [[B3GAT1-DT]] (+0.58, fdr 3e-05); moves opposite to [[TAF1B]] (-0.47, fdr 8e-05), [[NIBAN2]] (-0.47, fdr 2e-04), [[FGD6]] (-0.45, fdr 3e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CCDC170]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7424.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.34×** | +15.0 | 0e+00 | 10/14 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.56×** | +11.2 | 1e-26 | 4/10 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.38×** | +10.3 | 9e-23 | 2/5 (NCI-H2347, A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.66×** | +8.0 | 2e-13 | 5/8 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +5.5 | 3e-06 | 4/13 (LS 180, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +4.5 | 5e-04 | 2/12 (NCI-H460, HCT15) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +4.5 | 7e-04 | 6/16 (A-427, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +4.4 | 9e-04 | 4/13 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.61×** | +4.2 | 0.002 | 12/16 (LS 180, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.65×** | +4.1 | 0.003 | 7/15 (SW480, C-33 A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.003 | 8/15 (SW480, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.51×** | +3.6 | 0.013 | 6/15 (LoVo, J82, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.35×** | +3.5 | 0.017 | 6/16 (SW480, HCT15, …) | all doses, flat |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.026 | 1/15 (NCI-H2347) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.030 | 3/15 (HCT15, SW 900, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +3.3 | 0.035 | 5/15 (SW480, A-172, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.036 | 8/15 (A-172, NCI-H1792, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.038 | 5/15 (C-33 A, LS 180, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.063 | 3/16 (SW480, A-172, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7424.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-172 0.265×, LS 180 0.224×, SW1417 0.154×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (SW480 0.0255×, A-172 0.108×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (A-172 0.0864×, SW480 0.0689×; ⚠ cell-cycle shift, explains ~44% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 0.303×); [[XRK3F2 (drug)]] 0.5 µM in 1 line (LoVo 0.0698×); [[Pioglitazone (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0672×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.628×** | -4.1 | 0.021 | 8/16 (A-172, LoVo, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.640×** | -4.0 | 0.021 | 11/15 (A-172, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | 0.667× | -3.5 | 0.10 | 9/14 (NCI-H1792, A-172, …) | two highest doses | cell-cycle shift (explains ~6% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7424. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 100 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0864× (z -16.2) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SW480 (line)]] | alt | 37.0 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0255× (z -22.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.303× (z -10.2) |
| [[LoVo (line)]] | wt | 8.10 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +9.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[XRK3F2 (drug)]] 0.5 µM 0.0698× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 1.90 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +9.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.0917× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 18.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 4.73 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0672× (z -8.5) |
| [[SW1417 (line)]] | alt | 5.96 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.936 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.714 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.807 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.843 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.735 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.934 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.909 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.716 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.795 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.812 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.939 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.899 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7424), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01980]] | +0.65 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[SERPINF1]] | +0.60 | +0.46 / +0.34 | both halves | 1e-04 |  |
| [[B3GAT1-DT]] | +0.58 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[NBR2]] | +0.55 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[HNF1A]] | +0.55 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[LINC00491]] | +0.54 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[SLC6A9]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[PHYHIPL]] | +0.54 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[HS3ST5]] | +0.53 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[JAKMIP2-AS1]] | +0.53 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[PCK2]] | +0.53 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[HOTAIR]] | +0.52 | +0.27 / +0.23 | both halves | 5e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF1B]] | -0.47 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[NIBAN2]] | -0.47 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[FGD6]] | -0.45 | -0.37 / -0.29 | both halves | 3e-04 |  |
| [[AKAP13]] | -0.45 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[DUSP5]] | -0.43 | -0.22 / -0.41 | both halves | 6e-04 |  |
| [[MAP3K14]] | -0.43 | -0.25 / -0.28 | both halves | 4e-04 |  |
| [[RASA3]] | -0.43 | -0.34 / -0.27 | both halves | 3e-04 |  |
| [[POLM]] | -0.42 | -0.28 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[RIN1]] | -0.42 | -0.34 / -0.27 | both halves | 3e-04 |  |
| [[HRH1]] | -0.42 | -0.32 / -0.30 | both halves | 2e-04 |  |
| [[PC]] | -0.42 | -0.26 / -0.25 | both halves | 4e-04 |  |
| [[SERPINB1]] | -0.42 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[KCNN4]] | -0.42 | -0.28 / -0.30 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers MKX's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[PSG1]] | C | PSG1 activity raises MKX's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 3.02× lower at baseline in the lines without PSG1 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[APCDD1]] | C | APCDD1 activity raises MKX's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 1.99× lower at baseline in the lines without APCDD1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC170]] | B | MKX activity raises CCDC170's level | lines that do not express MKX (32) vs lines expressing it (18) | 1.54× lower at baseline in the lines without MKX | 0.072 | ⚠ within organs, on part of the lines; also absent: FGF20, ENSG00000251652, SPINK13 |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.539). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.1, 42.7); signed map (62.2, 17.9). **Vector** length 39.6, 9.19% of its response variance represented; |z| ≥ 3 in 410 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +15.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +8.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +4.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.4 | +2.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.7 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -1.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.1 | -1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -0.9 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -0.9 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -1.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -2.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | mohawk homeobox |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.1 — chr10:27,672,874-27,746,060 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC39616; previously C10orf48, IRXL1 |
| Gene groups (HGNC) | TALE class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYA7](https://www.uniprot.org/uniprotkb/Q8IYA7) (Homeobox protein Mohawk):

> May act as a morphogenetic regulator of cell adhesion.

**Summary**, from NCBI Gene [283078](https://www.ncbi.nlm.nih.gov/gene/283078):

> The protein encoded by this gene is an IRX family-related homeobox protein that may play a role in cell adhesion. Studies in mice suggest that this protein may be a regulator of tendon development. Two transcript variants encoding the same protein have been found for this gene.[provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:23729](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23729) · Entrez [283078](https://www.ncbi.nlm.nih.gov/gene/283078) · UniProt [Q8IYA7](https://www.uniprot.org/uniprotkb/Q8IYA7) · Ensembl [ENSG00000150051](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150051)

## Data

Gene col 7424: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7424); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7424, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7424]; `tensor/DDL_lfc|DDL_z.npy` [7424]; `embed/gene_vectors.npy` [7424]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7424 or target_col == 7424). Every well: [[MKX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MKX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "COBLL1"
type: "gene"
col: 1346
ensembl_id: "ENSG00000082438"
name: "cordon-bleu WH2 repeat protein like 1"
location: "2q24.3"
module: 34
arm: "+"
pooled_cpm: 50.99
n_lines_expressing: 43
n_dd_up: 24
n_dd_down: 10
n_dd_up_clean: 21
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# COBLL1

*cordon-bleu WH2 repeat protein like 1* — 2q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +13.0, q 4e-36, up in 29 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.465× (z -13.6, q 3e-39, down in 29 of 41 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGMS1]] (+0.59, fdr 1e-05), [[SMAD1]] (+0.56, fdr 1e-04), [[RDX]] (+0.56, fdr 2e-05); moves opposite to [[BAIAP3]] (-0.55, fdr 9e-05), [[HIF1AN]] (-0.54, fdr 5e-05), [[ARHGEF4]] (-0.53, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[JDP2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZBTB8A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1346.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +13.0 | 4e-36 | 29/41 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +10.4 | 4e-23 | 22/41 (hTERT-HPNE, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +6.9 | 1e-09 | 25/41 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.8 | 2e-09 | 25/41 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +6.0 | 3e-07 | 20/40 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.3 | 1e-05 | 20/41 (hTERT-HPNE, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.33×** | +5.1 | 3e-05 | 20/42 (HT-29, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +5.1 | 3e-05 | 19/41 (C32, KATO III, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +4.7 | 1e-04 | 16/41 (NCI-H1573, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +4.7 | 2e-04 | 18/41 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +4.6 | 3e-04 | 19/40 (NCI-H1573, Hs 766T, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.31×** | +4.5 | 3e-04 | 14/40 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.26×** | +4.2 | 9e-04 | 16/42 (NCI-H1573, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +4.2 | 9e-04 | 16/41 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **1.58×** | +4.2 | 1e-03 | 19/39 (LoVo, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.21×** | +4.1 | 0.002 | 15/41 (NCI-H1573, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1346.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.465×** | -13.6 | 3e-39 | 29/41 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.484×** | -12.9 | 2e-35 | 32/41 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.562×** | -10.2 | 3e-22 | 28/41 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.605×** | -8.9 | 6e-17 | 32/41 (LoVo, HT-29, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **0.731×** | -5.6 | 3e-06 | 19/39 (J82, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **0.819×** | -5.0 | 4e-05 | 18/41 (J82, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.742×** | -3.8 | 0.012 | 13/41 (A498, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.767×** | -3.4 | 0.046 | 14/38 (SK-MEL-2, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.696×** | -3.4 | 0.046 | 12/36 (SK-MEL-2, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.823×** | -3.3 | 0.046 | 15/34 (A498, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.838× | -3.1 | 0.085 | 15/42 (CHP-212, BT-474, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.787× | -3.0 | 0.11 | 12/39 (HT-29, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -3.0 | 0.11 | 14/41 (J82, A549, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1346. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 43.6 | 20 | 0 | [[Triamcinolone (drug)]] 5 µM 4.57× (z +14.9) | — |
| [[Hs 766T (line)]] | wt | 30.7 | 16 | 0 | [[Budesonide (drug)]] 5 µM 8.47× (z +12.5) | — |
| [[NCI-H1792 (line)]] | alt | 30.4 | 16 (1 ⚠) | 0 | [[Dexamethasone (drug)]] 0.5 µM 6.51× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 29.7 | 15 | 0 | [[Budesonide (drug)]] 5 µM 5.30× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 35.5 | 13 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 4.25× (z +11.2) | — |
| [[C32 (line)]] | wt | 41.7 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.50× (z +12.9) | — |
| [[A498 (line)]] | wt | 120 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -19.3) |
| [[HT-29 (line)]] | alt | 151 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -15.4) |
| [[LoVo (line)]] | wt | 115 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.305× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 74.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.375× (z -11.6) |
| [[LS 180 (line)]] | wt | 78.3 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +13.9) | [[Panobinostat (drug)]] 0.5 µM 0.240× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 49.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.77× (z +17.3) | — |
| [[KATO III (line)]] | alt | 95.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 91.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -10.6) |
| [[SW48 (line)]] | wt | 45.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.0618× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[A-427 (line)]] | wt | 65.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.448× (z -9.0) |
| [[BT-474 (line)]] | alt | 76.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +13.2) | [[Belinostat (drug)]] 5 µM 0.294× (z -10.8) |
| [[COLO 205 (line)]] | alt | 69.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.232× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 162 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -12.2) |
| [[J82 (line)]] | alt | 68.0 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.452× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 125 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.367× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 42.8 | 2 | 0 | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 3.22× (z +10.9) | — |
| [[NCI-H460 (line)]] | wt | 29.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +18.8) | — |
| [[RKO (line)]] | wt | 47.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -17.7) |
| [[SW1417 (line)]] | alt | 56.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.273× (z -11.0) |
| [[A549 (line)]] | wt | 43.9 | 1 | 0 | [[Clobetasol propionate (drug)]] 5 µM 2.90× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 19.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +16.5) | — |
| [[A-172 (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.70 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.16 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.22 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.46 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1346), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGMS1]] | +0.59 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[SMAD1]] | +0.56 | +0.52 / +0.36 | both halves | 1e-04 |  |
| [[RDX]] | +0.56 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ZBTB8A]] | +0.54 | +0.51 / +0.34 | both halves | 1e-04 |  |
| [[BATF]] | +0.53 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[FGD4]] | +0.53 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[SETD7]] | +0.53 | +0.51 / +0.31 | both halves | 2e-04 |  |
| [[OXCT1]] | +0.52 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[ATAD2B]] | +0.52 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[NFIB]] | +0.52 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[PDLIM1]] | +0.51 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[TDRD3]] | +0.51 | +0.36 / +0.37 | both halves | 1e-04 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAIAP3]] | -0.55 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[HIF1AN]] | -0.54 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ARHGEF4]] | -0.53 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[AFAP1]] | -0.53 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[WNT7B]] | -0.53 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[UBA6]] | -0.52 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[FCHO1]] | -0.52 | -0.51 / -0.25 | both halves | 4e-04 |  |
| [[MFSD12]] | -0.52 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[FCHSD1]] | -0.50 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[LTBP4]] | -0.50 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[NPTX1]] | -0.50 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[VRK3]] | -0.50 | -0.45 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JDP2]] | B | JDP2 activity raises COBLL1's level | lines that do not express JDP2 (12) vs lines expressing it (38) | 2.23× lower at baseline in the lines without JDP2 | 0.024 | ⚠ within organs, on part of the lines; also absent: JUP, LINC01836, SEL1L3; maybe low, not absent |
| [[TBC1D30]] | B | TBC1D30 activity raises COBLL1's level | lines that do not express TBC1D30 (8) vs lines expressing it (42) | 1.68× lower at baseline in the lines without TBC1D30 | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000288591, RAB3IP; maybe low, not absent |
| [[SYT13]] | B | SYT13 activity raises COBLL1's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 1.83× lower at baseline in the lines without SYT13 | 0.050 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1 |
| [[GRHL2]] | B | GRHL2 activity raises COBLL1's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 2.04× lower at baseline in the lines without GRHL2 | 0.062 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[MAP2K1]] | B | MAP2K1 activity lowers COBLL1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZBTB8A]] | B | COBLL1 activity lowers ZBTB8A's level | lines that do not express COBLL1 (7) vs lines expressing it (43) | 1.54× higher at baseline in the lines without COBLL1 | 0.035 | ⚠ within organs, on part of the lines; also absent: LRRCC1, DSG2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction -0.458). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.2, 10.7); signed map (26.1, -26.5). **Vector** length 128, 36.5% of its response variance represented; |z| ≥ 3 in 1,310 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +13.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +6.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +4.8 | +3.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.8 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +5.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +4.5 | +3.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.3 | +3.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.1 | +2.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -7.6 | -12.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.5 | -13.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.8 | -10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -8.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.7 | -5.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -1.6 |
|  | [[4EGI-1 (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | cordon-bleu WH2 repeat protein like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.3 — chr2:164,653,624-164,843,679 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0977 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q53SF7](https://www.uniprot.org/uniprotkb/Q53SF7) carries no function annotation.

**Summary**, from NCBI Gene [22837](https://www.ncbi.nlm.nih.gov/gene/22837):

> Enables cadherin binding activity. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23571](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23571) · Entrez [22837](https://www.ncbi.nlm.nih.gov/gene/22837) · UniProt [Q53SF7](https://www.uniprot.org/uniprotkb/Q53SF7) · Ensembl [ENSG00000082438](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082438)

## Data

Gene col 1346: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1346); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1346, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1346]; `tensor/DDL_lfc|DDL_z.npy` [1346]; `embed/gene_vectors.npy` [1346]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1346 or target_col == 1346). Every well: [[COBLL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COBLL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

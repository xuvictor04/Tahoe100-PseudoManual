---
symbol: "HLA-DMA"
type: "gene"
col: 12838
ensembl_id: "ENSG00000204257"
name: "major histocompatibility complex, class II, DM alpha"
location: "6p21.32"
module: 15
arm: "+"
pooled_cpm: 6.91
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 16
n_dd_up_clean: 20
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# HLA-DMA

*major histocompatibility complex, class II, DM alpha* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.08× (z +32.9, q 0e+00, up in 39 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.527× (z -7.6, q 1e-11, down in 22 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPESP1]] (+0.78, fdr 7e-06), [[KLF3-AS1]] (+0.75, fdr 7e-06), [[DARS1-AS1]] (+0.74, fdr 7e-06); moves opposite to [[NAA40]] (-0.62, fdr 4e-05), [[SPIDR]] (-0.60, fdr 4e-05), [[STUB1]] (-0.60, fdr 5e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12838.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.08×** | +32.9 | 0e+00 | 39/40 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.00×** | +12.5 | 2e-33 | 29/35 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +9.3 | 2e-18 | 24/37 (PANC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.78×** | +6.8 | 1e-09 | 25/44 (SW480, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +6.3 | 3e-08 | 12/29 (KATO III, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.58×** | +5.4 | 5e-06 | 19/43 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +4.9 | 8e-05 | 17/45 (HEC-1-A, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.5 | 5e-04 | 16/45 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.2 | 0.002 | 9/46 (NCI-H2030, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +4.1 | 0.002 | 14/44 (Panc 03.27, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.003 | 8/45 (HOP62, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.013 | 12/42 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.5 | 0.019 | 4/47 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.019 | 13/39 (LoVo, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.019 | 5/45 (SW480, A498, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.033 | 4/46 (KATO III, A498, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.042 | 5/47 (KATO III, H4, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12838.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.527×** | -7.6 | 1e-11 | 22/45 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.538×** | -7.4 | 5e-11 | 23/46 (SW480, H4, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.601×** | -6.0 | 3e-07 | 20/44 (H4, SW480, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.636×** | -5.2 | 3e-05 | 19/43 (Panc 03.27, HEC-1-A, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.656×** | -5.0 | 6e-05 | 17/43 (SW480, RPMI-7951, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.464×** | -4.8 | 2e-04 | 12/42 (SW480, H4, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.694×** | -4.3 | 0.001 | 15/44 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.512×** | -4.2 | 0.002 | 8/39 (SW480, HCT15, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.702×** | -4.0 | 0.003 | 12/44 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.732×** | -3.7 | 0.011 | 9/45 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.757×** | -3.3 | 0.047 | 11/44 (SW 900, A-172, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.761×** | -3.3 | 0.052 | 8/45 (SW480, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | **0.762×** | -3.2 | 0.052 | 15/36 (SW480, H4, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~65% of this change | **0.757×** | -3.2 | 0.056 | 15/31 (A-172, A498, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.766×** | -3.2 | 0.056 | 8/46 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.761×** | -3.1 | 0.077 | 15/43 (H4, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12838. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 49.4 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0721× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.194× (z -8.9) |
| [[SW480 (line)]] | alt | 26.3 | 1 | 6 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.0805× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 20.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0740× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 6.06 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 11.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.81× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 6.10 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.72× (z +13.2) | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.114× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 2.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +8.9) | — |
| [[C32 (line)]] | wt | 2.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 3.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.48× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 7.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.10× (z +12.9) | — |
| [[HS-578T (line)]] | alt | 2.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 4.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.16× (z +10.5) | — |
| [[J82 (line)]] | alt | 3.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.70× (z +8.9) | — |
| [[LoVo (line)]] | wt | 5.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +13.6) | — |
| [[LOX-IMVI (line)]] | wt | 3.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.88× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.9× (z +13.8) | — |
| [[NCI-H1792 (line)]] | alt | 3.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.70× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 2.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.33× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 4.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 4.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 8.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +15.1) | — |
| [[SNU-423 (line)]] | alt | 3.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +10.8) | — |
| [[SW 900 (line)]] | alt | 5.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.19× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 3.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +10.8) | — |
| [[A-172 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12838), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPESP1]] | +0.78 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[KLF3-AS1]] | +0.75 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[DARS1-AS1]] | +0.74 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ITFG2-AS1]] | +0.74 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[PELO-AS1]] | +0.74 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[ZNF213-AS1]] | +0.73 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[PRANCR]] | +0.73 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[UPP2]] | +0.73 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.73 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[DICER1-AS1]] | +0.72 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[HAVCR2]] | +0.71 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[DDX59-AS1]] | +0.71 | +0.69 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA40]] | -0.62 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[SPIDR]] | -0.60 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[STUB1]] | -0.60 | -0.41 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HLA-DMA's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MIA]] | B | MIA activity raises HLA-DMA's level | lines that do not express MIA (10) vs lines expressing it (40) | 1.37× lower at baseline in the lines without MIA | 0.093 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers HLA-DMA's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.729). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.8, 21.0); signed map (27.9, -6.1). **Vector** length 75.2, 13.1% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.0 | +32.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +12.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.2 | -7.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +0.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | -2.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.8 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | major histocompatibility complex, class II, DM alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:32,948,613-32,969,094 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D6S222E, RING6 |
| Gene groups (HGNC) | Histocompatibility complex; C1-set domain containing |
| Hallmark sets | ALLOGRAFT_REJECTION, INTERFERON_GAMMA_RESPONSE |
| Reactome | 5 pathways, smallest: Processing of antigen in germinal center B cells; MHC class II antigen presentation; Affinity selection of immunoglobulins |
| Matched by | ensembl_id |

**Function**, from UniProt [P28067](https://www.uniprot.org/uniprotkb/P28067) (HLA class II histocompatibility antigen, DM alpha chain):

> Plays a critical role in catalyzing the release of class II-associated invariant chain peptide (CLIP) from newly synthesized MHC class II molecules and freeing the peptide binding site for acquisition of antigenic peptides. In B-cells, the interaction between HLA-DM and MHC class II molecules is regulated by HLA-DO.

**Summary**, from NCBI Gene [3108](https://www.ncbi.nlm.nih.gov/gene/3108):

> HLA-DMA belongs to the HLA class II alpha chain paralogues. This class II molecule is a heterodimer consisting of an alpha (DMA) and a beta chain (DMB), both anchored in the membrane. It is located in intracellular vesicles. DM plays a central role in the peptide loading of MHC class II molecules by helping to release the CLIP molecule from the peptide binding site. Class II molecules are expressed in antigen presenting cells (APC: B lymphocytes, dendritic cells, macrophages). The alpha chain …

**Accessions** — [HGNC:4934](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4934) · Entrez [3108](https://www.ncbi.nlm.nih.gov/gene/3108) · UniProt [P28067](https://www.uniprot.org/uniprotkb/P28067) · Ensembl [ENSG00000204257](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204257)

## Data

Gene col 12838: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12838); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12838, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12838]; `tensor/DDL_lfc|DDL_z.npy` [12838]; `embed/gene_vectors.npy` [12838]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12838 or target_col == 12838). Every well: [[HLA-DMA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HLA-DMA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

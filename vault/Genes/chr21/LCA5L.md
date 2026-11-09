---
symbol: "LCA5L"
type: "gene"
col: 8085
ensembl_id: "ENSG00000157578"
name: "lebercilin LCA5 like"
location: "21q22.2"
module: 35
arm: "+"
pooled_cpm: 3.56
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 5
n_dd_up_clean: 21
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# LCA5L

*lebercilin LCA5 like* — 21q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.71× (z +15.6, q 0e+00, up in 34 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.514× (z -7.4, q 8e-11, down in 21 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPAG5-AS1]] (+0.68, fdr 1e-05), [[LINC02951]] (+0.64, fdr 3e-05), [[DUSP28]] (+0.64, fdr 1e-05); moves opposite to [[LDHB]] (-0.54, fdr 1e-04), [[ALDH3A2]] (-0.53, fdr 2e-04), [[CDCA7L]] (-0.52, fdr 7e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8085.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.71×** | +15.6 | 0e+00 | 34/39 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.16×** | +12.0 | 9e-31 | 25/37 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.76×** | +11.2 | 6e-27 | 34/46 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.52×** | +10.2 | 3e-22 | 32/45 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.38×** | +9.2 | 4e-18 | 28/44 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +7.6 | 3e-12 | 3/4 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.7 | 7e-07 | 15/35 (C-33 A, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.7 | 7e-07 | 12/33 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +5.4 | 5e-06 | 17/35 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +5.1 | 2e-05 | 9/43 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.58×** | +5.1 | 2e-05 | 12/44 (SW480, COLO 205, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.0 | 2e-05 | 7/20 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.63×** | +5.0 | 3e-05 | 3/7 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +4.8 | 8e-05 | 6/19 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +4.5 | 2e-04 | 9/45 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +4.5 | 2e-04 | 11/45 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.5 | 2e-04 | 13/46 (A549, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.91×** | +3.7 | 0.006 | 3/42 (A-172, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Monocrotaline (drug)]] 0.05 µM |  | **1.40×** | +3.4 | 0.017 | 2/32 (NCI-H2030, A-427) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8085.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.514×** | -7.4 | 8e-11 | 21/46 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.582×** | -5.8 | 2e-06 | 16/42 (A-427, HOP62, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.713×** | -3.8 | 0.031 | 13/29 (NCI-H460, A-427, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.541×** | -3.6 | 0.050 | 11/42 (HOP62, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.738×** | -3.4 | 0.083 | 12/44 (A549, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.741× | -3.2 | 0.12 | 11/43 (BT-474, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.580× | -3.2 | 0.12 | 6/34 (LoVo, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Malotilate (drug)]] 0.05 µM |  | 0.758× | -3.1 | 0.14 | 10/41 (RKO, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8085. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.04 | 0 | 2 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.113× (z -9.1) |
| [[KATO III (line)]] | alt | 4.74 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0458× (z -10.8) |
| [[LoVo (line)]] | wt | 3.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 4.25 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0595× (z -8.9) |
| [[SW480 (line)]] | alt | 5.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +8.6) | — |
| [[A-172 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8085), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG5-AS1]] | +0.68 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[LINC02951]] | +0.64 | +0.72 / +0.44 | both halves | 3e-05 |  |
| [[DUSP28]] | +0.64 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[USP34-DT]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[ATE1OSP]] | +0.62 | +0.77 / +0.46 | both halves | 2e-05 |  |
| [[PPP3CB-AS1]] | +0.61 | +0.74 / +0.43 | both halves | 4e-05 |  |
| [[PJVK]] | +0.61 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[DNAJC9-AS1-1]] | +0.61 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PPP1R3F]] | +0.60 | +0.73 / +0.32 | both halves | 2e-04 |  |
| [[LINC00863]] | +0.60 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[DDX19A-DT]] | +0.59 | +0.74 / +0.37 | both halves | 8e-05 |  |
| [[COPZ2]] | +0.59 | +0.54 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDHB]] | -0.54 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[ALDH3A2]] | -0.53 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[CDCA7L]] | -0.52 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[PPP1CC]] | -0.52 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[THEM6]] | -0.52 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[HPSE]] | -0.52 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[TBC1D2B]] | -0.51 | -0.58 / -0.22 | both halves | 6e-04 |  |
| [[PRKAR2B]] | -0.51 | -0.32 / -0.25 | both halves | 4e-04 |  |
| [[TGFBR3]] | -0.51 | -0.45 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LCA5L's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.6% of all compounds | 0.006 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.619). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (8.9, 21.1); signed map (29.4, -3.3). **Vector** length 43.4, 4.72% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +15.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +4.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +5.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.1 | +2.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.1 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +4.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | +1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.6 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +0.1 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | +3.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | lebercilin LCA5 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.2 — chr21:39,405,728-39,445,805 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33295; previously C21orf13 |
| Matched by | ensembl_id |

UniProt [O95447](https://www.uniprot.org/uniprotkb/O95447) carries no function annotation.

**Summary**, from NCBI Gene [150082](https://www.ncbi.nlm.nih.gov/gene/150082):

> Predicted to be involved in intraciliary transport. Predicted to be active in axoneme. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1255](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1255) · Entrez [150082](https://www.ncbi.nlm.nih.gov/gene/150082) · UniProt [O95447](https://www.uniprot.org/uniprotkb/O95447) · Ensembl [ENSG00000157578](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157578)

## Data

Gene col 8085: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8085); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8085, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8085]; `tensor/DDL_lfc|DDL_z.npy` [8085]; `embed/gene_vectors.npy` [8085]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8085 or target_col == 8085). Every well: [[LCA5L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LCA5L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

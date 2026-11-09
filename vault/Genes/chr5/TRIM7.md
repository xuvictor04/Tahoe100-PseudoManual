---
symbol: "TRIM7"
type: "gene"
col: 7056
ensembl_id: "ENSG00000146054"
name: "tripartite motif containing 7"
location: "5q35.3"
module: 15
arm: "+"
pooled_cpm: 4.76
n_lines_expressing: 41
n_dd_up: 9
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# TRIM7

*tripartite motif containing 7* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.16× (z +11.6, q 1e-28, up in 28 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.444× (z -12.2, q 1e-31, down in 25 of 31 measured lines).
> Its strongest partners by |cos| (76 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCTD1]] (+0.61, fdr 1e-04), [[LEMD3]] (+0.60, fdr 1e-04), [[PHC2-AS1]] (+0.60, fdr 2e-04); moves opposite to [[EXOC3]] (-0.52, fdr 1e-04), [[KIF3B]] (-0.49, fdr 7e-05), [[TBC1D19]] (-0.45, fdr 6e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[ANP32A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7056.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +11.6 | 1e-28 | 28/34 (NCI-H23, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +7.6 | 8e-12 | 3/8 (CFPAC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.03×** | +7.5 | 1e-11 | 17/22 (LS 180, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +5.1 | 6e-05 | 6/20 (SW 900, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.6 | 5e-04 | 11/29 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.011 | 5/37 (NCI-H2030, AsPC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +3.6 | 0.023 | 5/15 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.2 | 0.082 | 4/31 (NCI-H2030, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.2 | 0.082 | 4/23 (LoVo, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | 1.35× | +3.1 | 0.12 | 8/29 (A-172, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, none with an alert; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7056.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.444×** | -12.2 | 1e-31 | 25/31 (LoVo, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.344×** | -11.4 | 2e-27 | 30/38 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.360×** | -10.9 | 2e-25 | 26/37 (Hs 766T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.410×** | -9.5 | 3e-19 | 27/38 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.454×** | -8.4 | 5e-15 | 24/38 (SW 900, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.498×** | -7.4 | 1e-11 | 22/31 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.500×** | -7.1 | 1e-10 | 18/38 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.355×** | -5.8 | 5e-07 | 20/35 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.599×** | -5.5 | 3e-06 | 14/36 (SW 900, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.586×** | -5.4 | 4e-06 | 14/35 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.650×** | -4.6 | 2e-04 | 17/38 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.470×** | -4.2 | 0.001 | 15/35 (PANC-1, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.726×** | -3.4 | 0.029 | 10/37 (A-427, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.730×** | -3.3 | 0.033 | 13/36 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.552×** | -3.3 | 0.036 | 7/37 (LS 180, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7056. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 17.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -12.0) |
| [[LoVo (line)]] | wt | 11.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 7.87 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0583× (z -15.8) |
| [[A-172 (line)]] | wt | 5.77 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0992× (z -9.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 6.95 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.126× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 4.34 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -8.5) |
| [[HS-578T (line)]] | alt | 4.64 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0715× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 9.46 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -9.0) |
| [[PANC-1 (line)]] | alt | 6.79 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -10.6) |
| [[SW 900 (line)]] | alt | 7.58 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0939× (z -9.0) |
| [[SW480 (line)]] | alt | 5.64 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -12.0) |
| [[A498 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.696 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.909 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.765 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.677 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.635 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7056), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 24 of them with an alert (⚠; 24 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD1]] | +0.61 | +0.33 / +0.53 | both halves | 1e-04 |  |
| [[LEMD3]] | +0.60 | +0.34 / +0.44 | both halves | 1e-04 |  |
| [[PHC2-AS1]] | +0.60 | +0.30 / +0.61 | both halves | 2e-04 |  |
| [[ABHD15]] | +0.59 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[SLC12A9]] | +0.59 | +0.33 / +0.59 | both halves | 1e-04 |  |
| [[PROCA1]] | +0.57 | +0.37 / +0.48 | both halves | 9e-05 |  |
| [[PTGR3]] | +0.57 | +0.28 / +0.59 | both halves | 3e-04 |  |
| [[HOXB7]] | +0.57 | +0.30 / +0.49 | both halves | 2e-04 |  |
| [[TMEM187]] | +0.56 | +0.37 / +0.54 | both halves | 9e-05 |  |
| [[CDNF]] | +0.56 | +0.20 / +0.45 | both halves | 7e-04 |  |
| [[SATB2-AS1]] | +0.56 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[TP53I13]] | +0.56 | +0.42 / +0.63 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC3]] | -0.52 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[KIF3B]] | -0.49 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[TBC1D19]] | -0.45 | -0.22 / -0.45 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TRIM7's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers TRIM7's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANP32A]] | B | TRIM7 activity lowers ANP32A's level | lines that do not express TRIM7 (9) vs lines expressing it (41) | 1.11× higher at baseline in the lines without TRIM7 | 0.073 | ⚠ within organs, on part of the lines; also absent: IRAK2, A4GALT, PAPSS2 |
| [[LEMD3]] | B | TRIM7 activity lowers LEMD3's level | lines that do not express TRIM7 (9) vs lines expressing it (41) | 1.26× higher at baseline in the lines without TRIM7 | 0.089 | ⚠ within organs, on part of the lines; also absent: IRAK2, A4GALT, PAPSS2; its own permutation p |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.524). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.5, 19.9); signed map (17.6, -5.9). **Vector** length 44.4, 6.10% of its response variance represented; |z| ≥ 3 in 768 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +11.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +4.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +0.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +1.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.1 | +1.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -2.1 | -10.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.0 | -11.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -7.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.9 | -9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.5 | -12.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.8 | -0.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.7 | -1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -0.7 | -0.2 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:181,193,924-181,205,293 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNF90, GNIP |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C029](https://www.uniprot.org/uniprotkb/Q9C029) (E3 ubiquitin-protein ligase TRIM7):

> E3 ubiquitin-protein ligase that have both tumor-promoting and tumor-suppressing activities and functions in several biological processes including innate immunity, regulation of ferroptosis as well as cell proliferation and migration. Acts as an antiviral effector against multiple viruses by targeting specific viral proteins for ubiquitination and degradation including norovirus NTPase protein or SARS-CoV-2 NSP5 and NSP8 proteins. Mechanistically, recognizes the C-terminal glutamine-containing …

**Summary**, from NCBI Gene [81786](https://www.ncbi.nlm.nih.gov/gene/81786):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1, a B-box type 2, and a coiled-coil region. The protein localizes to both the nucleus and the cytoplasm, and may represent a participant in the initiation of glycogen synthesis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:16278](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16278) · Entrez [81786](https://www.ncbi.nlm.nih.gov/gene/81786) · UniProt [Q9C029](https://www.uniprot.org/uniprotkb/Q9C029) · Ensembl [ENSG00000146054](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146054)

## Data

Gene col 7056: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7056); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7056, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7056]; `tensor/DDL_lfc|DDL_z.npy` [7056]; `embed/gene_vectors.npy` [7056]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7056 or target_col == 7056). Every well: [[TRIM7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

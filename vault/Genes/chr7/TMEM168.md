---
symbol: "TMEM168"
type: "gene"
col: 7121
ensembl_id: "ENSG00000146802"
name: "transmembrane protein 168"
location: "7q31.1"
module: 4
arm: "+"
pooled_cpm: 58.11
n_lines_expressing: 48
n_dd_up: 0
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# TMEM168

*transmembrane protein 168* — 7q31.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.604× (z -13.7, q 5e-40, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOG]] (+0.65, fdr 1e-05), [[SCMH1]] (+0.59, fdr 1e-05), [[TERF2]] (+0.58, fdr 1e-05); moves opposite to [[LINC00672]] (-0.57, fdr 1e-05), [[LASP1]] (-0.56, fdr 1e-05), [[LINC00310]] (-0.51, fdr 2e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7121.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.604×** | -13.7 | 5e-40 | 35/47 (LOX-IMVI, C32, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.550×** | -11.5 | 3e-28 | 39/47 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.544×** | -11.3 | 3e-27 | 30/42 (A549, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.491×** | -9.6 | 2e-19 | 37/43 (SK-MEL-2, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.606×** | -9.3 | 2e-18 | 34/48 (A-427, C32, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.664×** | -7.6 | 3e-12 | 31/46 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.791×** | -6.4 | 1e-08 | 25/46 (J82, C32, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.828×** | -5.2 | 2e-05 | 23/46 (J82, NCI-H2347, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.603×** | -5.1 | 2e-05 | 19/35 (HCT15, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **0.808×** | -4.1 | 0.002 | 21/46 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.868× | -3.9 | 0.006 | 16/46 (J82, HEC-1-A, …) | top dose only | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.816×** | -3.8 | 0.007 | 21/45 (NCI-H460, C32, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.789×** | -3.3 | 0.047 | 16/46 (HEC-1-A, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7121. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 168 | 0 | 8 (5 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 79.6 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -12.4) |
| [[A549 (line)]] | wt | 62.3 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -12.9) |
| [[LOX-IMVI (line)]] | wt | 92.6 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -21.7) |
| [[RKO (line)]] | wt | 80.5 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -14.1) |
| [[A-427 (line)]] | wt | 74.9 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0736× (z -30.8) |
| [[HEC-1-A (line)]] | alt | 52.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.329× (z -9.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 57.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0568× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -11.2) |
| [[J82 (line)]] | alt | 44.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -16.6) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -8.6) |
| [[LS 180 (line)]] | wt | 62.4 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -13.4) |
| [[SHP-77 (line)]] | alt | 60.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -8.9) |
| [[SW48 (line)]] | wt | 70.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -10.8) |
| [[HOP62 (line)]] | alt | 41.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -14.4) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -8.7) |
| [[KATO III (line)]] | alt | 99.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -14.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 60.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -10.4) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H1792 (line)]] | alt | 64.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -10.2) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H23 (line)]] | alt | 92.9 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 44.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -10.2) |
| [[SNU-423 (line)]] | alt | 47.6 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -10.4) |
| [[SW1417 (line)]] | alt | 80.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -11.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 42.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -9.0) |
| [[A498 (line)]] | wt | 70.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -11.0) |
| [[C-33 A (line)]] | alt | 71.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -10.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 71.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0638× (z -14.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 46.9 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0645× (z -10.9) ⚠ toxic |
| [[HT-29 (line)]] | alt | 84.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -9.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -16.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 93.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 40.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7121), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOG]] | +0.65 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[SCMH1]] | +0.59 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[TERF2]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[TMEM177]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[JPX]] | +0.53 | +0.40 / +0.67 | both halves | 4e-05 |  |
| [[UQCC2]] | +0.53 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[ERCC8]] | +0.53 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[PTPMT1]] | +0.53 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[MTMR9]] | +0.52 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[KRI1]] | +0.51 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[COA4]] | +0.51 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[EIF2B3]] | +0.51 | +0.34 / +0.55 | both halves | 1e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00672]] | -0.57 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[LASP1]] | -0.56 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[LINC00310]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ADCY10]] | -0.50 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[CD27-AS1]] | -0.50 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[KLHL15]] | -0.50 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[CDKL2]] | -0.48 | -0.48 / -0.43 | both halves | 4e-05 |  |
| [[PLCD4]] | -0.47 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[KIAA1191]] | -0.47 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[OAT]] | -0.47 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[LNX2]] | -0.47 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[MAP7D2]] | -0.47 | -0.38 / -0.51 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TMEM168's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.388). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-16.8, -45.1); signed map (6.7, -46.3). **Vector** length 85.6, 18.7% of its response variance represented; |z| ≥ 3 in 867 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.6 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +1.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.0 | +2.4 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -9.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -13.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -4.0 | -6.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | -3.0 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -5.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 168 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.1 — chr7:112,762,377-112,790,423 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp564C012, FLJ13576 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0V1](https://www.uniprot.org/uniprotkb/Q9H0V1) (Transmembrane protein 168):

> Plays a key role in maintaining the cardiac electrical stability by modulating cell surface expression of SCN5A. May play a role in the modulation of anxiety behavior by regulating GABAergic neuronal system in the nucleus accumbens (By similarity).

**Summary**, from NCBI Gene [64418](https://www.ncbi.nlm.nih.gov/gene/64418):

> Enables sodium channel regulator activity. Predicted to act upstream of or within regulation of ubiquitin-dependent protein catabolic process and regulation of voltage-gated sodium channel activity. Located in nuclear membrane and transport vesicle. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:25826](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25826) · Entrez [64418](https://www.ncbi.nlm.nih.gov/gene/64418) · UniProt [Q9H0V1](https://www.uniprot.org/uniprotkb/Q9H0V1) · Ensembl [ENSG00000146802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146802)

## Data

Gene col 7121: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7121); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7121, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7121]; `tensor/DDL_lfc|DDL_z.npy` [7121]; `embed/gene_vectors.npy` [7121]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7121 or target_col == 7121). Every well: [[TMEM168 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM168.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

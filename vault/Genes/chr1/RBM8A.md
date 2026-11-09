---
symbol: "RBM8A"
type: "gene"
col: 15453
ensembl_id: "ENSG00000265241"
name: "RNA binding motif protein 8A"
location: "1q21.1"
module: 11
arm: "+"
pooled_cpm: 77.57
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# RBM8A

*RNA binding motif protein 8A* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.74× (z +7.9, q 1e-12, up in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~76% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.65× (z +7.2, q 1e-10, up in 42 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.431×; ⚠ cell-cycle shift, explains ~76% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBCC]] (+0.70, fdr 7e-06), [[CPT2]] (+0.66, fdr 7e-06), [[GPANK1]] (+0.64, fdr 7e-06); moves opposite to [[MAPK9]] (-0.66, fdr 1e-05), [[SEL1L3]] (-0.57, fdr 1e-05), [[PIP4K2A]] (-0.54, fdr 7e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15453.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.74×** | +7.9 | 1e-12 | 40/48 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +7.6 | 1e-11 | 46/47 (CFPAC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +7.2 | 1e-10 | 42/49 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.98×** | +6.9 | 6e-10 | 42/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.82×** | +6.1 | 1e-07 | 47/48 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **3.02×** | +5.9 | 4e-07 | 42/49 (COLO 205, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.98×** | +5.8 | 4e-07 | 34/49 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.81×** | +5.8 | 5e-07 | 40/48 (NCI-H1573, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.83×** | +5.2 | 1e-05 | 41/48 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.002 | 34/48 (A-172, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.50×** | +4.0 | 0.004 | 27/44 (A-172, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +3.7 | 0.009 | 33/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | **1.44×** | +3.7 | 0.010 | 28/47 (NCI-H1792, NCI-H460, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.40×** | +3.4 | 0.030 | 28/48 (Hs 766T, A-172, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~77% of this change | **1.37×** | +3.1 | 0.072 | 24/47 (COLO 205, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15453.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.431×; ⚠ cell-cycle shift, explains ~76% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.713× | -3.4 | 0.32 | 36/48 (SW1417, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15453. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 76.0 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.89× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 66.1 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.6) | — |
| [[LoVo (line)]] | wt | 62.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +13.3) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 69.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +12.2) ⚠ cell-cycle shift, explains ~76% of this change | — |
| [[NCI-H460 (line)]] | wt | 70.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +11.5) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.97× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 80.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.8) ⚠ cell-cycle shift, explains ~76% of this change | — |
| [[A-427 (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -10.1) ⚠ cell-cycle shift, explains ~76% of this change |
| [[A498 (line)]] | wt | 67.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.0) ⚠ cell-cycle shift, explains ~76% of this change | — |
| [[A549 (line)]] | wt | 56.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +12.6) ⚠ cell-cycle shift, explains ~76% of this change | — |
| [[AsPC-1 (line)]] | alt | 82.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.4) | — |
| [[C32 (line)]] | wt | 56.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +8.8) ⚠ cell-cycle shift, explains ~76% of this change | — |
| [[CFPAC-1 (line)]] | alt | 98.2 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.30× (z +8.9) ⚠ toxic | — |
| [[COLO 205 (line)]] | alt | 78.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +8.8) ⚠ cell-cycle shift, explains ~76% of this change | — |
| [[HS-578T (line)]] | alt | 45.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +8.9) | — |
| [[KATO III (line)]] | alt | 64.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.12× (z +8.7) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 72.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +12.7) ⚠ cell-cycle shift, explains ~76% of this change | — |
| [[AN3 CA (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 98.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 62.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 86.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 159 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 83.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15453), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCC]] | +0.70 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[CPT2]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[GPANK1]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[ABT1]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[SAP18]] | +0.61 | +0.72 / +0.55 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 916 |
| [[EID2]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[MED18]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[CRNKL1]] | +0.59 | +0.65 / +0.49 | both halves | 1e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 833 |
| [[PDCD7]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[UQCRFS1]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ARMC5]] | +0.58 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[CHKB-DT]] | +0.58 | +0.63 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK9]] | -0.66 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[SEL1L3]] | -0.57 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[PIP4K2A]] | -0.54 | -0.65 / -0.38 | both halves | 7e-05 |  |
| [[LIMK1]] | -0.52 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[DGKZ]] | -0.51 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[VOPP1]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[APIP]] | -0.51 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[FAM20B]] | -0.51 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[HACD3]] | -0.51 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[DNM1]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RBM8A's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.5, 5.4); signed map (2.5, -17.4). **Vector** length 67.5, 21.0% of its response variance represented; |z| ≥ 3 in 702 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +4.6 | +7.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +6.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.1 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +2.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.5 | +1.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.8 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | -4.6 | +5.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~77% of this change | -4.1 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.5 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 8A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.1 — chr1:145,921,556-145,927,678 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNRP, BOV-1A, BOV-1B, BOV-1C, Y14; previously RBM8 |
| Gene groups (HGNC) | RNA binding motif containing; Exon junction complex; Spliceosomal P complex |
| Reactome | 13 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5S9](https://www.uniprot.org/uniprotkb/Q9Y5S9) (RNA-binding protein 8A):

> Required for pre-mRNA splicing as component of the spliceosome. Core component of the splicing-dependent multiprotein exon junction complex (EJC) deposited at splice junctions on mRNAs. The EJC is a dynamic structure consisting of core proteins and several peripheral nuclear and cytoplasmic associated factors that join the complex only transiently either during EJC assembly or during subsequent mRNA metabolism. The EJC marks the position of the exon-exon junction in the mature mRNA for the gene …

**Summary**, from NCBI Gene [9939](https://www.ncbi.nlm.nih.gov/gene/9939):

> This gene encodes a protein with a conserved RNA-binding motif. The protein is found predominantly in the nucleus, although it is also present in the cytoplasm. It is preferentially associated with mRNAs produced by splicing, including both nuclear mRNAs and newly exported cytoplasmic mRNAs. It is thought that the protein remains associated with spliced mRNAs as a tag to indicate where introns had been present, thus coupling pre- and post-mRNA splicing events. Previously, it was thought that …

**Accessions** — [HGNC:9905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9905) · Entrez [9939](https://www.ncbi.nlm.nih.gov/gene/9939) · UniProt [Q9Y5S9](https://www.uniprot.org/uniprotkb/Q9Y5S9) · Ensembl [ENSG00000265241](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000265241)

## Data

Gene col 15453: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15453); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15453, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15453]; `tensor/DDL_lfc|DDL_z.npy` [15453]; `embed/gene_vectors.npy` [15453]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15453 or target_col == 15453). Every well: [[RBM8A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM8A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

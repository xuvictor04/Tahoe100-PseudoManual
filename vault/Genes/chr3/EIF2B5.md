---
symbol: "EIF2B5"
type: "gene"
col: 6961
ensembl_id: "ENSG00000145191"
name: "eukaryotic translation initiation factor 2B subunit epsilon"
location: "3q27.1"
module: 16
arm: "+"
pooled_cpm: 20.73
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# EIF2B5

*eukaryotic translation initiation factor 2B subunit epsilon* — 3q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.91× (z +17.6, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.767× (z -5.2, q 1e-04, down in 20 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PUF60]] (+0.71, fdr 7e-06), [[ARFGAP2]] (+0.70, fdr 1e-05), [[SRRM2]] (+0.70, fdr 1e-05); moves opposite to [[RAP1A]] (-0.70, fdr 1e-05), [[COX6A1]] (-0.66, fdr 1e-05), [[SEC11A]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6961.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +17.6 | 0e+00 | 41/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.15×** | +14.8 | 0e+00 | 41/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.96×** | +12.5 | 2e-33 | 39/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.71×** | +10.4 | 5e-23 | 37/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.63×** | +9.4 | 4e-19 | 35/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +8.4 | 6e-15 | 27/46 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +8.3 | 6e-15 | 3/48 (A-427, BT-474, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +6.6 | 3e-09 | 29/47 (LS 180, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +6.0 | 1e-07 | 27/47 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +6.0 | 1e-07 | 20/47 (MIA PaCa-2, SW 900, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +5.7 | 6e-07 | 21/46 (MIA PaCa-2, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.34×** | +5.4 | 3e-06 | 17/33 (A549, HT-29, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +5.0 | 2e-05 | 22/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +4.9 | 4e-05 | 16/47 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.29×** | +4.9 | 4e-05 | 21/42 (HCT15, A-172, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +4.7 | 7e-05 | 19/47 (HEC-1-A, A-427, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.30×** | +4.7 | 1e-04 | 16/47 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.6 | 1e-04 | 16/48 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +4.3 | 4e-04 | 11/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.002 | 7/48 (MIA PaCa-2, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.032 | 8/44 (SW480, LS 180, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6961.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.767×** | -5.2 | 1e-04 | 20/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.775×** | -4.9 | 2e-04 | 20/48 (SK-MEL-2, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.829×** | -3.7 | 0.043 | 13/47 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.832×** | -3.6 | 0.043 | 12/48 (KATO III, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.833× | -3.6 | 0.043 | 13/48 (KATO III, AsPC-1, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | 0.740× | -3.1 | 0.21 | 8/48 (SW480, hTERT-HPNE, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6961. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 30.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +16.0) | — |
| [[A498 (line)]] | wt | 15.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 24.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.0) | — |
| [[SW480 (line)]] | alt | 25.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.6) | — |
| [[A-172 (line)]] | wt | 15.2 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.212× (z -9.7) |
| [[A-427 (line)]] | wt | 33.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -9.0) |
| [[AN3 CA (line)]] | alt | 25.1 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0807× (z -9.0) ⚠ cell-cycle shift, explains ~24% of this change |
| [[COLO 205 (line)]] | alt | 27.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +8.6) | — |
| [[H4 (line)]] | wt | 28.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 33.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 38.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 18.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 20.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 14.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +10.3) | — |
| [[A549 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6961), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUF60]] | +0.71 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[ARFGAP2]] | +0.70 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[SRRM2]] | +0.70 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[CHTOP]] | +0.69 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[BRPF3]] | +0.69 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[SRSF6]] | +0.68 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[SRCAP]] | +0.68 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[AKT1S1]] | +0.68 | +0.78 / +0.36 | both halves | 1e-04 |  |
| [[KICS2]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[MEPCE]] | +0.67 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[ZXDB]] | +0.67 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[MED12]] | +0.67 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAP1A]] | -0.70 | -0.75 / -0.55 | both halves | 1e-05 |  |
| [[COX6A1]] | -0.66 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[SEC11A]] | -0.66 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[UBTD1]] | -0.64 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[MOSPD3]] | -0.63 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[ARL3]] | -0.63 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[GMCL1]] | -0.63 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[SDHAP4-1]] | -0.62 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[IER3IP1]] | -0.62 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[PDZD7]] | -0.61 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[SNRPD2]] | -0.61 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[GNB2]] | -0.61 | -0.52 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises EIF2B5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZC3H12B]] | B | ZC3H12B activity raises EIF2B5's level | lines that do not express ZC3H12B (21) vs lines expressing it (29) | 1.23× lower at baseline in the lines without ZC3H12B | 0.029 | ⚠ within organs, on part of the lines; also absent: RUNX3, TMEM132D, LINC01876 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-10.4, 4.4); signed map (15.7, -22.8). **Vector** length 78.2, 14.1% of its response variance represented; |z| ≥ 3 in 858 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +14.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +17.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.2 | +12.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +9.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +2.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.8 | -5.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.8 | -4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -3.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.7 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.8 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | +1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 2B subunit epsilon |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:184,135,038-184,146,127 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EIF2Bepsilon, EIF-2B |
| Reactome | 4 pathways, smallest: Recycling of eIF2:GDP; Cap-dependent Translation Initiation; Eukaryotic Translation Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13144](https://www.uniprot.org/uniprotkb/Q13144) (Translation initiation factor eIF2B subunit epsilon):

> Acts as a component of the translation initiation factor 2B (eIF2B) complex, which catalyzes the exchange of GDP for GTP on eukaryotic initiation factor 2 (eIF2) gamma subunit. Its guanine nucleotide exchange factor activity is repressed when bound to eIF2 complex phosphorylated on the alpha subunit, thereby limiting the amount of methionyl-initiator methionine tRNA available to the ribosome and consequently global translation is repressed.

**Summary**, from NCBI Gene [8893](https://www.ncbi.nlm.nih.gov/gene/8893):

> This gene encodes one of five subunits of eukaryotic translation initiation factor 2B (EIF2B), a GTP exchange factor for eukaryotic initiation factor 2 and an essential regulator for protein synthesis. Mutations in this gene and the genes encoding other EIF2B subunits have been associated with leukoencephalopathy with vanishing white matter. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:3261](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3261) · Entrez [8893](https://www.ncbi.nlm.nih.gov/gene/8893) · UniProt [Q13144](https://www.uniprot.org/uniprotkb/Q13144) · Ensembl [ENSG00000145191](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145191)

## Data

Gene col 6961: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6961); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6961, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6961]; `tensor/DDL_lfc|DDL_z.npy` [6961]; `embed/gene_vectors.npy` [6961]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6961 or target_col == 6961). Every well: [[EIF2B5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF2B5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

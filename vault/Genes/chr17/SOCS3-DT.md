---
symbol: "SOCS3-DT"
type: "gene"
col: 15509
ensembl_id: "ENSG00000266970"
name: "SOCS3 divergent transcript"
location: "17q25.3"
module: 35
arm: "+"
pooled_cpm: 3.42
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# SOCS3-DT

*SOCS3 divergent transcript* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.84× (z +20.8, q 0e+00, up in 28 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.286× (z -8.9, q 2e-16, down in 32 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RELA-DT]] (+0.63, fdr 1e-05), [[PPEF1]] (+0.63, fdr 1e-05), [[CHKB-DT]] (+0.61, fdr 1e-05); moves opposite to [[RPGRIP1L]] (-0.49, fdr 7e-05), [[AGO1]] (-0.49, fdr 9e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15509.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.84×** | +20.8 | 0e+00 | 28/28 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.28×** | +8.3 | 2e-14 | 21/40 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.01×** | +7.6 | 6e-12 | 16/22 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.82×** | +7.1 | 1e-10 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +5.8 | 6e-07 | 18/30 (PANC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +5.2 | 2e-05 | 1/4 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.020 | 6/39 (HOP62, PANC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.42×** | +3.4 | 0.048 | 8/41 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +3.3 | 0.062 | 1/10 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +3.3 | 0.062 | 0/15 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.53× | +3.0 | 0.12 | 6/33 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | 1.53× | +3.0 | 0.12 | 5/35 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15509.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.286×** | -8.9 | 2e-16 | 32/41 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.558×** | -5.9 | 1e-06 | 26/38 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.453×** | -5.7 | 3e-06 | 19/41 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.463×** | -5.5 | 5e-06 | 22/38 (PANC-1, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.531×** | -4.5 | 5e-04 | 17/39 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.531×** | -4.5 | 5e-04 | 13/42 (C32, LOX-IMVI, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.533×** | -4.5 | 5e-04 | 19/37 (A-427, SHP-77, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.533×** | -4.5 | 5e-04 | 18/36 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.567×** | -4.1 | 0.003 | 15/34 (A549, NCI-H23, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.378×** | -3.6 | 0.016 | 9/26 (NCI-H460, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[crizotinib (drug)]] 5 µM |  | **0.597×** | -3.5 | 0.020 | 10/39 (SW 900, BT-474, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.399×** | -3.4 | 0.028 | 10/33 (NCI-H460, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.627×** | -3.3 | 0.036 | 10/40 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.633×** | -3.1 | 0.066 | 9/39 (H4, SK-MEL-2, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.735×** | -3.1 | 0.066 | 13/39 (C32, SHP-77, …) | rises with dose |  |
| [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | **0.647×** | -3.1 | 0.066 | 4/40 (LoVo, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15509. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.7 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +9.6) | [[Ixazomib citrate (drug)]] 5 µM 0.158× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 5.45 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +10.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0302× (z -11.1) |
| [[A-427 (line)]] | wt | 6.94 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0263× (z -14.0) |
| [[A498 (line)]] | wt | 1.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.9× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 6.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.85× (z +11.6) | — |
| [[HepG2_C3A (line)]] | wt | 4.34 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0311× (z -8.6) |
| [[HOP62 (line)]] | alt | 1.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.0× (z +12.6) | — |
| [[NCI-H1573 (line)]] | alt | 3.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 3.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.33× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 4.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.17× (z +10.3) | — |
| [[PANC-1 (line)]] | alt | 4.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.63× (z +13.2) | — |
| [[SW480 (line)]] | alt | 4.40 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.125× (z -9.9) |
| [[A-172 (line)]] | wt | 0.814 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.880 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.971 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.881 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.472 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.891 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15509), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RELA-DT]] | +0.63 | +0.58 / +0.54 | both halves | 1e-05 | same gene group |
| [[PPEF1]] | +0.63 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[CHKB-DT]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 | same gene group |
| [[PJVK]] | +0.60 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[DGUOK-AS1]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[SPEN-AS1]] | +0.60 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[TP53TG5]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CEACAM16-AS1]] | +0.60 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[DENND5B-AS1]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[UPK2]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[HEATR4]] | +0.59 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ITGB2]] | +0.59 | +0.47 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPGRIP1L]] | -0.49 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[AGO1]] | -0.49 | -0.36 / -0.52 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SOCS3-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[STAT4]] | B | STAT4 activity strengthens SOCS3-DT's drug response | lines that do not express STAT4 (7) vs lines expressing it (35) | the lines without STAT4 respond 1.07× as strongly (z diff -0.09); strongest at Doxorubicin (hydrochloride) 5 µM: 2.18x vs 3.97x (z diff +2.5) | 0.081 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ZPLD1, SMAD7; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (7.3, 27.5); signed map (35.5, -6.5). **Vector** length 64.8, 11.5% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +20.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Oxaprozin (drug)]] 0.5 µM |  | +1.7 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -5.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.5 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.5 | -8.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -5.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.1 | -5.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -1.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | SOCS3 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q25.3 — chr17:78,360,376-78,373,911 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52799) · Entrez [101928674](https://www.ncbi.nlm.nih.gov/gene/101928674) · Ensembl [ENSG00000266970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000266970)

## Data

Gene col 15509: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15509); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15509, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15509]; `tensor/DDL_lfc|DDL_z.npy` [15509]; `embed/gene_vectors.npy` [15509]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15509 or target_col == 15509). Every well: [[SOCS3-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOCS3-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

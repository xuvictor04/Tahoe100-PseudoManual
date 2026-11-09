---
symbol: "DENND6B"
type: "gene"
col: 12993
ensembl_id: "ENSG00000205593"
name: "DENN domain containing 6B"
location: "22q13.33"
module: 3
arm: "+"
pooled_cpm: 7.92
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 25
n_dd_up_clean: 1
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# DENND6B

*DENN domain containing 6B* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.62× (z +3.8, q 0.088, up in 9 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.463× (z -8.5, q 2e-14, down in 33 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIRT2]] (+0.71, fdr 1e-05), [[LIN7B]] (+0.70, fdr 7e-06), [[VPS37D]] (+0.69, fdr 7e-06); moves opposite to [[PSME3]] (-0.70, fdr 7e-06), [[DARS2]] (-0.66, fdr 1e-05), [[M6PR]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12993.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +3.8 | 0.088 | 9/35 (A549, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.6 | 0.099 | 15/34 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.24× | +3.3 | 0.13 | 4/45 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.35× | +3.3 | 0.13 | 13/44 (NCI-H1792, A498, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.51× | +3.3 | 0.13 | 8/41 (SW480, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.34× | +3.2 | 0.13 | 9/46 (A498, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12993.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.463×** | -8.5 | 2e-14 | 33/46 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.645×** | -6.8 | 2e-09 | 23/37 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.539×** | -6.8 | 2e-09 | 29/44 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.558×** | -6.4 | 2e-08 | 28/46 (SW1417, Hs 766T, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.355×** | -5.9 | 3e-07 | 23/43 (PANC-1, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.593×** | -5.7 | 9e-07 | 24/46 (NCI-H1573, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.591×** | -5.4 | 4e-06 | 19/42 (Hs 766T, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.612×** | -5.4 | 5e-06 | 22/44 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.708×** | -5.3 | 6e-06 | 20/40 (HOP62, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.620×** | -5.2 | 8e-06 | 18/44 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.621×** | -5.2 | 8e-06 | 21/44 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.612×** | -5.2 | 1e-05 | 19/31 (LoVo, HS-578T, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.415×** | -5.0 | 2e-05 | 23/42 (HS-578T, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.636×** | -5.0 | 3e-05 | 22/42 (LS 180, C32, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.662×** | -4.5 | 2e-04 | 20/44 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.679×** | -4.2 | 8e-04 | 15/46 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[EX229 (drug)]] 5 µM |  | **0.480×** | -4.2 | 8e-04 | 17/38 (NCI-H1573, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.577×** | -3.2 | 0.043 | 5/38 (A498, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12993. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 13.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -13.6) |
| [[LoVo (line)]] | wt | 15.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 10.8 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0722× (z -13.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.308× (z -8.8) |
| [[A498 (line)]] | wt | 6.64 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -10.5) |
| [[HS-578T (line)]] | alt | 8.29 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0885× (z -9.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 12.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -12.6) |
| [[LS 180 (line)]] | wt | 6.50 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0992× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 19.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 7.35 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0998× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~11% of this change |
| [[NCI-H23 (line)]] | alt | 8.89 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.107× (z -9.3) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 4.38 | 0 | 1 | — | [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM 0.0618× (z -8.8) |
| [[A-427 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.811 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12993), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT2]] | +0.71 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[LIN7B]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[VPS37D]] | +0.69 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[CDKN2D]] | +0.67 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[WIPF2]] | +0.65 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[KBTBD3]] | +0.65 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[RNF114]] | +0.65 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[FAM193B]] | +0.65 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[ARID3A]] | +0.64 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[MALSU1]] | +0.64 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[SEC22A]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[CAMSAP3]] | +0.63 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.70 | -0.59 / -0.69 | both halves | 7e-06 |  |
| [[DARS2]] | -0.66 | -0.56 / -0.67 | both halves | 1e-05 |  |
| [[M6PR]] | -0.63 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[PTPN11]] | -0.62 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[ABCF2]] | -0.62 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[MOB1A]] | -0.62 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[EIF4G1]] | -0.62 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[XRCC5]] | -0.62 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[TRIP12]] | -0.60 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[HCFC1]] | -0.60 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[TMX3]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[CCT7]] | -0.59 | -0.51 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DENND6B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.609). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-21.9, -29.6); signed map (-28.4, 12.1). **Vector** length 68.6, 11.7% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +3.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.6 | +3.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.5 | +3.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -5.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.6 | -3.8 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | DENN domain containing 6B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,309,030-50,327,012 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33692, AFI1B; previously FAM116B |
| Gene groups (HGNC) | DENN domain containing |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEG7](https://www.uniprot.org/uniprotkb/Q8NEG7) (Protein DENND6B):

> Guanine nucleotide exchange factor (GEF) for RAB14. Also has some, lesser GEF activity towards RAB35.

**Summary**, from NCBI Gene [414918](https://www.ncbi.nlm.nih.gov/gene/414918):

> Enables guanyl-nucleotide exchange factor activity. Predicted to be located in cytosol. Predicted to be active in recycling endosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:32690](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32690) · Entrez [414918](https://www.ncbi.nlm.nih.gov/gene/414918) · UniProt [Q8NEG7](https://www.uniprot.org/uniprotkb/Q8NEG7) · Ensembl [ENSG00000205593](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205593)

## Data

Gene col 12993: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12993); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12993, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12993]; `tensor/DDL_lfc|DDL_z.npy` [12993]; `embed/gene_vectors.npy` [12993]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12993 or target_col == 12993). Every well: [[DENND6B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENND6B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "FITM2"
type: "gene"
col: 12375
ensembl_id: "ENSG00000197296"
name: "fat storage inducing transmembrane protein 2"
location: "20q13.12"
module: 17
arm: "+"
pooled_cpm: 6.8
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 13
n_dd_up_clean: 13
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# FITM2

*fat storage inducing transmembrane protein 2* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.09× (z +11.3, q 8e-27, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.662× (z -8.9, q 2e-16, down in 26 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COMMD2]] (+0.66, fdr 1e-05), [[ZNF30]] (+0.63, fdr 4e-05), [[HEATR6]] (+0.62, fdr 1e-05); moves opposite to [[PPP1R15B-AS1]] (-0.73, fdr 8e-06), [[HIVEP2-DT]] (-0.61, fdr 1e-05), [[ZHX2]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF420]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12375.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.09×** | +11.3 | 8e-27 | 39/47 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.09×** | +10.2 | 7e-22 | 33/47 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.93×** | +10.1 | 1e-21 | 35/47 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +7.8 | 8e-13 | 18/32 (KATO III, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +7.4 | 2e-11 | 21/47 (BT-474, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +5.8 | 7e-07 | 15/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +5.4 | 5e-06 | 11/42 (HT-29, BT-474, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.95×** | +5.3 | 7e-06 | 10/46 (BT-474, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +5.2 | 1e-05 | 6/46 (COLO 205, SW480, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.9 | 6e-05 | 4/48 (NCI-H23, A-427, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +4.1 | 0.002 | 5/48 (AN3 CA, PANC-1, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.004 | 9/48 (A498, COLO 205, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.006 | 10/46 (SW1417, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.084 | 2/46 (SW480, HOP62) | inconsistent across doses |  |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.24×** | +3.0 | 0.090 | 5/39 (A-172, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12375.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.662×** | -8.9 | 2e-16 | 26/45 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.704×** | -5.4 | 2e-05 | 20/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.704×** | -5.2 | 4e-05 | 16/38 (BT-474, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.705×** | -4.9 | 2e-04 | 13/47 (HOP62, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -4.8 | 2e-04 | 16/42 (BT-474, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.562×** | -4.6 | 4e-04 | 14/40 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.580×** | -4.4 | 9e-04 | 13/47 (Hs 766T, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.745×** | -4.4 | 9e-04 | 16/44 (A549, SNU-423, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.762×** | -4.2 | 0.002 | 10/46 (NCI-H1573, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -3.7 | 0.011 | 20/43 (Hs 766T, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.769×** | -3.6 | 0.014 | 10/46 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.726×** | -3.5 | 0.020 | 2/47 (SW48, PANC-1) | two highest doses | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.852× | -3.5 | 0.020 | 7/48 (SW1417, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.802×** | -3.4 | 0.027 | 9/47 (AN3 CA, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Atazanavir (sulfate) (drug)]] 0.05 µM |  | **0.820×** | -3.1 | 0.084 | 6/47 (NCI-H661, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12375. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 25.2 | 4 (2 ⚠) | 3 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 3.36× (z +9.6) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0533× (z -16.0) |
| [[PANC-1 (line)]] | alt | 8.34 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -14.4) |
| [[C32 (line)]] | wt | 11.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -11.0) |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.287× (z -8.6) |
| [[A498 (line)]] | wt | 4.55 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 3.43 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0696× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 6.61 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.141× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 3.82 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0688× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 7.26 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.167× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 6.36 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -13.4) |
| [[RKO (line)]] | wt | 6.01 | 0 | 1 | — | [[Finasteride (drug)]] 0.05 µM 0.0717× (z -8.8) |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0734× (z -8.9) |
| [[SNU-423 (line)]] | alt | 5.74 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0789× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12375), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD2]] | +0.66 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ZNF30]] | +0.63 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[HEATR6]] | +0.62 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ACTR5]] | +0.62 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[WRAP73]] | +0.61 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[ZNF559]] | +0.60 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[TRIM32]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ZNF445]] | +0.60 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[C17orf58]] | +0.60 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[KBTBD6]] | +0.60 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[SDHAF3]] | +0.57 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[MOCS1]] | +0.57 | +0.34 / +0.50 | both halves | 1e-04 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R15B-AS1]] | -0.73 | -0.66 / -0.58 | both halves | 8e-06 |  |
| [[HIVEP2-DT]] | -0.61 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ZHX2]] | -0.61 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[LINC02955]] | -0.59 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[HCG17]] | -0.58 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[LINC00393]] | -0.58 | -0.56 / -0.22 | both halves | 6e-04 |  |
| [[SIAH2-AS1]] | -0.57 | -0.49 / -0.24 | both halves | 4e-04 |  |
| [[THUMPD3-AS1]] | -0.57 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[FAM151B]] | -0.57 | -0.46 / -0.29 | both halves | 2e-04 |  |
| [[CIBAR1-DT]] | -0.56 | -0.46 / -0.25 | both halves | 4e-04 |  |
| [[IRF3]] | -0.56 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[BCL10-AS1]] | -0.56 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF420]] | B | ZNF420 activity raises FITM2's level | lines that do not express ZNF420 (7) vs lines expressing it (43) | 1.35× lower at baseline in the lines without ZNF420 | 0.076 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF850, ZNF540 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.572). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-27.8, -3.7); signed map (-24.5, -15.2). **Vector** length 58.3, 7.78% of its response variance represented; |z| ≥ 3 in 960 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +2.6 | +10.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +1.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.1 | +2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.1 | +3.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.1 | +10.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +5.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +4.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.3 | +0.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | -3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.4 | -8.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.0 | -0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.0 | -4.4 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | -0.9 | -1.0 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | fat storage inducing transmembrane protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:44,302,840-44,311,202 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ881L22.2, FIT2; previously C20orf142 |
| Gene groups (HGNC) | Fat storage inducing transmembrane protein family |
| Reactome | 1 pathways, smallest: Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N6M3](https://www.uniprot.org/uniprotkb/Q8N6M3) (Acyl-coenzyme A diphosphatase FITM2):

> Fatty acyl-coenzyme A (CoA) diphosphatase that hydrolyzes fatty acyl-CoA to yield acyl-4'-phosphopantetheine and adenosine 3',5'-bisphosphate (By similarity). Preferentially hydrolyzes unsaturated long-chain acyl-CoA substrates such as oleoyl-CoA/(9Z)-octadecenoyl-CoA and arachidonoyl-CoA/(5Z,8Z,11Z,14Z)-eicosatetraenoyl-CoA in the endoplasmic reticulum (ER) lumen (By similarity). This catalytic activity is required for maintaining ER structure and for lipid droplets (LDs) biogenesis, which are …

**Summary**, from NCBI Gene [128486](https://www.ncbi.nlm.nih.gov/gene/128486):

> Enables coenzyme A diphosphatase activity. Involved in fatty-acyl-CoA catabolic process; lipid droplet formation; and lipid homeostasis. Predicted to be active in endoplasmic reticulum membrane. Implicated in Siddiqi syndrome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16135](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16135) · Entrez [128486](https://www.ncbi.nlm.nih.gov/gene/128486) · UniProt [Q8N6M3](https://www.uniprot.org/uniprotkb/Q8N6M3) · Ensembl [ENSG00000197296](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197296)

## Data

Gene col 12375: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12375); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12375, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12375]; `tensor/DDL_lfc|DDL_z.npy` [12375]; `embed/gene_vectors.npy` [12375]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12375 or target_col == 12375). Every well: [[FITM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FITM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "ALG12"
type: "gene"
col: 11334
ensembl_id: "ENSG00000182858"
name: "ALG12 alpha-1,6-mannosyltransferase"
location: "22q13.33"
module: 12
arm: "+"
pooled_cpm: 7.17
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# ALG12

*ALG12 alpha-1,6-mannosyltransferase* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.07× (z +16.9, q 0e+00, up in 29 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.733× (z -5.6, q 1e-05, down in 14 of 47 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.751× (z -5.2, q 4e-05, down in 6 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF213]] (+0.66, fdr 3e-05), [[DXO]] (+0.65, fdr 4e-05), [[CYB561]] (+0.62, fdr 1e-04); moves opposite to [[PRIM2]] (-0.55, fdr 4e-05), [[SPATA5]] (-0.53, fdr 2e-05), [[SRPK2]] (-0.52, fdr 4e-04).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BMP6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11334.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +16.9 | 0e+00 | 29/40 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +7.2 | 2e-10 | 17/41 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +5.8 | 2e-06 | 14/38 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.27×** | +4.0 | 0.010 | 4/23 (HEC-1-A, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.027 | 3/44 (HOP62, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.034 | 4/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11334.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.733×** | -5.6 | 1e-05 | 14/47 (HS-578T, HCT15, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.743×** | -5.4 | 2e-05 | 10/47 (AN3 CA, A-172, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.751×** | -5.2 | 4e-05 | 6/47 (NCI-H661, HOP62, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.782×** | -4.4 | 0.001 | 10/47 (HS-578T, NCI-H2030, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.785×** | -4.2 | 0.003 | 10/34 (LOX-IMVI, SNU-423, …) | top dose only |  |
| [[Trimetrexate (drug)]] 0.05 µM |  | **0.807×** | -3.9 | 0.009 | 10/44 (CFPAC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.805×** | -3.8 | 0.012 | 7/48 (SK-MEL-2, C32, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.854× | -3.8 | 0.012 | 14/48 (HOP62, SNU-423, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.805×** | -3.7 | 0.013 | 8/46 (LOX-IMVI, C-33 A, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.845× | -3.6 | 0.016 | 7/47 (NCI-H2347, SW48, …) | top dose only |  |
| [[Procainamide (hydrochloride) (drug)]] 5 µM |  | **0.813×** | -3.6 | 0.016 | 5/45 (AN3 CA, hTERT-HPNE, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.816×** | -3.5 | 0.019 | 10/40 (BT-474, HOP62, …) | top dose only |  |
| [[Allantoin (drug)]] 5 µM |  | 0.868× | -3.5 | 0.021 | 3/48 (HT-29, KATO III, …) | rises with dose | position effect removed |
| [[Sunitinib (drug)]] 0.5 µM |  | **0.826×** | -3.5 | 0.022 | 7/44 (CFPAC-1, A-427, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **0.829×** | -3.4 | 0.025 | 13/32 (LS 180, C32, …) | inconsistent across doses | composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.824×** | -3.4 | 0.027 | 6/44 (A498, hTERT-HPNE, …) | top dose only |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | 0.840× | -3.2 | 0.051 | 12/44 (SNU-1, NCI-H460, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.718×** | -3.1 | 0.051 | 3/47 (NCI-H1792, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Busulfan (drug)]] 5 µM |  | 0.876× | -2.9 | 0.096 | 8/47 (NCI-H1792, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11334. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 6.72 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +12.2) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.322× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 5.93 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 7.57 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -10.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 9.55 | 0 | 1 | — | [[LJI308 (drug)]] 0.05 µM 0.0854× (z -8.6) |
| [[Hs 766T (line)]] | wt | 7.23 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.128× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 6.50 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0733× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 4.09 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0641× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 13.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +13.7) | — |
| [[SNU-423 (line)]] | alt | 8.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11334), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF213]] | +0.66 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[DXO]] | +0.65 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[CYB561]] | +0.62 | +0.67 / +0.36 | both halves | 1e-04 |  |
| [[BRPF3]] | +0.61 | +0.67 / +0.31 | both halves | 2e-04 |  |
| [[CIDECP1]] | +0.60 | +0.75 / +0.45 | both halves | 3e-05 |  |
| [[ARFGAP2]] | +0.59 | +0.64 / +0.36 | both halves | 1e-04 | pathway: Asparagine N-linked glycosylation |
| [[ATG4D]] | +0.59 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[SLC35B1]] | +0.58 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[AMZ2P1-1]] | +0.58 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[CLK4]] | +0.57 | +0.59 / +0.36 | both halves | 9e-05 |  |
| [[C19orf54]] | +0.57 | +0.60 / +0.39 | both halves | 6e-05 |  |
| [[CNOT3]] | +0.57 | +0.65 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRIM2]] | -0.55 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[SPATA5]] | -0.53 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[SRPK2]] | -0.52 | -0.58 / -0.25 | both halves | 4e-04 |  |
| [[RASA2]] | -0.52 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[BMP6]] | -0.52 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[LYPLA1]] | -0.51 | -0.58 / -0.32 | both halves | 1e-04 |  |
| [[DOCK9]] | -0.51 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[INPP4A]] | -0.51 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[NLK]] | -0.51 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[NHP2]] | -0.50 | -0.54 / -0.21 | both halves | 6e-04 |  |
| [[RNGTT]] | -0.50 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[CAP1]] | -0.50 | -0.48 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMP6]] | B | BMP6 activity lowers ALG12's level | lines that do not express BMP6 (23) vs lines expressing it (27) | 1.17× higher at baseline in the lines without BMP6 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000289418, LRRN2, LINC02864 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.400). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-12.1, 5.8); signed map (11.9, -19.4). **Vector** length 48.6, 5.54% of its response variance represented; |z| ≥ 3 in 814 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +16.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.6 | +7.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +2.6 | +0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +1.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.1 | +2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.1 | +1.5 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -1.5 | -5.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | -1.4 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -3.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ALG12 alpha-1,6-mannosyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:49,900,229-49,918,438 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ECM39, CDG1G |
| Gene groups (HGNC) | Dolichyl D-mannosyl phosphate dependent mannosyltransferases |
| Reactome | 5 pathways, smallest: Diseases associated with N-glycosylation of proteins; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein; Diseases of glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BV10](https://www.uniprot.org/uniprotkb/Q9BV10) (Dol-P-Man:Man(7)GlcNAc(2)-PP-Dol alpha-1,6-mannosyltransferase):

> Mannosyltransferase that operates in the biosynthetic pathway of dolichol-linked oligosaccharides, the glycan precursors employed in protein asparagine (N)-glycosylation. The assembly of dolichol-linked oligosaccharides begins on the cytosolic side of the endoplasmic reticulum membrane and finishes in its lumen. The sequential addition of sugars to dolichol pyrophosphate produces dolichol-linked oligosaccharides containing fourteen sugars, including two GlcNAcs, nine mannoses and three …

**Summary**, from NCBI Gene [79087](https://www.ncbi.nlm.nih.gov/gene/79087):

> This gene encodes a member of the glycosyltransferase 22 family. The encoded protein catalyzes the addition of the eighth mannose residue in an alpha-1,6 linkage onto the dolichol-PP-oligosaccharide precursor (dolichol-PP-Man(7)GlcNAc(2)) required for protein glycosylation. Mutations in this gene have been associated with congenital disorder of glycosylation type Ig (CDG-Ig)characterized by abnormal N-glycosylation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19358](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19358) · Entrez [79087](https://www.ncbi.nlm.nih.gov/gene/79087) · UniProt [Q9BV10](https://www.uniprot.org/uniprotkb/Q9BV10) · Ensembl [ENSG00000182858](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182858)

## Data

Gene col 11334: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11334); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11334, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11334]; `tensor/DDL_lfc|DDL_z.npy` [11334]; `embed/gene_vectors.npy` [11334]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11334 or target_col == 11334). Every well: [[ALG12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALG12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

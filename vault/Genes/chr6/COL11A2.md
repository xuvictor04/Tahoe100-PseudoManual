---
symbol: "COL11A2"
type: "gene"
col: 12836
ensembl_id: "ENSG00000204248"
name: "collagen type XI alpha 2 chain"
location: "6p21.32"
module: 181
arm: "+"
pooled_cpm: 4.09
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# COL11A2

*collagen type XI alpha 2 chain* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.30× (z +21.6, q 0e+00, up in 35 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.573× (z -4.3, q 0.011, down in 15 of 43 measured lines) ⚠ unreliable plate only.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NLGN3]] (+0.77, fdr 7e-06), [[DNAH12]] (+0.74, fdr 9e-06), [[CFAP53]] (+0.73, fdr 7e-06); moves opposite to [[CPSF4]] (-0.62, fdr 6e-05), [[RPE]] (-0.61, fdr 9e-06), [[MTERF3]] (-0.61, fdr 3e-05).
> It is in [[Module 181]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12836.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.30×** | +21.6 | 0e+00 | 35/36 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.00×** | +15.1 | 0e+00 | 34/35 (SW480, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.91×** | +12.2 | 5e-32 | 34/35 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.50×** | +11.1 | 1e-26 | 32/42 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.13×** | +8.4 | 4e-15 | 12/19 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +7.2 | 6e-11 | 3/4 (HEC-1-A, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +6.9 | 3e-10 | 3/8 (HEC-1-A, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.28×** | +6.6 | 4e-09 | 24/44 (NCI-H23, HEC-1-A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +5.2 | 1e-05 | 16/44 (HOP62, BT-474, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +4.8 | 8e-05 | 7/15 (C32, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +4.3 | 7e-04 | 11/34 (HS-578T, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +3.8 | 0.006 | 6/29 (A498, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +3.7 | 0.010 | 12/43 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.57×** | +3.5 | 0.022 | 9/42 (A498, HEC-1-A, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +3.4 | 0.025 | 6/37 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.57×** | +3.3 | 0.030 | 14/38 (SK-MEL-2, C32, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.031 | 5/42 (A498, RKO, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +3.2 | 0.037 | 5/43 (BT-474, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.49×** | +3.0 | 0.071 | 6/41 (SW48, A-172, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +3.0 | 0.090 | 5/40 (LoVo, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12836.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.573×** | -4.3 | 0.011 | 15/43 (NCI-H2030, HT-29, …) | inconsistent across doses |  |
| [[Adenine (drug)]] 5 µM |  | 0.750× | -3.1 | 0.42 | 7/44 (SW 1088, NCI-H1792, …) | top dose only | position effect removed |
| [[Relugolix (drug)]] 0.5 µM |  | 0.671× | -3.1 | 0.42 | 6/42 (PANC-1, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12836. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.88× (z +9.1) | — |
| [[A549 (line)]] | wt | 2.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 2.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 67.2× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 2.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 3.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +11.2) | — |
| [[LoVo (line)]] | wt | 5.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.46× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 4.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.25× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 6.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.64× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 20.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 1.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 1.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 1.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 7.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.32× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 2.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 1.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.8× (z +8.8) | — |
| [[A-427 (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.990 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.935 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12836), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NLGN3]] | +0.77 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.74 | +0.81 / +0.57 | both halves | 9e-06 |  |
| [[CFAP53]] | +0.73 | +0.81 / +0.60 | both halves | 7e-06 |  |
| [[IL34]] | +0.73 | +0.80 / +0.54 | both halves | 1e-05 |  |
| [[CCNP]] | +0.73 | +0.81 / +0.63 | both halves | 7e-06 |  |
| [[KCNN1]] | +0.73 | +0.84 / +0.63 | both halves | 7e-06 |  |
| [[TGIF2-RAB5IF]] | +0.72 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[PIWIL2]] | +0.72 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[NEK8]] | +0.69 | +0.79 / +0.42 | both halves | 4e-05 |  |
| [[PLA2G6]] | +0.69 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[LINC03048]] | +0.69 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[AGER]] | +0.68 | +0.65 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF4]] | -0.62 | -0.69 / -0.38 | both halves | 6e-05 |  |
| [[RPE]] | -0.61 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[MTERF3]] | -0.61 | -0.62 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers COL11A2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.861). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.0, -7.1); signed map (23.5, 6.8). **Vector** length 71.3, 11.8% of its response variance represented; |z| ≥ 3 in 1,118 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.0 | +21.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +15.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +6.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +0.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +0.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -4.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.7 | -3.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | collagen type XI alpha 2 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:33,162,681-33,192,499 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HKE5; previously DFNA13, DFNB53 |
| Gene groups (HGNC) | Fibrillar collagens |
| Reactome | 17 pathways, smallest: Developmental Lineage of Pancreatic Ductal Cells; Developmental Lineage of Pancreatic Endocrine Mid Progenitor Cells; Developmental Cell Lineages of the Endocrine Pancreas |
| Matched by | ensembl_id |

**Function**, from UniProt [P13942](https://www.uniprot.org/uniprotkb/P13942) (Collagen alpha-2(XI) chain):

> May play an important role in fibrillogenesis by controlling lateral growth of collagen II fibrils.

**Summary**, from NCBI Gene [1302](https://www.ncbi.nlm.nih.gov/gene/1302):

> This gene encodes one of the two alpha chains of type XI collagen, a minor fibrillar collagen. It is located on chromosome 6 very close to but separate from the gene for retinoid X receptor beta. Type XI collagen is a heterotrimer but the third alpha chain is a post-translationally modified alpha 1 type II chain. Proteolytic processing of this type XI chain produces PARP, a proline/arginine-rich protein that is an amino terminal domain. Mutations in this gene are associated with type III …

**Accessions** — [HGNC:2187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2187) · Entrez [1302](https://www.ncbi.nlm.nih.gov/gene/1302) · UniProt [P13942](https://www.uniprot.org/uniprotkb/P13942) · Ensembl [ENSG00000204248](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204248)

## Data

Gene col 12836: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12836); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12836, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12836]; `tensor/DDL_lfc|DDL_z.npy` [12836]; `embed/gene_vectors.npy` [12836]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12836 or target_col == 12836). Every well: [[COL11A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL11A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

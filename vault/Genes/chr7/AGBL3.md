---
symbol: "AGBL3"
type: "gene"
col: 7127
ensembl_id: "ENSG00000146856"
name: "AGBL carboxypeptidase 3"
location: "7q33"
module: 23
arm: "+"
pooled_cpm: 6.81
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 6
n_dd_up_clean: 29
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# AGBL3

*AGBL carboxypeptidase 3* — 7q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.18× (z +14.4, q 3e-44, up in 36 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.659× (z -5.5, q 2e-05, down in 19 of 46 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSH4]] (+0.74, fdr 7e-06), [[BAAT]] (+0.72, fdr 1e-05), [[NEB]] (+0.70, fdr 1e-05); moves opposite to [[STUB1]] (-0.57, fdr 0.003, ⚠ not reproduced).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7127.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +14.4 | 3e-44 | 36/43 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.04×** | +13.1 | 5e-37 | 34/48 (A498, A549, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +11.5 | 2e-28 | 34/46 (A498, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.49×** | +11.4 | 4e-28 | 29/33 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +10.6 | 5e-24 | 26/42 (C32, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +9.3 | 9e-19 | 12/19 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +8.7 | 4e-16 | 11/16 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +7.9 | 2e-13 | 23/47 (NCI-H2030, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +7.0 | 2e-10 | 22/40 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +6.8 | 8e-10 | 21/45 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +6.6 | 3e-09 | 21/45 (A-172, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +6.5 | 4e-09 | 17/47 (C32, BT-474, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.64×** | +6.5 | 4e-09 | 19/48 (SW480, hTERT-HPNE, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +6.3 | 1e-08 | 16/41 (HS-578T, A498, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +5.8 | 2e-07 | 18/45 (A498, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.8 | 3e-07 | 13/45 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +5.6 | 8e-07 | 14/47 (A498, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +5.4 | 2e-06 | 14/47 (BT-474, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7127.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.659×** | -5.5 | 2e-05 | 19/46 (LOX-IMVI, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.674×** | -5.2 | 6e-05 | 15/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.491×** | -4.9 | 2e-04 | 11/46 (C-33 A, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.556×** | -4.0 | 0.006 | 14/42 (C-33 A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.556×** | -4.0 | 0.006 | 6/39 (C32, A498, …) | top dose only | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.758×** | -3.5 | 0.053 | 4/45 (NCI-H23, C32, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Methotrexate (drug)]] 0.5 µM |  | 0.783× | -3.2 | 0.10 | 7/45 (CFPAC-1, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7127. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 11.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +12.4) | — |
| [[C32 (line)]] | wt | 15.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +14.1) | — |
| [[RPMI-7951 (line)]] | alt | 7.43 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +9.0) | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.0880× (z -8.8) |
| [[HS-578T (line)]] | alt | 5.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.95× (z +9.8) | — |
| [[KATO III (line)]] | alt | 4.92 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0776× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 14.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0371× (z -12.2) |
| [[LS 180 (line)]] | wt | 4.00 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0781× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 7.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.75× (z +11.8) | — |
| [[NCI-H2347 (line)]] | alt | 3.18 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.107× (z -9.1) |
| [[PANC-1 (line)]] | alt | 4.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +9.0) | — |
| [[SW480 (line)]] | alt | 8.07 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.19× (z +8.6) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7127), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSH4]] | +0.74 | +0.78 / +0.61 | both halves | 7e-06 |  |
| [[BAAT]] | +0.72 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[NEB]] | +0.70 | +0.77 / +0.51 | both halves | 1e-05 |  |
| [[PKD1L1]] | +0.69 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[LRRC37A3]] | +0.69 | +0.77 / +0.41 | both halves | 4e-05 |  |
| [[AMY2B]] | +0.67 | +0.75 / +0.45 | both halves | 3e-05 |  |
| [[LINC00486]] | +0.67 | +0.74 / +0.42 | both halves | 4e-05 |  |
| [[ANKDD1B]] | +0.66 | +0.73 / +0.42 | both halves | 4e-05 |  |
| [[N4BP2L1]] | +0.65 | +0.71 / +0.39 | both halves | 5e-05 |  |
| [[C2orf88]] | +0.65 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[ST8SIA5]] | +0.65 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[RFX3-DT]] | +0.64 | +0.73 / +0.26 | both halves | 4e-04 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STUB1]] | -0.57 | -0.47 / -0.09 | ⚠ not reproduced | 0.003 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AGBL3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (29.6, -10.7); signed map (18.1, 2.7). **Vector** length 65.8, 10.1% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.4 | +13.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +11.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +7.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +4.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +6.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.4 | +4.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.2 | +5.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.6 | +6.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.2 | +3.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -1.8 | -4.0 |
|  | [[Quinestrol (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.4 | -3.5 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | AGBL carboxypeptidase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q33 — chr7:134,986,508-135,147,963 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC32955, CCP3 |
| Gene groups (HGNC) | M14 carboxypeptidases |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEM8](https://www.uniprot.org/uniprotkb/Q8NEM8) (Cytosolic carboxypeptidase 3):

> Metallocarboxypeptidase that mediates deglutamylation of tubulin and non-tubulin target proteins. Catalyzes the removal of polyglutamate side chains present on the gamma-carboxyl group of glutamate residues within the C-terminal tail of tubulin protein. Specifically cleaves tubulin long-side-chains, while it is not able to remove the branching point glutamate. Also catalyzes the removal of polyglutamate residues from the carboxy-terminus of non-tubulin proteins such as MYLK. May catalyze the …

**Summary**, from NCBI Gene [340351](https://www.ncbi.nlm.nih.gov/gene/340351):

> Enables metallocarboxypeptidase activity. Involved in protein side chain deglutamylation. Predicted to be located in cytosol. Predicted to be active in centriole and cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27981](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27981) · Entrez [340351](https://www.ncbi.nlm.nih.gov/gene/340351) · UniProt [Q8NEM8](https://www.uniprot.org/uniprotkb/Q8NEM8) · Ensembl [ENSG00000146856](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146856)

## Data

Gene col 7127: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7127); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7127, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7127]; `tensor/DDL_lfc|DDL_z.npy` [7127]; `embed/gene_vectors.npy` [7127]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7127 or target_col == 7127). Every well: [[AGBL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGBL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

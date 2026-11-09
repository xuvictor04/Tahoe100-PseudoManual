---
symbol: "CCZ1P1"
type: "gene"
col: 14364
ensembl_id: "ENSG00000243554"
name: "CCZ1 pseudogene 1"
location: "7q21.3"
module: 15
arm: "+"
pooled_cpm: 10.16
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# CCZ1P1

*CCZ1 pseudogene 1* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.63× (z +5.6, q 1e-05, up in 21 of 40 measured lines) ⚠ toxic. The strongest without an alert is [[Neratinib (maleate) (drug)]] 0.5 µM: 1.34× (z +3.5, q 0.073, up in 14 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.653× (z -7.2, q 3e-10, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF500]] (+0.64, fdr 1e-05), [[GAS5]] (+0.63, fdr 7e-06), [[TAF11]] (+0.63, fdr 1e-05); moves opposite to [[TMEM107]] (-0.55, fdr 2e-05), [[MAPRE1]] (-0.55, fdr 1e-05), [[POLR2E]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC03046]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14364.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +5.6 | 1e-05 | 21/40 (RPMI-7951, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +4.0 | 0.022 | 11/26 (SW 900, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.073 | 14/44 (HCT15, H4, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.53×** | +3.5 | 0.073 | 7/42 (A498, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.080 | 7/45 (CFPAC-1, LoVo, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.30× | +3.1 | 0.16 | 10/43 (COLO 205, LOX-IMVI, …) | top dose only |  |
| [[Resveratrol (drug)]] 5 µM |  | 1.20× | +3.1 | 0.16 | 4/48 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14364.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.653×** | -7.2 | 3e-10 | 30/46 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.628×** | -5.6 | 7e-06 | 22/47 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.673×** | -4.8 | 4e-04 | 21/47 (SW480, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.672×** | -4.6 | 6e-04 | 22/46 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.484×** | -4.6 | 6e-04 | 16/47 (AsPC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.738×** | -3.6 | 0.025 | 13/47 (HepG2/C3A, A-172, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.762×** | -3.3 | 0.087 | 15/47 (H4, J82, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.606× | -3.1 | 0.11 | 12/44 (LoVo, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.759× | -3.1 | 0.11 | 13/47 (BT-474, C-33 A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.772× | -3.1 | 0.11 | 14/46 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Gefitinib (drug)]] 5 µM |  | 0.776× | -3.0 | 0.12 | 3/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14364. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 9.68 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.3) |
| [[BT-474 (line)]] | alt | 7.72 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0936× (z -9.1) |
| [[LoVo (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0701× (z -8.7) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 8.95 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.6) |
| [[SNU-1 (line)]] | wt | 14.1 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0945× (z -8.6) ⚠ toxic |
| [[SW48 (line)]] | wt | 15.0 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0713× (z -9.2) |
| [[A-427 (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14364), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF500]] | +0.64 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[GAS5]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[TAF11]] | +0.63 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[PHYKPL]] | +0.63 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[PGLS-DT]] | +0.62 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[MED10]] | +0.62 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[TMEM267]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[SNHG25]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[EPB41L4A-AS1]] | +0.60 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[NSUN5P2-1]] ⚠ | +0.59 | +0.51 / +0.60 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MORN4]] | +0.59 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[ADPRM]] | +0.59 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[SHARPIN]] | +0.58 | +0.57 / +0.66 | both halves | 9e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM107]] | -0.55 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[MAPRE1]] | -0.55 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[POLR2E]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[PKM]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[AP2M1]] | -0.54 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[CBX5]] | -0.54 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[HASPIN]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[AKAP11]] | -0.52 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[H2AX]] | -0.52 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[MYBL1]] | -0.51 | -0.40 / -0.52 | both halves | 4e-05 |  |
| [[RAB1B]] | -0.51 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[YWHAZ]] | -0.50 | -0.42 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC03046]] | B | LINC03046 activity raises CCZ1P1's level | lines that do not express LINC03046 (38) vs lines expressing it (12) | 1.14× lower at baseline in the lines without LINC03046 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, LINC00824, LINC01205 |
| [[HDAC6]] | B | HDAC6 activity raises CCZ1P1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.455). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-43.8, 12.3); signed map (-0.6, -0.7). **Vector** length 67.6, 11.7% of its response variance represented; |z| ≥ 3 in 646 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +5.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +1.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.1 | -4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.9 | +0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.2 | +1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -3.1 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.6 | -0.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | CCZ1 pseudogene 1 |
| Locus type | pseudogene |
| Location | 7q21.3 — chr7:97,969,005-97,972,254 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55746](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55746) · Entrez [110440226](https://www.ncbi.nlm.nih.gov/gene/110440226) · Ensembl [ENSG00000243554](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243554)

## Data

Gene col 14364: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14364); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14364, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14364]; `tensor/DDL_lfc|DDL_z.npy` [14364]; `embed/gene_vectors.npy` [14364]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14364 or target_col == 14364). Every well: [[CCZ1P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCZ1P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

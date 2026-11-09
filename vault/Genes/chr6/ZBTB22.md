---
symbol: "ZBTB22"
type: "gene"
col: 14061
ensembl_id: "ENSG00000236104"
name: "zinc finger and BTB domain containing 22"
location: "6p21.32"
module: 153
arm: "+"
pooled_cpm: 2.55
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# ZBTB22

*zinc finger and BTB domain containing 22* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.90× (z +6.1, q 8e-07, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cepharanthine (drug)]] 5 µM: 1.39× (z +4.6, q 0.001, up in 3 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.473× (z -7.3, q 1e-10, down in 26 of 44 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.586× (z -5.2, q 2e-05, down in 16 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RUSC1-AS1]] (+0.67, fdr 1e-05), [[FBRS]] (+0.63, fdr 1e-05), [[MED12]] (+0.62, fdr 1e-05); moves opposite to [[ECI2]] (-0.49, fdr 1e-04), [[RNF216]] (-0.48, fdr 2e-04), [[EEF1AKMT4]] (-0.47, fdr 5e-05).
> It is in [[Module 153]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14061.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +6.1 | 8e-07 | 2/5 (PANC-1, NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | **1.39×** | +4.6 | 0.001 | 3/43 (PANC-1, HCT15, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +3.8 | 0.027 | 1/5 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.49×** | +3.6 | 0.047 | 4/33 (NCI-H23, SHP-77, …) | all doses, flat | position effect removed |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 1.41× | +3.2 | 0.12 | 3/40 (SW 900, HS-578T, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | 1.38× | +3.2 | 0.12 | 1/42 (HS-578T) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.58× | +3.2 | 0.12 | 4/18 (LoVo, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | 1.37× | +3.1 | 0.13 | 1/42 (HepG2/C3A) | inconsistent across doses | position effect removed |
| [[Cepharanthine (drug)]] 0.5 µM |  | 1.36× | +3.0 | 0.13 | 2/35 (MIA PaCa-2, SW1417) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.0 | 0.13 | 4/47 (NCI-H23, HT-29, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.36× | +3.0 | 0.13 | 2/12 (PANC-1, A-172) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14061.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.473×** | -7.3 | 1e-10 | 26/44 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.555×** | -5.8 | 2e-06 | 18/45 (Panc 03.27, SW 900, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.574×** | -5.4 | 1e-05 | 20/44 (BT-474, C-33 A, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.586×** | -5.2 | 2e-05 | 16/44 (A-172, H4, …) | all doses, flat | cell-cycle shift (explains ~17% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.591×** | -5.1 | 3e-05 | 12/25 (BT-474, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.660×** | -4.1 | 0.005 | 14/33 (KATO III, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.683×** | -3.7 | 0.016 | 13/45 (Panc 03.27, COLO 205, …) | rises with dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.696×** | -3.5 | 0.028 | 9/44 (RKO, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.691×** | -3.4 | 0.041 | 11/39 (RKO, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14061. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.49 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0749× (z -9.1) ⚠ transcription drop; unreliable plate only |
| [[BT-474 (line)]] | alt | 4.17 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0510× (z -9.7) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H23 (line)]] | alt | 2.40 | 0 | 1 | — | [[Malotilate (drug)]] 0.05 µM 0.0460× (z -8.5) |
| [[A-427 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14061), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RUSC1-AS1]] | +0.67 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[FBRS]] | +0.63 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[MED12]] | +0.62 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[STRN4]] | +0.60 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[THBS3]] | +0.60 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ZNF628]] | +0.59 | +0.59 / +0.50 | both halves | 1e-05 | same gene group |
| [[ERMAP]] | +0.58 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[INPPL1]] | +0.58 | +0.49 / +0.50 | both halves | 2e-05 |  |
| [[CFAP410]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[MTX1]] | +0.57 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[HLA-H]] | +0.57 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[WIZ]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECI2]] | -0.49 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[RNF216]] | -0.48 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[EEF1AKMT4]] | -0.47 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[DUXAP10]] | -0.47 | -0.35 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ZBTB22's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises ZBTB22's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.5, -22.1); signed map (16.3, -21.1). **Vector** length 37.9, 3.50% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.5 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.1 | +1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.1 | +2.4 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.1 | +4.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.0 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.9 | +1.2 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -1.7 | -5.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.5 | -7.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.0 | -0.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -0.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:33,314,406-33,317,942 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BING1, ZNF297A, fruitless, fru, ZBTB22A; previously ZNF297 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O15209](https://www.uniprot.org/uniprotkb/O15209) (Zinc finger and BTB domain-containing protein 22):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [9278](https://www.ncbi.nlm.nih.gov/gene/9278):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in chromatin. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13085](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13085) · Entrez [9278](https://www.ncbi.nlm.nih.gov/gene/9278) · UniProt [O15209](https://www.uniprot.org/uniprotkb/O15209) · Ensembl [ENSG00000236104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236104)

## Data

Gene col 14061: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14061); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14061, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14061]; `tensor/DDL_lfc|DDL_z.npy` [14061]; `embed/gene_vectors.npy` [14061]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14061 or target_col == 14061). Every well: [[ZBTB22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

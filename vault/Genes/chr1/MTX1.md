---
symbol: "MTX1"
type: "gene"
col: 10350
ensembl_id: "ENSG00000173171"
name: "metaxin 1"
location: "1q22"
module: 153
arm: "+"
pooled_cpm: 2.31
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# MTX1

*metaxin 1* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.41× (z +6.9, q 2e-09, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.61× (z +5.7, q 2e-06, up in 5 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.537× (z -5.3, q 6e-05, down in 16 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASH8P]] (+0.72, fdr 7e-06, ⚠ WASH8P in the vector space only through flagged drug-doses), [[NAXD]] (+0.69, fdr 2e-05), [[ATP13A1]] (+0.69, fdr 1e-05), [[SF3B4]] (+0.68, fdr 1e-05); moves opposite to [[CDKN2D]] (-0.62, fdr 1e-05), [[PPP1R13B]] (-0.60, fdr 2e-05), [[TMEM191A-1]] (-0.58, fdr 1e-04).
> It is in [[Module 153]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10350.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.41×** | +6.9 | 2e-09 | 1/3 (PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +6.3 | 8e-08 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +5.7 | 2e-06 | 5/44 (NCI-H23, Hs 766T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.66×** | +4.4 | 0.002 | 11/37 (NCI-H2030, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.0 | 0.008 | 7/45 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.39×** | +3.9 | 0.008 | 5/26 (NCI-H2030, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.008 | 9/40 (NCI-H1573, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +3.9 | 0.008 | 8/43 (NCI-H2347, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +3.8 | 0.008 | 1/11 (HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.43× | +3.1 | 0.12 | 6/44 (A498, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10350.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.537×** | -5.3 | 6e-05 | 16/43 (NCI-H23, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.619×** | -4.1 | 0.012 | 10/44 (HepG2/C3A, SW1417, …) | all doses, flat | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.638×** | -3.8 | 0.024 | 13/43 (NCI-H23, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.645×** | -3.7 | 0.027 | 14/43 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.649×** | -3.5 | 0.045 | 8/38 (HT-29, SW1417, …) | top dose only | position effect removed |
| [[Artesunate (drug)]] 5 µM |  | 0.763× | -3.2 | 0.11 | 6/45 (NCI-H2347, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 0.692× | -3.1 | 0.14 | 8/44 (SNU-423, HOP62, …) | inconsistent across doses | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | 0.700× | -3.0 | 0.17 | 7/44 (PANC-1, NCI-H1573, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10350. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.73 | 0 | 2 | — | [[Clotrimazole (drug)]] 0.5 µM 0.0779× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 5.52 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0681× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 2.34 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.107× (z -8.6) |
| [[A-172 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10350), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASH8P]] ⚠ | +0.72 | +0.60 / +0.70 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[NAXD]] | +0.69 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[ATP13A1]] | +0.69 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[SF3B4]] | +0.68 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[NCSTN]] | +0.67 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[ANKRD30BL]] | +0.67 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[WASH9P]] | +0.67 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[U2AF2]] | +0.66 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[BAP1]] | +0.65 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[AHSA2P]] | +0.62 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[STK36]] | +0.62 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[VPS52]] | +0.62 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ANAPC2]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN2D]] | -0.62 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[PPP1R13B]] | -0.60 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[TMEM191A-1]] | -0.58 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[SPATA2L]] | -0.55 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[FAM89B]] | -0.55 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[DNAJC1]] | -0.54 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[ARID3A]] | -0.53 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[ETHE1]] | -0.52 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[PI4KA]] | -0.52 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[CCDC112]] | -0.52 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[MINDY2]] | -0.52 | -0.43 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MTX1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC01232]] | B | LINC01232 activity lowers MTX1's level | lines that do not express LINC01232 (11) vs lines expressing it (39) | 1.33× higher at baseline in the lines without LINC01232 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000286856, SERPINB1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.8, -24.8); signed map (-13.7, -32.7). **Vector** length 39.7, 3.91% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.5 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | +3.9 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -1.6 | -4.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.6 | -5.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.1 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | metaxin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,208,695-155,213,824 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MTXN; previously MTX |
| Gene groups (HGNC) | Metaxins |
| Reactome | 9 pathways, smallest: Cristae formation; Mitochondrial protein import; RAC2 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13505](https://www.uniprot.org/uniprotkb/Q13505) (Metaxin-1):

> Involved in transport of proteins into the mitochondrion. Essential for embryonic development (By similarity).

**Summary**, from NCBI Gene [4580](https://www.ncbi.nlm.nih.gov/gene/4580):

> Predicted to be involved in mitochondrial outer membrane translocase complex assembly and protein insertion into mitochondrial outer membrane. Located in mitochondrion. Part of MIB complex and SAM complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7504](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7504) · Entrez [4580](https://www.ncbi.nlm.nih.gov/gene/4580) · UniProt [Q13505](https://www.uniprot.org/uniprotkb/Q13505) · Ensembl [ENSG00000173171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173171)

## Data

Gene col 10350: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10350); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10350, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10350]; `tensor/DDL_lfc|DDL_z.npy` [10350]; `embed/gene_vectors.npy` [10350]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10350 or target_col == 10350). Every well: [[MTX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "EMILIN2"
type: "gene"
col: 5287
ensembl_id: "ENSG00000132205"
name: "elastin microfibril interfacer 2"
location: "18p11.32-p11.31"
module: 150
arm: "+"
pooled_cpm: 2.87
n_lines_expressing: 39
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# EMILIN2

*elastin microfibril interfacer 2* — 18p11.32-p11.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.36× (z +13.0, q 1e-35, up in 16 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.668× (z -4.3, q 0.010, down in 12 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW480 0.0993×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.293×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLD5]] (+0.56, fdr 1e-05), [[TRPM2]] (+0.55, fdr 3e-05), [[PLB1]] (+0.55, fdr 2e-05); moves opposite to [[DNAJC16]] (-0.46, fdr 6e-04), [[CETN2]] (-0.42, fdr 2e-04), [[KIAA1328]] (-0.42, fdr 3e-04).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5287.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +13.0 | 1e-35 | 16/23 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.68×** | +10.1 | 1e-21 | 2/4 (J82, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.27×** | +8.8 | 4e-16 | 4/10 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +8.0 | 3e-13 | 4/6 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +7.6 | 4e-12 | 16/32 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.60×** | +7.1 | 1e-10 | 6/33 (A-172, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +5.9 | 3e-07 | 9/24 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +5.5 | 3e-06 | 6/22 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.99×** | +5.2 | 1e-05 | 1/7 (HOP62) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +5.1 | 1e-05 | 10/29 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +3.8 | 0.006 | 3/10 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.010 | 6/33 (HOP62, A549, …) | top dose only |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.1 | 0.075 | 0/16 | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +3.1 | 0.075 | 2/8 (HS-578T, J82) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.33×** | +3.0 | 0.097 | 0/31 | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5287.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW480 0.0993×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.293×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.668×** | -4.3 | 0.010 | 12/34 (SW480, CHP-212, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.713× | -3.5 | 0.15 | 11/33 (NCI-H2030, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Rucaparib (phosphate) (drug)]] 5 µM |  | 0.735× | -3.2 | 0.31 | 3/34 (CFPAC-1, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.742× | -3.1 | 0.31 | 10/29 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~18% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5287. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +10.9) | — |
| [[NCI-H460 (line)]] | wt | 0.829 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.0× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -8.7) |
| [[SW480 (line)]] | alt | 2.45 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0993× (z -9.1) |
| [[A-172 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.532 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.670 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.973 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.894 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.413 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.789 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.505 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.747 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.817 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.819 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.562 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5287), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLD5]] | +0.56 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[TRPM2]] | +0.55 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[PLB1]] | +0.55 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[ARHGAP40]] | +0.54 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[THSD7B]] | +0.54 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[CACNA1E]] | +0.52 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[DGUOK-AS1]] | +0.52 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[ARNT2-DT]] | +0.52 | +0.45 / +0.40 | both halves | 5e-05 |  |
| [[AP3B2]] | +0.52 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[KCNG3]] | +0.50 | +0.39 / +0.47 | both halves | 5e-05 |  |
| [[NKAIN1]] | +0.50 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[GRIA4]] | +0.50 | +0.39 / +0.49 | both halves | 5e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC16]] | -0.46 | -0.22 / -0.36 | both halves | 6e-04 |  |
| [[CETN2]] | -0.42 | -0.31 / -0.34 | both halves | 2e-04 |  |
| [[KIAA1328]] | -0.42 | -0.34 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EMILIN2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CASC11]] | B | CASC11 activity lowers EMILIN2's level | lines that do not express CASC11 (13) vs lines expressing it (37) | 1.89× higher at baseline in the lines without CASC11 | 0.089 | ⚠ within organs, on part of the lines; also absent: ANKRD18A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.1, 22.4); signed map (28.4, 12.4). **Vector** length 39.9, 5.26% of its response variance represented; |z| ≥ 3 in 751 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +13.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.3 | -4.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -1.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -0.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | elastin microfibril interfacer 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.32-p11.31 — chr18:2,847,006-2,916,003 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33200, FOAP-10 |
| Gene groups (HGNC) | EMI domain containing; C1q domain containing |
| Reactome | 3 pathways, smallest: Molecules associated with elastic fibres; Elastic fibre formation; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXX0](https://www.uniprot.org/uniprotkb/Q9BXX0) (EMILIN-2):

> May be responsible for anchoring smooth muscle cells to elastic fibers, and may be involved not only in the formation of the elastic fiber, but also in the processes that regulate vessel assembly. Has cell adhesive capacity.

**Summary**, from NCBI Gene [84034](https://www.ncbi.nlm.nih.gov/gene/84034):

> Predicted to enable extracellular matrix constituent conferring elasticity. Involved in several processes, including positive regulation of angiogenesis; positive regulation of defense response to bacterium; and positive regulation of platelet aggregation. Located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19881](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19881) · Entrez [84034](https://www.ncbi.nlm.nih.gov/gene/84034) · UniProt [Q9BXX0](https://www.uniprot.org/uniprotkb/Q9BXX0) · Ensembl [ENSG00000132205](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132205)

## Data

Gene col 5287: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5287); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5287, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5287]; `tensor/DDL_lfc|DDL_z.npy` [5287]; `embed/gene_vectors.npy` [5287]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5287 or target_col == 5287). Every well: [[EMILIN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMILIN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

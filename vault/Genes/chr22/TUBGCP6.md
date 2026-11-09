---
symbol: "TUBGCP6"
type: "gene"
col: 4861
ensembl_id: "ENSG00000128159"
name: "tubulin gamma complex component 6"
location: "22q13.33"
module: 2
arm: "+"
pooled_cpm: 9.79
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TUBGCP6

*tubulin gamma complex component 6* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 3.49× (z +14.4, q 3e-44, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.694× (z -4.1, q 0.025, down in 9 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Oxaprozin (drug)]] 0.05 µM in 1 line (C-33 A 0.0564×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (BT-474 0.0649×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pemetrexed (drug)]] 5 µM in 1 line (SNU-423 0.0795×); [[Rosiglitazone (drug)]] 5 µM in 1 line (RPMI-7951 0.0749×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPSF1]] (+0.77, fdr 7e-06), [[PCNX3]] (+0.74, fdr 7e-06), [[KLHL17]] (+0.72, fdr 7e-06); moves opposite to [[MPLKIP]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SEPTIN5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4861.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.49×** | +14.4 | 3e-44 | 47/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.92×** | +12.4 | 1e-32 | 46/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.56×** | +10.8 | 4e-25 | 44/47 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +6.1 | 2e-07 | 25/45 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +5.8 | 6e-07 | 28/47 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.62×** | +5.8 | 6e-07 | 27/46 (COLO 205, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +5.0 | 4e-05 | 24/45 (KATO III, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.02×** | +4.2 | 0.002 | 18/44 (KATO III, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | 1.32× | +3.1 | 0.13 | 7/18 (LOX-IMVI, HEC-1-A, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.20× | +3.0 | 0.15 | 11/43 (Panc 03.27, Hs 766T, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4861.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Oxaprozin (drug)]] 0.05 µM in 1 line (C-33 A 0.0564×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (BT-474 0.0649×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pemetrexed (drug)]] 5 µM in 1 line (SNU-423 0.0795×); [[Rosiglitazone (drug)]] 5 µM in 1 line (RPMI-7951 0.0749×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.694×** | -4.1 | 0.025 | 9/46 (MIA PaCa-2, A498, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | 0.735× | -3.3 | 0.23 | 12/45 (NCI-H23, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | 0.746× | -3.2 | 0.23 | 18/44 (LS 180, BT-474, …) | top dose only | position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 0.755× | -3.1 | 0.23 | 9/46 (AN3 CA, NCI-H661, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4861. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 8.32 | 0 | 2 | — | [[Rosiglitazone (drug)]] 5 µM 0.0749× (z -9.3) |
| [[BT-474 (line)]] | alt | 8.46 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0649× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 12.8 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0564× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 9.96 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.5 µM 0.0698× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 6.40 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.17× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 7.32 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0795× (z -10.5) |
| [[SW48 (line)]] | wt | 14.3 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0866× (z -9.0) |
| [[A-172 (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4861), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF1]] | +0.77 | +0.69 / +0.75 | both halves | 7e-06 | STRING 450 |
| [[PCNX3]] | +0.74 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[KLHL17]] | +0.72 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[INTS1]] | +0.72 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[NOP9]] | +0.71 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[SBF1]] | +0.70 | +0.66 / +0.60 | both halves | 7e-06 | STRING 541 |
| [[ABCA2]] | +0.70 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[ABHD17A]] | +0.69 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ANAPC2]] | +0.68 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[EPN1]] | +0.68 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[CCAR2]] | +0.64 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[INTS11]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPLKIP]] | -0.59 | -0.46 / -0.60 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEPTIN5]] | B | SEPTIN5 activity raises TUBGCP6's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.19× lower at baseline in the lines without SEPTIN5 | 0.051 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[HDAC6]] | B | HDAC6 activity lowers TUBGCP6's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NOTCH2NLR]] | B | NOTCH2NLR activity raises TUBGCP6's level | lines that do not express NOTCH2NLR (9) vs lines expressing it (41) | 1.28× lower at baseline in the lines without NOTCH2NLR | 0.097 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.721). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.4, -23.7); signed map (-45.0, -11.0). **Vector** length 64.9, 9.95% of its response variance represented; |z| ≥ 3 in 918 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +1.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.8 | +14.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.8 | +5.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.4 | +10.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.4 | +12.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +4.2 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.7 | +0.8 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Arbutin (drug)]] 0.5 µM |  | +1.5 | +0.8 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.5 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -1.3 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | tubulin gamma complex component 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,217,689-50,245,023 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GCP6, KIAA1669, DJ402G11.6 |
| Gene groups (HGNC) | Tubulin gamma complex component family |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 9 pathways, smallest: Centrosome maturation; Recruitment of mitotic centrosome proteins and complexes; Recruitment of NuMA to mitotic centrosomes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RT7](https://www.uniprot.org/uniprotkb/Q96RT7) (Gamma-tubulin complex component 6):

> Component of the gamma-tubulin ring complex (gTuRC) which mediates microtubule nucleation. The gTuRC regulates the minus-end nucleation of alpha-beta tubulin heterodimers that grow into microtubule protafilaments, a critical step in centrosome duplication and spindle formation.

**Summary**, from NCBI Gene [85378](https://www.ncbi.nlm.nih.gov/gene/85378):

> The protein encoded by this gene is part of a large multisubunit complex required for microtubule nucleation at the centrosome. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18127](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18127) · Entrez [85378](https://www.ncbi.nlm.nih.gov/gene/85378) · UniProt [Q96RT7](https://www.uniprot.org/uniprotkb/Q96RT7) · Ensembl [ENSG00000128159](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128159)

## Data

Gene col 4861: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4861); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4861, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4861]; `tensor/DDL_lfc|DDL_z.npy` [4861]; `embed/gene_vectors.npy` [4861]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4861 or target_col == 4861). Every well: [[TUBGCP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBGCP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

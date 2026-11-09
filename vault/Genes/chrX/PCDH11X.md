---
symbol: "PCDH11X"
type: "gene"
col: 2234
ensembl_id: "ENSG00000102290"
name: "protocadherin 11 X-linked"
location: "Xq21.31"
module: 150
arm: "+"
pooled_cpm: 6.17
n_lines_expressing: 35
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# PCDH11X

*protocadherin 11 X-linked* — Xq21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.87× (z +14.9, q 0e+00, up in 17 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGFEM1P]] (+0.65, fdr 7e-06), [[CTNNA3]] (+0.64, fdr 3e-05), [[MAPK10]] (+0.62, fdr 1e-05); moves opposite to [[EDEM2]] (-0.49, fdr 6e-05).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[COL17A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2234.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.87×** | +14.9 | 0e+00 | 17/27 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.56×** | +13.3 | 7e-38 | 19/29 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.75×** | +13.2 | 2e-37 | 9/15 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +9.0 | 3e-17 | 1/6 (AsPC-1) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +7.9 | 3e-13 | 0/3 | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +4.6 | 4e-04 | 10/31 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +4.3 | 0.001 | 7/27 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.2 | 0.002 | 5/28 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +4.2 | 0.002 | 6/30 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.2 | 0.002 | 4/24 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.07×** | +3.8 | 0.007 | 0/6 | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.015 | 4/30 (HOP62, NCI-H460, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.42×** | +3.5 | 0.017 | 0/13 | inconsistent across doses | low cells (technical?) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.021 | 3/25 (LS 180, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.045 | 3/29 (J82, NCI-H1573, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.57×** | +3.2 | 0.049 | 8/27 (SW480, SW1417, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +2.9 | 0.088 | 5/31 (BT-474, NCI-H460, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.37×** | +2.9 | 0.088 | 2/29 (NCI-H460, LoVo) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2234. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.45× (z +10.2) | — |
| [[HOP62 (line)]] | alt | 1.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 2.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +10.6) | — |
| [[A-172 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 113 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2234), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGFEM1P]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[CTNNA3]] | +0.64 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[MAPK10]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[CFAP46]] | +0.61 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[CACNA1E]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[CNTN5]] | +0.59 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[FAT3]] | +0.59 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[LRRC4C]] | +0.58 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[HYDIN]] | +0.58 | +0.65 / +0.38 | both halves | 7e-05 | same gene group |
| [[MYO16]] | +0.58 | +0.66 / +0.36 | both halves | 1e-04 | same gene group |
| [[NPAS3]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[GALNTL6]] | +0.58 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDEM2]] | -0.49 | -0.39 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PCDH11X's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TFF2]] | B | TFF2 activity raises PCDH11X's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 1.22× lower at baseline in the lines without TFF2 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |
| [[TMEM229B]] | C | TMEM229B activity lowers PCDH11X's level | lines that do not express TMEM229B (3) vs lines expressing it (47) | 3.48× higher at baseline in the lines without TMEM229B | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MAGI1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL17A1]] | B | PCDH11X activity raises COL17A1's level | lines that do not express PCDH11X (15) vs lines expressing it (35) | 3.32× lower at baseline in the lines without PCDH11X | 0.016 | ⚠ within organs, on part of the lines; also absent: XDH, CRYBG2, SPATA6L; maybe low, not absent |
| [[KLK10]] | B | PCDH11X activity raises KLK10's level | lines that do not express PCDH11X (15) vs lines expressing it (35) | 3.55× lower at baseline in the lines without PCDH11X | 0.042 | ⚠ within organs, on part of the lines; also absent: XDH, CRYBG2, SPATA6L; maybe low, not absent |
| [[LINC00882]] | B | PCDH11X activity lowers LINC00882's level | lines that do not express PCDH11X (15) vs lines expressing it (35) | 2.43× higher at baseline in the lines without PCDH11X | 0.054 | ⚠ within organs, on part of the lines; also absent: XDH, CRYBG2, SPATA6L; maybe low, not absent |
| [[ADIRF]] | B | PCDH11X activity raises ADIRF's level | lines that do not express PCDH11X (15) vs lines expressing it (35) | 2.11× lower at baseline in the lines without PCDH11X | 0.078 | ⚠ within organs, on part of the lines; also absent: XDH, CRYBG2, SPATA6L; maybe low, not absent |
| [[PRSS48]] | B | PCDH11X activity raises PRSS48's level | lines that do not express PCDH11X (15) vs lines expressing it (35) | 1.13× lower at baseline in the lines without PCDH11X | 0.098 | ⚠ within organs, on part of the lines; also absent: XDH, CRYBG2, SPATA6L; maybe low, not absent |

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (27.5, 28.3); signed map (37.9, 17.3). **Vector** length 39.2, 5.33% of its response variance represented; |z| ≥ 3 in 635 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +13.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.9 | +2.2 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -1.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -1.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -0.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.9 | -2.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | protocadherin 11 X-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq21.31 — chrX:91,779,261-92,623,230 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PCDH-X, PCDHX, PPP1R119; previously PCDH11 |
| Gene groups (HGNC) | Non-clustered protocadherins; Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZA7](https://www.uniprot.org/uniprotkb/Q9BZA7) (Protocadherin-11 X-linked):

> Potential calcium-dependent cell-adhesion protein.

**Summary**, from NCBI Gene [27328](https://www.ncbi.nlm.nih.gov/gene/27328):

> This gene belongs to the protocadherin gene family, a subfamily of the cadherin superfamily. The encoded protein consists of an extracellular domain containing 7 cadherin repeats, a transmembrane domain and a cytoplasmic tail that differs from those of the classical cadherins. The gene is located in a major X/Y block of homology and its Y homolog, despite divergence leading to coding region changes, is the most closely related cadherin family member. The protein is thought to play a fundamental …

**Accessions** — [HGNC:8656](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8656) · Entrez [27328](https://www.ncbi.nlm.nih.gov/gene/27328) · UniProt [Q9BZA7](https://www.uniprot.org/uniprotkb/Q9BZA7) · Ensembl [ENSG00000102290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102290)

## Data

Gene col 2234: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2234); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2234, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2234]; `tensor/DDL_lfc|DDL_z.npy` [2234]; `embed/gene_vectors.npy` [2234]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2234 or target_col == 2234). Every well: [[PCDH11X — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCDH11X.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

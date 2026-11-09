---
symbol: "PPP1R3F"
type: "gene"
col: 556
ensembl_id: "ENSG00000049769"
name: "protein phosphatase 1 regulatory subunit 3F"
location: "Xp11.23"
module: 23
arm: "+"
pooled_cpm: 5.01
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# PPP1R3F

*protein phosphatase 1 regulatory subunit 3F* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.37× (z +14.1, q 2e-42, up in 27 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.420× (z -10.0, q 4e-21, down in 35 of 45 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.421× (z -10.0, q 4e-21, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEPTIN7-DT]] (+0.83, fdr 7e-06), [[RFX3-DT]] (+0.81, fdr 1e-05), [[CHD1-DT]] (+0.81, fdr 8e-06).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CHD1-DT]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 556.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.37×** | +14.1 | 2e-42 | 27/38 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +12.1 | 3e-31 | 32/38 (PANC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +8.8 | 4e-16 | 7/24 (HEC-1-A, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +7.7 | 2e-12 | 22/37 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +6.7 | 2e-09 | 10/15 (SW480, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +6.1 | 1e-07 | 4/8 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.8 | 2e-04 | 16/45 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.0 | 0.005 | 7/26 (KATO III, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.009 | 12/44 (A-427, SNU-423, …) | top dose only | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.041 | 4/47 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.2 | 0.074 | 4/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 556.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.420×** | -10.0 | 4e-21 | 35/45 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.421×** | -10.0 | 4e-21 | 32/45 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.451×** | -9.2 | 5e-18 | 31/45 (NCI-H1792, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.650×** | -5.0 | 9e-05 | 17/45 (AN3 CA, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.530×** | -3.8 | 0.014 | 10/32 (C-33 A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.726×** | -3.7 | 0.020 | 15/36 (PANC-1, H4, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.735×** | -3.6 | 0.030 | 16/44 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.743×** | -3.4 | 0.041 | 12/43 (PANC-1, SW480, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | **0.718×** | -3.4 | 0.050 | 11/43 (Panc 03.27, SW1417, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.739×** | -3.3 | 0.052 | 10/43 (MIA PaCa-2, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Baicalin (drug)]] 0.5 µM |  | **0.753×** | -3.3 | 0.053 | 6/44 (SK-MEL-2, SNU-423, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 556. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 8.56 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0779× (z -9.0) |
| [[J82 (line)]] | alt | 3.84 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0797× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 2.46 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0792× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 6.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 8.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 7.90 | 0 | 1 | — | [[Arbutin (drug)]] 5 µM 0.0570× (z -8.9) |
| [[A-172 (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 556), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN7-DT]] | +0.83 | +0.81 / +0.58 | both halves | 7e-06 |  |
| [[RFX3-DT]] | +0.81 | +0.79 / +0.52 | both halves | 1e-05 |  |
| [[CHD1-DT]] | +0.81 | +0.77 / +0.57 | both halves | 8e-06 |  |
| [[LRRC37A3]] | +0.80 | +0.83 / +0.33 | both halves | 1e-04 |  |
| [[SMIM15-AS1]] | +0.80 | +0.79 / +0.55 | both halves | 1e-05 |  |
| [[OXA1L-DT]] | +0.79 | +0.76 / +0.51 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | +0.79 | +0.77 / +0.41 | both halves | 4e-05 |  |
| [[GLIPR1-AS1]] | +0.79 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[ATE1OSP]] | +0.78 | +0.80 / +0.43 | both halves | 3e-05 |  |
| [[RBM26-AS1]] | +0.78 | +0.76 / +0.46 | both halves | 3e-05 |  |
| [[TMEM202-AS1]] | +0.78 | +0.75 / +0.45 | both halves | 3e-05 |  |
| [[PSMD6-AS1]] | +0.78 | +0.74 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHD1-DT]] | C | CHD1-DT's natural level strengthens PPP1R3F's drug response | CHD1-DT's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.17; direction not clear | 0.096 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.816). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (5.4, 15.8); signed map (26.1, -8.8). **Vector** length 74.0, 12.4% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +14.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +12.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.9 | -9.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.7 | -10.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.1 | -10.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.3 | -5.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -1.0 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 3F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:49,269,793-49,301,461 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Hb2E |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZSY5](https://www.uniprot.org/uniprotkb/Q6ZSY5) (Protein phosphatase 1 regulatory subunit 3F):

> Glycogen-targeting subunit for protein phosphatase 1 (PP1).

**Summary**, from NCBI Gene [89801](https://www.ncbi.nlm.nih.gov/gene/89801):

> This gene encodes a protein that has been identified as one of several type-1 protein phosphatase (PP1) regulatory subunits. One or two of these subunits, together with the well-conserved catalytic subunit, can form the PP1 holoenzyme, where the regulatory subunit functions to regulate substrate specificity and/or targeting to a particular cellular compartment. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:14944](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14944) · Entrez [89801](https://www.ncbi.nlm.nih.gov/gene/89801) · UniProt [Q6ZSY5](https://www.uniprot.org/uniprotkb/Q6ZSY5) · Ensembl [ENSG00000049769](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000049769)

## Data

Gene col 556: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 556); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 556, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 556]; `tensor/DDL_lfc|DDL_z.npy` [556]; `embed/gene_vectors.npy` [556]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 556 or target_col == 556). Every well: [[PPP1R3F — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R3F.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

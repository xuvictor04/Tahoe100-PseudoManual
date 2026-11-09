---
symbol: "THAP10"
type: "gene"
col: 4942
ensembl_id: "ENSG00000129028"
name: "THAP domain containing 10"
location: "15q23"
module: 35
arm: "+"
pooled_cpm: 2.33
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# THAP10

*THAP domain containing 10* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.70× (z +17.8, q 0e+00, up in 27 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.539× (z -6.0, q 1e-06, down in 14 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SW480 0.0928×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.193×).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD9B]] (+0.64, fdr 1e-05), [[C19orf54]] (+0.62, fdr 3e-05), [[ZNF213]] (+0.59, fdr 2e-05); moves opposite to [[CYB5R3]] (-0.53, fdr 1e-04), [[SLC23A2]] (-0.51, fdr 2e-04), [[KANK2]] (-0.47, fdr 0.002, ⚠ not reproduced).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4942.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.70×** | +17.8 | 0e+00 | 27/28 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +9.1 | 3e-17 | 12/31 (HEC-1-A, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.71×** | +8.9 | 2e-16 | 1/2 (A498) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.40×** | +8.4 | 6e-15 | 14/29 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.43×** | +8.2 | 3e-14 | 2/2 (PANC-1, A498) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.25×** | +7.5 | 7e-12 | 6/12 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.11×** | +7.2 | 6e-11 | 5/12 (HEC-1-A, J82, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.10×** | +7.1 | 8e-11 | 7/10 (KATO III, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.9 | 3e-10 | 11/43 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +6.5 | 6e-09 | 12/43 (KATO III, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.87×** | +6.0 | 9e-08 | 13/41 (HEC-1-A, HOP62, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.76×** | +5.4 | 3e-06 | 5/43 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +5.3 | 5e-06 | 8/24 (NCI-H2030, HOP62, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +5.2 | 9e-06 | 10/37 (HEC-1-A, SW480, …) | two highest doses | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +5.2 | 9e-06 | 12/36 (LoVo, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.4 | 0.022 | 5/40 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.076 | 1/27 (MIA PaCa-2) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.077 | 0/22 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4942.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SW480 0.0928×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.193×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.539×** | -6.0 | 1e-06 | 14/38 (HT-29, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.705× | -3.4 | 0.21 | 13/37 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rutin (trihydrate) (drug)]] 0.5 µM |  | 0.732× | -3.0 | 0.35 | 3/43 (BT-474, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4942. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 4.74 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.193× (z -9.5) |
| [[SW480 (line)]] | alt | 2.59 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.0928× (z -10.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 2.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.9× (z +9.6) | — |
| [[A-172 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.904 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.851 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.968 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.831 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.709 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4942), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD9B]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[C19orf54]] | +0.62 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[ZNF213]] | +0.59 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[MALINC1]] | +0.59 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[RWDD2B]] | +0.58 | +0.63 / +0.35 | both halves | 1e-04 |  |
| [[ZNF773]] | +0.57 | +0.59 / +0.24 | both halves | 4e-04 |  |
| [[MAD2L1BP]] | +0.57 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[ZNF85]] | +0.56 | +0.50 / +0.37 | both halves | 7e-05 |  |
| [[EIF5]] | +0.56 | +0.59 / +0.24 | both halves | 5e-04 |  |
| [[ZNF419]] | +0.55 | +0.45 / +0.38 | both halves | 6e-05 |  |
| [[ZNF689]] | +0.55 | +0.62 / +0.34 | both halves | 1e-04 |  |
| [[DUSP28]] | +0.55 | +0.54 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5R3]] | -0.53 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[SLC23A2]] | -0.51 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[KANK2]] | -0.47 | -0.45 / -0.12 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers THAP10's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.500). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-12.0, 6.9); signed map (12.8, -20.2). **Vector** length 42.8, 4.85% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +17.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +5.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.4 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +5.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +3.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.6 | -3.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.3 | -2.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.0 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | +1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | +0.0 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.8 | -1.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -0.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | THAP domain containing 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:70,881,342-70,892,433 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | THAP domain family |
| Matched by | ensembl_id |

UniProt [Q9P2Z0](https://www.uniprot.org/uniprotkb/Q9P2Z0) carries no function annotation.

**Summary**, from NCBI Gene [56906](https://www.ncbi.nlm.nih.gov/gene/56906):

> This gene encodes a member of a family of proteins sharing an N-terminal Thanatos-associated domain. The Thanatos-associated domain contains a zinc finger signature similar to DNA-binding domains. This gene is part of a bidirectional gene pair on the long arm of chromosome 15 that is regulated by estrogen and may play a role in breast cancer. [provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:23193](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23193) · Entrez [56906](https://www.ncbi.nlm.nih.gov/gene/56906) · UniProt [Q9P2Z0](https://www.uniprot.org/uniprotkb/Q9P2Z0) · Ensembl [ENSG00000129028](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129028)

## Data

Gene col 4942: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4942); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4942, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4942]; `tensor/DDL_lfc|DDL_z.npy` [4942]; `embed/gene_vectors.npy` [4942]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4942 or target_col == 4942). Every well: [[THAP10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THAP10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

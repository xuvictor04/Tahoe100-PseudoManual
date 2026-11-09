---
symbol: "NPIPA1"
type: "gene"
col: 11401
ensembl_id: "ENSG00000183426"
name: "nuclear pore complex interacting protein family member A1"
location: "16p13.11"
module: 2
arm: "+"
pooled_cpm: 4.44
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# NPIPA1

*nuclear pore complex interacting protein family member A1* — 16p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.48× (z +6.4, q 1e-07, up in 17 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.613× (z -5.6, q 1e-05, down in 17 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPIPP1]] (+0.69, fdr 7e-06), [[RHOT2]] (+0.63, fdr 7e-06), [[HGS]] (+0.62, fdr 1e-05); moves opposite to [[ATP5MC3]] (-0.57, fdr 2e-05, ⚠ ATP5MC3 in the vector space only through flagged drug-doses), [[TMSB4X]] (-0.51, fdr 3e-05), [[PARK7]] (-0.51, fdr 5e-05, ⚠ PARK7 in the vector space only through flagged drug-doses), [[BANF1]] (-0.50, fdr 4e-05), [[EID1]] (-0.45, fdr 4e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TMSB4X]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11401.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +6.4 | 1e-07 | 17/40 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +5.7 | 4e-06 | 1/7 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +4.6 | 7e-04 | 7/45 (A498, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +4.5 | 8e-04 | 15/39 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.67×** | +4.2 | 0.003 | 8/40 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.1 | 0.003 | 12/36 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.41×** | +4.0 | 0.006 | 8/39 (HOP62, SW480, …) | rises with dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.006 | 6/42 (hTERT-HPNE, C-33 A, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +3.9 | 0.007 | 5/30 (HOP62, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.009 | 14/45 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.009 | 7/40 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.016 | 9/44 (CFPAC-1, PANC-1, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.016 | 2/46 (Hs 766T, SW480) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11401.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.613×** | -5.6 | 1e-05 | 17/45 (NCI-H23, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.399×** | -5.5 | 1e-05 | 15/40 (MIA PaCa-2, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.706×** | -4.0 | 0.012 | 10/44 (H4, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | 0.765× | -3.1 | 0.30 | 20/38 (J82, KATO III, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11401. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 2.86 | 0 | 1 | — | [[5-Fluorouracil (drug)]] 0.5 µM 0.0727× (z -8.5) |
| [[A-172 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11401), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPIPP1]] | +0.69 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[RHOT2]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[HGS]] | +0.62 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[WDR6]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[HDAC10]] | +0.61 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[PKD1]] | +0.59 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[ZNF598]] | +0.59 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[UCKL1]] | +0.59 | +0.35 / +0.61 | both halves | 1e-04 |  |
| [[PLA2G4B]] | +0.58 | +0.39 / +0.66 | both halves | 6e-05 |  |
| [[PKD1P6]] | +0.57 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[U2AF1L4]] | +0.56 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[FHIP2B]] | +0.55 | +0.33 / +0.68 | both halves | 1e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MC3]] ⚠ | -0.57 | -0.61 / -0.46 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMSB4X]] | -0.51 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PARK7]] ⚠ | -0.51 | -0.39 / -0.44 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BANF1]] | -0.50 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[EID1]] | -0.45 | -0.26 / -0.51 | both halves | 4e-04 |  |
| [[ACTR2]] | -0.45 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[FAM104B]] | -0.45 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[C1GALT1C1]] | -0.45 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMSB4X]] | B | TMSB4X activity lowers NPIPA1's level | lines that do not express TMSB4X (9) vs lines expressing it (41) | 1.26× higher at baseline in the lines without TMSB4X | 0.085 | ⚠ within organs, on part of the lines; also absent: PRSS23, TCN2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.476). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-11.7, -24.1); signed map (-26.1, 0.6). **Vector** length 46.2, 5.18% of its response variance represented; |z| ≥ 3 in 834 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +2.1 | +6.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.0 | +4.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.7 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.6 | +4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +4.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +1.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | +0.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.8 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.5 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.3 | -2.8 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.1 | -2.9 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.1 | -2.7 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | nuclear pore complex interacting protein family member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.11 — chr16:14,922,802-14,952,060 (+) |
| Ensembl biotype | protein_coding |
| Also known as | morpheus; previously NPIP |
| Matched by | ensembl_id |

UniProt [Q9UND3](https://www.uniprot.org/uniprotkb/Q9UND3) carries no function annotation.

**Summary**, from NCBI Gene [9284](https://www.ncbi.nlm.nih.gov/gene/9284):

> Predicted to be involved in mRNA transport and protein transport. Predicted to be located in nuclear membrane. Predicted to be part of nuclear pore. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7909](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7909) · Entrez [9284](https://www.ncbi.nlm.nih.gov/gene/9284) · UniProt [Q9UND3](https://www.uniprot.org/uniprotkb/Q9UND3) · Ensembl [ENSG00000183426](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183426)

## Data

Gene col 11401: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11401); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11401, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11401]; `tensor/DDL_lfc|DDL_z.npy` [11401]; `embed/gene_vectors.npy` [11401]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11401 or target_col == 11401). Every well: [[NPIPA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPIPA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

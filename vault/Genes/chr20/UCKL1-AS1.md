---
symbol: "UCKL1-AS1"
type: "gene"
col: 15955
ensembl_id: "ENSG00000280213"
name: "UCKL1 antisense RNA 1"
location: "20q13.33"
module: 47
arm: "+"
pooled_cpm: 3.47
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# UCKL1-AS1

*UCKL1 antisense RNA 1* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.18× (z +9.2, q 2e-17, up in 29 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.518× (z -5.3, q 8e-05, down in 17 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C11orf91]] (+0.71, fdr 7e-06), [[WNT2B]] (+0.70, fdr 7e-06), [[SMIM41]] (+0.70, fdr 7e-06); moves opposite to [[WDSUB1]] (-0.57, fdr 1e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[EPHA1-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15955.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.18×** | +9.2 | 2e-17 | 29/41 (SW480, NCI-H23, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +6.9 | 2e-09 | 18/35 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.13×** | +6.0 | 3e-07 | 26/45 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +5.7 | 2e-06 | 1/6 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.88×** | +5.0 | 5e-05 | 18/44 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +4.2 | 0.002 | 8/33 (LOX-IMVI, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.61×** | +3.8 | 0.012 | 1/18 (CFPAC-1) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.59×** | +3.7 | 0.016 | 11/43 (RPMI-7951, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +3.2 | 0.073 | 9/44 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.17×** | +3.2 | 0.073 | 3/24 (SW480, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.089 | 4/43 (LS 180, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15955.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.518×** | -5.3 | 8e-05 | 17/44 (AsPC-1, J82, …) | inconsistent across doses | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.610×** | -4.0 | 0.021 | 14/45 (HEC-1-A, RPMI-7951, …) | top dose only | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.726×** | -3.6 | 0.054 | 16/42 (AsPC-1, RKO, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.743×** | -3.4 | 0.098 | 11/44 (J82, SHP-77, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~6% here); position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.649×** | -3.3 | 0.098 | 11/43 (A549, hTERT-HPNE, …) | top dose only | plate-row cell shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.674× | -3.2 | 0.15 | 16/46 (AsPC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.683× | -3.1 | 0.18 | 17/42 (H4, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15955. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 8.61 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0266× (z -13.1) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0903× (z -12.7) |
| [[SW480 (line)]] | alt | 3.17 | 1 | 1 | [[Auranofin (drug)]] 5 µM 7.03× (z +8.5) | [[Bendamustine (drug)]] 5 µM 0.118× (z -8.8) |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0738× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~51% of this change |
| [[Hs 766T (line)]] | wt | 4.95 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.0772× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 4.58 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0725× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 4.69 | 0 | 1 | — | [[Verapamil (drug)]] 5 µM 0.0691× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 2.01 | 0 | 1 (1 ⚠) | — | [[Edoxaban (tosylate monohydrate) (drug)]] 0.5 µM 0.0702× (z -8.5) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 7.35 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0932× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.918 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15955), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf91]] | +0.71 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[WNT2B]] | +0.70 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.70 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[LINC02133]] | +0.69 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.68 | +0.70 / +0.71 | both halves | 7e-06 | same gene group |
| [[PDE2A]] | +0.68 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[MYO15A]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[HYAL1]] | +0.68 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[MSANTD1]] | +0.67 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[HPX]] | +0.67 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[ORAI2]] | +0.67 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[CHADL]] | +0.67 | +0.65 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDSUB1]] | -0.57 | -0.54 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA1-AS1]] | B | EPHA1-AS1 activity raises UCKL1-AS1's level | lines that do not express EPHA1-AS1 (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without EPHA1-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| [[LMO7DN]] | B | LMO7DN activity raises UCKL1-AS1's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.38× lower at baseline in the lines without LMO7DN | 0.075 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[FAM3B]] | B | FAM3B activity raises UCKL1-AS1's level | lines that do not express FAM3B (12) vs lines expressing it (38) | 1.51× lower at baseline in the lines without FAM3B | 0.090 | ⚠ within organs, on part of the lines; also absent: TXNIP, CADPS2, PLAC4; maybe low, not absent |
| [[CYP2E1]], [[SCART1]] | C | CYP2E1, SCART1 activity raises UCKL1-AS1's level | lines that do not express CYP2E1, SCART1 (3) vs lines expressing them (47) | 2.13× lower at baseline in the lines without CYP2E1, SCART1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AHRR, ARHGAP15, FAT1; maybe low, not absent; its own permutation p; co-absent genes |
| [[ZDHHC11]] | C | ZDHHC11 activity raises UCKL1-AS1's level | lines that do not express ZDHHC11 (4) vs lines expressing it (46) | 1.48× lower at baseline in the lines without ZDHHC11 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[LINC02133]] | C | LINC02133 activity raises UCKL1-AS1's level | lines that do not express LINC02133 (4) vs lines expressing it (46) | 1.69× lower at baseline in the lines without LINC02133 | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LYG1, RBM44, TRIM72; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.768). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.6, -19.4); signed map (15.1, 14.5). **Vector** length 75.9, 12.9% of its response variance represented; |z| ≥ 3 in 1,145 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.1 | +9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.6 | +2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +5.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +0.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +2.8 |
| fall | [[Radotinib (drug)]] 5 µM |  | -4.0 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.8 | -5.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.5 | -4.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Afatinib (drug)]] 5 µM |  | -2.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | UCKL1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20q13.33 — chr20:63,953,384-63,956,985 (+) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ46647; previously UCKL1OS, UCKL1AS, UCKL1-AS |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:31967](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31967) · Entrez [100113386](https://www.ncbi.nlm.nih.gov/gene/100113386) · Ensembl [ENSG00000280213](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000280213)

## Data

Gene col 15955: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15955); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15955, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15955]; `tensor/DDL_lfc|DDL_z.npy` [15955]; `embed/gene_vectors.npy` [15955]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15955 or target_col == 15955). Every well: [[UCKL1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UCKL1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "C1QTNF7"
type: "gene"
col: 8643
ensembl_id: "ENSG00000163145"
name: "C1q and TNF related 7"
location: "4p15.32"
module: 21
arm: "+"
pooled_cpm: 2.14
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# C1QTNF7

*C1q and TNF related 7* — 4p15.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.00× (z +10.3, q 4e-22, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +4.2, q 0.002, up in 8 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.877× (z -4.5, q 0.004, down in 12 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.640× (z -4.3, q 0.004, down in 7 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0916×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EAF1-AS1]] (+0.70, fdr 7e-06), [[ZRANB2-AS1]] (+0.69, fdr 7e-06), [[VPS39-DT]] (+0.68, fdr 1e-05); moves opposite to [[ALG10]] (-0.53, fdr 3e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC01917]] → it (grade B ⚠); 2 go from it, the strongest it → [[C1QTNF7-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8643.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.00×** | +10.3 | 4e-22 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.65×** | +9.5 | 5e-19 | 4/8 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +7.1 | 3e-10 | 1/2 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.75×** | +5.5 | 6e-06 | 2/8 (HT-29, NCI-H1573) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +4.4 | 0.001 | 5/23 (NCI-H460, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.2 | 0.002 | 8/29 (A549, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.027 | 0/23 | inconsistent across doses | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.5 | 0.038 | 6/33 (LS 180, HOP62, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8643.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0916×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.877× | -4.5 | 0.004 | 12/47 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.640×** | -4.3 | 0.004 | 7/44 (BT-474, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.645×** | -4.3 | 0.004 | 11/44 (HOP62, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.694× | -3.4 | 0.11 | 4/40 (A-172, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Ciclopirox (drug)]] 0.05 µM |  | 0.723× | -3.2 | 0.18 | 5/40 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8643. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 4.42 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0916× (z -8.8) |
| [[A-172 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8643), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EAF1-AS1]] | +0.70 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.69 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[VPS39-DT]] | +0.68 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[HSPA2-AS1]] | +0.68 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[PP2D1]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[SLC13A4]] | +0.68 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[CTBP1-AS]] ⚠ | +0.67 | +0.65 / +0.63 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[C1QTNF7-AS1]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[TTC36-AS1]] | +0.66 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[SLC23A1]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[FLJ40194]] | +0.66 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[MLANA]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[TOMM20L-DT]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG10]] | -0.53 | -0.44 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01917]] | B | LINC01917 activity raises C1QTNF7's level | lines that do not express LINC01917 (19) vs lines expressing it (31) | 1.32× lower at baseline in the lines without LINC01917 | 0.002 | ⚠ within organs, on part of the lines; also absent: LINC00504, RMEL3, TEK; maybe low, not absent |
| [[CASC20]] | B | CASC20 activity raises C1QTNF7's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 1.31× lower at baseline in the lines without CASC20 | 0.013 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[LINC02641]] | B | LINC02641 activity raises C1QTNF7's level | lines that do not express LINC02641 (14) vs lines expressing it (36) | 1.31× lower at baseline in the lines without LINC02641 | 0.043 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent |
| [[LINC02398]] | B | LINC02398 activity raises C1QTNF7's level | lines that do not express LINC02398 (13) vs lines expressing it (37) | 1.31× lower at baseline in the lines without LINC02398 | 0.050 | ⚠ within organs, on part of the lines; also absent: ANKRD7, KCNMB2, IGSF11; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1QTNF7-AS1]] | C | C1QTNF7's natural level strengthens C1QTNF7-AS1's drug response | C1QTNF7's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.77, reverse -0.18; direction not clear | 0.002 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Belzutifan (drug)]] 5 µM | C | C1QTNF7's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | C1QTNF7's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.61 | 0.446 over the table, 0.063 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.685). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.3, 27.7); signed map (32.8, 6.1). **Vector** length 28.7, 2.02% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.5 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.4 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.7 | -0.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.7 | -0.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -4.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.8 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.8 | -1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -0.8 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.7 | -1.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | C1q and TNF related 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.32 — chr4:15,339,818-15,446,167 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CTRP7 |
| Gene groups (HGNC) | C1q and TNF related |
| Matched by | ensembl_id |

UniProt [Q9BXJ2](https://www.uniprot.org/uniprotkb/Q9BXJ2) carries no function annotation.

**Summary**, from NCBI Gene [114905](https://www.ncbi.nlm.nih.gov/gene/114905):

> Predicted to enable identical protein binding activity. Predicted to be located in endoplasmic reticulum lumen and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14342](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14342) · Entrez [114905](https://www.ncbi.nlm.nih.gov/gene/114905) · UniProt [Q9BXJ2](https://www.uniprot.org/uniprotkb/Q9BXJ2) · Ensembl [ENSG00000163145](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163145)

## Data

Gene col 8643: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8643); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8643, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8643]; `tensor/DDL_lfc|DDL_z.npy` [8643]; `embed/gene_vectors.npy` [8643]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8643 or target_col == 8643). Every well: [[C1QTNF7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1QTNF7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

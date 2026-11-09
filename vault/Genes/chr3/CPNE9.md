---
symbol: "CPNE9"
type: "gene"
col: 6891
ensembl_id: "ENSG00000144550"
name: "copine family member 9"
location: "3p25.3"
module: 53
arm: "+"
pooled_cpm: 2.14
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# CPNE9

*copine family member 9* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.76× (z +16.9, q 0e+00, up in 29 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 0.569× (z -4.2, q 0.019, down in 13 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0567×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF17]] (+0.81, fdr 7e-06), [[TRIM72]] (+0.81, fdr 7e-06), [[MIR9-1HG]] (+0.81, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LAG3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6891.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.76×** | +16.9 | 0e+00 | 29/32 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **4.67×** | +11.8 | 2e-29 | 38/45 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.92×** | +11.6 | 1e-28 | 24/28 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.39×** | +9.0 | 5e-17 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.12×** | +8.7 | 4e-16 | 30/41 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.96×** | +8.0 | 2e-13 | 23/36 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.73×** | +7.7 | 1e-12 | 18/28 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.72×** | +7.6 | 1e-12 | 28/42 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.64×** | +7.4 | 7e-12 | 21/35 (A-172, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +7.0 | 2e-10 | 5/11 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +5.7 | 5e-07 | 1/3 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.6 | 2e-04 | 7/42 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.79×** | +4.4 | 4e-04 | 13/43 (A549, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +3.7 | 0.008 | 2/9 (NCI-H23, A498) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +3.3 | 0.032 | 6/47 (HEC-1-A, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6891.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0567×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.569×** | -4.2 | 0.019 | 13/36 (A549, KATO III, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM |  | **0.710×** | -3.7 | 0.057 | 7/44 (Hs 766T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 5 µM |  | 0.648× | -3.3 | 0.17 | 8/45 (SNU-1, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.658× | -3.2 | 0.19 | 13/39 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.643× | -3.1 | 0.19 | 8/43 (SK-MEL-2, BT-474, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | 0.467× | -3.1 | 0.19 | 5/20 (SK-MEL-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.672× | -3.0 | 0.19 | 8/43 (SW48, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6891. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 1.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 3.73 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0567× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 2.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.02× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 0.902 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.3× (z +9.9) | — |
| [[SW480 (line)]] | alt | 2.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.83× (z +12.0) | — |
| [[A-172 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.785 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.885 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.836 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.885 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.853 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.869 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.960 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6891), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF17]] | +0.81 | +0.81 / +0.78 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.81 | +0.84 / +0.83 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.81 | +0.83 / +0.81 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.81 | +0.83 / +0.80 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.80 | +0.83 / +0.85 | both halves | 7e-06 |  |
| [[TINCR]] | +0.80 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[SGSM3-AS1]] | +0.79 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.79 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[USP50]] | +0.79 | +0.85 / +0.84 | both halves | 7e-06 |  |
| [[PILRA]] | +0.79 | +0.80 / +0.79 | both halves | 7e-06 |  |
| [[ELAVL3]] | +0.79 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[HPX]] | +0.78 | +0.81 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAG3]] | B | LAG3 activity raises CPNE9's level | lines that do not express LAG3 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without LAG3 | 0.053 | ⚠ within organs, on part of the lines; also absent: SCML2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[NPAS1]] | B | NPAS1 activity raises CPNE9's level | lines that do not express NPAS1 (9) vs lines expressing it (41) | 1.45× lower at baseline in the lines without NPAS1 | 0.080 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[XG]] | B | XG activity raises CPNE9's level | lines that do not express XG (5) vs lines expressing it (45) | 1.48× lower at baseline in the lines without XG | 0.097 | ⚠ within organs, on part of the lines; also absent: TXNRD3, FSCN1, ELK3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.852). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.0, -16.0); signed map (16.6, 12.6). **Vector** length 60.9, 8.95% of its response variance represented; |z| ≥ 3 in 1,242 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +16.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +7.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.8 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.7 |
|  | [[NG25 (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.0 | -2.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | copine family member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:9,703,826-9,729,908 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA4217 |
| Gene groups (HGNC) | Copines |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYJ1](https://www.uniprot.org/uniprotkb/Q8IYJ1) (Copine-9):

> Probable calcium-dependent phospholipid-binding protein that may play a role in calcium-mediated intracellular processes (By similarity). Plays a role in dendrite formation by melanocytes.

**Summary**, from NCBI Gene [151835](https://www.ncbi.nlm.nih.gov/gene/151835):

> Predicted to enable calcium-dependent phospholipid binding activity. Involved in positive regulation of dendrite extension. Located in extracellular exosome and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24336](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24336) · Entrez [151835](https://www.ncbi.nlm.nih.gov/gene/151835) · UniProt [Q8IYJ1](https://www.uniprot.org/uniprotkb/Q8IYJ1) · Ensembl [ENSG00000144550](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144550)

## Data

Gene col 6891: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6891); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6891, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6891]; `tensor/DDL_lfc|DDL_z.npy` [6891]; `embed/gene_vectors.npy` [6891]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6891 or target_col == 6891). Every well: [[CPNE9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPNE9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

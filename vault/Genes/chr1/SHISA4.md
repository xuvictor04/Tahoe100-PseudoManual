---
symbol: "SHISA4"
type: "gene"
col: 12723
ensembl_id: "ENSG00000198892"
name: "shisa family member 4"
location: "1q32.1"
module: 130
arm: "+"
pooled_cpm: 2.67
n_lines_expressing: 47
n_dd_up: 4
n_dd_down: 2
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# SHISA4

*shisa family member 4* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.76× (z +11.3, q 4e-27, up in 13 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.46× (z +3.9, q 0.015, up in 4 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.512× (z -4.9, q 6e-04, down in 22 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Abiraterone acetate (drug)]] 5 µM in 1 line (SNU-423 0.0501×); [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM in 1 line (NCI-H460 0.0700×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLMP]] (+0.59, fdr 1e-05), [[ATP6V0E1]] (+0.53, fdr 1e-04), [[GPBP1]] (+0.53, fdr 5e-05); moves opposite to [[DKC1]] (-0.47, fdr 3e-05), [[B3GNTL1]] (-0.47, fdr 5e-05), [[ZNF850]] (-0.47, fdr 4e-04).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MRAS]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SPACA9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12723.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.76×** | +11.3 | 4e-27 | 13/13 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.11×** | +9.8 | 3e-20 | 5/5 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.83×** | +7.0 | 5e-10 | 4/5 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.015 | 4/39 (A498, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.62× | +3.3 | 0.10 | 3/14 (NCI-H2347, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.57× | +3.3 | 0.10 | 3/11 (C32, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.83× | +3.1 | 0.14 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | 1.52× | +3.0 | 0.18 | 6/37 (J82, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12723.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Abiraterone acetate (drug)]] 5 µM in 1 line (SNU-423 0.0501×); [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM in 1 line (NCI-H460 0.0700×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.512×** | -4.9 | 6e-04 | 22/42 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.558×** | -4.3 | 0.005 | 15/33 (hTERT-HPNE, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.644× | -3.2 | 0.24 | 14/35 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.642× | -3.0 | 0.31 | 3/38 (PANC-1, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12723. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.07 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0700× (z -8.7) |
| [[SNU-423 (line)]] | alt | 3.19 | 0 | 1 | — | [[Abiraterone acetate (drug)]] 5 µM 0.0501× (z -8.9) |
| [[A-172 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.757 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.556 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.886 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.949 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.190 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.794 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12723), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLMP]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ATP6V0E1]] | +0.53 | +0.35 / +0.62 | both halves | 1e-04 |  |
| [[GPBP1]] | +0.53 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[CTSF]] | +0.52 | +0.33 / +0.62 | both halves | 1e-04 |  |
| [[LINC00847]] | +0.52 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[SPACA9]] | +0.52 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[PTRHD1]] ⚠ | +0.52 | +0.36 / +0.51 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[DNASE2]] | +0.51 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[CLIP3]] | +0.51 | +0.58 / +0.38 | both halves | 7e-05 |  |
| [[AIP]] | +0.50 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[PANX2]] | +0.50 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[HSPB1]] | +0.50 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[PPM1M]] | +0.49 | +0.49 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DKC1]] | -0.47 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[B3GNTL1]] | -0.47 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[ZNF850]] | -0.47 | -0.25 / -0.53 | both halves | 4e-04 |  |
| [[NOLC1]] | -0.47 | -0.26 / -0.55 | both halves | 4e-04 |  |
| [[TRAP1]] | -0.46 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[DDX11]] | -0.46 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[TREX2]] | -0.46 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[PPM1G]] | -0.45 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[URB2]] | -0.45 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[NOM1]] | -0.44 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[RRM2]] | -0.44 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[PHC2]] | -0.44 | -0.54 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MRAS]] | B | MRAS activity raises SHISA4's level | lines that do not express MRAS (11) vs lines expressing it (39) | 1.70× lower at baseline in the lines without MRAS | 0.018 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[ARMCX1]] | B | ARMCX1 activity raises SHISA4's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 1.82× lower at baseline in the lines without ARMCX1 | 0.062 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPACA9]] | C | SHISA4 activity raises SPACA9's level | lines that do not express SHISA4 (3) vs lines expressing it (47) | 1.83× lower at baseline in the lines without SHISA4 | 0.043 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: PPP2R3A, CCDC102A, ENSG00000250264 |

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.402). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (4.1, -52.0); signed map (-10.1, 1.7). **Vector** length 39.1, 4.66% of its response variance represented; |z| ≥ 3 in 761 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +11.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.9 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.3 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -3.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.7 | -4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -1.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -1.8 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.0 | -2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | shisa family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:201,888,680-201,892,587 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hShisa4; previously C1orf40, TMEM58 |
| Gene groups (HGNC) | Shisa family members |
| Matched by | ensembl_id |

UniProt [Q96DD7](https://www.uniprot.org/uniprotkb/Q96DD7) carries no function annotation.

**Summary**, from NCBI Gene [149345](https://www.ncbi.nlm.nih.gov/gene/149345):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27139](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27139) · Entrez [149345](https://www.ncbi.nlm.nih.gov/gene/149345) · UniProt [Q96DD7](https://www.uniprot.org/uniprotkb/Q96DD7) · Ensembl [ENSG00000198892](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198892)

## Data

Gene col 12723: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12723); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12723, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12723]; `tensor/DDL_lfc|DDL_z.npy` [12723]; `embed/gene_vectors.npy` [12723]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12723 or target_col == 12723). Every well: [[SHISA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHISA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

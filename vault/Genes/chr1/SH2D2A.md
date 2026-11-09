---
symbol: "SH2D2A"
type: "gene"
col: 380
ensembl_id: "ENSG00000027869"
name: "SH2 domain containing 2A"
location: "1q23.1"
module: 81
arm: "+"
pooled_cpm: 3.21
n_lines_expressing: 30
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# SH2D2A

*SH2 domain containing 2A* — 1q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.75× (z +8.2, q 2e-13, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.77× (z +5.2, q 3e-05, up in 12 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.547× (z -4.3, q 0.010, down in 9 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.169×, HOP62 0.0707×; ⚠ cell-cycle shift, explains ~20% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.0579×; ⚠ cell-cycle shift, would explain all of this change); [[Binimetinib (drug)]] 0.5 µM in 1 line (NCI-H460 0.205×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (NCI-H460 0.151×); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM in 1 line (NCI-H460 0.148×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC46A3]] (+0.66, fdr 7e-06), [[NLRP3]] (+0.63, fdr 7e-06), [[LINC02454]] (+0.63, fdr 1e-05); moves opposite to [[TNS3]] (-0.51, fdr 3e-05), [[MYOF]] (-0.50, fdr 4e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[CXCL8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 380.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.75×** | +8.2 | 2e-13 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.42×** | +7.9 | 8e-13 | 1/4 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.55×** | +5.8 | 1e-06 | 1/4 (KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +5.2 | 3e-05 | 12/27 (NCI-H2347, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.37×** | +5.0 | 7e-05 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.83×** | +3.5 | 0.040 | 1/2 (NCI-H460) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.81×** | +3.4 | 0.040 | 3/12 (HOP62, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.70×** | +3.4 | 0.040 | 3/26 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.040 | 2/26 (NCI-H460, KATO III) | top dose only | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +3.4 | 0.040 | 5/20 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.040 | 1/27 (HepG2/C3A) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **2.06×** | +3.3 | 0.049 | 2/12 (PANC-1, LS 180) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.66×** | +3.2 | 0.051 | 10/27 (HepG2/C3A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.64×** | +3.2 | 0.062 | 2/11 (LS 180, SW480) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.00×** | +3.1 | 0.062 | 2/14 (KATO III, LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.95×** | +3.0 | 0.089 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 380.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.169×, HOP62 0.0707×; ⚠ cell-cycle shift, explains ~20% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.0579×; ⚠ cell-cycle shift, would explain all of this change); [[Binimetinib (drug)]] 0.5 µM in 1 line (NCI-H460 0.205×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (NCI-H460 0.151×); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM in 1 line (NCI-H460 0.148×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.547×** | -4.3 | 0.010 | 9/27 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.571× | -3.3 | 0.32 | 6/27 (NCI-H460, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 380. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 40.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -12.5) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.205× (z -9.3) |
| [[HOP62 (line)]] | alt | 5.91 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0579× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.512 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.278 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.620 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.862 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.483 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.833 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.678 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.699 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.831 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.658 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.867 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.996 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.663 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.916 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.325 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.992 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.928 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 380), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC46A3]] | +0.66 | +0.58 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[NLRP3]] | +0.63 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[LINC02454]] | +0.63 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[BCL2A1]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SERPIND1]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[SHANK1]] | +0.61 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[PNP]] | +0.61 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[ROBO3]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.60 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[LRRC8C]] | +0.60 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[STX1A]] | +0.59 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ESM1]] | +0.59 | +0.57 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNS3]] | -0.51 | -0.45 / -0.50 | both halves | 3e-05 | same gene group |
| [[MYOF]] | -0.50 | -0.41 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL8]] | B | SH2D2A activity raises CXCL8's level | lines that do not express SH2D2A (20) vs lines expressing it (30) | 2.28× lower at baseline in the lines without SH2D2A | 0.035 | ⚠ within organs, on part of the lines; also absent: IL1R2, SLC17A9, MT1G; maybe low, not absent |
| [[PDCD1LG2]] | B | SH2D2A activity raises PDCD1LG2's level | lines that do not express SH2D2A (20) vs lines expressing it (30) | 1.66× lower at baseline in the lines without SH2D2A | 0.079 | ⚠ within organs, on part of the lines; also absent: IL1R2, SLC17A9, MT1G; maybe low, not absent |
| [[OAF]] | B | SH2D2A activity raises OAF's level | lines that do not express SH2D2A (20) vs lines expressing it (30) | 1.61× lower at baseline in the lines without SH2D2A | 0.089 | ⚠ within organs, on part of the lines; also absent: IL1R2, SLC17A9, MT1G; maybe low, not absent |
| [[ANTXR2]] | B | SH2D2A activity raises ANTXR2's level | lines that do not express SH2D2A (20) vs lines expressing it (30) | 2.10× lower at baseline in the lines without SH2D2A | 0.093 | ⚠ within organs, on part of the lines; also absent: IL1R2, SLC17A9, MT1G; maybe low, not absent |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.4, 4.5); signed map (13.0, 53.9). **Vector** length 42.1, 7.64% of its response variance represented; |z| ≥ 3 in 617 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.7 | +5.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.0 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.8 | +1.9 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.4 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -2.7 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | SH2 domain containing 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.1 — chr1:156,806,243-156,816,848 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TSAd, F2771 |
| Gene groups (HGNC) | SH2 domain containing |
| Reactome | 3 pathways, smallest: VEGFA-VEGFR2 Pathway; Signaling by VEGF; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP31](https://www.uniprot.org/uniprotkb/Q9NP31) (SH2 domain-containing protein 2A):

> Could be a T-cell-specific adapter protein involved in the control of T-cell activation. May play a role in the CD4-p56-LCK-dependent signal transduction pathway. Could also play an important role in normal and pathological angiogenesis. Could be an adapter protein that facilitates and regulates interaction of KDR with effector proteins important to endothelial cell survival and proliferation.

**Summary**, from NCBI Gene [9047](https://www.ncbi.nlm.nih.gov/gene/9047):

> This gene encodes an adaptor protein thought to function in T-cell signal transduction. A related protein in mouse is responsible for the activation of lymphocyte-specific protein-tyrosine kinase and functions in downstream signaling. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:10821](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10821) · Entrez [9047](https://www.ncbi.nlm.nih.gov/gene/9047) · UniProt [Q9NP31](https://www.uniprot.org/uniprotkb/Q9NP31) · Ensembl [ENSG00000027869](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000027869)

## Data

Gene col 380: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 380); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 380, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 380]; `tensor/DDL_lfc|DDL_z.npy` [380]; `embed/gene_vectors.npy` [380]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 380 or target_col == 380). Every well: [[SH2D2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH2D2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

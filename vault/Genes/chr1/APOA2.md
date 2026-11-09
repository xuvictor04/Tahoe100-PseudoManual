---
symbol: "APOA2"
type: "gene"
col: 8203
ensembl_id: "ENSG00000158874"
name: "apolipoprotein A2"
location: "1q23.3"
module: 8
arm: "+"
pooled_cpm: 6.51
n_lines_expressing: 4
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 9
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# APOA2

*apolipoprotein A2* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 12.8× (z +9.3, q 7e-18, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.72× (z +5.2, q 4e-05, up in 1 of 1 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.170×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (6 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 94 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AFP]] (+0.71, fdr 7e-06), [[PEG3]] (+0.59, fdr 1.00, ⚠ not reproduced), [[APOB]] (+0.56, fdr 0.003, ⚠ one half only (not replicated)), [[S100A1]] (+0.49, fdr 1e-05), [[AHSG]] (+0.47, fdr 7e-06); moves opposite to [[CENPS]] (-0.34, fdr 0.002, ⚠ not reproduced), [[PIGQ]] (-0.32, fdr 1e-03, ⚠ not reproduced), [[TTF2]] (-0.31, fdr 0.001, ⚠ not reproduced).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PEG3]] → it (grade C ⚠); 9 go from it, the strongest it → [[APOB]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8203.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **12.8×** | +9.3 | 7e-18 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.04×** | +7.3 | 7e-11 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.22×** | +6.2 | 1e-07 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.72×** | +5.2 | 4e-05 | 1/1 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.31×** | +4.2 | 0.003 | 1/1 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **6.13×** | +4.0 | 0.006 | 1/1 (HepG2/C3A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **2.84×** | +3.8 | 0.011 | 0/1 | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **6.08×** | +3.4 | 0.041 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +3.3 | 0.062 | 0/1 | top dose only | cell-cycle shift (explains ~24% here); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **4.38×** | +3.2 | 0.065 | 1/1 (HepG2/C3A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.170×; ⚠ cell-cycle shift, explains ~0% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8203. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 512 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.806 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.698 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.619 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.498 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.830 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.984 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.710 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.712 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.878 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.917 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.632 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.676 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.732 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.919 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.760 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.698 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.785 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.800 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.681 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.918 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.852 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.742 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.676 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8203), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 89 of them with an alert (⚠; 89 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AFP]] | +0.71 | +0.88 / +0.67 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation; STRING 905 |
| [[PEG3]] | +0.59 | +0.88 / -0.33 | ⚠ not reproduced | 1.00 |  |
| [[APOB]] | +0.56 | +0.90 / +0.08 | ⚠ one half (not replicated) | 0.003 | same gene group; pathway: Chylomicron assembly; STRING 999 |
| [[S100A1]] | +0.49 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[AHSG]] | +0.47 | +0.65 / +0.83 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation; STRING 943 |
| [[F2]] | +0.44 | +0.72 / +0.17 | ⚠ one half (not replicated) | 0.001 | pathway: Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs); STRING 798 |
| [[LNCAROD]] | +0.42 | +0.64 / -0.11 | ⚠ one half (not replicated) | 1.00 |  |
| [[NKD1]] | +0.40 | +0.44 / -0.12 | ⚠ not reproduced | 1.00 |  |
| [[TFF3]] | +0.40 | +0.26 / +0.17 | ⚠ not reproduced | 0.001 |  |
| [[RPL8]] ⚠ | +0.40 | +0.10 / +0.47 | ⚠ not reproduced | 0.003 | ⚠ in the vector space only through flagged drug-doses |
| [[RBP1]] | +0.39 | +0.53 / +0.06 | ⚠ one half (not replicated) | 0.004 | pathway: Metabolism of fat-soluble vitamins; STRING 512 |
| [[COLGALT2]] | +0.38 | +0.35 / +0.00 | ⚠ not reproduced | 0.009 |  |
| [[ITIH2]] | +0.38 | +0.41 / +0.56 | both halves | 4e-05 | pathway: Post-translational protein phosphorylation; STRING 677 |
| [[ALB]] | +0.38 | +0.47 / +0.70 | both halves | 2e-05 | pathway: Plasma lipoprotein assembly, remodeling, and clearance; STRING 962 |
| [[CPE]] | +0.34 | +0.27 / +0.31 | both halves | 3e-04 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPS]] | -0.34 | -0.13 / -0.35 | ⚠ not reproduced | 0.002 |  |
| [[PIGQ]] | -0.32 | -0.18 / -0.25 | ⚠ not reproduced | 1e-03 |  |
| [[TTF2]] | -0.31 | -0.16 / -0.25 | ⚠ not reproduced | 0.001 |  |
| [[RFLNB]] | -0.31 | -0.16 / -0.21 | ⚠ not reproduced | 0.001 |  |
| [[FAM83H]] | -0.31 | -0.25 / -0.14 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PEG3]] | C | PEG3 activity raises APOA2's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 2.97× lower at baseline in the lines without PEG3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1; co-absent with the target |
| [[APOB]] | C | APOB activity raises APOA2's level | lines that do not express APOB (47) vs lines expressing it (3) | 20.92× lower at baseline in the lines without APOB | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: APOA2, BMP10, TBXT; co-absent with the target; its own permutation p |
| [[AFP]], [[AHSG]], [[ALB]] | C | AFP, AHSG, ALB activity raises APOA2's level | lines that do not express AFP, AHSG, ALB (45) vs lines expressing them (5) | 7.34× lower at baseline in the lines without AFP, AHSG, ALB | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target; co-absent genes |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOB]] | C | APOA2 activity raises APOB's level | lines that do not express APOA2 (46) vs lines expressing it (4) | 15.44× lower at baseline in the lines without APOA2 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, AFP, BMP10; co-absent with the target; its own permutation p |
| [[ALB]] | C | APOA2 activity raises ALB's level | lines that do not express APOA2 (46) vs lines expressing it (4) | 13.82× lower at baseline in the lines without APOA2 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, AFP, BMP10; co-absent with the target; its own permutation p |
| [[AFP]] | C | APOA2 activity raises AFP's level | lines that do not express APOA2 (46) vs lines expressing it (4) | 13.37× lower at baseline in the lines without APOA2 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, AFP, BMP10; co-absent with the target; its own permutation p |
| [[AHSG]] | C | APOA2 activity raises AHSG's level | lines that do not express APOA2 (46) vs lines expressing it (4) | 13.22× lower at baseline in the lines without APOA2 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, AFP, BMP10; co-absent with the target; its own permutation p |
| [[NKD1]] | C | APOA2 activity raises NKD1's level | lines that do not express APOA2 (46) vs lines expressing it (4) | 7.46× lower at baseline in the lines without APOA2 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, AFP, BMP10; co-absent with the target; its own permutation p |
| [[RBP1]] | C | APOA2 activity raises RBP1's level | lines that do not express APOA2 (46) vs lines expressing it (4) | 5.84× lower at baseline in the lines without APOA2 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, AFP, BMP10; co-absent with the target; its own permutation p |
| [[LGR5]] | C | APOA2 activity raises LGR5's level | lines that do not express APOA2 (46) vs lines expressing it (4) | 4.28× lower at baseline in the lines without APOA2 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, AFP, BMP10; co-absent with the target; its own permutation p |
| [[AZGP1]] | C | APOA2 activity raises AZGP1's level | lines that do not express APOA2 (46) vs lines expressing it (4) | 3.59× lower at baseline in the lines without APOA2 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, AFP, BMP10; co-absent with the target; its own permutation p |
| [[EEPD1]] | C | APOA2 activity raises EEPD1's level | lines that do not express APOA2 (46) vs lines expressing it (4) | 2.29× lower at baseline in the lines without APOA2 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, AFP, BMP10; its own permutation p |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.0317). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.8, 54.1); signed map (65.7, 19.9). **Vector** length 4.52, 2.18% of its response variance represented; |z| ≥ 3 in 15 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +0.2 | -1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +0.2 | +2.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +0.1 | -0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +0.1 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.1 | +0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +0.1 | -0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.1 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.1 | +0.9 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.1 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.1 | +0.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.1 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -0.1 | +6.2 |
|  | [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.1 | -0.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.1 | -0.1 |
|  | [[Docetaxel (drug)]] 5 µM |  | -0.1 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.1 | +0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -0.1 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | apolipoprotein A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:161,222,292-161,223,631 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Apolipoproteins |
| Reactome | 16 pathways, smallest: Chylomicron remodeling; Chylomicron assembly; Plasma lipoprotein assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P02652](https://www.uniprot.org/uniprotkb/P02652) (Apolipoprotein A-II):

> May stabilize HDL (high density lipoprotein) structure by its association with lipids, and affect the HDL metabolism.

**Summary**, from NCBI Gene [336](https://www.ncbi.nlm.nih.gov/gene/336):

> This gene encodes apolipoprotein (apo-) A-II, which is the second most abundant protein of the high density lipoprotein particles. The protein is found in plasma as a monomer, homodimer, or heterodimer with apolipoprotein D. Defects in this gene may result in apolipoprotein A-II deficiency or hypercholesterolemia. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:601](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:601) · Entrez [336](https://www.ncbi.nlm.nih.gov/gene/336) · UniProt [P02652](https://www.uniprot.org/uniprotkb/P02652) · Ensembl [ENSG00000158874](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158874)

## Data

Gene col 8203: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8203); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8203, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8203]; `tensor/DDL_lfc|DDL_z.npy` [8203]; `embed/gene_vectors.npy` [8203]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8203 or target_col == 8203). Every well: [[APOA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APOA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

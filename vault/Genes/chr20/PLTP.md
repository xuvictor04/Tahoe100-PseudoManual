---
symbol: "PLTP"
type: "gene"
col: 2051
ensembl_id: "ENSG00000100979"
name: "phospholipid transfer protein"
location: "20q13.12"
module: 78
arm: "+"
pooled_cpm: 10.76
n_lines_expressing: 23
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# PLTP

*phospholipid transfer protein* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.79× (z +11.2, q 3e-26, up in 15 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +6.9, q 6e-10, up in 2 of 18 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H23 0.302×, NCI-H1792 0.353×, LOX-IMVI 0.363×, SW 900 0.380×, …; ⚠ cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 1 line (PANC-1 0.294×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.265×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC6A6]] (+0.64, fdr 1e-05), [[IDS]] (+0.60, fdr 1e-05), [[LOXL2]] (+0.56, fdr 1e-05); moves opposite to [[PYM1]] (-0.48, fdr 1e-04), [[LINC01551]] (-0.47, fdr 4e-04), [[FBXO4]] (-0.46, fdr 2e-04).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RGS16]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CRABP2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2051.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.79×** | +11.2 | 3e-26 | 15/19 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.30×** | +10.5 | 4e-23 | 5/12 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +8.1 | 9e-14 | 9/15 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.9 | 6e-10 | 2/18 (AsPC-1, CFPAC-1) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +5.8 | 1e-06 | 8/21 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +5.5 | 4e-06 | 6/21 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +5.2 | 1e-05 | 8/20 (HepG2/C3A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +5.0 | 4e-05 | 4/21 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.4 | 7e-04 | 5/15 (CFPAC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.003 | 1/20 (PANC-1) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +4.0 | 0.003 | 2/14 (Hs 766T, SW 900) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.65×** | +3.9 | 0.005 | 5/17 (Hs 766T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +3.9 | 0.005 | 2/19 (SW480, Hs 766T) | top dose only | cell-cycle shift (explains ~18% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.55×** | +3.4 | 0.027 | 5/17 (NCI-H460, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +3.3 | 0.040 | 4/17 (CFPAC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Darolutamide (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.083 | 0/20 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2051.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H23 0.302×, NCI-H1792 0.353×, LOX-IMVI 0.363×, SW 900 0.380×, …; ⚠ cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 1 line (PANC-1 0.294×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.265×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | 0.682× | -3.4 | 0.45 | 7/21 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.732× | -3.2 | 0.46 | 1/20 (SW480) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2051. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 39.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 40.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 134 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.217× (z -8.7) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 53.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 5.32 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.294× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 5.16 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.999 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.27 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2051), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC6A6]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[IDS]] | +0.60 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[LOXL2]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ECE1]] | +0.54 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[EDIL3]] | +0.54 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[ZNF385A]] | +0.54 | +0.31 / +0.64 | both halves | 2e-04 |  |
| [[LRP1]] | +0.54 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[TMEM132A]] | +0.53 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[TTYH2]] | +0.53 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[KCNMA1]] | +0.52 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[AZIN2]] | +0.52 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[F11R]] | +0.51 | +0.45 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYM1]] | -0.48 | -0.45 / -0.32 | both halves | 1e-04 |  |
| [[LINC01551]] | -0.47 | -0.52 / -0.24 | both halves | 4e-04 |  |
| [[FBXO4]] | -0.46 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[DIS3L]] | -0.46 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[NIPAL2]] | -0.45 | -0.51 / -0.20 | both halves | 7e-04 |  |
| [[PIGZ]] | -0.44 | -0.46 / -0.29 | both halves | 2e-04 |  |
| [[GABPB2]] | -0.44 | -0.36 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS16]] | B | RGS16 activity raises PLTP's level | lines that do not express RGS16 (13) vs lines expressing it (37) | 1.98× lower at baseline in the lines without RGS16 | 0.076 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ABCA1]] | B | ABCA1 activity raises PLTP's level | lines that do not express ABCA1 (20) vs lines expressing it (30) | 2.73× lower at baseline in the lines without ABCA1 | 0.092 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRABP2]] | C | PLTP activity raises CRABP2's level | lines that do not express PLTP (27) vs lines expressing it (23) | 2.68× lower at baseline in the lines without PLTP | 0.089 | ⚠ within organs, on part of the lines; also absent: SEC14L4, HAS2, PPP1R14A; co-absent with the target |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.318). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.7, -6.1); signed map (-10.5, 39.6). **Vector** length 33.4, 6.28% of its response variance represented; |z| ≥ 3 in 333 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.3 | +5.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +3.9 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.1 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -0.9 | +1.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -0.9 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | phospholipid transfer protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:45,898,621-45,912,155 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BPIFE |
| Gene groups (HGNC) | BPI fold containing |
| Reactome | 7 pathways, smallest: HDL remodeling; Plasma lipoprotein remodeling; NR1H3 & NR1H2 regulate gene expression linked to cholesterol transport and efflux |
| Matched by | ensembl_id |

**Function**, from UniProt [P55058](https://www.uniprot.org/uniprotkb/P55058) (Phospholipid transfer protein):

> Mediates the transfer of phospholipids and free cholesterol from triglyceride-rich lipoproteins (low density lipoproteins or LDL and very low density lipoproteins or VLDL) into high-density lipoproteins (HDL) as well as the exchange of phospholipids between triglyceride-rich lipoproteins themselves. Facilitates the transfer of a spectrum of different lipid molecules, including diacylglycerol, phosphatidic acid, sphingomyelin, phosphatidylcholine, phosphatidylinositol, phosphatidylglycerol, …

**Summary**, from NCBI Gene [5360](https://www.ncbi.nlm.nih.gov/gene/5360):

> The protein encoded by this gene is one of at least two lipid transfer proteins found in human plasma. The encoded protein transfers phospholipids from triglyceride-rich lipoproteins to high density lipoprotein (HDL). In addition to regulating the size of HDL particles, this protein may be involved in cholesterol metabolism. At least two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9093](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9093) · Entrez [5360](https://www.ncbi.nlm.nih.gov/gene/5360) · UniProt [P55058](https://www.uniprot.org/uniprotkb/P55058) · Ensembl [ENSG00000100979](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100979)

## Data

Gene col 2051: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2051); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2051, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2051]; `tensor/DDL_lfc|DDL_z.npy` [2051]; `embed/gene_vectors.npy` [2051]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2051 or target_col == 2051). Every well: [[PLTP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLTP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

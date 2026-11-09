---
symbol: "ITGA7"
type: "gene"
col: 5702
ensembl_id: "ENSG00000135424"
name: "integrin subunit alpha 7"
location: "12q13.2"
module: 100
arm: "+"
pooled_cpm: 4.23
n_lines_expressing: 44
n_dd_up: 32
n_dd_down: 2
n_dd_up_clean: 24
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# ITGA7

*integrin subunit alpha 7* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.39× (z +18.8, q 0e+00, up in 28 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.702× (z -3.9, q 0.059, down in 4 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (RPMI-7951 0.101×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CELF5]] (+0.75, fdr 1e-05), [[LHX4]] (+0.67, fdr 1e-05), [[ELAVL3]] (+0.67, fdr 7e-06); moves opposite to [[RPAP2]] (-0.58, fdr 2e-04), [[QRSL1]] (-0.56, fdr 5e-05), [[ARMC1]] (-0.54, fdr 3e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SEMA6B]] → it (grade B ⚠); 1 goes from it, the strongest it → [[KCNQ1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5702.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.39×** | +18.8 | 0e+00 | 28/30 (C32, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.02×** | +15.2 | 0e+00 | 35/39 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.61×** | +14.0 | 3e-42 | 33/38 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.34×** | +13.2 | 2e-37 | 27/36 (SW480, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.35×** | +13.2 | 2e-37 | 23/32 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.71×** | +13.1 | 3e-37 | 31/37 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.14×** | +12.5 | 7e-34 | 34/40 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.63×** | +10.6 | 3e-24 | 11/15 (SW1417, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +9.5 | 1e-19 | 5/6 (SK-MEL-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +8.8 | 1e-16 | 2/3 (SW1417, SNU-423) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +8.3 | 5e-15 | 11/25 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.70×** | +8.1 | 2e-14 | 23/37 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.13×** | +7.6 | 2e-12 | 17/27 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.87×** | +6.8 | 4e-10 | 21/34 (C-33 A, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.1 | 4e-08 | 8/38 (SW480, NCI-H2347, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.58×** | +5.4 | 2e-06 | 15/35 (SW1417, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +4.6 | 1e-04 | 6/30 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.76×** | +4.4 | 3e-04 | 8/22 (SHP-77, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.2 | 7e-04 | 6/25 (SNU-423, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5702.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (RPMI-7951 0.101×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.702×** | -3.9 | 0.059 | 4/38 (HS-578T, RKO, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.715×** | -3.7 | 0.068 | 13/39 (RKO, SW480, …) | rises with dose |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.712× | -3.4 | 0.11 | 6/39 (AsPC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.736× | -3.4 | 0.11 | 10/39 (NCI-H1792, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5702. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 17.6 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.65× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.06× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 4.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.34× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 1.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +12.0) | — |
| [[RPMI-7951 (line)]] | alt | 8.36 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.101× (z -8.9) |
| [[SNU-423 (line)]] | alt | 13.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +12.7) | — |
| [[A-172 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.944 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.905 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.855 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.862 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5702), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CELF5]] | +0.75 | +0.57 / +0.77 | both halves | 1e-05 |  |
| [[LHX4]] | +0.67 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[ELAVL3]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[RUNDC3B]] | +0.65 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[SEMA3F]] | +0.63 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[NRTN]] | +0.62 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[SYN1]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[RYR1]] | +0.62 | +0.43 / +0.78 | both halves | 3e-05 | pathway: HALLMARK_MYOGENESIS; STRING 558 |
| [[HCN2]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[CDH23]] | +0.60 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[KNDC1]] | +0.59 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[MAST1]] | +0.59 | +0.43 / +0.67 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPAP2]] | -0.58 | -0.31 / -0.61 | both halves | 2e-04 |  |
| [[QRSL1]] | -0.56 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[ARMC1]] | -0.54 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[TBCK]] | -0.51 | -0.24 / -0.51 | both halves | 5e-04 |  |
| [[PTCD2]] | -0.50 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[PARG]] | -0.49 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[ANGEL2]] | -0.49 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[MRPL9]] | -0.49 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[AGAP9]] | -0.49 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[MBTPS2]] | -0.49 | -0.42 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6B]] | B | SEMA6B activity raises ITGA7's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.93× lower at baseline in the lines without SEMA6B | 0.023 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ITGA7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SEMA3F]] | B | SEMA3F activity raises ITGA7's level | lines that do not express SEMA3F (6) vs lines expressing it (44) | 1.77× lower at baseline in the lines without SEMA3F | 0.093 | ⚠ within organs, on part of the lines; also absent: MCM2, PIMREG, GKAP1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNQ1]] | B | ITGA7 activity lowers KCNQ1's level | lines that do not express ITGA7 (6) vs lines expressing it (44) | 1.85× higher at baseline in the lines without ITGA7 | 0.079 | ⚠ within organs, on part of the lines; also absent: NXPE3, SLC22A4, TTC23L; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.716). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (14.3, 34.7); signed map (26.0, 19.2). **Vector** length 47.2, 6.14% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.3 | +13.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +18.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +6.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +6.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +1.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -0.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit alpha 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:55,684,568-55,716,404 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Integrin alpha subunits |
| Hallmark sets | MYOGENESIS, ADIPOGENESIS |
| Reactome | 4 pathways, smallest: Laminin interactions; ECM proteoglycans; Integrin cell surface interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13683](https://www.uniprot.org/uniprotkb/Q13683) (Integrin alpha-7):

> Integrin alpha-7/beta-1 is the primary laminin receptor on skeletal myoblasts and adult myofibers. During myogenic differentiation, it may induce changes in the shape and mobility of myoblasts, and facilitate their localization at laminin-rich sites of secondary fiber formation. It is involved in the maintenance of the myofibers cytoarchitecture as well as for their anchorage, viability and functional integrity. Isoform Alpha-7X2B and isoform Alpha-7X1B promote myoblast migration on laminin 1 …

**Summary**, from NCBI Gene [3679](https://www.ncbi.nlm.nih.gov/gene/3679):

> The protein encoded by this gene belongs to the integrin alpha chain family. Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain. They mediate a wide spectrum of cell-cell and cell-matrix interactions, and thus play a role in cell migration, morphologic development, differentiation, and metastasis. This protein functions as a receptor for the basement membrane protein laminin-1. It is mainly expressed in skeletal and cardiac muscles and may be …

**Accessions** — [HGNC:6143](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6143) · Entrez [3679](https://www.ncbi.nlm.nih.gov/gene/3679) · UniProt [Q13683](https://www.uniprot.org/uniprotkb/Q13683) · Ensembl [ENSG00000135424](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135424)

## Data

Gene col 5702: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5702); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5702, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5702]; `tensor/DDL_lfc|DDL_z.npy` [5702]; `embed/gene_vectors.npy` [5702]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5702 or target_col == 5702). Every well: [[ITGA7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGA7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

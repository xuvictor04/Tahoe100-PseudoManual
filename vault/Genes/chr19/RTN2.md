---
symbol: "RTN2"
type: "gene"
col: 4656
ensembl_id: "ENSG00000125744"
name: "reticulon 2"
location: "19q13.32"
module: 192
arm: "+"
pooled_cpm: 7.55
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/192"]
generated_by: "tahoemap"
---

# RTN2

*reticulon 2* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.68× (z +10.5, q 5e-23, up in 32 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.496× (z -7.5, q 5e-11, down in 24 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLIN3]] (+0.72, fdr 7e-06), [[TNNT1]] (+0.71, fdr 7e-06), [[RRAS]] (+0.70, fdr 7e-06); moves opposite to [[FUBP1]] (-0.64, fdr 2e-05), [[SNX5]] (-0.62, fdr 1e-05), [[NT5DC1]] (-0.61, fdr 1e-05).
> It is in [[Module 192]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MEIS3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4656.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.68×** | +10.5 | 5e-23 | 32/45 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.37×** | +9.2 | 1e-17 | 33/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +8.5 | 3e-15 | 33/46 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.13×** | +8.0 | 1e-13 | 29/45 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.13×** | +7.6 | 3e-12 | 28/43 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.81×** | +6.1 | 1e-07 | 22/44 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +5.7 | 8e-07 | 20/46 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.66×** | +5.4 | 6e-06 | 23/44 (LoVo, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +5.1 | 3e-05 | 7/15 (NCI-H2030, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +4.7 | 1e-04 | 19/39 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.001 | 14/40 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.59×** | +3.4 | 0.031 | 4/39 (PANC-1, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4656.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.496×** | -7.5 | 5e-11 | 24/44 (LoVo, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.627×** | -7.0 | 5e-10 | 24/40 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.518×** | -7.0 | 5e-10 | 28/46 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.523×** | -6.5 | 9e-09 | 22/41 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.660×** | -4.4 | 0.001 | 21/46 (MIA PaCa-2, NCI-H1792, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.669×** | -4.3 | 0.002 | 16/44 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -4.0 | 0.006 | 16/39 (J82, A-427, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.497×** | -3.9 | 0.007 | 17/43 (NCI-H1792, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.689×** | -3.7 | 0.011 | 11/45 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.713×** | -3.6 | 0.018 | 15/45 (LOX-IMVI, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.801×** | -3.3 | 0.043 | 18/47 (HS-578T, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.733×** | -3.3 | 0.046 | 17/46 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4656. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 24.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 16.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -11.9) |
| [[A-172 (line)]] | wt | 5.18 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0980× (z -13.0) |
| [[A-427 (line)]] | wt | 12.4 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -9.9) |
| [[C-33 A (line)]] | alt | 6.44 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0561× (z -8.7) |
| [[J82 (line)]] | alt | 3.69 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0464× (z -10.1) |
| [[LoVo (line)]] | wt | 11.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0745× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SHP-77 (line)]] | alt | 7.47 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0659× (z -9.5) |
| [[SW1417 (line)]] | alt | 27.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -9.5) |
| [[A498 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4656), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLIN3]] | +0.72 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[TNNT1]] | +0.71 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[RRAS]] | +0.70 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[MEIS3]] | +0.67 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[PRKCD]] | +0.66 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[GIPR]] | +0.66 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[FAM89B]] | +0.66 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[KLC3]] | +0.66 | +0.53 / +0.58 | both halves | 1e-05 | STRING 566 |
| [[DNASE1L1]] | +0.65 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[SLC66A2]] | +0.64 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[SYP]] | +0.64 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[TMEM184B]] | +0.64 | +0.51 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUBP1]] | -0.64 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[SNX5]] | -0.62 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[NT5DC1]] | -0.61 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[MBNL3]] | -0.59 | -0.53 / -0.40 | both halves | 4e-05 |  |
| [[LINC01515]] | -0.58 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[ENOSF1]] | -0.56 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[SUCLG2]] | -0.56 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[CASD1]] | -0.56 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[BCLAF1]] | -0.55 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[C5orf15]] | -0.55 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[FAM111A]] | -0.55 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[FZD6]] | -0.55 | -0.50 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEIS3]] | B | MEIS3 activity raises RTN2's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without MEIS3 | 0.023 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[TOP2A]] | B | TOP2A activity raises RTN2's level | compounds that target TOP2A: 3 of 5 lower it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SIGIRR]] | B | SIGIRR activity lowers RTN2's level | lines that do not express SIGIRR (9) vs lines expressing it (41) | 1.14× higher at baseline in the lines without SIGIRR | 0.074 | ⚠ within organs, on part of the lines; also absent: CLCF1, LTBR, MYOF |
| [[ATP2B4]] | B | ATP2B4 activity lowers RTN2's level | lines that do not express ATP2B4 (8) vs lines expressing it (42) | 1.47× higher at baseline in the lines without ATP2B4 | 0.078 | ⚠ within organs, on part of the lines; also absent: PROCR, ARSJ, LAMB1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RTN2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers RTN2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 192]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.830). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.50; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.2, 0.4); signed map (-24.2, 23.4). **Vector** length 88.1, 18.5% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +8.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.6 | +8.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.5 | +4.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +9.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.1 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -6.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.5 | -3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | reticulon 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,485,294-45,497,055 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NSP2, NSPL1; previously SPG12 |
| Gene groups (HGNC) | Reticulons |
| Matched by | ensembl_id |

**Function**, from UniProt [O75298](https://www.uniprot.org/uniprotkb/O75298) (Reticulon-2):

> Inhibits amyloid precursor protein processing, probably by blocking BACE1 activity. Enhances trafficking of the glutamate transporter SLC1A1/EAAC1 from the endoplasmic reticulum to the cell surface (By similarity). Plays a role in the translocation of SLC2A4/GLUT4 from intracellular membranes to the cell membrane which facilitates the uptake of glucose into the cell (By similarity).

**Summary**, from NCBI Gene [6253](https://www.ncbi.nlm.nih.gov/gene/6253):

> This gene belongs to the family of reticulon encoding genes. Reticulons are associated with the endoplasmic reticulum, and are involved in neuroendocrine secretion or in membrane trafficking in neuroendocrine cells. Reticulon proteins also play an important role in the replication of positive-strand RNA (ssRNA) viruses. Mutations at this locus have been associated with autosomal dominant spastic paraplegia-12. [provided by RefSeq, Aug 2020]

**Accessions** — [HGNC:10468](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10468) · Entrez [6253](https://www.ncbi.nlm.nih.gov/gene/6253) · UniProt [O75298](https://www.uniprot.org/uniprotkb/O75298) · Ensembl [ENSG00000125744](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125744)

## Data

Gene col 4656: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4656); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4656, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4656]; `tensor/DDL_lfc|DDL_z.npy` [4656]; `embed/gene_vectors.npy` [4656]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4656 or target_col == 4656). Every well: [[RTN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

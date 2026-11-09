---
symbol: "ROBO3"
type: "gene"
col: 7776
ensembl_id: "ENSG00000154134"
name: "roundabout guidance receptor 3"
location: "11q24.2"
module: 125
arm: "+"
pooled_cpm: 4.39
n_lines_expressing: 42
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# ROBO3

*roundabout guidance receptor 3* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.01× (z +9.3, q 7e-18, up in 12 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.64× (z +5.9, q 8e-07, up in 19 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.397× (z -7.8, q 3e-12, down in 24 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH2D2A]] (+0.61, fdr 1e-05), [[LIMD2]] (+0.58, fdr 9e-05), [[FSD1]] (+0.56, fdr 3e-05); moves opposite to [[CMPK1]] (-0.45, fdr 7e-04), [[PGM1]] (-0.43, fdr 4e-04), [[NDUFS1]] (-0.43, fdr 3e-04).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ROBO4]] → it (grade B ⚠); 5 go from it, the strongest it → [[PCCA-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7776.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.01×** | +9.3 | 7e-18 | 12/18 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +6.8 | 3e-09 | 5/10 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +5.9 | 8e-07 | 19/38 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +5.6 | 3e-06 | 6/11 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +5.4 | 8e-06 | 18/33 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +5.3 | 9e-06 | 11/39 (A-172, Hs 766T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~8% here); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.28×** | +3.6 | 0.026 | 3/30 (NCI-H460, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.48×** | +3.3 | 0.066 | 8/31 (SNU-423, PANC-1, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.12×** | +3.3 | 0.066 | 4/27 (Hs 766T, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7776.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.397×** | -7.8 | 3e-12 | 24/39 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.433×** | -7.1 | 3e-10 | 20/35 (NCI-H23, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.494×** | -6.0 | 4e-07 | 19/34 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.627×** | -5.6 | 3e-06 | 18/32 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.561×** | -4.9 | 1e-04 | 15/30 (HS-578T, H4, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.598×** | -4.4 | 0.001 | 14/40 (PANC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.624×** | -4.0 | 0.005 | 9/34 (SNU-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7776. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 12.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0849× (z -9.2) |
| [[PANC-1 (line)]] | alt | 5.63 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -12.2) |
| [[HS-578T (line)]] | alt | 9.96 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0879× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 2.60 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0937× (z -11.9) |
| [[A-172 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.500 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.320 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.919 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7776), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH2D2A]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[LIMD2]] | +0.58 | +0.36 / +0.67 | both halves | 9e-05 |  |
| [[FSD1]] | +0.56 | +0.45 / +0.59 | both halves | 3e-05 | same gene group |
| [[C12orf56]] | +0.55 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[TMEM132A]] | +0.55 | +0.37 / +0.62 | both halves | 8e-05 |  |
| [[OCIAD2]] | +0.54 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[RPLP0P2]] | +0.54 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[ROBO4]] | +0.54 | +0.52 / +0.56 | both halves | 1e-05 | same gene group; STRING 413; ⚠ same locus (2.2 kb: neighbours can correlate without regulation) |
| [[PDZD4]] | +0.53 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[STX1A]] | +0.53 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[UPP1]] | +0.53 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[PNP]] | +0.52 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[ESYT3]] | +0.51 | +0.40 / +0.42 | both halves | 5e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMPK1]] | -0.45 | -0.21 / -0.55 | both halves | 7e-04 |  |
| [[PGM1]] | -0.43 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[NDUFS1]] | -0.43 | -0.28 / -0.40 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ROBO4]] | B | ROBO4 activity raises ROBO3's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.37× lower at baseline in the lines without ROBO4 | 0.005 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[RPLP0P2]] | B | RPLP0P2 activity lowers ROBO3's level | lines that do not express RPLP0P2 (7) vs lines expressing it (43) | 1.85× higher at baseline in the lines without RPLP0P2 | 0.022 | ⚠ within organs, on part of the lines; also absent: CAMK2N1, ETS2, CSTB; maybe low, not absent |
| [[F2RL2]] | B | F2RL2 activity raises ROBO3's level | lines that do not express F2RL2 (32) vs lines expressing it (18) | 2.21× lower at baseline in the lines without F2RL2 | 0.053 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA |
| [[CTSL]] | C | CTSL activity raises ROBO3's level | lines that do not express CTSL (9) vs lines expressing it (41) | 2.55× lower at baseline in the lines without CTSL | 0.055 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000286964, FRMD6, SYDE1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCCA-DT]] | B | ROBO3 activity lowers PCCA-DT's level | lines that do not express ROBO3 (8) vs lines expressing it (42) | 1.93× higher at baseline in the lines without ROBO3 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000232295, DYRK3, SCHIP1 |
| [[GLIPR2]] | B | ROBO3 activity raises GLIPR2's level | lines that do not express ROBO3 (8) vs lines expressing it (42) | 2.91× lower at baseline in the lines without ROBO3 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000232295, DYRK3, SCHIP1 |
| [[CSNK1E]] | B | ROBO3 activity raises CSNK1E's level | lines that do not express ROBO3 (8) vs lines expressing it (42) | 1.87× lower at baseline in the lines without ROBO3 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000232295, DYRK3, SCHIP1 |
| [[PLEKHG5]] | B | ROBO3 activity raises PLEKHG5's level | lines that do not express ROBO3 (8) vs lines expressing it (42) | 1.82× lower at baseline in the lines without ROBO3 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000232295, DYRK3, SCHIP1 |
| [[CTSL]] | C | ROBO3 activity raises CTSL's level | lines that do not express ROBO3 (8) vs lines expressing it (42) | 3.92× lower at baseline in the lines without ROBO3 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000232295, DYRK3, SCHIP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.373). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (53.0, -1.6); signed map (10.4, 55.9). **Vector** length 50.0, 8.04% of its response variance represented; |z| ≥ 3 in 668 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.1 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +9.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +3.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.8 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +1.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -7.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -7.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.7 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.6 | -6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.3 | -2.3 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | roundabout guidance receptor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:124,865,432-124,881,471 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RBIG1, FLJ21044, HGPS; previously HGPPS |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Roundabout guidance receptor family |
| Reactome | 6 pathways, smallest: ROBO receptors bind AKAP5; Regulation of commissural axon pathfinding by SLIT and ROBO; Regulation of expression of SLITs and ROBOs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MS0](https://www.uniprot.org/uniprotkb/Q96MS0) (Roundabout homolog 3):

> Receptor involved in axon guidance during development. Acts as a multifunctional regulator of pathfinding that simultaneously mediates NELL2 repulsion, inhibits SLIT repulsion, and facilitates Netrin-1/NTN1 attraction. In spinal cord development plays a role in guiding commissural axons probably by preventing premature sensitivity to Slit proteins thus inhibiting Slit signaling through ROBO1/ROBO2. Binding OF NELL2 to the receptor ROBO3 promotes oligomerization of ROBO3, resulting in the …

**Summary**, from NCBI Gene [64221](https://www.ncbi.nlm.nih.gov/gene/64221):

> This gene is a member of the Roundabout (ROBO) gene family that controls neurite outgrowth, growth cone guidance, and axon fasciculation. ROBO proteins are a subfamily of the immunoglobulin transmembrane receptor superfamily. SLIT proteins 1-3, a family of secreted chemorepellants, are ligands for ROBO proteins and SLIT/ROBO interactions regulate myogenesis, leukocyte migration, kidney morphogenesis, angiogenesis, and vasculogenesis in addition to neurogenesis. This gene, ROBO3, has a putative …

**Accessions** — [HGNC:13433](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13433) · Entrez [64221](https://www.ncbi.nlm.nih.gov/gene/64221) · UniProt [Q96MS0](https://www.uniprot.org/uniprotkb/Q96MS0) · Ensembl [ENSG00000154134](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154134)

## Data

Gene col 7776: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7776); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7776, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7776]; `tensor/DDL_lfc|DDL_z.npy` [7776]; `embed/gene_vectors.npy` [7776]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7776 or target_col == 7776). Every well: [[ROBO3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ROBO3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

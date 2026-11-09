---
symbol: "INHA"
type: "gene"
col: 4471
ensembl_id: "ENSG00000123999"
name: "inhibin subunit alpha"
location: "2q35"
module: 15
arm: "+"
pooled_cpm: 3.09
n_lines_expressing: 39
n_dd_up: 2
n_dd_down: 26
n_dd_up_clean: 1
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# INHA

*inhibin subunit alpha* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.39× (z +8.8, q 6e-16, up in 18 of 26 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 5.66×).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.225× (z -10.5, q 5e-23, down in 29 of 35 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PROCA1]] (+0.62, fdr 1e-05), [[ZSWIM5]] (+0.59, fdr 1e-05), [[DICER1-AS1]] (+0.58, fdr 6e-05); moves opposite to [[MYH14]] (-0.46, fdr 1e-04), [[TPCN2]] (-0.45, fdr 2e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KDM2B-DT]] → it (grade B ⚠); 10 go from it, the strongest it → [[ATP6V0D1-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4471.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 5.66×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.39×** | +8.8 | 6e-16 | 18/26 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +4.7 | 8e-04 | 3/13 (A-172, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.35× | +3.1 | 0.31 | 4/34 (LoVo, SW480, …) | top dose only | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.55× | +3.1 | 0.31 | 7/22 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4471.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.225×** | -10.5 | 5e-23 | 29/35 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.391×** | -9.3 | 3e-18 | 20/26 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.278×** | -9.0 | 4e-17 | 22/31 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.298×** | -8.5 | 3e-15 | 23/34 (Hs 766T, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.302×** | -8.4 | 4e-15 | 23/32 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.300×** | -8.1 | 4e-14 | 24/30 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.315×** | -8.1 | 4e-14 | 23/32 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.325×** | -7.9 | 2e-13 | 19/25 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.325×** | -7.5 | 6e-12 | 22/28 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.375×** | -6.9 | 3e-10 | 21/32 (C32, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.413×** | -6.2 | 3e-08 | 18/30 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.422×** | -6.1 | 7e-08 | 15/21 (SW480, C32, …) | all doses, flat | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.431×** | -5.9 | 2e-07 | 21/31 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.469×** | -5.3 | 5e-06 | 19/34 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.472×** | -5.3 | 6e-06 | 17/30 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.547×** | -4.2 | 9e-04 | 13/33 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4471. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 15.1 | 0 | 8 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0235× (z -14.0) |
| [[SW480 (line)]] | alt | 7.99 | 0 | 8 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0505× (z -15.2) |
| [[PANC-1 (line)]] | alt | 3.06 | 0 | 6 | — | [[Harringtonine (drug)]] 5 µM 0.0584× (z -10.6) |
| [[LoVo (line)]] | wt | 3.76 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0312× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 3.49 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0676× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 2.96 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0498× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0474× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 5.39 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0231× (z -12.4) |
| [[SW48 (line)]] | wt | 11.5 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0385× (z -10.2) |
| [[A-172 (line)]] | wt | 5.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -9.0) |
| [[A549 (line)]] | wt | 2.99 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0339× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 2.70 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -8.5) |
| [[Hs 766T (line)]] | wt | 2.74 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0272× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 4.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 5.84 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -10.0) |
| [[A-427 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.376 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.774 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.741 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.853 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.273 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.626 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4471), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PROCA1]] | +0.62 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ZSWIM5]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[DICER1-AS1]] | +0.58 | +0.39 / +0.56 | both halves | 6e-05 |  |
| [[NUDT13]] | +0.57 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[HOXA6]] | +0.56 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[PHC2-AS1]] | +0.56 | +0.43 / +0.54 | both halves | 4e-05 |  |
| [[CDNF]] | +0.55 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[TAGAP-AS1]] | +0.55 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[DDX59-AS1]] | +0.54 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[SOCS3-DT]] | +0.54 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[LINC02256]] | +0.54 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[LINC02269]] | +0.54 | +0.52 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYH14]] | -0.46 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[TPCN2]] | -0.45 | -0.30 / -0.34 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KDM2B-DT]] | B | KDM2B-DT activity raises INHA's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 2.16× lower at baseline in the lines without KDM2B-DT | 0.056 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[MIR1915HG]] | B | MIR1915HG activity raises INHA's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.71× lower at baseline in the lines without MIR1915HG | 0.087 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[OBSL1]] | C | OBSL1 activity raises INHA's level | lines that do not express OBSL1 (6) vs lines expressing it (44) | 2.72× lower at baseline in the lines without OBSL1 | 0.025 | ⚠ within organs, on part of the lines; also absent: PHC1, HECTD2, TPST1; co-absent with the target |
| [[CATSPER2P1]] | C | CATSPER2P1 activity raises INHA's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 2.07× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP6V0D1-DT]] | B | INHA activity raises ATP6V0D1-DT's level | lines that do not express INHA (11) vs lines expressing it (39) | 1.50× lower at baseline in the lines without INHA | 0.031 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13 |
| [[SCGB2B2]] | B | INHA activity raises SCGB2B2's level | lines that do not express INHA (11) vs lines expressing it (39) | 1.45× lower at baseline in the lines without INHA | 0.044 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13 |
| [[NIFK-AS1]] | B | INHA activity raises NIFK-AS1's level | lines that do not express INHA (11) vs lines expressing it (39) | 1.70× lower at baseline in the lines without INHA | 0.045 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13 |
| [[KAZALD1]] | B | INHA activity raises KAZALD1's level | lines that do not express INHA (11) vs lines expressing it (39) | 1.21× lower at baseline in the lines without INHA | 0.047 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13 |
| [[C1QTNF6]] | B | INHA activity strengthens C1QTNF6's drug response | lines that do not express INHA (11) vs lines expressing it (37) | the lines without INHA respond 0.56× as strongly (z diff +2.01); strongest at Homoharringtonine 0.5 µM: 0.70x vs 0.35x (z diff +3.7) | 0.050 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13; target measured in part of the lines; artifact flags |
| [[CRTC3-AS1]] | B | INHA activity raises CRTC3-AS1's level | lines that do not express INHA (11) vs lines expressing it (39) | 1.28× lower at baseline in the lines without INHA | 0.051 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13 |
| [[DPY19L2P3]] | B | INHA activity raises DPY19L2P3's level | lines that do not express INHA (11) vs lines expressing it (39) | 1.43× lower at baseline in the lines without INHA | 0.056 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13 |
| [[C1QTNF6]] | B | INHA activity raises C1QTNF6's level | lines that do not express INHA (11) vs lines expressing it (39) | 1.50× lower at baseline in the lines without INHA | 0.083 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13 |
| [[BRPF3-AS1]] | B | INHA activity raises BRPF3-AS1's level | lines that do not express INHA (11) vs lines expressing it (39) | 1.66× lower at baseline in the lines without INHA | 0.086 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13 |
| [[OBSL1]] | C | INHA activity raises OBSL1's level | lines that do not express INHA (11) vs lines expressing it (39) | 2.87× lower at baseline in the lines without INHA | 0.018 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13; co-absent with the target |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.493). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (3.9, 24.4); signed map (34.0, -6.0). **Vector** length 56.9, 10.7% of its response variance represented; |z| ≥ 3 in 851 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +8.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +1.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.0 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +0.9 | +3.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.9 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +0.8 | +2.4 |
|  | [[Ixazomib (drug)]] 5 µM |  | +0.7 | +0.8 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -2.7 | -10.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | -8.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.6 | -8.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.4 | -6.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -6.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | inhibin subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,569,162-219,575,711 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Inhibin subunits |
| Hallmark sets | HYPOXIA |
| Reactome | 8 pathways, smallest: Glycoprotein hormones; TGFBR3 regulates activin signaling; Peptide hormone biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P05111](https://www.uniprot.org/uniprotkb/P05111) (Inhibin alpha chain):

> Inhibins and activins inhibit and activate, respectively, the secretion of follitropin by the pituitary gland. Inhibins/activins are involved in regulating a number of diverse functions such as hypothalamic and pituitary hormone secretion, gonadal hormone secretion, germ cell development and maturation, erythroid differentiation, insulin secretion, nerve cell survival, embryonic axial development or bone growth, depending on their subunit composition. Inhibins appear to oppose the functions of …

**Summary**, from NCBI Gene [3623](https://www.ncbi.nlm.nih.gov/gene/3623):

> This gene encodes a member of the TGF-beta (transforming growth factor-beta) superfamily of proteins. The encoded preproprotein is proteolytically processed to generate multiple peptide products, including the alpha subunit of the inhibin A and B protein complexes. These complexes negatively regulate follicle stimulating hormone secretion from the pituitary gland. Inhibins have also been implicated in regulating numerous cellular processes including cell proliferation, apoptosis, immune …

**Accessions** — [HGNC:6065](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6065) · Entrez [3623](https://www.ncbi.nlm.nih.gov/gene/3623) · UniProt [P05111](https://www.uniprot.org/uniprotkb/P05111) · Ensembl [ENSG00000123999](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123999)

## Data

Gene col 4471: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4471); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4471, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4471]; `tensor/DDL_lfc|DDL_z.npy` [4471]; `embed/gene_vectors.npy` [4471]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4471 or target_col == 4471). Every well: [[INHA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INHA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

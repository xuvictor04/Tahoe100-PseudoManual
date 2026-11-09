---
symbol: "BCAM"
type: "gene"
col: 11905
ensembl_id: "ENSG00000187244"
name: "basal cell adhesion molecule (Lutheran blood group)"
location: "19q13.32"
module: 2
arm: "+"
pooled_cpm: 17.67
n_lines_expressing: 42
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 8
direction_downstream: 17
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# BCAM

*basal cell adhesion molecule (Lutheran blood group)* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.91× (z +14.8, q 0e+00, up in 36 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.575× (z -7.7, q 9e-12, down in 22 of 37 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A23]] (+0.70, fdr 1e-05), [[ABCA2]] (+0.65, fdr 2e-05), [[CLSTN1]] (+0.65, fdr 1e-05); moves opposite to [[C10orf88]] (-0.59, fdr 3e-05), [[PRR14L]] (-0.56, fdr 3e-05), [[ENOX2]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[COL18A1]] → it (grade B ⚠); 17 go from it, the strongest it → [[GUSB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11905.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.91×** | +14.8 | 0e+00 | 36/40 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.72×** | +13.8 | 5e-41 | 35/39 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.40×** | +12.1 | 2e-31 | 35/39 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +9.0 | 4e-17 | 18/24 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +8.6 | 1e-15 | 28/40 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +8.0 | 2e-13 | 31/40 (J82, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +7.3 | 2e-11 | 19/32 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +5.6 | 2e-06 | 14/26 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.04×** | +5.2 | 2e-05 | 22/39 (MIA PaCa-2, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +4.9 | 5e-05 | 17/37 (MIA PaCa-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +4.8 | 9e-05 | 18/37 (J82, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.014 | 14/40 (NCI-H2030, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.087 | 7/37 (A-427, HEC-1-A, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11905.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.575×** | -7.7 | 9e-12 | 22/37 (Panc 03.27, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.707×** | -4.6 | 0.001 | 18/38 (Panc 03.27, HOP62, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.724×** | -4.5 | 0.001 | 15/38 (NCI-H23, A498, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.727×** | -4.4 | 0.001 | 19/39 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.743×** | -4.1 | 0.004 | 18/38 (SW480, NCI-H460, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.609×** | -3.6 | 0.025 | 14/38 (A549, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.772×** | -3.6 | 0.025 | 11/38 (Panc 03.27, HT-29, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.640×** | -3.2 | 0.083 | 11/35 (SW1417, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.787×** | -3.2 | 0.083 | 9/38 (LS 180, AN3 CA, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11905. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 63.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +11.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 14.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.07× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.6 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.08× (z +8.5) | [[vincristine (drug)]] 0.5 µM 0.0517× (z -11.3) |
| [[HOP62 (line)]] | alt | 39.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.92× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 66.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.319× (z -8.6) |
| [[KATO III (line)]] | alt | 30.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 4.43 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.34× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 33.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0936× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -14.4) |
| [[SW480 (line)]] | alt | 21.9 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.96× (z +8.6) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -11.1) |
| [[BT-474 (line)]] | alt | 73.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -9.0) |
| [[HS-578T (line)]] | alt | 12.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.80× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 7.05 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM 0.0859× (z -9.3) |
| [[A-172 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11905), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A23]] | +0.70 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[ABCA2]] | +0.65 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[CLSTN1]] | +0.65 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[KCTD17]] | +0.65 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[HDAC1]] | +0.65 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[NCOR2]] | +0.65 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[ROGDI]] | +0.64 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[MAPK11]] | +0.64 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[CADM4]] | +0.63 | +0.42 / +0.54 | both halves | 4e-05 | same gene group |
| [[RAB3D]] | +0.63 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[FCHO1]] | +0.62 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[IL11RA]] | +0.61 | +0.57 / +0.59 | both halves | 9e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C10orf88]] | -0.59 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[PRR14L]] | -0.56 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[ENOX2]] | -0.56 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[TMEM267]] | -0.55 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[PAAF1]] | -0.55 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[YARS2]] | -0.54 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[KRIT1]] | -0.54 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[BMS1P4-1]] | -0.53 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[CCDC122]] | -0.53 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[NMNAT1]] | -0.53 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[MTG2]] | -0.53 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[MCPH1]] | -0.53 | -0.33 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL18A1]] | B | COL18A1 activity raises BCAM's level | lines that do not express COL18A1 (18) vs lines expressing it (32) | 1.85× lower at baseline in the lines without COL18A1 | 0.009 | ⚠ within organs, on part of the lines; also absent: NGFR, CX3CL1, PPP2R2B |
| [[CDC42BPG]] | B | CDC42BPG activity raises BCAM's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 2.14× lower at baseline in the lines without CDC42BPG | 0.029 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[CCDC120]] | B | CCDC120 activity raises BCAM's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 2.25× lower at baseline in the lines without CCDC120 | 0.052 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[KIAA1522]] | B | KIAA1522 activity raises BCAM's level | lines that do not express KIAA1522 (5) vs lines expressing it (45) | 3.18× lower at baseline in the lines without KIAA1522 | 0.073 | ⚠ across organs; also absent: ENSG00000257489, TRIB3, PBX4 |
| [[CD74]] | B | CD74 activity raises BCAM's level | lines that do not express CD74 (31) vs lines expressing it (19) | 1.46× lower at baseline in the lines without CD74 | 0.087 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers BCAM's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers BCAM's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TIMP2]] | C | TIMP2 activity raises BCAM's level | lines that do not express TIMP2 (4) vs lines expressing it (46) | 2.04× lower at baseline in the lines without TIMP2 | 0.050 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CNTNAP1, P3H1, RDX; maybe low, not absent |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GUSB]] | B | BCAM activity raises GUSB's level | lines that do not express BCAM (8) vs lines expressing it (42) | 1.49× lower at baseline in the lines without BCAM | 0.007 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[NIPSNAP1]] | B | BCAM activity raises NIPSNAP1's level | lines that do not express BCAM (8) vs lines expressing it (42) | 1.72× lower at baseline in the lines without BCAM | 0.015 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[PAFAH1B3]] | B | BCAM activity raises PAFAH1B3's level | lines that do not express BCAM (8) vs lines expressing it (42) | 1.73× lower at baseline in the lines without BCAM | 0.015 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[ABHD16A]] | B | BCAM activity raises ABHD16A's level | lines that do not express BCAM (8) vs lines expressing it (42) | 1.37× lower at baseline in the lines without BCAM | 0.018 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[THRA]] | B | BCAM activity raises THRA's level | lines that do not express BCAM (8) vs lines expressing it (42) | 1.63× lower at baseline in the lines without BCAM | 0.032 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[SEMA3F]] | B | BCAM activity raises SEMA3F's level | lines that do not express BCAM (8) vs lines expressing it (42) | 2.25× lower at baseline in the lines without BCAM | 0.054 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[ARRB2]] | B | BCAM activity raises ARRB2's level | lines that do not express BCAM (8) vs lines expressing it (42) | 1.94× lower at baseline in the lines without BCAM | 0.057 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[OLFML2A]] | B | BCAM activity raises OLFML2A's level | lines that do not express BCAM (8) vs lines expressing it (42) | 2.31× lower at baseline in the lines without BCAM | 0.058 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[TP53I11]] | B | BCAM activity raises TP53I11's level | lines that do not express BCAM (8) vs lines expressing it (42) | 2.56× lower at baseline in the lines without BCAM | 0.060 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[ANKDD1A]] | B | BCAM activity raises ANKDD1A's level | lines that do not express BCAM (8) vs lines expressing it (42) | 1.49× lower at baseline in the lines without BCAM | 0.063 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[LAMA5]] | B | BCAM activity raises LAMA5's level | lines that do not express BCAM (8) vs lines expressing it (42) | 3.23× lower at baseline in the lines without BCAM | 0.068 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[HMGN3]] | B | BCAM activity raises HMGN3's level | lines that do not express BCAM (8) vs lines expressing it (42) | 1.88× lower at baseline in the lines without BCAM | 0.070 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.434). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (11.2, -5.4); signed map (-10.8, 29.0). **Vector** length 80.1, 17.0% of its response variance represented; |z| ≥ 3 in 779 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +9.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.6 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +4.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +1.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +0.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -7.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -2.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | basal cell adhesion molecule (Lutheran blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:44,809,071-44,821,421 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD239, B-CAM, F8/G253; previously LU |
| Gene groups (HGNC) | Blood group antigens; CD molecules; V-set domain containing; C2-set domain containing; Ig-like cell adhesion molecule family |
| Hallmark sets | DNA_REPAIR, HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [P50895](https://www.uniprot.org/uniprotkb/P50895) (Basal cell adhesion molecule):

> Transmembrane glycoprotein that functions as both a receptor and an adhesion molecule playing a crucial role in cell adhesion, motility, migration and invasion. Extracellular domain enables binding to extracellular matrix proteins, such as laminin, integrin and other ligands while its intracellular domain interacts with cytoskeletal proteins like hemoglobin, facilitating cell signal transduction. Serves as a receptor for laminin alpha-5/LAMA5 to promote cell adhesion. Mechanistically, JAK2 …

**Summary**, from NCBI Gene [4059](https://www.ncbi.nlm.nih.gov/gene/4059):

> This gene encodes Lutheran blood group glycoprotein, a member of the immunoglobulin superfamily and a receptor for the extracellular matrix protein, laminin. The protein contains five extracellular immunoglobulin domains, a single transmembrane domain, and a short C-terminal cytoplasmic tail. This protein may play a role in epithelial cell cancer and in vaso-occlusion of red blood cells in sickle cell disease. Polymorphisms in this gene define some of the antigens in the Lutheran system and …

**Accessions** — [HGNC:6722](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6722) · Entrez [4059](https://www.ncbi.nlm.nih.gov/gene/4059) · UniProt [P50895](https://www.uniprot.org/uniprotkb/P50895) · Ensembl [ENSG00000187244](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187244)

## Data

Gene col 11905: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11905); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11905, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11905]; `tensor/DDL_lfc|DDL_z.npy` [11905]; `embed/gene_vectors.npy` [11905]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11905 or target_col == 11905). Every well: [[BCAM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCAM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

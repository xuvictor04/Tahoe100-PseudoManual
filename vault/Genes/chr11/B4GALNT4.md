---
symbol: "B4GALNT4"
type: "gene"
col: 11268
ensembl_id: "ENSG00000182272"
name: "beta-1,4-N-acetyl-galactosaminyltransferase 4"
location: "11p15.5"
module: 132
arm: "+"
pooled_cpm: 6.27
n_lines_expressing: 32
n_dd_up: 2
n_dd_down: 27
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 9
direction_downstream: 14
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# B4GALNT4

*beta-1,4-N-acetyl-galactosaminyltransferase 4* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.65× (z +5.3, q 6e-05, up in 11 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.28× (z +3.8, q 0.043, up in 9 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.299× (z -18.1, q 0e+00, down in 23 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRSK2]] (+0.68, fdr 7e-06), [[MAPK12]] (+0.65, fdr 7e-06), [[SEPTIN5]] (+0.65, fdr 1e-05); moves opposite to [[TRMT1L]] (-0.49, fdr 3e-05), [[RSPH3]] (-0.48, fdr 3e-05), [[STAMBP]] (-0.46, fdr 6e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 14 go from it, the strongest it → [[ST6GAL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11268.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +5.3 | 6e-05 | 11/17 (LS 180, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.043 | 9/30 (SNU-1, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.37× | +3.4 | 0.14 | 7/22 (BT-474, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.40× | +3.1 | 0.25 | 3/9 (LoVo, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.33× | +3.1 | 0.25 | 3/29 (LoVo, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.48× | +3.0 | 0.25 | 3/24 (SW480, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11268.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.299×** | -18.1 | 0e+00 | 23/26 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.271×** | -11.9 | 3e-30 | 24/28 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.353×** | -11.0 | 6e-26 | 21/25 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.365×** | -10.7 | 1e-24 | 21/28 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.408×** | -9.5 | 2e-19 | 23/29 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.468×** | -8.1 | 7e-14 | 21/29 (A-172, LoVo, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.521×** | -6.9 | 4e-10 | 22/29 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.567×** | -6.0 | 1e-07 | 16/29 (C32, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.574×** | -5.9 | 3e-07 | 17/28 (A498, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.603×** | -5.4 | 5e-06 | 14/29 (SW 900, A549, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.566×** | -5.2 | 1e-05 | 15/26 (PANC-1, A498, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.625×** | -5.0 | 3e-05 | 16/29 (NCI-H460, AN3 CA, …) | all doses, stronger at high dose | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.630×** | -4.9 | 5e-05 | 11/29 (LoVo, A-172, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.639×** | -4.7 | 8e-05 | 14/28 (HepG2/C3A, SNU-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.666×** | -4.3 | 6e-04 | 14/28 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.635×** | -4.1 | 0.001 | 13/27 (BT-474, A498, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.778×** | -3.7 | 0.006 | 14/30 (MIA PaCa-2, A-427, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.784×** | -3.6 | 0.009 | 11/29 (PANC-1, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.532×** | -3.5 | 0.012 | 7/26 (C32, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 5 µM |  | **0.799×** | -3.3 | 0.020 | 8/30 (SHP-77, SW480, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.748×** | -3.1 | 0.052 | 8/27 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.736×** | -3.0 | 0.061 | 5/25 (NCI-H460, A-172, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11268. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 20.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0909× (z -19.7) |
| [[A-172 (line)]] | wt | 24.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -14.8) |
| [[LS 180 (line)]] | wt | 14.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -17.6) |
| [[PANC-1 (line)]] | alt | 10.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -13.9) |
| [[HOP62 (line)]] | alt | 5.74 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -8.5) |
| [[LoVo (line)]] | wt | 14.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -17.4) |
| [[NCI-H2347 (line)]] | alt | 8.64 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 5.28 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -10.8) |
| [[RKO (line)]] | wt | 8.90 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0603× (z -9.7) |
| [[SW480 (line)]] | alt | 4.83 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -11.9) |
| [[A-427 (line)]] | wt | 13.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -10.7) |
| [[A549 (line)]] | wt | 6.00 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -8.6) |
| [[BT-474 (line)]] | alt | 8.25 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -8.7) |
| [[C32 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -9.0) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H2030 (line)]] | alt | 4.13 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -9.9) |
| [[A498 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.680 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.698 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11268), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRSK2]] | +0.68 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[MAPK12]] | +0.65 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[SEPTIN5]] | +0.65 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[KLHL17]] | +0.65 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[PGGHG]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 | STRING 707 |
| [[SHANK3]] | +0.60 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[GNAZ]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[PDZD4]] | +0.59 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ANO8]] | +0.57 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[TBX1]] | +0.57 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ZDHHC8]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ABCA2]] | +0.56 | +0.54 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT1L]] | -0.49 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[RSPH3]] | -0.48 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[STAMBP]] | -0.46 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[NIPBL]] | -0.45 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises B4GALNT4's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[AIF1L]] | B | AIF1L activity raises B4GALNT4's level | lines that do not express AIF1L (12) vs lines expressing it (38) | 2.11× lower at baseline in the lines without AIF1L | 0.057 | ⚠ within organs, on part of the lines; also absent: FAM169A, NUP210, PRR36; maybe low, not absent |
| [[JAG2]] | B | JAG2 activity raises B4GALNT4's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.75× lower at baseline in the lines without JAG2 | 0.073 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[SEPTIN3]] | B | SEPTIN3 activity raises B4GALNT4's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 2.52× lower at baseline in the lines without SEPTIN3 | 0.091 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[CHD5]] | C | CHD5 activity raises B4GALNT4's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 2.32× lower at baseline in the lines without CHD5 | 0.002 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent; co-absent with the target |
| [[ST6GAL1]] | C | ST6GAL1 activity raises B4GALNT4's level | lines that do not express ST6GAL1 (14) vs lines expressing it (36) | 3.75× lower at baseline in the lines without ST6GAL1 | 0.003 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent; co-absent with the target |
| [[KIF26A]] | C | KIF26A activity raises B4GALNT4's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 3.23× lower at baseline in the lines without KIF26A | 0.020 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN; co-absent with the target |
| [[MSI1]] | C | MSI1 activity raises B4GALNT4's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.35× lower at baseline in the lines without MSI1 | 0.035 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B; co-absent with the target |
| [[ADGRB1]] | C | ADGRB1 activity raises B4GALNT4's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 2.58× lower at baseline in the lines without ADGRB1 | 0.038 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 8, C 6. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST6GAL1]] | B | B4GALNT4 activity strengthens ST6GAL1's drug response | lines that do not express B4GALNT4 (6) vs lines expressing it (28) | the lines without B4GALNT4 respond 0.43× as strongly (z diff +3.70); strongest at Homoharringtonine 0.5 µM: 0.68x vs 0.16x (z diff +6.1) | 0.002 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A; target measured in part of the lines; artifact flags |
| [[SHANK3]] | B | B4GALNT4 activity raises SHANK3's level | lines that do not express B4GALNT4 (18) vs lines expressing it (32) | 1.80× lower at baseline in the lines without B4GALNT4 | 0.030 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A |
| [[AKT1]] | B | B4GALNT4 activity raises AKT1's level | lines that do not express B4GALNT4 (18) vs lines expressing it (32) | 1.21× lower at baseline in the lines without B4GALNT4 | 0.036 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A |
| [[SMO]] | B | B4GALNT4 activity strengthens SMO's drug response | lines that do not express B4GALNT4 (8) vs lines expressing it (23) | the lines without B4GALNT4 respond 0.54× as strongly (z diff +2.12); strongest at Homoharringtonine 5 µM: 0.61x vs 0.34x (z diff +4.1) | 0.056 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A; target measured in part of the lines; artifact flags |
| [[MAPK12]] | B | B4GALNT4 activity strengthens MAPK12's drug response | lines that do not express B4GALNT4 (17) vs lines expressing it (29) | the lines without B4GALNT4 respond 0.67× as strongly (z diff +1.25); strongest at Belinostat 5 µM: 0.66x vs 0.42x (z diff +2.2) | 0.068 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A; target measured in part of the lines; artifact flags |
| [[SEPTIN3]] | B | B4GALNT4 activity raises SEPTIN3's level | lines that do not express B4GALNT4 (18) vs lines expressing it (32) | 2.04× lower at baseline in the lines without B4GALNT4 | 0.079 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A |
| [[CGREF1]] | B | B4GALNT4 activity raises CGREF1's level | lines that do not express B4GALNT4 (18) vs lines expressing it (32) | 1.60× lower at baseline in the lines without B4GALNT4 | 0.082 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A |
| [[GNAZ]] | B | B4GALNT4 activity raises GNAZ's level | lines that do not express B4GALNT4 (18) vs lines expressing it (32) | 1.77× lower at baseline in the lines without B4GALNT4 | 0.090 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A |
| [[ST6GAL1]] | C | B4GALNT4 activity raises ST6GAL1's level | lines that do not express B4GALNT4 (18) vs lines expressing it (32) | 4.34× lower at baseline in the lines without B4GALNT4 | 0.004 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A; co-absent with the target |
| [[KIF26A]] | C | B4GALNT4 activity raises KIF26A's level | lines that do not express B4GALNT4 (18) vs lines expressing it (32) | 2.79× lower at baseline in the lines without B4GALNT4 | 0.016 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A; co-absent with the target |
| [[PDZD4]] | C | B4GALNT4 activity raises PDZD4's level | lines that do not express B4GALNT4 (18) vs lines expressing it (32) | 2.43× lower at baseline in the lines without B4GALNT4 | 0.065 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A; co-absent with the target |
| [[CHD5]] | C | B4GALNT4 activity raises CHD5's level | lines that do not express B4GALNT4 (18) vs lines expressing it (32) | 2.04× lower at baseline in the lines without B4GALNT4 | 0.087 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A; co-absent with the target |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.645). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.1, 41.1); signed map (-27.2, -0.5). **Vector** length 55.8, 11.2% of its response variance represented; |z| ≥ 3 in 644 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | -0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.3 | +0.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.2 | +2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.1 | +1.1 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.0 | +1.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.0 | -10.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.0 | -11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -11.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.6 | -5.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | beta-1,4-N-acetyl-galactosaminyltransferase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:369,499-382,117 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25045, NGalNAc-T1 |
| Gene groups (HGNC) | Beta 4-glycosyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q76KP1](https://www.uniprot.org/uniprotkb/Q76KP1) (N-acetyl-beta-glucosaminyl-glycoprotein 4-beta-N-acetylgalactosaminyltransferase 1):

> Transfers N-acetylgalactosamine (GalNAc) from UDP-GalNAc to N-acetylglucosamine-beta-benzyl with a beta-1,4-linkage to form N,N'-diacetyllactosediamine, GalNAc-beta-1,4-GlcNAc structures in N-linked glycans and probably O-linked glycans.

**Summary**, from NCBI Gene [338707](https://www.ncbi.nlm.nih.gov/gene/338707):

> Enables acetylgalactosaminyltransferase activity. Predicted to be located in Golgi cisterna membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26315](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26315) · Entrez [338707](https://www.ncbi.nlm.nih.gov/gene/338707) · UniProt [Q76KP1](https://www.uniprot.org/uniprotkb/Q76KP1) · Ensembl [ENSG00000182272](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182272)

## Data

Gene col 11268: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11268); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11268, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11268]; `tensor/DDL_lfc|DDL_z.npy` [11268]; `embed/gene_vectors.npy` [11268]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11268 or target_col == 11268). Every well: [[B4GALNT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B4GALNT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

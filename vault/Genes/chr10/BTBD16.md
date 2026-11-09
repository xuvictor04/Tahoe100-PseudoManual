---
symbol: "BTBD16"
type: "gene"
col: 6133
ensembl_id: "ENSG00000138152"
name: "BTB domain containing 16"
location: "10q26.13"
module: 47
arm: "+"
pooled_cpm: 5.87
n_lines_expressing: 39
n_dd_up: 15
n_dd_down: 16
n_dd_up_clean: 10
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 6
direction_downstream: 5
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# BTBD16

*BTB domain containing 16* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.10× (z +16.2, q 0e+00, up in 22 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.407× (z -9.2, q 2e-17, down in 20 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.434× (z -8.5, q 4e-15, down in 18 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC2A9]] (+0.75, fdr 7e-06), [[BCAR3-AS1]] (+0.69, fdr 7e-06), [[FBXW10B]] (+0.66, fdr 1e-05); moves opposite to [[FLYWCH2]] (-0.55, fdr 2e-04).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[NDUFA4L2]] → it (grade B ⚠); 5 go from it, the strongest it → [[RAB11FIP4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6133.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.10×** | +16.2 | 0e+00 | 22/28 (NCI-H460, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.57×** | +13.5 | 4e-39 | 19/30 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.52×** | +9.0 | 4e-17 | 3/6 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.24×** | +7.7 | 2e-12 | 21/33 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.91×** | +6.5 | 8e-09 | 20/36 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +5.3 | 1e-05 | 2/7 (AsPC-1, HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +4.6 | 4e-04 | 6/26 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.60×** | +4.5 | 5e-04 | 9/33 (SW 900, LS 180, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +4.5 | 5e-04 | 2/16 (CFPAC-1, A549) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +4.4 | 7e-04 | 12/32 (NCI-H460, LoVo, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +4.2 | 0.001 | 5/23 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brimonidine (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.007 | 3/31 (CFPAC-1, COLO 205, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.032 | 2/27 (HOP62, AsPC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.26×** | +3.3 | 0.037 | 6/36 (AsPC-1, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.063 | 5/36 (HepG2/C3A, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6133.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.407×** | -9.2 | 2e-17 | 20/25 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.434×** | -8.5 | 4e-15 | 18/33 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.470×** | -7.7 | 2e-12 | 18/36 (HT-29, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.494×** | -7.2 | 7e-11 | 23/36 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.504×** | -7.0 | 2e-10 | 19/36 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.565×** | -5.9 | 4e-07 | 18/34 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.566×** | -5.8 | 4e-07 | 19/36 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.605×** | -5.0 | 5e-05 | 14/32 (KATO III, SW480, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.422×** | -4.6 | 2e-04 | 15/31 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.689×** | -3.8 | 0.007 | 15/29 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.698×** | -3.7 | 0.011 | 10/36 (SW 900, A549, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.545×** | -3.3 | 0.053 | 2/34 (HEC-1-A, HepG2/C3A) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pimitespib (drug)]] 0.05 µM |  | **0.725×** | -3.1 | 0.066 | 3/35 (A-427, HCT15, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.730×** | -3.1 | 0.066 | 12/17 (KATO III, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Fumaric acid (drug)]] 5 µM |  | **0.730×** | -3.1 | 0.066 | 3/36 (NCI-H1573, SW48, …) | top dose only | plate-row cell shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.662×** | -3.0 | 0.085 | 5/36 (KATO III, SW 1271, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6133. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 41.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -14.7) |
| [[SW480 (line)]] | alt | 14.6 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.102× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 36.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -10.5) |
| [[HT-29 (line)]] | alt | 8.84 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0499× (z -12.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 6.24 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -9.3) |
| [[PANC-1 (line)]] | alt | 5.94 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0887× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.150× (z -8.6) |
| [[SHP-77 (line)]] | alt | 8.40 | 0 | 2 (1 ⚠) | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0473× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 3.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.21× (z +10.9) | — |
| [[A-172 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.878 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6133), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC2A9]] | +0.75 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[BCAR3-AS1]] | +0.69 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[FBXW10B]] | +0.66 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[CCDC162P]] | +0.65 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[LINC00486]] | +0.65 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[AXDND1]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[C19orf38]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[STPG4]] | +0.64 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[HGD]] | +0.64 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[MTNR1A]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[DPYS]] | +0.64 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[PARD6G-AS1]] | +0.63 | +0.61 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLYWCH2]] | -0.55 | -0.50 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDUFA4L2]] | B | NDUFA4L2 activity raises BTBD16's level | lines that do not express NDUFA4L2 (16) vs lines expressing it (34) | 2.21× lower at baseline in the lines without NDUFA4L2 | 0.003 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers BTBD16's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DSCAML1]] | B | DSCAML1 activity strengthens BTBD16's drug response | lines that do not express DSCAML1 (29) vs lines expressing it (7) | the lines without DSCAML1 respond 0.92× as strongly (z diff +0.24); strongest at Ouabain (Octahydrate) 5 µM: 0.49x vs 0.22x (z diff +4.1) | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG; target measured in part of the lines; both ways; artifact flags |
| [[DSCAML1]] | B | DSCAML1 activity raises BTBD16's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 1.54× lower at baseline in the lines without DSCAML1 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[CFAP161]] | B | CFAP161 activity raises BTBD16's level | lines that do not express CFAP161 (6) vs lines expressing it (44) | 1.42× lower at baseline in the lines without CFAP161 | 0.089 | ⚠ within organs, on part of the lines; also absent: CRB1; maybe low, not absent; its own permutation p |
| [[GARIN1B]] | C | GARIN1B activity lowers BTBD16's level | lines that do not express GARIN1B (4) vs lines expressing it (46) | 2.04× higher at baseline in the lines without GARIN1B | 0.077 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PGGHG, ALPK1; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB11FIP4]] | B | BTBD16 activity lowers RAB11FIP4's level | lines that do not express BTBD16 (11) vs lines expressing it (39) | 1.02× higher at baseline in the lines without BTBD16 | 0.065 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TTC39A]] | B | BTBD16 activity lowers TTC39A's level | lines that do not express BTBD16 (11) vs lines expressing it (39) | 1.08× higher at baseline in the lines without BTBD16 | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HPN]] | B | BTBD16 activity lowers HPN's level | lines that do not express BTBD16 (11) vs lines expressing it (39) | 1.21× higher at baseline in the lines without BTBD16 | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[KCNQ4]] | B | BTBD16 activity lowers KCNQ4's level | lines that do not express BTBD16 (11) vs lines expressing it (39) | 1.11× higher at baseline in the lines without BTBD16 | 0.092 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PLB1]] | B | BTBD16 activity lowers PLB1's level | lines that do not express BTBD16 (11) vs lines expressing it (39) | 1.17× higher at baseline in the lines without BTBD16 | 0.097 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.7, -9.5); signed map (57.8, 13.5). **Vector** length 62.8, 10.7% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +13.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +16.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +4.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +6.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +7.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.0 | -7.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | -7.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -8.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.3 | -7.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.9 | -5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -3.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | BTB domain containing 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:122,271,296-122,338,159 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25359, Em:AC061711.1; previously C10orf87 |
| Gene groups (HGNC) | BTB domain containing |
| Matched by | ensembl_id |

UniProt [Q32M84](https://www.uniprot.org/uniprotkb/Q32M84) carries no function annotation.

**Summary**, from NCBI Gene [118663](https://www.ncbi.nlm.nih.gov/gene/118663):

> This gene encodes a protein that contains a BTB/POZ domain. This domain mediates protein-protein interactions. A mutation in this gene may be associated with bipolar disorder. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:26340](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26340) · Entrez [118663](https://www.ncbi.nlm.nih.gov/gene/118663) · UniProt [Q32M84](https://www.uniprot.org/uniprotkb/Q32M84) · Ensembl [ENSG00000138152](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138152)

## Data

Gene col 6133: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6133); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6133, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6133]; `tensor/DDL_lfc|DDL_z.npy` [6133]; `embed/gene_vectors.npy` [6133]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6133 or target_col == 6133). Every well: [[BTBD16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTBD16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

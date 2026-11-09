---
symbol: "ST6GALNAC2"
type: "gene"
col: 961
ensembl_id: "ENSG00000070731"
name: "ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 2"
location: "17q25.1"
module: 128
arm: "+"
pooled_cpm: 3.12
n_lines_expressing: 42
n_dd_up: 7
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 9
direction_downstream: 5
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# ST6GALNAC2

*ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 2* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.70× (z +13.1, q 2e-36, up in 2 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.59× (z +4.6, q 8e-04, up in 9 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.552× (z -8.8, q 1e-15, down in 21 of 27 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.496× (z -7.0, q 5e-10, down in 21 of 33 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMO7-AS1]] (+0.54, fdr 4e-05), [[B3GNT7]] (+0.54, fdr 2e-05), [[MDGA1]] (+0.50, fdr 3e-05); moves opposite to [[LINC01473]] (-0.46, fdr 1e-04), [[BABAM2]] (-0.43, fdr 7e-05), [[PDE4D]] (-0.43, fdr 5e-05).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[HES2]] → it (grade B ⚠); 5 go from it, the strongest it → [[HES2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 961.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.70×** | +13.1 | 2e-36 | 2/6 (BT-474, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +4.9 | 3e-04 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.59×** | +4.6 | 8e-04 | 9/28 (C32, SNU-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.5 | 1e-03 | 2/17 (SK-MEL-2, BT-474) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +4.1 | 0.004 | 2/12 (A498, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.8 | 0.016 | 2/26 (SK-MEL-2, SNU-1) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +3.3 | 0.068 | 2/15 (Panc 03.27, SW1417) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 1.23× | +3.0 | 0.16 | 2/35 (KATO III, A549) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.74× | +3.0 | 0.16 | 0/5 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 961.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.552×** | -8.8 | 1e-15 | 21/27 (BT-474, NCI-H2347, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.496×** | -7.0 | 5e-10 | 21/33 (A549, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.516×** | -6.9 | 1e-09 | 22/32 (LoVo, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.536×** | -6.5 | 1e-08 | 20/35 (SK-MEL-2, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.542×** | -6.4 | 2e-08 | 17/26 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.556×** | -6.1 | 9e-08 | 19/36 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.570×** | -5.9 | 4e-07 | 18/34 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.604×** | -5.3 | 1e-05 | 17/32 (BT-474, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.610×** | -5.2 | 2e-05 | 17/36 (Hs 766T, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.649×** | -4.5 | 4e-04 | 11/36 (SK-MEL-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.700×** | -3.7 | 0.009 | 11/32 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Fumaric acid (drug)]] 5 µM |  | **0.690×** | -3.7 | 0.009 | 6/37 (HepG2/C3A, SW1417, …) | top dose only | plate-row cell shift |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.699×** | -3.6 | 0.014 | 5/36 (A549, NCI-H23, …) | top dose only | plate-row cell shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.716×** | -3.5 | 0.020 | 13/33 (HOP62, PANC-1, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.815×** | -3.0 | 0.091 | 11/34 (BT-474, SNU-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 961. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 4.36 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0334× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.151× (z -9.4) |
| [[BT-474 (line)]] | alt | 14.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -13.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 6.82 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0294× (z -14.3) ⚠ cell-cycle shift, explains ~94% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.111× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 6.72 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0457× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 3.07 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0506× (z -11.2) |
| [[A549 (line)]] | wt | 2.15 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0666× (z -10.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 7.91 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -9.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Hs 766T (line)]] | wt | 9.85 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0512× (z -10.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[LoVo (line)]] | wt | 2.96 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0443× (z -10.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H2347 (line)]] | alt | 6.35 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -10.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-1 (line)]] | wt | 5.95 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 5 µM 0.0426× (z -8.7) |
| [[SNU-423 (line)]] | alt | 2.56 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0457× (z -8.6) |
| [[A-172 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.661 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.783 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.823 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.922 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.658 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.586 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.506 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.714 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.516 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 961), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 10 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMO7-AS1]] | +0.54 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[B3GNT7]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 | pathway: O-linked glycosylation |
| [[MDGA1]] | +0.50 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[HES2]] | +0.50 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[BMP1]] | +0.49 | +0.39 / +0.46 | both halves | 6e-05 |  |
| [[EBF4]] | +0.48 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[SYT17]] | +0.46 | +0.40 / +0.40 | both halves | 5e-05 |  |
| [[CYS1]] | +0.45 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[KCNC4]] | +0.44 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[CAPN1-AS1]] | +0.44 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[LURAP1]] | +0.44 | +0.42 / +0.33 | both halves | 1e-04 |  |
| [[FBLN7]] | +0.43 | +0.39 / +0.46 | both halves | 5e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01473]] | -0.46 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[BABAM2]] | -0.43 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[PDE4D]] | -0.43 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[RAD51B]] | -0.43 | -0.29 / -0.45 | both halves | 3e-04 |  |
| [[FHIT]] | -0.43 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[TBC1D32]] | -0.42 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[TBCK]] | -0.42 | -0.37 / -0.50 | both halves | 7e-05 |  |
| [[PRELID2]] | -0.41 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[INTS13]] | -0.40 | -0.29 / -0.41 | both halves | 3e-04 |  |
| [[PRKN]] | -0.39 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[SPTLC3]] | -0.39 | -0.39 / -0.37 | both halves | 9e-05 |  |
| [[ROBO2]] | -0.39 | -0.38 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES2]] | B | HES2 activity raises ST6GALNAC2's level | lines that do not express HES2 (20) vs lines expressing it (30) | 1.59× lower at baseline in the lines without HES2 | 0.021 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[EFCAB13]] | B | EFCAB13 activity raises ST6GALNAC2's level | lines that do not express EFCAB13 (14) vs lines expressing it (36) | 1.58× lower at baseline in the lines without EFCAB13 | 0.032 | ⚠ within organs, on part of the lines; also absent: KCNS3, TRIM6, GPR176; maybe low, not absent |
| [[TBX1]] | B | TBX1 activity raises ST6GALNAC2's level | lines that do not express TBX1 (23) vs lines expressing it (27) | 1.26× lower at baseline in the lines without TBX1 | 0.042 | ⚠ within organs, on part of the lines; also absent: BEGAIN, PALM, OLFM1 |
| [[B3GNT7]] | B | B3GNT7 activity raises ST6GALNAC2's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 1.84× lower at baseline in the lines without B3GNT7 | 0.060 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2 |
| [[PDE4D]] | B | PDE4D activity lowers ST6GALNAC2's level | lines that do not express PDE4D (13) vs lines expressing it (37) | 1.49× higher at baseline in the lines without PDE4D | 0.061 | ⚠ within organs, on part of the lines; also absent: RGS2, LINC02269; maybe low, not absent |
| [[PROSER2]] | B | PROSER2 activity raises ST6GALNAC2's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 1.40× lower at baseline in the lines without PROSER2 | 0.062 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |
| [[MDGA1]] | B | MDGA1 activity raises ST6GALNAC2's level | lines that do not express MDGA1 (13) vs lines expressing it (37) | 1.37× lower at baseline in the lines without MDGA1 | 0.070 | ⚠ within organs, on part of the lines; also absent: TCF7L1, ZNF470, FBXL2 |
| [[ZNF665]] | B | ZNF665 activity raises ST6GALNAC2's level | lines that do not express ZNF665 (24) vs lines expressing it (26) | 1.44× lower at baseline in the lines without ZNF665 | 0.078 | ⚠ within organs, on part of the lines; also absent: ZNF93, ZNF818P, ZNF347 |
| [[CELSR1]] | C | CELSR1 activity raises ST6GALNAC2's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 2.10× lower at baseline in the lines without CELSR1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES2]] | B | ST6GALNAC2 activity raises HES2's level | lines that do not express ST6GALNAC2 (8) vs lines expressing it (42) | 1.80× lower at baseline in the lines without ST6GALNAC2 | 0.020 | ⚠ within organs, on part of the lines; also absent: CELSR1, CTSD, TRIM47; maybe low, not absent |
| [[BABAM2]] | B | ST6GALNAC2 activity raises BABAM2's level | lines that do not express ST6GALNAC2 (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without ST6GALNAC2 | 0.083 | ⚠ within organs, on part of the lines; also absent: CELSR1, CTSD, TRIM47; maybe low, not absent |
| [[B3GNT7]] | B | ST6GALNAC2 activity raises B3GNT7's level | lines that do not express ST6GALNAC2 (8) vs lines expressing it (42) | 1.85× lower at baseline in the lines without ST6GALNAC2 | 0.088 | ⚠ within organs, on part of the lines; also absent: CELSR1, CTSD, TRIM47; maybe low, not absent |
| [[PLEKHN1]] | B | ST6GALNAC2 activity raises PLEKHN1's level | lines that do not express ST6GALNAC2 (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without ST6GALNAC2 | 0.089 | ⚠ within organs, on part of the lines; also absent: CELSR1, CTSD, TRIM47; maybe low, not absent |
| [[CELSR1]] | C | ST6GALNAC2 activity raises CELSR1's level | lines that do not express ST6GALNAC2 (8) vs lines expressing it (42) | 3.17× lower at baseline in the lines without ST6GALNAC2 | 0.007 | ⚠ within organs, on part of the lines; also absent: CELSR1, CTSD, TRIM47; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.270). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.9, 47.8); signed map (23.3, 22.0). **Vector** length 53.1, 8.52% of its response variance represented; |z| ≥ 3 in 844 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +4.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.5 | +2.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.4 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +2.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.1 | +3.0 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.1 | +2.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -1.9 | -5.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.7 | -7.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.5 | -5.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.0 | -3.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -1.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.0 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:76,565,377-76,586,956 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ST6GalNAII, STHM; previously SIAT7, SIAT7B, SIATL1 |
| Gene groups (HGNC) | Sialyltransferases |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 17 pathways, smallest: Maturation of protein 3a_9683673; Maturation of protein 3a_9694719; Termination of O-glycan biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJ37](https://www.uniprot.org/uniprotkb/Q9UJ37) (Alpha-N-acetylgalactosaminide alpha-2,6-sialyltransferase 2):

> Catalyzes the transfer of N-acetylneuraminyl groups onto glycan chains in glycoproteins. Conjugates sialic acid with an alpha-2-6 linkage to N-acetylgalactosamine (GalNAc) glycan chains linked to serine or threonine in glycoproteins. Sialylates alphaGalNAc- and Galbeta1->3GalNAc-O-Ser/Thr epitopes also known as Tn and T antigens.

**Summary**, from NCBI Gene [10610](https://www.ncbi.nlm.nih.gov/gene/10610):

> ST6GALNAC2 belongs to a family of sialyltransferases that add sialic acids to the nonreducing ends of glycoconjugates. At the cell surface, these modifications have roles in cell-cell and cell-substrate interactions, bacterial adhesion, and protein targeting (Samyn-Petit et al., 2000 [PubMed 10742600]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:10867](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10867) · Entrez [10610](https://www.ncbi.nlm.nih.gov/gene/10610) · UniProt [Q9UJ37](https://www.uniprot.org/uniprotkb/Q9UJ37) · Ensembl [ENSG00000070731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070731)

## Data

Gene col 961: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 961); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 961, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 961]; `tensor/DDL_lfc|DDL_z.npy` [961]; `embed/gene_vectors.npy` [961]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 961 or target_col == 961). Every well: [[ST6GALNAC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST6GALNAC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

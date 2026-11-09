---
symbol: "HS3ST3B1"
type: "gene"
col: 4612
ensembl_id: "ENSG00000125430"
name: "heparan sulfate-glucosamine 3-sulfotransferase 3B1"
location: "17p12"
module: 104
arm: "+"
pooled_cpm: 12.84
n_lines_expressing: 32
n_dd_up: 33
n_dd_down: 11
n_dd_up_clean: 27
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 16
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# HS3ST3B1

*heparan sulfate-glucosamine 3-sulfotransferase 3B1* — 17p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.16× (z +14.0, q 1e-41, up in 19 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.502× (z -8.5, q 1e-14, down in 13 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.672× (z -5.1, q 7e-05, down in 12 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAMTS9]] (+0.74, fdr 7e-06), [[ZMYND8]] (+0.65, fdr 1e-05), [[MT1X]] (+0.65, fdr 7e-06); moves opposite to [[SIRLNT]] (-0.51, fdr 1e-05), [[BBOX1-AS1]] (-0.48, fdr 2e-04).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SLC7A2]] → it (grade B ⚠); 16 go from it, the strongest it → [[HIPK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4612.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +14.0 | 1e-41 | 19/27 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.02×** | +9.1 | 4e-17 | 22/30 (NCI-H460, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +8.6 | 2e-15 | 17/29 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.95×** | +8.6 | 2e-15 | 17/29 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.94×** | +8.5 | 2e-15 | 18/30 (NCI-H23, HOP62, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.87×** | +7.7 | 9e-13 | 19/29 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.82×** | +7.7 | 9e-13 | 16/28 (NCI-H460, LOX-IMVI, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.75×** | +7.2 | 4e-11 | 14/26 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.74×** | +7.1 | 6e-11 | 15/28 (NCI-H460, SW 900, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +6.9 | 3e-10 | 19/30 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.78×** | +6.9 | 3e-10 | 15/28 (H4, LOX-IMVI, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.65×** | +6.5 | 4e-09 | 13/29 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Econazole (drug)]] 5 µM |  | **1.64×** | +6.3 | 1e-08 | 14/30 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +6.3 | 2e-08 | 12/30 (SW480, HS-578T, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.53×** | +5.4 | 2e-06 | 13/30 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.50×** | +5.2 | 7e-06 | 14/29 (NCI-H460, H4, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.49×** | +5.2 | 8e-06 | 13/29 (H4, NCI-H460, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.13×** | +5.1 | 1e-05 | 16/28 (LOX-IMVI, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4612.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.502×** | -8.5 | 1e-14 | 13/18 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.591×** | -6.7 | 5e-09 | 16/23 (SW 900, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.672×** | -5.1 | 7e-05 | 12/30 (SW 900, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.700×** | -4.2 | 0.003 | 14/23 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.744×** | -3.8 | 0.017 | 10/28 (NCI-H1573, A498, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.729×** | -3.7 | 0.017 | 9/30 (C32, BT-474, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.763×** | -3.5 | 0.044 | 7/29 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.766×** | -3.4 | 0.045 | 9/27 (NCI-H1573, A549, …) | two highest doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.768×** | -3.4 | 0.046 | 11/29 (HS-578T, NCI-H1792, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.769×** | -3.2 | 0.069 | 11/28 (HepG2/C3A, HOP62, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.778×** | -3.2 | 0.069 | 13/29 (SW 900, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.840× | -3.1 | 0.080 | 13/30 (BT-474, SW 900, …) | top dose only | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4612. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 24.1 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 32.9 | 2 (1 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 3.46× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.0981× (z -16.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 48.2 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0776× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0976× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 20.5 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.107× (z -17.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 8.41 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +8.9) | [[Entrectinib (drug)]] 5 µM 0.0381× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 82.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -20.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 19.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.188× (z -8.8) |
| [[C32 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -9.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 27.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[HS-578T (line)]] | alt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 21.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +8.7) | — |
| [[J82 (line)]] | alt | 8.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +8.5) | — |
| [[LoVo (line)]] | wt | 8.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.39× (z +12.1) | — |
| [[SNU-1 (line)]] | wt | 9.42 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0690× (z -8.9) |
| [[SW480 (line)]] | alt | 12.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +11.2) | — |
| [[A-427 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.66 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4612), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS9]] | +0.74 | +0.72 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[ZMYND8]] | +0.65 | +0.52 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[MT1X]] | +0.65 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[DNER]] | +0.64 | +0.68 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[MAP3K5]] | +0.64 | +0.51 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[TLR2]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[IRAK3]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[IRX3]] | +0.62 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[B3GNT5]] | +0.61 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[MT2A]] | +0.61 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[ANGPTL4]] | +0.61 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[SAA1]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRLNT]] | -0.51 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[BBOX1-AS1]] | -0.48 | -0.30 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC7A2]] | B | SLC7A2 activity raises HS3ST3B1's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 2.29× lower at baseline in the lines without SLC7A2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D |
| [[PID1]] | B | PID1 activity raises HS3ST3B1's level | lines that do not express PID1 (22) vs lines expressing it (28) | 2.72× lower at baseline in the lines without PID1 | 0.041 | ⚠ within organs, on part of the lines; also absent: TRPA1, DOCK10, ENSG00000289600 |
| [[ITGA10]] | B | ITGA10 activity raises HS3ST3B1's level | lines that do not express ITGA10 (9) vs lines expressing it (41) | 3.02× lower at baseline in the lines without ITGA10 | 0.047 | ⚠ within organs, on part of the lines; also absent: SLC17A7, ZEB1, BOLA3-DT; maybe low, not absent |
| [[ADAMTS9]] | B | ADAMTS9 activity raises HS3ST3B1's level | lines that do not express ADAMTS9 (18) vs lines expressing it (32) | 2.96× lower at baseline in the lines without ADAMTS9 | 0.056 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2 |
| [[NR3C1]] | B | NR3C1 activity raises HS3ST3B1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[HIPK2]] | B | HIPK2 activity raises HS3ST3B1's level | lines that do not express HIPK2 (5) vs lines expressing it (45) | 3.18× lower at baseline in the lines without HIPK2 | 0.089 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HIPK2]] | B | HS3ST3B1 activity raises HIPK2's level | lines that do not express HS3ST3B1 (18) vs lines expressing it (32) | 2.11× lower at baseline in the lines without HS3ST3B1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[ZNF281]] | B | HS3ST3B1 activity raises ZNF281's level | lines that do not express HS3ST3B1 (18) vs lines expressing it (32) | 1.50× lower at baseline in the lines without HS3ST3B1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[CCND3]] | B | HS3ST3B1 activity lowers CCND3's level | lines that do not express HS3ST3B1 (18) vs lines expressing it (32) | 1.42× higher at baseline in the lines without HS3ST3B1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[MLKL]] | B | HS3ST3B1 activity raises MLKL's level | lines that do not express HS3ST3B1 (18) vs lines expressing it (32) | 1.81× lower at baseline in the lines without HS3ST3B1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[SLC7A2]] | B | HS3ST3B1 activity raises SLC7A2's level | lines that do not express HS3ST3B1 (18) vs lines expressing it (32) | 2.81× lower at baseline in the lines without HS3ST3B1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[MFSD2A]] | B | HS3ST3B1 activity raises MFSD2A's level | lines that do not express HS3ST3B1 (18) vs lines expressing it (32) | 1.62× lower at baseline in the lines without HS3ST3B1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| cells under [[Sapanisertib (drug)]] 0.5 µM | B | HS3ST3B1 activity lowers the cells' numbers under Sapanisertib 0.5 µM (makes them more sensitive) | lines that do not express HS3ST3B1 (18) vs lines expressing it (30) | the lines without HS3ST3B1: 1.12× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| cells under [[LY-2584702 (tosylate salt) (drug)]] 5 µM | B | HS3ST3B1 activity lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | lines that do not express HS3ST3B1 (18) vs lines expressing it (30) | the lines without HS3ST3B1: 1.28× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| cells under [[Osimertinib (mesylate) (drug)]] 5 µM | B | HS3ST3B1 activity lowers the cells' numbers under Osimertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express HS3ST3B1 (18) vs lines expressing it (30) | the lines without HS3ST3B1: 1.14× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| cells under [[Ipatasertib (drug)]] 0.5 µM | B | HS3ST3B1 activity lowers the cells' numbers under Ipatasertib 0.5 µM (makes them more sensitive) | lines that do not express HS3ST3B1 (18) vs lines expressing it (30) | the lines without HS3ST3B1: 1.30× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[PRKACB]] | B | HS3ST3B1 activity raises PRKACB's level | lines that do not express HS3ST3B1 (18) vs lines expressing it (32) | 2.11× lower at baseline in the lines without HS3ST3B1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[ATP2B1]] | B | HS3ST3B1 activity raises ATP2B1's level | lines that do not express HS3ST3B1 (18) vs lines expressing it (32) | 1.82× lower at baseline in the lines without HS3ST3B1 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.630). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.2, 14.3); signed map (16.6, 32.3). **Vector** length 88.8, 22.0% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.5 | +4.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.4 | +5.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.4 | +7.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.2 | +7.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.1 | +7.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +2.8 | +3.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -3.7 | -3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.3 | -6.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -5.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | heparan sulfate-glucosamine 3-sulfotransferase 3B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p12 — chr17:14,301,081-14,349,404 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 3OST3B1, 30ST3B1 |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Reactome | 4 pathways, smallest: HS-GAG biosynthesis; Heparan sulfate/heparin (HS-GAG) metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y662](https://www.uniprot.org/uniprotkb/Q9Y662) (Heparan sulfate glucosamine 3-O-sulfotransferase 3B1):

> Sulfotransferase that utilizes 3'-phospho-5'-adenylyl sulfate (PAPS) to catalyze the transfer of a sulfo group to an N-unsubstituted glucosamine linked to a 2-O-sulfo iduronic acid unit on heparan sulfate. Catalyzes the O-sulfation of glucosamine in IdoUA2S-GlcNS and also in IdoUA2S-GlcNH2. The substrate-specific O-sulfation generates an enzyme-modified heparan sulfate which acts as a binding receptor to Herpes simplex virus-1 (HSV-1) and permits its entry. Unlike HS3ST1/3-OST-1, does not …

**Summary**, from NCBI Gene [9953](https://www.ncbi.nlm.nih.gov/gene/9953):

> The protein encoded by this gene is a type II integral membrane protein that belongs to the 3-O-sulfotransferases family. These proteins catalyze the addition of sulfate groups at the 3-OH position of glucosamine in heparan sulfate. The substrate specificity of individual members of the family is based on prior modification of the heparan sulfate chain, thus allowing different members of the family to generate binding sites for different proteins on the same heparan sulfate chain. Following …

**Accessions** — [HGNC:5198](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5198) · Entrez [9953](https://www.ncbi.nlm.nih.gov/gene/9953) · UniProt [Q9Y662](https://www.uniprot.org/uniprotkb/Q9Y662) · Ensembl [ENSG00000125430](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125430)

## Data

Gene col 4612: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4612); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4612, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4612]; `tensor/DDL_lfc|DDL_z.npy` [4612]; `embed/gene_vectors.npy` [4612]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4612 or target_col == 4612). Every well: [[HS3ST3B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HS3ST3B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

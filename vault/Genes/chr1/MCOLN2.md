---
symbol: "MCOLN2"
type: "gene"
col: 7746
ensembl_id: "ENSG00000153898"
name: "mucolipin TRP cation channel 2"
location: "1p22.3"
module: 33
arm: "+"
pooled_cpm: 13.2
n_lines_expressing: 32
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 11
direction_downstream: 53
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# MCOLN2

*mucolipin TRP cation channel 2* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.30× (z +15.9, q 0e+00, up in 28 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.558× (z -11.1, q 5e-26, down in 19 of 27 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.619× (z -6.5, q 2e-08, down in 17 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASIC1]] (+0.75, fdr 7e-06), [[FXN]] (+0.69, fdr 7e-06), [[ANKS6]] (+0.68, fdr 7e-06); moves opposite to [[EFCAB6]] (-0.65, fdr 1e-05), [[ZMAT2]] (-0.63, fdr 1e-05), [[SYNRG]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[GNAZ]] → it (grade B ⚠); 53 go from it, the strongest it → [[POLR3G]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7746.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.30×** | +15.9 | 0e+00 | 28/30 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.57×** | +12.7 | 9e-35 | 24/29 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.50×** | +12.4 | 9e-33 | 23/29 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.33×** | +11.4 | 6e-28 | 23/29 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.20×** | +10.6 | 3e-24 | 23/29 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.08×** | +9.9 | 5e-21 | 22/27 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.69×** | +7.0 | 3e-10 | 16/30 (PANC-1, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +6.6 | 2e-09 | 15/27 (A498, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.31×** | +5.1 | 2e-05 | 14/30 (C32, A-427, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +4.4 | 5e-04 | 8/29 (NCI-H460, C32, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +4.0 | 0.004 | 5/13 (NCI-H1792, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.9 | 0.004 | 5/14 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.50×** | +3.9 | 0.004 | 4/29 (PANC-1, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.31×** | +3.6 | 0.012 | 9/29 (C32, LOX-IMVI, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.022 | 9/29 (A498, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Pemetrexed (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.037 | 4/29 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Lopinavir (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.039 | 2/29 (A498, A-427) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7746.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.558×** | -11.1 | 5e-26 | 19/27 (A549, A-427, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.428×** | -11.0 | 1e-25 | 18/27 (A-427, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.619×** | -6.5 | 2e-08 | 17/29 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.665×** | -5.5 | 5e-06 | 16/26 (LOX-IMVI, C-33 A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.478×** | -5.2 | 2e-05 | 17/28 (PANC-1, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.683×** | -5.2 | 2e-05 | 15/27 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.695×** | -4.9 | 7e-05 | 14/29 (PANC-1, RKO, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.836× | -3.4 | 0.046 | 12/30 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~76% of this change | **0.783×** | -3.3 | 0.061 | 10/22 (HS-578T, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | **0.789×** | -3.2 | 0.079 | 8/28 (NCI-H23, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7746. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 49.5 | 2 | 7 (7 ⚠) | [[Panobinostat (drug)]] 5 µM 2.57× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -10.9) ⚠ cell-cycle shift, explains ~51% of this change |
| [[A549 (line)]] | wt | 11.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0927× (z -16.7) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.145× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 14.9 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.183× (z -11.3) |
| [[A-427 (line)]] | wt | 47.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -15.9) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H2030 (line)]] | alt | 28.8 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 77.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -9.9) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SK-MEL-2 (line)]] | alt | 36.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -12.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.128× (z -10.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HS-578T (line)]] | alt | 9.50 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.127× (z -9.5) ⚠ transcription drop; cell-cycle shift, explains ~76% of this change |
| [[LoVo (line)]] | wt | 18.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.51× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -12.0) ⚠ cell-cycle shift, explains ~42% of this change |
| [[MIA PaCa-2 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -12.0) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SW48 (line)]] | wt | 35.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -9.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-172 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.903 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.945 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7746), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASIC1]] | +0.75 | +0.69 / +0.72 | both halves | 7e-06 | pathway: Ion channel transport |
| [[FXN]] | +0.69 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ANKS6]] | +0.68 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[LPAR3]] | +0.67 | +0.57 / +0.67 | both halves | 9e-06 | ⚠ same locus (32.4 kb, same strand: neighbours can correlate without regulation) |
| [[PACC1]] | +0.66 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[METAP1]] | +0.66 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[CHST10]] | +0.66 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[CCDC88C]] | +0.66 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[LHX6]] | +0.65 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[RSAD1]] | +0.65 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[ASB13]] | +0.65 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[PALS2]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ADAT2]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB6]] | -0.65 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[ZMAT2]] | -0.63 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[SYNRG]] | -0.62 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[KRCC1]] | -0.61 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[UBE3B]] | -0.60 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[AEBP2]] | -0.59 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[DNASE1]] | -0.59 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[FAM120AOS]] | -0.58 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[HOMEZ]] | -0.58 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[PKN2-AS1]] | -0.58 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[PCNX4-DT]] | -0.58 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[ZNF764]] | -0.58 | -0.49 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAZ]] | B | GNAZ activity raises MCOLN2's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.63× lower at baseline in the lines without GNAZ | 0.009 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[KIF26A]] | B | KIF26A activity raises MCOLN2's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.25× lower at baseline in the lines without KIF26A | 0.022 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[LINC00937]] | B | LINC00937 activity raises MCOLN2's level | lines that do not express LINC00937 (13) vs lines expressing it (37) | 2.42× lower at baseline in the lines without LINC00937 | 0.027 | ⚠ within organs, on part of the lines; also absent: SYCP2, ENSG00000255367, MRAS; maybe low, not absent |
| [[LPAR3]] | B | LPAR3 activity raises MCOLN2's level | lines that do not express LPAR3 (16) vs lines expressing it (34) | 2.86× lower at baseline in the lines without LPAR3 | 0.043 | ⚠ within organs, on part of the lines; also absent: BEX4, ADAMTS18, GAB3; maybe low, not absent |
| [[RNF220]] | B | RNF220 activity raises MCOLN2's level | lines that do not express RNF220 (9) vs lines expressing it (41) | 2.73× lower at baseline in the lines without RNF220 | 0.065 | ⚠ within organs, on part of the lines; also absent: GNAZ, ENSG00000287400, CTXN1; maybe low, not absent |
| [[BRSK2]] | B | BRSK2 activity raises MCOLN2's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 3.01× lower at baseline in the lines without BRSK2 | 0.071 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[SYN2]] | B | SYN2 activity raises MCOLN2's level | lines that do not express SYN2 (23) vs lines expressing it (27) | 2.41× lower at baseline in the lines without SYN2 | 0.079 | ⚠ within organs, on part of the lines; also absent: ACP7, PRRX2, LINC01357; maybe low, not absent |
| [[SLC19A3]] | B | SLC19A3 activity raises MCOLN2's level | lines that do not express SLC19A3 (36) vs lines expressing it (14) | 2.18× lower at baseline in the lines without SLC19A3 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, MTND1P23, LINC00824 |
| [[FAM78B]] | B | FAM78B activity raises MCOLN2's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 2.44× lower at baseline in the lines without FAM78B | 0.090 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[SEPTIN3]] | B | SEPTIN3 activity raises MCOLN2's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 2.77× lower at baseline in the lines without SEPTIN3 | 0.097 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[TUB]] | C | TUB activity raises MCOLN2's level | lines that do not express TUB (18) vs lines expressing it (32) | 2.24× lower at baseline in the lines without TUB | 0.092 | ⚠ within organs, on part of the lines; also absent: SLC22A17, CPEB1, ZFP82; co-absent with the target |

### Downstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 52, C 1. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POLR3G]] | B | MCOLN2 activity raises POLR3G's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 2.14× lower at baseline in the lines without MCOLN2 | 0.006 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[KIF26A]] | B | MCOLN2 activity raises KIF26A's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.80× lower at baseline in the lines without MCOLN2 | 0.007 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[FXN]] | B | MCOLN2 activity raises FXN's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.28× lower at baseline in the lines without MCOLN2 | 0.008 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[ASIC1]] | B | MCOLN2 activity raises ASIC1's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.50× lower at baseline in the lines without MCOLN2 | 0.009 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[BRSK2]] | B | MCOLN2 activity raises BRSK2's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 2.22× lower at baseline in the lines without MCOLN2 | 0.011 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[CHST10]] | B | MCOLN2 activity raises CHST10's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.75× lower at baseline in the lines without MCOLN2 | 0.011 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[NT5M]] | B | MCOLN2 activity raises NT5M's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 2.08× lower at baseline in the lines without MCOLN2 | 0.011 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[PRTG]] | B | MCOLN2 activity raises PRTG's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 2.21× lower at baseline in the lines without MCOLN2 | 0.011 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[UBE3D]] | B | MCOLN2 activity raises UBE3D's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.15× lower at baseline in the lines without MCOLN2 | 0.012 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[ZFP69]] | B | MCOLN2 activity raises ZFP69's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.71× lower at baseline in the lines without MCOLN2 | 0.013 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[PPARGC1B]] | B | MCOLN2 activity raises PPARGC1B's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.68× lower at baseline in the lines without MCOLN2 | 0.023 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[VASH1]] | B | MCOLN2 activity raises VASH1's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.77× lower at baseline in the lines without MCOLN2 | 0.025 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.609). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.3, 40.1); signed map (-8.5, -54.7). **Vector** length 72.4, 17.5% of its response variance represented; |z| ≥ 3 in 699 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +15.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +9.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.7 | +10.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.9 | +4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | +12.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[EX229 (drug)]] 5 µM |  | +1.4 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -4.9 | -11.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.7 | -11.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.0 | -5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -1.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.6 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | mucolipin TRP cation channel 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:84,925,583-84,997,113 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRPML2, FLJ36691, TRP-ML2 |
| Gene groups (HGNC) | Mucolipin TRP cation channel family |
| Reactome | 4 pathways, smallest: TRP channels; Stimuli-sensing channels; Ion channel transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZK6](https://www.uniprot.org/uniprotkb/Q8IZK6) (Mucolipin-2):

> Nonselective cation channel probably playing a role in the regulation of membrane trafficking events. Acts as a Ca(2+)-permeable cation channel with inwardly rectifying activity. May activate ARF6 and be involved in the trafficking of GPI-anchored cargo proteins to the cell surface via the ARF6-regulated recycling pathway. May play a role in immune processes. In adaptive immunity, TRPML2 and TRPML1 may play redundant roles in the function of the specialized lysosomes of B cells (By similarity). …

**Summary**, from NCBI Gene [255231](https://www.ncbi.nlm.nih.gov/gene/255231):

> Mucolipins constitute a family of cation channel proteins with homology to the transient receptor potential superfamily. In mammals, the mucolipin family includes 3 members, MCOLN1 (MIM 605248), MCOLN2, and MCOLN3 (MIM 607400), that exhibit a common 6-membrane-spanning topology. Homologs of mammalian mucolipins exist in Drosophila and C. elegans. Mutations in the human MCOLN1 gene cause mucolipodosis IV (MIM 262650) (Karacsonyi et al., 2007 [PubMed 17662026]).[supplied by OMIM, Sep 2009]

**Accessions** — [HGNC:13357](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13357) · Entrez [255231](https://www.ncbi.nlm.nih.gov/gene/255231) · UniProt [Q8IZK6](https://www.uniprot.org/uniprotkb/Q8IZK6) · Ensembl [ENSG00000153898](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153898)

## Data

Gene col 7746: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7746); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7746, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7746]; `tensor/DDL_lfc|DDL_z.npy` [7746]; `embed/gene_vectors.npy` [7746]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7746 or target_col == 7746). Every well: [[MCOLN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCOLN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "LEMD1"
type: "gene"
col: 11765
ensembl_id: "ENSG00000186007"
name: "LEM domain containing 1"
location: "1q32.1"
module: 31
arm: "+"
pooled_cpm: 22.79
n_lines_expressing: 28
n_dd_up: 5
n_dd_down: 48
n_dd_up_clean: 4
n_dd_down_clean: 36
in_vector_space: true
direction_upstream: 62
direction_downstream: 86
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# LEMD1

*LEM domain containing 1* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.68× (z +7.3, q 2e-10, up in 20 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 48 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.344× (z -15.0, q 0e+00, down in 25 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BLACAT1]] (+0.91, fdr 7e-06, ⚠ same locus), [[B3GNT3]] (+0.78, fdr 7e-06), [[LCK]] (+0.74, fdr 7e-06), [[PADI1]] (+0.73, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 62 arrows point to it, the strongest [[CARD11]] → it (grade B ⚠); 86 go from it, the strongest it → [[FHDC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11765.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +7.3 | 2e-10 | 20/26 (A498, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.80×** | +5.8 | 2e-06 | 16/25 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.68×** | +5.2 | 5e-05 | 19/25 (SW48, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.44×** | +3.5 | 0.077 | 15/25 (SW48, C32, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.090 | 9/26 (SW480, KATO III, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 48 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11765.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.344×** | -15.0 | 0e+00 | 25/26 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.265×** | -13.2 | 3e-37 | 23/25 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.270×** | -12.5 | 2e-33 | 24/25 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.404×** | -9.0 | 4e-17 | 23/25 (COLO 205, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.451×** | -7.9 | 3e-13 | 23/25 (COLO 205, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.573×** | -7.8 | 6e-13 | 24/26 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.464×** | -7.6 | 2e-12 | 21/25 (COLO 205, HEC-1-A, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.469×** | -7.5 | 4e-12 | 20/25 (SW480, LS 180, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.471×** | -7.5 | 5e-12 | 18/25 (H4, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.480×** | -7.0 | 1e-10 | 20/25 (KATO III, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.481×** | -7.0 | 2e-10 | 23/25 (COLO 205, KATO III, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.623×** | -5.5 | 2e-06 | 18/26 (HEC-1-A, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.577×** | -5.4 | 2e-06 | 20/25 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.600×** | -5.1 | 1e-05 | 20/26 (HEC-1-A, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.323×** | -5.1 | 1e-05 | 19/27 (KATO III, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.697×** | -5.0 | 2e-05 | 14/26 (C32, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.601×** | -5.0 | 2e-05 | 20/26 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.602×** | -5.0 | 2e-05 | 18/26 (HEC-1-A, SW48, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.613×** | -4.8 | 4e-05 | 19/25 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.728×** | -4.4 | 2e-04 | 15/26 (HEC-1-A, SW48, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.625×** | -4.4 | 3e-04 | 17/26 (HEC-1-A, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.56 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11765. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 92.3 | 0 | 21 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0866× (z -29.0) |
| [[HEC-1-A (line)]] | alt | 27.6 | 0 | 19 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0990× (z -18.3) |
| [[COLO 205 (line)]] | alt | 136 | 0 | 17 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0442× (z -31.1) |
| [[KATO III (line)]] | alt | 119 | 0 | 17 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0399× (z -30.7) |
| [[CFPAC-1 (line)]] | alt | 60.1 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0697× (z -24.2) |
| [[LS 180 (line)]] | wt | 42.4 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0590× (z -22.4) |
| [[H4 (line)]] | wt | 22.9 | 0 | 8 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0297× (z -14.6) |
| [[SW48 (line)]] | wt | 104 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0462× (z -23.4) |
| [[AsPC-1 (line)]] | alt | 28.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -14.1) |
| [[C32 (line)]] | wt | 78.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0686× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.266× (z -11.9) |
| [[A-172 (line)]] | wt | 16.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -11.6) |
| [[A498 (line)]] | wt | 32.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -19.6) |
| [[MIA PaCa-2 (line)]] | alt | 19.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 25.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -12.8) |
| [[SW1417 (line)]] | alt | 45.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0868× (z -19.2) |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.0556× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 28.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0803× (z -14.6) |
| [[HT-29 (line)]] | alt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -11.7) |
| [[LoVo (line)]] | wt | 9.51 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -8.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H1573 (line)]] | alt | 8.10 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0568× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[NCI-H2347 (line)]] | alt | 7.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -8.6) |
| [[RKO (line)]] | wt | 9.33 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0844× (z -8.6) |
| [[SW 900 (line)]] | alt | 7.70 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -9.5) |
| [[A-427 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.59 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.35 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11765), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLACAT1]] | +0.91 | +0.92 / +0.86 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[B3GNT3]] | +0.78 | +0.78 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[LCK]] | +0.74 | +0.68 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[PADI1]] | +0.73 | +0.68 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[KIAA0040]] | +0.71 | +0.73 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[INPP5D]] | +0.70 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[EPHA2-AS1]] | +0.69 | +0.63 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[LINC00659]] | +0.68 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[CEACAM1]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[TLDC2]] | +0.67 | +0.58 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[GPR35]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[RDH13]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[CRYBG2]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*62 arrows, 62 of them with an alert ⚠; grade A 0, B 12, C 50. Shown: the 12 strongest; 50 more arrows (50 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD11]] | B | CARD11 activity raises LEMD1's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.05× lower at baseline in the lines without CARD11 | 0.016 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[ANO1]] | B | ANO1 activity raises LEMD1's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 3.03× lower at baseline in the lines without ANO1 | 0.023 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[PRAG1]] | B | PRAG1 activity raises LEMD1's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 2.62× lower at baseline in the lines without PRAG1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[IL19]] | B | IL19 activity raises LEMD1's level | lines that do not express IL19 (23) vs lines expressing it (27) | 2.26× lower at baseline in the lines without IL19 | 0.040 | ⚠ within organs, on part of the lines; also absent: PKHD1, IHO1, CASC20; maybe low, not absent |
| [[LCK]] | B | LCK activity raises LEMD1's level | lines that do not express LCK (31) vs lines expressing it (19) | 2.31× lower at baseline in the lines without LCK | 0.069 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent |
| [[FGF19]] | B | FGF19 activity raises LEMD1's level | lines that do not express FGF19 (42) vs lines expressing it (8) | 3.02× lower at baseline in the lines without FGF19 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, SFTPA2, KRT5 |
| [[MYO1D]] | B | MYO1D activity raises LEMD1's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 2.43× lower at baseline in the lines without MYO1D | 0.077 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[ZBED2]] | B | ZBED2 activity raises LEMD1's level | lines that do not express ZBED2 (39) vs lines expressing it (11) | 3.34× lower at baseline in the lines without ZBED2 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPON1, ENSG00000289850, KLK11 |
| [[SHROOM4]] | B | SHROOM4 activity raises LEMD1's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 1.87× lower at baseline in the lines without SHROOM4 | 0.080 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539 |
| [[MALL]] | B | MALL activity raises LEMD1's level | lines that do not express MALL (21) vs lines expressing it (29) | 2.58× lower at baseline in the lines without MALL | 0.082 | ⚠ within organs, on part of the lines; also absent: SDR16C5, SPNS2, CLDN4 |
| [[FKBP9P1-1]] | B | FKBP9P1-1 activity raises LEMD1's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 2.36× lower at baseline in the lines without FKBP9P1-1 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[MYEOV]] | B | MYEOV activity raises LEMD1's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 2.68× lower at baseline in the lines without MYEOV | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |

### Downstream of this gene

*86 arrows, 86 of them with an alert ⚠; grade A 0, B 41, C 45. Shown: the 12 strongest; 74 more arrows (74 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FHDC1]] | B | LEMD1 activity raises FHDC1's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 2.01× lower at baseline in the lines without LEMD1 | 0.001 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[EPS8L1]] | B | LEMD1 activity raises EPS8L1's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 2.97× lower at baseline in the lines without LEMD1 | 0.003 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[LSMEM2]] | B | LEMD1 activity raises LSMEM2's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 2.11× lower at baseline in the lines without LEMD1 | 0.004 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[KRT15]] | B | LEMD1 activity raises KRT15's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 3.03× lower at baseline in the lines without LEMD1 | 0.005 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[SHROOM4]] | B | LEMD1 activity raises SHROOM4's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 2.85× lower at baseline in the lines without LEMD1 | 0.005 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[TMC6]] | B | LEMD1 activity raises TMC6's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 2.60× lower at baseline in the lines without LEMD1 | 0.008 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[FAM83E]] | B | LEMD1 activity raises FAM83E's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 2.49× lower at baseline in the lines without LEMD1 | 0.010 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[C3orf18]] | B | LEMD1 activity lowers C3orf18's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 1.60× higher at baseline in the lines without LEMD1 | 0.010 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[RDH13]] | B | LEMD1 activity raises RDH13's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 1.82× lower at baseline in the lines without LEMD1 | 0.012 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[SPATA13]] | B | LEMD1 activity raises SPATA13's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 2.42× lower at baseline in the lines without LEMD1 | 0.013 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[TLDC2]] | B | LEMD1 activity raises TLDC2's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 2.07× lower at baseline in the lines without LEMD1 | 0.015 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[MST1R]] | B | LEMD1 activity raises MST1R's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 3.00× lower at baseline in the lines without LEMD1 | 0.015 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.3, 52.3); signed map (3.6, 38.8). **Vector** length 111, 37.9% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | -1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.7 | -0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | -7.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | -0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.0 | +2.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.8 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.5 | -4.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.7 | -5.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.7 | -5.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | LEM domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:205,381,378-205,455,954 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LEMP-1, CT50 |
| Gene groups (HGNC) | LEM domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q68G75](https://www.uniprot.org/uniprotkb/Q68G75) carries no function annotation.

**Summary**, from NCBI Gene [93273](https://www.ncbi.nlm.nih.gov/gene/93273):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18725](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18725) · Entrez [93273](https://www.ncbi.nlm.nih.gov/gene/93273) · UniProt [Q68G75](https://www.uniprot.org/uniprotkb/Q68G75) · Ensembl [ENSG00000186007](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186007)

## Data

Gene col 11765: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11765); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11765, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11765]; `tensor/DDL_lfc|DDL_z.npy` [11765]; `embed/gene_vectors.npy` [11765]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11765 or target_col == 11765). Every well: [[LEMD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LEMD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

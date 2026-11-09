---
symbol: "LIPC"
type: "gene"
col: 9229
ensembl_id: "ENSG00000166035"
name: "lipase C, hepatic type"
location: "15q21.3"
module: 90
arm: "+"
pooled_cpm: 2.49
n_lines_expressing: 32
n_dd_up: 18
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 12
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# LIPC

*lipase C, hepatic type* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.64× (z +11.8, q 2e-29, up in 10 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.511× (z -5.8, q 4e-06, down in 15 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01483]] (+0.69, fdr 1e-05), [[A1CF]] (+0.68, fdr 1e-05), [[BANK1]] (+0.66, fdr 1e-05).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 12 go from it, the strongest it → [[LINC02694]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9229.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +11.8 | 2e-29 | 10/22 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +8.6 | 3e-15 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.60×** | +7.6 | 5e-12 | 2/5 (A498, MIA PaCa-2) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.17×** | +6.7 | 3e-09 | 9/25 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +6.6 | 6e-09 | 1/12 (HEC-1-A) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.2 | 2e-05 | 5/29 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.019 | 3/20 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.58×** | +3.6 | 0.020 | 3/23 (H4, SW480, …) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.80×** | +3.6 | 0.020 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.74×** | +3.4 | 0.038 | 2/19 (SW480, A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.043 | 2/23 (KATO III, PANC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.043 | 2/22 (SNU-1, HOP62) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.3 | 0.043 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.33×** | +3.2 | 0.056 | 5/27 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.67×** | +3.1 | 0.059 | 1/15 (HepG2/C3A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.44×** | +3.1 | 0.059 | 2/15 (MIA PaCa-2, J82) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.32×** | +3.0 | 0.087 | 6/27 (SW480, LoVo, …) | inconsistent across doses | position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.41×** | +3.0 | 0.089 | 4/24 (HepG2/C3A, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9229.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.511×** | -5.8 | 4e-06 | 15/27 (MIA PaCa-2, H4, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.500×** | -5.5 | 1e-05 | 11/26 (COLO 205, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.592×** | -4.5 | 0.001 | 11/28 (COLO 205, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.585×** | -4.2 | 0.003 | 14/25 (Hs 766T, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.588×** | -4.2 | 0.003 | 12/23 (COLO 205, SW480, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.621×** | -4.1 | 0.004 | 8/27 (COLO 205, H4, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -3.5 | 0.045 | 3/29 (MIA PaCa-2, SW48, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.679× | -3.0 | 0.17 | 7/27 (SHP-77, A498, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9229. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 18.4 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0157× (z -14.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0719× (z -13.1) |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 3 | — | [[Bendamustine (drug)]] 0.05 µM 0.0713× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0595× (z -10.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Hs 766T (line)]] | wt | 6.55 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0595× (z -9.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 37.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -9.5) |
| [[A-172 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.351 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.595 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.724 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.599 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.517 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.489 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.766 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.961 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.932 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.421 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.921 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.853 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.931 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9229), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01483]] | +0.69 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[A1CF]] | +0.68 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[BANK1]] | +0.66 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[SATB1-AS1]] | +0.65 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[LINC00298]] | +0.64 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[CCDC170]] | +0.63 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[THBS4-AS1]] | +0.63 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[LINC02068]] | +0.62 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[GRM8]] | +0.62 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[ALDH1A2]] | +0.62 | +0.66 / +0.49 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[DLEU7]] | +0.61 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[PKHD1]] | +0.59 | +0.58 / +0.57 | both halves | 8e-06 |  |
| [[LINC02058]] | +0.59 | +0.58 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises LIPC's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LMO2]] | B | LMO2 activity raises LIPC's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 1.82× lower at baseline in the lines without LMO2 | 0.089 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[APOB]] | C | APOB activity raises LIPC's level | lines that do not express APOB (47) vs lines expressing it (3) | 2.25× lower at baseline in the lines without APOB | 0.086 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: APOA2, BMP10, TBXT |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 10, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02694]] | B | LIPC activity raises LINC02694's level | lines that do not express LIPC (18) vs lines expressing it (32) | 1.19× lower at baseline in the lines without LIPC | 0.038 | ⚠ within organs, on part of the lines; also absent: TNFSF10, NIHCOLE, HNMT; maybe low, not absent |
| [[ALDH1A2]] | B | LIPC activity raises ALDH1A2's level | lines that do not express LIPC (18) vs lines expressing it (32) | 2.92× lower at baseline in the lines without LIPC | 0.048 | ⚠ within organs, on part of the lines; also absent: TNFSF10, NIHCOLE, HNMT; maybe low, not absent |
| [[MYO3B]] | B | LIPC activity raises MYO3B's level | lines that do not express LIPC (18) vs lines expressing it (32) | 1.28× lower at baseline in the lines without LIPC | 0.049 | ⚠ within organs, on part of the lines; also absent: TNFSF10, NIHCOLE, HNMT; maybe low, not absent |
| [[PKHD1]] | B | LIPC activity raises PKHD1's level | lines that do not express LIPC (18) vs lines expressing it (32) | 1.86× lower at baseline in the lines without LIPC | 0.054 | ⚠ within organs, on part of the lines; also absent: TNFSF10, NIHCOLE, HNMT; maybe low, not absent |
| [[ENPP3]] | B | LIPC activity raises ENPP3's level | lines that do not express LIPC (18) vs lines expressing it (32) | 1.39× lower at baseline in the lines without LIPC | 0.060 | ⚠ within organs, on part of the lines; also absent: TNFSF10, NIHCOLE, HNMT; maybe low, not absent |
| [[MALRD1]] | B | LIPC activity raises MALRD1's level | lines that do not express LIPC (18) vs lines expressing it (32) | 1.41× lower at baseline in the lines without LIPC | 0.079 | ⚠ within organs, on part of the lines; also absent: TNFSF10, NIHCOLE, HNMT; maybe low, not absent |
| [[BANK1]] | B | LIPC activity raises BANK1's level | lines that do not express LIPC (18) vs lines expressing it (32) | 1.61× lower at baseline in the lines without LIPC | 0.092 | ⚠ within organs, on part of the lines; also absent: TNFSF10, NIHCOLE, HNMT; maybe low, not absent |
| [[LINC01285]] | B | LIPC activity raises LINC01285's level | lines that do not express LIPC (18) vs lines expressing it (32) | 1.88× lower at baseline in the lines without LIPC | 0.092 | ⚠ within organs, on part of the lines; also absent: TNFSF10, NIHCOLE, HNMT; maybe low, not absent |
| [[LINC00992]] | B | LIPC activity raises LINC00992's level | lines that do not express LIPC (18) vs lines expressing it (32) | 1.49× lower at baseline in the lines without LIPC | 0.098 | ⚠ within organs, on part of the lines; also absent: TNFSF10, NIHCOLE, HNMT; maybe low, not absent |
| [[MAN1A1]] | B | LIPC activity raises MAN1A1's level | lines that do not express LIPC (18) vs lines expressing it (32) | 1.65× lower at baseline in the lines without LIPC | 0.098 | ⚠ within organs, on part of the lines; also absent: TNFSF10, NIHCOLE, HNMT; maybe low, not absent |
| [[NIHCOLE]] | C | LIPC activity raises NIHCOLE's level | lines that do not express LIPC (18) vs lines expressing it (32) | 3.47× lower at baseline in the lines without LIPC | 0.009 | ⚠ within organs, on part of the lines; also absent: TNFSF10, NIHCOLE, HNMT; maybe low, not absent; co-absent with the target |
| [[TNFSF10]] | C | LIPC activity raises TNFSF10's level | lines that do not express LIPC (18) vs lines expressing it (32) | 3.36× lower at baseline in the lines without LIPC | 0.078 | ⚠ within organs, on part of the lines; also absent: TNFSF10, NIHCOLE, HNMT; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.518). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.9, 45.5); signed map (57.5, 17.4). **Vector** length 43.1, 7.59% of its response variance represented; |z| ≥ 3 in 615 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.4 | +1.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -1.4 | -4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.2 | -5.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | lipase C, hepatic type |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:58,410,569-58,569,844 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HL, HTGL |
| Gene groups (HGNC) | Lipases |
| Reactome | 6 pathways, smallest: Chylomicron clearance; Assembly of active LPL and LIPC lipase complexes; Plasma lipoprotein remodeling |
| Matched by | ensembl_id |

**Function**, from UniProt [P11150](https://www.uniprot.org/uniprotkb/P11150) (Hepatic triacylglycerol lipase):

> Catalyzes the hydrolysis of triglycerides and phospholipids present in circulating plasma lipoproteins, including chylomicrons, intermediate density lipoproteins (IDL), low density lipoproteins (LDL) of large size and high density lipoproteins (HDL), releasing free fatty acids (FFA) and smaller lipoprotein particles. Also exhibits lysophospholipase activity (By similarity). Can hydrolyze both neutral lipid and phospholipid substrates but shows a greater binding affinity for neutral lipid …

**Summary**, from NCBI Gene [3990](https://www.ncbi.nlm.nih.gov/gene/3990):

> Enables glycerophospholipid phospholipase A1 activity and triacylglycerol lipase activity. Involved in several processes, including cholesterol homeostasis; plasma lipoprotein particle remodeling; and triglyceride catabolic process. Located in obsolete extracellular space. Implicated in several diseases, including Alzheimer's disease; coronary artery disease; familial combined hyperlipidemia; peripheral vascular disease; and type 2 diabetes mellitus. Biomarker of hyperinsulinism; obesity; and …

**Accessions** — [HGNC:6619](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6619) · Entrez [3990](https://www.ncbi.nlm.nih.gov/gene/3990) · UniProt [P11150](https://www.uniprot.org/uniprotkb/P11150) · Ensembl [ENSG00000166035](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166035)

## Data

Gene col 9229: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9229); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9229, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9229]; `tensor/DDL_lfc|DDL_z.npy` [9229]; `embed/gene_vectors.npy` [9229]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9229 or target_col == 9229). Every well: [[LIPC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIPC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "SAMSN1"
type: "gene"
col: 7885
ensembl_id: "ENSG00000155307"
name: "SAM domain, SH3 domain and nuclear localization signals 1"
location: "21q11.2"
module: 98
arm: "+"
pooled_cpm: 2.83
n_lines_expressing: 44
n_dd_up: 48
n_dd_down: 4
n_dd_up_clean: 42
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 6
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# SAMSN1

*SAM domain, SH3 domain and nuclear localization signals 1* — 21q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 48 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.16× (z +14.3, q 1e-43, up in 22 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.499× (z -6.1, q 5e-07, down in 21 of 38 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H1573 0.0565×, HEC-1-A 0.0587×, A498 0.0815×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0570×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (Hs 766T 0.0175×; ⚠ cell-cycle shift, explains ~53% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.222×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00607]] (+0.67, fdr 7e-06), [[MGC4859]] (+0.66, fdr 7e-06), [[LINC01170]] (+0.65, fdr 8e-06); moves opposite to [[SCAI]] (-0.50, fdr 1e-04), [[UBA6]] (-0.49, fdr 3e-04), [[DNMT3B]] (-0.49, fdr 4e-04).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 6 go from it, the strongest it → [[PPFIA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 48 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7885.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.16×** | +14.3 | 1e-43 | 22/30 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.41×** | +10.9 | 2e-25 | 27/36 (Panc 03.27, NCI-H460, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **8.87×** | +10.0 | 2e-21 | 6/6 (A549, A498, …) | rises with dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **7.76×** | +9.4 | 6e-19 | 26/30 (A498, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.76×** | +8.6 | 1e-15 | 18/31 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **6.31×** | +8.5 | 2e-15 | 19/29 (C32, Panc 03.27, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +8.4 | 3e-15 | 12/27 (NCI-H2030, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.49×** | +8.0 | 8e-14 | 22/38 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.55×** | +7.8 | 3e-13 | 15/29 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.54×** | +7.8 | 3e-13 | 19/30 (NCI-H1573, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +7.4 | 9e-12 | 3/14 (HOP62, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **4.61×** | +7.0 | 1e-10 | 18/24 (NCI-H1573, A498, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +6.8 | 4e-10 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +6.5 | 3e-09 | 1/4 (A498) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.18×** | +6.5 | 3e-09 | 21/33 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.01×** | +6.1 | 3e-08 | 14/28 (NCI-H1573, Panc 03.27, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.85×** | +5.4 | 2e-06 | 16/27 (Panc 03.27, SNU-423, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +5.2 | 5e-06 | 15/37 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.70×** | +4.7 | 9e-05 | 11/30 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7885.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H1573 0.0565×, HEC-1-A 0.0587×, A498 0.0815×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0570×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (Hs 766T 0.0175×; ⚠ cell-cycle shift, explains ~53% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.222×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.499×** | -6.1 | 5e-07 | 21/38 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.534×** | -5.5 | 9e-06 | 19/33 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.540×** | -5.4 | 1e-05 | 16/36 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.597×** | -4.6 | 8e-04 | 15/38 (HEC-1-A, CHP-212, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.888× | -3.7 | 0.026 | 13/39 (SW1417, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.691× | -3.3 | 0.11 | 9/31 (SW 900, hTERT-HPNE, …) | rises with dose |  |
| [[Busulfan (drug)]] 5 µM |  | 0.782× | -3.1 | 0.17 | 3/34 (CHP-212, HepG2/C3A, …) | all doses, flat | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.709× | -3.0 | 0.17 | 9/33 (HEC-1-A, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.63 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7885. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 25.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0570× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 4.98 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +10.0) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0443× (z -11.8) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A498 (line)]] | wt | 4.22 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 12.7× (z +8.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0815× (z -8.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 3.95 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0175× (z -11.9) ⚠ cell-cycle shift, explains ~53% of this change |
| [[LoVo (line)]] | wt | 1.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 2.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.1× (z +12.1) | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0460× (z -11.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 0.721 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.537 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.858 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.794 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.836 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.885 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.857 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.577 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.835 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.809 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.762 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.518 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7885), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00607]] | +0.67 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[MGC4859]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[LINC01170]] | +0.65 | +0.57 / +0.61 | both halves | 8e-06 |  |
| [[NPR3]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[VSTM2L]] | +0.63 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[TG]] | +0.62 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[RIPOR2]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[PDZD2]] | +0.60 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[MT1M]] | +0.60 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[LINC01807]] | +0.60 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ABCA6]] | +0.59 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[LINC00240]] | +0.59 | +0.58 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAI]] | -0.50 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[UBA6]] | -0.49 | -0.50 / -0.29 | both halves | 3e-04 |  |
| [[DNMT3B]] | -0.49 | -0.54 / -0.26 | both halves | 4e-04 |  |
| [[WNT7B]] | -0.48 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[GRK5]] | -0.47 | -0.47 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SAMSN1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TLR2]] | B | TLR2 activity raises SAMSN1's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.81× lower at baseline in the lines without TLR2 | 0.056 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[ENOX1]] | B | ENOX1 activity raises SAMSN1's level | lines that do not express ENOX1 (12) vs lines expressing it (38) | 1.91× lower at baseline in the lines without ENOX1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CYP1B1-AS1, HTR7, SLC1A3; maybe low, not absent |
| [[SLC1A3]] | B | SLC1A3 activity raises SAMSN1's level | lines that do not express SLC1A3 (21) vs lines expressing it (29) | 1.68× lower at baseline in the lines without SLC1A3 | 0.075 | ⚠ within organs, on part of the lines; also absent: LRP2, SLIT2, CHSY3 |
| [[SVEP1]] | B | SVEP1 activity raises SAMSN1's level | lines that do not express SVEP1 (15) vs lines expressing it (35) | 1.62× lower at baseline in the lines without SVEP1 | 0.093 | ⚠ within organs, on part of the lines; also absent: LPAR1, CDH8, ENSG00000253100; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity raises SAMSN1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 7.3% of all compounds | 0.099 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPFIA2]] | B | SAMSN1 activity lowers PPFIA2's level | lines that do not express SAMSN1 (6) vs lines expressing it (44) | 2.76× higher at baseline in the lines without SAMSN1 | 0.028 | ⚠ within organs, on part of the lines; also absent: SYTL2, GNA14, ENSG00000235609; maybe low, not absent |
| [[BCL9L]] | B | SAMSN1 activity raises BCL9L's level | lines that do not express SAMSN1 (6) vs lines expressing it (44) | 1.82× lower at baseline in the lines without SAMSN1 | 0.029 | ⚠ within organs, on part of the lines; also absent: SYTL2, GNA14, ENSG00000235609; maybe low, not absent |
| [[ZC3H12A]] | B | SAMSN1 activity raises ZC3H12A's level | lines that do not express SAMSN1 (6) vs lines expressing it (44) | 2.06× lower at baseline in the lines without SAMSN1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SYTL2, GNA14, ENSG00000235609; maybe low, not absent |
| [[C12orf60]] | B | SAMSN1 activity lowers C12orf60's level | lines that do not express SAMSN1 (6) vs lines expressing it (44) | 1.77× higher at baseline in the lines without SAMSN1 | 0.082 | ⚠ within organs, on part of the lines; also absent: SYTL2, GNA14, ENSG00000235609; maybe low, not absent |
| [[B4GALT1]] | C | SAMSN1 activity raises B4GALT1's level | lines that do not express SAMSN1 (6) vs lines expressing it (44) | 2.47× lower at baseline in the lines without SAMSN1 | 0.005 | ⚠ within organs, on part of the lines; also absent: SYTL2, GNA14, ENSG00000235609; maybe low, not absent; co-absent with the target |
| [[TBX15]] | C | SAMSN1 activity weakens TBX15's drug response | lines that do not express SAMSN1 (4) vs lines expressing it (36) | the lines without SAMSN1 respond 1.58× as strongly (z diff -0.50); strongest at Belinostat 5 µM: 0.14x vs 0.47x (z diff -5.2) | 0.093 | ⚠ within organs, on part of the lines; also absent: SYTL2, GNA14, ENSG00000235609; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.678). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.5, 19.5); signed map (20.2, 30.5). **Vector** length 74.1, 14.9% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +14.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +10.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +7.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.6 | +8.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.3 | +6.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.3 | +5.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.0 | +4.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.7 | +4.1 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.4 | -2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -2.2 | -5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.2 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.3 | -1.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | SAM domain, SH3 domain and nuclear localization signals 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q11.2 — chr21:14,485,228-14,658,821 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NASH1, SASH2, SH3D6B, HACS1, SLy2 |
| Gene groups (HGNC) | SAM and SH3 domain containing; Sterile alpha motif domain containing; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NSI8](https://www.uniprot.org/uniprotkb/Q9NSI8) (SAM domain-containing protein SAMSN-1):

> Negative regulator of B-cell activation. Down-regulates cell proliferation (in vitro). Promotes RAC1-dependent membrane ruffle formation and reorganization of the actin cytoskeleton. Regulates cell spreading and cell polarization. Stimulates HDAC1 activity. Regulates LYN activity by modulating its tyrosine phosphorylation (By similarity).

**Summary**, from NCBI Gene [64092](https://www.ncbi.nlm.nih.gov/gene/64092):

> SAMSN1 is a member of a novel gene family of putative adaptors and scaffold proteins containing SH3 and SAM (sterile alpha motif) domains (Claudio et al., 2001 [PubMed 11536050]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:10528](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10528) · Entrez [64092](https://www.ncbi.nlm.nih.gov/gene/64092) · UniProt [Q9NSI8](https://www.uniprot.org/uniprotkb/Q9NSI8) · Ensembl [ENSG00000155307](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155307)

## Data

Gene col 7885: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7885); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7885, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7885]; `tensor/DDL_lfc|DDL_z.npy` [7885]; `embed/gene_vectors.npy` [7885]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7885 or target_col == 7885). Every well: [[SAMSN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAMSN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

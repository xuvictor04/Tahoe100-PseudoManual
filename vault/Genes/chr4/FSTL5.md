---
symbol: "FSTL5"
type: "gene"
col: 9709
ensembl_id: "ENSG00000168843"
name: "follistatin like 5"
location: "4q32.2"
module: 9
arm: "+"
pooled_cpm: 24.71
n_lines_expressing: 16
n_dd_up: 44
n_dd_down: 3
n_dd_up_clean: 31
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 13
direction_downstream: 20
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# FSTL5

*follistatin like 5* — 4q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.81× (z +19.8, q 0e+00, up in 2 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Fenofibrate (drug)]] 0.05 µM: 0.690× (z -4.7, q 0.002, down in 0 of 13 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SK-MEL-2 0.117×, LS 180 0.156×, RPMI-7951 0.1000×, A-172 0.142×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LS 180 0.247×, A-427 0.192×, SK-MEL-2 0.399×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SHP-77 0.284×, KATO III 0.494×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.420×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DISC1FP1]] (+0.83, fdr 7e-06), [[LINC02241]] (+0.74, fdr 7e-06), [[LINC01320]] (+0.69, fdr 1e-05); moves opposite to [[SIRT3]] (-0.46, fdr 4e-05), [[INO80E]] (-0.45, fdr 4e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[PTPRM]] → it (grade B ⚠); 20 go from it, the strongest it → [[KCNH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9709.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.81×** | +19.8 | 0e+00 | 2/14 (A-172, SW1417) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.74×** | +19.3 | 0e+00 | 14/14 (C32, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.53×** | +17.8 | 0e+00 | 7/14 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.70×** | +17.7 | 0e+00 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.65×** | +17.6 | 0e+00 | 12/13 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.81×** | +14.0 | 1e-42 | 12/13 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.64×** | +13.2 | 1e-37 | 13/13 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.68×** | +12.9 | 5e-36 | 1/11 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.08×** | +9.9 | 2e-21 | 10/13 (SNU-423, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +9.5 | 2e-19 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.81×** | +8.1 | 3e-14 | 6/13 (A-172, SNU-423, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.77×** | +7.7 | 5e-13 | 1/14 (A-172) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +7.0 | 1e-10 | 1/13 (A-172) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +6.4 | 7e-09 | 4/13 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +6.1 | 4e-08 | 12/13 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +6.0 | 5e-08 | 6/13 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +5.5 | 1e-06 | 2/13 (A-172, SK-MEL-2) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +5.2 | 7e-06 | 8/13 (A-172, C32, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.40×** | +4.6 | 1e-04 | 0/13 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9709.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SK-MEL-2 0.117×, LS 180 0.156×, RPMI-7951 0.1000×, A-172 0.142×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LS 180 0.247×, A-427 0.192×, SK-MEL-2 0.399×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SHP-77 0.284×, KATO III 0.494×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.420×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.690×** | -4.7 | 0.002 | 0/13 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.756×** | -3.8 | 0.027 | 6/13 (A-427, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.746×** | -3.8 | 0.027 | 1/13 (C32) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -3.7 | 0.027 | 2/14 (hTERT-HPNE, SW 1088) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.773× | -3.2 | 0.13 | 0/13 | inconsistent across doses |  |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.853× | -3.1 | 0.17 | 0/14 | top dose only |  |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | 0.798× | -3.1 | 0.17 | 0/13 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9709. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 53.4 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.40× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.142× (z -13.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 257 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.98× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.117× (z -20.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 71.2 | 2 (1 ⚠) | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.94× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -8.5) |
| [[C32 (line)]] | wt | 22.4 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.39× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 107 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -16.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 40.7 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.96× (z +9.3) | — |
| [[A-427 (line)]] | wt | 238 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -11.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 79.3 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.42× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.1000× (z -15.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 147 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -13.6) |
| [[A498 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.20 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.90 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.63 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.63 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.20 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.33 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9709), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DISC1FP1]] | +0.83 | +0.74 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[LINC02241]] | +0.74 | +0.69 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[LINC01320]] | +0.69 | +0.76 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[FAM110B]] | +0.65 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[FMN2]] | +0.64 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[LINC02484]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[CPED1]] | +0.63 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[CTNNA2]] | +0.62 | +0.53 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[ERBB4]] | +0.62 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[EPHA5]] | +0.61 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[MARCHF1]] | +0.61 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[LINC01695]] | +0.61 | +0.48 / +0.78 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT3]] | -0.46 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[INO80E]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 1, C 12. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRM]] | B | PTPRM activity raises FSTL5's level | lines that do not express PTPRM (18) vs lines expressing it (32) | 2.32× lower at baseline in the lines without PTPRM | 0.062 | ⚠ within organs, on part of the lines; also absent: FIGN, MAP9, CCDC169 |
| [[FAM133A]] | C | FAM133A activity raises FSTL5's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 4.40× lower at baseline in the lines without FAM133A | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4; co-absent with the target |
| [[MGAT4C]] | C | MGAT4C activity raises FSTL5's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 4.55× lower at baseline in the lines without MGAT4C | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |
| [[NAALADL2-AS2]] | C | NAALADL2-AS2 activity raises FSTL5's level | lines that do not express NAALADL2-AS2 (36) vs lines expressing it (14) | 4.55× lower at baseline in the lines without NAALADL2-AS2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RNF17, ENSG00000287598, SSX1; co-absent with the target |
| [[SLITRK6]] | C | SLITRK6 activity raises FSTL5's level | lines that do not express SLITRK6 (28) vs lines expressing it (22) | 3.12× lower at baseline in the lines without SLITRK6 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4; co-absent with the target |
| [[MSR1]] | C | MSR1 activity raises FSTL5's level | lines that do not express MSR1 (36) vs lines expressing it (14) | 5.06× lower at baseline in the lines without MSR1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02438, SAMMSON, ENSG00000286523; co-absent with the target |
| [[LINC01029]] | C | LINC01029 activity raises FSTL5's level | lines that do not express LINC01029 (42) vs lines expressing it (8) | 5.97× lower at baseline in the lines without LINC01029 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, LINC00879, OVAAL; co-absent with the target |
| [[DISC1FP1]] | C | DISC1FP1 activity raises FSTL5's level | lines that do not express DISC1FP1 (29) vs lines expressing it (21) | 3.30× lower at baseline in the lines without DISC1FP1 | 0.069 | ⚠ within organs, on part of the lines; also absent: FSTL5, ENSG00000250954, ENSG00000251574; co-absent with the target |
| [[RERG]] | C | RERG activity raises FSTL5's level | lines that do not express RERG (24) vs lines expressing it (26) | 2.52× lower at baseline in the lines without RERG | 0.094 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MGAT4C, ENSG00000266450; maybe low, not absent; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises FSTL5's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 2.26× lower at baseline in the lines without KCNH7 | 0.096 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[NRXN3]] | C | NRXN3 activity raises FSTL5's level | lines that do not express NRXN3 (23) vs lines expressing it (27) | 2.38× lower at baseline in the lines without NRXN3 | 0.097 | ⚠ within organs, on part of the lines; also absent: RGS7, FGF13, ENSG00000255983; co-absent with the target |
| [[LINC02506]] | C | LINC02506 activity raises FSTL5's level | lines that do not express LINC02506 (40) vs lines expressing it (10) | 3.99× lower at baseline in the lines without LINC02506 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC01610, ENSG00000241168; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 4, C 16. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNH1]] | B | FSTL5 activity raises KCNH1's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 1.73× lower at baseline in the lines without FSTL5 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2 |
| [[GALNT13]] | B | FSTL5 activity lowers GALNT13's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 1.33× higher at baseline in the lines without FSTL5 | 0.049 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2 |
| [[MID1]] | B | FSTL5 activity raises MID1's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 1.88× lower at baseline in the lines without FSTL5 | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2 |
| [[NRXN1]] | B | FSTL5 activity raises NRXN1's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 2.43× lower at baseline in the lines without FSTL5 | 0.082 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2 |
| [[FAM133A]] | C | FSTL5 activity raises FAM133A's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 3.02× lower at baseline in the lines without FSTL5 | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2; co-absent with the target |
| [[LINC01320]] | C | FSTL5 activity raises LINC01320's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 4.14× lower at baseline in the lines without FSTL5 | 0.021 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2; co-absent with the target |
| [[DISC1FP1]] | C | FSTL5 activity raises DISC1FP1's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 4.94× lower at baseline in the lines without FSTL5 | 0.023 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2; co-absent with the target |
| [[ERBB4]] | C | FSTL5 activity raises ERBB4's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 2.38× lower at baseline in the lines without FSTL5 | 0.033 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2; co-absent with the target |
| [[NFASC]] | C | FSTL5 activity raises NFASC's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 3.23× lower at baseline in the lines without FSTL5 | 0.038 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2; co-absent with the target |
| [[LINC02506]] | C | FSTL5 activity raises LINC02506's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 4.33× lower at baseline in the lines without FSTL5 | 0.038 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2; co-absent with the target |
| [[EPHA5-AS1]] | C | FSTL5 activity raises EPHA5-AS1's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 2.18× lower at baseline in the lines without FSTL5 | 0.049 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2; co-absent with the target |
| [[KCNJ6]] | C | FSTL5 activity raises KCNJ6's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 2.56× lower at baseline in the lines without FSTL5 | 0.063 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.645). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.9, 27.8); signed map (38.3, 27.1). **Vector** length 53.0, 16.8% of its response variance represented; |z| ≥ 3 in 403 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +19.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +17.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +12.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +1.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +4.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -3.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | follistatin like 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.2 — chr4:161,383,897-162,164,004 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp566D234, KIAA1263 |
| Gene groups (HGNC) | I-set domain containing; EF-hand domain containing |
| Matched by | ensembl_id |

UniProt [Q8N475](https://www.uniprot.org/uniprotkb/Q8N475) carries no function annotation.

**Summary**, from NCBI Gene [56884](https://www.ncbi.nlm.nih.gov/gene/56884):

> Predicted to enable calcium ion binding activity. Predicted to be involved in cell differentiation and regulation of BMP signaling pathway. Predicted to be active in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21386](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21386) · Entrez [56884](https://www.ncbi.nlm.nih.gov/gene/56884) · UniProt [Q8N475](https://www.uniprot.org/uniprotkb/Q8N475) · Ensembl [ENSG00000168843](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168843)

## Data

Gene col 9709: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9709); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9709, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9709]; `tensor/DDL_lfc|DDL_z.npy` [9709]; `embed/gene_vectors.npy` [9709]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9709 or target_col == 9709). Every well: [[FSTL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FSTL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

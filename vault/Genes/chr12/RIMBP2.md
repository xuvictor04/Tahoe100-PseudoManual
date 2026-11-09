---
symbol: "RIMBP2"
type: "gene"
col: 692
ensembl_id: "ENSG00000060709"
name: "RIMS binding protein 2"
location: "12q24.33"
module: 27
arm: "+"
pooled_cpm: 18.52
n_lines_expressing: 19
n_dd_up: 20
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 38
direction_downstream: 31
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# RIMBP2

*RIMS binding protein 2* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.25× (z +15.2, q 0e+00, up in 4 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.692× (z -4.9, q 7e-04, down in 9 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST18]] (+0.78, fdr 7e-06), [[RMST]] (+0.74, fdr 7e-06), [[LINC02058]] (+0.69, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 38 arrows point to it, the strongest [[RUNX1T1]] → it (grade C ⚠); 31 go from it, the strongest it → [[RGL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 692.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +15.2 | 0e+00 | 4/15 (LOX-IMVI, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.45×** | +11.2 | 1e-26 | 1/8 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +9.0 | 4e-17 | 4/15 (HS-578T, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.93×** | +8.7 | 5e-16 | 2/11 (HS-578T, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +6.0 | 2e-07 | 2/10 (HS-578T, HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +5.6 | 2e-06 | 2/16 (SNU-1, H4) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +5.3 | 9e-06 | 3/13 (COLO 205, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.37×** | +4.1 | 0.002 | 0/14 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.53×** | +4.0 | 0.004 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.007 | 4/14 (HS-578T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.010 | 2/14 (CHP-212, SW 900) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.70×** | +3.7 | 0.011 | 0/15 | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.012 | 1/14 (LOX-IMVI) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.34×** | +3.6 | 0.013 | 1/13 (HS-578T) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.019 | 7/15 (SW1417, SHP-77, …) | top dose only |  |
| [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.020 | 0/13 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.028 | 1/14 (SNU-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.064 | 1/16 (LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 692.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.692×** | -4.9 | 7e-04 | 9/15 (CHP-212, SW480, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.737×** | -4.0 | 0.015 | 8/15 (CHP-212, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.723×** | -4.0 | 0.015 | 1/15 (LOX-IMVI) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.768×** | -3.5 | 0.070 | 9/14 (SW480, SHP-77, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.773×** | -3.4 | 0.079 | 8/14 (SW480, SHP-77, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.790× | -3.1 | 0.18 | 5/14 (HS-578T, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 692. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 169 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -18.9) |
| [[COLO 205 (line)]] | alt | 21.6 | 0 | 3 (2 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0620× (z -12.3) |
| [[LS 180 (line)]] | wt | 25.6 | 0 | 3 (2 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.119× (z -11.6) |
| [[SHP-77 (line)]] | alt | 142 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -11.2) |
| [[HS-578T (line)]] | alt | 4.67 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0393× (z -11.6) |
| [[CHP-212 (line)]] | wt | 66.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 5.04 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0618× (z -10.5) ⚠ cell-cycle shift, explains ~16% of this change |
| [[SW1417 (line)]] | alt | 54.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -12.9) |
| [[A-172 (line)]] | wt | 4.11 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.78 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.08 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.42 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.88 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.46 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 692), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST18]] | +0.78 | +0.77 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[RMST]] | +0.74 | +0.70 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[LINC02058]] | +0.69 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[NKD1]] | +0.68 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[JAKMIP2-AS1]] | +0.67 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[PROX1]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1]] | +0.67 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[SMOC2]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[PROX1-AS1]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MIR3667HG]] | +0.64 | +0.50 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[VWA2]] | +0.64 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[SLC30A10]] | +0.64 | +0.53 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 0, C 38. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RUNX1T1]] | C | RUNX1T1 activity raises RIMBP2's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 3.42× lower at baseline in the lines without RUNX1T1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[JAKMIP2-AS1]] | C | JAKMIP2-AS1 activity raises RIMBP2's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 3.64× lower at baseline in the lines without JAKMIP2-AS1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[LINC02405]] | C | LINC02405 activity raises RIMBP2's level | lines that do not express LINC02405 (27) vs lines expressing it (23) | 3.29× lower at baseline in the lines without LINC02405 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000286016, ENSG00000278266, LINC02360; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises RIMBP2's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.16× lower at baseline in the lines without RIT2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[PHYHIPL]] | C | PHYHIPL activity raises RIMBP2's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 2.82× lower at baseline in the lines without PHYHIPL | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |
| [[ST18]] | C | ST18 activity raises RIMBP2's level | lines that do not express ST18 (39) vs lines expressing it (11) | 3.92× lower at baseline in the lines without ST18 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent; co-absent with the target |
| [[MIR3667HG]] | C | MIR3667HG activity raises RIMBP2's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 2.95× lower at baseline in the lines without MIR3667HG | 0.007 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[CALCA]] | C | CALCA activity raises RIMBP2's level | lines that do not express CALCA (45) vs lines expressing it (5) | 3.75× lower at baseline in the lines without CALCA | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[PCSK1]] | C | PCSK1 activity raises RIMBP2's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 3.15× lower at baseline in the lines without PCSK1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[TSHZ2]] | C | TSHZ2 activity raises RIMBP2's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 2.72× lower at baseline in the lines without TSHZ2 | 0.008 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5; co-absent with the target |
| [[HS3ST5]] | C | HS3ST5 activity raises RIMBP2's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 2.08× lower at baseline in the lines without HS3ST5 | 0.008 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises RIMBP2's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 4.63× lower at baseline in the lines without SYT4 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 1, C 30. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGL1]] | B | RIMBP2 activity raises RGL1's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 1.55× lower at baseline in the lines without RIMBP2 | 0.090 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent |
| [[PROX1-AS1]] | C | RIMBP2 activity raises PROX1-AS1's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 2.66× lower at baseline in the lines without RIMBP2 | 0.003 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent; co-absent with the target |
| [[RUNX1T1]] | C | RIMBP2 activity raises RUNX1T1's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 3.86× lower at baseline in the lines without RIMBP2 | 0.005 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent; co-absent with the target |
| [[MIR3667HG]] | C | RIMBP2 activity raises MIR3667HG's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 3.62× lower at baseline in the lines without RIMBP2 | 0.010 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent; co-absent with the target |
| [[PROX1]] | C | RIMBP2 activity raises PROX1's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 3.05× lower at baseline in the lines without RIMBP2 | 0.010 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent; co-absent with the target |
| [[NKD1]] | C | RIMBP2 activity raises NKD1's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 2.49× lower at baseline in the lines without RIMBP2 | 0.013 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent; co-absent with the target |
| [[LINC02405]] | C | RIMBP2 activity raises LINC02405's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 3.23× lower at baseline in the lines without RIMBP2 | 0.013 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent; co-absent with the target |
| [[ST18]] | C | RIMBP2 activity raises ST18's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 2.37× lower at baseline in the lines without RIMBP2 | 0.015 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent; co-absent with the target |
| [[TSHZ2]] | C | RIMBP2 activity raises TSHZ2's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 3.53× lower at baseline in the lines without RIMBP2 | 0.016 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent; co-absent with the target |
| [[PKHD1]] | C | RIMBP2 activity raises PKHD1's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 2.05× lower at baseline in the lines without RIMBP2 | 0.019 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent; co-absent with the target |
| [[LINC01622]] | C | RIMBP2 activity raises LINC01622's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 1.80× lower at baseline in the lines without RIMBP2 | 0.022 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent; co-absent with the target |
| [[RMST]] | C | RIMBP2 activity raises RMST's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 2.44× lower at baseline in the lines without RIMBP2 | 0.023 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.724). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.4, 43.8); signed map (63.3, 15.4). **Vector** length 47.2, 14.0% of its response variance represented; |z| ≥ 3 in 335 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.6 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +4.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +1.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.4 | -4.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | RIMS binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:130,396,133-130,768,228 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0318, RBP2, MGC15831, RIM-BP2, PPP1R133 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O15034](https://www.uniprot.org/uniprotkb/O15034) (RIMS-binding protein 2):

> Plays a role in the synaptic transmission as bifunctional linker that interacts simultaneously with RIMS1, RIMS2, CACNA1D and CACNA1B.

**Summary**, from NCBI Gene [23504](https://www.ncbi.nlm.nih.gov/gene/23504):

> Predicted to enable protein-macromolecule adaptor activity; voltage-gated calcium channel activity involved in regulation of presynaptic cytosolic calcium levels; and voltage-gated monoatomic ion channel activity involved in regulation of presynaptic membrane potential. Predicted to be a structural constituent of presynaptic active zone. Predicted to be involved in neuromuscular synaptic transmission; regulation of calcium-dependent activation of synaptic vesicle fusion; and regulation of …

**Accessions** — [HGNC:30339](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30339) · Entrez [23504](https://www.ncbi.nlm.nih.gov/gene/23504) · UniProt [O15034](https://www.uniprot.org/uniprotkb/O15034) · Ensembl [ENSG00000060709](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000060709)

## Data

Gene col 692: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 692); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 692, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 692]; `tensor/DDL_lfc|DDL_z.npy` [692]; `embed/gene_vectors.npy` [692]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 692 or target_col == 692). Every well: [[RIMBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIMBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

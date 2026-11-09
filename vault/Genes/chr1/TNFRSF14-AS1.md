---
symbol: "TNFRSF14-AS1"
type: "gene"
col: 14172
ensembl_id: "ENSG00000238164"
name: "TNFRSF14 antisense RNA 1"
location: "1p36.32"
module: 55
arm: "+"
pooled_cpm: 2.06
n_lines_expressing: 27
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 129
direction_downstream: 90
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# TNFRSF14-AS1

*TNFRSF14 antisense RNA 1* — 1p36.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.12× (z +8.6, q 5e-15, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.85× (z +5.5, q 6e-06, up in 3 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.417× (z -5.6, q 1e-05, down in 18 of 20 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.426× (z -5.4, q 2e-05, down in 16 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPS8L3]] (+0.79, fdr 7e-06), [[ARHGEF38]] (+0.76, fdr 7e-06), [[ABO]] (+0.76, fdr 7e-06); moves opposite to [[ITGB1BP1]] (-0.61, fdr 2e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 129 arrows point to it, the strongest [[RASSF6]] → it (grade B ⚠); 90 go from it, the strongest it → [[FUT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14172.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.12×** | +8.6 | 5e-15 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.15×** | +6.7 | 6e-09 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +6.3 | 6e-08 | 2/7 (LS 180, KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +5.5 | 6e-06 | 3/15 (HepG2/C3A, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +4.2 | 0.003 | 1/14 (KATO III) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.90×** | +4.1 | 0.005 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.27×** | +3.7 | 0.019 | 2/9 (SW480, KATO III) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.22×** | +3.6 | 0.024 | 1/9 (KATO III) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.75×** | +3.5 | 0.027 | 0/14 | top dose only | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.71×** | +3.4 | 0.045 | 3/10 (HT-29, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.2 | 0.065 | 3/14 (LS 180, COLO 205, …) | top dose only | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.61×** | +3.2 | 0.073 | 1/7 (SW480) | top dose only | noisy plate (z scaled) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | 1.65× | +3.0 | 0.10 | 1/10 (SW1417) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | 1.41× | +3.0 | 0.10 | 1/21 (HepG2/C3A) | rises with dose | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | 1.61× | +3.0 | 0.10 | 1/13 (KATO III) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14172.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.417×** | -5.6 | 1e-05 | 18/20 (KATO III, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.426×** | -5.4 | 2e-05 | 16/21 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.484×** | -4.6 | 7e-04 | 17/21 (SW480, COLO 205, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.516×** | -4.2 | 0.004 | 17/21 (SW480, KATO III, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.344×** | -3.5 | 0.042 | 12/16 (HT-29, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.577×** | -3.5 | 0.042 | 11/19 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | **0.564×** | -3.4 | 0.059 | 4/20 (RPMI-7951, SNU-423, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.700×** | -3.2 | 0.084 | 4/19 (HCT15, C32, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14172. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 6.86 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0502× (z -15.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -13.9) |
| [[COLO 205 (line)]] | alt | 9.22 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0331× (z -11.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.154× (z -9.0) |
| [[KATO III (line)]] | alt | 6.54 | 0 | 4 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0259× (z -13.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 9.50 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.106× (z -9.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 4.42 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0279× (z -13.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HT-29 (line)]] | alt | 5.30 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0359× (z -11.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 0.204 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.164 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.159 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.166 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.609 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.190 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.218 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.276 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.268 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.566 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.524 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.733 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.286 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.164 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.185 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.782 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.179 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.265 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.677 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.335 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.213 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.902 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.734 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.690 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14172), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPS8L3]] | +0.79 | +0.81 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[ARHGEF38]] | +0.76 | +0.80 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[ABO]] | +0.76 | +0.77 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[TMC4]] | +0.75 | +0.75 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[KCNE3]] | +0.74 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[IL20RA]] | +0.74 | +0.79 / +0.53 | both halves | 1e-05 |  |
| [[C9orf152]] | +0.73 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[TNFRSF14]] | +0.72 | +0.70 / +0.70 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[LINC01559]] | +0.71 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[TMPRSS2]] | +0.71 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[TMPRSS3]] | +0.71 | +0.77 / +0.58 | both halves | 7e-06 |  |
| [[SULT1C2]] | +0.70 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[PROM1]] | +0.70 | +0.72 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB1BP1]] | -0.61 | -0.54 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*129 arrows, 129 of them with an alert ⚠; grade A 0, B 35, C 94. Shown: the 12 strongest; 117 more arrows (117 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASSF6]] | B | RASSF6 activity raises TNFRSF14-AS1's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.01× lower at baseline in the lines without RASSF6 | 0.003 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[TMPRSS3]] | B | TMPRSS3 activity raises TNFRSF14-AS1's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.20× lower at baseline in the lines without TMPRSS3 | 0.004 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[DCLK2]] | B | DCLK2 activity lowers TNFRSF14-AS1's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 2.79× higher at baseline in the lines without DCLK2 | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[BAIAP2L2]] | B | BAIAP2L2 activity raises TNFRSF14-AS1's level | lines that do not express BAIAP2L2 (13) vs lines expressing it (37) | 1.78× lower at baseline in the lines without BAIAP2L2 | 0.009 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC02253]] | B | LINC02253 activity raises TNFRSF14-AS1's level | lines that do not express LINC02253 (35) vs lines expressing it (15) | 1.90× lower at baseline in the lines without LINC02253 | 0.012 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02058, ENSG00000289349 |
| [[FXYD2]] | B | FXYD2 activity raises TNFRSF14-AS1's level | lines that do not express FXYD2 (38) vs lines expressing it (12) | 1.97× lower at baseline in the lines without FXYD2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSCAML1, ITIH2, FGA |
| [[SPINT1-AS1]] | B | SPINT1-AS1 activity raises TNFRSF14-AS1's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 2.18× lower at baseline in the lines without SPINT1-AS1 | 0.015 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[ANK3]] | B | ANK3 activity raises TNFRSF14-AS1's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 1.82× lower at baseline in the lines without ANK3 | 0.015 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[CLDN3]] | B | CLDN3 activity raises TNFRSF14-AS1's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.08× lower at baseline in the lines without CLDN3 | 0.019 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[SLC44A3]] | B | SLC44A3 activity raises TNFRSF14-AS1's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 1.83× lower at baseline in the lines without SLC44A3 | 0.021 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[RORC]] | B | RORC activity raises TNFRSF14-AS1's level | lines that do not express RORC (30) vs lines expressing it (20) | 2.02× lower at baseline in the lines without RORC | 0.024 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[ANXA3]] | B | ANXA3 activity raises TNFRSF14-AS1's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 1.95× lower at baseline in the lines without ANXA3 | 0.028 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |

### Downstream of this gene

*90 arrows, 90 of them with an alert ⚠; grade A 0, B 19, C 71. Shown: the 12 strongest; 78 more arrows (78 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FUT2]] | B | TNFRSF14-AS1 activity raises FUT2's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 2.32× lower at baseline in the lines without TNFRSF14-AS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[TJP2]] | B | TNFRSF14-AS1 activity raises TJP2's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 2.66× lower at baseline in the lines without TNFRSF14-AS1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[LGR5]] | B | TNFRSF14-AS1 activity raises LGR5's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 1.71× lower at baseline in the lines without TNFRSF14-AS1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[FGD3]] | B | TNFRSF14-AS1 activity raises FGD3's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 1.80× lower at baseline in the lines without TNFRSF14-AS1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[RORC]] | B | TNFRSF14-AS1 activity raises RORC's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 1.65× lower at baseline in the lines without TNFRSF14-AS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[RAMP1]] | B | TNFRSF14-AS1 activity raises RAMP1's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 2.00× lower at baseline in the lines without TNFRSF14-AS1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[MROH6]] | B | TNFRSF14-AS1 activity raises MROH6's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 1.78× lower at baseline in the lines without TNFRSF14-AS1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[DDR1]] | B | TNFRSF14-AS1 activity raises DDR1's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 2.11× lower at baseline in the lines without TNFRSF14-AS1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[BCL2L15]] | B | TNFRSF14-AS1 activity raises BCL2L15's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 2.31× lower at baseline in the lines without TNFRSF14-AS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[CROCCP3-1]] | B | TNFRSF14-AS1 activity lowers CROCCP3-1's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 1.45× higher at baseline in the lines without TNFRSF14-AS1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[CYP3A5]] | B | TNFRSF14-AS1 activity raises CYP3A5's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 2.93× lower at baseline in the lines without TNFRSF14-AS1 | 0.065 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[SULF2]] | B | TNFRSF14-AS1 activity raises SULF2's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 2.42× lower at baseline in the lines without TNFRSF14-AS1 | 0.065 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.783). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.5, 49.2); signed map (62.0, 7.8). **Vector** length 52.2, 14.0% of its response variance represented; |z| ≥ 3 in 520 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +6.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.0 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +0.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -1.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -1.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -1.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | TNFRSF14 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p36.32 — chr1:2,549,920-2,557,031 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ENST00000416860.2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26966](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26966) · Entrez [115110](https://www.ncbi.nlm.nih.gov/gene/115110) · Ensembl [ENSG00000238164](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000238164)

## Data

Gene col 14172: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14172); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14172, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14172]; `tensor/DDL_lfc|DDL_z.npy` [14172]; `embed/gene_vectors.npy` [14172]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14172 or target_col == 14172). Every well: [[TNFRSF14-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFRSF14-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

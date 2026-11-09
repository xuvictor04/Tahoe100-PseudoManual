---
symbol: "TIMP3"
type: "gene"
col: 1899
ensembl_id: "ENSG00000100234"
name: "TIMP metallopeptidase inhibitor 3"
location: "22q12.3"
module: 66
arm: "+"
pooled_cpm: 123.6
n_lines_expressing: 17
n_dd_up: 8
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 33
direction_downstream: 48
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# TIMP3

*TIMP metallopeptidase inhibitor 3* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.58× (z +10.3, q 4e-22, up in 7 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.67× (z +6.1, q 1e-07, up in 9 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.608× (z -4.2, q 0.014, down in 11 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IGFBP5]] (+0.70, fdr 7e-06), [[ZMAT4]] (+0.66, fdr 7e-06), [[LINC01411]] (+0.65, fdr 7e-06); moves opposite to [[FOXC2]] (-0.46, fdr 4e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 33 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 48 go from it, the strongest it → [[ZCCHC24]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1899.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.58×** | +10.3 | 4e-22 | 7/16 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.37×** | +9.9 | 1e-20 | 7/14 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +6.1 | 1e-07 | 9/15 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +5.3 | 2e-05 | 5/14 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.86×** | +5.2 | 2e-05 | 10/15 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +4.7 | 2e-04 | 8/15 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +3.8 | 0.010 | 11/16 (NCI-H2347, SW 1088, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.017 | 9/15 (H4, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1899.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.608×** | -4.2 | 0.014 | 11/14 (C32, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.620×** | -4.1 | 0.014 | 8/15 (NCI-H1792, HS-578T, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.642×** | -3.8 | 0.023 | 9/14 (H4, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.643×** | -3.7 | 0.023 | 13/15 (HS-578T, NCI-H1792, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.645×** | -3.7 | 0.023 | 14/15 (HS-578T, NCI-H1792, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.653×** | -3.6 | 0.029 | 13/15 (HS-578T, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.660×** | -3.5 | 0.031 | 8/15 (C32, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.661×** | -3.5 | 0.031 | 4/15 (NCI-H1792, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.648×** | -3.4 | 0.040 | 1/15 (A-172) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.658×** | -3.4 | 0.040 | 13/15 (RPMI-7951, SW 1088, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.679×** | -3.3 | 0.054 | 9/15 (HS-578T, NCI-H1792, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.682×** | -3.2 | 0.055 | 8/15 (Hs 766T, C32, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.765×** | -3.2 | 0.056 | 11/15 (NCI-H1792, HS-578T, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.676×** | -3.2 | 0.056 | 14/15 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ciclopirox (drug)]] 0.5 µM |  | **0.695×** | -3.1 | 0.076 | 0/16 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1899. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 1,189 | 0 | 18 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.118× (z -19.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0964× (z -14.2) |
| [[H4 (line)]] | wt | 565 | 1 (1 ⚠) | 15 (11 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 5.38× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -15.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0789× (z -13.9) |
| [[C32 (line)]] | wt | 850 | 0 | 15 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0567× (z -31.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.115× (z -16.7) |
| [[RPMI-7951 (line)]] | alt | 1,429 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -17.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -13.8) |
| [[Hs 766T (line)]] | wt | 1,743 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0838× (z -26.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -16.5) |
| [[NCI-H1792 (line)]] | alt | 88.3 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -13.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 42.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +15.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 4.43× (z +15.6) | — |
| [[SK-MEL-2 (line)]] | alt | 106 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -15.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -10.9) |
| [[CHP-212 (line)]] | wt | 292 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 36.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +9.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.68× (z +8.7) | — |
| [[SW 1088 (line)]] | alt | 1,322 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0892× (z -15.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 65.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.56 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.22 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.57 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.19 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.64 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.7 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.33 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.05 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.16 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 18.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 97.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.13 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.62 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 20.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.28 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.64 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.42 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.50 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 25.1 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.93 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.49 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.25 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 24.1 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 18.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1899), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGFBP5]] | +0.70 | +0.64 / +0.75 | both halves | 7e-06 | STRING 516 |
| [[ZMAT4]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[LINC01411]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[SYN3]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 | STRING 555; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[DIRC3]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[COL1A2]] | +0.63 | +0.53 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 662 |
| [[FCRLA]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[FBN1]] | +0.61 | +0.54 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_COAGULATION; STRING 610 |
| [[DPYSL3]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[SEMA5A]] | +0.58 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[COL15A1]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[COL1A1]] | +0.58 | +0.38 / +0.71 | both halves | 7e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 684 |
| [[SIRLNT]] | +0.58 | +0.46 / +0.63 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXC2]] | -0.46 | -0.40 / -0.41 | both halves | 4e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 2, C 31. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TIMP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[ABCA13]] | B | ABCA13 activity raises TIMP3's level | lines that do not express ABCA13 (19) vs lines expressing it (31) | 3.05× lower at baseline in the lines without ABCA13 | 0.061 | ⚠ within organs, on part of the lines; also absent: SHC4, MIR3681HG, LINC02930; maybe low, not absent |
| [[HTR1F]] | C | HTR1F activity raises TIMP3's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 14.51× lower at baseline in the lines without HTR1F | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises TIMP3's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 7.22× lower at baseline in the lines without C5orf46 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises TIMP3's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 15.03× lower at baseline in the lines without AEBP1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[A2M]] | C | A2M activity raises TIMP3's level | lines that do not express A2M (42) vs lines expressing it (8) | 8.88× lower at baseline in the lines without A2M | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises TIMP3's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 6.74× lower at baseline in the lines without COL5A1 | 0.012 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[MIR3681HG]] | C | MIR3681HG activity raises TIMP3's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 6.48× lower at baseline in the lines without MIR3681HG | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent; co-absent with the target |
| [[SEMA5A]] | C | SEMA5A activity raises TIMP3's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 5.75× lower at baseline in the lines without SEMA5A | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH; co-absent with the target |
| [[IGFBP5]] | C | IGFBP5 activity raises TIMP3's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 9.02× lower at baseline in the lines without IGFBP5 | 0.016 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2; co-absent with the target |
| [[CSPG4]] | C | CSPG4 activity raises TIMP3's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 7.11× lower at baseline in the lines without CSPG4 | 0.020 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1; co-absent with the target |
| [[KC6]] | C | KC6 activity raises TIMP3's level | lines that do not express KC6 (32) vs lines expressing it (18) | 10.15× lower at baseline in the lines without KC6 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1; co-absent with the target |

### Downstream of this gene

*48 arrows, 48 of them with an alert ⚠; grade A 0, B 8, C 40. Shown: the 12 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZCCHC24]] | B | TIMP3 activity raises ZCCHC24's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 3.10× lower at baseline in the lines without TIMP3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1 |
| [[ZMIZ1]] | B | TIMP3 activity raises ZMIZ1's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 1.91× lower at baseline in the lines without TIMP3 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1 |
| [[DIRC3]] | B | TIMP3 activity raises DIRC3's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 3.52× lower at baseline in the lines without TIMP3 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1 |
| [[LDB2]] | B | TIMP3 activity raises LDB2's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 3.31× lower at baseline in the lines without TIMP3 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1 |
| [[PTHLH]] | B | TIMP3 activity weakens PTHLH's drug response | lines that do not express TIMP3 (16) vs lines expressing it (12) | the lines without TIMP3 respond 1.18× as strongly (z diff -1.07); strongest at Homoharringtonine 5 µM: 2.76x vs 0.84x (z diff -7.1) | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; target measured in part of the lines; artifact flags |
| [[SYN3]] | B | TIMP3 activity raises SYN3's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 2.18× lower at baseline in the lines without TIMP3 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1 |
| [[PTHLH]] | B | TIMP3 activity raises PTHLH's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 2.28× lower at baseline in the lines without TIMP3 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1 |
| [[SLC6A6]] | B | TIMP3 activity raises SLC6A6's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 2.53× lower at baseline in the lines without TIMP3 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1 |
| [[CSPG4]] | C | TIMP3 activity raises CSPG4's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 6.58× lower at baseline in the lines without TIMP3 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; co-absent with the target |
| [[HTR1F]] | C | TIMP3 activity raises HTR1F's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 3.10× lower at baseline in the lines without TIMP3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; co-absent with the target |
| [[CTHRC1]] | C | TIMP3 activity raises CTHRC1's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 3.36× lower at baseline in the lines without TIMP3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; co-absent with the target |
| [[AIM2]] | C | TIMP3 activity raises AIM2's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 5.06× lower at baseline in the lines without TIMP3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.442). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (51.2, 25.3); signed map (28.6, 42.8). **Vector** length 88.7, 33.7% of its response variance represented; |z| ≥ 3 in 640 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.7 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +0.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +2.8 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.3 | -4.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.2 | -3.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.2 | -3.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | TIMP metallopeptidase inhibitor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:32,801,705-32,863,041 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SFD |
| Gene groups (HGNC) | Tissue inhibitor of metallopeptidases |
| Hallmark sets | COAGULATION, APOPTOSIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [P35625](https://www.uniprot.org/uniprotkb/P35625) (Metalloproteinase inhibitor 3):

> Mediates a variety of processes including matrix regulation and turnover, inflammation, and angiogenesis, through reversible inhibition of zinc protease superfamily enzymes, primarily matrix metalloproteinases (MMPs). Regulates extracellular matrix (ECM) remodeling through inhibition of matrix metalloproteinases (MMP) including MMP-1, MMP-2, MMP-3, MMP-7, MMP-9, MMP-13, MMP-14 and MMP-15. Additionally, modulates the processing of amyloid precursor protein (APP) and apolipoprotein E receptor …

**Summary**, from NCBI Gene [7078](https://www.ncbi.nlm.nih.gov/gene/7078):

> This gene belongs to the TIMP gene family. The proteins encoded by this gene family are inhibitors of the matrix metalloproteinases, a group of peptidases involved in degradation of the extracellular matrix (ECM). Expression of this gene is induced in response to mitogenic stimulation and this netrin domain-containing protein is localized to the ECM. Mutations in this gene have been associated with the autosomal dominant disorder Sorsby's fundus dystrophy. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11822](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11822) · Entrez [7078](https://www.ncbi.nlm.nih.gov/gene/7078) · UniProt [P35625](https://www.uniprot.org/uniprotkb/P35625) · Ensembl [ENSG00000100234](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100234)

## Data

Gene col 1899: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1899); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1899, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1899]; `tensor/DDL_lfc|DDL_z.npy` [1899]; `embed/gene_vectors.npy` [1899]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1899 or target_col == 1899). Every well: [[TIMP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

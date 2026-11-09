---
symbol: "CHD1L"
type: "gene"
col: 5244
ensembl_id: "ENSG00000131778"
name: "chromodomain helicase DNA binding protein 1 like"
location: "1q21.1"
module: 84
arm: "+"
pooled_cpm: 110.56
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 36
n_dd_up_clean: 1
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 14
direction_downstream: 0
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# CHD1L

*chromodomain helicase DNA binding protein 1 like* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Dimethyl fumarate (drug)]] 5 µM: 1.31× (z +4.6, q 0.002, up in 28 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.517× (z -16.4, q 0e+00, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PYGL]] (+0.68, fdr 7e-06), [[CEP170]] (+0.64, fdr 1e-05), [[TRIM9]] (+0.60, fdr 3e-05); moves opposite to [[ARHGEF34P]] (-0.56, fdr 3e-05), [[PSORS1C1]] (-0.56, fdr 4e-05), [[ARHGEF5]] (-0.56, fdr 3e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[SPOCK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5244.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.31×** | +4.6 | 0.002 | 28/49 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift |
| [[TAK-901 (drug)]] 5 µM |  | 1.47× | +3.6 | 0.10 | 22/49 (AsPC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 1.41× | +3.2 | 0.27 | 17/48 (A-427, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 1.20× | +3.1 | 0.27 | 14/48 (NCI-H23, A549, …) | top dose only | position effect removed |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.19× | +3.0 | 0.27 | 17/48 (A-172, Hs 766T, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5244.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.517×** | -16.4 | 0e+00 | 38/48 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.536×** | -15.5 | 0e+00 | 40/49 (NCI-H1792, C32, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.604×** | -12.5 | 1e-33 | 44/48 (A-427, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.527×** | -11.3 | 2e-27 | 38/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.527×** | -11.3 | 2e-27 | 39/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.546×** | -10.2 | 1e-22 | 40/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.593×** | -9.2 | 4e-18 | 35/48 (NCI-H1792, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.707×** | -8.6 | 6e-16 | 34/48 (C32, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.671×** | -6.7 | 1e-09 | 34/47 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.683×** | -6.7 | 1e-09 | 31/48 (C32, hTERT-HPNE, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.689×** | -6.3 | 2e-08 | 33/48 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.707×** | -5.9 | 2e-07 | 34/50 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.765×** | -5.7 | 6e-07 | 29/48 (A-172, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.729×** | -5.5 | 1e-06 | 26/48 (NCI-H1792, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.733×** | -5.5 | 2e-06 | 28/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.737×** | -5.3 | 3e-06 | 31/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5244. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 163 | 0 | 22 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -19.8) |
| [[C32 (line)]] | wt | 226 | 0 | 20 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -23.4) |
| [[hTERT-HPNE (line)]] | wt | 160 | 0 | 16 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -18.5) |
| [[HOP62 (line)]] | alt | 207 | 0 | 15 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -17.8) |
| [[NCI-H1792 (line)]] | alt | 291 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -30.7) |
| [[NCI-H460 (line)]] | wt | 243 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -24.6) |
| [[HS-578T (line)]] | alt | 110 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -16.9) |
| [[H4 (line)]] | wt | 192 | 0 | 11 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -13.2) |
| [[MIA PaCa-2 (line)]] | alt | 114 | 0 | 7 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.400× (z -13.1) |
| [[LOX-IMVI (line)]] | wt | 136 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -18.7) |
| [[RKO (line)]] | wt | 110 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -15.3) |
| [[A549 (line)]] | wt | 120 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -13.7) |
| [[NCI-H23 (line)]] | alt | 221 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -18.8) |
| [[PANC-1 (line)]] | alt | 109 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -14.9) |
| [[RPMI-7951 (line)]] | alt | 106 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -14.2) |
| [[Hs 766T (line)]] | wt | 89.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -13.2) |
| [[SHP-77 (line)]] | alt | 217 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 209 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -17.3) |
| [[SNU-1 (line)]] | wt | 157 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -15.4) |
| [[SW 900 (line)]] | alt | 159 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -13.7) |
| [[A-427 (line)]] | wt | 100 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.392× (z -16.7) |
| [[C-33 A (line)]] | alt | 122 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.377× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 115 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -12.1) |
| [[SW 1088 (line)]] | alt | 100 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 82.2 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.441× (z -9.0) |
| [[J82 (line)]] | alt | 56.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -9.5) |
| [[LoVo (line)]] | wt | 75.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.391× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 68.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -12.7) |
| [[SNU-423 (line)]] | alt | 63.0 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.467× (z -8.7) |
| [[A498 (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 90.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 97.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 65.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5244), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYGL]] | +0.68 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[CEP170]] | +0.64 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[TRIM9]] | +0.60 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[LINC03047]] | +0.60 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[LOXL2]] | +0.60 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[TFB1M]] | +0.60 | +0.61 / +0.34 | both halves | 1e-04 |  |
| [[CHSY1]] | +0.59 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[COL13A1]] | +0.59 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[UBA6]] | +0.57 | +0.66 / +0.40 | both halves | 5e-05 |  |
| [[TMEM255B]] | +0.57 | +0.63 / +0.39 | both halves | 5e-05 |  |
| [[BOLA3]] | +0.55 | +0.41 / +0.39 | both halves | 5e-05 |  |
| [[INSYN2B]] | +0.55 | +0.59 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF34P]] | -0.56 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[PSORS1C1]] | -0.56 | -0.40 / -0.53 | both halves | 4e-05 |  |
| [[ARHGEF5]] | -0.56 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[MUC20]] | -0.55 | -0.60 / -0.37 | both halves | 9e-05 |  |
| [[N4BP2L2]] | -0.54 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[RNF103]] | -0.54 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[TMC4]] | -0.52 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[KANSL1L]] | -0.51 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[DAZAP2]] | -0.51 | -0.51 / -0.24 | both halves | 5e-04 |  |
| [[HNF4G]] | -0.51 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[ACTR3C]] | -0.50 | -0.53 / -0.23 | both halves | 5e-04 |  |
| [[OCLN]] | -0.50 | -0.34 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPOCK1]] | B | SPOCK1 activity raises CHD1L's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 1.96× lower at baseline in the lines without SPOCK1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[SGIP1]] | B | SGIP1 activity raises CHD1L's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 1.75× lower at baseline in the lines without SGIP1 | 0.012 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG |
| [[BRSK1]] | B | BRSK1 activity raises CHD1L's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 2.20× lower at baseline in the lines without BRSK1 | 0.017 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[OCLN]] | B | OCLN activity lowers CHD1L's level | lines that do not express OCLN (19) vs lines expressing it (31) | 1.72× higher at baseline in the lines without OCLN | 0.025 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |
| [[TMC4]] | B | TMC4 activity lowers CHD1L's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 1.81× higher at baseline in the lines without TMC4 | 0.033 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[ATP8B3]] | B | ATP8B3 activity raises CHD1L's level | lines that do not express ATP8B3 (5) vs lines expressing it (45) | 2.39× lower at baseline in the lines without ATP8B3 | 0.036 | ⚠ within organs, on part of the lines; also absent: CEP85L, PARP3, SOAT1; maybe low, not absent |
| [[ITPR1]] | B | ITPR1 activity raises CHD1L's level | lines that do not express ITPR1 (15) vs lines expressing it (35) | 2.11× lower at baseline in the lines without ITPR1 | 0.043 | ⚠ within organs, on part of the lines; also absent: SPART-AS1, CCDC169, SPART; maybe low, not absent |
| [[MPP2]] | B | MPP2 activity raises CHD1L's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 2.22× lower at baseline in the lines without MPP2 | 0.043 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[TOP2A]] | B | TOP2A activity raises CHD1L's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MUC20]] | B | MUC20 activity lowers CHD1L's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 1.84× higher at baseline in the lines without MUC20 | 0.048 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[LRRC8C]] | B | LRRC8C activity raises CHD1L's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 1.98× lower at baseline in the lines without LRRC8C | 0.062 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[TMC4]] | B | TMC4 activity weakens CHD1L's drug response | lines that do not express TMC4 (26) vs lines expressing it (23) | the lines without TMC4 respond 2.26× as strongly (z diff -3.77); strongest at Panobinostat 5 µM: 0.36x vs 0.76x (z diff -5.5) | 0.070 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (54.7, 6.1); signed map (-4.7, 54.0). **Vector** length 123, 41.3% of its response variance represented; |z| ≥ 3 in 1,598 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.5 | -0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.3 | -2.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.5 | -11.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.3 | -9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.3 | -1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.5 | +2.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.4 | +2.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +0.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.7 | -5.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.5 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.1 | -5.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.9 | -5.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.9 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.5 | -5.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -4.3 | -4.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.0 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.0 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | chromodomain helicase DNA binding protein 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.1 — chr1:147,242,654-147,295,765 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ALC1 |
| Gene groups (HGNC) | SNF2 related family; Macro domain containing |
| Reactome | 5 pathways, smallest: Dual Incision in GG-NER; Formation of Incision Complex in GG-NER; Global Genome Nucleotide Excision Repair (GG-NER) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86WJ1](https://www.uniprot.org/uniprotkb/Q86WJ1) (ATP-dependent chromatin remodeler CHD1L):

> ATP-dependent chromatin remodeler that mediates chromatin-remodeling following DNA damage. Recruited to DNA damage sites through interaction with poly-ADP-ribose: specifically recognizes and binds histones that are poly-ADP-ribosylated on serine residues in response to DNA damage. Poly-ADP-ribose-binding activates the ATP-dependent chromatin remodeler activity, thereby regulating chromatin during DNA repair. Catalyzes nucleosome sliding away from DNA breaks in an ATP-dependent manner. Chromatin …

**Summary**, from NCBI Gene [9557](https://www.ncbi.nlm.nih.gov/gene/9557):

> This gene encodes a DNA helicase protein involved in DNA repair. The protein converts ATP to add poly(ADP-ribose) as it regulates chromatin relaxation following DNA damage. Overexpression of this gene has been linked to several types of cancers. [provided by RefSeq, Feb 2017]

**Accessions** — [HGNC:1916](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1916) · Entrez [9557](https://www.ncbi.nlm.nih.gov/gene/9557) · UniProt [Q86WJ1](https://www.uniprot.org/uniprotkb/Q86WJ1) · Ensembl [ENSG00000131778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131778)

## Data

Gene col 5244: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5244); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5244, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5244]; `tensor/DDL_lfc|DDL_z.npy` [5244]; `embed/gene_vectors.npy` [5244]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5244 or target_col == 5244). Every well: [[CHD1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHD1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "CRTAC1"
type: "gene"
col: 1752
ensembl_id: "ENSG00000095713"
name: "cartilage acidic protein 1"
location: "10q24.2"
module: 112
arm: "+"
pooled_cpm: 9.88
n_lines_expressing: 23
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 14
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 12
direction_downstream: 12
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# CRTAC1

*cartilage acidic protein 1* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.39× (z +15.7, q 0e+00, up in 13 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 0.559× (z -5.3, q 7e-05, down in 17 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYP26B1]] (+0.68, fdr 1e-05), [[C15orf48]] (+0.66, fdr 7e-06), [[CPAMD8]] (+0.65, fdr 1e-05); moves opposite to [[ARMC8]] (-0.54, fdr 2e-05), [[ZZZ3]] (-0.52, fdr 3e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[PDGFB]] → it (grade B ⚠); 12 go from it, the strongest it → cells under [[Almonertinib (hydrochloride) (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1752.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.39×** | +15.7 | 0e+00 | 13/18 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.90×** | +13.7 | 3e-40 | 19/20 (PANC-1, C32, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.57×** | +12.1 | 1e-31 | 12/20 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.79×** | +9.3 | 2e-18 | 4/14 (Panc 03.27, HOP62, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.60×** | +8.0 | 1e-13 | 2/11 (HOP62, PANC-1) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +7.3 | 2e-11 | 2/11 (HOP62, CFPAC-1) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.54×** | +7.2 | 6e-11 | 14/19 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.10×** | +6.7 | 1e-09 | 14/20 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.12×** | +6.6 | 3e-09 | 12/20 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.94×** | +6.0 | 1e-07 | 13/20 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.0 | 0.003 | 7/19 (HOP62, SK-MEL-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.006 | 5/17 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +3.8 | 0.006 | 5/18 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.015 | 9/20 (CFPAC-1, NCI-H460, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **2.04×** | +3.4 | 0.026 | 7/17 (HOP62, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.086 | 6/20 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.100 | 9/20 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1752.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.559×** | -5.3 | 7e-05 | 17/20 (NCI-H1792, RPMI-7951, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.579×** | -5.0 | 2e-04 | 9/19 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.585×** | -4.9 | 2e-04 | 11/19 (NCI-H1792, H4, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.662×** | -3.8 | 0.025 | 10/17 (NCI-H1792, SNU-423, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.672×** | -3.6 | 0.032 | 13/19 (NCI-H1792, A549, …) | all doses, flat |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.674×** | -3.6 | 0.032 | 7/20 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.766×** | -3.4 | 0.048 | 12/20 (NCI-H1792, A549, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.693×** | -3.3 | 0.061 | 9/20 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.703×** | -3.2 | 0.087 | 5/20 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.689×** | -3.1 | 0.099 | 12/17 (NCI-H1792, CFPAC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.713× | -3.1 | 0.11 | 8/19 (SW 900, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 0.05 µM |  | 0.718× | -3.0 | 0.12 | 8/19 (A549, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1752. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 38.2 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0453× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0654× (z -11.3) |
| [[A549 (line)]] | wt | 121 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0298× (z -23.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0469× (z -10.5) |
| [[PANC-1 (line)]] | alt | 3.94 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 11.3× (z +13.5) | — |
| [[NCI-H460 (line)]] | wt | 7.65 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +13.1) | [[Digitoxin (drug)]] 5 µM 0.0988× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 116 | 0 | 3 | — | [[PH-797804 (drug)]] 5 µM 0.0518× (z -10.3) |
| [[BT-474 (line)]] | alt | 5.43 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.5× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 15.3 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 6.09× (z +10.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.0323× (z -11.3) |
| [[C32 (line)]] | wt | 18.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.56× (z +11.5) | — |
| [[HEC-1-A (line)]] | alt | 2.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.58× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 17.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +9.1) | — |
| [[J82 (line)]] | alt | 18.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 9.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.43× (z +9.7) | — |
| [[A-172 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.972 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.25 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1752), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP26B1]] | +0.68 | +0.49 / +0.75 | both halves | 1e-05 |  |
| [[C15orf48]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CPAMD8]] | +0.65 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[HMGN2P46]] | +0.64 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[TMOD1]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[IL1B]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[IL1A]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[IRF4]] | +0.59 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ADAM7-AS1]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[WNT7B]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[PTGS2]] | +0.58 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[RPLP0P2]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC8]] | -0.54 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ZZZ3]] | -0.52 | -0.45 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 1, C 11.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFB]] | B | PDGFB activity raises CRTAC1's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 2.09× lower at baseline in the lines without PDGFB | 0.069 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[MAF]] | C | MAF activity raises CRTAC1's level | lines that do not express MAF (27) vs lines expressing it (23) | 3.57× lower at baseline in the lines without MAF | 0.011 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1; co-absent with the target |
| [[CRLF2]] | C | CRLF2 activity raises CRTAC1's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 3.94× lower at baseline in the lines without CRLF2 | 0.025 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR; co-absent with the target |
| [[ANXA10]] | C | ANXA10 activity raises CRTAC1's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 2.60× lower at baseline in the lines without ANXA10 | 0.032 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP; co-absent with the target |
| [[WNT7B]] | C | WNT7B activity raises CRTAC1's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 2.21× lower at baseline in the lines without WNT7B | 0.033 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG; co-absent with the target |
| [[ZMAT4]] | C | ZMAT4 activity raises CRTAC1's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 3.15× lower at baseline in the lines without ZMAT4 | 0.048 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11; co-absent with the target |
| [[IGFBP3]] | C | IGFBP3 activity raises CRTAC1's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 3.05× lower at baseline in the lines without IGFBP3 | 0.048 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF; co-absent with the target |
| [[AADACP1]] | C | AADACP1 activity raises CRTAC1's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 2.66× lower at baseline in the lines without AADACP1 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1; co-absent with the target |
| [[SCUBE1]] | C | SCUBE1 activity raises CRTAC1's level | lines that do not express SCUBE1 (28) vs lines expressing it (22) | 2.46× lower at baseline in the lines without SCUBE1 | 0.060 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MEG3, GREM1; co-absent with the target |
| [[ACKR3]] | C | ACKR3 activity raises CRTAC1's level | lines that do not express ACKR3 (30) vs lines expressing it (20) | 2.96× lower at baseline in the lines without ACKR3 | 0.070 | ⚠ within organs, on part of the lines; also absent: IGFN1, ITGA11, NCAM1; co-absent with the target |
| [[LINC01583]] | C | LINC01583 activity raises CRTAC1's level | lines that do not express LINC01583 (28) vs lines expressing it (22) | 3.24× lower at baseline in the lines without LINC01583 | 0.079 | ⚠ within organs, on part of the lines; also absent: INSYN2B, ADAM12, ZEB2; co-absent with the target |
| [[RUBCNL]] | C | RUBCNL activity raises CRTAC1's level | lines that do not express RUBCNL (30) vs lines expressing it (20) | 1.95× lower at baseline in the lines without RUBCNL | 0.088 | ⚠ within organs, on part of the lines; also absent: LINC01967, LRRN1, CADPS; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 6, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Almonertinib (hydrochloride) (drug)]] 5 µM | B | CRTAC1 activity lowers the cells' numbers under Almonertinib (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express CRTAC1 (27) vs lines expressing it (21) | the lines without CRTAC1: 1.08× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2 |
| [[SERPINB1]] | B | CRTAC1 activity raises SERPINB1's level | lines that do not express CRTAC1 (27) vs lines expressing it (23) | 1.18× lower at baseline in the lines without CRTAC1 | 0.071 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2 |
| [[SH3GL3]] | B | CRTAC1 activity strengthens SH3GL3's drug response | lines that do not express CRTAC1 (10) vs lines expressing it (16) | the lines without CRTAC1 respond 0.67× as strongly (z diff +1.92); strongest at Panobinostat 5 µM: 2.78x vs 6.70x (z diff +3.2) | 0.071 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2; target measured in part of the lines; artifact flags |
| [[AADACL2-AS1]] | B | CRTAC1 activity raises AADACL2-AS1's level | lines that do not express CRTAC1 (27) vs lines expressing it (23) | 1.33× lower at baseline in the lines without CRTAC1 | 0.088 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2 |
| [[ITPR1]] | B | CRTAC1 activity raises ITPR1's level | lines that do not express CRTAC1 (27) vs lines expressing it (23) | 2.71× lower at baseline in the lines without CRTAC1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2 |
| [[RABGEF1P3]] | B | CRTAC1 activity raises RABGEF1P3's level | lines that do not express CRTAC1 (27) vs lines expressing it (23) | 1.44× lower at baseline in the lines without CRTAC1 | 0.097 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2 |
| [[HMGN2P46]] | C | CRTAC1 activity raises HMGN2P46's level | lines that do not express CRTAC1 (27) vs lines expressing it (23) | 3.70× lower at baseline in the lines without CRTAC1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2; co-absent with the target |
| [[MAF]] | C | CRTAC1 activity raises MAF's level | lines that do not express CRTAC1 (27) vs lines expressing it (23) | 3.90× lower at baseline in the lines without CRTAC1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2; co-absent with the target |
| [[ATP6V0D2]] | C | CRTAC1 activity raises ATP6V0D2's level | lines that do not express CRTAC1 (27) vs lines expressing it (23) | 2.47× lower at baseline in the lines without CRTAC1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2; co-absent with the target |
| [[ACKR3]] | C | CRTAC1 activity raises ACKR3's level | lines that do not express CRTAC1 (27) vs lines expressing it (23) | 2.34× lower at baseline in the lines without CRTAC1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2; co-absent with the target |
| [[IGFBP3]] | C | CRTAC1 activity raises IGFBP3's level | lines that do not express CRTAC1 (27) vs lines expressing it (23) | 4.26× lower at baseline in the lines without CRTAC1 | 0.073 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2; co-absent with the target |
| [[BEX4]] | C | CRTAC1 activity raises BEX4's level | lines that do not express CRTAC1 (27) vs lines expressing it (23) | 2.41× lower at baseline in the lines without CRTAC1 | 0.099 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2; co-absent with the target |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.4, 0.3); signed map (40.3, 11.4). **Vector** length 74.6, 23.2% of its response variance represented; |z| ≥ 3 in 655 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-4 and Interleukin-13 signaling* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +13.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +15.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +1.2 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -2.9 | -5.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.8 | -5.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.4 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -3.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.4 | -2.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | cartilage acidic protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.2 — chr10:97,865,000-98,030,828 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10320, CEP-68, ASPIC1 |
| Matched by | ensembl_id |

UniProt [Q9NQ79](https://www.uniprot.org/uniprotkb/Q9NQ79) carries no function annotation.

**Summary**, from NCBI Gene [55118](https://www.ncbi.nlm.nih.gov/gene/55118):

> This gene encodes a glycosylated extracellular matrix protein that is found in the interterritorial matrix of articular deep zone cartilage. This protein is used as a marker to distinguish chondrocytes from osteoblasts and mesenchymal stem cells in culture. The presence of FG-GAP motifs and an RGD integrin-binding motif suggests that this protein may be involved in cell-cell or cell-matrix interactions. Copy number alterations in this gene have been observed in neurofibromatosis type …

**Accessions** — [HGNC:14882](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14882) · Entrez [55118](https://www.ncbi.nlm.nih.gov/gene/55118) · UniProt [Q9NQ79](https://www.uniprot.org/uniprotkb/Q9NQ79) · Ensembl [ENSG00000095713](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095713)

## Data

Gene col 1752: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1752); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1752, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1752]; `tensor/DDL_lfc|DDL_z.npy` [1752]; `embed/gene_vectors.npy` [1752]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1752 or target_col == 1752). Every well: [[CRTAC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRTAC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

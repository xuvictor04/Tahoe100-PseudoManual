---
symbol: "TNFAIP6"
type: "gene"
col: 4450
ensembl_id: "ENSG00000123610"
name: "TNF alpha induced protein 6"
location: "2q23.3"
module: 14
arm: "+"
pooled_cpm: 8.23
n_lines_expressing: 19
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 22
direction_downstream: 31
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# TNFAIP6

*TNF alpha induced protein 6* — 2q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.89× (z +15.5, q 0e+00, up in 14 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 0.217×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OLR1]] (+0.73, fdr 7e-06), [[LINC02605]] (+0.66, fdr 7e-06), [[ROS1]] (+0.66, fdr 7e-06); moves opposite to [[AK5]] (-0.55, fdr 3e-05), [[FXYD5]] (-0.51, fdr 1e-05), [[ENG]] (-0.50, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[VASN]] → it (grade B ⚠); 31 go from it, the strongest it → [[NINJ1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4450.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.89×** | +15.5 | 0e+00 | 14/15 (hTERT-HPNE, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.20×** | +11.3 | 3e-27 | 13/15 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.37×** | +10.7 | 3e-24 | 16/16 (C32, hTERT-HPNE, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **5.02×** | +9.6 | 9e-20 | 15/15 (J82, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.53×** | +9.0 | 2e-17 | 1/6 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.58×** | +7.6 | 3e-12 | 8/10 (J82, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.31×** | +7.4 | 1e-11 | 9/14 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.14×** | +7.1 | 1e-10 | 1/10 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.40×** | +7.0 | 1e-10 | 1/7 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +6.7 | 1e-09 | 5/13 (hTERT-HPNE, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **6.72×** | +6.2 | 3e-08 | 11/16 (J82, hTERT-HPNE, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.55×** | +5.8 | 3e-07 | 15/16 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.44×** | +5.5 | 1e-06 | 13/16 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Trametinib (drug)]] 5 µM |  | **2.03×** | +4.8 | 8e-05 | 12/17 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.91×** | +4.6 | 1e-04 | 10/16 (HOP62, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.65×** | +4.4 | 4e-04 | 5/16 (A-172, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.02×** | +4.4 | 4e-04 | 11/16 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **2.00×** | +4.2 | 0.001 | 9/17 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.79×** | +3.6 | 0.009 | 5/15 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.79×** | +3.6 | 0.009 | 10/16 (HOP62, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4450.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 0.217×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.588× | -3.3 | 0.53 | 4/16 (NCI-H1792, SW 900, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.605× | -3.1 | 0.53 | 9/16 (NCI-H1792, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4450. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 116 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -8.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.02 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 112× (z +17.3) | — |
| [[hTERT-HPNE (line)]] | wt | 26.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 47.0× (z +17.7) | — |
| [[J82 (line)]] | alt | 8.22 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 63.7× (z +14.0) | — |
| [[HS-578T (line)]] | alt | 22.0 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 23.1× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 4.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 65.4× (z +12.6) | — |
| [[A-427 (line)]] | wt | 0.428 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.906 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.867 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.715 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.610 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.894 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.891 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.878 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.566 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.595 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.675 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.535 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4450), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OLR1]] | +0.73 | +0.61 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[LINC02605]] | +0.66 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[ROS1]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[CFH]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[TNFAIP2]] | +0.64 | +0.57 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 508 |
| [[SOD2]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 412 |
| [[KYNU]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[LUM]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[VCAM1]] | +0.63 | +0.64 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[GBP2]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[AKR1B1]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[SLC2A6]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AK5]] | -0.55 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[FXYD5]] | -0.51 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ENG]] | -0.50 | -0.53 / -0.45 | both halves | 3e-05 | STRING 496 |
| [[PCYT1A]] | -0.50 | -0.50 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 7, C 15. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VASN]] | B | VASN activity lowers TNFAIP6's level | lines that do not express VASN (6) vs lines expressing it (44) | 1.17× higher at baseline in the lines without VASN | 0.031 | ⚠ within organs, on part of the lines; also absent: PAQR7, DBN1, C5AR1; maybe low, not absent |
| [[IL32]] | B | IL32 activity raises TNFAIP6's level | lines that do not express IL32 (18) vs lines expressing it (32) | 2.05× lower at baseline in the lines without IL32 | 0.048 | ⚠ within organs, on part of the lines; also absent: PODXL, APOL1, F3 |
| [[LINC02605]] | B | LINC02605 activity raises TNFAIP6's level | lines that do not express LINC02605 (15) vs lines expressing it (35) | 2.56× lower at baseline in the lines without LINC02605 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000285744, FAR2, ENSG00000285517 |
| [[C1QTNF1-AS1]] | B | C1QTNF1-AS1 activity raises TNFAIP6's level | lines that do not express C1QTNF1-AS1 (24) vs lines expressing it (26) | 2.13× lower at baseline in the lines without C1QTNF1-AS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ADAMTS12, ENSG00000287335, FBLN2; maybe low, not absent |
| [[NEDD9]] | B | NEDD9 activity raises TNFAIP6's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 2.08× lower at baseline in the lines without NEDD9 | 0.069 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[NEURL3]] | B | NEURL3 activity raises TNFAIP6's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 2.20× lower at baseline in the lines without NEURL3 | 0.080 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[MLPH]] | B | MLPH activity raises TNFAIP6's level | lines that do not express MLPH (13) vs lines expressing it (37) | 2.10× lower at baseline in the lines without MLPH | 0.085 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[IRAG2]] | C | IRAG2 activity raises TNFAIP6's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 3.89× lower at baseline in the lines without IRAG2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411; co-absent with the target |
| [[ZEB2]] | C | ZEB2 activity raises TNFAIP6's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 3.86× lower at baseline in the lines without ZEB2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[SSTR2]] | C | SSTR2 activity raises TNFAIP6's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 2.27× lower at baseline in the lines without SSTR2 | 0.012 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517; co-absent with the target |
| [[GBP5]] | C | GBP5 activity raises TNFAIP6's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 3.32× lower at baseline in the lines without GBP5 | 0.019 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3; co-absent with the target |
| [[ROS1]] | C | ROS1 activity raises TNFAIP6's level | lines that do not express ROS1 (30) vs lines expressing it (20) | 2.72× lower at baseline in the lines without ROS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: COL1A1, APCDD1L, GYPC; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 15, C 16. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NINJ1]] | B | TNFAIP6 activity raises NINJ1's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 2.87× lower at baseline in the lines without TNFAIP6 | 3e-04 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF |
| [[GBP2]] | B | TNFAIP6 activity raises GBP2's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 3.12× lower at baseline in the lines without TNFAIP6 | 0.009 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF |
| [[LINC02605]] | B | TNFAIP6 activity raises LINC02605's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 2.75× lower at baseline in the lines without TNFAIP6 | 0.017 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF |
| [[SOD2]] | B | TNFAIP6 activity raises SOD2's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 2.10× lower at baseline in the lines without TNFAIP6 | 0.033 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF |
| [[NEURL3]] | B | TNFAIP6 activity raises NEURL3's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 1.64× lower at baseline in the lines without TNFAIP6 | 0.038 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF |
| [[GBP1]] | B | TNFAIP6 activity raises GBP1's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 3.24× lower at baseline in the lines without TNFAIP6 | 0.039 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF |
| [[C12orf50]] | B | TNFAIP6 activity raises C12orf50's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 1.59× lower at baseline in the lines without TNFAIP6 | 0.040 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF |
| [[IL15]] | B | TNFAIP6 activity raises IL15's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 2.15× lower at baseline in the lines without TNFAIP6 | 0.067 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF |
| [[MLPH]] | B | TNFAIP6 activity raises MLPH's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 2.59× lower at baseline in the lines without TNFAIP6 | 0.068 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF |
| [[PCYT1A]] | B | TNFAIP6 activity weakens PCYT1A's drug response | lines that do not express TNFAIP6 (31) vs lines expressing it (18) | the lines without TNFAIP6 respond 1.53× as strongly (z diff -1.47); strongest at Panobinostat 5 µM: 1.52x vs 1.06x (z diff -3.9) | 0.071 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF; target measured in part of the lines; artifact flags |
| [[FXYD5]] | B | TNFAIP6 activity raises FXYD5's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 2.30× lower at baseline in the lines without TNFAIP6 | 0.073 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF |
| [[GATA6]] | B | TNFAIP6 activity raises GATA6's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 1.50× lower at baseline in the lines without TNFAIP6 | 0.079 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.659). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.5, 22.6); signed map (45.9, 21.4). **Vector** length 63.7, 23.3% of its response variance represented; |z| ≥ 3 in 443 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +10.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.1 | +9.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +15.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +4.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +3.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.3 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -0.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -0.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.3 | -1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | TNF alpha induced protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q23.3 — chr2:151,357,592-151,380,046 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TSG6, TSG-6 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | INFLAMMATORY_RESPONSE, INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P98066](https://www.uniprot.org/uniprotkb/P98066) (Tumor necrosis factor-inducible gene 6 protein):

> Major regulator of extracellular matrix organization during tissue remodeling. Catalyzes the transfer of a heavy chain (HC) from inter-alpha-inhibitor (I-alpha-I) complex to hyaluronan. Cleaves the ester bond between the C-terminus of the HC and GalNAc residue of the chondroitin sulfate chain in I-alpha-I complex followed by transesterification of the HC to hyaluronan. In the process, potentiates the antiprotease function of I-alpha-I complex through release of free bikunin. Acts as a catalyst …

**Summary**, from NCBI Gene [7130](https://www.ncbi.nlm.nih.gov/gene/7130):

> The protein encoded by this gene is a secretory protein that contains a hyaluronan-binding domain, and thus is a member of the hyaluronan-binding protein family. The hyaluronan-binding domain is known to be involved in extracellular matrix stability and cell migration. This protein has been shown to form a stable complex with inter-alpha-inhibitor (I alpha I), and thus enhance the serine protease inhibitory activity of I alpha I, which is important in the protease network associated with …

**Accessions** — [HGNC:11898](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11898) · Entrez [7130](https://www.ncbi.nlm.nih.gov/gene/7130) · UniProt [P98066](https://www.uniprot.org/uniprotkb/P98066) · Ensembl [ENSG00000123610](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123610)

## Data

Gene col 4450: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4450); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4450, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4450]; `tensor/DDL_lfc|DDL_z.npy` [4450]; `embed/gene_vectors.npy` [4450]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4450 or target_col == 4450). Every well: [[TNFAIP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFAIP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

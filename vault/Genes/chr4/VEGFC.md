---
symbol: "VEGFC"
type: "gene"
col: 7448
ensembl_id: "ENSG00000150630"
name: "vascular endothelial growth factor C"
location: "4q34.3"
module: 13
arm: "+"
pooled_cpm: 95.73
n_lines_expressing: 28
n_dd_up: 0
n_dd_down: 60
n_dd_up_clean: 0
n_dd_down_clean: 47
in_vector_space: true
direction_upstream: 43
direction_downstream: 26
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# VEGFC

*vascular endothelial growth factor C* — 4q34.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 60 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.0652× (z -28.6, q 0e+00, down in 26 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GJA1]] (+0.72, fdr 7e-06), [[KIRREL3]] (+0.69, fdr 7e-06), [[ADAMTS6]] (+0.68, fdr 7e-06); moves opposite to [[ACSL1]] (-0.59, fdr 1e-05), [[FGD4]] (-0.55, fdr 1e-05), [[PHKA1]] (-0.53, fdr 2e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 43 arrows point to it, the strongest [[ANTXR2]] → it (grade B ⚠); 26 go from it, the strongest it → [[CD44]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 60 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7448.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.0652×** | -28.6 | 0e+00 | 26/26 (C-33 A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.0839×** | -25.9 | 0e+00 | 26/26 (C-33 A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.138×** | -20.7 | 0e+00 | 26/26 (C-33 A, SW 900, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.252×** | -20.4 | 0e+00 | 26/27 (NCI-H1792, C-33 A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.209×** | -16.0 | 0e+00 | 25/26 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.245×** | -14.1 | 3e-43 | 22/24 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.362×** | -10.6 | 2e-24 | 25/26 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.342×** | -10.4 | 3e-23 | 21/24 (C-33 A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.428×** | -8.8 | 6e-17 | 22/26 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.430×** | -8.8 | 7e-17 | 23/26 (MIA PaCa-2, H4, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.469×** | -7.6 | 2e-12 | 24/28 (MIA PaCa-2, C-33 A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.470×** | -7.6 | 2e-12 | 23/26 (MIA PaCa-2, hTERT-HPNE, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.602×** | -7.4 | 4e-12 | 17/26 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.487×** | -7.1 | 6e-11 | 25/26 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.501×** | -6.9 | 2e-10 | 22/25 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.542×** | -6.4 | 6e-09 | 22/26 (HOP62, PANC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.544×** | -6.3 | 7e-09 | 20/26 (H4, A498, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.557×** | -6.1 | 3e-08 | 21/26 (HOP62, H4, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.546×** | -6.1 | 4e-08 | 23/27 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.554×** | -6.0 | 5e-08 | 22/26 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.670×** | -5.9 | 1e-07 | 19/26 (A498, NCI-H1792, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.58 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7448. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 189 | 0 | 23 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0503× (z -18.5) |
| [[HOP62 (line)]] | alt | 228 | 0 | 23 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0487× (z -24.6) |
| [[A-172 (line)]] | wt | 294 | 0 | 16 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0289× (z -24.8) |
| [[SW 900 (line)]] | alt | 276 | 0 | 16 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0263× (z -25.7) |
| [[C-33 A (line)]] | alt | 296 | 0 | 14 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0197× (z -32.6) |
| [[NCI-H1573 (line)]] | alt | 248 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0891× (z -27.4) |
| [[MIA PaCa-2 (line)]] | alt | 231 | 0 | 12 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0362× (z -25.6) |
| [[HS-578T (line)]] | alt | 268 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0469× (z -22.6) |
| [[hTERT-HPNE (line)]] | wt | 275 | 0 | 11 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0506× (z -21.1) |
| [[A498 (line)]] | wt | 64.8 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.120× (z -17.2) |
| [[NCI-H1792 (line)]] | alt | 297 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -24.9) |
| [[NCI-H2030 (line)]] | alt | 182 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0652× (z -22.0) |
| [[RPMI-7951 (line)]] | alt | 156 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0906× (z -18.4) |
| [[NCI-H460 (line)]] | wt | 131 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0874× (z -20.4) |
| [[SNU-423 (line)]] | alt | 113 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0475× (z -23.6) |
| [[J82 (line)]] | alt | 313 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0404× (z -22.2) |
| [[A549 (line)]] | wt | 124 | 0 | 7 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0371× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.0521× (z -19.2) |
| [[Hs 766T (line)]] | wt | 113 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0567× (z -19.7) |
| [[LOX-IMVI (line)]] | wt | 92.0 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0450× (z -19.7) |
| [[PANC-1 (line)]] | alt | 50.1 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -19.7) |
| [[SW 1088 (line)]] | alt | 526 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0226× (z -17.4) |
| [[Panc 03.27 (line)]] | alt | 35.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 35.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -11.4) |
| [[BT-474 (line)]] | alt | 24.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -8.7) |
| [[CHP-212 (line)]] | wt | 40.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0723× (z -9.6) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 51.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -8.7) |
| [[A-427 (line)]] | wt | 5.68 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.93 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 13.8 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.97 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.42 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.91 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.97 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.81 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.64 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.68 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 13.8 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.33 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.68 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.40 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.80 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.27 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7448), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GJA1]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[KIRREL3]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS6]] | +0.68 | +0.69 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[BMPER]] | +0.67 | +0.66 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[STEAP1B-AS1]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[RAI14]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[KCNMA1]] | +0.63 | +0.67 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[SPOCK1]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[LINC01411]] | +0.62 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[LOXL2]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 409 |
| [[APCDD1L-DT]] | +0.61 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[IL1B]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 | STRING 717 |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACSL1]] | -0.59 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[FGD4]] | -0.55 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[PHKA1]] | -0.53 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[ARHGEF34P]] | -0.51 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[CHPT1]] | -0.51 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[CMKLR2]] | -0.50 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[PLEKHA7]] | -0.50 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[JDP2]] | -0.49 | -0.47 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 10, C 33. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANTXR2]] | B | ANTXR2 activity raises VEGFC's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 4.62× lower at baseline in the lines without ANTXR2 | 0.009 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[SMOX]] | B | SMOX activity raises VEGFC's level | lines that do not express SMOX (6) vs lines expressing it (44) | 2.60× lower at baseline in the lines without SMOX | 0.012 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[GJA1]] | B | GJA1 activity strengthens VEGFC's drug response | lines that do not express GJA1 (7) vs lines expressing it (20) | the lines without GJA1 respond 0.76× as strongly (z diff +2.25); strongest at Dinaciclib 0.05 µM: 0.69x vs 0.27x (z diff +6.0) | 0.023 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1; target measured in part of the lines; artifact flags |
| [[ANXA10]] | B | ANXA10 activity raises VEGFC's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 3.18× lower at baseline in the lines without ANXA10 | 0.028 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[HRH1]] | B | HRH1 activity raises VEGFC's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 3.00× lower at baseline in the lines without HRH1 | 0.035 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[CD44]] | B | CD44 activity raises VEGFC's level | lines that do not express CD44 (15) vs lines expressing it (35) | 3.63× lower at baseline in the lines without CD44 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[CMKLR2]] | B | CMKLR2 activity raises VEGFC's level | lines that do not express CMKLR2 (16) vs lines expressing it (34) | 2.08× lower at baseline in the lines without CMKLR2 | 0.058 | ⚠ within organs, on part of the lines; also absent: SATB1-AS1, ENSG00000231772, NYAP2; maybe low, not absent |
| [[BMPER]] | B | BMPER activity raises VEGFC's level | lines that do not express BMPER (21) vs lines expressing it (29) | 3.34× lower at baseline in the lines without BMPER | 0.062 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[PRDM8]] | B | PRDM8 activity raises VEGFC's level | lines that do not express PRDM8 (17) vs lines expressing it (33) | 3.11× lower at baseline in the lines without PRDM8 | 0.081 | ⚠ within organs, on part of the lines; also absent: TLR6, CFAP299, EDIL3 |
| [[SERPIND1]] | B | SERPIND1 activity raises VEGFC's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 1.66× lower at baseline in the lines without SERPIND1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[KCNMA1]] | C | KCNMA1 activity raises VEGFC's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 9.72× lower at baseline in the lines without KCNMA1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN; co-absent with the target |
| [[ADAM12]] | C | ADAM12 activity raises VEGFC's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 8.43× lower at baseline in the lines without ADAM12 | 7e-04 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 9, C 17. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD44]] | B | VEGFC activity raises CD44's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 4.28× lower at baseline in the lines without VEGFC | 0.007 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1 |
| [[SMOX]] | B | VEGFC activity raises SMOX's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 2.46× lower at baseline in the lines without VEGFC | 0.008 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1 |
| [[PRSS23]] | B | VEGFC activity raises PRSS23's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 2.88× lower at baseline in the lines without VEGFC | 0.015 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1 |
| [[ATP13A3]] | B | VEGFC activity raises ATP13A3's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 1.69× lower at baseline in the lines without VEGFC | 0.031 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1 |
| [[NT5E]] | B | VEGFC activity raises NT5E's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 2.96× lower at baseline in the lines without VEGFC | 0.032 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1 |
| [[TPBG]] | B | VEGFC activity raises TPBG's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 2.95× lower at baseline in the lines without VEGFC | 0.042 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1 |
| [[ANTXR2]] | B | VEGFC activity raises ANTXR2's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 2.05× lower at baseline in the lines without VEGFC | 0.063 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1 |
| cells under [[Ivermectin (drug)]] 0.5 µM | B | VEGFC activity lowers the cells' numbers under Ivermectin 0.5 µM (makes them more sensitive) | lines that do not express VEGFC (22) vs lines expressing it (26) | the lines without VEGFC: 1.18× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1 |
| cells under [[Sulfatinib (drug)]] 5 µM | B | VEGFC activity raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | lines that do not express VEGFC (22) vs lines expressing it (26) | the lines without VEGFC: 0.81× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1 |
| [[MIR100HG]] | C | VEGFC activity raises MIR100HG's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 5.71× lower at baseline in the lines without VEGFC | 0.004 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1; co-absent with the target |
| [[KCNMA1]] | C | VEGFC activity raises KCNMA1's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 9.93× lower at baseline in the lines without VEGFC | 0.007 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1; co-absent with the target |
| [[LOXL2]] | C | VEGFC activity raises LOXL2's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 5.80× lower at baseline in the lines without VEGFC | 0.016 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.669). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.2, 15.9); signed map (21.3, 49.9). **Vector** length 124, 44.9% of its response variance represented; |z| ≥ 3 in 1,237 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | -7.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | -0.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | -0.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +0.7 |
| fall | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.7 | -5.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.4 | -5.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.4 | -6.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.3 | -4.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.3 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | vascular endothelial growth factor C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q34.3 — chr4:176,683,538-176,792,922 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VRP, VEGF-C |
| Gene groups (HGNC) | VEGF family |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 8 pathways, smallest: VEGF binds to VEGFR leading to receptor dimerization; VEGF ligand-receptor interactions; Signaling by VEGF |
| Matched by | ensembl_id |

**Function**, from UniProt [P49767](https://www.uniprot.org/uniprotkb/P49767) (Vascular endothelial growth factor C):

> Growth factor active in angiogenesis, and endothelial cell growth, stimulating their proliferation and migration and also has effects on the permeability of blood vessels. May function in angiogenesis of the venous and lymphatic vascular systems during embryogenesis, and also in the maintenance of differentiated lymphatic endothelium in adults. Binds and activates KDR/VEGFR2 and FLT4/VEGFR3 receptors.

**Summary**, from NCBI Gene [7424](https://www.ncbi.nlm.nih.gov/gene/7424):

> The protein encoded by this gene is a member of the platelet-derived growth factor/vascular endothelial growth factor (PDGF/VEGF) family. The encoded protein promotes angiogenesis and endothelial cell growth, and can also affect the permeability of blood vessels. The proprotein is further cleaved into a fully processed form that can bind and activate VEGFR-2 and VEGFR-3 receptors. [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:12682](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12682) · Entrez [7424](https://www.ncbi.nlm.nih.gov/gene/7424) · UniProt [P49767](https://www.uniprot.org/uniprotkb/P49767) · Ensembl [ENSG00000150630](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150630)

## Data

Gene col 7448: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7448); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7448, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7448]; `tensor/DDL_lfc|DDL_z.npy` [7448]; `embed/gene_vectors.npy` [7448]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7448 or target_col == 7448). Every well: [[VEGFC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VEGFC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

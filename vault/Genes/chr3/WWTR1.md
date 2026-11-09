---
symbol: "WWTR1"
type: "gene"
col: 306
ensembl_id: "ENSG00000018408"
name: "WW domain containing transcription regulator 1"
location: "3q25.1"
module: 84
arm: "+"
pooled_cpm: 295.55
n_lines_expressing: 43
n_dd_up: 0
n_dd_down: 52
n_dd_up_clean: 0
n_dd_down_clean: 43
in_vector_space: true
direction_upstream: 8
direction_downstream: 4
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# WWTR1

*WW domain containing transcription regulator 1* — 3q25.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 2.09×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 2.13×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 2.06×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change).
> Pooled over the cell lines (median), lowered significantly by 52 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.486× (z -17.5, q 0e+00, down in 32 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNMBP]] (+0.66, fdr 7e-06), [[ADAM19]] (+0.65, fdr 7e-06), [[PHC2]] (+0.65, fdr 7e-06); moves opposite to [[RAB32]] (-0.53, fdr 2e-05), [[CMKLR2]] (-0.51, fdr 4e-05), [[SLC22A5]] (-0.51, fdr 3e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TMEM158]] → it (grade B ⚠); 4 go from it, the strongest it → [[MYO10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 2.09×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 2.13×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 2.06×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change).

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 68 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 52 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 306.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.486×** | -17.5 | 0e+00 | 32/41 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.581×** | -13.2 | 5e-37 | 32/42 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.536×** | -10.7 | 3e-24 | 34/41 (HepG2/C3A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.590×** | -8.7 | 5e-16 | 29/41 (HepG2/C3A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.662×** | -7.1 | 2e-10 | 35/41 (SK-MEL-2, NCI-H2030, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.487×** | -6.4 | 1e-08 | 32/42 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.736×** | -6.4 | 1e-08 | 27/41 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.684×** | -6.2 | 3e-08 | 25/41 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.724×** | -6.2 | 3e-08 | 25/43 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.700×** | -6.1 | 6e-08 | 29/41 (SK-MEL-2, NCI-H2030, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.509×** | -6.0 | 8e-08 | 34/41 (SK-MEL-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.698×** | -5.9 | 1e-07 | 25/40 (HepG2/C3A, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.787×** | -5.8 | 3e-07 | 25/42 (H4, SK-MEL-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.714×** | -5.8 | 3e-07 | 31/41 (RPMI-7951, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.722×** | -5.6 | 9e-07 | 24/42 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.723×** | -5.5 | 1e-06 | 27/41 (HepG2/C3A, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.718×** | -5.5 | 2e-06 | 28/40 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.756×** | -5.3 | 3e-06 | 24/42 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 306. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 350 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -24.2) |
| [[MIA PaCa-2 (line)]] | alt | 910 | 0 | 10 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.552× (z -22.5) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -17.7) |
| [[NCI-H460 (line)]] | wt | 339 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -20.4) |
| [[SK-MEL-2 (line)]] | alt | 504 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -16.0) |
| [[A-172 (line)]] | wt | 379 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -19.9) |
| [[H4 (line)]] | wt | 390 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -13.4) |
| [[A549 (line)]] | wt | 285 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -17.4) |
| [[C32 (line)]] | wt | 616 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 625 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 530 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -12.8) |
| [[SW 900 (line)]] | alt | 381 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -17.0) |
| [[A498 (line)]] | wt | 225 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 379 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -14.3) |
| [[NCI-H2030 (line)]] | alt | 285 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -17.1) |
| [[NCI-H23 (line)]] | alt | 345 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 441 | 0 | 3 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.267× (z -10.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.629× (z -9.6) |
| [[PANC-1 (line)]] | alt | 656 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -13.2) |
| [[Hs 766T (line)]] | wt | 183 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -11.1) |
| [[HS-578T (line)]] | alt | 688 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -13.6) |
| [[LOX-IMVI (line)]] | wt | 195 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 222 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -19.2) |
| [[NCI-H2347 (line)]] | alt | 361 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -13.5) |
| [[SNU-423 (line)]] | alt | 317 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -15.0) |
| [[A-427 (line)]] | wt | 171 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.595× (z -9.5) |
| [[COLO 205 (line)]] | alt | 135 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.400× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 248 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.323× (z -8.8) |
| [[HOP62 (line)]] | alt | 287 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 292 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -9.4) |
| [[RKO (line)]] | wt | 147 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.437× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 138 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -10.1) |
| [[AN3 CA (line)]] | alt | 193 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.6 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 269 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.3 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 56.1 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 86.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 40.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 348 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 47.4 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 129 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 306), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNMBP]] | +0.66 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[ADAM19]] | +0.65 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[PHC2]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[PPFIBP1]] | +0.64 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[RGS17]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[NT5E]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[COL13A1]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[ECE1]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[DCBLD2]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ETV1]] | +0.63 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[SMOX]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[SPRED2]] | +0.62 | +0.66 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB32]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[CMKLR2]] | -0.51 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[SLC22A5]] | -0.51 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[ROS1]] | -0.51 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[MIR3936HG]] | -0.51 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[SLC3A2]] | -0.51 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[TRPM7]] | -0.51 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[FSTL3]] | -0.50 | -0.49 / -0.47 | both halves | 2e-05 | pathway: Signaling by TGFB family members |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM158]] | B | TMEM158 activity raises WWTR1's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 3.20× lower at baseline in the lines without TMEM158 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[KCNN4]] | B | KCNN4 activity raises WWTR1's level | lines that do not express KCNN4 (12) vs lines expressing it (38) | 2.76× lower at baseline in the lines without KCNN4 | 0.011 | ⚠ within organs, on part of the lines; also absent: RP1, GSPT2, GALC |
| [[COL13A1]] | B | COL13A1 activity raises WWTR1's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 2.74× lower at baseline in the lines without COL13A1 | 0.017 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[MAP2K1]] | B | MAP2K1 activity raises WWTR1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 9.0% of all compounds | 0.048 | ⚠ off-target possible; 4 compounds |
| [[LINC02813]] | B | LINC02813 activity raises WWTR1's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 2.27× lower at baseline in the lines without LINC02813 | 0.067 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[TM4SF1]] | B | TM4SF1 activity raises WWTR1's level | lines that do not express TM4SF1 (12) vs lines expressing it (38) | 1.79× lower at baseline in the lines without TM4SF1 | 0.083 | ⚠ within organs, on part of the lines; also absent: TM4SF1-AS1; maybe low, not absent |
| [[PRSS23]] | B | PRSS23 activity raises WWTR1's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 2.02× lower at baseline in the lines without PRSS23 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[TIMP1]] | C | TIMP1 activity raises WWTR1's level | lines that do not express TIMP1 (3) vs lines expressing it (47) | 2.76× lower at baseline in the lines without TIMP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: COTL1, OSBPL3, IGF2BP2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO10]] | B | WWTR1 activity raises MYO10's level | lines that do not express WWTR1 (7) vs lines expressing it (43) | 2.71× lower at baseline in the lines without WWTR1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ZNF585A, LGALS1, EBI3 |
| [[KCNN4]] | B | WWTR1 activity raises KCNN4's level | lines that do not express WWTR1 (7) vs lines expressing it (43) | 3.86× lower at baseline in the lines without WWTR1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ZNF585A, LGALS1, EBI3 |
| [[FXYD5]] | B | WWTR1 activity raises FXYD5's level | lines that do not express WWTR1 (7) vs lines expressing it (43) | 1.91× lower at baseline in the lines without WWTR1 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ZNF585A, LGALS1, EBI3 |
| [[NPAS2]] | B | WWTR1 activity raises NPAS2's level | lines that do not express WWTR1 (7) vs lines expressing it (43) | 1.85× lower at baseline in the lines without WWTR1 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ZNF585A, LGALS1, EBI3 |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.2, 6.0); signed map (5.4, 49.4). **Vector** length 133, 44.0% of its response variance represented; |z| ≥ 3 in 1,632 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.5 | +2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | -0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.6 | -0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | -1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.5 | +0.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | +1.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.4 | +2.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.4 | +2.8 |
| fall | [[Trametinib (drug)]] 5 µM |  | -8.5 | -6.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -8.1 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -7.5 | -6.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -7.3 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.9 | -5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | WW domain containing transcription regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.1 — chr3:149,517,235-149,736,714 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAZ, DKFZp586I1419 |
| Gene groups (HGNC) | TEAD interacting region 3, omega loop domain containing |
| Hallmark sets | TGF_BETA_SIGNALING, MYOGENESIS |
| Reactome | 22 pathways, smallest: RUNX3 regulates YAP1-mediated transcription; Physiological factors; YAP1- and WWTR1 (TAZ)-stimulated gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZV5](https://www.uniprot.org/uniprotkb/Q9GZV5) (WW domain-containing transcription regulator protein 1):

> Transcriptional coactivator which acts as a downstream regulatory target in the Hippo signaling pathway that plays a pivotal role in organ size control and tumor suppression by restricting proliferation and promoting apoptosis. The core of this pathway is composed of a kinase cascade wherein STK3/MST2 and STK4/MST1, in complex with its regulatory protein SAV1, phosphorylates and activates LATS1/2 in complex with its regulatory protein MOB1, which in turn phosphorylates and inactivates YAP1 …

**Summary**, from NCBI Gene [25937](https://www.ncbi.nlm.nih.gov/gene/25937):

> Enables transcription coactivator activity. Involved in several processes, including intracellular signal transduction; negative regulation of canonical Wnt signaling pathway; and positive regulation of cell differentiation. Located in cytosol and nuclear body. Is active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24042](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24042) · Entrez [25937](https://www.ncbi.nlm.nih.gov/gene/25937) · UniProt [Q9GZV5](https://www.uniprot.org/uniprotkb/Q9GZV5) · Ensembl [ENSG00000018408](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000018408)

## Data

Gene col 306: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 306); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 306, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 306]; `tensor/DDL_lfc|DDL_z.npy` [306]; `embed/gene_vectors.npy` [306]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 306 or target_col == 306). Every well: [[WWTR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WWTR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

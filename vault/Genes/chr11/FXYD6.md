---
symbol: "FXYD6"
type: "gene"
col: 6056
ensembl_id: "ENSG00000137726"
name: "FXYD domain containing ion transport regulator 6"
location: "11q23.3"
module: 82
arm: "+"
pooled_cpm: 2.6
n_lines_expressing: 25
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 9
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# FXYD6

*FXYD domain containing ion transport regulator 6* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.02× (z +9.7, q 1e-19, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.08× (z +7.5, q 9e-12, up in 8 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.532× (z -4.6, q 0.002, down in 10 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CACNG4]] (+0.58, fdr 2e-05), [[MAST1]] (+0.58, fdr 3e-05), [[MYT1]] (+0.58, fdr 3e-05); moves opposite to [[ENOX2]] (-0.55, fdr 3e-05), [[PTPRG]] (-0.52, fdr 3e-05), [[RNASEH1]] (-0.51, fdr 3e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PRR36]] → it (grade B ⚠); 9 go from it, the strongest it → [[SGSM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6056.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.02×** | +9.7 | 1e-19 | 1/4 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.15×** | +8.3 | 2e-14 | 1/7 (A549) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.08×** | +7.5 | 9e-12 | 8/20 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.98×** | +6.8 | 1e-09 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.17×** | +5.6 | 2e-06 | 8/18 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.67×** | +5.1 | 3e-05 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +4.9 | 9e-05 | 0/14 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.6 | 0.022 | 0/13 | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.44×** | +3.4 | 0.042 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.2 | 0.071 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.52× | +3.0 | 0.13 | 1/16 (MIA PaCa-2) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6056.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.532×** | -4.6 | 0.002 | 10/20 (SW480, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.529×** | -4.5 | 0.002 | 10/16 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.573×** | -4.1 | 0.009 | 10/21 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.583×** | -3.9 | 0.009 | 12/20 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.584×** | -3.9 | 0.009 | 13/21 (SW480, A549, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.591×** | -3.9 | 0.011 | 13/19 (NCI-H2347, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.605×** | -3.7 | 0.019 | 11/20 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.615×** | -3.6 | 0.026 | 10/20 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **0.649×** | -3.2 | 0.096 | 0/21 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6056. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 15.1 | 0 | 8 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0448× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -12.7) |
| [[NCI-H2347 (line)]] | alt | 4.85 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0333× (z -13.6) |
| [[A549 (line)]] | wt | 3.09 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0358× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 10.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0791× (z -16.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -9.0) |
| [[A-172 (line)]] | wt | 17.4 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -11.4) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-427 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.254 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.485 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.302 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.573 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.813 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.276 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.270 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.797 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.296 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.337 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6056), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACNG4]] | +0.58 | +0.50 / +0.47 | both halves | 2e-05 | pathway: Cardiac conduction |
| [[MAST1]] | +0.58 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[MYT1]] | +0.58 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[FAM161A]] | +0.56 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[RASAL1]] | +0.55 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[F10]] | +0.55 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[ZNF836]] | +0.54 | +0.53 / +0.43 | both halves | 4e-05 |  |
| [[LINC00674]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[ATG9B]] | +0.53 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[KIF3C]] | +0.52 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[ATL1]] | +0.52 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[FKBP1B]] | +0.52 | +0.41 / +0.41 | both halves | 4e-05 | pathway: Cardiac conduction |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOX2]] | -0.55 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[PTPRG]] | -0.52 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[RNASEH1]] | -0.51 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[NSD1]] | -0.50 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[PUDP]] | -0.50 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[ATR]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[AP4E1]] | -0.47 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[CPSF2]] | -0.47 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[EXOSC6]] | -0.47 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[ZNG1F]] | -0.46 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[ATE1]] | -0.46 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[FBXL17]] | -0.46 | -0.42 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRR36]] | B | PRR36 activity raises FXYD6's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 1.64× lower at baseline in the lines without PRR36 | 0.076 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[ETNK2]] | B | ETNK2 activity raises FXYD6's level | lines that do not express ETNK2 (11) vs lines expressing it (39) | 2.12× lower at baseline in the lines without ETNK2 | 0.099 | ⚠ within organs, on part of the lines; also absent: DLK2, FBXL2, DUSP15; maybe low, not absent |
| [[CACNG4]] | C | CACNG4 activity raises FXYD6's level | lines that do not express CACNG4 (21) vs lines expressing it (29) | 2.10× lower at baseline in the lines without CACNG4 | 0.028 | ⚠ within organs, on part of the lines; also absent: FRMPD3, PALM, PCSK1N; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SGSM1]] | B | FXYD6 activity raises SGSM1's level | lines that do not express FXYD6 (25) vs lines expressing it (25) | 1.76× lower at baseline in the lines without FXYD6 | 0.025 | ⚠ within organs, on part of the lines; also absent: MARK1, KIF1A, MAP6 |
| [[PTK7]] | B | FXYD6 activity raises PTK7's level | lines that do not express FXYD6 (25) vs lines expressing it (25) | 2.22× lower at baseline in the lines without FXYD6 | 0.059 | ⚠ within organs, on part of the lines; also absent: MARK1, KIF1A, MAP6 |
| [[AP4E1]] | B | FXYD6 activity strengthens AP4E1's drug response | lines that do not express FXYD6 (25) vs lines expressing it (23) | the lines without FXYD6 respond 0.83× as strongly (z diff +1.08); strongest at Homoharringtonine 5 µM: 1.43x vs 1.81x (z diff +2.3) | 0.068 | ⚠ within organs, on part of the lines; also absent: MARK1, KIF1A, MAP6; target measured in part of the lines; artifact flags |
| [[EPHA10]] | B | FXYD6 activity raises EPHA10's level | lines that do not express FXYD6 (25) vs lines expressing it (25) | 1.66× lower at baseline in the lines without FXYD6 | 0.084 | ⚠ within organs, on part of the lines; also absent: MARK1, KIF1A, MAP6 |
| [[LINC00674]] | B | FXYD6 activity raises LINC00674's level | lines that do not express FXYD6 (25) vs lines expressing it (25) | 1.52× lower at baseline in the lines without FXYD6 | 0.096 | ⚠ within organs, on part of the lines; also absent: MARK1, KIF1A, MAP6 |
| [[TMEM150C]] | C | FXYD6 activity raises TMEM150C's level | lines that do not express FXYD6 (25) vs lines expressing it (25) | 2.55× lower at baseline in the lines without FXYD6 | 0.054 | ⚠ within organs, on part of the lines; also absent: MARK1, KIF1A, MAP6; co-absent with the target |
| [[C14orf132]] | C | FXYD6 activity raises C14orf132's level | lines that do not express FXYD6 (25) vs lines expressing it (25) | 3.37× lower at baseline in the lines without FXYD6 | 0.061 | ⚠ within organs, on part of the lines; also absent: MARK1, KIF1A, MAP6; co-absent with the target |
| [[CACNG4]] | C | FXYD6 activity raises CACNG4's level | lines that do not express FXYD6 (25) vs lines expressing it (25) | 2.34× lower at baseline in the lines without FXYD6 | 0.084 | ⚠ within organs, on part of the lines; also absent: MARK1, KIF1A, MAP6; co-absent with the target |
| [[HEYL]] | C | FXYD6 activity raises HEYL's level | lines that do not express FXYD6 (25) vs lines expressing it (25) | 1.75× lower at baseline in the lines without FXYD6 | 0.085 | ⚠ within organs, on part of the lines; also absent: MARK1, KIF1A, MAP6; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.502). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.5, -1.3); signed map (-26.5, 32.1). **Vector** length 43.9, 9.49% of its response variance represented; |z| ≥ 3 in 545 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +2.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -3.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -3.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.0 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -3.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | FXYD domain containing ion transport regulator 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:117,836,976-117,877,486 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | FXYD domain containing ion transport regulators |
| Reactome | 9 pathways, smallest: Ion homeostasis; Ion transport by P-type ATPases; Potential therapeutics for SARS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0Q3](https://www.uniprot.org/uniprotkb/Q9H0Q3) (FXYD domain-containing ion transport regulator 6):

> Associates with and regulates the activity of the sodium/potassium-transporting ATPase (NKA) which catalyzes the hydrolysis of ATP coupled with the exchange of Na(+) and K(+) ions across the plasma membrane. Reduces the apparent affinity for intracellular Na(+) with no change in the apparent affinity for extracellular K(+). In addition to modulating NKA kinetics, may also function as a regulator of NKA localization to the plasma membrane (By similarity).

**Summary**, from NCBI Gene [53826](https://www.ncbi.nlm.nih.gov/gene/53826):

> This gene encodes a member of the FXYD family of transmembrane proteins. This particular protein encodes phosphohippolin, which likely affects the activity of Na,K-ATPase. Multiple alternatively spliced transcript variants encoding the same protein have been described. Related pseudogenes have been identified on chromosomes 10 and X. Read-through transcripts have been observed between this locus and the downstream sodium/potassium-transporting ATPase subunit gamma (FXYD2, GeneID 486) …

**Accessions** — [HGNC:4030](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4030) · Entrez [53826](https://www.ncbi.nlm.nih.gov/gene/53826) · UniProt [Q9H0Q3](https://www.uniprot.org/uniprotkb/Q9H0Q3) · Ensembl [ENSG00000137726](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137726)

## Data

Gene col 6056: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6056); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6056, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6056]; `tensor/DDL_lfc|DDL_z.npy` [6056]; `embed/gene_vectors.npy` [6056]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6056 or target_col == 6056). Every well: [[FXYD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FXYD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

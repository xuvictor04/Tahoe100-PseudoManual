---
symbol: "FBXO15"
type: "gene"
col: 6564
ensembl_id: "ENSG00000141665"
name: "F-box protein 15"
location: "18q22.3"
module: 10
arm: "+"
pooled_cpm: 4.25
n_lines_expressing: 44
n_dd_up: 4
n_dd_down: 32
n_dd_up_clean: 2
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 10
direction_downstream: 15
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# FBXO15

*F-box protein 15* — 18q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.40× (z +7.1, q 8e-10, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.73× (z +4.6, q 6e-04, up in 12 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 1.70×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.212× (z -12.9, q 2e-35, down in 30 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC63]] (+0.63, fdr 1e-05), [[ZMAT1]] (+0.62, fdr 2e-05), [[LINC00466]] (+0.61, fdr 1e-05); moves opposite to [[LINC01956]] (-0.45, fdr 2e-04), [[KBTBD12]] (-0.44, fdr 1e-04), [[ABO]] (-0.43, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[RASGEF1A]] → it (grade B ⚠); 15 go from it, the strongest it → [[CASC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6564.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 1.70×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +7.1 | 8e-10 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +4.7 | 6e-04 | 1/8 (HEC-1-A) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.73×** | +4.6 | 6e-04 | 12/39 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.70×** | +4.5 | 9e-04 | 14/33 (NCI-H23, NCI-H1792, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.45× | +3.1 | 0.21 | 8/40 (NCI-H23, C-33 A, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.48× | +3.0 | 0.22 | 4/33 (A549, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6564.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.212×** | -12.9 | 2e-35 | 30/40 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.334×** | -12.9 | 2e-35 | 28/31 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.234×** | -12.1 | 2e-31 | 29/39 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.245×** | -11.7 | 2e-29 | 31/35 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.319×** | -9.1 | 9e-18 | 26/35 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.367×** | -8.3 | 8e-15 | 26/31 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.398×** | -7.6 | 2e-12 | 19/27 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.403×** | -7.5 | 3e-12 | 20/23 (A-427, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.400×** | -7.0 | 2e-10 | 23/39 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.485×** | -6.0 | 1e-07 | 19/39 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.463×** | -5.9 | 2e-07 | 16/32 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.509×** | -5.6 | 1e-06 | 21/35 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.554×** | -4.9 | 5e-05 | 13/31 (NCI-H2030, NCI-H23, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.542×** | -4.8 | 7e-05 | 17/32 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.566×** | -4.7 | 1e-04 | 19/37 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.584×** | -4.4 | 3e-04 | 14/26 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.494×** | -4.2 | 1e-03 | 9/40 (PANC-1, H4, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.388×** | -4.1 | 0.001 | 11/32 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.710×** | -4.0 | 0.002 | 15/37 (HS-578T, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.654×** | -3.5 | 0.012 | 14/36 (NCI-H23, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6564. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 13.3 | 0 | 16 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0792× (z -20.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0311× (z -19.8) |
| [[A-427 (line)]] | wt | 22.5 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0286× (z -21.0) |
| [[NCI-H23 (line)]] | alt | 14.1 | 1 (1 ⚠) | 5 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.70× (z +9.0) ⚠ position not correctable | [[Digitoxin (drug)]] 5 µM 0.0450× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0878× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 4.56 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0636× (z -16.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0227× (z -15.6) |
| [[A549 (line)]] | wt | 7.48 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0108× (z -17.4) |
| [[C-33 A (line)]] | alt | 25.6 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0231× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 5.79 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -10.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0521× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 5.78 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0543× (z -15.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0546× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 6.94 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -12.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.111× (z -9.3) |
| [[A-172 (line)]] | wt | 4.48 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0679× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 4.45 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -9.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0592× (z -8.7) |
| [[HOP62 (line)]] | alt | 2.45 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0750× (z -10.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[MIA PaCa-2 (line)]] | alt | 3.32 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0438× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 4.82 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0259× (z -11.5) |
| [[A498 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.684 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.501 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6564), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC63]] | +0.63 | +0.66 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[ZMAT1]] | +0.62 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[LINC00466]] | +0.61 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[ID2-AS1]] | +0.59 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[BASP1-AS1]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[FAM66C]] | +0.55 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ABCA17P]] | +0.54 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[SPANXA2-OT1]] | +0.54 | +0.55 / +0.41 | both halves | 4e-05 | **novel candidate** |
| [[LINC02026]] | +0.53 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SSPOP]] | +0.53 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[VASH1]] | +0.52 | +0.57 / +0.36 | both halves | 9e-05 |  |
| [[RDM1P5]] | +0.52 | +0.51 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01956]] | -0.45 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[KBTBD12]] | -0.44 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[ABO]] | -0.43 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[GALNT5]] | -0.42 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[TMEM181]] | -0.41 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[IL20RA]] | -0.41 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[CRACR2A]] | -0.40 | -0.44 / -0.22 | both halves | 6e-04 |  |
| [[PROM1]] | -0.40 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[SAMD12-AS1]] | -0.40 | -0.29 / -0.36 | both halves | 2e-04 |  |
| [[FGFR2]] | -0.39 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[FBXO34]] | -0.39 | -0.34 / -0.34 | both halves | 1e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGEF1A]] | B | RASGEF1A activity raises FBXO15's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.80× lower at baseline in the lines without RASGEF1A | 0.033 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[PRKN]] | B | PRKN activity raises FBXO15's level | lines that do not express PRKN (8) vs lines expressing it (42) | 1.82× lower at baseline in the lines without PRKN | 0.041 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[ANKS1B]] | B | ANKS1B activity raises FBXO15's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 1.92× lower at baseline in the lines without ANKS1B | 0.075 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[RFPL1S]] | B | RFPL1S activity raises FBXO15's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 1.70× lower at baseline in the lines without RFPL1S | 0.090 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent |
| [[LRRC63]] | B | LRRC63 activity raises FBXO15's level | lines that do not express LRRC63 (25) vs lines expressing it (25) | 2.16× lower at baseline in the lines without LRRC63 | 0.090 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, STAC, CRLF2 |
| [[MIR1915HG]] | B | MIR1915HG activity raises FBXO15's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.65× lower at baseline in the lines without MIR1915HG | 0.091 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[GALNT5]] | B | GALNT5 activity lowers FBXO15's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 1.92× higher at baseline in the lines without GALNT5 | 0.095 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2 |
| [[LINC00466]] | B | LINC00466 activity raises FBXO15's level | lines that do not express LINC00466 (15) vs lines expressing it (35) | 1.82× lower at baseline in the lines without LINC00466 | 0.097 | ⚠ within organs, on part of the lines; also absent: FAM124A, NTN1, SSPOP; maybe low, not absent |
| [[KATNAL2]] | C | KATNAL2 activity raises FBXO15's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 2.48× lower at baseline in the lines without KATNAL2 | 0.009 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent; co-absent with the target |
| [[CRB1]] | C | CRB1 activity raises FBXO15's level | lines that do not express CRB1 (6) vs lines expressing it (44) | 2.26× lower at baseline in the lines without CRB1 | 0.071 | ⚠ within organs, on part of the lines; also absent: DNAI1, RBFOX1, RHBDL3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASC2]] | B | FBXO15 activity raises CASC2's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 2.23× lower at baseline in the lines without FBXO15 | 0.003 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[LRRIQ3]] | B | FBXO15 activity raises LRRIQ3's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 1.72× lower at baseline in the lines without FBXO15 | 0.009 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[KBTBD12]] | B | FBXO15 activity lowers KBTBD12's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 2.08× higher at baseline in the lines without FBXO15 | 0.013 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[DUSP19]] | B | FBXO15 activity raises DUSP19's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without FBXO15 | 0.017 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[PRDX6-AS1]] | B | FBXO15 activity raises PRDX6-AS1's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 1.77× lower at baseline in the lines without FBXO15 | 0.018 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[C3orf18]] | B | FBXO15 activity raises C3orf18's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 1.82× lower at baseline in the lines without FBXO15 | 0.023 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[CCDC191]] | B | FBXO15 activity raises CCDC191's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 2.07× lower at baseline in the lines without FBXO15 | 0.068 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[TTC30A]] | B | FBXO15 activity raises TTC30A's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 1.98× lower at baseline in the lines without FBXO15 | 0.072 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[SPATA17]] | B | FBXO15 activity raises SPATA17's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 1.89× lower at baseline in the lines without FBXO15 | 0.073 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[C11orf65]] | B | FBXO15 activity raises C11orf65's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 1.28× lower at baseline in the lines without FBXO15 | 0.074 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[ZNF48]] | B | FBXO15 activity raises ZNF48's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 1.47× lower at baseline in the lines without FBXO15 | 0.085 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| cells under [[Minodronic acid (drug)]] 0.5 µM | B | FBXO15 activity raises the cells' numbers under Minodronic acid 0.5 µM (protects the cells) | lines that do not express FBXO15 (6) vs lines expressing it (42) | the lines without FBXO15: 0.82× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.306). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.7, 30.1); signed map (36.9, -9.2). **Vector** length 63.6, 11.8% of its response variance represented; |z| ≥ 3 in 1,119 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +1.9 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.3 | +4.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +1.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.0 | +2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.0 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +4.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.8 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.7 | -3.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +0.7 | +2.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.2 | -12.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.8 | -4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.3 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -4.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.5 | -3.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q22.3 — chr18:74,073,353-74,147,843 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC39671, FBX15 |
| Gene groups (HGNC) | F-boxes other |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCQ5](https://www.uniprot.org/uniprotkb/Q8NCQ5) (F-box only protein 15):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex.

**Summary**, from NCBI Gene [201456](https://www.ncbi.nlm.nih.gov/gene/201456):

> Members of the F-box protein family, such as FBXO15, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (MIM 601434), cullin (see CUL1; MIM 603134), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:13617](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13617) · Entrez [201456](https://www.ncbi.nlm.nih.gov/gene/201456) · UniProt [Q8NCQ5](https://www.uniprot.org/uniprotkb/Q8NCQ5) · Ensembl [ENSG00000141665](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141665)

## Data

Gene col 6564: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6564); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6564, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6564]; `tensor/DDL_lfc|DDL_z.npy` [6564]; `embed/gene_vectors.npy` [6564]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6564 or target_col == 6564). Every well: [[FBXO15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

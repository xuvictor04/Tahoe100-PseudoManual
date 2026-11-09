---
symbol: "MAML3"
type: "gene"
col: 12283
ensembl_id: "ENSG00000196782"
name: "mastermind like transcriptional coactivator 3"
location: "4q31.1"
module: 92
arm: "+"
pooled_cpm: 250.94
n_lines_expressing: 41
n_dd_up: 1
n_dd_down: 59
n_dd_up_clean: 1
n_dd_down_clean: 41
in_vector_space: true
direction_upstream: 8
direction_downstream: 7
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# MAML3

*mastermind like transcriptional coactivator 3* — 4q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Filgotinib (drug)]] 5 µM: 1.31× (z +4.2, q 0.014, up in 24 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 1.85×; ⚠ cell-cycle shift, explains ~33% of this change).
> Pooled over the cell lines (median), lowered significantly by 59 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.309× (z -25.7, q 0e+00, down in 36 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PITPNC1]] (+0.66, fdr 7e-06), [[ETV1]] (+0.64, fdr 7e-06), [[ETV4]] (+0.60, fdr 1e-05); moves opposite to [[CIAO3]] (-0.44, fdr 8e-05), [[BLTP3B]] (-0.44, fdr 6e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[DUSP4]] → it (grade B ⚠); 7 go from it, the strongest it → [[ST3GAL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12283.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 1.85×; ⚠ cell-cycle shift, explains ~33% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | **1.31×** | +4.2 | 0.014 | 24/39 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.22× | +3.4 | 0.14 | 17/40 (A-427, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.24× | +3.4 | 0.14 | 18/39 (NCI-H1792, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 64 in all, 19 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 59 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12283.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.309×** | -25.7 | 0e+00 | 36/39 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.322×** | -17.5 | 0e+00 | 38/39 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.356×** | -15.4 | 0e+00 | 37/38 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.373×** | -15.2 | 0e+00 | 38/39 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.375×** | -15.2 | 0e+00 | 35/39 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.370×** | -14.8 | 0e+00 | 35/39 (RKO, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.394×** | -14.4 | 6e-45 | 37/39 (SW48, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.408×** | -13.3 | 2e-38 | 36/38 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.440×** | -12.7 | 5e-35 | 36/39 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.443×** | -12.6 | 2e-34 | 37/39 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.444×** | -12.5 | 3e-34 | 38/39 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.483×** | -11.2 | 2e-27 | 34/39 (LS 180, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.487×** | -10.7 | 5e-25 | 27/35 (C-33 A, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.495×** | -10.2 | 5e-23 | 36/39 (A-427, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.518×** | -10.1 | 1e-22 | 33/39 (LS 180, A-427, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.536×** | -9.6 | 3e-20 | 37/39 (SK-MEL-2, A-427, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.330×** | -8.4 | 2e-15 | 37/39 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.358×** | -7.8 | 2e-13 | 36/39 (NCI-H460, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.358×** | -7.8 | 2e-13 | 37/39 (NCI-H460, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.383×** | -7.3 | 1e-11 | 36/39 (NCI-H460, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.413×** | -6.7 | 6e-10 | 35/39 (NCI-H460, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12283. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1,025 | 0 | 28 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -26.9) |
| [[SK-MEL-2 (line)]] | alt | 491 | 0 | 22 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -30.5) |
| [[C32 (line)]] | wt | 470 | 0 | 18 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -15.2) |
| [[NCI-H23 (line)]] | alt | 129 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -23.9) |
| [[A-427 (line)]] | wt | 212 | 0 | 16 (7 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.236× (z -16.0) |
| [[NCI-H1792 (line)]] | alt | 466 | 0 | 16 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -25.0) |
| [[C-33 A (line)]] | alt | 285 | 0 | 15 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0483× (z -29.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -20.7) |
| [[LoVo (line)]] | wt | 262 | 0 | 15 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -24.2) |
| [[HOP62 (line)]] | alt | 361 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -19.9) |
| [[PANC-1 (line)]] | alt | 269 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -23.8) |
| [[LOX-IMVI (line)]] | wt | 133 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -19.3) |
| [[hTERT-HPNE (line)]] | wt | 322 | 0 | 11 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.144× (z -15.4) |
| [[KATO III (line)]] | alt | 131 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -16.9) |
| [[RKO (line)]] | wt | 136 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -21.2) |
| [[RPMI-7951 (line)]] | alt | 196 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -21.9) |
| [[SW48 (line)]] | wt | 267 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -17.2) |
| [[LS 180 (line)]] | wt | 444 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.269× (z -16.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.284× (z -15.6) |
| [[NCI-H2030 (line)]] | alt | 617 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -22.1) |
| [[SHP-77 (line)]] | alt | 325 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -17.3) |
| [[A549 (line)]] | wt | 596 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0965× (z -24.0) |
| [[CFPAC-1 (line)]] | alt | 201 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -20.7) |
| [[HT-29 (line)]] | alt | 440 | 0 | 8 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.164× (z -15.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.323× (z -14.4) |
| [[NCI-H1573 (line)]] | alt | 373 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0754× (z -28.0) |
| [[H4 (line)]] | wt | 124 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -13.0) |
| [[Panc 03.27 (line)]] | alt | 219 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW480 (line)]] | alt | 72.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -17.6) |
| [[A498 (line)]] | wt | 67.9 | 1 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +9.0) ⚠ cell-cycle shift, explains ~33% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.319× (z -11.6) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.342× (z -10.5) |
| [[AN3 CA (line)]] | alt | 235 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.168× (z -11.6) |
| [[COLO 205 (line)]] | alt | 106 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -17.2) |
| [[Hs 766T (line)]] | wt | 136 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -15.0) |
| [[SW 900 (line)]] | alt | 93.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -11.9) |
| [[SW1417 (line)]] | alt | 96.7 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.380× (z -9.6) |
| [[BT-474 (line)]] | alt | 172 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.330× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.446× (z -8.6) |
| [[CHP-212 (line)]] | wt | 149 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.197× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 140 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.335× (z -11.0) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.443× (z -8.5) |
| [[SNU-423 (line)]] | alt | 86.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -13.1) |
| [[NCI-H596 (line)]] | alt | 304 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.269× (z -11.8) ⚠ transcription drop |
| [[SW 1271 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0770× (z -9.3) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 60.3 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.0 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 38.5 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 27.1 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 62.6 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 57.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 356 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 24.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 125 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12283), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PITPNC1]] | +0.66 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[ETV1]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[ETV4]] | +0.60 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[SPRY4]] | +0.59 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[DUSP4]] | +0.59 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[DUSP6]] | +0.59 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[EFNA5]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[NPAS2]] | +0.58 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[SPRY4-AS1]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[ITGB5]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[LINC02454]] | +0.56 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[EGR3]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAO3]] | -0.44 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[BLTP3B]] | -0.44 | -0.39 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUSP4]] | B | DUSP4 activity raises MAML3's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.49× lower at baseline in the lines without DUSP4 | 0.004 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[ITGA6]] | B | ITGA6 activity raises MAML3's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 1.99× lower at baseline in the lines without ITGA6 | 0.024 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DOCK4]] | B | DOCK4 activity raises MAML3's level | lines that do not express DOCK4 (14) vs lines expressing it (36) | 2.36× lower at baseline in the lines without DOCK4 | 0.044 | ⚠ within organs, on part of the lines; also absent: STC2 |
| [[ST3GAL1]] | B | ST3GAL1 activity raises MAML3's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 1.67× lower at baseline in the lines without ST3GAL1 | 0.065 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[THSD4]] | B | THSD4 activity raises MAML3's level | lines that do not express THSD4 (18) vs lines expressing it (32) | 1.74× lower at baseline in the lines without THSD4 | 0.069 | ⚠ within organs, on part of the lines; also absent: NR2E3, EDN1, CLDN1 |
| [[MIR100HG]] | B | MIR100HG activity raises MAML3's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 1.94× lower at baseline in the lines without MIR100HG | 0.089 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[HTR7]] | B | HTR7 activity raises MAML3's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 2.02× lower at baseline in the lines without HTR7 | 0.092 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[SGIP1]] | B | SGIP1 activity raises MAML3's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 1.92× lower at baseline in the lines without SGIP1 | 0.094 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST3GAL1]] | B | MAML3 activity raises ST3GAL1's level | lines that do not express MAML3 (9) vs lines expressing it (41) | 2.57× lower at baseline in the lines without MAML3 | 0.013 | ⚠ within organs, on part of the lines; also absent: SOX4, GOLGA7B-DT, STEAP2-AS1 |
| [[LINC01844]] | B | MAML3 activity lowers LINC01844's level | lines that do not express MAML3 (9) vs lines expressing it (41) | 2.32× higher at baseline in the lines without MAML3 | 0.065 | ⚠ within organs, on part of the lines; also absent: SOX4, GOLGA7B-DT, STEAP2-AS1 |
| [[FMN1]] | B | MAML3 activity raises FMN1's level | lines that do not express MAML3 (9) vs lines expressing it (41) | 3.23× lower at baseline in the lines without MAML3 | 0.068 | ⚠ within organs, on part of the lines; also absent: SOX4, GOLGA7B-DT, STEAP2-AS1 |
| [[MAP3K5]] | B | MAML3 activity raises MAP3K5's level | lines that do not express MAML3 (9) vs lines expressing it (41) | 2.41× lower at baseline in the lines without MAML3 | 0.073 | ⚠ within organs, on part of the lines; also absent: SOX4, GOLGA7B-DT, STEAP2-AS1 |
| [[DUSP4]] | B | MAML3 activity raises DUSP4's level | lines that do not express MAML3 (9) vs lines expressing it (41) | 2.64× lower at baseline in the lines without MAML3 | 0.079 | ⚠ within organs, on part of the lines; also absent: SOX4, GOLGA7B-DT, STEAP2-AS1 |
| [[EGR1]] | B | MAML3 activity raises EGR1's level | lines that do not express MAML3 (9) vs lines expressing it (41) | 1.75× lower at baseline in the lines without MAML3 | 0.083 | ⚠ within organs, on part of the lines; also absent: SOX4, GOLGA7B-DT, STEAP2-AS1 |
| [[FAM117B]] | B | MAML3 activity lowers FAM117B's level | lines that do not express MAML3 (9) vs lines expressing it (41) | 1.21× higher at baseline in the lines without MAML3 | 0.095 | ⚠ within organs, on part of the lines; also absent: SOX4, GOLGA7B-DT, STEAP2-AS1 |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.2, 6.5); signed map (8.9, 48.3). **Vector** length 108, 37.7% of its response variance represented; |z| ≥ 3 in 1,727 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MAPK output* (control, mean cos +0.56 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.5 | +1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.9 | -4.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | -0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | -3.9 |
| fall | [[Trametinib (drug)]] 5 µM |  | -7.3 | -4.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.4 | -14.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -6.1 | -2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.1 | -8.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.0 | -7.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -6.0 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.9 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | mastermind like transcriptional coactivator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.1 — chr4:139,716,753-140,154,184 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1816, MAM2, CAGH3, GDN; previously TNRC3 |
| Gene groups (HGNC) | Mastermind like transcriptional coactivator family |
| Reactome | 28 pathways, smallest: NOTCH2 intracellular domain regulates transcription; RUNX3 regulates NOTCH signaling; Regulation of gene expression in late stage (branching morphogenesis) pancreatic bud precursor cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JK9](https://www.uniprot.org/uniprotkb/Q96JK9) (Mastermind-like protein 3):

> Acts as a transcriptional coactivator for NOTCH proteins. Has been shown to amplify NOTCH-induced transcription of HES1.

**Summary**, from NCBI Gene [55534](https://www.ncbi.nlm.nih.gov/gene/55534):

> Enables transcription coactivator activity. Involved in Notch signaling pathway and positive regulation of transcription by RNA polymerase II. Located in nuclear speck. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16272](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16272) · Entrez [55534](https://www.ncbi.nlm.nih.gov/gene/55534) · UniProt [Q96JK9](https://www.uniprot.org/uniprotkb/Q96JK9) · Ensembl [ENSG00000196782](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196782)

## Data

Gene col 12283: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12283); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12283, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12283]; `tensor/DDL_lfc|DDL_z.npy` [12283]; `embed/gene_vectors.npy` [12283]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12283 or target_col == 12283). Every well: [[MAML3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAML3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

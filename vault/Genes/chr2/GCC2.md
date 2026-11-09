---
symbol: "GCC2"
type: "gene"
col: 5792
ensembl_id: "ENSG00000135968"
name: "GRIP and coiled-coil domain containing 2"
location: "2q12.3"
module: 74
arm: "+"
pooled_cpm: 264.54
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# GCC2

*GRIP and coiled-coil domain containing 2* — 2q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.18× (z +5.2, q 9e-05, up in 23 of 49 measured lines) ⚠ cell-cycle shift, explains ~0% of this change. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.20× (z +3.9, q 0.024, up in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (AsPC-1 2.10×, NCI-H460 1.62×, NCI-H2030 1.61×, NCI-H1573 1.53×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 1.81×, A-427 1.53×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.505× (z -14.8, q 0e+00, down in 46 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.515× (z -7.5, q 1e-11, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLU7]] (+0.85, fdr 7e-06), [[CCDC186]] (+0.74, fdr 7e-06), [[CIR1]] (+0.73, fdr 7e-06); moves opposite to [[VMA21]] (-0.65, fdr 1e-05), [[RPSA]] (-0.64, fdr 7e-06), [[WDR77]] (-0.64, fdr 7e-06).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NCS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5792.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (AsPC-1 2.10×, NCI-H460 1.62×, NCI-H2030 1.61×, NCI-H1573 1.53×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 1.81×, A-427 1.53×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.2 | 9e-05 | 23/49 (AsPC-1, NCI-H460, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.9 | 0.024 | 25/48 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.028 | 30/48 (HEC-1-A, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5792.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.505×** | -14.8 | 0e+00 | 46/48 (MIA PaCa-2, HEC-1-A, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.673×** | -8.6 | 3e-15 | 36/48 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.515×** | -7.5 | 1e-11 | 41/49 (SW 900, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.522×** | -7.4 | 3e-11 | 44/48 (SW 900, Panc 03.27, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.736×** | -6.6 | 4e-09 | 31/48 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.564×** | -6.5 | 8e-09 | 42/48 (SW1417, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.741×** | -6.5 | 8e-09 | 37/48 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.724×** | -6.4 | 8e-09 | 34/45 (NCI-H1792, SW 900, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.571×** | -6.3 | 1e-08 | 41/48 (SW 900, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.737×** | -6.3 | 1e-08 | 38/47 (HepG2/C3A, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.577×** | -6.2 | 3e-08 | 41/48 (SW 900, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.602×** | -5.7 | 4e-07 | 38/48 (SW 900, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.771×** | -5.6 | 1e-06 | 29/48 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.626×** | -5.3 | 5e-06 | 27/38 (SW 900, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.707×** | -5.2 | 8e-06 | 39/48 (SW 900, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.793×** | -5.0 | 2e-05 | 32/48 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.785×** | -4.9 | 3e-05 | 30/48 (SW 900, SW48, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.663×** | -4.7 | 1e-04 | 40/48 (C32, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.825×** | -4.0 | 0.002 | 26/48 (PANC-1, LoVo, …) | top dose only |  |
| [[Volasertib (drug)]] 0.5 µM |  | **0.779×** | -3.7 | 0.005 | 30/48 (SW480, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5792. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 437 | 0 | 11 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.373× (z -15.5) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 0.304× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 299 | 0 | 10 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.396× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.440× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 190 | 1 (1 ⚠) | 9 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.301× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.362× (z -16.4) |
| [[CFPAC-1 (line)]] | alt | 420 | 0 | 9 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.330× (z -16.2) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.528× (z -9.3) |
| [[SW480 (line)]] | alt | 364 | 0 | 6 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.406× (z -15.3) ⚠ unreliable plate only · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.552× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 429 | 1 (1 ⚠) | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +16.0) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.420× (z -13.0) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 0.330× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 319 | 0 | 5 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.405× (z -15.0) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 202 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.503× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.529× (z -9.3) |
| [[COLO 205 (line)]] | alt | 518 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -22.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.481× (z -9.6) |
| [[LS 180 (line)]] | wt | 466 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.389× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.428× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 289 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[TAK-733 (drug)]] 5 µM 0.324× (z -8.5) |
| [[H4 (line)]] | wt | 245 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.443× (z -8.8) |
| [[PANC-1 (line)]] | alt | 192 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.593× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 425 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.412× (z -11.7) ⚠ toxic |
| [[HOP62 (line)]] | alt | 208 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.503× (z -9.9) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 332 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.449× (z -11.7) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 224 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.293× (z -16.7) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 208 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.369× (z -10.8) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 359 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.404× (z -14.4) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 216 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.563× (z -8.5) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 145 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 404 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.459× (z -12.2) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 249 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.569× (z -9.4) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 205 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.509× (z -9.6) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 278 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.355× (z -16.7) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 171 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.486× (z -8.8) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 513 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.394× (z -15.7) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 208 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.420× (z -12.2) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 237 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.458× (z -12.1) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 210 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.53× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 186 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 214 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.496× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[NCI-H2347 (line)]] | alt | 165 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.507× (z -9.8) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 207 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.380× (z -9.9) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 124 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 157 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 219 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 163 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 264 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 167 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 362 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 255 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5792), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLU7]] | +0.85 | +0.80 / +0.85 | both halves | 7e-06 |  |
| [[CCDC186]] | +0.74 | +0.65 / +0.76 | both halves | 7e-06 | STRING 458 |
| [[CIR1]] | +0.73 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[ARID4A]] | +0.73 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[SYF2]] | +0.73 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[NKAP]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[TMF1]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 | same gene group; pathway: Intra-Golgi and retrograde Golgi-to-ER traffic; STRING 782 |
| [[TERF2IP]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[AKAP9]] | +0.70 | +0.73 / +0.69 | both halves | 7e-06 | STRING 723 |
| [[ZKSCAN1]] | +0.69 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[YTHDC1]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[UPF2]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.65 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[RPSA]] | -0.64 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[WDR77]] | -0.64 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[GOT2]] | -0.63 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[TMEM33]] | -0.62 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[LARP1]] | -0.62 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[CS]] | -0.62 | -0.59 / -0.72 | both halves | 7e-06 |  |
| [[PRPS1]] | -0.61 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[PPP5C]] | -0.61 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[CAD]] | -0.61 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[ANKRD52]] | -0.61 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[TFDP1]] | -0.60 | -0.60 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCS1]] | B | NCS1 activity lowers GCC2's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 1.76× higher at baseline in the lines without NCS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[DHRS3]] | B | DHRS3 activity raises GCC2's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 1.24× lower at baseline in the lines without DHRS3 | 0.086 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.767). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.8, -45.2); signed map (-12.6, 6.8). **Vector** length 145, 51.6% of its response variance represented; |z| ≥ 3 in 1,237 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.3 | +5.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +3.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +4.3 | +3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.1 | +1.0 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | +3.5 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.4 | +2.3 |
|  | [[Resveratrol (drug)]] 5 µM |  | +3.3 | +2.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +3.2 | +1.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -15.8 | -14.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.9 | -7.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -8.2 | -5.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -8.0 | -6.2 |
|  | [[EX229 (drug)]] 5 µM |  | -7.9 | -6.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.4 | -6.5 |

## What is on record

|  |  |
|---|---|
| Name | GRIP and coiled-coil domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q12.3 — chr2:108,449,107-108,509,415 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GCC185, KIAA0336 |
| Gene groups (HGNC) | Golgins |
| Reactome | 7 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Signaling by ALK fusions and activated point mutants; Signaling by ALK in cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWJ2](https://www.uniprot.org/uniprotkb/Q8IWJ2) (GRIP and coiled-coil domain-containing protein 2):

> Golgin which probably tethers transport vesicles to the trans-Golgi network (TGN) and regulates vesicular transport between the endosomes and the Golgi. As a RAB9A effector it is involved in recycling of the mannose 6-phosphate receptor from the late endosomes to the TGN. May also play a role in transport between the recycling endosomes and the Golgi. Required for maintenance of the Golgi structure, it is involved in the biogenesis of noncentrosomal, Golgi-associated microtubules through …

**Summary**, from NCBI Gene [9648](https://www.ncbi.nlm.nih.gov/gene/9648):

> The protein encoded by this gene is a peripheral membrane protein localized to the trans-Golgi network. It is sensitive to brefeldin A. This encoded protein contains a GRIP domain which is thought to be used in targeting. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2009]

**Accessions** — [HGNC:23218](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23218) · Entrez [9648](https://www.ncbi.nlm.nih.gov/gene/9648) · UniProt [Q8IWJ2](https://www.uniprot.org/uniprotkb/Q8IWJ2) · Ensembl [ENSG00000135968](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135968)

## Data

Gene col 5792: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5792); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5792, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5792]; `tensor/DDL_lfc|DDL_z.npy` [5792]; `embed/gene_vectors.npy` [5792]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5792 or target_col == 5792). Every well: [[GCC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

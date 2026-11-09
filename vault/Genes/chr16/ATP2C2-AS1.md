---
symbol: "ATP2C2-AS1"
type: "gene"
col: 15337
ensembl_id: "ENSG00000261286"
name: "ATP2C2 antisense RNA 1"
location: "16q24.1"
module: 101
arm: "+"
pooled_cpm: 5.3
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# ATP2C2-AS1

*ATP2C2 antisense RNA 1* — 16q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.65× (z +18.2, q 0e+00, up in 41 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.10× (z +11.0, q 9e-26, up in 21 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-172 27.6×, HOP62 10.9×, BT-474 78.8×, J82 8.67×, …); [[Adagrasib (drug)]] 0.05 µM in 5 lines (HOP62 1.95×, A498 1.93×, HEC-1-A 1.86×, NCI-H1573 1.80×, …; ⚠ position not correctable); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 12.0×).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.481× (z -7.7, q 9e-12, down in 27 of 46 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.465× (z -4.2, q 0.004, down in 14 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (A549 0.0715×, NCI-H23 0.0927×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0413×; ⚠ cell-cycle shift, explains ~83% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.179×; ⚠ cell-cycle shift, would explain all of this change); [[Thymol (drug)]] 0.5 µM in 1 line (LoVo 0.0982×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMRN2]] (+0.66, fdr 1e-05), [[MSANTD3-TMEFF1]] (+0.60, fdr 1e-05), [[MEAK7]] (+0.60, fdr 7e-06, ⚠ read-through risk), [[NOTCH2NLC]] (+0.59, fdr 1e-05); moves opposite to [[SDHAF1]] (-0.56, fdr 2e-05), [[GAPVD1]] (-0.53, fdr 3e-05), [[KIAA2013]] (-0.53, fdr 4e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ADTRP]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MEAK7]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15337.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-172 27.6×, HOP62 10.9×, BT-474 78.8×, J82 8.67×, …); [[Adagrasib (drug)]] 0.05 µM in 5 lines (HOP62 1.95×, A498 1.93×, HEC-1-A 1.86×, NCI-H1573 1.80×, …; ⚠ position not correctable); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 12.0×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.65×** | +18.2 | 0e+00 | 41/47 (HOP62, A498, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.10×** | +11.0 | 9e-26 | 21/38 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Rimonabant (Hydrochloride) (drug)]] 0.05 µM | ⚠ unreliable plate only; position correction uncertain | **1.67×** | +5.4 | 2e-05 | 17/43 (A498, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +4.0 | 0.009 | 6/25 (HT-29, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 1.36× | +3.2 | 0.14 | 3/37 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.45× | +3.1 | 0.19 | 1/11 (HEC-1-A) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15337.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (A549 0.0715×, NCI-H23 0.0927×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0413×; ⚠ cell-cycle shift, explains ~83% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.179×; ⚠ cell-cycle shift, would explain all of this change); [[Thymol (drug)]] 0.5 µM in 1 line (LoVo 0.0982×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.481×** | -7.7 | 9e-12 | 27/46 (H4, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.659×** | -4.4 | 0.003 | 14/43 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.669×** | -4.2 | 0.004 | 17/43 (HEC-1-A, NCI-H1573, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.465×** | -4.2 | 0.004 | 14/40 (NCI-H1792, H4, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.711×** | -3.6 | 0.037 | 16/42 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **0.723×** | -3.4 | 0.061 | 17/34 (A549, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.732×** | -3.3 | 0.080 | 11/45 (NCI-H1792, H4, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.803×** | -3.3 | 0.080 | 11/45 (NCI-H460, SNU-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.688× | -3.1 | 0.12 | 8/28 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.748× | -3.0 | 0.12 | 5/45 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.05 µM |  | 0.737× | -3.0 | 0.12 | 4/43 (SW1417, HOP62, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.751× | -3.0 | 0.12 | 13/44 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15337. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 11.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +21.8) | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.86× (z +10.5) ⚠ position not correctable | [[Panobinostat (drug)]] 0.5 µM 0.149× (z -9.8) ⚠ cell-cycle shift, explains ~56% of this change |
| [[HOP62 (line)]] | alt | 9.38 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +15.9) | — |
| [[LOX-IMVI (line)]] | wt | 9.73 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0413× (z -14.8) ⚠ cell-cycle shift, explains ~83% of this change |
| [[NCI-H1573 (line)]] | alt | 9.21 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.80× (z +9.5) ⚠ position not correctable | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0743× (z -9.9) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 3.43 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +9.4) | — |
| [[A498 (line)]] | wt | 5.15 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.93× (z +10.6) ⚠ position not correctable | — |
| [[A549 (line)]] | wt | 6.38 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0715× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[BT-474 (line)]] | alt | 3.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 78.8× (z +15.2) | — |
| [[J82 (line)]] | alt | 8.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.67× (z +12.2) | — |
| [[LoVo (line)]] | wt | 3.15 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0982× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 7.91 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0927× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[A-427 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15337), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMRN2]] | +0.66 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[MSANTD3-TMEFF1]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[MEAK7]] | +0.60 | +0.71 / +0.61 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 9.0 kb 3′ of MEAK7 on the same strand (can correlate by spillover, not regulation) |
| [[NOTCH2NLC]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[FMNL3]] | +0.58 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[DNAH17]] | +0.56 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[ABR]] | +0.54 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[CYFIP1]] | +0.53 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[NOTCH2NLB]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[SSUH2]] | +0.52 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[SLC45A3]] | +0.52 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[SMCO2]] | +0.51 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[ROBO4]] | +0.51 | +0.49 / +0.37 | both halves | 9e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF1]] | -0.56 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[GAPVD1]] | -0.53 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[KIAA2013]] | -0.53 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[TYW1]] | -0.52 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[TMEM276]] | -0.52 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[MICOS13]] | -0.51 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[MRPL34]] | -0.49 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[LAMTOR2]] | -0.48 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[B4GAT1]] | -0.48 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[LSM2]] | -0.47 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[PPP2R5E]] | -0.47 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[HS2ST1]] | -0.46 | -0.38 / -0.48 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADTRP]] | B | ADTRP activity raises ATP2C2-AS1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 1.72× lower at baseline in the lines without ADTRP | 0.031 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[SYNPO]] | B | SYNPO activity raises ATP2C2-AS1's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 1.51× lower at baseline in the lines without SYNPO | 0.042 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[LTBP2]] | B | LTBP2 activity raises ATP2C2-AS1's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 1.52× lower at baseline in the lines without LTBP2 | 0.067 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[HDAC6]] | B | HDAC6 activity raises ATP2C2-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ROBO4]] | B | ROBO4 activity raises ATP2C2-AS1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 1.55× lower at baseline in the lines without ROBO4 | 0.095 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[CROCC]] | C | CROCC's natural level strengthens ATP2C2-AS1's drug response | CROCC's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.10; direction not clear | 0.066 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEAK7]] | C | ATP2C2-AS1's natural level strengthens MEAK7's drug response | ATP2C2-AS1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.27; direction not clear | 0.044 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.513). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.4, -3.5); signed map (18.6, 43.2). **Vector** length 54.1, 7.26% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +11.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.8 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.4 | +1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.3 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +0.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.0 | +0.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -1.6 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | -1.4 | -2.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.4 | -2.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ATP2C2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16q24.1 — chr16:84,459,259-84,467,361 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-517C16.2-001, RP11-517C16.2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53167](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53167) · Entrez [105371374](https://www.ncbi.nlm.nih.gov/gene/105371374) · Ensembl [ENSG00000261286](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261286)

## Data

Gene col 15337: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15337); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15337, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15337]; `tensor/DDL_lfc|DDL_z.npy` [15337]; `embed/gene_vectors.npy` [15337]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15337 or target_col == 15337). Every well: [[ATP2C2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP2C2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

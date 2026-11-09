---
symbol: "SMC5"
type: "gene"
col: 12721
ensembl_id: "ENSG00000198887"
name: "structural maintenance of chromosomes 5"
location: "9q21.12"
module: 199
arm: "+"
pooled_cpm: 243.74
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/199"]
generated_by: "tahoemap"
---

# SMC5

*structural maintenance of chromosomes 5* — 9q21.12

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H1573 1.73×, NCI-H23 1.62×, BT-474 1.51×, HS-578T 1.46×, …; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SHP-77 1.94×, C32 1.81×; ⚠ cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (C32 2.06×, SHP-77 1.87×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1573 1.84×).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.658× (z -16.1, q 0e+00, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAPG]] (+0.61, fdr 2e-05), [[PCMT1]] (+0.60, fdr 7e-05), [[CALU]] (+0.59, fdr 1e-05); moves opposite to [[RNF146]] (-0.61, fdr 2e-05), [[TIGD6]] (-0.60, fdr 1e-05), [[HOMEZ]] (-0.60, fdr 4e-05).
> It is in [[Module 199]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12721.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H1573 1.73×, NCI-H23 1.62×, BT-474 1.51×, HS-578T 1.46×, …; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SHP-77 1.94×, C32 1.81×; ⚠ cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (C32 2.06×, SHP-77 1.87×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1573 1.84×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +4.8 | 9e-04 | 0/50 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.9 | 0.023 | 17/48 (SHP-77, C32, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.14× | +3.6 | 0.059 | 17/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12721.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.658×** | -16.1 | 0e+00 | 42/49 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.694×** | -9.6 | 3e-19 | 30/48 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.706×** | -9.5 | 5e-19 | 38/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.812×** | -8.0 | 1e-13 | 33/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.754×** | -7.4 | 1e-11 | 33/47 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.778×** | -6.8 | 8e-10 | 34/48 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.802×** | -5.8 | 4e-07 | 31/48 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.815×** | -5.6 | 2e-06 | 25/49 (RKO, J82, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.771×** | -5.1 | 3e-05 | 32/47 (HEC-1-A, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.826×** | -5.0 | 3e-05 | 26/50 (H4, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.790×** | -4.7 | 1e-04 | 25/45 (J82, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.841× | -4.7 | 1e-04 | 22/48 (A-172, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change | 0.839× | -4.6 | 2e-04 | 19/44 (SW48, J82, …) | all doses, flat | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | 0.839× | -4.6 | 2e-04 | 23/48 (MIA PaCa-2, hTERT-HPNE, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.859× | -4.0 | 0.003 | 18/48 (H4, HOP62, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.879× | -3.4 | 0.022 | 13/48 (hTERT-HPNE, SW 1271, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.789×** | -3.4 | 0.023 | 23/49 (HS-578T, J82, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.886× | -3.3 | 0.029 | 11/48 (PANC-1, SK-MEL-2, …) | top dose only |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.883× | -3.2 | 0.037 | 6/48 (HCT15, A549, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.801×** | -3.2 | 0.043 | 21/47 (RKO, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.856× | -3.0 | 0.063 | 13/48 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12721. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 312 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -12.4) |
| [[A-172 (line)]] | wt | 273 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.581× (z -13.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.470× (z -13.3) |
| [[H4 (line)]] | wt | 300 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -16.4) |
| [[J82 (line)]] | alt | 358 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -14.5) |
| [[A498 (line)]] | wt | 291 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.464× (z -12.9) |
| [[HOP62 (line)]] | alt | 305 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 139 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +12.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.84× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.562× (z -8.7) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 177 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.535× (z -11.7) |
| [[SHP-77 (line)]] | alt | 227 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-423 (line)]] | alt | 288 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -14.3) |
| [[A549 (line)]] | wt | 234 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -21.3) |
| [[AsPC-1 (line)]] | alt | 236 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.589× (z -12.6) |
| [[BT-474 (line)]] | alt | 166 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -10.1) |
| [[C32 (line)]] | wt | 196 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.06× (z +10.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 159 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -14.7) |
| [[HCT15 (line)]] | alt | 405 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -13.7) |
| [[KATO III (line)]] | alt | 310 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -14.8) |
| [[LoVo (line)]] | wt | 238 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.658× (z -10.8) |
| [[LS 180 (line)]] | wt | 212 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.532× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 220 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.519× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 225 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -15.3) |
| [[NCI-H2347 (line)]] | alt | 235 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 312 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -12.5) |
| [[RKO (line)]] | wt | 292 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -16.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 216 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.507× (z -10.0) |
| [[SW48 (line)]] | wt | 338 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -14.9) |
| [[C-33 A (line)]] | alt | 290 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.502× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 233 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 374 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -20.4) |
| [[HepG2_C3A (line)]] | wt | 195 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Hs 766T (line)]] | wt | 216 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.482× (z -10.3) |
| [[HS-578T (line)]] | alt | 224 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -13.4) |
| [[LOX-IMVI (line)]] | wt | 213 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.660× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 196 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +10.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 229 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.666× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 232 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -13.7) |
| [[SW480 (line)]] | alt | 310 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -16.5) |
| [[A-427 (line)]] | wt | 165 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 199 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 294 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 314 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 272 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12721), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*33 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAPG]] | +0.61 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[PCMT1]] | +0.60 | +0.58 / +0.38 | both halves | 7e-05 |  |
| [[CALU]] | +0.59 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[GP6-AS1]] | +0.57 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[PHKA2]] | +0.56 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[KANK2]] | +0.56 | +0.45 / +0.40 | both halves | 5e-05 |  |
| [[TTC3]] | +0.55 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[SLC25A42]] | +0.54 | +0.44 / +0.38 | both halves | 6e-05 |  |
| [[RBM44]] | +0.53 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[NUP160]] | +0.53 | +0.57 / +0.35 | both halves | 1e-04 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[GGCT]] | +0.53 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[PTPRS]] | +0.53 | +0.41 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*67 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF146]] | -0.61 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[TIGD6]] | -0.60 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[HOMEZ]] | -0.60 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[GAS2]] | -0.57 | -0.57 / -0.25 | both halves | 4e-04 |  |
| [[PLS3-AS1]] | -0.56 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[LINC02100]] | -0.56 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[PATL2]] | -0.55 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[LINC00938]] | -0.55 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[SCAMP1-AS1]] | -0.54 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[DNAI4]] | -0.54 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[ZNF827]] | -0.54 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[TAFA2]] | -0.54 | -0.57 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SMC5's level | compounds that target TOP2A: 3 of 5 lower it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 199]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.484). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.1, 15.6); signed map (-44.0, 9.2). **Vector** length 116, 35.9% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.9 | +2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.9 | +2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +3.0 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.7 | +1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +0.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.5 | +0.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -9.2 | -9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -16.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.5 | -9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.1 | -8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -6.1 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.0 | -4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.0 | -4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | structural maintenance of chromosomes 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.12 — chr9:70,258,978-70,354,873 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0594; previously SMC5L1 |
| Gene groups (HGNC) | Structural maintenance of chromosomes proteins; SMC5/6 complex |
| Reactome | 3 pathways, smallest: SUMOylation of DNA damage response and repair proteins; SUMO E3 ligases SUMOylate target proteins; SUMOylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IY18](https://www.uniprot.org/uniprotkb/Q8IY18) (Structural maintenance of chromosomes protein 5):

> Core component of the SMC5-SMC6 complex, a complex involved in repair of DNA double-strand breaks by homologous recombination. The complex may promote sister chromatid homologous recombination by recruiting the SMC1-SMC3 cohesin complex to double-strand breaks. The complex is required for telomere maintenance via recombination in ALT (alternative lengthening of telomeres) cell lines and mediates sumoylation of shelterin complex (telosome) components which is proposed to lead to shelterin …

**Summary**, from NCBI Gene [23137](https://www.ncbi.nlm.nih.gov/gene/23137):

> Enables DNA secondary structure binding activity. Involved in several processes, including DNA recombination; host-mediated suppression of viral genome replication; and positive regulation of cell cycle process. Located in chromosome and nuclear body. Part of Smc5-Smc6 complex. Is active in nucleus. Implicated in mosaic variegated aneuploidy syndrome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20465](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20465) · Entrez [23137](https://www.ncbi.nlm.nih.gov/gene/23137) · UniProt [Q8IY18](https://www.uniprot.org/uniprotkb/Q8IY18) · Ensembl [ENSG00000198887](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198887)

## Data

Gene col 12721: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12721); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12721, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12721]; `tensor/DDL_lfc|DDL_z.npy` [12721]; `embed/gene_vectors.npy` [12721]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12721 or target_col == 12721). Every well: [[SMC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

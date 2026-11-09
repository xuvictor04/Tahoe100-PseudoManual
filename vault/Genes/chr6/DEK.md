---
symbol: "DEK"
type: "gene"
col: 4575
ensembl_id: "ENSG00000124795"
name: "DEK proto-oncogene"
location: "6p22.3"
module: 22
arm: "+"
pooled_cpm: 273.53
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# DEK

*DEK proto-oncogene* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.16× (z +22.0, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 1.36× (z +3.3, q 0.055, up in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 15 lines (NCI-H1792 7.23×, A549 5.57×, SNU-423 6.51×, SW480 4.12×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 1.71×).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.709× (z -7.5, q 3e-11, down in 35 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSIP1]] (+0.76, fdr 7e-06), [[SMC4]] (+0.70, fdr 7e-06), [[CENPU]] (+0.69, fdr 7e-06); moves opposite to [[PEX16]] (-0.56, fdr 3e-05), [[MRPS12]] (-0.54, fdr 1e-04).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MYBL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4575.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 15 lines (NCI-H1792 7.23×, A549 5.57×, SNU-423 6.51×, SW480 4.12×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 1.71×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.16×** | +22.0 | 0e+00 | 49/49 (NCI-H1792, A549, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.48×** | +15.9 | 0e+00 | 44/44 (A549, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.02×** | +15.8 | 0e+00 | 45/45 (SW1417, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~68% of this change | **1.43×** | +5.5 | 7e-06 | 43/48 (HT-29, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.48×** | +5.0 | 8e-05 | 41/47 (C32, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.22×** | +4.3 | 0.002 | 27/48 (SNU-1, HT-29, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **1.31×** | +4.2 | 0.003 | 34/48 (KATO III, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +4.0 | 0.004 | 34/48 (KATO III, hTERT-HPNE, …) | rises with dose | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.055 | 32/48 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.12 | 9/49 (Hs 766T, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4575.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -7.5 | 3e-11 | 35/49 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.643×** | -6.8 | 2e-09 | 37/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.703×** | -5.4 | 1e-05 | 37/48 (J82, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **0.782×** | -5.4 | 1e-05 | 31/48 (A-427, A-172, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.713×** | -4.9 | 9e-05 | 36/48 (LS 180, SW48, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.766×** | -4.1 | 0.004 | 33/48 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.708×** | -3.7 | 0.016 | 29/48 (A-427, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.647×** | -3.5 | 0.032 | 29/48 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 0.676× | -3.2 | 0.10 | 26/49 (LS 180, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4575. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 375 | 5 (5 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +18.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -11.3) |
| [[SW480 (line)]] | alt | 334 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +19.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -14.6) |
| [[LS 180 (line)]] | wt | 298 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +18.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -12.1) |
| [[A-427 (line)]] | wt | 262 | 3 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +14.6) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.433× (z -13.8) ⚠ cell-cycle shift, explains ~98% of this change |
| [[A498 (line)]] | wt | 202 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +16.2) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.458× (z -11.7) ⚠ cell-cycle shift, explains ~98% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -8.6) |
| [[J82 (line)]] | alt | 1,097 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +18.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.444× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 264 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +17.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -14.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -11.1) |
| [[SW1417 (line)]] | alt | 315 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +17.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.516× (z -9.8) |
| [[A-172 (line)]] | wt | 205 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +15.1) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.404× (z -13.3) ⚠ cell-cycle shift, explains ~98% of this change |
| [[AsPC-1 (line)]] | alt | 199 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +11.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.465× (z -9.5) |
| [[C32 (line)]] | wt | 144 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.46× (z +17.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 356 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +16.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -10.8) |
| [[LoVo (line)]] | wt | 277 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.06× (z +18.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -11.6) |
| [[A549 (line)]] | wt | 161 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +20.0) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 390 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +13.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 220 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +17.1) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 181 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.16× (z +13.5) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 235 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +13.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 265 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +13.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -9.4) |
| [[HOP62 (line)]] | alt | 234 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.28× (z +17.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 155 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +17.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 218 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.81× (z +17.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 267 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +17.9) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 175 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.37× (z +17.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 256 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.61× (z +16.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 85.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +15.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 122 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.23× (z +21.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 280 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +13.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 328 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 139 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +16.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 330 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +18.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 328 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +18.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 300 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +14.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 198 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +15.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 245 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +13.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 199 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +13.5) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 362 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.51× (z +19.9) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 155 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +15.8) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 335 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +12.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 326 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +14.7) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 205 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +9.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 164 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +11.8) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 189 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +14.4) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 233 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +12.0) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 159 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0643× (z -9.4) |
| [[AN3 CA (line)]] | alt | 424 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 343 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 479 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4575), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSIP1]] | +0.76 | +0.72 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 464 |
| [[SMC4]] | +0.70 | +0.66 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 514 |
| [[CENPU]] | +0.69 | +0.66 / +0.75 | both halves | 7e-06 |  |
| [[YEATS4]] | +0.68 | +0.73 / +0.57 | both halves | 1e-05 | pathway: Transcriptional regulation by the AP-2 (TFAP2) family of transcription factors |
| [[SGO1]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[PRC1]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 | STRING 440 |
| [[DIAPH3]] | +0.66 | +0.62 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[KIF15]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 | STRING 449 |
| [[SYNE2]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SKA3]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ANLN]] | +0.65 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[SKA1]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX16]] | -0.56 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[MRPS12]] | -0.54 | -0.35 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYBL1]] | B | MYBL1 activity raises DEK's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.24× lower at baseline in the lines without MYBL1 | 0.031 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[ZNF726]] | B | ZNF726 activity raises DEK's level | lines that do not express ZNF726 (20) vs lines expressing it (30) | 1.17× lower at baseline in the lines without ZNF726 | 0.055 | ⚠ within organs, on part of the lines; also absent: SUSD5, RNF150, BVES |
| [[CDCA7L]] | B | CDCA7L activity raises DEK's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.13× lower at baseline in the lines without CDCA7L | 0.071 | ⚠ within organs, on part of the lines |
| [[HDAC6]] | B | HDAC6 activity raises DEK's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PBK]] | C | PBK activity raises DEK's level | lines that do not express PBK (4) vs lines expressing it (46) | 1.47× lower at baseline in the lines without PBK | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.591). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.1, -52.2); signed map (-47.5, -46.8). **Vector** length 111, 47.5% of its response variance represented; |z| ≥ 3 in 1,068 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Condensation of Prometaphase Chromosomes* (reactome, mean cos +0.57 to 8); *Kinesins* (reactome, mean cos +0.55 to 10); *Factors involved in megakaryocyte development and platelet production* (reactome, mean cos +0.50 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.2 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +0.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | -2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.2 | -1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -7.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | -6.0 | -5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.9 | -0.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | -5.3 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -1.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | -4.5 | -2.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -4.5 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -3.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.8 | -1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | DEK proto-oncogene |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:18,223,860-18,264,548 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D6S231E |
| Gene groups (HGNC) | B-WICH chromatin-remodelling complex subunits |
| Hallmark sets | E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 5 pathways, smallest: Transcriptional regulation by the AP-2 (TFAP2) family of transcription factors; Transcriptional regulation of granulopoiesis; B-WICH complex positively regulates rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [P35659](https://www.uniprot.org/uniprotkb/P35659) (Protein DEK):

> Involved in chromatin organization.

**Summary**, from NCBI Gene [7913](https://www.ncbi.nlm.nih.gov/gene/7913):

> This gene encodes a protein with one SAP domain. This protein binds to cruciform and superhelical DNA and induces positive supercoils into closed circular DNA, and is also involved in splice site selection during mRNA processing. Chromosomal aberrations involving this region, increased expression of this gene, and the presence of antibodies against this protein are all associated with various diseases. Two transcript variants encoding different isoforms have been found for this gene. [provided …

**Accessions** — [HGNC:2768](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2768) · Entrez [7913](https://www.ncbi.nlm.nih.gov/gene/7913) · UniProt [P35659](https://www.uniprot.org/uniprotkb/P35659) · Ensembl [ENSG00000124795](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124795)

## Data

Gene col 4575: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4575); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4575, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4575]; `tensor/DDL_lfc|DDL_z.npy` [4575]; `embed/gene_vectors.npy` [4575]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4575 or target_col == 4575). Every well: [[DEK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DEK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "NT5C2"
type: "gene"
col: 1160
ensembl_id: "ENSG00000076685"
name: "5'-nucleotidase, cytosolic II"
location: "10q24.32-q24.33"
module: 8
arm: "+"
pooled_cpm: 251.95
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 26
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 21
direction_downstream: 0
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# NT5C2

*5'-nucleotidase, cytosolic II* — 10q24.32-q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.25× (z +5.6, q 7e-06, up in 25 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.23× (z +5.6, q 7e-06, up in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (MIA PaCa-2 1.90×, J82 1.66×, PANC-1 1.45×, HOP62 1.48×; ⚠ cell-cycle shift, would explain all of this change); [[Bortezomib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 1.86×, H4 2.31×; ⚠ cell-cycle shift, explains ~40% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 2.01×; ⚠ cell-cycle shift, explains ~8% of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (MIA PaCa-2 1.72×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.70×).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.711× (z -13.0, q 1e-35, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYH14]] (+0.57, fdr 2e-05), [[FUT2]] (+0.54, fdr 4e-05), [[TC2N]] (+0.50, fdr 3e-05); moves opposite to [[ARL10]] (-0.48, fdr 5e-05), [[PTPN14]] (-0.45, fdr 1e-04), [[HAS2]] (-0.44, fdr 2e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[CATSPERB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1160.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (MIA PaCa-2 1.90×, J82 1.66×, PANC-1 1.45×, HOP62 1.48×; ⚠ cell-cycle shift, would explain all of this change); [[Bortezomib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 1.86×, H4 2.31×; ⚠ cell-cycle shift, explains ~40% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 2.01×; ⚠ cell-cycle shift, explains ~8% of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (MIA PaCa-2 1.72×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.70×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.25×** | +5.6 | 7e-06 | 25/48 (MIA PaCa-2, H4, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +5.6 | 7e-06 | 26/48 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +3.5 | 0.083 | 17/48 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.30× | +3.2 | 0.18 | 15/50 (NCI-H1573, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 23 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1160.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -13.0 | 1e-35 | 39/49 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.715×** | -9.0 | 4e-17 | 34/48 (Panc 03.27, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.699×** | -8.9 | 9e-17 | 30/45 (CFPAC-1, NCI-H460, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.730×** | -8.5 | 4e-15 | 39/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.745×** | -7.9 | 3e-13 | 33/48 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.748×** | -7.8 | 5e-13 | 32/48 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.756×** | -7.5 | 4e-12 | 28/48 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.821×** | -7.5 | 4e-12 | 22/48 (Panc 03.27, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **0.760×** | -7.1 | 7e-11 | 27/44 (SNU-1, CFPAC-1, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.774×** | -6.9 | 3e-10 | 32/48 (CFPAC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.779×** | -6.7 | 1e-09 | 28/49 (NCI-H460, CFPAC-1, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.844× | -6.4 | 5e-09 | 21/48 (SW1417, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.782×** | -6.4 | 9e-09 | 28/48 (NCI-H460, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.792×** | -6.3 | 1e-08 | 33/48 (SW48, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.809×** | -5.7 | 4e-07 | 24/48 (NCI-H23, LS 180, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.629×** | -5.7 | 5e-07 | 39/48 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.666×** | -5.0 | 2e-05 | 33/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.681×** | -4.7 | 6e-05 | 28/48 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.705×** | -4.3 | 4e-04 | 22/47 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.719×** | -4.0 | 0.001 | 24/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.871× | -3.7 | 0.004 | 16/48 (LS 180, SW480, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.754×** | -3.4 | 0.010 | 18/48 (NCI-H2347, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.885× | -3.3 | 0.018 | 17/48 (LoVo, BT-474, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.777×** | -3.1 | 0.034 | 15/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.898× | -2.8 | 0.082 | 17/48 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.898× | -2.7 | 0.091 | 9/49 (A549, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1160. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 671 | 0 | 18 (15 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -30.8) |
| [[CFPAC-1 (line)]] | alt | 496 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -17.4) |
| [[HT-29 (line)]] | alt | 333 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -18.0) |
| [[LoVo (line)]] | wt | 335 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 282 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -19.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.594× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 423 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -14.1) |
| [[COLO 205 (line)]] | alt | 322 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -10.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.485× (z -9.7) |
| [[BT-474 (line)]] | alt | 267 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -12.8) |
| [[LS 180 (line)]] | wt | 245 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -13.5) |
| [[MIA PaCa-2 (line)]] | alt | 206 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +15.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.72× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 285 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.421× (z -12.0) ⚠ cell-cycle shift, explains ~75% of this change |
| [[A498 (line)]] | wt | 220 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.612× (z -13.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 286 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -17.2) |
| [[C-33 A (line)]] | alt | 272 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -10.7) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.522× (z -8.8) |
| [[SNU-423 (line)]] | alt | 406 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.336× (z -10.0) |
| [[A-427 (line)]] | wt | 136 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.82× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.510× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HCT15 (line)]] | alt | 189 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[OTS514 (drug)]] 5 µM 0.160× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 177 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.511× (z -9.4) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.631× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 129 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.593× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 200 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.551× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[SNU-1 (line)]] | wt | 288 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -11.8) |
| [[H4 (line)]] | wt | 144 | 1 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 2.31× (z +8.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[HOP62 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -9.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[Hs 766T (line)]] | wt | 345 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.490× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 166 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 237 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -11.8) |
| [[RKO (line)]] | wt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.444× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SW1417 (line)]] | alt | 241 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.548× (z -10.4) ⚠ transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW48 (line)]] | wt | 140 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.362× (z -9.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 154 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.622× (z -9.6) |
| [[A-172 (line)]] | wt | 294 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 333 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 182 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 265 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 118 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 187 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 196 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 105 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 335 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 244 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1160), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYH14]] | +0.57 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[FUT2]] | +0.54 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[TC2N]] | +0.50 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[CDH3]] | +0.50 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[BICDL2]] | +0.50 | +0.34 / +0.46 | both halves | 1e-04 |  |
| [[IL22RA1]] | +0.50 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[MAP3K8]] | +0.49 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[C6orf132]] | +0.48 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[CATSPERB]] | +0.48 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[UBE2H]] | +0.48 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[MUC4]] | +0.47 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[RBM47]] | +0.47 | +0.44 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL10]] | -0.48 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[PTPN14]] | -0.45 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[HAS2]] | -0.44 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[ATXN7L3B]] | -0.43 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[AGPAT5]] | -0.42 | -0.37 / -0.42 | both halves | 9e-05 |  |
| [[ZNF717]] | -0.42 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[ANPEP]] | -0.41 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[COL6A3]] | -0.41 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[KIAA1549L]] | -0.40 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[C8orf58]] | -0.40 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[NHSL1-AS1]] | -0.40 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[CHST14]] | -0.39 | -0.48 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 21, C 0. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CATSPERB]] | B | CATSPERB activity raises NT5C2's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 1.46× lower at baseline in the lines without CATSPERB | 0.008 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[SIDT1]] | B | SIDT1 activity strengthens NT5C2's drug response | lines that do not express SIDT1 (32) vs lines expressing it (17) | the lines without SIDT1 respond 0.57× as strongly (z diff +2.48); strongest at Panobinostat 5 µM: 0.81x vs 0.59x (z diff +3.8) | 0.016 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2; target measured in part of the lines; artifact flags |
| [[SIDT1]] | B | SIDT1 activity raises NT5C2's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 1.44× lower at baseline in the lines without SIDT1 | 0.019 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[LIPH]] | B | LIPH activity raises NT5C2's level | lines that do not express LIPH (27) vs lines expressing it (23) | 1.44× lower at baseline in the lines without LIPH | 0.020 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[CYP4F12]] | B | CYP4F12 activity raises NT5C2's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 1.47× lower at baseline in the lines without CYP4F12 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[PSMB5]] | B | PSMB5 activity lowers NT5C2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TC2N]] | B | TC2N activity raises NT5C2's level | lines that do not express TC2N (28) vs lines expressing it (22) | 1.40× lower at baseline in the lines without TC2N | 0.033 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[CATSPERB]] | B | CATSPERB activity strengthens NT5C2's drug response | lines that do not express CATSPERB (30) vs lines expressing it (19) | the lines without CATSPERB respond 0.55× as strongly (z diff +2.45); strongest at Belinostat 5 µM: 0.81x vs 0.59x (z diff +3.7) | 0.036 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14; target measured in part of the lines; artifact flags |
| [[JUP]] | B | JUP activity raises NT5C2's level | lines that do not express JUP (16) vs lines expressing it (34) | 1.42× lower at baseline in the lines without JUP | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[TC2N]] | B | TC2N activity strengthens NT5C2's drug response | lines that do not express TC2N (28) vs lines expressing it (21) | the lines without TC2N respond 0.56× as strongly (z diff +2.29); strongest at Panobinostat 5 µM: 0.83x vs 0.61x (z diff +3.5) | 0.039 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14; target measured in part of the lines; artifact flags |
| [[GCNT3]] | B | GCNT3 activity raises NT5C2's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 1.47× lower at baseline in the lines without GCNT3 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[ALOX5]] | B | ALOX5 activity raises NT5C2's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 1.37× lower at baseline in the lines without ALOX5 | 0.055 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.423). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.1, 54.5); signed map (60.7, 6.3). **Vector** length 116, 35.5% of its response variance represented; |z| ≥ 3 in 1,325 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.5 | +5.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | +6.3 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.3 | +3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.1 | +1.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.0 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +0.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.8 | -0.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.5 | +0.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.8 | -8.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.5 | -7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -4.8 | -5.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.6 | -5.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.3 | -5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.8 | -5.7 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -3.4 | -1.4 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | 5'-nucleotidase, cytosolic II |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32-q24.33 — chr10:103,087,185-103,277,605 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PNT5, GMP, cN-II, SPG65; previously NT5B, SPG45 |
| Gene groups (HGNC) | 5'-nucleotidases |
| Reactome | 7 pathways, smallest: Abacavir metabolism; Abacavir ADME; Ribavirin ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [P49902](https://www.uniprot.org/uniprotkb/P49902) (Cytosolic purine 5'-nucleotidase):

> Broad specificity cytosolic 5'-nucleotidase that catalyzes the dephosphorylation of 6-hydroxypurine nucleoside 5'-monophosphates. In addition, possesses a phosphotransferase activity by which it can transfer a phosphate from a donor nucleoside monophosphate to an acceptor nucleoside, preferably inosine, deoxyinosine and guanosine. Has the highest activities for IMP and GMP followed by dIMP, dGMP and XMP. Could also catalyze the transfer of phosphates from pyrimidine monophosphates but with …

**Summary**, from NCBI Gene [22978](https://www.ncbi.nlm.nih.gov/gene/22978):

> This gene encodes a hydrolase that serves as an important role in cellular purine metabolism by acting primarily on inosine 5'-monophosphate and other purine nucleotides. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:8022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8022) · Entrez [22978](https://www.ncbi.nlm.nih.gov/gene/22978) · UniProt [P49902](https://www.uniprot.org/uniprotkb/P49902) · Ensembl [ENSG00000076685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076685)

## Data

Gene col 1160: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1160); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1160, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1160]; `tensor/DDL_lfc|DDL_z.npy` [1160]; `embed/gene_vectors.npy` [1160]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1160 or target_col == 1160). Every well: [[NT5C2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NT5C2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

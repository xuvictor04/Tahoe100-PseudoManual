---
symbol: "YWHAG"
type: "gene"
col: 9895
ensembl_id: "ENSG00000170027"
name: "tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein gamma"
location: "7q11.23"
module: 60
arm: "+"
pooled_cpm: 245.72
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 2
n_dd_up_clean: 25
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# YWHAG

*tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein gamma* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.29× (z +19.4, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.856× (z -5.2, q 1e-04, down in 15 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.433×, SK-MEL-2 0.540×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ponatinib (drug)]] 5 µM in 1 line (KATO III 0.510×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.569×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Cabozantinib (S-malate) (drug)]] 5 µM in 1 line (KATO III 0.594×); [[Ponatinib (drug)]] 0.5 µM in 1 line (KATO III 0.604×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTGR1]] (+0.60, fdr 1e-05), [[STIP1]] (+0.58, fdr 1e-05), [[HSPA1B]] (+0.55, fdr 2e-05); moves opposite to [[CEP57]] (-0.55, fdr 2e-05), [[UPF2]] (-0.54, fdr 1e-05), [[TNRC6C]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CLSTN3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9895.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.29×** | +19.4 | 0e+00 | 47/48 (BT-474, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.66×** | +18.9 | 0e+00 | 49/49 (NCI-H2347, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.13×** | +17.7 | 0e+00 | 48/48 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +17.7 | 0e+00 | 39/48 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.89×** | +15.0 | 0e+00 | 48/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.96×** | +14.9 | 0e+00 | 48/48 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.88×** | +14.8 | 0e+00 | 47/48 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +14.3 | 8e-45 | 48/48 (KATO III, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +12.5 | 6e-34 | 47/48 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +11.8 | 3e-30 | 46/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +10.5 | 4e-24 | 40/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.52×** | +9.8 | 3e-21 | 41/48 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.16×** | +9.5 | 1e-19 | 41/48 (C32, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +9.5 | 1e-19 | 36/48 (hTERT-HPNE, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +9.4 | 2e-19 | 39/48 (hTERT-HPNE, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +9.4 | 3e-19 | 39/48 (KATO III, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9895.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.433×, SK-MEL-2 0.540×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ponatinib (drug)]] 5 µM in 1 line (KATO III 0.510×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.569×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Cabozantinib (S-malate) (drug)]] 5 µM in 1 line (KATO III 0.594×); [[Ponatinib (drug)]] 0.5 µM in 1 line (KATO III 0.604×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | 0.856× | -5.2 | 1e-04 | 15/49 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.827×** | -4.5 | 0.001 | 24/48 (KATO III, hTERT-HPNE, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.874× | -4.5 | 0.001 | 12/49 (NCI-H1792, C32, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.829×** | -4.4 | 0.002 | 24/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.847× | -3.9 | 0.011 | 19/48 (C32, LoVo, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.865× | -3.4 | 0.063 | 9/49 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.877× | -3.1 | 0.13 | 14/48 (A-172, MIA PaCa-2, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.878× | -3.1 | 0.13 | 12/48 (C32, J82, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.878× | -3.1 | 0.13 | 11/49 (LoVo, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9895. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 235 | 18 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +17.7) | — |
| [[KATO III (line)]] | alt | 319 | 14 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +19.0) | [[Ponatinib (drug)]] 5 µM 0.510× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 163 | 15 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +17.7) | — |
| [[LS 180 (line)]] | wt | 142 | 14 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +14.5) | — |
| [[PANC-1 (line)]] | alt | 181 | 14 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.79× (z +17.9) | — |
| [[COLO 205 (line)]] | alt | 137 | 13 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +17.6) | — |
| [[NCI-H1792 (line)]] | alt | 215 | 13 (3 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.96× (z +15.5) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 2.92× (z +15.3) | — |
| [[SW480 (line)]] | alt | 209 | 13 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.06× (z +20.1) | — |
| [[LOX-IMVI (line)]] | wt | 180 | 11 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.32× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 188 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +17.4) | — |
| [[Hs 766T (line)]] | wt | 190 | 10 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.62× (z +13.2) | — |
| [[hTERT-HPNE (line)]] | wt | 156 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +21.0) | — |
| [[A498 (line)]] | wt | 427 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +21.0) | — |
| [[HS-578T (line)]] | alt | 221 | 9 | 0 | [[Panobinostat (drug)]] 5 µM 2.69× (z +12.3) | — |
| [[LoVo (line)]] | wt | 240 | 9 | 0 | [[Auranofin (drug)]] 5 µM 2.73× (z +16.7) | — |
| [[SW48 (line)]] | wt | 203 | 9 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.12× (z +12.2) | — |
| [[A-172 (line)]] | wt | 329 | 8 | 0 | [[Auranofin (drug)]] 5 µM 3.71× (z +15.7) | — |
| [[A549 (line)]] | wt | 207 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +13.5) | — |
| [[H4 (line)]] | wt | 275 | 8 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.68× (z +11.5) | — |
| [[NCI-H23 (line)]] | alt | 176 | 8 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.16× (z +11.1) | — |
| [[NCI-H2347 (line)]] | alt | 287 | 6 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.35× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.569× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 313 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +13.4) | [[Dinaciclib (drug)]] 0.05 µM 0.540× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 219 | 8 | 0 | [[Auranofin (drug)]] 5 µM 2.49× (z +12.5) | — |
| [[SW1417 (line)]] | alt | 322 | 8 | 0 | [[TAK-901 (drug)]] 5 µM 4.14× (z +13.1) | — |
| [[A-427 (line)]] | wt | 181 | 6 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.75× (z +15.4) | [[Dinaciclib (drug)]] 0.05 µM 0.433× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 297 | 7 | 0 | [[Auranofin (drug)]] 5 µM 2.70× (z +13.8) | — |
| [[Panc 03.27 (line)]] | alt | 240 | 7 | 0 | [[TAK-901 (drug)]] 5 µM 8.26× (z +15.5) | — |
| [[BT-474 (line)]] | alt | 260 | 6 | 0 | [[Auranofin (drug)]] 5 µM 5.34× (z +24.1) | — |
| [[C32 (line)]] | wt | 592 | 6 | 0 | [[Auranofin (drug)]] 5 µM 3.21× (z +16.9) | — |
| [[CFPAC-1 (line)]] | alt | 246 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.8) | — |
| [[HT-29 (line)]] | alt | 319 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.12× (z +16.0) | — |
| [[NCI-H2030 (line)]] | alt | 152 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.84× (z +13.7) | — |
| [[AsPC-1 (line)]] | alt | 305 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +16.9) | — |
| [[HCT15 (line)]] | alt | 263 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.16× (z +10.1) | — |
| [[HepG2_C3A (line)]] | wt | 189 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.12× (z +9.4) | — |
| [[J82 (line)]] | alt | 251 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 456 | 4 | 0 | [[Auranofin (drug)]] 5 µM 2.88× (z +16.7) | — |
| [[RKO (line)]] | wt | 205 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.29× (z +12.1) | — |
| [[RPMI-7951 (line)]] | alt | 167 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.72× (z +11.5) | — |
| [[SW 900 (line)]] | alt | 231 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +14.0) | — |
| [[C-33 A (line)]] | alt | 166 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.43× (z +10.8) | — |
| [[SNU-1 (line)]] | wt | 173 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.18× (z +11.6) | — |
| [[AN3 CA (line)]] | alt | 296 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.30× (z +11.6) | — |
| [[SHP-77 (line)]] | alt | 155 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.15× (z +9.4) | — |
| [[CHP-212 (line)]] | wt | 224 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 238 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 230 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9895), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTGR1]] | +0.60 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[STIP1]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[HSPA1B]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[DNAJB1]] | +0.52 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[CYP4F11]] | +0.51 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[ANXA1]] | +0.51 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[STON2]] | +0.51 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[GALNT2]] | +0.50 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[HSP90AA2P]] | +0.49 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[NXPE3]] | +0.49 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[NORAD]] | +0.49 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[CLU]] | +0.49 | +0.27 / +0.58 | both halves | 3e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP57]] | -0.55 | -0.48 / -0.53 | both halves | 2e-05 | pathway: AURKA Activation by TPX2 |
| [[UPF2]] | -0.54 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.50 | -0.50 / -0.45 | both halves | 3e-05 | pathway: Cilium Assembly |
| [[FAM76B]] | -0.50 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[UBN2]] | -0.50 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[RSPRY1]] | -0.48 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[PWWP2A]] | -0.46 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[CEP44]] | -0.44 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[CEP95]] | -0.44 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[NDUFAF6]] | -0.44 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[ARID4A]] | -0.44 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[GOLGA2P5]] | -0.44 | -0.29 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLSTN3]] | C | CLSTN3 activity lowers YWHAG's level | lines that do not express CLSTN3 (3) vs lines expressing it (47) | 1.70× higher at baseline in the lines without CLSTN3 | 0.092 | ⚠ few lines (3 vs 47); across organs; also absent: PIM1, HACD1, ENSG00000286782 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.526). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-6.9, 45.8); signed map (38.2, -31.2). **Vector** length 97.4, 36.8% of its response variance represented; |z| ≥ 3 in 1,651 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.5 | +9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.0 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +19.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.7 | +15.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.4 | +17.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +4.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | +0.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -4.8 | +9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | +17.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | +9.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.9 | +11.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.5 | -5.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.4 | -4.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.4 | -3.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.1 | -3.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:76,326,799-76,358,991 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PPP1R170, 14-3-3GAMMA, 14-3-3γ |
| Gene groups (HGNC) | 14-3-3 phospho-serine/phospho-threonine binding proteins |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 53 pathways, smallest: Regulation of localization of FOXO transcription factors; SARS-CoV-2 targets host intracellular signalling and regulatory pathways; Chk1/Chk2(Cds1) mediated inactivation of Cyclin B:Cdk1 complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P61981](https://www.uniprot.org/uniprotkb/P61981) (14-3-3 protein gamma):

> Adapter protein implicated in the regulation of a large spectrum of both general and specialized signaling pathways. Binds to a large number of partners, usually by recognition of a phosphoserine or phosphothreonine motif. Binding generally results in the modulation of the activity of the binding partner. Promotes inactivation of WDR24 component of the GATOR2 complex by binding to phosphorylated WDR24. Participates in the positive regulation of NMDA glutamate receptor activity by promoting the …

**Summary**, from NCBI Gene [7532](https://www.ncbi.nlm.nih.gov/gene/7532):

> This gene product belongs to the 14-3-3 family of proteins which mediate signal transduction by binding to phosphoserine-containing proteins. This highly conserved protein family is found in both plants and mammals, and this protein is 100% identical to the rat ortholog. It is induced by growth factors in human vascular smooth muscle cells, and is also highly expressed in skeletal and heart muscles, suggesting an important role for this protein in muscle tissue. It has been shown to interact …

**Accessions** — [HGNC:12852](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12852) · Entrez [7532](https://www.ncbi.nlm.nih.gov/gene/7532) · UniProt [P61981](https://www.uniprot.org/uniprotkb/P61981) · Ensembl [ENSG00000170027](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170027)

## Data

Gene col 9895: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9895); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9895, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9895]; `tensor/DDL_lfc|DDL_z.npy` [9895]; `embed/gene_vectors.npy` [9895]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9895 or target_col == 9895). Every well: [[YWHAG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YWHAG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "COG5"
type: "gene"
col: 8967
ensembl_id: "ENSG00000164597"
name: "component of oligomeric golgi complex 5"
location: "7q22.3"
module: 40
arm: "+"
pooled_cpm: 397.94
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# COG5

*component of oligomeric golgi complex 5* — 7q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.42× (z +6.9, q 2e-09, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.495× (z -19.7, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM120B]] (+0.77, fdr 1e-05), [[IER3IP1]] (+0.76, fdr 7e-06), [[PRRC1]] (+0.75, fdr 7e-06); moves opposite to [[MED12]] (-0.74, fdr 1e-05), [[ZNF764]] (-0.72, fdr 7e-06), [[PNRC2]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[VPS35L]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FNIP2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8967.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +6.9 | 2e-09 | 34/48 (BT-474, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +6.3 | 1e-07 | 37/48 (BT-474, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +5.5 | 7e-06 | 32/48 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +5.3 | 1e-05 | 32/48 (BT-474, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +5.2 | 3e-05 | 27/49 (NCI-H1573, H4, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +5.0 | 5e-05 | 29/47 (COLO 205, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.014 | 22/48 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.17× | +3.1 | 0.15 | 14/47 (SNU-1, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8967.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.495×** | -19.7 | 0e+00 | 46/48 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.387×** | -17.9 | 0e+00 | 46/49 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.406×** | -17.1 | 0e+00 | 42/44 (SNU-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.500×** | -13.2 | 2e-37 | 48/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.508×** | -12.9 | 7e-36 | 45/47 (RKO, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.550×** | -10.9 | 7e-26 | 39/45 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.597×** | -10.2 | 2e-22 | 45/48 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.726×** | -8.9 | 3e-17 | 34/49 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.633×** | -8.6 | 6e-16 | 44/48 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.659×** | -8.2 | 1e-14 | 42/48 (SW1417, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.713×** | -6.3 | 1e-08 | 43/48 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.742×** | -5.9 | 2e-07 | 34/48 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.767×** | -4.8 | 5e-05 | 33/47 (HS-578T, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **0.791×** | -4.6 | 1e-04 | 32/48 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.820×** | -3.8 | 0.006 | 24/48 (NCI-H1792, NCI-H2030, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.837× | -3.5 | 0.014 | 20/48 (A498, KATO III, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.839× | -3.5 | 0.017 | 19/47 (COLO 205, LS 180, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.840× | -3.4 | 0.017 | 21/48 (LOX-IMVI, AsPC-1, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.844× | -3.3 | 0.022 | 19/49 (SW 900, A498, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.835× | -3.3 | 0.023 | 23/48 (A498, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8967. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 302 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -15.4) |
| [[PANC-1 (line)]] | alt | 393 | 1 (1 ⚠) | 10 (5 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.92× (z +10.0) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -26.7) |
| [[A-172 (line)]] | wt | 283 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -25.3) |
| [[A498 (line)]] | wt | 736 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -26.5) |
| [[HS-578T (line)]] | alt | 521 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -22.9) |
| [[NCI-H2030 (line)]] | alt | 469 | 1 (1 ⚠) | 9 (5 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.05× (z +10.5) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -23.2) |
| [[AsPC-1 (line)]] | alt | 561 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -20.4) |
| [[C32 (line)]] | wt | 759 | 2 | 7 (3 ⚠) | [[Ponatinib (drug)]] 5 µM 2.27× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -30.3) |
| [[J82 (line)]] | alt | 303 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -22.4) |
| [[NCI-H1573 (line)]] | alt | 321 | 1 | 7 (4 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.52× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -18.5) |
| [[NCI-H460 (line)]] | wt | 341 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -18.8) |
| [[SW1417 (line)]] | alt | 516 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -23.2) |
| [[KATO III (line)]] | alt | 406 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.361× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 311 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -23.0) |
| [[SW 900 (line)]] | alt | 409 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -18.5) |
| [[CFPAC-1 (line)]] | alt | 334 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.338× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.517× (z -14.5) |
| [[HT-29 (line)]] | alt | 470 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -15.4) |
| [[Panc 03.27 (line)]] | alt | 314 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -14.2) |
| [[A549 (line)]] | wt | 322 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -16.9) |
| [[H4 (line)]] | wt | 487 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -17.9) |
| [[HOP62 (line)]] | alt | 310 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -15.6) |
| [[LoVo (line)]] | wt | 587 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -18.5) |
| [[LOX-IMVI (line)]] | wt | 352 | 1 (1 ⚠) | 4 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.85× (z +8.6) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -13.0) |
| [[MIA PaCa-2 (line)]] | alt | 377 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.256× (z -15.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.542× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 430 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -24.2) |
| [[NCI-H23 (line)]] | alt | 374 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.600× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 214 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.571× (z -10.3) |
| [[Hs 766T (line)]] | wt | 393 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.570× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 298 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -17.0) |
| [[RKO (line)]] | wt | 614 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.229× (z -21.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -16.6) |
| [[SK-MEL-2 (line)]] | alt | 400 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -12.9) |
| [[SNU-1 (line)]] | wt | 390 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0994× (z -28.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.612× (z -8.8) |
| [[SNU-423 (line)]] | alt | 246 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -17.7) |
| [[A-427 (line)]] | wt | 263 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.628× (z -9.9) |
| [[AN3 CA (line)]] | alt | 339 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -10.2) |
| [[BT-474 (line)]] | alt | 275 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.35× (z +13.2) | — |
| [[COLO 205 (line)]] | alt | 267 | 1 (1 ⚠) | 2 | [[Niclosamide (olamine) (drug)]] 5 µM 2.12× (z +8.9) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -11.7) |
| [[SHP-77 (line)]] | alt | 187 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.12× (z +10.8) | — |
| [[SW48 (line)]] | wt | 725 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -17.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 416 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.346× (z -15.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 318 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.431× (z -8.8) ⚠ toxic |
| [[LS 180 (line)]] | wt | 437 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 331 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -9.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 540 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.289× (z -10.2) |
| [[C-33 A (line)]] | alt | 237 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.529× (z -8.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 274 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.479× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 391 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -8.6) |
| [[CHP-212 (line)]] | wt | 252 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 393 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8967), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM120B]] | +0.77 | +0.78 / +0.57 | both halves | 1e-05 |  |
| [[IER3IP1]] | +0.76 | +0.82 / +0.70 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.75 | +0.78 / +0.61 | both halves | 7e-06 |  |
| [[PDIA5]] | +0.74 | +0.81 / +0.59 | both halves | 7e-06 |  |
| [[HSPA5]] | +0.74 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[SLC31A1]] | +0.74 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[CSNK2A1]] | +0.73 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[EIF4EBP1]] | +0.73 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[SLC37A3]] | +0.73 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[DYM]] | +0.73 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[ZCCHC7]] | +0.72 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[GFPT1]] | +0.72 | +0.74 / +0.64 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED12]] | -0.74 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[ZNF764]] | -0.72 | -0.69 / -0.61 | both halves | 7e-06 |  |
| [[PNRC2]] | -0.69 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[C11orf58]] | -0.68 | -0.70 / -0.43 | both halves | 3e-05 |  |
| [[ZNF776]] | -0.68 | -0.69 / -0.61 | both halves | 7e-06 |  |
| [[DDX6]] | -0.67 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[HNRNPH2]] | -0.67 | -0.68 / -0.57 | both halves | 9e-06 |  |
| [[ZFX]] | -0.67 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[ZC3H4]] | -0.66 | -0.69 / -0.44 | both halves | 3e-05 |  |
| [[SKIL]] | -0.66 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[ZNF253]] | -0.65 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[PATL2]] | -0.65 | -0.73 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VPS35L]] | B | VPS35L activity lowers COG5's level | lines that do not express VPS35L (9) vs lines expressing it (41) | 1.33× higher at baseline in the lines without VPS35L | 0.056 | ⚠ within organs, on part of the lines; also absent: HDGFL3, CHST11, RNF150 |
| [[HDAC6]] | B | HDAC6 activity lowers COG5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FAM111A]] | C | FAM111A activity raises COG5's level | lines that do not express FAM111A (3) vs lines expressing it (47) | 1.81× lower at baseline in the lines without FAM111A | 0.041 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FNIP2]] | C | COG5's natural level weakens FNIP2's drug response | COG5's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.11; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.810). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (2.8, -20.6); signed map (-45.1, 7.5). **Vector** length 151, 62.6% of its response variance represented; |z| ≥ 3 in 1,423 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +9.2 | +6.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +8.9 | +6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.7 | +5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.5 | +5.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.2 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.9 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.5 | +1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.0 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -15.3 | -19.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -12.8 | -13.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.0 | -10.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -10.2 | -8.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.3 | -12.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.6 | -5.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.4 | -4.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -4.9 | -4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.7 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | component of oligomeric golgi complex 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.3 — chr7:107,201,372-107,564,261 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GTC90; previously GOLTC1 |
| Gene groups (HGNC) | Components of oligomeric golgi complex |
| Reactome | 9 pathways, smallest: Intra-Golgi traffic; Retrograde transport at the Trans-Golgi-Network; COPI-mediated anterograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UP83](https://www.uniprot.org/uniprotkb/Q9UP83) (Conserved oligomeric Golgi complex subunit 5):

> Required for normal Golgi function.

**Summary**, from NCBI Gene [10466](https://www.ncbi.nlm.nih.gov/gene/10466):

> The protein encoded by this gene is one of eight proteins (Cog1-8) which form a Golgi-localized complex (COG) required for normal Golgi morphology and function. The encoded protein is organized with conserved oligomeric Golgi complex components 6, 7 and 8 into a sub-complex referred to as lobe B. Alternative splicing results in multiple transcript variants. Mutations in this gene result in congenital disorder of glycosylation type 2I.[provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:14857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14857) · Entrez [10466](https://www.ncbi.nlm.nih.gov/gene/10466) · UniProt [Q9UP83](https://www.uniprot.org/uniprotkb/Q9UP83) · Ensembl [ENSG00000164597](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164597)

## Data

Gene col 8967: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8967); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8967, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8967]; `tensor/DDL_lfc|DDL_z.npy` [8967]; `embed/gene_vectors.npy` [8967]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8967 or target_col == 8967). Every well: [[COG5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COG5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

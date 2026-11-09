---
symbol: "HMGA1"
type: "gene"
col: 5999
ensembl_id: "ENSG00000137309"
name: "high mobility group AT-hook 1"
location: "6p21.31"
module: 206
arm: "+"
pooled_cpm: 303.3
n_lines_expressing: 46
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/206"]
generated_by: "tahoemap"
---

# HMGA1

*high mobility group AT-hook 1* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.75× (z +12.0, q 1e-30, up in 44 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.68× (z +4.7, q 2e-04, up in 38 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H1792 7.46×, HT-29 4.86×, NCI-H460 5.80×, LOX-IMVI 5.44×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (LOX-IMVI 5.38×, HT-29 4.54×, NCI-H1792 6.24×, HOP62 5.66×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 2.90×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (KATO III 3.24×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SNU-1 3.25×).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.470× (z -6.3, q 1e-07, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX1A]] (+0.66, fdr 7e-06), [[DRAP1]] (+0.66, fdr 7e-06), [[CSGALNACT2]] (+0.64, fdr 1e-05); moves opposite to [[RFX7]] (-0.55, fdr 1e-05), [[ZNF148]] (-0.55, fdr 3e-05), [[GTF2I]] (-0.54, fdr 4e-05).
> It is in [[Module 206]], a single-armed module (Constitutive Signaling by Aberrant PI3K in Cancer).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[EPHB1]] → it (grade B ⚠); 3 go from it, the strongest it → [[FOSL1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5999.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H1792 7.46×, HT-29 4.86×, NCI-H460 5.80×, LOX-IMVI 5.44×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (LOX-IMVI 5.38×, HT-29 4.54×, NCI-H1792 6.24×, HOP62 5.66×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 2.90×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (KATO III 3.24×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SNU-1 3.25×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.75×** | +12.0 | 1e-30 | 44/45 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.16×** | +10.1 | 2e-21 | 40/41 (LOX-IMVI, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +7.7 | 3e-12 | 41/42 (RPMI-7951, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.93×** | +5.8 | 1e-06 | 33/44 (PANC-1, HOP62, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.80×** | +5.3 | 1e-05 | 32/44 (PANC-1, HOP62, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.71×** | +4.9 | 1e-04 | 36/44 (SNU-1, SW48, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +4.7 | 2e-04 | 38/44 (KATO III, AN3 CA, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~65% of this change | **1.60×** | +4.3 | 0.001 | 37/44 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.61×** | +4.2 | 0.002 | 32/43 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.54×** | +4.0 | 0.004 | 30/44 (NCI-H460, KATO III, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.043 | 31/43 (HT-29, KATO III, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +3.1 | 0.086 | 22/44 (AsPC-1, Hs 766T, …) | two highest doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5999.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.470×** | -6.3 | 1e-07 | 42/46 (SK-MEL-2, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.637×** | -5.8 | 2e-06 | 41/44 (C32, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.539×** | -5.4 | 1e-05 | 39/43 (HS-578T, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.627×** | -4.9 | 1e-04 | 39/44 (SK-MEL-2, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.567×** | -4.9 | 1e-04 | 38/44 (HepG2/C3A, SK-MEL-2, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.572×** | -4.9 | 1e-04 | 39/45 (SK-MEL-2, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.709×** | -4.3 | 0.001 | 34/45 (HepG2/C3A, SW48, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.719×** | -4.2 | 0.002 | 36/44 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.610×** | -4.2 | 0.002 | 36/44 (SK-MEL-2, HepG2/C3A, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.642×** | -4.0 | 0.003 | 39/44 (SK-MEL-2, KATO III, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.695×** | -3.8 | 0.008 | 33/44 (HepG2/C3A, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.426×** | -3.7 | 0.010 | 40/44 (SK-MEL-2, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.676×** | -3.6 | 0.016 | 31/43 (HepG2/C3A, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.679×** | -3.4 | 0.028 | 30/44 (HS-578T, HepG2/C3A, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.708×** | -3.1 | 0.064 | 31/44 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Encorafenib (drug)]] 5 µM |  | **0.490×** | -3.1 | 0.069 | 31/44 (SK-MEL-2, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.716×** | -3.0 | 0.077 | 27/44 (NCI-H1573, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.70 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5999. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 252 | 0 | 8 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.213× (z -12.4) |
| [[HepG2_C3A (line)]] | wt | 469 | 0 | 7 | — | [[Trametinib (drug)]] 5 µM 0.231× (z -10.1) |
| [[PANC-1 (line)]] | alt | 315 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.89× (z +11.9) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[HOP62 (line)]] | alt | 245 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +12.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 717 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +13.4) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.380× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 325 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.24× (z +9.7) | [[Selinexor (drug)]] 5 µM 0.473× (z -8.6) ⚠ cell-cycle shift, explains ~66% of this change |
| [[NCI-H460 (line)]] | wt | 120 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +13.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 180 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.51× (z +11.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 263 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +11.7) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 231 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +10.3) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 171 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +10.7) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.362× (z -9.7) ⚠ cell-cycle shift, explains ~66% of this change |
| [[Hs 766T (line)]] | wt | 182 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +11.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HT-29 (line)]] | alt | 280 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +14.0) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 164 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.21× (z +12.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 429 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.44× (z +13.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 300 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +10.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 579 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +8.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.313× (z -10.0) ⚠ cell-cycle shift, explains ~58% of this change |
| [[SNU-1 (line)]] | wt | 259 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 4.32× (z +10.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 3.25× (z +8.8) | — |
| [[SW480 (line)]] | alt | 372 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +12.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 366 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +13.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 321 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +10.1) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 216 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 197 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.40× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 336 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +11.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 496 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 191 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.83× (z +8.8) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[NCI-H1792 (line)]] | alt | 329 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.46× (z +14.2) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 297 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 418 | 1 (1 ⚠) | 1 | [[Harringtonine (drug)]] 0.5 µM 3.18× (z +9.6) ⚠ cell-cycle shift, explains ~26% of this change | [[Trametinib (drug)]] 5 µM 0.325× (z -8.8) |
| [[A498 (line)]] | wt | 171 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 219 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.243× (z -11.2) |
| [[LoVo (line)]] | wt | 214 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 192 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +9.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 775 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 59.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 331 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 74.8 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 599 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 142 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 66.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 304 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 362 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 630 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 69.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 149 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5999), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX1A]] | +0.66 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[DRAP1]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[CSGALNACT2]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[PHLDA1]] | +0.64 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[AGO2]] | +0.64 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[N4BP3]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[WNT7B]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[SLC45A3]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[CALB2]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[EHD1]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFX7]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ZNF148]] | -0.55 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[GTF2I]] | -0.54 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[MFSD14A]] | -0.53 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[LUC7L2]] | -0.53 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[WBP11]] | -0.52 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[STOM]] | -0.51 | -0.58 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHB1]] | B | EPHB1 activity lowers HMGA1's level | lines that do not express EPHB1 (16) vs lines expressing it (34) | 2.01× higher at baseline in the lines without EPHB1 | 0.005 | ⚠ within organs, on part of the lines; also absent: KCNG1, DOCK2, GLIS1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises HMGA1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CNIH3]] | B | CNIH3 activity lowers HMGA1's level | lines that do not express CNIH3 (12) vs lines expressing it (38) | 1.56× higher at baseline in the lines without CNIH3 | 0.085 | ⚠ within organs, on part of the lines; also absent: HDGFL3, RIMKLB, ZNF793; maybe low, not absent |
| [[UPP1]] | B | UPP1 activity raises HMGA1's level | lines that do not express UPP1 (9) vs lines expressing it (41) | 1.44× lower at baseline in the lines without UPP1 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, PPP1R18, EBI3; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FOSL1]] | C | HMGA1 activity raises FOSL1's level | lines that do not express HMGA1 (4) vs lines expressing it (46) | 2.96× lower at baseline in the lines without HMGA1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: POLR3G, CMTM7, BOK; maybe low, not absent; its own permutation p |
| [[MAMLD1]] | C | HMGA1 activity raises MAMLD1's level | lines that do not express HMGA1 (4) vs lines expressing it (46) | 3.27× lower at baseline in the lines without HMGA1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: POLR3G, CMTM7, BOK; maybe low, not absent; its own permutation p |
| [[ARID3B]] | C | HMGA1 activity raises ARID3B's level | lines that do not express HMGA1 (4) vs lines expressing it (46) | 1.94× lower at baseline in the lines without HMGA1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: POLR3G, CMTM7, BOK; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 206]] — Constitutive Signaling by Aberrant PI3K in Cancer; 15 genes; every member is in the + arm (projection on the module's main direction 0.755). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.7, -0.7); signed map (2.2, 45.9). **Vector** length 107, 42.2% of its response variance represented; |z| ≥ 3 in 1,446 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.3 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.3 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +1.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.5 | -0.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +1.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.2 | +0.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +3.2 | +0.5 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +4.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -7.1 | -5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.9 | -3.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.4 | -4.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.2 | -6.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.0 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.8 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.8 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | high mobility group AT-hook 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:34,236,873-34,246,231 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HMGIY |
| Gene groups (HGNC) | Canonical high mobility group; MicroRNA protein coding host genes |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 17 pathways, smallest: Autointegration results in viral DNA circles; Integration of viral DNA into host genomic DNA; APOBEC3G mediated resistance to HIV-1 infection |
| Matched by | ensembl_id |

**Function**, from UniProt [P17096](https://www.uniprot.org/uniprotkb/P17096) (High mobility group protein HMG-I/HMG-Y):

> HMG-I/Y bind preferentially to the minor groove of A+T rich regions in double-stranded DNA. It is suggested that these proteins could function in nucleosome phasing and in the 3'-end processing of mRNA transcripts. They are also involved in the transcription regulation of genes containing, or in close proximity to A+T-rich regions.

**Summary**, from NCBI Gene [3159](https://www.ncbi.nlm.nih.gov/gene/3159):

> This gene encodes a chromatin-associated protein involved in the regulation of gene transcription, integration of retroviruses into chromosomes, and the metastatic progression of cancer cells. The encoded protein preferentially binds to the minor groove of AT-rich regions in double-stranded DNA. Multiple transcript variants encoding different isoforms have been found for this gene. Pseudogenes of this gene have been identified on multiple chromosomes. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:5010](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5010) · Entrez [3159](https://www.ncbi.nlm.nih.gov/gene/3159) · UniProt [P17096](https://www.uniprot.org/uniprotkb/P17096) · Ensembl [ENSG00000137309](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137309)

## Data

Gene col 5999: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5999); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5999, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5999]; `tensor/DDL_lfc|DDL_z.npy` [5999]; `embed/gene_vectors.npy` [5999]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5999 or target_col == 5999). Every well: [[HMGA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

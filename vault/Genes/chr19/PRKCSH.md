---
symbol: "PRKCSH"
type: "gene"
col: 5029
ensembl_id: "ENSG00000130175"
name: "PRKCSH beta subunit of glucosidase II"
location: "19p13.2"
module: 50
arm: "+"
pooled_cpm: 73.6
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# PRKCSH

*PRKCSH beta subunit of glucosidase II* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.05× (z +16.2, q 0e+00, up in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Peretinoin (drug)]] 0.05 µM: 1.28× (z +3.3, q 0.059, up in 26 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (LoVo 4.93×, PANC-1 3.44×, A549 4.68×, SW480 3.31×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (A549 5.28×, LoVo 4.34×, PANC-1 3.27×, C32 4.17×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.430× (z -17.3, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMB2]] (+0.74, fdr 7e-06), [[SELENON]] (+0.70, fdr 7e-06), [[ABCA2]] (+0.70, fdr 7e-06); moves opposite to [[RPP25L]] (-0.63, fdr 1e-05), [[PIGBOS1]] (-0.59, fdr 1e-05), [[MED18]] (-0.59, fdr 3e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5029.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (LoVo 4.93×, PANC-1 3.44×, A549 4.68×, SW480 3.31×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (A549 5.28×, LoVo 4.34×, PANC-1 3.27×, C32 4.17×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.05×** | +16.2 | 0e+00 | 46/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.86×** | +14.7 | 0e+00 | 43/43 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.46×** | +12.1 | 3e-31 | 42/44 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +6.9 | 7e-10 | 0/48 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.47×** | +5.6 | 3e-06 | 39/47 (SW480, BT-474, …) | two highest doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +5.4 | 8e-06 | 37/47 (SW1417, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.41×** | +5.0 | 6e-05 | 34/47 (SW480, HEC-1-A, …) | two highest doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.23×** | +4.3 | 0.001 | 24/47 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.4 | 0.044 | 21/37 (NCI-H2347, C32, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.28×** | +3.3 | 0.059 | 26/47 (hTERT-HPNE, HT-29, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.092 | 25/46 (SW48, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.34× | +3.1 | 0.10 | 21/47 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5029.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.430×** | -17.3 | 0e+00 | 46/47 (H4, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.472×** | -10.9 | 5e-25 | 44/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.711×** | -4.7 | 3e-04 | 32/47 (SNU-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.712×** | -4.7 | 3e-04 | 33/48 (SNU-423, SW 1088, …) | top dose only | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.830×** | -3.8 | 0.017 | 26/47 (PANC-1, HOP62, …) | top dose only | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.839× | -3.6 | 0.032 | 18/47 (CHP-212, PANC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5029. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 80.1 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +13.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -18.3) |
| [[HS-578T (line)]] | alt | 132 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -12.2) |
| [[LoVo (line)]] | wt | 69.9 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +15.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -14.5) |
| [[MIA PaCa-2 (line)]] | alt | 80.7 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +14.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -20.6) |
| [[NCI-H1573 (line)]] | alt | 32.6 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +13.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 92.4 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -16.4) |
| [[NCI-H460 (line)]] | wt | 65.6 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -16.6) |
| [[PANC-1 (line)]] | alt | 77.2 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +15.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -11.9) |
| [[SW480 (line)]] | alt | 63.3 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +14.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -15.7) |
| [[A498 (line)]] | wt | 104 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.483× (z -8.5) |
| [[A549 (line)]] | wt | 55.9 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.28× (z +15.3) ⚠ toxic; transcription drop | [[AZD2858 (drug)]] 0.5 µM 0.283× (z -8.6) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 45.2 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.90× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -19.6) |
| [[CFPAC-1 (line)]] | alt | 56.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -11.1) |
| [[HT-29 (line)]] | alt | 52.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -17.8) |
| [[SK-MEL-2 (line)]] | alt | 118 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.81× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -10.4) |
| [[SNU-423 (line)]] | alt | 113 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +12.7) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.305× (z -11.3) |
| [[C-33 A (line)]] | alt | 82.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -9.5) |
| [[C32 (line)]] | wt | 92.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.17× (z +13.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 105 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -23.8) |
| [[HEC-1-A (line)]] | alt | 56.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +13.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 64.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -9.9) |
| [[J82 (line)]] | alt | 91.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -11.0) |
| [[KATO III (line)]] | alt | 53.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 57.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -14.3) |
| [[LS 180 (line)]] | wt | 55.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 65.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.86× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 62.5 | 2 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +9.9) ⚠ cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 65.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 3.14× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.265× (z -12.4) |
| [[RKO (line)]] | wt | 101 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -9.3) |
| [[SW 900 (line)]] | alt | 64.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -11.6) |
| [[A-172 (line)]] | wt | 112 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +11.5) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 84.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -12.1) |
| [[hTERT-HPNE (line)]] | wt | 105 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 51.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +11.9) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 115 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -15.1) |
| [[SW 1088 (line)]] | alt | 90.0 | 0 | 2 | — | [[Tadalafil (drug)]] 5 µM 0.104× (z -8.8) |
| [[SW1417 (line)]] | alt | 64.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +12.5) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 103 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -12.4) |
| [[AN3 CA (line)]] | alt | 113 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -14.4) |
| [[BT-474 (line)]] | alt | 76.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -9.2) |
| [[COLO 205 (line)]] | alt | 50.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 59.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -10.9) |
| [[SNU-1 (line)]] | wt | 84.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -16.2) |
| [[A-427 (line)]] | wt | 3.82 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 62.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5029), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMB2]] | +0.74 | +0.77 / +0.70 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation |
| [[SELENON]] | +0.70 | +0.71 / +0.59 | both halves | 7e-06 | same gene group |
| [[ABCA2]] | +0.70 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[GANAB]] | +0.69 | +0.67 / +0.68 | both halves | 7e-06 | pathway: Adherens junctions interactions; STRING 999 |
| [[SNRNP200]] | +0.69 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[SBF1]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[FKBP9]] | +0.67 | +0.69 / +0.66 | both halves | 7e-06 | same gene group |
| [[CRTAP]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[MAN2B2]] | +0.67 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[INTS1]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[CTSZ]] | +0.65 | +0.73 / +0.58 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[BSG]] | +0.65 | +0.63 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP25L]] | -0.63 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[PIGBOS1]] | -0.59 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[MED18]] | -0.59 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[TIPRL]] | -0.58 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[C1orf131]] | -0.58 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[MMADHC]] | -0.58 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[PBDC1]] | -0.58 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.58 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[C14orf119]] | -0.58 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[TMEM265]] | -0.57 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[FDX2]] | -0.57 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[MRPS18C]] | -0.56 | -0.49 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.790). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.8, -22.9); signed map (-26.3, -38.0). **Vector** length 113, 32.6% of its response variance represented; |z| ≥ 3 in 810 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Extracellular matrix organization* (reactome, mean cos +0.55 to 12); *Degradation of the extracellular matrix* (reactome, mean cos +0.56 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +5.0 | +6.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.0 | +5.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +3.6 | +5.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +2.6 | +1.3 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +2.3 | +1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.3 | +0.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.5 | -10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -10.1 | -17.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.4 | -4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.1 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.3 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.0 | -4.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | PRKCSH beta subunit of glucosidase II |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:11,435,284-11,450,968 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VASAP-60, GIIB, PKCSH, 80K-H, AGE-R2, GIIbeta, GluIIbeta; previously G19P1, PCLD, PLD1 |
| Gene groups (HGNC) | EF-hand domain containing; MRH domain containing |
| Reactome | 24 pathways, smallest: Maturation of spike protein_9683686; Advanced glycosylation endproduct receptor signaling; Calnexin/calreticulin cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P14314](https://www.uniprot.org/uniprotkb/P14314) (Glucosidase 2 subunit beta):

> Regulatory subunit of glucosidase II that cleaves sequentially the 2 innermost alpha-1,3-linked glucose residues from the Glc(2)Man(9)GlcNAc(2) oligosaccharide precursor of immature glycoproteins. Required for efficient PKD1/Polycystin-1 biogenesis and trafficking to the plasma membrane of the primary cilia (By similarity).

**Summary**, from NCBI Gene [5589](https://www.ncbi.nlm.nih.gov/gene/5589):

> This gene encodes the beta-subunit of glucosidase II, an N-linked glycan-processing enzyme in the endoplasmic reticulum. The encoded protein is an acidic phosphoprotein known to be a substrate for protein kinase C. Mutations in this gene have been associated with the autosomal dominant polycystic liver disease. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2014]

**Accessions** — [HGNC:9411](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9411) · Entrez [5589](https://www.ncbi.nlm.nih.gov/gene/5589) · UniProt [P14314](https://www.uniprot.org/uniprotkb/P14314) · Ensembl [ENSG00000130175](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130175)

## Data

Gene col 5029: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5029); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5029, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5029]; `tensor/DDL_lfc|DDL_z.npy` [5029]; `embed/gene_vectors.npy` [5029]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5029 or target_col == 5029). Every well: [[PRKCSH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKCSH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

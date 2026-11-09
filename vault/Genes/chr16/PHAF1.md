---
symbol: "PHAF1"
type: "gene"
col: 4591
ensembl_id: "ENSG00000125149"
name: "phagophore assembly factor 1"
location: "16q22.1"
module: 30
arm: "+"
pooled_cpm: 29.09
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 4
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# PHAF1

*phagophore assembly factor 1* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.23× (z +20.1, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.340× (z -18.6, q 0e+00, down in 37 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 0.05 µM: 0.786× (z -4.2, q 0.004, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SW480 0.228×, A498 0.115×, RPMI-7951 0.0550×, SW48 0.0883×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (A-172 0.121×, Hs 766T 0.124×, SW1417 0.229×, KATO III 0.180×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.161×, CFPAC-1 0.142×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIAA2013]] (+0.79, fdr 7e-06), [[SUFU]] (+0.76, fdr 7e-06), [[MRPL34]] (+0.75, fdr 1e-05); moves opposite to [[ZNF655]] (-0.76, fdr 7e-06), [[ERCC6L2]] (-0.67, fdr 1e-05), [[CPSF2]] (-0.65, fdr 2e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PI4KAP1-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4591.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.23×** | +20.1 | 0e+00 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.98×** | +18.7 | 0e+00 | 47/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.74×** | +17.3 | 0e+00 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +11.5 | 1e-28 | 35/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.90×** | +11.0 | 4e-26 | 37/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.07×** | +10.1 | 8e-22 | 41/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **3.06×** | +10.0 | 8e-22 | 43/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +7.4 | 7e-12 | 34/47 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.48×** | +6.4 | 9e-09 | 27/45 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +6.3 | 2e-08 | 31/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.30×** | +6.2 | 3e-08 | 25/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +6.1 | 4e-08 | 25/47 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +5.9 | 1e-07 | 26/48 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +5.7 | 5e-07 | 28/48 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.33×** | +4.9 | 3e-05 | 22/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +4.8 | 6e-05 | 22/47 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.6 | 1e-04 | 20/48 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.61×** | +4.2 | 7e-04 | 14/48 (NCI-H460, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.57×** | +4.0 | 0.002 | 17/47 (A498, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +3.7 | 0.006 | 14/48 (CFPAC-1, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.025 | 11/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4591.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SW480 0.228×, A498 0.115×, RPMI-7951 0.0550×, SW48 0.0883×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (A-172 0.121×, Hs 766T 0.124×, SW1417 0.229×, KATO III 0.180×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.161×, CFPAC-1 0.142×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.340×** | -18.6 | 0e+00 | 37/42 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.453×** | -12.6 | 5e-34 | 28/40 (NCI-H2030, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.509×** | -11.2 | 8e-27 | 28/37 (A-172, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.786×** | -4.2 | 0.004 | 19/48 (SNU-423, AsPC-1, …) | inconsistent across doses |  |
| [[Rimonabant (drug)]] 5 µM |  | 0.875× | -3.1 | 0.17 | 2/48 (SW1417, HS-578T) | top dose only |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | 0.835× | -3.1 | 0.17 | 6/48 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.828× | -3.0 | 0.18 | 16/47 (BT-474, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Flutamide (drug)]] 5 µM |  | 0.840× | -3.0 | 0.18 | 10/48 (LOX-IMVI, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4591. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 47.2 | 8 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.92× (z +17.6) | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -19.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 39.1 | 5 (1 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.50× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 30.5 | 6 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.51× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -9.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 23.8 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.41× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -12.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 22.3 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.32× (z +9.4) | [[AZD2858 (drug)]] 0.5 µM 0.0756× (z -11.8) ⚠ toxic |
| [[KATO III (line)]] | alt | 22.5 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.13× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.180× (z -12.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 21.3 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.81× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 70.9 | 3 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 3.00× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 24.3 | 1 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.08× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -10.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 24.8 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.09× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -14.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 32.3 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.55× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.221× (z -10.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 23.8 | 2 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 3.72× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.233× (z -9.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 21.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.90× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -9.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 19.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.70× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 23.7 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.73× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.124× (z -13.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 24.4 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.72× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.241× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 27.8 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.41× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -11.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 30.9 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.52× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -11.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 25.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -16.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 37.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -17.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 21.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.66× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -11.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 26.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.92× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -9.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 65.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -10.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 25.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.51× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 18.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.44× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 25.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.29× (z +9.8) | — |
| [[RKO (line)]] | wt | 23.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.90× (z +9.9) | — |
| [[SW48 (line)]] | wt | 39.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0883× (z -13.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 28.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -13.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -8.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -10.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 41.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -9.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Torkinib (drug)]] 5 µM 0.0472× (z -9.7) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -9.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0550× (z -16.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -11.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4591), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA2013]] | +0.79 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[SUFU]] | +0.76 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[MRPL34]] | +0.75 | +0.56 / +0.76 | both halves | 1e-05 |  |
| [[MALSU1]] | +0.72 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[CARHSP1]] | +0.70 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[BAG4]] | +0.70 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[SLC9A6]] | +0.70 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[MED26]] | +0.69 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[SDHAP2]] | +0.69 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ALG9]] | +0.69 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[SCAI]] | +0.68 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[RAB40C]] | +0.68 | +0.66 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF655]] | -0.76 | -0.59 / -0.70 | both halves | 7e-06 |  |
| [[ERCC6L2]] | -0.67 | -0.72 / -0.49 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.65 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[PSMD6-AS1]] | -0.65 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[C11orf58]] | -0.65 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[AKT1S1]] | -0.64 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[MIS12]] | -0.64 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[FKRP]] | -0.63 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[MSRA]] | -0.62 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[ELK4]] | -0.62 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[PSME3IP1]] | -0.62 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[DCAF8]] | -0.62 | -0.43 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PI4KAP1-1]] | B | PI4KAP1-1 activity raises PHAF1's level | lines that do not express PI4KAP1-1 (26) vs lines expressing it (24) | 1.18× lower at baseline in the lines without PI4KAP1-1 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PI4KAP1, ENSG00000260573, LCK |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.739). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (0.9, -12.1); signed map (-33.5, -0.6). **Vector** length 82.5, 19.2% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.5 | +18.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +20.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | +17.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +2.7 | +6.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +10.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.7 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.2 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.6 | +0.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.7 | -18.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.5 | -11.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | +1.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.9 | -12.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | phagophore assembly factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,109,941-67,148,544 (+) |
| Ensembl biotype | protein_coding |
| Also known as | lin-10, FLJ12076, MYTHO; previously C16orf6, LIN10, C16orf70 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSU1](https://www.uniprot.org/uniprotkb/Q9BSU1) (Phagosome assembly factor 1):

> Plays a regulatory role in autophagic activity. In complex with BCAS3, associates with the autophagosome formation site during both non-selective and selective autophagy.

**Summary**, from NCBI Gene [80262](https://www.ncbi.nlm.nih.gov/gene/80262):

> Predicted to be involved in Golgi to plasma membrane protein transport. Located in phagophore assembly site. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29564](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29564) · Entrez [80262](https://www.ncbi.nlm.nih.gov/gene/80262) · UniProt [Q9BSU1](https://www.uniprot.org/uniprotkb/Q9BSU1) · Ensembl [ENSG00000125149](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125149)

## Data

Gene col 4591: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4591); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4591, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4591]; `tensor/DDL_lfc|DDL_z.npy` [4591]; `embed/gene_vectors.npy` [4591]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4591 or target_col == 4591). Every well: [[PHAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

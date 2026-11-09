---
symbol: "VMA21"
type: "gene"
col: 8303
ensembl_id: "ENSG00000160131"
name: "vacuolar ATPase assembly factor VMA21"
location: "Xq28"
module: 20
arm: "+"
pooled_cpm: 36.09
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# VMA21

*vacuolar ATPase assembly factor VMA21* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (21 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.58× (z +28.9, q 0e+00, up in 45 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.51× (z +6.9, q 3e-10, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.831× (z -4.4, q 0.005, down in 22 of 48 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 5 µM: 0.617× (z -4.3, q 0.005, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.301×, NCI-H2030 0.504×; ⚠ cell-cycle shift, would explain all of this change); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (AN3 CA 0.107×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIGMAR1]] (+0.75, fdr 7e-06), [[WDR77]] (+0.73, fdr 7e-06), [[TMEM33]] (+0.72, fdr 7e-06); moves opposite to [[NKAP]] (-0.76, fdr 7e-06), [[ING2]] (-0.74, fdr 7e-06), [[PMM1]] (-0.74, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 25 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8303.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.58×** | +28.9 | 0e+00 | 45/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.27×** | +26.9 | 0e+00 | 40/40 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.41×** | +23.1 | 0e+00 | 41/41 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.88×** | +10.6 | 3e-24 | 37/46 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +9.8 | 1e-20 | 36/47 (NCI-H2030, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.64×** | +8.3 | 7e-15 | 33/47 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.61×** | +7.7 | 2e-12 | 29/47 (NCI-H1792, C32, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.57×** | +7.6 | 2e-12 | 32/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +6.9 | 3e-10 | 32/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +6.6 | 2e-09 | 33/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.48×** | +6.5 | 4e-09 | 35/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.42×** | +5.8 | 2e-07 | 30/48 (H4, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.40×** | +5.6 | 7e-07 | 29/48 (A-172, SNU-423, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.6 | 7e-07 | 2/48 (SNU-1, HCT15) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.38×** | +5.4 | 2e-06 | 26/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +5.2 | 6e-06 | 24/48 (SNU-423, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +4.8 | 6e-05 | 26/48 (PANC-1, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.62×** | +4.2 | 6e-04 | 22/48 (SW1417, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.58×** | +4.0 | 0.001 | 19/47 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.0 | 0.002 | 19/48 (A-172, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.004 | 17/48 (SW 900, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.51×** | +3.6 | 0.006 | 9/48 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.006 | 15/48 (PANC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.027 | 5/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.20×** | +3.1 | 0.035 | 10/48 (PANC-1, A549, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.041 | 12/47 (SW1417, C32, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.41×** | +3.0 | 0.043 | 13/48 (NCI-H460, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 0.05 µM |  | 1.19× | +2.9 | 0.054 | 3/48 (MIA PaCa-2, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8303.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.301×, NCI-H2030 0.504×; ⚠ cell-cycle shift, would explain all of this change); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (AN3 CA 0.107×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.831×** | -4.4 | 0.005 | 22/48 (LS 180, SNU-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.617×** | -4.3 | 0.005 | 23/48 (RPMI-7951, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.818× | -3.4 | 0.13 | 18/47 (LoVo, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~72% of this change | 0.821× | -3.2 | 0.21 | 17/48 (SK-MEL-2, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | 0.827× | -3.1 | 0.21 | 13/48 (MIA PaCa-2, HOP62, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8303. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 76.3 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +21.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 32.5 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.01× (z +16.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 48.7 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +12.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -14.6) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 49.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.37× (z +17.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 13.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 16.8× (z +15.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 44.6 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 40.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.42× (z +16.8) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 22.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.93× (z +14.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 26.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.0× (z +15.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 28.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.79× (z +13.7) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 25.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.04× (z +12.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 21.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.95× (z +12.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 23.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.58× (z +12.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 27.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.86× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 25.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.92× (z +16.1) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 42.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.58× (z +17.2) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 14.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.26× (z +12.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 37.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +14.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 39.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +13.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 34.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.22× (z +15.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 28.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +12.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 23.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.93× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 42.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +14.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 25.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.17× (z +14.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 24.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.30× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 75.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +14.3) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 43.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 41.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.55× (z +21.9) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 32.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.88× (z +10.6) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 28.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.15× (z +9.1) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 21.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.69× (z +10.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 36.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +12.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 20.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.13× (z +13.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 21.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.40× (z +13.4) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 70.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +13.2) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 41.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 34.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.03× (z +12.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 28.3 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.107× (z -9.0) |
| [[C-33 A (line)]] | alt | 67.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 30.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +9.1) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8303), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIGMAR1]] | +0.75 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[WDR77]] | +0.73 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[TMEM33]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[EIF5A]] | +0.71 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[PSME3]] | +0.70 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[ICMT]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[MMGT1]] | +0.69 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[ALG10]] | +0.69 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[C1QBP]] | +0.69 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[MTHFD1]] | +0.68 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[TFDP1]] | +0.68 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[ALG10B]] | +0.68 | +0.54 / +0.74 | both halves | 1e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKAP]] | -0.76 | -0.62 / -0.77 | both halves | 7e-06 |  |
| [[ING2]] | -0.74 | -0.65 / -0.73 | both halves | 7e-06 |  |
| [[PMM1]] | -0.74 | -0.72 / -0.78 | both halves | 7e-06 |  |
| [[SNHG32]] | -0.74 | -0.65 / -0.70 | both halves | 7e-06 |  |
| [[SELENOK]] | -0.73 | -0.62 / -0.73 | both halves | 7e-06 |  |
| [[MTIF3]] | -0.73 | -0.65 / -0.73 | both halves | 7e-06 |  |
| [[ZMYM5]] | -0.72 | -0.60 / -0.78 | both halves | 7e-06 |  |
| [[SUGP1]] | -0.71 | -0.70 / -0.65 | both halves | 7e-06 |  |
| [[SNHG6]] | -0.70 | -0.65 / -0.70 | both halves | 7e-06 |  |
| [[ZFAND2B]] | -0.69 | -0.54 / -0.71 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.69 | -0.50 / -0.77 | both halves | 1e-05 |  |
| [[RNF181]] | -0.69 | -0.55 / -0.72 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.5, -29.2); signed map (-15.9, -40.0). **Vector** length 94.6, 24.9% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.4 | +6.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +23.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +4.4 | +7.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.7 | +5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +4.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +1.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.3 | +3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.2 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +6.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~72% of this change | -4.7 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.6 | +0.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -3.2 | -4.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.1 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -0.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.3 | +0.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.1 | -2.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | vacuolar ATPase assembly factor VMA21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:151,396,515-151,409,364 (+) |
| Ensembl biotype | protein_coding |
| Also known as | XMEA; previously MEAX |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3ZAQ7](https://www.uniprot.org/uniprotkb/Q3ZAQ7) (Vacuolar ATPase assembly integral membrane protein VMA21):

> Required for the assembly of the V0 complex of the vacuolar ATPase (V-ATPase) in the endoplasmic reticulum.

**Summary**, from NCBI Gene [203547](https://www.ncbi.nlm.nih.gov/gene/203547):

> This gene encodes a chaperone for assembly of lysosomal vacuolar ATPase.[provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:22082](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22082) · Entrez [203547](https://www.ncbi.nlm.nih.gov/gene/203547) · UniProt [Q3ZAQ7](https://www.uniprot.org/uniprotkb/Q3ZAQ7) · Ensembl [ENSG00000160131](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160131)

## Data

Gene col 8303: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8303); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8303, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8303]; `tensor/DDL_lfc|DDL_z.npy` [8303]; `embed/gene_vectors.npy` [8303]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8303 or target_col == 8303). Every well: [[VMA21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VMA21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

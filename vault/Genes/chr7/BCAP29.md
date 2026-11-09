---
symbol: "BCAP29"
type: "gene"
col: 1132
ensembl_id: "ENSG00000075790"
name: "B cell receptor associated protein 29"
location: "7q22.3"
module: 118
arm: "-"
pooled_cpm: 83.56
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# BCAP29

*B cell receptor associated protein 29* — 7q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.33× (z +20.8, q 0e+00, up in 46 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (RKO 3.50×, LoVo 2.60×, SW480 2.38×, NCI-H460 2.62×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 2.72×, PANC-1 2.34×, HT-29 2.99×, KATO III 3.25×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.553× (z -20.6, q 0e+00, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTR2]] (+0.63, fdr 7e-06), [[REEP3]] (+0.62, fdr 7e-06), [[SLC25A24]] (+0.58, fdr 6e-05); moves opposite to [[GPRC5C]] (-0.58, fdr 4e-05), [[CCDC115]] (-0.57, fdr 1e-05), [[NGDN]] (-0.57, fdr 2e-05).
> It sits in the **-** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GPRC5C]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[AT7519 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1132.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (RKO 3.50×, LoVo 2.60×, SW480 2.38×, NCI-H460 2.62×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 2.72×, PANC-1 2.34×, HT-29 2.99×, KATO III 3.25×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.33×** | +20.8 | 0e+00 | 46/49 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +20.0 | 0e+00 | 41/41 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +13.5 | 2e-39 | 35/43 (LS 180, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.18× | +3.8 | 0.021 | 18/47 (LoVo, C32, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.16× | +3.7 | 0.027 | 18/48 (LoVo, SW480, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.14× | +3.2 | 0.14 | 11/47 (LoVo, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1132.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.553×** | -20.6 | 0e+00 | 40/49 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.673×** | -13.8 | 8e-41 | 30/47 (LOX-IMVI, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.615×** | -12.0 | 1e-30 | 37/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.644×** | -10.8 | 3e-25 | 35/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.652×** | -10.0 | 3e-21 | 42/48 (A-172, C32, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.468×** | -9.8 | 2e-20 | 40/49 (RKO, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.471×** | -9.7 | 3e-20 | 37/47 (RKO, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.689×** | -9.2 | 3e-18 | 36/48 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.762×** | -6.7 | 1e-09 | 29/48 (C32, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.825×** | -6.7 | 1e-09 | 21/48 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **0.763×** | -6.4 | 9e-09 | 28/49 (NCI-H2030, C32, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.770×** | -6.2 | 3e-08 | 27/48 (C32, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.619×** | -6.2 | 3e-08 | 29/44 (RPMI-7951, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.808×** | -5.2 | 6e-06 | 25/48 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -4.8 | 7e-05 | 5/49 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.880× | -4.4 | 3e-04 | 17/48 (HOP62, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.783×** | -4.3 | 6e-04 | 26/49 (C32, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.788×** | -4.2 | 9e-04 | 22/48 (HCT15, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1132. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 110 | 3 (3 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -15.8) |
| [[SW480 (line)]] | alt | 87.1 | 3 (3 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 2.72× (z +15.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.369× (z -15.6) |
| [[A-172 (line)]] | wt | 148 | 1 (1 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.35× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -12.6) |
| [[C32 (line)]] | wt | 138 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +11.9) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.265× (z -14.3) |
| [[RKO (line)]] | wt | 113 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +14.7) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -24.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.389× (z -15.8) |
| [[LS 180 (line)]] | wt | 39.7 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +12.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 77.3 | 2 (2 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.32× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -13.5) |
| [[HS-578T (line)]] | alt | 146 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +10.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -13.7) |
| [[LoVo (line)]] | wt | 82.7 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +14.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -18.3) |
| [[LOX-IMVI (line)]] | wt | 89.8 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -17.7) |
| [[NCI-H1792 (line)]] | alt | 128 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -20.5) |
| [[NCI-H460 (line)]] | wt | 64.6 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +13.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -14.8) |
| [[PANC-1 (line)]] | alt | 96.8 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +12.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -17.0) |
| [[HEC-1-A (line)]] | alt | 70.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -11.0) |
| [[Hs 766T (line)]] | wt | 104 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.52× (z +11.0) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.550× (z -10.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -10.2) |
| [[J82 (line)]] | alt | 82.8 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.17× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -17.1) |
| [[MIA PaCa-2 (line)]] | alt | 81.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +11.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -13.0) |
| [[A498 (line)]] | wt | 110 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +10.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -8.8) |
| [[A549 (line)]] | wt | 74.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 71.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +9.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -9.0) |
| [[HT-29 (line)]] | alt | 57.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +12.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -11.0) |
| [[KATO III (line)]] | alt | 50.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +11.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 116 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -17.2) |
| [[SNU-423 (line)]] | alt | 74.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +11.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 95.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -15.7) |
| [[AsPC-1 (line)]] | alt | 125 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -13.6) |
| [[C-33 A (line)]] | alt | 89.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +9.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -9.2) |
| [[HCT15 (line)]] | alt | 50.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +10.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 147 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -14.6) |
| [[NCI-H2347 (line)]] | alt | 57.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.15× (z +8.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 54.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.558× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 64.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +11.3) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 29.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +9.9) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 69.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 40.9 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.182× (z -12.2) |
| [[hTERT-HPNE (line)]] | wt | 86.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 52.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -9.4) |
| [[SW 1088 (line)]] | alt | 93.2 | 0 | 1 | — | [[Mifepristone (drug)]] 5 µM 0.0730× (z -9.6) |
| [[SW 900 (line)]] | alt | 54.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +11.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 78.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 56.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1132), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTR2]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[REEP3]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SLC25A24]] | +0.58 | +0.39 / +0.64 | both halves | 6e-05 |  |
| [[RB1]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[BZW1]] | +0.56 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[MMGT1]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[SEPTIN10]] | +0.55 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[EFR3A]] | +0.54 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[AKAP11]] | +0.53 | +0.32 / +0.61 | both halves | 1e-04 |  |
| [[BTBD1]] | +0.53 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[IDH3A]] | +0.53 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[GMFB]] | +0.52 | +0.20 / +0.65 | both halves | 7e-04 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRC5C]] | -0.58 | -0.40 / -0.56 | both halves | 4e-05 |  |
| [[CCDC115]] | -0.57 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[NGDN]] | -0.57 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[ZNF581]] | -0.55 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[TFPT]] | -0.54 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[RPAIN]] | -0.53 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[SLC25A38]] | -0.52 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[IST1]] | -0.52 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[TMEM208]] | -0.50 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[ATP6V0E1]] | -0.50 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[TTC9C]] | -0.50 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[KBTBD4]] | -0.50 | -0.38 / -0.46 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRC5C]] | B | GPRC5C activity lowers BCAP29's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 1.64× higher at baseline in the lines without GPRC5C | 0.010 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1 |
| [[MSRB3]] | B | MSRB3 activity raises BCAP29's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 1.48× lower at baseline in the lines without MSRB3 | 0.050 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[CCDC88A]] | B | CCDC88A activity raises BCAP29's level | lines that do not express CCDC88A (8) vs lines expressing it (42) | 1.68× lower at baseline in the lines without CCDC88A | 0.089 | ⚠ within organs, on part of the lines; also absent: LIX1L, HEG1, CHROMR |
| [[SEPTIN10]] | C | SEPTIN10's natural level strengthens BCAP29's drug response | SEPTIN10's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.29; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[AT7519 (drug)]] 5 µM | C | BCAP29's natural level raises the cells' numbers under AT7519 5 µM (protects the cells) | BCAP29's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.305 over the table, 0.077 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **-** arm (projection on the module's main direction -0.548). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.0, -14.2); signed map (9.0, -8.3). **Vector** length 115, 33.6% of its response variance represented; |z| ≥ 3 in 1,269 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +20.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +20.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | -0.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.4 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | -0.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.6 | -20.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.0 | -10.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.6 | -9.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.3 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.0 | -9.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.9 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -6.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | B cell receptor associated protein 29 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.3 — chr7:107,580,246-107,629,170 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BAP29, DKFZp686M2086 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHQ4](https://www.uniprot.org/uniprotkb/Q9UHQ4) (B-cell receptor-associated protein 29):

> May play a role in anterograde transport of membrane proteins from the endoplasmic reticulum to the Golgi. May be involved in CASP8-mediated apoptosis (By similarity).

**Summary**, from NCBI Gene [55973](https://www.ncbi.nlm.nih.gov/gene/55973):

> Involved in osteoblast differentiation. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24131](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24131) · Entrez [55973](https://www.ncbi.nlm.nih.gov/gene/55973) · UniProt [Q9UHQ4](https://www.uniprot.org/uniprotkb/Q9UHQ4) · Ensembl [ENSG00000075790](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075790)

## Data

Gene col 1132: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1132); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1132, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1132]; `tensor/DDL_lfc|DDL_z.npy` [1132]; `embed/gene_vectors.npy` [1132]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1132 or target_col == 1132). Every well: [[BCAP29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCAP29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

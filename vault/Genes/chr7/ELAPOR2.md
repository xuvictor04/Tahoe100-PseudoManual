---
symbol: "ELAPOR2"
type: "gene"
col: 8982
ensembl_id: "ENSG00000164659"
name: "endosome-lysosome associated apoptosis and autophagy regulator family member 2"
location: "7q21.12"
module: 17
arm: "+"
pooled_cpm: 25.07
n_lines_expressing: 33
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 7
direction_downstream: 2
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ELAPOR2

*endosome-lysosome associated apoptosis and autophagy regulator family member 2* — 7q21.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.65× (z +24.2, q 0e+00, up in 23 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Abemaciclib (drug)]] 5 µM: 0.646× (z -4.0, q 0.035, down in 9 of 29 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 6 lines (HEC-1-A 0.190×, SW480 0.319×, AsPC-1 0.239×, LOX-IMVI 0.299×, …); [[Dinaciclib (drug)]] 5 µM in 5 lines (H4 0.0565×, LoVo 0.0786×, LOX-IMVI 0.102×, SHP-77 0.196×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C32 0.124×, NCI-H1573 0.235×, SK-MEL-2 0.143×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (H4 0.308×, HepG2/C3A 0.328×, C32 0.388×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.368×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AMOT]] (+0.64, fdr 1e-05), [[GABRG2]] (+0.63, fdr 5e-05), [[KPNA5]] (+0.59, fdr 1e-05); moves opposite to [[NPIPB11]] (-0.57, fdr 4e-05), [[TRPV1]] (-0.53, fdr 2e-04), [[TMEM11-DT]] (-0.53, fdr 6e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MIR2052HG]] → it (grade B ⚠); 2 go from it, the strongest it → [[CHRM3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8982.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.65×** | +24.2 | 0e+00 | 23/31 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.24×** | +20.0 | 0e+00 | 18/30 (NCI-H2030, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.75×** | +17.8 | 0e+00 | 14/30 (NCI-H2030, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.67×** | +17.3 | 0e+00 | 16/30 (LoVo, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.44×** | +15.7 | 0e+00 | 12/30 (SW 900, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.32×** | +14.8 | 0e+00 | 16/30 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.07×** | +12.8 | 8e-36 | 25/29 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +10.5 | 5e-24 | 5/25 (hTERT-HPNE, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +10.1 | 4e-22 | 5/20 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.9 | 2e-13 | 8/30 (RKO, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.36×** | +7.7 | 6e-13 | 16/29 (LOX-IMVI, LS 180, …) | rises with dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **2.21×** | +7.3 | 1e-11 | 13/30 (LoVo, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +6.4 | 6e-09 | 10/30 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.38×** | +5.5 | 2e-06 | 4/30 (SW 900, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +5.0 | 3e-05 | 6/23 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +4.3 | 5e-04 | 12/30 (SW480, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.002 | 9/30 (J82, C32, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.002 | 9/31 (NCI-H460, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.014 | 7/29 (NCI-H460, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8982.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 6 lines (HEC-1-A 0.190×, SW480 0.319×, AsPC-1 0.239×, LOX-IMVI 0.299×, …); [[Dinaciclib (drug)]] 5 µM in 5 lines (H4 0.0565×, LoVo 0.0786×, LOX-IMVI 0.102×, SHP-77 0.196×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C32 0.124×, NCI-H1573 0.235×, SK-MEL-2 0.143×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (H4 0.308×, HepG2/C3A 0.328×, C32 0.388×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.368×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Abemaciclib (drug)]] 5 µM |  | **0.646×** | -4.0 | 0.035 | 9/29 (SW 1271, NCI-H661, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.818× | -3.5 | 0.11 | 9/30 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.946× | -3.4 | 0.11 | 2/31 (RKO, SW48) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.825× | -3.4 | 0.11 | 21/30 (HEC-1-A, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.832× | -3.2 | 0.15 | 14/30 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.829× | -3.2 | 0.15 | 5/30 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.883× | -3.1 | 0.15 | 7/31 (AsPC-1, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.839× | -3.1 | 0.15 | 12/30 (NCI-H2030, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8982. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 39.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.368× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 7.27 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +17.4) | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.112× (z -10.0) |
| [[H4 (line)]] | wt | 77.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0565× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -12.0) |
| [[C-33 A (line)]] | alt | 90.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.324× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 46.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -10.8) |
| [[LoVo (line)]] | wt | 40.8 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.72× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.0786× (z -19.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 48.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.299× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 153 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -15.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 6.93 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 4.37× (z +8.5) | [[Auranofin (drug)]] 5 µM 0.103× (z -9.3) |
| [[SHP-77 (line)]] | alt | 112 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -14.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 76.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.9) | [[Auranofin (drug)]] 5 µM 0.319× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 42.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.239× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 57.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.190× (z -14.7) |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +11.7) | — |
| [[J82 (line)]] | alt | 28.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +11.4) | — |
| [[LS 180 (line)]] | wt | 36.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 11.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.50× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -13.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 8.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.67× (z +13.1) | — |
| [[SW48 (line)]] | wt | 7.85 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0464× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.04 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.59 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.71 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.55 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.41 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8982), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AMOT]] | +0.64 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[GABRG2]] | +0.63 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[KPNA5]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[HTR2C]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CXADR]] | +0.58 | +0.34 / +0.63 | both halves | 1e-04 |  |
| [[PLCB1]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[TAB2]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[RAB30]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[SPTB]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[COMMD8]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[CDC73]] | +0.55 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[NELL2]] | +0.54 | +0.38 / +0.61 | both halves | 7e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPIPB11]] | -0.57 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[TRPV1]] | -0.53 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[TMEM11-DT]] | -0.53 | -0.38 / -0.60 | both halves | 6e-05 |  |
| [[ANKMY1]] | -0.52 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[SMG1P6]] | -0.49 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[VPS53]] | -0.49 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[ING5]] | -0.49 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[PDCD6]] | -0.49 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[TIMM23B-AGAP6]] | -0.48 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[MAD1L1]] | -0.48 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[GOSR2]] | -0.47 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[SENP5]] | -0.47 | -0.41 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR2052HG]] | B | MIR2052HG activity raises ELAPOR2's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 3.02× lower at baseline in the lines without MIR2052HG | 0.048 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent |
| [[CHRM3]] | B | CHRM3 activity raises ELAPOR2's level | lines that do not express CHRM3 (20) vs lines expressing it (30) | 2.90× lower at baseline in the lines without CHRM3 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, NRXN1, MIR2052HG |
| [[JAKMIP2]] | B | JAKMIP2 activity raises ELAPOR2's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 2.37× lower at baseline in the lines without JAKMIP2 | 0.064 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent |
| [[CRISPLD1]] | B | CRISPLD1 activity raises ELAPOR2's level | lines that do not express CRISPLD1 (28) vs lines expressing it (22) | 2.78× lower at baseline in the lines without CRISPLD1 | 0.066 | ⚠ within organs, on part of the lines; also absent: GALNT13, ADAM23, SNCA |
| [[NELL2]] | B | NELL2 activity raises ELAPOR2's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 2.94× lower at baseline in the lines without NELL2 | 0.074 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent |
| [[SPINK5]] | B | SPINK5 activity raises ELAPOR2's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 2.23× lower at baseline in the lines without SPINK5 | 0.079 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588 |
| [[SGCE]] | B | SGCE activity raises ELAPOR2's level | lines that do not express SGCE (12) vs lines expressing it (38) | 2.76× lower at baseline in the lines without SGCE | 0.0998 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CHST10, HSPA2 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHRM3]] | B | ELAPOR2 activity raises CHRM3's level | lines that do not express ELAPOR2 (17) vs lines expressing it (33) | 3.81× lower at baseline in the lines without ELAPOR2 | 0.023 | ⚠ within organs, on part of the lines; also absent: SCN2A, CACNB2, ENSG00000227681 |
| [[RETREG1]] | B | ELAPOR2 activity raises RETREG1's level | lines that do not express ELAPOR2 (17) vs lines expressing it (33) | 2.25× lower at baseline in the lines without ELAPOR2 | 0.079 | ⚠ within organs, on part of the lines; also absent: SCN2A, CACNB2, ENSG00000227681 |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.451). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (31.2, 39.4); signed map (47.6, 36.8). **Vector** length 65.1, 13.0% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +24.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +12.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | -2.4 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -3.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.6 | -0.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | endosome-lysosome associated apoptosis and autophagy regulator family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.12 — chr7:86,876,906-87,059,654 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31340, EIG121L; previously KIAA1324L |
| Matched by | ensembl_id |

**Function**, from UniProt [A8MWY0](https://www.uniprot.org/uniprotkb/A8MWY0) (Endosome/lysosome-associated apoptosis and autophagy regulator family member 2):

> Functions as a regulator of the BMP signaling pathway and may be involved in epidermal differentiation.

**Summary**, from NCBI Gene [222223](https://www.ncbi.nlm.nih.gov/gene/222223):

> Predicted to enable BMP receptor binding activity. Predicted to be involved in negative regulation of nervous system development; positive regulation of BMP signaling pathway; and positive regulation of epidermis development. Predicted to be located in plasma membrane. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21945](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21945) · Entrez [222223](https://www.ncbi.nlm.nih.gov/gene/222223) · UniProt [A8MWY0](https://www.uniprot.org/uniprotkb/A8MWY0) · Ensembl [ENSG00000164659](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164659)

## Data

Gene col 8982: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8982); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8982, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8982]; `tensor/DDL_lfc|DDL_z.npy` [8982]; `embed/gene_vectors.npy` [8982]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8982 or target_col == 8982). Every well: [[ELAPOR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELAPOR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

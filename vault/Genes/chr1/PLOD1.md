---
symbol: "PLOD1"
type: "gene"
col: 1369
ensembl_id: "ENSG00000083444"
name: "procollagen-lysine,2-oxoglutarate 5-dioxygenase 1"
location: "1p36.22"
module: 50
arm: "+"
pooled_cpm: 57.24
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 28
n_dd_up_clean: 1
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# PLOD1

*procollagen-lysine,2-oxoglutarate 5-dioxygenase 1* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.90× (z +8.9, q 2e-16, up in 36 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 5 µM: 1.66× (z +3.7, q 0.035, up in 23 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HS-578T 2.84×, A498 2.82×, HOP62 2.90×, NCI-H460 2.69×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (A498 2.64×, A-172 2.77×, LoVo 2.89×; ⚠ toxic; transcription drop); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.49×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.283× (z -24.8, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUCB1]] (+0.69, fdr 7e-06), [[GANAB]] (+0.66, fdr 7e-06), [[PDIA4]] (+0.65, fdr 1e-05); moves opposite to [[PBDC1]] (-0.53, fdr 3e-05), [[CRCP]] (-0.51, fdr 3e-05), [[PTPN21]] (-0.51, fdr 3e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[APLP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1369.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HS-578T 2.84×, A498 2.82×, HOP62 2.90×, NCI-H460 2.69×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (A498 2.64×, A-172 2.77×, LoVo 2.89×; ⚠ toxic; transcription drop); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.49×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +8.9 | 2e-16 | 36/45 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +7.3 | 8e-11 | 32/41 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +3.9 | 0.016 | 23/43 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.66×** | +3.7 | 0.035 | 23/46 (RKO, KATO III, …) | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.25× | +3.1 | 0.18 | 16/47 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 1.25× | +3.1 | 0.18 | 18/47 (RPMI-7951, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 1.24× | +3.0 | 0.18 | 20/47 (RKO, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1369.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.283×** | -24.8 | 0e+00 | 44/47 (H4, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.238×** | -19.9 | 0e+00 | 46/47 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.343×** | -14.3 | 5e-44 | 47/47 (RPMI-7951, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.545×** | -8.4 | 6e-15 | 40/47 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.562×** | -8.0 | 2e-13 | 42/47 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.570×** | -7.8 | 6e-13 | 41/47 (NCI-H23, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.581×** | -7.5 | 4e-12 | 39/47 (SK-MEL-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.570×** | -7.5 | 5e-12 | 40/47 (HS-578T, A498, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.610×** | -6.8 | 5e-10 | 36/47 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.599×** | -6.8 | 5e-10 | 31/46 (HCT15, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.685×** | -5.2 | 8e-06 | 35/46 (C-33 A, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.712×** | -4.7 | 1e-04 | 30/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.708×** | -4.6 | 2e-04 | 26/46 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.793×** | -4.5 | 2e-04 | 28/47 (MIA PaCa-2, RPMI-7951, …) | rises with dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.748×** | -4.0 | 0.002 | 31/47 (LOX-IMVI, C-33 A, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.733×** | -4.0 | 0.003 | 23/46 (HS-578T, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.761×** | -3.8 | 0.005 | 24/47 (MIA PaCa-2, SW 1088, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.596×** | -3.8 | 0.005 | 22/48 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1369. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 109 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0540× (z -24.9) |
| [[NCI-H23 (line)]] | alt | 45.2 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -17.3) |
| [[SW480 (line)]] | alt | 32.3 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -14.1) |
| [[A498 (line)]] | wt | 67.9 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -18.4) |
| [[C-33 A (line)]] | alt | 55.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -14.6) |
| [[HS-578T (line)]] | alt | 200 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -27.5) |
| [[LS 180 (line)]] | wt | 60.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -18.9) |
| [[NCI-H460 (line)]] | wt | 40.4 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -15.4) |
| [[H4 (line)]] | wt | 116 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0318× (z -36.3) |
| [[NCI-H1792 (line)]] | alt | 56.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -17.4) |
| [[PANC-1 (line)]] | alt | 56.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -25.8) |
| [[SK-MEL-2 (line)]] | alt | 87.0 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.154× (z -13.6) |
| [[A-172 (line)]] | wt | 44.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -16.0) |
| [[A-427 (line)]] | wt | 35.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0985× (z -17.2) |
| [[HCT15 (line)]] | alt | 62.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -16.5) |
| [[HEC-1-A (line)]] | alt | 69.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -18.0) |
| [[HOP62 (line)]] | alt | 92.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -15.7) |
| [[Hs 766T (line)]] | wt | 73.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -22.3) |
| [[hTERT-HPNE (line)]] | wt | 159 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -19.2) |
| [[J82 (line)]] | alt | 50.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -21.9) |
| [[KATO III (line)]] | alt | 53.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -18.2) |
| [[LoVo (line)]] | wt | 25.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.340× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 43.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -17.5) |
| [[RPMI-7951 (line)]] | alt | 206 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -25.8) |
| [[A549 (line)]] | wt | 22.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 31.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.154× (z -11.6) |
| [[BT-474 (line)]] | alt | 23.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -12.8) |
| [[C32 (line)]] | wt | 184 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.265× (z -13.1) |
| [[CFPAC-1 (line)]] | alt | 27.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -12.9) |
| [[HepG2_C3A (line)]] | wt | 97.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -18.8) |
| [[LOX-IMVI (line)]] | wt | 29.8 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.180× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 29.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -10.1) |
| [[SNU-1 (line)]] | wt | 78.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0501× (z -20.4) |
| [[SNU-423 (line)]] | alt | 71.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -18.1) |
| [[SW 1088 (line)]] | alt | 287 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -15.7) |
| [[SW 1271 (line)]] | alt | 55.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -10.4) |
| [[SW 900 (line)]] | alt | 20.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -9.4) |
| [[AN3 CA (line)]] | alt | 87.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -11.8) |
| [[HT-29 (line)]] | alt | 21.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -11.1) |
| [[NCI-H661 (line)]] | alt | 61.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -13.1) |
| [[Panc 03.27 (line)]] | alt | 40.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -14.8) |
| [[SHP-77 (line)]] | alt | 28.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -11.9) |
| [[SW1417 (line)]] | alt | 22.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -10.3) |
| [[CHP-212 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1369), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUCB1]] | +0.69 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[GANAB]] | +0.66 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[PDIA4]] | +0.65 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[FKBP10]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 | STRING 535 |
| [[ABCA2]] | +0.63 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[GLG1]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[GPI]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[DDX41]] | +0.62 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[MAN1B1]] | +0.62 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[BSG]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[LRPAP1]] | +0.61 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[P4HB]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 | pathway: Collagen biosynthesis and modifying enzymes; STRING 434 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBDC1]] | -0.53 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[CRCP]] | -0.51 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PTPN21]] | -0.51 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[HSPBAP1]] | -0.50 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ITSN2]] | -0.50 | -0.46 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APLP1]] | B | APLP1 activity raises PLOD1's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 1.47× lower at baseline in the lines without APLP1 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[P3H3]] | B | P3H3 activity raises PLOD1's level | lines that do not express P3H3 (10) vs lines expressing it (40) | 1.80× lower at baseline in the lines without P3H3 | 0.038 | ⚠ within organs, on part of the lines; also absent: STARD9, GSTA4, CTXN1 |
| [[SEPTIN5]] | B | SEPTIN5 activity raises PLOD1's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.36× lower at baseline in the lines without SEPTIN5 | 0.058 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[SPARC]] | B | SPARC activity raises PLOD1's level | lines that do not express SPARC (34) vs lines expressing it (16) | 2.16× lower at baseline in the lines without SPARC | 0.066 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032 |
| [[COL1A2]] | B | COL1A2 activity raises PLOD1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 2.34× lower at baseline in the lines without COL1A2 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5 |
| [[CRTAP]] | C | CRTAP activity raises PLOD1's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 3.19× lower at baseline in the lines without CRTAP | 0.049 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.8, -21.6); signed map (-52.2, -4.1). **Vector** length 111, 34.2% of its response variance represented; |z| ≥ 3 in 1,128 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Degradation of the extracellular matrix* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.2 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | -1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | -1.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +0.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.6 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.5 | +3.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.7 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.4 | -19.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.4 | -4.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.0 | -14.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.3 | -6.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.2 | -4.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.8 | -7.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -4.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | procollagen-lysine,2-oxoglutarate 5-dioxygenase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:11,934,205-11,975,538 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LH1; previously LLH, PLOD |
| Gene groups (HGNC) | Procollagen-lysine,2-oxoglutarate 5-dioxygenase family |
| Hallmark sets | GLYCOLYSIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 3 pathways, smallest: Collagen biosynthesis and modifying enzymes; Collagen formation; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02809](https://www.uniprot.org/uniprotkb/Q02809) (Procollagen-lysine,2-oxoglutarate 5-dioxygenase 1):

> Part of a complex composed of PLOD1, P3H3 and P3H4 that catalyzes hydroxylation of lysine residues in collagen alpha chains and is required for normal assembly and cross-linkling of collagen fibrils (By similarity). Forms hydroxylysine residues in -Xaa-Lys-Gly- sequences in collagens. These hydroxylysines serve as sites of attachment for carbohydrate units and are essential for the stability of the intermolecular collagen cross-links (Probable).

**Summary**, from NCBI Gene [5351](https://www.ncbi.nlm.nih.gov/gene/5351):

> Lysyl hydroxylase is a membrane-bound homodimeric protein localized to the cisternae of the endoplasmic reticulum. The enzyme (cofactors iron and ascorbate) catalyzes the hydroxylation of lysyl residues in collagen-like peptides. The resultant hydroxylysyl groups are attachment sites for carbohydrates in collagen and thus are critical for the stability of intermolecular crosslinks. Some patients with Ehlers-Danlos syndrome type VI have deficiencies in lysyl hydroxylase activity. Two transcript …

**Accessions** — [HGNC:9081](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9081) · Entrez [5351](https://www.ncbi.nlm.nih.gov/gene/5351) · UniProt [Q02809](https://www.uniprot.org/uniprotkb/Q02809) · Ensembl [ENSG00000083444](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083444)

## Data

Gene col 1369: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1369); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1369, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1369]; `tensor/DDL_lfc|DDL_z.npy` [1369]; `embed/gene_vectors.npy` [1369]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1369 or target_col == 1369). Every well: [[PLOD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLOD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

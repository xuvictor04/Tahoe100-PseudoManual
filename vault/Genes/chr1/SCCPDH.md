---
symbol: "SCCPDH"
type: "gene"
col: 6787
ensembl_id: "ENSG00000143653"
name: "saccharopine dehydrogenase (putative)"
location: "1q44"
module: 25
arm: "+"
pooled_cpm: 34.71
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 21
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SCCPDH

*saccharopine dehydrogenase (putative)* — 1q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.17× (z +14.9, q 0e+00, up in 38 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.33× (z +4.0, q 0.011, up in 16 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (PANC-1 2.42×, A498 3.47×, SNU-423 3.11×, NCI-H2347 2.42×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (Hs 766T 4.91×, A549 3.11×, PANC-1 2.30×, SK-MEL-2 2.83×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.406× (z -24.4, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NELFCD]] (+0.69, fdr 7e-06), [[TSPAN6]] (+0.67, fdr 7e-06), [[MANEA]] (+0.67, fdr 1e-05); moves opposite to [[ZBTB7A]] (-0.66, fdr 7e-06), [[UBE2CP5]] (-0.60, fdr 1e-05), [[TTLL3]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NUP210]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6787.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (PANC-1 2.42×, A498 3.47×, SNU-423 3.11×, NCI-H2347 2.42×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (Hs 766T 4.91×, A549 3.11×, PANC-1 2.30×, SK-MEL-2 2.83×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +14.9 | 0e+00 | 38/44 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +13.5 | 4e-39 | 29/38 (Hs 766T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +7.6 | 5e-12 | 28/41 (A549, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.33×** | +4.0 | 0.011 | 16/46 (J82, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6787.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.406×** | -24.4 | 0e+00 | 44/47 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.567×** | -15.4 | 0e+00 | 38/48 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.484×** | -13.9 | 2e-41 | 44/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.509×** | -12.9 | 6e-36 | 38/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.534×** | -12.0 | 4e-31 | 39/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.537×** | -11.9 | 1e-30 | 39/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.539×** | -11.8 | 3e-30 | 37/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.558×** | -11.1 | 5e-27 | 36/48 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.605×** | -9.6 | 6e-20 | 35/47 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.599×** | -9.4 | 3e-19 | 34/48 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.620×** | -9.1 | 4e-18 | 37/47 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.655×** | -8.1 | 3e-14 | 28/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.670×** | -7.6 | 1e-12 | 34/47 (A-427, SW48, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.479×** | -7.4 | 7e-12 | 29/48 (NCI-H23, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.701×** | -6.8 | 5e-10 | 31/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.528×** | -6.4 | 6e-09 | 29/46 (LoVo, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6787. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 34.2 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -16.5) |
| [[A549 (line)]] | wt | 37.2 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 164 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -23.7) |
| [[SNU-1 (line)]] | wt | 50.7 | 0 | 6 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0872× (z -12.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -11.6) |
| [[SW480 (line)]] | alt | 24.7 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.261× (z -12.8) |
| [[HCT15 (line)]] | alt | 48.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -11.1) |
| [[A-172 (line)]] | wt | 42.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.356× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.529× (z -8.8) |
| [[Hs 766T (line)]] | wt | 24.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.91× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 36.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0638× (z -21.8) |
| [[SK-MEL-2 (line)]] | alt | 62.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -17.1) |
| [[SNU-423 (line)]] | alt | 33.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -14.4) |
| [[A498 (line)]] | wt | 14.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 34.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -21.4) |
| [[HOP62 (line)]] | alt | 31.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -19.7) |
| [[J82 (line)]] | alt | 30.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -16.0) |
| [[KATO III (line)]] | alt | 10.5 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.137× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 21.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -14.4) |
| [[NCI-H2347 (line)]] | alt | 32.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -13.0) |
| [[SW 900 (line)]] | alt | 33.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -12.6) |
| [[A-427 (line)]] | wt | 41.6 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.231× (z -14.3) |
| [[C-33 A (line)]] | alt | 68.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -10.1) |
| [[C32 (line)]] | wt | 24.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -10.5) |
| [[COLO 205 (line)]] | alt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 42.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -11.7) |
| [[HepG2_C3A (line)]] | wt | 27.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -11.0) |
| [[HS-578T (line)]] | alt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -13.9) |
| [[HT-29 (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -9.1) |
| [[LoVo (line)]] | wt | 20.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 25.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.6) |
| [[LS 180 (line)]] | wt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 21.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.311× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -14.8) |
| [[SW 1271 (line)]] | alt | 83.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -8.6) |
| [[SW1417 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -9.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 48.8 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.228× (z -9.8) |
| [[AN3 CA (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6787), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NELFCD]] | +0.69 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[TSPAN6]] | +0.67 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[MANEA]] | +0.67 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[MBTPS2]] | +0.64 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[EXOC5]] | +0.64 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[TMEM237]] | +0.64 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[DLD]] | +0.64 | +0.54 / +0.69 | both halves | 1e-05 | same gene group |
| [[OCRL]] | +0.63 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[PTGR2]] | +0.62 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SGCB]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[ALG10]] | +0.61 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[RBBP9]] | +0.60 | +0.50 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB7A]] | -0.66 | -0.62 / -0.67 | both halves | 7e-06 |  |
| [[UBE2CP5]] | -0.60 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[TTLL3]] | -0.58 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[ELL]] | -0.57 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[FBXL18]] | -0.56 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SMBD1P]] | -0.55 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[LINC00685]] | -0.55 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[RPL36AL]] ⚠ | -0.54 | -0.52 / -0.51 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[KCNK6]] | -0.54 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[HIC2]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ISG20L2]] | -0.54 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[MIDN]] | -0.54 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[ZNF324]] | -0.54 | -0.46 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUP210]] | B | NUP210 activity raises SCCPDH's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 1.63× lower at baseline in the lines without NUP210 | 0.092 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A |
| [[CFL2]] | C | CFL2 activity raises SCCPDH's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.93× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.731). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.1, -18.6); signed map (-16.6, -40.2). **Vector** length 70.4, 14.2% of its response variance represented; |z| ≥ 3 in 1,106 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +7.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.3 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.7 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.4 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -15.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.8 | -11.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.4 | -7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.1 | -9.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.7 | -1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.6 | -2.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.6 | -0.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | saccharopine dehydrogenase (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q44 — chr1:246,724,409-246,768,137 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-49, NET11 |
| Gene groups (HGNC) | Oxidoreductases |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

UniProt [Q8NBX0](https://www.uniprot.org/uniprotkb/Q8NBX0) carries no function annotation.

**Summary**, from NCBI Gene [51097](https://www.ncbi.nlm.nih.gov/gene/51097):

> Predicted to enable oxidoreductase activity. Predicted to be involved in glycolipid biosynthetic process. Located in lipid droplet and midbody. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24275](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24275) · Entrez [51097](https://www.ncbi.nlm.nih.gov/gene/51097) · UniProt [Q8NBX0](https://www.uniprot.org/uniprotkb/Q8NBX0) · Ensembl [ENSG00000143653](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143653)

## Data

Gene col 6787: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6787); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6787, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6787]; `tensor/DDL_lfc|DDL_z.npy` [6787]; `embed/gene_vectors.npy` [6787]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6787 or target_col == 6787). Every well: [[SCCPDH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCCPDH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

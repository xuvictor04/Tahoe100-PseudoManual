---
symbol: "WASHC2A"
type: "gene"
col: 1791
ensembl_id: "ENSG00000099290"
name: "WASH complex subunit 2A"
location: "10q11.23"
module: 122
arm: "+"
pooled_cpm: 26.81
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 6
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# WASHC2A

*WASH complex subunit 2A* — 10q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.23× (z +23.9, q 0e+00, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.574× (z -16.6, q 0e+00, down in 45 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Tucidinostat (drug)]] 5 µM in 4 lines (CFPAC-1 0.453×, SW480 0.491×, LoVo 0.444×, SW1417 0.484×); [[Tucidinostat (drug)]] 0.5 µM in 3 lines (SW480 0.369×, LoVo 0.285×, SHP-77 0.156×); [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.173×, HCT15 0.228×; ⚠ toxic; transcription drop); [[Decitabine (drug)]] 0.05 µM in 1 line (SW48 0.0583×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASHC2C]] (+0.98, fdr 7e-06), [[ATP6V1C1]] (+0.73, fdr 7e-06), [[RRAGB]] (+0.70, fdr 7e-06); moves opposite to [[LSM4]] (-0.59, fdr 1e-05), [[EXTL3]] (-0.52, fdr 3e-05), [[CD320]] (-0.50, fdr 4e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1791.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.23×** | +23.9 | 0e+00 | 37/48 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +13.4 | 9e-39 | 41/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.88×** | +13.3 | 5e-38 | 37/47 (NCI-H460, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.62×** | +10.2 | 3e-22 | 36/48 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +10.0 | 3e-21 | 29/43 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +9.4 | 8e-19 | 28/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +7.2 | 4e-11 | 28/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +6.9 | 3e-10 | 26/47 (MIA PaCa-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.39×** | +6.9 | 3e-10 | 26/48 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +5.4 | 3e-06 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +5.4 | 3e-06 | 14/35 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 5 µM |  | 1.20× | +5.3 | 6e-06 | 16/48 (NCI-H460, RPMI-7951, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +5.1 | 2e-05 | 18/48 (RKO, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.9 | 3e-05 | 15/48 (A-427, J82, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.25×** | +4.7 | 1e-04 | 18/46 (PANC-1, RPMI-7951, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.24×** | +4.6 | 2e-04 | 11/48 (PANC-1, RPMI-7951, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.24×** | +4.6 | 2e-04 | 17/48 (SW1417, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +4.5 | 2e-04 | 14/48 (NCI-H460, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.16× | +4.4 | 3e-04 | 9/48 (PANC-1, RPMI-7951, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.001 | 12/48 (SW1417, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1791.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Tucidinostat (drug)]] 5 µM in 4 lines (CFPAC-1 0.453×, SW480 0.491×, LoVo 0.444×, SW1417 0.484×); [[Tucidinostat (drug)]] 0.5 µM in 3 lines (SW480 0.369×, LoVo 0.285×, SHP-77 0.156×); [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.173×, HCT15 0.228×; ⚠ toxic; transcription drop); [[Decitabine (drug)]] 0.05 µM in 1 line (SW48 0.0583×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.574×** | -16.6 | 0e+00 | 45/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.521×** | -13.7 | 2e-40 | 41/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.807×** | -4.4 | 0.002 | 17/46 (SNU-423, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.827×** | -4.0 | 0.007 | 19/48 (LoVo, NCI-H2030, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.827×** | -4.0 | 0.007 | 10/47 (SW480, PANC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.830×** | -4.0 | 0.007 | 14/48 (NCI-H460, SNU-423, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.844× | -3.6 | 0.024 | 13/47 (NCI-H460, KATO III, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.844× | -3.6 | 0.024 | 7/48 (LOX-IMVI, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 0.848× | -3.5 | 0.029 | 10/46 (SW 900, NCI-H661, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.851× | -3.3 | 0.056 | 11/48 (SNU-423, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | 0.867× | -3.0 | 0.13 | 13/46 (LS 180, SW480, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1791. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.20× (z +32.2) | — |
| [[SW1417 (line)]] | alt | 32.4 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.9) | [[Tucidinostat (drug)]] 5 µM 0.484× (z -9.2) |
| [[A-172 (line)]] | wt | 21.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +13.3) | — |
| [[NCI-H1573 (line)]] | alt | 15.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.14× (z +19.4) | — |
| [[SNU-423 (line)]] | alt | 104 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +15.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -11.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A498 (line)]] | wt | 29.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +11.6) | — |
| [[AsPC-1 (line)]] | alt | 14.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +11.8) | — |
| [[J82 (line)]] | alt | 20.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +18.7) | — |
| [[LoVo (line)]] | wt | 21.9 | 0 | 2 | — | [[Tucidinostat (drug)]] 0.5 µM 0.285× (z -10.4) |
| [[LS 180 (line)]] | wt | 24.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -12.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 28.6 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.84× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +13.7) | [[Belinostat (drug)]] 0.5 µM 0.216× (z -8.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW480 (line)]] | alt | 34.0 | 0 | 2 | — | [[Tucidinostat (drug)]] 5 µM 0.491× (z -10.7) |
| [[A-427 (line)]] | wt | 24.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +13.8) | — |
| [[AN3 CA (line)]] | alt | 66.5 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0931× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 36.4 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.453× (z -10.9) |
| [[COLO 205 (line)]] | alt | 24.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -9.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 29.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 27.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +20.3) | — |
| [[HT-29 (line)]] | alt | 20.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.32× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 27.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +10.8) | — |
| [[KATO III (line)]] | alt | 20.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 41.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +11.9) | — |
| [[NCI-H2347 (line)]] | alt | 18.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +19.2) | — |
| [[RPMI-7951 (line)]] | alt | 26.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +11.4) | — |
| [[SHP-77 (line)]] | alt | 16.9 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.156× (z -10.1) |
| [[SW 900 (line)]] | alt | 31.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +12.7) | — |
| [[SW48 (line)]] | wt | 29.7 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0583× (z -14.8) |
| [[A549 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1791), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASHC2C]] | +0.98 | +0.96 / +0.98 | both halves | 7e-06 | same gene group; STRING 963 |
| [[ATP6V1C1]] | +0.73 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[RRAGB]] | +0.70 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[VPS11]] | +0.67 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[ALG1]] | +0.65 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[HPS1]] | +0.65 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[HEXA]] | +0.65 | +0.47 / +0.72 | both halves | 2e-05 |  |
| [[AP5Z1]] | +0.64 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[VPS33A]] | +0.64 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[SLC38A7]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[CLN3]] | +0.62 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[TMEM192]] | +0.61 | +0.59 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM4]] | -0.59 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[EXTL3]] | -0.52 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[CD320]] | -0.50 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[SRGAP2D]] | -0.48 | -0.44 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers WASHC2A's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 5.3% of all compounds | 0.026 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises WASHC2A's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.843). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-19.2, 13.9); signed map (-9.6, -19.5). **Vector** length 113, 27.7% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.4 | +13.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +23.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +8.1 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.4 | +13.3 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | +5.7 | +6.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.0 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +5.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +3.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +3.4 | +4.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.0 | -16.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.4 | -13.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.4 | -4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.9 | -4.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.6 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.5 | -3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.3 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | WASH complex subunit 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.23 — chr10:50,067,888-50,133,509 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA56A21.1, bA98I6.1, FLJ10824; previously FAM21B, FAM21A |
| Gene groups (HGNC) | WASH complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q641Q2](https://www.uniprot.org/uniprotkb/Q641Q2) (WASH complex subunit 2A):

> Acts at least in part as component of the WASH core complex whose assembly at the surface of endosomes inhibits WASH nucleation-promoting factor (NPF) activity in recruiting and activating the Arp2/3 complex to induce actin polymerization and is involved in the fission of tubules that serve as transport intermediates during endosome sorting. Mediates the recruitment of the WASH core complex to endosome membranes via binding to phospholipids and VPS35 of the retromer CSC. Mediates the …

**Summary**, from NCBI Gene [387680](https://www.ncbi.nlm.nih.gov/gene/387680):

> Predicted to enable phosphatidylinositol phosphate binding activity and retromer complex binding activity. Involved in protein localization to endosome. Predicted to be located in early endosome membrane. Predicted to be part of WASH complex. Predicted to be active in early endosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23416](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23416) · Entrez [387680](https://www.ncbi.nlm.nih.gov/gene/387680) · UniProt [Q641Q2](https://www.uniprot.org/uniprotkb/Q641Q2) · Ensembl [ENSG00000099290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099290)

## Data

Gene col 1791: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1791); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1791, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1791]; `tensor/DDL_lfc|DDL_z.npy` [1791]; `embed/gene_vectors.npy` [1791]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1791 or target_col == 1791). Every well: [[WASHC2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WASHC2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

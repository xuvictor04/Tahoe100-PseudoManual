---
symbol: "ITM2B"
type: "gene"
col: 5825
ensembl_id: "ENSG00000136156"
name: "integral membrane protein 2B"
location: "13q14.2"
module: 29
arm: "+"
pooled_cpm: 89.51
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 18
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# ITM2B

*integral membrane protein 2B* — 13q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.06× (z +12.6, q 1e-33, up in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.50× (z +10.0, q 3e-21, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.574× (z -9.7, q 3e-19, down in 46 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.679× (z -9.5, q 4e-19, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCARB2]] (+0.76, fdr 7e-06), [[TMEM59]] (+0.74, fdr 7e-06), [[GRN]] (+0.71, fdr 7e-06); moves opposite to [[EIF5B]] (-0.67, fdr 7e-06), [[NIFK]] (-0.65, fdr 7e-06), [[MPP3]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5825.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +12.6 | 1e-33 | 43/49 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +10.5 | 4e-23 | 36/40 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +10.0 | 3e-21 | 41/49 (AsPC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +8.1 | 8e-14 | 31/45 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.7 | 2e-04 | 30/50 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.3 | 0.002 | 19/48 (HOP62, A-172, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.010 | 27/47 (A498, AsPC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.8 | 0.011 | 20/48 (J82, LS 180, …) | rises with dose | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.011 | 25/48 (AsPC-1, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.011 | 25/48 (HEC-1-A, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.013 | 23/47 (LoVo, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5825.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.574×** | -9.7 | 3e-19 | 46/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.679×** | -9.5 | 4e-19 | 35/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.621×** | -7.2 | 1e-10 | 39/48 (AN3 CA, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.687×** | -6.3 | 5e-08 | 38/48 (H4, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.754×** | -4.9 | 1e-04 | 32/48 (SNU-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.627×** | -4.2 | 0.002 | 27/48 (NCI-H460, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.784×** | -4.2 | 0.002 | 29/48 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.641×** | -4.0 | 0.004 | 26/48 (NCI-H23, A498, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.645×** | -4.0 | 0.004 | 26/48 (MIA PaCa-2, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.795×** | -4.0 | 0.004 | 24/48 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.850× | -4.0 | 0.004 | 19/49 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.800×** | -3.9 | 0.005 | 24/48 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.810×** | -3.6 | 0.012 | 24/48 (LoVo, HepG2/C3A, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.815×** | -3.6 | 0.015 | 21/48 (MIA PaCa-2, NCI-H460, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -3.5 | 0.018 | 2/50 (SW 1088, SW 1271) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.687×** | -3.4 | 0.021 | 24/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.825×** | -3.2 | 0.040 | 23/49 (hTERT-HPNE, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5825. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 135 | 4 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.32× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +10.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.508× (z -8.5) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 71.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 75.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.238× (z -10.2) |
| [[A498 (line)]] | wt | 220 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 179 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -9.5) |
| [[J82 (line)]] | alt | 83.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 96.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +13.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 65.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +10.4) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.341× (z -11.9) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.565× (z -8.9) |
| [[A549 (line)]] | wt | 59.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +12.3) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 103 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -11.5) |
| [[KATO III (line)]] | alt | 146 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.553× (z -9.0) |
| [[LoVo (line)]] | wt | 84.5 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.449× (z -8.8) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.577× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 59.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +12.2) | — |
| [[PANC-1 (line)]] | alt | 51.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +13.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 57.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -9.9) |
| [[SW480 (line)]] | alt | 68.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +13.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 50.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 146 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0872× (z -14.6) |
| [[AsPC-1 (line)]] | alt | 56.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +13.1) | — |
| [[C-33 A (line)]] | alt | 35.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +10.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 111 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 71.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 94.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +12.3) | — |
| [[NCI-H1792 (line)]] | alt | 52.1 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0853× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~23% of this change |
| [[NCI-H2030 (line)]] | alt | 44.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 97.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -14.1) |
| [[Panc 03.27 (line)]] | alt | 147 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.489× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 113 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -9.8) |
| [[SHP-77 (line)]] | alt | 43.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 40.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 61.4 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0922× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~23% of this change |
| [[A-172 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 81.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 80.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 59.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5825), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCARB2]] | +0.76 | +0.72 / +0.79 | both halves | 7e-06 |  |
| [[TMEM59]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 | STRING 427 |
| [[GRN]] | +0.71 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[SH3BGRL]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[LAMP2]] | +0.67 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[ATRAID]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TMEM30A]] | +0.66 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[TMEM123]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[PRCP]] | +0.65 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[ERAP1]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[HLA-C]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[LAPTM4A]] | +0.64 | +0.57 / +0.72 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF5B]] | -0.67 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[NIFK]] | -0.65 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[MPP3]] | -0.64 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[UTP14A]] | -0.62 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[PDCD11]] | -0.61 | -0.57 / -0.60 | both halves | 9e-06 |  |
| [[GPSM1]] | -0.61 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[EIF3J]] | -0.60 | -0.56 / -0.67 | both halves | 1e-05 |  |
| [[SNHG17]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[RRP7BP-1]] | -0.59 | -0.46 / -0.66 | both halves | 3e-05 |  |
| [[BRIX1]] | -0.58 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[SURF6]] | -0.58 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[DNAJA3]] | -0.58 | -0.51 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ITM2B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CD74]] | B | CD74 activity raises ITM2B's level | lines that do not express CD74 (31) vs lines expressing it (19) | 1.34× lower at baseline in the lines without CD74 | 0.090 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[FTH1]] | C | FTH1 activity raises ITM2B's level | lines that do not express FTH1 (4) vs lines expressing it (46) | 1.85× lower at baseline in the lines without FTH1 | 0.082 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000284716, ZFP36, DDR1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.713). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.1, -20.0); signed map (-24.1, -37.4). **Vector** length 130, 40.8% of its response variance represented; |z| ≥ 3 in 879 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +10.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | +1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.6 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.3 | +3.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.1 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.8 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.7 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.9 | -9.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.2 | -7.2 |
|  | [[EX229 (drug)]] 5 µM |  | -5.2 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -3.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.7 | -6.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.5 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -4.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.2 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | integral membrane protein 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.2 — chr13:48,232,612-48,270,357 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BRI, E25B, E3-16, BRICD2B, BRI2 |
| Gene groups (HGNC) | BRICHOS domain containing |
| Reactome | 1 pathways, smallest: Amyloid fiber formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y287](https://www.uniprot.org/uniprotkb/Q9Y287) (Integral membrane protein 2B):

> Plays a regulatory role in the processing of the amyloid-beta A4 precursor protein (APP) and acts as an inhibitor of amyloid-beta peptide aggregation and fibril deposition. Plays a role in the induction of neurite outgrowth. Functions as a protease inhibitor by blocking access of secretases to APP cleavage sites.; [BRI2, membrane form]: Functions as a modulator of amyloid-beta A4 precursor protein (APP) processing, leading to a strong reduction in the secretion of secretase-processed …

**Summary**, from NCBI Gene [9445](https://www.ncbi.nlm.nih.gov/gene/9445):

> Amyloid precursor proteins are processed by beta-secretase and gamma-secretase to produce beta-amyloid peptides which form the characteristic plaques of Alzheimer disease. This gene encodes a transmembrane protein which is processed at the C-terminus by furin or furin-like proteases to produce a small secreted peptide which inhibits the deposition of beta-amyloid. Mutations which result in extension of the C-terminal end of the encoded protein, thereby increasing the size of the secreted …

**Accessions** — [HGNC:6174](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6174) · Entrez [9445](https://www.ncbi.nlm.nih.gov/gene/9445) · UniProt [Q9Y287](https://www.uniprot.org/uniprotkb/Q9Y287) · Ensembl [ENSG00000136156](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136156)

## Data

Gene col 5825: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5825); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5825, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5825]; `tensor/DDL_lfc|DDL_z.npy` [5825]; `embed/gene_vectors.npy` [5825]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5825 or target_col == 5825). Every well: [[ITM2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITM2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

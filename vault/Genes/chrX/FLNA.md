---
symbol: "FLNA"
type: "gene"
col: 12305
ensembl_id: "ENSG00000196924"
name: "filamin A"
location: "Xq28"
module: 111
arm: "+"
pooled_cpm: 243.4
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# FLNA

*filamin A* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.43× (z +14.4, q 2e-44, up in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.47× (z +6.3, q 4e-08, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 0.727× (z -3.8, q 0.096, down in 37 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C-33 A 0.462×, BT-474 0.487×; ⚠ cell-cycle shift, explains ~25% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (C-33 A 0.350×, LoVo 0.356×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cabozantinib (S-malate) (drug)]] 5 µM in 1 line (KATO III 0.348×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR1]] (+0.71, fdr 7e-06), [[ACTB]] (+0.71, fdr 7e-06), [[ACADVL]] (+0.69, fdr 8e-06); moves opposite to [[SMIM26]] (-0.67, fdr 8e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[ATP5MC2]] (-0.62, fdr 1e-05), [[MRPL23]] (-0.61, fdr 3e-05), [[PIGBOS1]] (-0.60, fdr 2e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[CD59]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12305.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.43×** | +14.4 | 2e-44 | 48/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.06×** | +12.6 | 5e-34 | 44/44 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.79×** | +11.1 | 2e-26 | 45/45 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.3 | 4e-08 | 38/48 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +6.2 | 8e-08 | 41/49 (LS 180, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.39×** | +5.4 | 6e-06 | 29/47 (NCI-H1792, A498, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.6 | 3e-04 | 36/47 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +4.6 | 4e-04 | 34/47 (MIA PaCa-2, HT-29, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.46×** | +4.4 | 7e-04 | 37/47 (HCT15, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.43×** | +4.2 | 0.002 | 30/47 (HCT15, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.44×** | +4.0 | 0.003 | 36/47 (HEC-1-A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.36×** | +3.6 | 0.014 | 25/47 (NCI-H460, AsPC-1, …) | top dose only | composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.35×** | +3.5 | 0.018 | 31/47 (HT-29, NCI-H1573, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.024 | 27/47 (A-427, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.036 | 31/47 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.040 | 26/47 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.045 | 26/47 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.056 | 30/48 (RKO, A498, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12305.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C-33 A 0.462×, BT-474 0.487×; ⚠ cell-cycle shift, explains ~25% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (C-33 A 0.350×, LoVo 0.356×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cabozantinib (S-malate) (drug)]] 5 µM in 1 line (KATO III 0.348×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.727×** | -3.8 | 0.096 | 37/47 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.810× | -3.5 | 0.12 | 30/47 (HEC-1-A, J82, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 0.590× | -3.3 | 0.22 | 30/44 (NCI-H2030, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.773× | -3.0 | 0.34 | 30/48 (SW 1088, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12305. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 226 | 10 (8 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.78× (z +12.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 120 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +11.3) | — |
| [[A-427 (line)]] | wt | 129 | 5 (4 ⚠) | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.43× (z +11.8) | — |
| [[A498 (line)]] | wt | 276 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.46× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 161 | 3 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -9.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HT-29 (line)]] | alt | 136 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 2.05× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 102 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +13.7) | — |
| [[NCI-H1792 (line)]] | alt | 130 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +17.2) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[PANC-1 (line)]] | alt | 179 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +17.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 337 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +11.4) | — |
| [[SW 900 (line)]] | alt | 298 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.97× (z +9.3) | — |
| [[A-172 (line)]] | wt | 474 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +8.6) | — |
| [[A549 (line)]] | wt | 306 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.14× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 224 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +11.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[LoVo (line)]] | wt | 107 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +13.7) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.356× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 181 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +13.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 225 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +12.2) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SW1417 (line)]] | alt | 256 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +12.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 163 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +14.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.36× (z +9.8) | — |
| [[C32 (line)]] | wt | 215 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 395 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +12.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 366 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 328 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +14.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 423 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +11.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 154 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +10.6) ⚠ toxic; transcription drop | [[Cabozantinib (S-malate) (drug)]] 5 µM 0.348× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 117 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +13.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.26× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 258 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +12.2) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 86.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +8.8) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SW480 (line)]] | alt | 221 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +12.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 194 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.91× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 231 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 395 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.2) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H23 (line)]] | alt | 202 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 253 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 69.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 255 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.9) | — |
| [[BT-474 (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -9.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[CHP-212 (line)]] | wt | 117 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.08× (z +10.5) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 319 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 542 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +9.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 296 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +9.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 284 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +9.4) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 22.1 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 161 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 450 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 410 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 260 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12305), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR1]] | +0.71 | +0.71 / +0.71 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 874 |
| [[ACTB]] | +0.71 | +0.72 / +0.69 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 750 |
| [[ACADVL]] | +0.69 | +0.58 / +0.71 | both halves | 8e-06 |  |
| [[MYH9]] | +0.68 | +0.67 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 861 |
| [[LAMC1]] | +0.67 | +0.56 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[PLEC]] | +0.66 | +0.68 / +0.66 | both halves | 7e-06 | pathway: Cell junction organization; STRING 812 |
| [[DCTN1]] | +0.66 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[DBN1]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 | STRING 612 |
| [[HAPSTR1]] | +0.64 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[DBNL]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ITPR3]] | +0.62 | +0.57 / +0.63 | both halves | 9e-06 | pathway: Platelet activation, signaling and aggregation |
| [[YWHAZ]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 | pathway: GP1b-IX-V activation signalling; STRING 538 |

## Genes that move opposite

*30 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | -0.67 | -0.58 / -0.67 | both halves | 8e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MC2]] | -0.62 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[MRPL23]] | -0.61 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[PIGBOS1]] | -0.60 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[CHCHD5]] | -0.60 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[WDR83OS]] ⚠ | -0.60 | -0.53 / -0.59 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS18C]] | -0.60 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[MRPS36]] ⚠ | -0.59 | -0.48 / -0.60 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[C15orf61]] ⚠ | -0.59 | -0.47 / -0.64 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LSM2]] | -0.59 | -0.41 / -0.71 | both halves | 4e-05 |  |
| [[SELENOH]] | -0.58 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[CHCHD1]] | -0.58 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[USP42]] | -0.57 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[PPIG]] | -0.57 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[YBEY]] | -0.57 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[TMEM258]] | -0.57 | -0.43 / -0.57 | both halves | 3e-05 | pathway: Cell junction organization |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD59]] | B | CD59 activity raises FLNA's level | lines that do not express CD59 (7) vs lines expressing it (43) | 2.53× lower at baseline in the lines without CD59 | 0.003 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[CTSZ]] | B | CTSZ activity raises FLNA's level | lines that do not express CTSZ (8) vs lines expressing it (42) | 1.60× lower at baseline in the lines without CTSZ | 0.018 | ⚠ within organs, on part of the lines; also absent: LRRK1, CAV2, PIWIL4; maybe low, not absent |
| [[VIM-AS1]] | B | VIM-AS1 activity raises FLNA's level | lines that do not express VIM-AS1 (6) vs lines expressing it (44) | 2.73× lower at baseline in the lines without VIM-AS1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000290876, SCHIP1, BLVRA; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers FLNA's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DBN1]] | C | DBN1 activity raises FLNA's level | lines that do not express DBN1 (3) vs lines expressing it (47) | 3.56× lower at baseline in the lines without DBN1 | 0.009 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: LTBP3, NUAK1, BLVRA; maybe low, not absent |
| [[PLEC]] | C | PLEC activity raises FLNA's level | lines that do not express PLEC (3) vs lines expressing it (47) | 4.31× lower at baseline in the lines without PLEC | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |
| [[ANXA2]] | C | ANXA2 activity raises FLNA's level | lines that do not express ANXA2 (4) vs lines expressing it (46) | 1.83× lower at baseline in the lines without ANXA2 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, RARG, NABP1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.2, -20.1); signed map (-7.9, 33.9). **Vector** length 152, 54.8% of its response variance represented; |z| ≥ 3 in 1,172 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *EPHB-mediated forward signaling* (reactome, mean cos +0.51 to 6); *Leishmania infection* (reactome, mean cos +0.53 to 8); *Parasitic Infection Pathways* (reactome, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +12.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +6.1 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +11.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +5.1 | -1.5 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +4.9 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.4 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +3.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +4.2 | +1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.9 | +1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +2.4 |
| fall | [[Verteporfin (drug)]] 5 µM |  | -6.0 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.2 | -0.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.1 | -1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.8 | -1.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.8 | -3.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.8 | -3.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -3.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | filamin A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,348,524-154,374,634 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ABP-280; previously FLN1, FLN, OPD2, OPD1 |
| Gene groups (HGNC) | Filamin family |
| Hallmark sets | ALLOGRAFT_REJECTION, EPITHELIAL_MESENCHYMAL_TRANSITION, MITOTIC_SPINDLE |
| Reactome | 16 pathways, smallest: GP1b-IX-V activation signalling; OAS antiviral response; Cell-extracellular matrix interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P21333](https://www.uniprot.org/uniprotkb/P21333) (Filamin-A):

> Promotes orthogonal branching of actin filaments and links actin filaments to membrane glycoproteins. Anchors various transmembrane proteins to the actin cytoskeleton and serves as a scaffold for a wide range of cytoplasmic signaling proteins. Interaction with FLNB may allow neuroblast migration from the ventricular zone into the cortical plate. Tethers cell surface-localized furin, modulates its rate of internalization and directs its intracellular trafficking (By similarity). Involved in …

**Summary**, from NCBI Gene [2316](https://www.ncbi.nlm.nih.gov/gene/2316):

> The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several syndromes, including periventricular nodular heterotopias (PVNH1, PVNH4), otopalatodigital syndromes …

**Accessions** — [HGNC:3754](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3754) · Entrez [2316](https://www.ncbi.nlm.nih.gov/gene/2316) · UniProt [P21333](https://www.uniprot.org/uniprotkb/P21333) · Ensembl [ENSG00000196924](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196924)

## Data

Gene col 12305: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12305); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12305, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12305]; `tensor/DDL_lfc|DDL_z.npy` [12305]; `embed/gene_vectors.npy` [12305]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12305 or target_col == 12305). Every well: [[FLNA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLNA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

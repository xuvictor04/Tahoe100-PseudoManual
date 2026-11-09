---
symbol: "CCNH"
type: "gene"
col: 5567
ensembl_id: "ENSG00000134480"
name: "cyclin H"
location: "5q14.3"
module: 179
arm: "+"
pooled_cpm: 131.24
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# CCNH

*cyclin H* — 5q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.62× (z +27.7, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.809× (z -6.1, q 5e-07, down in 26 of 48 measured lines) ⚠ transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.866× (z -5.9, q 1e-06, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (Hs 766T 0.377×, HCT15 0.342×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.379×; ⚠ toxic; cell-cycle shift, explains ~38% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HCT15 0.431×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYCP2L]] (+0.59, fdr 2e-05), [[TMEM161B-DT]] (+0.56, fdr 1e-05), [[TMED7-TICAM2]] (+0.52, fdr 3e-05); moves opposite to [[SOX9]] (-0.48, fdr 2e-05), [[FAM76A]] (-0.46, fdr 3e-04), [[LCOR]] (-0.46, fdr 4e-05).
> It sits in the **+** arm of [[Module 179]] (RHOA GTPase cycle).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5567.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.62×** | +27.7 | 0e+00 | 46/48 (SW480, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +14.2 | 2e-43 | 46/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +12.3 | 2e-32 | 40/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +10.6 | 5e-24 | 42/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +10.2 | 2e-22 | 37/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +9.9 | 3e-21 | 39/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +9.4 | 5e-19 | 38/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +9.2 | 2e-18 | 26/48 (AsPC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +9.1 | 7e-18 | 39/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +8.7 | 2e-16 | 36/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +8.4 | 3e-15 | 26/48 (NCI-H2347, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +8.2 | 1e-14 | 33/49 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +8.0 | 7e-14 | 33/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +7.5 | 3e-12 | 30/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +7.2 | 2e-11 | 37/45 (PANC-1, RKO, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +6.3 | 1e-08 | 27/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.51×** | +6.2 | 2e-08 | 32/49 (Panc 03.27, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +6.2 | 2e-08 | 26/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5567.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (Hs 766T 0.377×, HCT15 0.342×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.379×; ⚠ toxic; cell-cycle shift, explains ~38% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HCT15 0.431×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.809×** | -6.1 | 5e-07 | 26/48 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.866× | -5.9 | 1e-06 | 18/48 (SNU-1, Hs 766T, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.815×** | -5.7 | 2e-06 | 24/48 (NCI-H2347, A498, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | 0.887× | -3.5 | 0.074 | 9/48 (hTERT-HPNE, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.893× | -3.3 | 0.12 | 7/48 (A498, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5567. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 68.4 | 9 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.95× (z +11.5) | — |
| [[SW480 (line)]] | alt | 151 | 9 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.08× (z +23.1) | — |
| [[LS 180 (line)]] | wt | 125 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +14.7) | — |
| [[NCI-H460 (line)]] | wt | 160 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.72× (z +18.4) | — |
| [[HOP62 (line)]] | alt | 134 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +14.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 133 | 6 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.53× (z +13.1) | — |
| [[AsPC-1 (line)]] | alt | 138 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +17.2) | — |
| [[HS-578T (line)]] | alt | 95.1 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.15× (z +18.1) | — |
| [[PANC-1 (line)]] | alt | 112 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.47× (z +17.1) | — |
| [[C32 (line)]] | wt | 99.9 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.06× (z +16.9) | — |
| [[NCI-H23 (line)]] | alt | 142 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.02× (z +15.8) | — |
| [[RKO (line)]] | wt | 194 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.84× (z +14.6) | — |
| [[SNU-1 (line)]] | wt | 198 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.46× (z +14.1) | — |
| [[HCT15 (line)]] | alt | 232 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.33× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 87.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.62× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +9.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.379× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[NCI-H1792 (line)]] | alt | 88.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.41× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.11× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 126 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.32× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 111 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.54× (z +12.8) | — |
| [[HEC-1-A (line)]] | alt | 141 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.19× (z +14.2) | [[Lonafarnib (drug)]] 5 µM 0.367× (z -9.5) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 167 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.48× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 207 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.21× (z +18.5) | — |
| [[LOX-IMVI (line)]] | wt | 105 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +14.3) | — |
| [[Panc 03.27 (line)]] | alt | 90.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +11.2) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.85× (z +10.6) | — |
| [[SK-MEL-2 (line)]] | alt | 119 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.51× (z +14.8) | — |
| [[SW 900 (line)]] | alt | 194 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.88× (z +17.8) | — |
| [[SW48 (line)]] | wt | 174 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.87× (z +12.3) | — |
| [[A-427 (line)]] | wt | 123 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.04× (z +9.6) | — |
| [[A498 (line)]] | wt | 129 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.07× (z +10.0) | — |
| [[A549 (line)]] | wt | 85.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.88× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | — |
| [[COLO 205 (line)]] | alt | 143 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.34× (z +9.6) | — |
| [[H4 (line)]] | wt | 131 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.69× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 143 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.78× (z +13.5) | — |
| [[hTERT-HPNE (line)]] | wt | 127 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.11× (z +11.7) | — |
| [[J82 (line)]] | alt | 131 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.36× (z +12.2) | — |
| [[KATO III (line)]] | alt | 102 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.00× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 100 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.26× (z +17.4) | — |
| [[NCI-H2347 (line)]] | alt | 110 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.70× (z +15.1) | — |
| [[RPMI-7951 (line)]] | alt | 137 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.25× (z +13.1) | — |
| [[SNU-423 (line)]] | alt | 143 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.15× (z +10.5) | — |
| [[SW1417 (line)]] | alt | 62.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.11× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 150 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 171 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 176 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 294 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5567), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYCP2L]] | +0.59 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[TMEM161B-DT]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[TMED7-TICAM2]] | +0.52 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[CDC26]] | +0.50 | +0.38 / +0.47 | both halves | 6e-05 | pathway: S Phase |
| [[XPNPEP3]] | +0.50 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[FKBP11]] | +0.50 | +0.56 / +0.32 | both halves | 2e-04 |  |
| [[HDAC8]] | +0.50 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[APRG1]] | +0.49 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[LINC03009-1]] | +0.48 | +0.28 / +0.51 | both halves | 3e-04 |  |
| [[ATM]] | +0.48 | +0.49 / +0.47 | both halves | 2e-05 | pathway: TP53 Regulates Transcription of DNA Repair Genes; STRING 642 |
| [[ZNF814]] | +0.48 | +0.34 / +0.52 | both halves | 1e-04 |  |
| [[RPL34-DT]] | +0.47 | +0.37 / +0.49 | both halves | 7e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOX9]] | -0.48 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[FAM76A]] | -0.46 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[LCOR]] | -0.46 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[PTP4A3]] | -0.45 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[HIRIP3]] | -0.44 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[PRR14]] | -0.42 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[DYNC2I2]] | -0.42 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[USP43]] | -0.42 | -0.29 / -0.41 | both halves | 2e-04 |  |
| [[ZNF624]] | -0.41 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[ARHGAP23]] | -0.41 | -0.42 / -0.37 | both halves | 7e-05 |  |
| [[PRXL2B]] | -0.41 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[SFR1]] | -0.40 | -0.36 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **+** arm (projection on the module's main direction 0.470). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (24.3, -21.5); signed map (7.1, 5.1). **Vector** length 94.0, 24.3% of its response variance represented; |z| ≥ 3 in 1,376 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.7 | +27.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.8 | +8.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.8 | +9.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +3.4 | +8.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.3 | +10.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.0 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +2.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +2.4 | +1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | +9.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | +2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -0.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.8 | -5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -5.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.1 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | cyclin H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.3 — chr5:87,318,416-87,413,029 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p34, p37, CycH |
| Gene groups (HGNC) | Cyclins; CDK activating kinase complex |
| Reactome | 55 pathways, smallest: RNA Pol II CTD phosphorylation and interaction with CE during HIV infection; RNA Pol II CTD phosphorylation and interaction with CE; mRNA Capping |
| Matched by | ensembl_id |

**Function**, from UniProt [P51946](https://www.uniprot.org/uniprotkb/P51946) (Cyclin-H):

> Component of the CDK-activating kinase (CAK) complex, a master regulator of CDK activity by catalyzing the activating threonine phosphorylation of CDKs. Binds and activates cyclin-dependent protein kinase CDK7, the catalytic subunit of CAK. CAK activates major mediators of cell cycle control, including CDK1, CDK2, CDK4 and CDK6, and plays a key role in regulating cell cycle progression. CAK complexed to the core-TFIIH basal transcription factor activates RNA polymerase II by serine …

**Summary**, from NCBI Gene [902](https://www.ncbi.nlm.nih.gov/gene/902):

> The protein encoded by this gene belongs to the highly conserved cyclin family, whose members are characterized by a dramatic periodicity in protein abundance through the cell cycle. Cyclins function as regulators of CDK kinases. Different cyclins exhibit distinct expression and degradation patterns which contribute to the temporal coordination of each mitotic event. This cyclin forms a complex with CDK7 kinase and ring finger protein MAT1. The kinase complex is able to phosphorylate CDK2 and …

**Accessions** — [HGNC:1594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1594) · Entrez [902](https://www.ncbi.nlm.nih.gov/gene/902) · UniProt [P51946](https://www.uniprot.org/uniprotkb/P51946) · Ensembl [ENSG00000134480](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134480)

## Data

Gene col 5567: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5567); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5567, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5567]; `tensor/DDL_lfc|DDL_z.npy` [5567]; `embed/gene_vectors.npy` [5567]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5567 or target_col == 5567). Every well: [[CCNH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

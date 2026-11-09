---
symbol: "KLHL11"
type: "gene"
col: 10933
ensembl_id: "ENSG00000178502"
name: "kelch like family member 11"
location: "17q21.2"
module: 153
arm: "+"
pooled_cpm: 22.5
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# KLHL11

*kelch like family member 11* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.95× (z +11.5, q 7e-28, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.513× (z -8.2, q 2e-13, down in 31 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Gallic acid (hydrate) (drug)]] 0.05 µM: 0.754× (z -3.5, q 0.100, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H2030 0.207×, C32 0.129×, LOX-IMVI 0.214×, RPMI-7951 0.123×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (J82 0.0813×, A549 0.186×, HS-578T 0.186×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 0.168×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Tofacitinib (citrate) (drug)]] 0.5 µM in 1 line (CHP-212 0.0608×); [[Tadalafil (drug)]] 0.05 µM in 1 line (AN3 CA 0.0719×); [[DT-061 (drug)]] 5 µM in 1 line (SHP-77 0.0654×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIPC]] (+0.62, fdr 4e-05), [[USF1]] (+0.62, fdr 4e-05), [[POMK]] (+0.61, fdr 7e-06); moves opposite to [[ABAT]] (-0.60, fdr 3e-05), [[DAP3]] (-0.51, fdr 2e-05), [[GOLGA6L9]] (-0.50, fdr 9e-05).
> It is in [[Module 153]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10933.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +11.5 | 7e-28 | 43/47 (NCI-H23, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +11.5 | 7e-28 | 41/48 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.22×** | +9.7 | 9e-20 | 42/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.00×** | +8.4 | 8e-15 | 41/48 (AsPC-1, NCI-H460, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.98×** | +8.3 | 1e-14 | 40/47 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.83×** | +7.3 | 2e-11 | 40/47 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +7.2 | 7e-11 | 37/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.07×** | +7.1 | 8e-11 | 38/48 (SW480, SW48, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +7.0 | 1e-10 | 33/45 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +6.8 | 5e-10 | 34/48 (A549, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.68×** | +6.3 | 1e-08 | 37/48 (NCI-H460, HT-29, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.56×** | +5.9 | 1e-07 | 26/47 (NCI-H2030, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +5.9 | 2e-07 | 7/48 (NCI-H2030, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +5.6 | 8e-07 | 33/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +5.1 | 1e-05 | 32/47 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +5.1 | 1e-05 | 28/47 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +4.9 | 3e-05 | 28/48 (SW48, RKO, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.41×** | +4.2 | 1e-03 | 20/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.001 | 20/48 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.019 | 17/48 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Erlotinib (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.062 | 12/47 (SK-MEL-2, COLO 205, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10933.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H2030 0.207×, C32 0.129×, LOX-IMVI 0.214×, RPMI-7951 0.123×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (J82 0.0813×, A549 0.186×, HS-578T 0.186×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 0.168×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Tofacitinib (citrate) (drug)]] 0.5 µM in 1 line (CHP-212 0.0608×); [[Tadalafil (drug)]] 0.05 µM in 1 line (AN3 CA 0.0719×); [[DT-061 (drug)]] 5 µM in 1 line (SHP-77 0.0654×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.513×** | -8.2 | 2e-13 | 31/44 (NCI-H2030, C32, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.600×** | -6.0 | 6e-07 | 22/35 (J82, A549, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.754×** | -3.5 | 0.100 | 18/48 (KATO III, A549, …) | inconsistent across doses | position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | 0.832× | -3.2 | 0.19 | 16/48 (CFPAC-1, HCT15, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.842× | -3.0 | 0.30 | 16/48 (RPMI-7951, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10933. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 27.2 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.62× (z +11.1) | — |
| [[A-172 (line)]] | wt | 18.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 28.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -9.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 20.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.186× (z -10.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 48.3 | 0 | 2 (1 ⚠) | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0608× (z -10.7) |
| [[HT-29 (line)]] | alt | 17.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +9.6) | — |
| [[KATO III (line)]] | alt | 27.3 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.98× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 22.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -9.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 36.8 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0719× (z -9.4) |
| [[BT-474 (line)]] | alt | 19.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +8.5) | — |
| [[C32 (line)]] | wt | 14.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -10.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 25.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 15.1 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.135× (z -8.6) |
| [[HS-578T (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -9.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0813× (z -14.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 54.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 30.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +12.1) | — |
| [[Panc 03.27 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -9.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -9.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 25.5 | 0 | 1 | — | [[DT-061 (drug)]] 5 µM 0.0654× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -9.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10933), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIPC]] | +0.62 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[USF1]] | +0.62 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[POMK]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[SF3B4]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[MBLAC2]] | +0.59 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[TSPYL1]] | +0.59 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[LDB1]] | +0.57 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[ZBTB39]] | +0.57 | +0.49 / +0.63 | both halves | 1e-05 | same gene group |
| [[PPP1R8]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[PTPN18]] | +0.56 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ZFP62]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[UNC119B]] | +0.55 | +0.48 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABAT]] | -0.60 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[DAP3]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[GOLGA6L9]] | -0.50 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[SAMD4B]] | -0.49 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[TALAM1]] | -0.49 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[PI4KA]] | -0.49 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[ACAP2]] | -0.49 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[LRRC75A]] | -0.47 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[TMEM41B]] | -0.47 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[UBE2B]] | -0.47 | -0.39 / -0.43 | both halves | 5e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[THOC2]] | -0.47 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[SPAG9]] | -0.46 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KLHL11's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TPST1]] | B | TPST1 activity raises KLHL11's level | lines that do not express TPST1 (5) vs lines expressing it (45) | 1.37× lower at baseline in the lines without TPST1 | 0.063 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CYP46A1, CSRP2, MYO5A |
| [[LINC01232]] | B | LINC01232 activity lowers KLHL11's level | lines that do not express LINC01232 (11) vs lines expressing it (39) | 1.50× higher at baseline in the lines without LINC01232 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000286856, SERPINB1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.507). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-30.0, 19.1); signed map (-10.5, -36.2). **Vector** length 74.2, 15.6% of its response variance represented; |z| ≥ 3 in 1,064 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.1 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +11.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.7 | +6.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +5.3 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Erlotinib (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +2.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.7 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | +0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | +1.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.4 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:41,848,518-41,865,423 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10572 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVR0](https://www.uniprot.org/uniprotkb/Q9NVR0) (Kelch-like protein 11):

> Component of a cullin-RING-based BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complex that mediates the ubiquitination of target proteins, leading most often to their proteasomal degradation.

**Summary**, from NCBI Gene [55175](https://www.ncbi.nlm.nih.gov/gene/55175):

> Predicted to enable ubiquitin-like ligase-substrate adaptor activity. Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process. Predicted to be located in cytosol. Predicted to be part of Cul3-RING ubiquitin ligase complex. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19008](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19008) · Entrez [55175](https://www.ncbi.nlm.nih.gov/gene/55175) · UniProt [Q9NVR0](https://www.uniprot.org/uniprotkb/Q9NVR0) · Ensembl [ENSG00000178502](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178502)

## Data

Gene col 10933: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10933); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10933, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10933]; `tensor/DDL_lfc|DDL_z.npy` [10933]; `embed/gene_vectors.npy` [10933]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10933 or target_col == 10933). Every well: [[KLHL11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

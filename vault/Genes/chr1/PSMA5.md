---
symbol: "PSMA5"
type: "gene"
col: 6677
ensembl_id: "ENSG00000143106"
name: "proteasome 20S subunit alpha 5"
location: "1p13.3"
module: 64
arm: "+"
pooled_cpm: 52.92
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# PSMA5

*proteasome 20S subunit alpha 5* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (18 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.67× (z +21.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.815× (z -4.5, q 0.005, down in 20 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (Panc 03.27 0.136×, LOX-IMVI 0.0885×, Hs 766T 0.256×, NCI-H23 0.370×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.185×, RKO 0.426×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 0.320×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMB6]] (+0.68, fdr 8e-06), [[PSMB5]] (+0.64, fdr 1e-05), [[PSMD3]] (+0.63, fdr 1e-05); moves opposite to [[ARHGAP12]] (-0.48, fdr 3e-05), [[KAT2B]] (-0.47, fdr 5e-05), [[SNX30]] (-0.45, fdr 4e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 22 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6677.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.67×** | +21.3 | 0e+00 | 47/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.57×** | +20.5 | 0e+00 | 48/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.53×** | +17.8 | 0e+00 | 47/48 (NCI-H1792, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.78×** | +12.4 | 2e-33 | 43/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +11.3 | 3e-27 | 39/48 (SK-MEL-2, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +11.1 | 9e-27 | 40/47 (NCI-H23, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.66×** | +10.9 | 1e-25 | 40/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.65×** | +10.8 | 3e-25 | 40/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +10.2 | 1e-22 | 34/48 (SNU-423, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +8.3 | 5e-15 | 34/48 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.31×** | +8.1 | 2e-14 | 32/47 (MIA PaCa-2, NCI-H2347, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.47×** | +8.1 | 4e-14 | 34/46 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.44×** | +7.9 | 9e-14 | 33/48 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +7.8 | 2e-13 | 34/48 (SNU-423, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.39×** | +7.1 | 4e-11 | 30/48 (NCI-H23, SNU-423, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.57×** | +6.9 | 2e-10 | 35/48 (NCI-H1573, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +6.0 | 6e-08 | 20/48 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +4.6 | 8e-05 | 23/48 (C32, AsPC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.6 | 0.005 | 14/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.020 | 10/48 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.022 | 7/47 (Hs 766T, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.022 | 7/48 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.046 | 13/48 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6677.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (Panc 03.27 0.136×, LOX-IMVI 0.0885×, Hs 766T 0.256×, NCI-H23 0.370×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.185×, RKO 0.426×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 0.320×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.815×** | -4.5 | 0.005 | 20/48 (KATO III, BT-474, …) | all doses, flat |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.833×** | -4.0 | 0.018 | 21/48 (C32, A498, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.858× | -3.4 | 0.14 | 14/48 (KATO III, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6677. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 54.9 | 6 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.42× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 36.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +13.6) | — |
| [[SK-MEL-2 (line)]] | alt | 98.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 23.0 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.40× (z +11.8) | — |
| [[LOX-IMVI (line)]] | wt | 27.1 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.37× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.0885× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 40.5 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.63× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 133 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.40× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.370× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 48.6 | 3 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.35× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 42.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.69× (z +10.6) | — |
| [[COLO 205 (line)]] | alt | 34.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.61× (z +11.9) | — |
| [[HEC-1-A (line)]] | alt | 34.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.43× (z +12.2) | — |
| [[HT-29 (line)]] | alt | 60.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.72× (z +10.2) | — |
| [[LoVo (line)]] | wt | 59.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.52× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 58.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.74× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 53.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.65× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 40.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.69× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 36.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.74× (z +15.0) | — |
| [[PANC-1 (line)]] | alt | 42.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.68× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 37.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +16.5) | — |
| [[A-172 (line)]] | wt | 52.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.81× (z +11.3) | — |
| [[A-427 (line)]] | wt | 42.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.98× (z +10.1) | — |
| [[A549 (line)]] | wt | 35.4 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.45× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 50.6 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.55× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 67.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.256× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 53.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.94× (z +9.5) | — |
| [[KATO III (line)]] | alt | 62.2 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.57× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.320× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[MIA PaCa-2 (line)]] | alt | 53.8 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.67× (z +9.6) | — |
| [[RKO (line)]] | wt | 87.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 37.0 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.67× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 32.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.8) | — |
| [[H4 (line)]] | wt | 58.3 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.04× (z +8.7) | — |
| [[SW48 (line)]] | wt | 51.6 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0946× (z -8.7) ⚠ toxic |
| [[A498 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6677), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMB6]] | +0.68 | +0.72 / +0.58 | both halves | 8e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMB5]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMD3]] | +0.63 | +0.72 / +0.56 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMA4]] | +0.60 | +0.67 / +0.58 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMB3]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[KEAP1]] | +0.59 | +0.52 / +0.58 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 566 |
| [[PHF5A]] | +0.59 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[PSMD13]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[FLAD1]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[PSMC4]] | +0.57 | +0.62 / +0.49 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMA3]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[TRMT2A]] | +0.57 | +0.45 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP12]] | -0.48 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[KAT2B]] | -0.47 | -0.41 / -0.39 | both halves | 5e-05 | pathway: Deubiquitination |
| [[SNX30]] | -0.45 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[SUN2]] | -0.45 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[TMSB4X]] | -0.45 | -0.41 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PSMA5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.418). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-43.0, -4.0); signed map (-24.4, -24.6). **Vector** length 86.8, 21.4% of its response variance represented; |z| ≥ 3 in 1,170 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.2 | +17.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.6 | +20.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.1 | +21.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.1 | +5.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.0 | +6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +6.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +3.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.5 | +1.8 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.2 | -4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.3 | -0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.4 | -2.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.8 | -1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 20S subunit alpha 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:109,399,042-109,426,448 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZETA |
| Gene groups (HGNC) | Proteasome |
| Reactome | 171 pathways, smallest: Antigen processing: Ub, ATP-independent proteasomal degradation; Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC) |
| Matched by | ensembl_id |

**Function**, from UniProt [P28066](https://www.uniprot.org/uniprotkb/P28066) (Proteasome subunit alpha type-5):

> Component of the 20S core proteasome complex involved in the proteolytic degradation of most intracellular proteins. This complex plays numerous essential roles within the cell by associating with different regulatory particles. Associated with two 19S regulatory particles, forms the 26S proteasome and thus participates in the ATP-dependent degradation of ubiquitinated proteins. The 26S proteasome plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged …

**Summary**, from NCBI Gene [5686](https://www.ncbi.nlm.nih.gov/gene/5686):

> The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent process in a non-lysosomal pathway. An essential function of a modified proteasome, the …

**Accessions** — [HGNC:9534](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9534) · Entrez [5686](https://www.ncbi.nlm.nih.gov/gene/5686) · UniProt [P28066](https://www.uniprot.org/uniprotkb/P28066) · Ensembl [ENSG00000143106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143106)

## Data

Gene col 6677: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6677); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6677, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6677]; `tensor/DDL_lfc|DDL_z.npy` [6677]; `embed/gene_vectors.npy` [6677]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6677 or target_col == 6677). Every well: [[PSMA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "TCFL5"
type: "gene"
col: 2090
ensembl_id: "ENSG00000101190"
name: "transcription factor like 5"
location: "20q13.33"
module: 2
arm: "+"
pooled_cpm: 20.62
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 12
n_dd_up_clean: 18
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TCFL5

*transcription factor like 5* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.36× (z +13.9, q 3e-41, up in 35 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.01× (z +11.3, q 2e-27, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.571× (z -9.1, q 6e-17, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (76 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GATD1]] (+0.55, fdr 1e-05), [[CARM1]] (+0.53, fdr 1e-04), [[ZNF891]] (+0.52, fdr 2e-04); moves opposite to [[THRB]] (-0.44, fdr 3e-04), [[GSTP1]] (-0.44, fdr 9e-04, ⚠ not reproduced), [[NSUN3]] (-0.43, fdr 5e-04), [[SELENOK]] (-0.42, fdr 2e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PARD6G]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2090.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.36×** | +13.9 | 3e-41 | 35/42 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +13.3 | 5e-38 | 22/30 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.01×** | +11.3 | 2e-27 | 38/48 (Hs 766T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.92×** | +10.6 | 7e-24 | 37/48 (KATO III, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +9.5 | 2e-19 | 34/47 (KATO III, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +8.1 | 4e-14 | 29/48 (SHP-77, SW1417, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.63×** | +7.4 | 2e-11 | 24/40 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +6.9 | 4e-10 | 30/47 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +6.8 | 5e-10 | 28/44 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.44×** | +5.9 | 2e-07 | 28/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +5.9 | 2e-07 | 26/48 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.38×** | +5.3 | 6e-06 | 21/47 (LOX-IMVI, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +5.2 | 8e-06 | 23/48 (SW480, C32, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.70×** | +4.5 | 3e-04 | 14/48 (Hs 766T, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.30×** | +4.3 | 7e-04 | 20/48 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.004 | 14/48 (NCI-H1792, LOX-IMVI, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.005 | 13/48 (NCI-H1792, SK-MEL-2, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.017 | 8/45 (LoVo, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.046 | 7/45 (SHP-77, AN3 CA, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.058 | 11/47 (NCI-H460, SW48, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2090.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.571×** | -9.1 | 6e-17 | 31/48 (LOX-IMVI, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.648×** | -7.0 | 6e-10 | 26/47 (SNU-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.652×** | -6.9 | 8e-10 | 28/46 (LOX-IMVI, HCT15, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.670×** | -6.5 | 1e-08 | 24/47 (C-33 A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.706×** | -5.6 | 2e-06 | 26/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.728×** | -5.1 | 3e-05 | 24/47 (LOX-IMVI, A-427, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.567×** | -4.8 | 1e-04 | 21/48 (SW480, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.578×** | -4.6 | 2e-04 | 17/46 (SW480, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.750×** | -4.4 | 7e-04 | 18/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.830×** | -4.3 | 0.001 | 21/47 (SNU-1, RKO, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.775×** | -4.1 | 0.002 | 21/47 (LOX-IMVI, A-172, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.814×** | -3.3 | 0.041 | 7/48 (KATO III, SHP-77, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2090. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 24.1 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -15.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -9.8) |
| [[A498 (line)]] | wt | 16.9 | 3 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +9.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.91× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 37.0 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +9.3) | — |
| [[KATO III (line)]] | alt | 19.3 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.68× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.68× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 32.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.45× (z +9.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -15.4) ⚠ cell-cycle shift, explains ~59% of this change |
| [[NCI-H460 (line)]] | wt | 17.2 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.243× (z -11.3) ⚠ cell-cycle shift, explains ~48% of this change |
| [[PANC-1 (line)]] | alt | 23.9 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.27× (z +11.0) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[SNU-1 (line)]] | wt | 28.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -16.1) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.129× (z -10.6) |
| [[A-427 (line)]] | wt | 34.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -10.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HEC-1-A (line)]] | alt | 18.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.06× (z +11.9) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 20.8 | 0 | 1 | — | [[Bendamustine (drug)]] 0.05 µM 0.130× (z -9.1) |
| [[HOP62 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -9.8) ⚠ cell-cycle shift, explains ~61% of this change |
| [[NCI-H23 (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -10.4) ⚠ cell-cycle shift, explains ~61% of this change |
| [[NCI-H2347 (line)]] | alt | 9.95 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 38.4 | 0 | 1 | — | [[Vitamin K4 (drug)]] 0.5 µM 0.0742× (z -8.6) |
| [[RKO (line)]] | wt | 24.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -13.7) ⚠ cell-cycle shift, explains ~61% of this change |
| [[RPMI-7951 (line)]] | alt | 17.0 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.184× (z -8.7) |
| [[SW1417 (line)]] | alt | 32.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 15.6 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0921× (z -9.3) |
| [[A-172 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2090), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 21 of them with an alert (⚠; 21 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATD1]] | +0.55 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[CARM1]] | +0.53 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[ZNF891]] | +0.52 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[CPSF6]] | +0.50 | +0.28 / +0.45 | both halves | 3e-04 |  |
| [[PACS2]] | +0.50 | +0.49 / +0.30 | both halves | 2e-04 |  |
| [[PCBP4]] | +0.49 | +0.41 / +0.40 | both halves | 5e-05 |  |
| [[PGAP6]] | +0.48 | +0.45 / +0.37 | both halves | 7e-05 |  |
| [[ANKRD52]] | +0.48 | +0.24 / +0.43 | both halves | 4e-04 |  |
| [[NCK2]] | +0.48 | +0.26 / +0.37 | both halves | 4e-04 |  |
| [[GNAZ]] | +0.48 | +0.30 / +0.48 | both halves | 2e-04 |  |
| [[CSK]] | +0.47 | +0.30 / +0.34 | both halves | 2e-04 |  |
| [[PPP1R12C]] | +0.47 | +0.19 / +0.52 | ⚠ one half (not replicated) | 8e-04 |  |
| [[LRP3]] | +0.47 | +0.36 / +0.50 | both halves | 1e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THRB]] | -0.44 | -0.28 / -0.37 | both halves | 3e-04 |  |
| [[GSTP1]] | -0.44 | -0.19 / -0.44 | ⚠ not reproduced | 9e-04 |  |
| [[NSUN3]] | -0.43 | -0.29 / -0.24 | both halves | 5e-04 |  |
| [[PUS10]] | -0.42 | -0.13 / -0.41 | ⚠ not reproduced | 0.002 |  |
| [[SELENOK]] | -0.42 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[KBTBD4]] | -0.42 | -0.19 / -0.38 | ⚠ not reproduced | 8e-04 |  |
| [[PSMB10]] | -0.41 | -0.27 / -0.33 | both halves | 3e-04 |  |
| [[GPATCH1]] | -0.41 | -0.23 / -0.35 | both halves | 5e-04 |  |
| [[SYNJ1]] | -0.40 | -0.24 / -0.39 | both halves | 4e-04 |  |
| [[RNASEL]] | -0.40 | -0.38 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARD6G]] | B | PARD6G activity raises TCFL5's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without PARD6G | 0.022 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent |
| [[THRB]] | B | THRB activity lowers TCFL5's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.55× higher at baseline in the lines without THRB | 0.022 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[GNAZ]] | B | GNAZ activity raises TCFL5's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.61× lower at baseline in the lines without GNAZ | 0.030 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[NCS1]] | B | NCS1 activity raises TCFL5's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 1.63× lower at baseline in the lines without NCS1 | 0.070 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[USP31]] | C | USP31 activity raises TCFL5's level | lines that do not express USP31 (3) vs lines expressing it (47) | 2.16× lower at baseline in the lines without USP31 | 0.070 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.413). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-5.7, -24.5); signed map (-40.7, -27.8). **Vector** length 63.1, 10.6% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.3 | +8.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.2 | +6.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +3.0 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.6 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | -0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | -0.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.3 | +0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.3 | -0.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -4.5 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | +2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -3.1 | +2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.3 | +2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -5.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.3 | -0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -3.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.1 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor like 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:62,841,005-62,861,822 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Figlb, E2BP-1, CHA, bHLHe82 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UL49](https://www.uniprot.org/uniprotkb/Q9UL49) (Transcription factor-like 5 protein):

> Putative transcription factor. Isoform 3 may play a role in early spermatogenesis.

**Summary**, from NCBI Gene [10732](https://www.ncbi.nlm.nih.gov/gene/10732):

> Enables DNA-binding transcription repressor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Involved in several processes, including negative regulation of transcription by RNA polymerase II; regulation of cell population proliferation; and spermatogenesis. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11646](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11646) · Entrez [10732](https://www.ncbi.nlm.nih.gov/gene/10732) · UniProt [Q9UL49](https://www.uniprot.org/uniprotkb/Q9UL49) · Ensembl [ENSG00000101190](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101190)

## Data

Gene col 2090: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2090); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2090, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2090]; `tensor/DDL_lfc|DDL_z.npy` [2090]; `embed/gene_vectors.npy` [2090]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2090 or target_col == 2090). Every well: [[TCFL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCFL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

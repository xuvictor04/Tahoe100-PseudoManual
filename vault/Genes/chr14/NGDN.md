---
symbol: "NGDN"
type: "gene"
col: 4973
ensembl_id: "ENSG00000129460"
name: "neuroguidin"
location: "14q11.2"
module: 118
arm: "+"
pooled_cpm: 31.9
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 4
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# NGDN

*neuroguidin* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (15 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.99× (z +12.5, q 6e-33, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.438× (z -14.5, q 8e-45, down in 30 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Brivudine (drug)]] 5 µM: 0.614× (z -4.7, q 6e-04, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (SW1417 0.148×, LOX-IMVI 0.0933×, NCI-H2030 0.192×, C32 0.0891×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H23 0.202×, SHP-77 0.193×, C-33 A 0.129×, NCI-H2347 0.279×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.172×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 900 0.249×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A17]] (+0.72, fdr 1e-05), [[ALKBH4]] (+0.71, fdr 1e-05), [[COA6]] (+0.71, fdr 3e-05); moves opposite to [[SSX2IP]] (-0.62, fdr 3e-05), [[LBR]] (-0.60, fdr 3e-05), [[IDH3A]] (-0.59, fdr 4e-05).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HOOK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4973.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.99×** | +12.5 | 6e-33 | 43/48 (NCI-H23, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.94×** | +12.0 | 8e-31 | 45/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +10.2 | 2e-22 | 34/48 (BT-474, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +10.2 | 4e-22 | 38/46 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.89×** | +10.1 | 6e-22 | 41/48 (LoVo, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.70×** | +9.7 | 3e-20 | 42/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +9.5 | 3e-19 | 39/48 (CFPAC-1, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +8.8 | 1e-16 | 36/47 (NCI-H1573, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +8.7 | 1e-16 | 39/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.38×** | +8.3 | 8e-15 | 35/48 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.55×** | +8.0 | 7e-14 | 38/48 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.33×** | +7.4 | 7e-12 | 29/47 (NCI-H1573, A498, …) | two highest doses | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +7.0 | 1e-10 | 29/48 (BT-474, SW1417, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.47×** | +7.0 | 1e-10 | 30/47 (LoVo, SW480, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.89×** | +6.0 | 6e-08 | 23/34 (NCI-H2030, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.56×** | +5.8 | 3e-07 | 28/48 (PANC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 3e-04 | 19/48 (Panc 03.27, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.012 | 10/48 (A498, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.022 | 11/48 (Hs 766T, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.022 | 11/47 (CHP-212, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4973.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (SW1417 0.148×, LOX-IMVI 0.0933×, NCI-H2030 0.192×, C32 0.0891×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H23 0.202×, SHP-77 0.193×, C-33 A 0.129×, NCI-H2347 0.279×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.172×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 900 0.249×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.438×** | -14.5 | 8e-45 | 30/39 (SW1417, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.550×** | -10.9 | 2e-25 | 35/45 (NCI-H23, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.614×** | -4.7 | 6e-04 | 22/48 (NCI-H23, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.778×** | -4.0 | 0.007 | 17/48 (PANC-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.869× | -3.7 | 0.029 | 14/48 (CFPAC-1, SW1417, …) | rises with dose |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.836× | -3.1 | 0.17 | 4/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 0.889× | -3.1 | 0.18 | 1/48 (RPMI-7951) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4973. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 29.1 | 6 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.23× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.20× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 28.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -12.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 31.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.81× (z +8.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 2.64× (z +8.6) | [[AZD2858 (drug)]] 0.5 µM 0.257× (z -8.6) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 42.7 | 3 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.29× (z +11.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.42× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 77.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[NCI-H23 (line)]] | alt | 46.1 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.86× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -15.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 26.4 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.50× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -12.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 32.0 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.68× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 53.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +11.0) | — |
| [[C-33 A (line)]] | alt | 39.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 42.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -13.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 47.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -14.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 25.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.249× (z -9.1) |
| [[SW1417 (line)]] | alt | 41.1 | 1 | 1 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.06× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.148× (z -17.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 33.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0891× (z -15.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -10.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 35.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -11.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -12.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -8.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0933× (z -16.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 33.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 30.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.5) | — |
| [[A-172 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4973), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A17]] | +0.72 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[ALKBH4]] | +0.71 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[COA6]] | +0.71 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[TEFM]] | +0.69 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[IGBP1]] | +0.69 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[GPATCH3]] | +0.69 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[TMEM101]] | +0.68 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[SCNM1]] | +0.68 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[CCDC12]] | +0.67 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[TTF1]] | +0.67 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[MRPL32]] | +0.66 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[NOXRED1]] | +0.66 | +0.58 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSX2IP]] | -0.62 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[LBR]] | -0.60 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[IDH3A]] | -0.59 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[AKAP11]] | -0.59 | -0.39 / -0.65 | both halves | 5e-05 |  |
| [[DIAPH1]] | -0.58 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[UXS1]] | -0.57 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[DNAJC10]] | -0.57 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[PRKACA]] | -0.57 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[BCAP29]] | -0.57 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[NAB1]] | -0.57 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[EFR3A]] | -0.56 | -0.36 / -0.61 | both halves | 1e-04 |  |
| [[EPB41L2]] | -0.56 | -0.60 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOOK1]] | B | HOOK1 activity raises NGDN's level | lines that do not express HOOK1 (22) vs lines expressing it (28) | 1.20× lower at baseline in the lines without HOOK1 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.786). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-45.2, 9.0); signed map (-5.9, -5.4). **Vector** length 90.9, 22.0% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.8 | +9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.1 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +12.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.4 | +12.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.2 | +8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +9.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +8.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +1.9 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.8 | -14.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.8 | -10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -4.9 | +3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.2 | -4.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | -3.9 | +5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.5 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[Berbamine (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.2 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | neuroguidin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:23,469,679-23,509,862 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564O092, LCP5, lpd-2, NGD, CANu1; previously C14orf120 |
| Gene groups (HGNC) | SSU processome |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEJ9](https://www.uniprot.org/uniprotkb/Q8NEJ9) (Neuroguidin):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome. Its dissociation from the complex determines the transition from …

**Summary**, from NCBI Gene [25983](https://www.ncbi.nlm.nih.gov/gene/25983):

> Neuroguidin is an EIF4E (MIM 133440)-binding protein that interacts with CPEB (MIM 607342) and functions as a translational regulatory protein during development of the vertebrate nervous system (Jung et al., 2006 [PubMed 16705177]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:20271](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20271) · Entrez [25983](https://www.ncbi.nlm.nih.gov/gene/25983) · UniProt [Q8NEJ9](https://www.uniprot.org/uniprotkb/Q8NEJ9) · Ensembl [ENSG00000129460](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129460)

## Data

Gene col 4973: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4973); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4973, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4973]; `tensor/DDL_lfc|DDL_z.npy` [4973]; `embed/gene_vectors.npy` [4973]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4973 or target_col == 4973). Every well: [[NGDN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NGDN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

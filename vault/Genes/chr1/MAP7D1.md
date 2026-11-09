---
symbol: "MAP7D1"
type: "gene"
col: 3850
ensembl_id: "ENSG00000116871"
name: "MAP7 domain containing 1"
location: "1p34.3"
module: 96
arm: "+"
pooled_cpm: 41.6
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# MAP7D1

*MAP7 domain containing 1* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (22 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.42× (z +22.2, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Anethole trithione (drug)]] 5 µM: 0.805× (z -5.5, q 3e-05, down in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~13% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 1 line (LOX-IMVI 0.0792×; ⚠ toxic); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.138×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFE3]] (+0.59, fdr 1e-05), [[DCTN2]] (+0.56, fdr 1e-05), [[CDV3]] (+0.56, fdr 1e-05); moves opposite to [[CNOT2]] (-0.54, fdr 1e-05), [[SHQ1]] (-0.50, fdr 1e-05), [[ARMC10]] (-0.50, fdr 3e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HEG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 23 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3850.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.42×** | +22.2 | 0e+00 | 45/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.48×** | +15.6 | 0e+00 | 45/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Peretinoin (drug)]] 0.5 µM | ⚠ position correction uncertain | **2.22×** | +14.2 | 1e-43 | 47/47 (NCI-H1573, HT-29, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.16×** | +13.7 | 1e-40 | 43/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.00×** | +12.3 | 9e-33 | 43/48 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Peretinoin (drug)]] 0.05 µM | ⚠ position correction uncertain | **2.08×** | +12.0 | 2e-31 | 48/48 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM | ⚠ position correction uncertain | **1.93×** | +11.2 | 2e-27 | 44/47 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.82×** | +10.7 | 1e-24 | 32/46 (SW480, NCI-H23, …) | all doses, flat | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +8.4 | 4e-15 | 38/48 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +8.2 | 9e-15 | 38/48 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.55×** | +7.5 | 3e-12 | 22/36 (NCI-H460, RPMI-7951, …) | all doses, flat | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +7.3 | 1e-11 | 36/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Minodronic acid (drug)]] 0.5 µM | ⚠ position correction uncertain | **1.78×** | +7.3 | 1e-11 | 37/48 (HOP62, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Minodronic acid (drug)]] 0.05 µM | ⚠ position correction uncertain | **1.54×** | +7.2 | 2e-11 | 39/48 (A498, PANC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.53×** | +7.0 | 7e-11 | 27/44 (RPMI-7951, J82, …) | all doses, flat | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +6.9 | 2e-10 | 34/48 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +5.3 | 3e-06 | 23/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.52×** | +5.3 | 3e-06 | 25/48 (NCI-H1573, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.37×** | +5.1 | 7e-06 | 22/47 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[vincristine (drug)]] 5 µM |  | **1.61×** | +4.4 | 2e-04 | 21/45 (NCI-H1573, HT-29, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +4.4 | 2e-04 | 23/48 (SW480, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.28×** | +4.4 | 2e-04 | 20/48 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.1 | 6e-04 | 20/48 (LOX-IMVI, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3850.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 1 line (LOX-IMVI 0.0792×; ⚠ toxic); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.138×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.805×** | -5.5 | 3e-05 | 28/48 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.802×** | -3.9 | 0.026 | 16/48 (HS-578T, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.829× | -3.3 | 0.16 | 13/48 (A-427, A549, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.837× | -3.2 | 0.21 | 18/48 (SW 1088, HOP62, …) | top dose only |  |
| [[Saquinavir (drug)]] 0.05 µM |  | 0.839× | -3.1 | 0.21 | 17/48 (Hs 766T, H4, …) | inconsistent across doses |  |
| [[Fumaric acid (drug)]] 0.5 µM |  | 0.842× | -3.1 | 0.21 | 7/48 (NCI-H23, HOP62, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3850. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.7 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +12.6) | — |
| [[A549 (line)]] | wt | 33.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +18.8) | — |
| [[PANC-1 (line)]] | alt | 38.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +19.9) | — |
| [[SNU-1 (line)]] | wt | 46.1 | 5 | 0 | [[Harringtonine (drug)]] 0.5 µM 8.26× (z +12.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 42.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +17.2) | — |
| [[SW480 (line)]] | alt | 29.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 39.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +15.9) | — |
| [[LoVo (line)]] | wt | 18.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +17.5) | — |
| [[NCI-H2030 (line)]] | alt | 56.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +13.9) | — |
| [[NCI-H23 (line)]] | alt | 51.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.4) | — |
| [[AsPC-1 (line)]] | alt | 25.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +12.8) | — |
| [[COLO 205 (line)]] | alt | 16.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +10.1) | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.138× (z -9.0) ⚠ toxic |
| [[HT-29 (line)]] | alt | 34.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +13.2) | — |
| [[LOX-IMVI (line)]] | wt | 52.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +12.9) | [[Lonafarnib (drug)]] 5 µM 0.0792× (z -12.5) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 39.9 | 2 (2 ⚠) | 0 | [[Peretinoin (drug)]] 5 µM 3.86× (z +11.0) ⚠ position correction uncertain | — |
| [[NCI-H1792 (line)]] | alt | 27.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 37.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +12.6) | — |
| [[A498 (line)]] | wt | 96.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 40.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +11.9) | — |
| [[HepG2_C3A (line)]] | wt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 51.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 55.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 68.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.8) | — |
| [[KATO III (line)]] | alt | 21.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +15.2) | — |
| [[LS 180 (line)]] | wt | 15.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 39.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.3) | — |
| [[RKO (line)]] | wt | 45.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +12.9) | — |
| [[RPMI-7951 (line)]] | alt | 56.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 39.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 27.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +13.3) | — |
| [[A-172 (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3850), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFE3]] | +0.59 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[DCTN2]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CDV3]] | +0.56 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[SYNPO]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[ZYX]] | +0.55 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[DBN1]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[PLEKHG4]] | +0.55 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[RIPOR1]] | +0.54 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[SCAF1]] | +0.52 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[PIEZO1]] | +0.52 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[CIC]] | +0.52 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[FLII]] | +0.52 | +0.54 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNOT2]] | -0.54 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[SHQ1]] | -0.50 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ARMC10]] | -0.50 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[UQCRH]] | -0.49 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[SLC25A14]] | -0.49 | -0.37 / -0.58 | both halves | 9e-05 |  |
| [[SBNO1]] | -0.49 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[NME2]] | -0.48 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[DUXAP10]] | -0.47 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[SFXN1]] | -0.47 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[SNRPD2]] | -0.46 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[PIBF1]] | -0.46 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[RPLP0]] | -0.46 | -0.56 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HEG1]] | B | HEG1 activity raises MAP7D1's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without HEG1 | 0.058 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.467). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (4.0, -23.3); signed map (11.3, -7.8). **Vector** length 102, 26.5% of its response variance represented; |z| ≥ 3 in 1,242 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.4 | +12.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +15.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +5.6 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +5.3 | +10.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +8.4 |
|  | [[Peretinoin (drug)]] 0.5 µM | ⚠ position correction uncertain | +4.4 | +14.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.2 | +5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.6 | +4.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -0.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.5 | +4.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -1.8 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -3.2 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.9 | -2.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | MAP7 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:36,155,579-36,180,849 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10350, FLJ39022; previously PARCC1, RPRC1 |
| Gene groups (HGNC) | Microtubule associated protein 7 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3KQU3](https://www.uniprot.org/uniprotkb/Q3KQU3) (MAP7 domain-containing protein 1):

> Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth. Facilitate microtubule stabilization through the maintenance of acetylated stable microtubules.

**Summary**, from NCBI Gene [55700](https://www.ncbi.nlm.nih.gov/gene/55700):

> Predicted to be involved in microtubule cytoskeleton organization. Located in spindle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25514](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25514) · Entrez [55700](https://www.ncbi.nlm.nih.gov/gene/55700) · UniProt [Q3KQU3](https://www.uniprot.org/uniprotkb/Q3KQU3) · Ensembl [ENSG00000116871](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116871)

## Data

Gene col 3850: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3850); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3850, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3850]; `tensor/DDL_lfc|DDL_z.npy` [3850]; `embed/gene_vectors.npy` [3850]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3850 or target_col == 3850). Every well: [[MAP7D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP7D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

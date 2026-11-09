---
symbol: "TBC1D17"
type: "gene"
col: 2526
ensembl_id: "ENSG00000104946"
name: "TBC1 domain family member 17"
location: "19q13.33"
module: 74
arm: "+"
pooled_cpm: 21.36
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 23
n_dd_up_clean: 14
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# TBC1D17

*TBC1 domain family member 17* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.59× (z +7.8, q 4e-12, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.575× (z -13.1, q 2e-36, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WBP2]] (+0.72, fdr 7e-06), [[UBE2B]] (+0.71, fdr 7e-06), [[HDAC5]] (+0.69, fdr 1e-05); moves opposite to [[MSANTD2]] (-0.62, fdr 2e-05), [[SPOPL-DT]] (-0.62, fdr 1e-05), [[PRDM5]] (-0.62, fdr 3e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[DDAH2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2526.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.59×** | +7.8 | 4e-12 | 28/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.28×** | +7.2 | 2e-10 | 32/46 (A-172, Panc 03.27, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +6.1 | 3e-07 | 27/48 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +5.5 | 5e-06 | 25/48 (NCI-H2030, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.24×** | +5.1 | 3e-05 | 18/48 (LS 180, SNU-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +5.0 | 6e-05 | 23/47 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +4.7 | 2e-04 | 23/47 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.011 | 16/46 (LS 180, NCI-H460, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (drug)]] 5 µM |  | 1.16× | +3.6 | 0.019 | 11/48 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.028 | 17/47 (KATO III, NCI-H1792, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.028 | 13/48 (A-172, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.037 | 14/48 (A-427, NCI-H1573, …) | two highest doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.057 | 7/46 (SW480, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.063 | 10/48 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.076 | 12/47 (NCI-H2030, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2526.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.575×** | -13.1 | 2e-36 | 40/47 (NCI-H1792, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.559×** | -9.8 | 5e-20 | 40/47 (NCI-H1792, A-427, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.573×** | -9.0 | 6e-17 | 36/46 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.624×** | -7.6 | 4e-12 | 34/48 (hTERT-HPNE, KATO III, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.791×** | -5.6 | 3e-06 | 23/48 (A-427, RPMI-7951, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.531×** | -5.5 | 3e-06 | 22/45 (A498, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **0.732×** | -5.2 | 1e-05 | 20/41 (KATO III, LS 180, …) | rises with dose | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.725×** | -5.2 | 2e-05 | 24/47 (HS-578T, SW48, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.750×** | -4.8 | 9e-05 | 21/47 (KATO III, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **0.744×** | -4.7 | 1e-04 | 17/33 (HEC-1-A, LS 180, …) | rises with dose | composition shift |
| [[Busulfan (drug)]] 5 µM |  | **0.825×** | -4.6 | 3e-04 | 19/48 (LS 180, NCI-H1573, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.608×** | -4.3 | 6e-04 | 16/48 (NCI-H1792, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.772×** | -4.3 | 6e-04 | 19/46 (KATO III, BT-474, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.613×** | -4.3 | 8e-04 | 16/45 (CFPAC-1, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.699×** | -4.0 | 0.003 | 12/48 (SW480, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.808×** | -3.6 | 0.013 | 15/48 (LS 180, A-172, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.809×** | -3.4 | 0.025 | 14/48 (BT-474, Hs 766T, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.686×** | -3.3 | 0.030 | 16/44 (SK-MEL-2, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.822×** | -3.3 | 0.030 | 16/47 (AN3 CA, MIA PaCa-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.827×** | -3.2 | 0.038 | 9/47 (SW 900, NCI-H460, …) | rises with dose |  |
| [[Canagliflozin (drug)]] 5 µM |  | **0.824×** | -3.1 | 0.046 | 9/46 (A549, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2526. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 40.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[KATO III (line)]] | alt | 41.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[LS 180 (line)]] | wt | 20.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[MIA PaCa-2 (line)]] | alt | 28.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 30.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -14.1) |
| [[Panc 03.27 (line)]] | alt | 21.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -9.8) |
| [[SNU-423 (line)]] | alt | 22.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -9.4) |
| [[SW1417 (line)]] | alt | 33.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -8.9) |
| [[A-427 (line)]] | wt | 27.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.319× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[HT-29 (line)]] | alt | 67.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0794× (z -11.5) ⚠ toxic |
| [[J82 (line)]] | alt | 17.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -9.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 14.2 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.159× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -9.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H460 (line)]] | wt | 10.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -9.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2526), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WBP2]] | +0.72 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[UBE2B]] | +0.71 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[HDAC5]] | +0.69 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[PIP4P1]] | +0.66 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[TOM1]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 | same gene group |
| [[RANBP10]] | +0.63 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[RETREG2]] | +0.62 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[NFKBIL1]] | +0.61 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[BAD]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[CLIP3]] | +0.61 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[JUND]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[GOLPH3L]] | +0.61 | +0.46 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSANTD2]] | -0.62 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[SPOPL-DT]] | -0.62 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[PRDM5]] | -0.62 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[SUV39H2]] | -0.61 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[GSTCD]] | -0.60 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[ARSB]] | -0.59 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[TRNT1]] | -0.59 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[SNX5]] | -0.59 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[ZNF124]] | -0.58 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[BTBD1]] | -0.58 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[PIGW]] | -0.58 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[SLC25A15]] | -0.57 | -0.54 / -0.52 | both halves | 1e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TBC1D17's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CLIP3]] | C | CLIP3 activity raises TBC1D17's level | lines that do not express CLIP3 (4) vs lines expressing it (46) | 1.69× lower at baseline in the lines without CLIP3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RAPGEF4, MEGF11, TMEM170B; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDAH2]] | C | TBC1D17's natural level strengthens DDAH2's drug response | TBC1D17's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.12; direction not clear | 0.029 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.3, -48.2); signed map (-17.0, 6.0). **Vector** length 108, 25.3% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.3 | +6.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.0 | +7.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.7 | +5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +3.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.7 | +5.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.6 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.9 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.7 | +1.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -7.5 | -9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -13.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -6.0 | -7.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.5 | -9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -5.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.6 | -4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -5.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,877,666-49,888,750 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12168 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; TBC1 domain family members |
| Reactome | 4 pathways, smallest: TBC/RABGAPs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HA65](https://www.uniprot.org/uniprotkb/Q9HA65) (TBC1 domain family member 17):

> Probable RAB GTPase-activating protein that inhibits RAB8A/B function. Reduces Rab8 recruitment to tubules emanating from the endocytic recycling compartment (ERC) and inhibits Rab8-mediated endocytic trafficking, such as that of transferrin receptor (TfR). Involved in regulation of autophagy.

**Summary**, from NCBI Gene [79735](https://www.ncbi.nlm.nih.gov/gene/79735):

> Predicted to enable GTPase activator activity. Involved in retrograde transport, endosome to Golgi. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25699](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25699) · Entrez [79735](https://www.ncbi.nlm.nih.gov/gene/79735) · UniProt [Q9HA65](https://www.uniprot.org/uniprotkb/Q9HA65) · Ensembl [ENSG00000104946](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104946)

## Data

Gene col 2526: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2526); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2526, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2526]; `tensor/DDL_lfc|DDL_z.npy` [2526]; `embed/gene_vectors.npy` [2526]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2526 or target_col == 2526). Every well: [[TBC1D17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

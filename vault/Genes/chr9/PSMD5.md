---
symbol: "PSMD5"
type: "gene"
col: 1739
ensembl_id: "ENSG00000095261"
name: "proteasome 26S subunit, non-ATPase 5"
location: "9q33.2"
module: 149
arm: "+"
pooled_cpm: 82.23
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# PSMD5

*proteasome 26S subunit, non-ATPase 5* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.30× (z +7.9, q 2e-12, up in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 15 lines (HOP62 8.12×, hTERT-HPNE 4.39×, SNU-423 3.40×, SK-MEL-2 4.75×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HS-578T 4.18×; ⚠ cell-cycle shift, explains ~37% of this change).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.511× (z -14.2, q 5e-43, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.665× (z -8.6, q 1e-15, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM216]] (+0.70, fdr 7e-06), [[ALKBH1]] (+0.68, fdr 7e-06), [[DRG1]] (+0.67, fdr 7e-06); moves opposite to [[MAPRE1]] (-0.64, fdr 1e-05), [[DIAPH1]] (-0.60, fdr 1e-05), [[YWHAZ]] (-0.58, fdr 3e-05).
> It is in [[Module 149]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF264]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1739.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 15 lines (HOP62 8.12×, hTERT-HPNE 4.39×, SNU-423 3.40×, SK-MEL-2 4.75×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HS-578T 4.18×; ⚠ cell-cycle shift, explains ~37% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +7.9 | 2e-12 | 24/48 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.021 | 21/47 (NCI-H23, A498, …) | top dose only | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1739.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.511×** | -14.2 | 5e-43 | 45/49 (RKO, HCT15, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.498×** | -14.2 | 5e-43 | 40/44 (C-33 A, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.506×** | -13.3 | 4e-38 | 41/45 (SK-MEL-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.665×** | -8.6 | 1e-15 | 34/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.759×** | -8.3 | 2e-14 | 32/49 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.717×** | -7.0 | 2e-10 | 37/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.718×** | -7.0 | 2e-10 | 33/48 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.745×** | -6.0 | 2e-07 | 28/47 (H4, COLO 205, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.767×** | -5.4 | 4e-06 | 27/48 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.802×** | -4.7 | 2e-04 | 27/48 (SK-MEL-2, HCT15, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.815×** | -4.3 | 8e-04 | 26/48 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.820×** | -4.0 | 0.002 | 22/48 (A498, SW480, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.815×** | -3.6 | 0.014 | 21/48 (HOP62, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.846× | -3.4 | 0.028 | 21/48 (A-172, LOX-IMVI, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 0.862× | -3.1 | 0.066 | 15/48 (RPMI-7951, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1739. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 100 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.92× (z +9.4) ⚠ cell-cycle shift, explains ~37% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -10.7) ⚠ cell-cycle shift, explains ~18% of this change |
| [[HOP62 (line)]] | alt | 80.9 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.12× (z +31.2) | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -11.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 70.9 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +19.9) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -10.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 110 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +17.7) | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -11.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 88.2 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +19.9) | [[Auranofin (drug)]] 5 µM 0.434× (z -9.5) |
| [[SW480 (line)]] | alt | 107 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.487× (z -9.8) |
| [[A549 (line)]] | wt | 85.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.465× (z -10.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 66.7 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -12.7) ⚠ cell-cycle shift, explains ~18% of this change |
| [[BT-474 (line)]] | alt | 121 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.23× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -9.7) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.481× (z -8.5) |
| [[HCT15 (line)]] | alt | 157 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -15.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 97.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -16.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 114 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 78.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.398× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 90.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -12.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 75.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -10.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 84.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +13.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -9.1) ⚠ cell-cycle shift, explains ~48% of this change |
| [[C-33 A (line)]] | alt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -20.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 70.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +18.9) | — |
| [[KATO III (line)]] | alt | 86.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.387× (z -9.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 72.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -12.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 92.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +14.4) | — |
| [[NCI-H460 (line)]] | wt | 92.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.380× (z -12.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 86.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -18.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 63.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +12.9) | [[Dinaciclib (drug)]] 0.05 µM 0.515× (z -8.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0811× (z -31.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 83.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -11.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 55.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +19.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0727× (z -21.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 60.2 | 0 | 2 | — | [[Cyclosporin A (drug)]] 5 µM 0.0725× (z -8.6) |
| [[SW48 (line)]] | wt | 52.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +14.3) | — |
| [[C32 (line)]] | wt | 52.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.266× (z -10.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 49.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +18.9) | — |
| [[H4 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.303× (z -9.7) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 29.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +15.2) | — |
| [[LoVo (line)]] | wt | 65.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.422× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 48.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +13.4) | — |
| [[NCI-H23 (line)]] | alt | 75.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +14.6) | — |
| [[NCI-H2347 (line)]] | alt | 62.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -11.7) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SHP-77 (line)]] | alt | 98.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.393× (z -9.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 77.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -9.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -11.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 77.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1739), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM216]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ALKBH1]] | +0.68 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[DRG1]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[NBPF11]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[TTI2]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 | same gene group |
| [[GOSR1]] | +0.65 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[SETDB1]] | +0.64 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[ZNF766]] | +0.63 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[NSUN4]] | +0.63 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[AARSD1]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[TTF1]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[BRAP]] | +0.62 | +0.67 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE1]] | -0.64 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[DIAPH1]] | -0.60 | -0.51 / -0.66 | both halves | 1e-05 | same gene group |
| [[YWHAZ]] | -0.58 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[DDX5]] | -0.57 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[APP]] | -0.57 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[KLC2]] | -0.53 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[WWC3]] | -0.53 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[ITGB1]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF264]] | B | ZNF264 activity raises PSMD5's level | lines that do not express ZNF264 (5) vs lines expressing it (45) | 1.21× lower at baseline in the lines without ZNF264 | 0.084 | ⚠ within organs, on part of the lines; also absent: ZNF548, ZNF550, ZNF419 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.9, -7.4); signed map (-12.9, -12.1). **Vector** length 113, 30.3% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.5 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +5.0 | +2.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +3.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +2.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.0 | +0.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.7 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +1.2 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.3 | -13.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -14.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.1 | -14.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.7 | -6.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -4.0 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -2.3 | -1.8 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.2 | -0.4 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -2.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit, non-ATPase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:120,815,496-120,842,951 (-) |
| Ensembl biotype | protein_coding |
| Also known as | S5B, KIAA0072 |
| Gene groups (HGNC) | Proteasome; Armadillo like helical domain containing |
| Reactome | 1 pathways, smallest: Proteasome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16401](https://www.uniprot.org/uniprotkb/Q16401) (26S proteasome non-ATPase regulatory subunit 5):

> Acts as a chaperone during the assembly of the 26S proteasome, specifically of the base subcomplex of the PA700/19S regulatory complex (RC). In the initial step of the base subcomplex assembly is part of an intermediate PSMD5:PSMC2:PSMC1:PSMD2 module which probably assembles with a PSMD10:PSMC4:PSMC5:PAAF1 module followed by dissociation of PSMD5.

**Summary**, from NCBI Gene [5711](https://www.ncbi.nlm.nih.gov/gene/5711):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9563](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9563) · Entrez [5711](https://www.ncbi.nlm.nih.gov/gene/5711) · UniProt [Q16401](https://www.uniprot.org/uniprotkb/Q16401) · Ensembl [ENSG00000095261](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095261)

## Data

Gene col 1739: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1739); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1739, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1739]; `tensor/DDL_lfc|DDL_z.npy` [1739]; `embed/gene_vectors.npy` [1739]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1739 or target_col == 1739). Every well: [[PSMD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

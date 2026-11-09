---
symbol: "KANSL1L-AS1"
type: "gene"
col: 13693
ensembl_id: "ENSG00000229127"
name: "KANSL1L antisense RNA 1"
location: "2q34"
module: 39
arm: "+"
pooled_cpm: 22.6
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# KANSL1L-AS1

*KANSL1L antisense RNA 1* — 2q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.33× (z +12.5, q 8e-33, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.330× (z -11.6, q 2e-28, down in 42 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.438× (z -8.6, q 2e-15, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDI2-AS1]] (+0.73, fdr 7e-06), [[ZNF26]] (+0.72, fdr 7e-06), [[ANKAR]] (+0.69, fdr 1e-05); moves opposite to [[KBTBD3]] (-0.60, fdr 4e-05), [[HMGN3]] (-0.58, fdr 5e-05), [[CAT]] (-0.57, fdr 2e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13693.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +12.5 | 8e-33 | 42/48 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.26×** | +11.8 | 8e-30 | 46/47 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +9.6 | 1e-19 | 42/48 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **2.12×** | +7.5 | 8e-12 | 35/45 (NCI-H1573, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.97×** | +7.1 | 2e-10 | 41/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +6.8 | 1e-09 | 37/47 (SW480, HT-29, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.1 | 7e-08 | 36/48 (SW1417, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.68×** | +5.4 | 6e-06 | 31/47 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.55×** | +4.6 | 3e-04 | 24/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +4.5 | 4e-04 | 28/48 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.51×** | +4.3 | 0.001 | 30/48 (PANC-1, LoVo, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.48×** | +3.8 | 0.007 | 24/47 (C-33 A, A-172, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.42×** | +3.6 | 0.012 | 21/47 (CFPAC-1, LOX-IMVI, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +3.1 | 0.070 | 12/47 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13693.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.330×** | -11.6 | 2e-28 | 42/47 (BT-474, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.438×** | -8.6 | 2e-15 | 35/48 (HepG2/C3A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.528×** | -6.4 | 2e-08 | 36/47 (NCI-H2030, NCI-H460, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.530×** | -6.4 | 2e-08 | 32/46 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.634×** | -4.8 | 2e-04 | 32/48 (H4, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.732×** | -4.7 | 3e-04 | 24/47 (C32, HEC-1-A, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.664×** | -4.3 | 0.001 | 27/47 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.690×** | -3.9 | 0.007 | 22/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.514×** | -3.6 | 0.017 | 22/46 (C32, AN3 CA, …) | top dose only | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.724×** | -3.2 | 0.075 | 21/46 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.739×** | -3.2 | 0.075 | 16/48 (HepG2/C3A, BT-474, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM |  | 0.815× | -3.1 | 0.10 | 14/48 (SHP-77, SNU-423, …) | top dose only | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13693. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 39.0 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0976× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 32.0 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +9.6) | [[Harringtonine (drug)]] 5 µM 0.132× (z -11.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[NCI-H460 (line)]] | wt | 28.6 | 1 | 4 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.241× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.304× (z -8.9) |
| [[BT-474 (line)]] | alt | 25.3 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0336× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0868× (z -13.0) |
| [[C32 (line)]] | wt | 42.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -13.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.257× (z -9.7) |
| [[PANC-1 (line)]] | alt | 16.2 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +11.9) | [[Digitoxin (drug)]] 5 µM 0.187× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 49.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -12.8) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 18.6 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 11.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.63× (z +9.8) | — |
| [[SW480 (line)]] | alt | 25.6 | 2 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +12.6) | [[Digitoxin (drug)]] 5 µM 0.249× (z -10.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 19.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 10.7 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 9.54× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 20.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 13.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.167× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 26.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 10.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +11.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.103× (z -9.9) |
| [[A-427 (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -10.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 13.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -8.8) |
| [[H4 (line)]] | wt | 17.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.0599× (z -11.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 19.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 20.6 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.98× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0688× (z -11.3) |
| [[J82 (line)]] | alt | 38.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -10.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.199× (z -11.8) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 8.95× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 16.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 7.25 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0568× (z -12.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 33.8 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 13.5 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.32× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 15.3 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0589× (z -13.4) |
| [[A-172 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13693), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDI2-AS1]] | +0.73 | +0.70 / +0.71 | both halves | 7e-06 | same gene group |
| [[ZNF26]] | +0.72 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[ANKAR]] | +0.69 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[LINC01588]] | +0.69 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[HCG18]] | +0.68 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[RAPSN]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[EXOSC3]] | +0.67 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[MYH3]] | +0.66 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[EEF1AKMT1]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[LINC01355]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[PLAC8L1]] | +0.66 | +0.67 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD3]] | -0.60 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[HMGN3]] | -0.58 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[CAT]] | -0.57 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[DBP]] | -0.57 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ALAD]] | -0.56 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[TMEM14A]] | -0.54 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[MOSPD2]] | -0.54 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[FOXO6]] | -0.54 | -0.49 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KANSL1L-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.6, -11.3); signed map (15.4, 1.7). **Vector** length 103, 28.4% of its response variance represented; |z| ≥ 3 in 1,212 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.7 | +6.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +6.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +9.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.5 | +3.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | -0.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.2 | -4.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -6.1 | -6.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.6 | +4.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.9 | -2.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.9 | +5.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.7 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | +0.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.3 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | +2.3 |

## What is on record

|  |  |
|---|---|
| Name | KANSL1L antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q34 — chr2:210,030,572-210,064,356 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41139](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41139) · Entrez [101928020](https://www.ncbi.nlm.nih.gov/gene/101928020) · Ensembl [ENSG00000229127](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229127)

## Data

Gene col 13693: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13693); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13693, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13693]; `tensor/DDL_lfc|DDL_z.npy` [13693]; `embed/gene_vectors.npy` [13693]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13693 or target_col == 13693). Every well: [[KANSL1L-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KANSL1L-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

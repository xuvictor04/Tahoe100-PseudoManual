---
symbol: "GRK5"
type: "gene"
col: 12716
ensembl_id: "ENSG00000198873"
name: "G protein-coupled receptor kinase 5"
location: "10q26.11"
module: 154
arm: "+"
pooled_cpm: 67.65
n_lines_expressing: 47
n_dd_up: 11
n_dd_down: 24
n_dd_up_clean: 11
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# GRK5

*G protein-coupled receptor kinase 5* — 10q26.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.48× (z +17.9, q 0e+00, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.579× (z -9.9, q 2e-20, down in 30 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[5-Azacytidine (drug)]] 5 µM: 0.716× (z -6.5, q 8e-09, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKIA]] (+0.64, fdr 1e-05), [[FAM107B]] (+0.64, fdr 1e-05), [[GALNT12]] (+0.62, fdr 1e-05); moves opposite to [[C1RL]] (-0.56, fdr 3e-05), [[NNMT]] (-0.52, fdr 3e-05), [[HECTD1]] (-0.51, fdr 4e-05).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ADAM19]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12716.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.48×** | +17.9 | 0e+00 | 39/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.29×** | +16.3 | 0e+00 | 38/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.16×** | +15.1 | 0e+00 | 36/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +12.2 | 6e-32 | 30/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +11.4 | 4e-28 | 35/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.39×** | +9.0 | 3e-17 | 36/46 (SW480, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +6.5 | 6e-09 | 25/45 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +5.2 | 1e-05 | 19/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.18× | +4.7 | 2e-04 | 22/45 (NCI-H460, SW480, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +4.5 | 4e-04 | 17/45 (A549, C32, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.52×** | +4.3 | 8e-04 | 20/45 (RKO, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.012 | 10/45 (A549, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.049 | 8/45 (NCI-H1792, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +3.2 | 0.059 | 7/45 (NCI-H1792, SNU-423, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.077 | 14/45 (SW480, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12716.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.579×** | -9.9 | 2e-20 | 30/40 (PANC-1, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.661×** | -8.1 | 1e-13 | 29/43 (PANC-1, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.679×** | -7.3 | 6e-11 | 19/35 (Hs 766T, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.716×** | -6.5 | 8e-09 | 29/45 (LOX-IMVI, SHP-77, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.707×** | -6.5 | 8e-09 | 23/44 (HepG2/C3A, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **0.743×** | -5.8 | 6e-07 | 26/44 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.765×** | -5.2 | 1e-05 | 19/45 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.767×** | -5.2 | 2e-05 | 22/45 (Hs 766T, hTERT-HPNE, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.843× | -4.7 | 2e-04 | 18/45 (Hs 766T, SNU-423, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.783×** | -4.6 | 3e-04 | 19/45 (Hs 766T, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.792×** | -4.6 | 3e-04 | 19/45 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.795×** | -4.5 | 4e-04 | 22/45 (Hs 766T, A549, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.800×** | -4.4 | 6e-04 | 19/45 (Hs 766T, A498, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **0.810×** | -4.1 | 0.002 | 17/45 (Hs 766T, SNU-423, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.813×** | -4.0 | 0.002 | 20/45 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.755×** | -3.9 | 0.003 | 18/44 (A549, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.690×** | -3.8 | 0.004 | 19/46 (A549, SK-MEL-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.830×** | -3.6 | 0.008 | 18/45 (SHP-77, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.830×** | -3.6 | 0.008 | 15/45 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.833× | -3.6 | 0.009 | 16/45 (Hs 766T, SNU-423, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12716. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 255 | 0 | 19 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Betamethasone dipropionate (drug)]] 5 µM 0.255× (z -12.7) |
| [[SHP-77 (line)]] | alt | 157 | 0 | 10 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.307× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.342× (z -10.8) |
| [[PANC-1 (line)]] | alt | 272 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -14.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 30.6 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.23× (z +15.1) | — |
| [[NCI-H460 (line)]] | wt | 23.1 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +15.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.50× (z +13.4) | — |
| [[NCI-H2030 (line)]] | alt | 26.1 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 4.96× (z +12.5) | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.268× (z -9.5) |
| [[SW1417 (line)]] | alt | 80.3 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.45× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.399× (z -9.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 27.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.61× (z +11.6) | — |
| [[LoVo (line)]] | wt | 28.3 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.97× (z +10.5) | — |
| [[NCI-H2347 (line)]] | alt | 43.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +10.1) | — |
| [[A-427 (line)]] | wt | 25.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.07× (z +12.5) | — |
| [[C32 (line)]] | wt | 149 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -12.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 162 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 91.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.429× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 19.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.40× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 73.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -15.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 93.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -10.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 45.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.49× (z +9.9) | — |
| [[C-33 A (line)]] | alt | 35.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +9.5) ⚠ cell-cycle shift, explains ~34% of this change | [[Digitoxin (drug)]] 5 µM 0.144× (z -11.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 168 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0764× (z -11.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 23.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.50× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 29.3 | 2 | 0 | [[Belinostat (drug)]] 5 µM 3.26× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 49.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +10.3) ⚠ cell-cycle shift, explains ~34% of this change | [[Digitoxin (drug)]] 5 µM 0.308× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 44.3 | 0 | 2 | — | [[Tucatinib (drug)]] 0.05 µM 0.0524× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 67.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.03× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -10.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 54.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -12.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 54.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 65.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.179× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.364× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 55.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.275× (z -8.6) ⚠ cell-cycle shift, explains ~43% of this change |
| [[LOX-IMVI (line)]] | wt | 56.2 | 0 | 1 | — | [[5-Azacytidine (drug)]] 5 µM 0.330× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 63.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -12.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 43.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.27× (z +8.7) | — |
| [[SW48 (line)]] | wt | 26.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +12.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[BT-474 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.93 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.53 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12716), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKIA]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[FAM107B]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[GALNT12]] | +0.62 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[ADAM19]] | +0.61 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[WNT7B]] | +0.61 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[DPF3]] | +0.60 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[UBA6]] | +0.60 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[LPCAT2]] | +0.60 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[IFFO2]] | +0.60 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[SYNJ2]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[SH3BGRL3]] | +0.60 | +0.57 / +0.37 | both halves | 8e-05 |  |
| [[TNFRSF11A]] | +0.60 | +0.49 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1RL]] | -0.56 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[NNMT]] | -0.52 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[HECTD1]] | -0.51 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[MCPH1]] | -0.51 | -0.43 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers GRK5's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers GRK5's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers GRK5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[C12orf75]] | B | C12orf75 activity raises GRK5's level | lines that do not express C12orf75 (5) vs lines expressing it (45) | 2.74× lower at baseline in the lines without C12orf75 | 0.095 | ⚠ within organs, on part of the lines; also absent: FKBP7, VAT1, KCNC4 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM19]] | C | GRK5 activity raises ADAM19's level | lines that do not express GRK5 (3) vs lines expressing it (47) | 5.64× lower at baseline in the lines without GRK5 | 0.052 | ⚠ few lines (3 vs 47); across organs; co-occurs with MET, ERBB2; also absent: VAT1, CEP112, SLC16A1 |

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.6, -0.8); signed map (-2.8, 48.3). **Vector** length 114, 30.6% of its response variance represented; |z| ≥ 3 in 1,472 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +12.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.5 | +11.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.7 | +4.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +16.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +5.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +9.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +4.3 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -5.1 | -3.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -5.1 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.8 | -6.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.8 | -4.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor kinase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.11 — chr10:119,207,571-119,459,745 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GPRK5 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; G protein-coupled receptor kinase family |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 4 pathways, smallest: G alpha (s) signalling events; G alpha (q) signalling events; GPCR downstream signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [P34947](https://www.uniprot.org/uniprotkb/P34947) (G protein-coupled receptor kinase 5):

> Serine/threonine kinase that phosphorylates preferentially the activated forms of a variety of G protein-coupled receptors (GPCRs). Such receptor phosphorylation initiates beta-arrestin-mediated receptor desensitization, internalization, and signaling events leading to their down-regulation. Phosphorylates a variety of GPCRs, including adrenergic receptors, muscarinic acetylcholine receptors (more specifically Gi-coupled M2/M4 subtypes), dopamine receptors and opioid receptors. In addition to …

**Summary**, from NCBI Gene [2869](https://www.ncbi.nlm.nih.gov/gene/2869):

> This gene encodes a member of the guanine nucleotide-binding protein (G protein)-coupled receptor kinase subfamily of the Ser/Thr protein kinase family. The protein phosphorylates the activated forms of G protein-coupled receptors thus initiating their deactivation. It has also been shown to play a role in regulating the motility of polymorphonuclear leukocytes (PMNs). [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4544](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4544) · Entrez [2869](https://www.ncbi.nlm.nih.gov/gene/2869) · UniProt [P34947](https://www.uniprot.org/uniprotkb/P34947) · Ensembl [ENSG00000198873](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198873)

## Data

Gene col 12716: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12716); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12716, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12716]; `tensor/DDL_lfc|DDL_z.npy` [12716]; `embed/gene_vectors.npy` [12716]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12716 or target_col == 12716). Every well: [[GRK5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRK5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

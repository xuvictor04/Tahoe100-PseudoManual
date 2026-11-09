---
symbol: "PPIF"
type: "gene"
col: 2923
ensembl_id: "ENSG00000108179"
name: "peptidylprolyl isomerase F"
location: "10q22.3"
module: 125
arm: "+"
pooled_cpm: 24.39
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 7
n_dd_up_clean: 23
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# PPIF

*peptidylprolyl isomerase F* — 10q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.72× (z +19.8, q 0e+00, up in 41 of 46 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 4.52× (z +16.1, q 0e+00, up in 39 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.653× (z -4.6, q 0.003, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ROR1-AS1]] (+0.61, fdr 1e-05), [[SLC31A2]] (+0.61, fdr 1e-05), [[ZNF513]] (+0.60, fdr 1e-05); moves opposite to [[TM9SF2]] (-0.62, fdr 1e-05), [[SETD3]] (-0.60, fdr 1e-05), [[SEC63]] (-0.56, fdr 1e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SLC43A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2923.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.72×** | +19.8 | 0e+00 | 41/46 (AsPC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.52×** | +16.1 | 0e+00 | 39/44 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.56×** | +13.0 | 2e-36 | 41/47 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.72×** | +10.7 | 2e-24 | 42/45 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.67×** | +10.5 | 1e-23 | 41/48 (SNU-423, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.33×** | +9.0 | 2e-17 | 33/48 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.31×** | +8.9 | 3e-17 | 36/47 (SNU-423, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.16×** | +8.2 | 2e-14 | 38/48 (NCI-H1573, HepG2/C3A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.15×** | +8.2 | 2e-14 | 36/46 (NCI-H1573, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.13×** | +8.1 | 5e-14 | 36/47 (SW480, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.11×** | +8.0 | 8e-14 | 33/47 (NCI-H1573, SNU-423, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **2.10×** | +7.6 | 2e-12 | 34/43 (NCI-H460, J82, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +7.1 | 6e-11 | 34/42 (J82, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.84×** | +6.5 | 4e-09 | 30/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.73×** | +5.8 | 2e-07 | 30/48 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.64×** | +5.0 | 2e-05 | 26/46 (NCI-H1573, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.56×** | +4.6 | 2e-04 | 27/46 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.003 | 21/47 (SK-MEL-2, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.006 | 22/48 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.67×** | +3.6 | 0.009 | 17/46 (NCI-H460, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.013 | 20/45 (HT-29, NCI-H2030, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.65×** | +3.4 | 0.013 | 17/47 (CFPAC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.62×** | +3.3 | 0.019 | 13/43 (J82, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2923.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.653×** | -4.6 | 0.003 | 25/48 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.674×** | -4.2 | 0.006 | 22/48 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.706×** | -3.6 | 0.050 | 21/46 (NCI-H2030, NCI-H1573, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.718×** | -3.6 | 0.050 | 19/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.733×** | -3.3 | 0.082 | 17/48 (LOX-IMVI, hTERT-HPNE, …) | rises with dose |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **0.725×** | -3.3 | 0.082 | 13/48 (HEC-1-A, KATO III, …) | rises with dose | plate-row cell shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.739×** | -3.3 | 0.092 | 18/48 (H4, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2923. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 14.5 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 17.1× (z +13.6) | — |
| [[SNU-423 (line)]] | alt | 66.6 | 8 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +12.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 5.45× (z +11.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 68.9 | 7 (3 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 5.08× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.130× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 24.6 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +15.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.91× (z +12.5) | — |
| [[A498 (line)]] | wt | 36.9 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.61× (z +20.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.60× (z +14.1) | [[Belinostat (drug)]] 5 µM 0.359× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 59.0 | 4 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +13.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.72× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.223× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 23.7 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.4× (z +23.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 19.9× (z +15.6) | — |
| [[HepG2_C3A (line)]] | wt | 38.7 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.78× (z +14.8) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 17.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.19× (z +16.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.54× (z +12.1) | — |
| [[HS-578T (line)]] | alt | 12.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.67× (z +14.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 8.72× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 37.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +13.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.09× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 27.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.94× (z +15.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 12.1× (z +15.0) | — |
| [[HT-29 (line)]] | alt | 11.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.67× (z +14.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 3.96× (z +8.9) | — |
| [[LoVo (line)]] | wt | 16.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +21.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.59× (z +12.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.70× (z +15.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.72× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 16.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.90× (z +14.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 9.57× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 8.84 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +14.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.62× (z +11.2) | — |
| [[A549 (line)]] | wt | 14.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +13.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 8.42× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 24.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +11.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.74× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 22.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +11.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.67× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 40.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +11.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.55× (z +10.3) | — |
| [[SW 900 (line)]] | alt | 24.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +9.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.49× (z +9.1) | — |
| [[SW480 (line)]] | alt | 30.1 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.02× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 14.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.85× (z +9.3) | — |
| [[C32 (line)]] | wt | 8.83 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +9.0) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[LOX-IMVI (line)]] | wt | 24.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +10.4) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2030 (line)]] | alt | 26.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.19× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +8.8) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW1417 (line)]] | alt | 21.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +10.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A-427 (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2923), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROR1-AS1]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SLC31A2]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ZNF513]] | +0.60 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[C12orf50]] | +0.59 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[CRYM]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[HDAC9]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[ABL2]] | +0.58 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[KBTBD8]] | +0.58 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[HDX]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ZNF469]] | +0.57 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[OSGIN1]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[PLA2G4C]] | +0.56 | +0.57 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM9SF2]] | -0.62 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[SETD3]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[SEC63]] | -0.56 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[SEPTIN2]] | -0.55 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[SPAST]] | -0.55 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[RPA1]] | -0.55 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[ATP6AP2]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[ALDH6A1]] | -0.54 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[ARL3]] | -0.54 | -0.57 / -0.38 | both halves | 7e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[AKTIP]] | -0.54 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[DDOST]] | -0.54 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.53 | -0.60 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC43A3]] | B | SLC43A3 activity raises PPIF's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 1.50× lower at baseline in the lines without SLC43A3 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261 |
| [[CCDC71L]] | B | CCDC71L activity raises PPIF's level | lines that do not express CCDC71L (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without CCDC71L | 0.053 | ⚠ within organs, on part of the lines; also absent: RAI14, VIM-AS1, ENSG00000243797; maybe low, not absent |
| [[LY6K]] | B | LY6K activity raises PPIF's level | lines that do not express LY6K (32) vs lines expressing it (18) | 1.36× lower at baseline in the lines without LY6K | 0.073 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, TNIP3 |
| [[HDAC6]] | B | HDAC6 activity raises PPIF's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CARD6]] | B | CARD6 activity raises PPIF's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 1.58× lower at baseline in the lines without CARD6 | 0.089 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[INHBA]] | B | INHBA activity raises PPIF's level | lines that do not express INHBA (32) vs lines expressing it (18) | 1.42× lower at baseline in the lines without INHBA | 0.095 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.653). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (56.3, 11.1); signed map (37.6, 20.9). **Vector** length 94.8, 26.5% of its response variance represented; |z| ≥ 3 in 1,270 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.2 | +16.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +6.3 | +19.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.1 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +6.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.5 | +3.3 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | +0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.6 | -2.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.5 | -4.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.1 | -0.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | peptidylprolyl isomerase F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.3 — chr10:79,347,469-79,355,334 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hCyP3, Cyp-D, CypD |
| Gene groups (HGNC) | Cyclophilin peptidylprolyl isomerases |
| Hallmark sets | UV_RESPONSE_UP, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [P30405](https://www.uniprot.org/uniprotkb/P30405) (Peptidyl-prolyl cis-trans isomerase F, mitochondrial):

> PPIase that catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides and may therefore assist protein folding. Involved in regulation of the mitochondrial permeability transition pore (mPTP). It is proposed that its association with the mPTP is masking a binding site for inhibiting inorganic phosphate (Pi) and promotes the open probability of the mPTP leading to apoptosis or necrosis; the requirement of the PPIase activity for this function is debated. In …

**Summary**, from NCBI Gene [10105](https://www.ncbi.nlm.nih.gov/gene/10105):

> The protein encoded by this gene is a member of the peptidyl-prolyl cis-trans isomerase (PPIase) family. PPIases catalyze the cis-trans isomerization of proline imidic peptide bonds in oligopeptides and accelerate the folding of proteins. This protein is part of the mitochondrial permeability transition pore in the inner mitochondrial membrane. Activation of this pore is thought to be involved in the induction of apoptotic and necrotic cell death. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9259](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9259) · Entrez [10105](https://www.ncbi.nlm.nih.gov/gene/10105) · UniProt [P30405](https://www.uniprot.org/uniprotkb/P30405) · Ensembl [ENSG00000108179](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108179)

## Data

Gene col 2923: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2923); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2923, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2923]; `tensor/DDL_lfc|DDL_z.npy` [2923]; `embed/gene_vectors.npy` [2923]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2923 or target_col == 2923). Every well: [[PPIF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPIF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

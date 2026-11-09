---
symbol: "PARVA"
type: "gene"
col: 12443
ensembl_id: "ENSG00000197702"
name: "parvin alpha"
location: "11p15.3"
module: 79
arm: "+"
pooled_cpm: 80.05
n_lines_expressing: 44
n_dd_up: 6
n_dd_down: 24
n_dd_up_clean: 3
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# PARVA

*parvin alpha* — 11p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.94× (z +11.1, q 4e-26, up in 29 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.26× (z +3.8, q 0.013, up in 17 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.193× (z -28.7, q 0e+00, down in 42 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMYND11]] (+0.69, fdr 1e-05), [[TRIP12]] (+0.67, fdr 1e-05), [[AVEN]] (+0.66, fdr 1e-05); moves opposite to [[UBE2O]] (-0.69, fdr 7e-06), [[FAM162A]] (-0.68, fdr 1e-05), [[HILPDA]] (-0.66, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[AXL]] → it (grade B ⚠); 5 go from it, the strongest it → [[ENO2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12443.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +11.1 | 4e-26 | 29/36 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +7.9 | 1e-12 | 29/43 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +5.1 | 6e-05 | 21/39 (CFPAC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.18× | +4.2 | 0.004 | 21/42 (MIA PaCa-2, SW480, …) | rises with dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.013 | 17/42 (PANC-1, SW480, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.054 | 16/43 (AsPC-1, A-172, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.054 | 18/42 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.20× | +3.2 | 0.10 | 13/42 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.20× | +3.0 | 0.16 | 14/42 (C32, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12443.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.193×** | -28.7 | 0e+00 | 42/42 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.209×** | -27.4 | 0e+00 | 42/42 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.235×** | -25.3 | 0e+00 | 42/42 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.369×** | -17.4 | 0e+00 | 42/42 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.422×** | -15.1 | 0e+00 | 40/42 (RKO, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.423×** | -7.9 | 4e-13 | 39/43 (SW480, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.730×** | -7.8 | 6e-13 | 28/43 (SW1417, COLO 205, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.656×** | -7.4 | 1e-11 | 37/42 (LOX-IMVI, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.657×** | -7.3 | 1e-11 | 36/42 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.747×** | -7.2 | 3e-11 | 34/42 (LOX-IMVI, RKO, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.693×** | -6.4 | 7e-09 | 25/42 (SW48, RKO, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.729×** | -5.3 | 5e-06 | 27/41 (LOX-IMVI, RKO, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.745×** | -5.2 | 1e-05 | 26/42 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.760×** | -4.8 | 7e-05 | 29/42 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.765×** | -4.7 | 1e-04 | 28/42 (LOX-IMVI, RKO, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.761×** | -4.5 | 2e-04 | 24/42 (RKO, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.618×** | -4.4 | 4e-04 | 24/42 (LOX-IMVI, RKO, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12443. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 201 | 0 | 16 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.115× (z -25.9) |
| [[SW480 (line)]] | alt | 130 | 3 (3 ⚠) | 7 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +18.9) ⚠ cell-cycle shift, explains ~17% of this change | [[Panobinostat (drug)]] 0.5 µM 0.128× (z -30.4) |
| [[MIA PaCa-2 (line)]] | alt | 58.3 | 3 (3 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +21.7) ⚠ cell-cycle shift, explains ~17% of this change | [[Belinostat (drug)]] 5 µM 0.160× (z -17.2) |
| [[HEC-1-A (line)]] | alt | 94.5 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -20.0) |
| [[LS 180 (line)]] | wt | 61.3 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.142× (z -19.4) |
| [[PANC-1 (line)]] | alt | 43.0 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +11.0) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.381× (z -10.3) |
| [[RKO (line)]] | wt | 135 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0322× (z -35.8) |
| [[COLO 205 (line)]] | alt | 63.8 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.115× (z -18.9) |
| [[H4 (line)]] | wt | 171 | 1 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.6) ⚠ cell-cycle shift, explains ~17% of this change | [[Panobinostat (drug)]] 5 µM 0.103× (z -20.8) |
| [[HOP62 (line)]] | alt | 163 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.57× (z +10.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -20.9) |
| [[HT-29 (line)]] | alt | 84.5 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +8.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.193× (z -13.9) |
| [[LoVo (line)]] | wt | 77.3 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0947× (z -27.2) |
| [[SNU-1 (line)]] | wt | 116 | 1 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.0) ⚠ cell-cycle shift, explains ~17% of this change | [[Belinostat (drug)]] 5 µM 0.0553× (z -23.6) |
| [[SNU-423 (line)]] | alt | 116 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.41× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.182× (z -18.2) |
| [[SW1417 (line)]] | alt | 178 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -17.3) |
| [[Hs 766T (line)]] | wt | 76.5 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.142× (z -17.7) |
| [[HS-578T (line)]] | alt | 76.7 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.215× (z -15.5) |
| [[KATO III (line)]] | alt | 37.3 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.124× (z -18.9) |
| [[NCI-H1792 (line)]] | alt | 75.3 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.178× (z -16.2) |
| [[NCI-H23 (line)]] | alt | 40.9 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +12.0) ⚠ cell-cycle shift, explains ~17% of this change | [[Belinostat (drug)]] 5 µM 0.135× (z -15.4) |
| [[NCI-H460 (line)]] | wt | 50.7 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -22.0) |
| [[Panc 03.27 (line)]] | alt | 119 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -20.7) |
| [[RPMI-7951 (line)]] | alt | 123 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +9.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.284× (z -11.6) |
| [[SW48 (line)]] | wt | 74.0 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0693× (z -18.2) |
| [[A-172 (line)]] | wt | 115 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +10.9) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.350× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 69.7 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -18.3) |
| [[CFPAC-1 (line)]] | alt | 29.9 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 3.02× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -13.6) |
| [[J82 (line)]] | alt | 193 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.274× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 75.7 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +10.6) ⚠ cell-cycle shift, explains ~17% of this change | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -13.9) |
| [[A549 (line)]] | wt | 61.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -13.4) |
| [[AN3 CA (line)]] | alt | 125 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.113× (z -13.6) |
| [[BT-474 (line)]] | alt | 50.4 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +8.5) ⚠ cell-cycle shift, explains ~17% of this change | [[Panobinostat (drug)]] 0.5 µM 0.0969× (z -17.5) |
| [[C-33 A (line)]] | alt | 43.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -11.8) |
| [[C32 (line)]] | wt | 92.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.226× (z -14.8) |
| [[HCT15 (line)]] | alt | 75.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -12.1) |
| [[HepG2_C3A (line)]] | wt | 65.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -13.3) |
| [[hTERT-HPNE (line)]] | wt | 166 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 57.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -11.6) |
| [[A498 (line)]] | wt | 29.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +8.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.357× (z -9.0) |
| [[SW 1088 (line)]] | alt | 106 | 0 | 2 | — | [[Talc (drug)]] 0.05 µM 0.0941× (z -9.4) |
| [[SW 900 (line)]] | alt | 37.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -12.8) |
| [[A-427 (line)]] | wt | 4.53 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.70 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 19.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.15 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 57.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12443), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND11]] | +0.69 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[TRIP12]] | +0.67 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[AVEN]] | +0.66 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[ZNF655]] | +0.65 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[TRIM44]] | +0.62 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[IL6ST]] | +0.62 | +0.48 / +0.57 | both halves | 2e-05 | pathway: Cell junction organization |
| [[MSRA]] | +0.61 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[DDAH1]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[HDHD2]] | +0.60 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[ME3]] | +0.60 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ZNF644]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ITPRIPL2]] | +0.59 | +0.61 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2O]] | -0.69 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[FAM162A]] | -0.68 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[HILPDA]] | -0.66 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[SNAPC3]] | -0.65 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[INSIG2]] | -0.65 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[DDIT4]] | -0.65 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[TBC1D20]] | -0.64 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[CAMLG]] | -0.64 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[ENO2]] | -0.63 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[ANKRD37]] | -0.62 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[CNOT8]] | -0.62 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[RNF149]] | -0.62 | -0.49 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AXL]] | B | AXL activity raises PARVA's level | lines that do not express AXL (14) vs lines expressing it (36) | 1.66× lower at baseline in the lines without AXL | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |
| [[MYOF]] | B | MYOF activity raises PARVA's level | lines that do not express MYOF (6) vs lines expressing it (44) | 3.32× lower at baseline in the lines without MYOF | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |
| [[MSRB3]] | B | MSRB3 activity raises PARVA's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 1.13× lower at baseline in the lines without MSRB3 | 0.086 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[VGLL3]] | B | VGLL3 activity raises PARVA's level | lines that do not express VGLL3 (30) vs lines expressing it (20) | 1.50× lower at baseline in the lines without VGLL3 | 0.091 | ⚠ within organs, on part of the lines; also absent: EDNRA, APBB1IP, LINC02882 |
| [[DDIT4]] | C | DDIT4 activity raises PARVA's level | lines that do not express DDIT4 (3) vs lines expressing it (47) | 4.15× lower at baseline in the lines without DDIT4 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, TIMP1, UGDH; maybe low, not absent; its own permutation p |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENO2]] | B | PARVA activity raises ENO2's level | lines that do not express PARVA (6) vs lines expressing it (44) | 2.81× lower at baseline in the lines without PARVA | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969 |
| [[RIN3]] | B | PARVA activity raises RIN3's level | lines that do not express PARVA (6) vs lines expressing it (44) | 2.55× lower at baseline in the lines without PARVA | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969 |
| [[SDHAP2]] | B | PARVA activity raises SDHAP2's level | lines that do not express PARVA (6) vs lines expressing it (44) | 1.75× lower at baseline in the lines without PARVA | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969 |
| [[AXL]] | B | PARVA activity raises AXL's level | lines that do not express PARVA (6) vs lines expressing it (44) | 2.75× lower at baseline in the lines without PARVA | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969 |
| [[TBC1D20]] | B | PARVA activity raises TBC1D20's level | lines that do not express PARVA (6) vs lines expressing it (44) | 1.60× lower at baseline in the lines without PARVA | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969 |

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction -0.641). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.1, -15.3); signed map (18.1, -32.1). **Vector** length 126, 40.1% of its response variance represented; |z| ≥ 3 in 1,185 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.0 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.6 | +7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +10.3 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +9.0 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.9 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | -0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.1 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.1 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +3.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.1 | +3.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.9 | -15.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.7 | -17.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.1 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -7.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.4 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -7.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -3.0 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | parvin alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.3 — chr11:12,377,563-12,535,356 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12254, FLJ10793; previously MXRA2 |
| Gene groups (HGNC) | Parvins; ILK-PINCH-Parvin complex subunits |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 5 pathways, smallest: Localization of the PINCH-ILK-PARVIN complex to focal adhesions; Regulation of cytoskeletal remodeling and cell spreading by IPP complex components; Cell-extracellular matrix interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVD7](https://www.uniprot.org/uniprotkb/Q9NVD7) (Alpha-parvin):

> Plays a role in sarcomere organization and in smooth muscle cell contraction. Required for normal development of the embryonic cardiovascular system, and for normal septation of the heart outflow tract. Plays a role in sprouting angiogenesis and is required for normal adhesion of vascular smooth muscle cells to endothelial cells during blood vessel development (By similarity). Plays a role in the reorganization of the actin cytoskeleton, formation of lamellipodia and ciliogenesis. Plays a role …

**Summary**, from NCBI Gene [55742](https://www.ncbi.nlm.nih.gov/gene/55742):

> This gene encodes a member of the parvin family of actin-binding proteins. Parvins are associated with focal contacts and contain calponin homology domains that bind to actin filaments. The encoded protein is part of the integrin-linked kinase signaling complex and plays a role in cell adhesion, motility and survival. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:14652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14652) · Entrez [55742](https://www.ncbi.nlm.nih.gov/gene/55742) · UniProt [Q9NVD7](https://www.uniprot.org/uniprotkb/Q9NVD7) · Ensembl [ENSG00000197702](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197702)

## Data

Gene col 12443: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12443); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12443, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12443]; `tensor/DDL_lfc|DDL_z.npy` [12443]; `embed/gene_vectors.npy` [12443]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12443 or target_col == 12443). Every well: [[PARVA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARVA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

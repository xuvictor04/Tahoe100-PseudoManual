---
symbol: "UBN2"
type: "gene"
col: 8097
ensembl_id: "ENSG00000157741"
name: "ubinuclein 2"
location: "7q34"
module: 69
arm: "+"
pooled_cpm: 134.6
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 20
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# UBN2

*ubinuclein 2* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.22× (z +6.0, q 1e-06, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.416× (z -18.7, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.410× (z -9.7, q 3e-20, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CREBRF]] (+0.72, fdr 7e-06), [[JMY]] (+0.71, fdr 7e-06), [[SMIM14]] (+0.71, fdr 1e-05); moves opposite to [[CORO1C]] (-0.55, fdr 3e-05), [[UBE2N]] (-0.54, fdr 1e-05), [[RNGTT]] (-0.52, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8097.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +6.0 | 1e-06 | 26/48 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.013 | 23/48 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.6 | 0.049 | 20/49 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.049 | 18/49 (LS 180, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.049 | 21/48 (BT-474, LOX-IMVI, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | 1.35× | +3.2 | 0.11 | 22/48 (LS 180, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.16 | 13/49 (A549, LOX-IMVI, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.17 | 15/49 (H4, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8097.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.416×** | -18.7 | 0e+00 | 47/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.507×** | -14.5 | 6e-45 | 45/49 (A498, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.506×** | -14.0 | 4e-42 | 36/44 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.569×** | -11.1 | 2e-26 | 40/45 (A498, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.410×** | -9.7 | 3e-20 | 45/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.410×** | -9.7 | 3e-20 | 45/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.440×** | -8.9 | 4e-17 | 43/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.499×** | -7.5 | 3e-12 | 40/48 (SW 900, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.504×** | -7.4 | 7e-12 | 43/48 (SW1417, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.811×** | -6.3 | 1e-08 | 29/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.751×** | -6.1 | 5e-08 | 30/48 (SW480, KATO III, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.756×** | -6.0 | 1e-07 | 30/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.759×** | -5.9 | 2e-07 | 33/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.601×** | -5.5 | 1e-06 | 34/47 (SW48, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.647×** | -4.7 | 8e-05 | 20/38 (HS-578T, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.677×** | -4.6 | 2e-04 | 25/48 (AsPC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.709×** | -4.0 | 0.002 | 31/49 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.722×** | -3.8 | 0.004 | 25/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.824×** | -3.7 | 0.006 | 23/48 (SW48, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.848× | -3.5 | 0.010 | 21/48 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.860× | -3.2 | 0.027 | 18/49 (LS 180, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8097. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 140 | 13 (10 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +36.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.236× (z -22.9) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.245× (z -11.4) |
| [[SW1417 (line)]] | alt | 201 | 0 | 6 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.300× (z -16.8) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.243× (z -10.1) |
| [[HT-29 (line)]] | alt | 220 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +13.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.302× (z -13.5) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 182 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 136 | 1 (1 ⚠) | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.288× (z -16.1) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.240× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 130 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.235× (z -17.1) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.244× (z -8.5) |
| [[SNU-423 (line)]] | alt | 117 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.478× (z -13.1) |
| [[SW480 (line)]] | alt | 199 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.316× (z -16.7) ⚠ unreliable plate only · without an alert: [[Tucidinostat (drug)]] 5 µM 0.655× (z -8.7) |
| [[A498 (line)]] | wt | 202 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[AsPC-1 (line)]] | alt | 138 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.171× (z -19.6) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.205× (z -8.9) |
| [[C32 (line)]] | wt | 187 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[H4 (line)]] | wt | 117 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[Hs 766T (line)]] | wt | 157 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.441× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HS-578T (line)]] | alt | 125 | 0 | 4 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0404× (z -20.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.447× (z -13.9) |
| [[NCI-H23 (line)]] | alt | 199 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.468× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A549 (line)]] | wt | 103 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 90.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.334× (z -12.6) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 112 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0671× (z -28.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.445× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 96.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[PANC-1 (line)]] | alt | 111 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.412× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW 900 (line)]] | alt | 193 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.373× (z -12.1) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.248× (z -8.7) |
| [[SW48 (line)]] | wt | 151 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.157× (z -16.3) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.147× (z -8.6) |
| [[COLO 205 (line)]] | alt | 143 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[hTERT-HPNE (line)]] | wt | 125 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[LoVo (line)]] | wt | 171 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[LS 180 (line)]] | wt | 156 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +14.1) | — |
| [[SK-MEL-2 (line)]] | alt | 132 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SNU-1 (line)]] | wt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 74.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.312× (z -13.9) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 66.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CHP-212 (line)]] | wt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0850× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HCT15 (line)]] | alt | 172 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 82.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.359× (z -11.3) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.327× (z -11.6) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 96.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.371× (z -10.6) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 74.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.443× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 84.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.412× (z -11.0) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 81.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.301× (z -14.0) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[RKO (line)]] | wt | 176 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.365× (z -12.2) ⚠ unreliable plate only |
| [[SW 1088 (line)]] | alt | 178 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.158× (z -8.7) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 98.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 131 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 150 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8097), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CREBRF]] | +0.72 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[JMY]] | +0.71 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[SMIM14]] | +0.71 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[KLHL24]] | +0.70 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[TCP11L2]] | +0.67 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[SLU7]] | +0.67 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[PIK3CA]] | +0.67 | +0.46 / +0.71 | both halves | 2e-05 |  |
| [[CCDC186]] | +0.67 | +0.46 / +0.76 | both halves | 3e-05 |  |
| [[NBR1]] | +0.66 | +0.46 / +0.72 | both halves | 3e-05 |  |
| [[TERF2IP]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[CEP57]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[BET1]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO1C]] | -0.55 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[UBE2N]] | -0.54 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[RNGTT]] | -0.52 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[CCT2]] | -0.52 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[AGK]] | -0.51 | -0.38 / -0.48 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.725). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.4, -44.9); signed map (-13.5, 9.5). **Vector** length 125, 40.8% of its response variance represented; |z| ≥ 3 in 1,226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | +3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.7 | +4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.6 | +2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.8 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.7 | +1.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.5 | +1.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -12.2 | -18.7 |
|  | [[EX229 (drug)]] 5 µM |  | -8.7 | -9.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.0 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.9 | -6.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.6 | -8.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.4 | -7.5 |

## What is on record

|  |  |
|---|---|
| Name | ubinuclein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:139,230,356-139,308,236 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25778, KIAA2030 |
| Matched by | ensembl_id |

UniProt [Q6ZU65](https://www.uniprot.org/uniprotkb/Q6ZU65) carries no function annotation.

**Summary**, from NCBI Gene [254048](https://www.ncbi.nlm.nih.gov/gene/254048):

> Predicted to be involved in chromatin organization. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21931](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21931) · Entrez [254048](https://www.ncbi.nlm.nih.gov/gene/254048) · UniProt [Q6ZU65](https://www.uniprot.org/uniprotkb/Q6ZU65) · Ensembl [ENSG00000157741](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157741)

## Data

Gene col 8097: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8097); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8097, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8097]; `tensor/DDL_lfc|DDL_z.npy` [8097]; `embed/gene_vectors.npy` [8097]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8097 or target_col == 8097). Every well: [[UBN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

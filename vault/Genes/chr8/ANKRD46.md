---
symbol: "ANKRD46"
type: "gene"
col: 11778
ensembl_id: "ENSG00000186106"
name: "ankyrin repeat domain 46"
location: "8q22.3"
module: 15
arm: "+"
pooled_cpm: 16.79
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 12
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ANKRD46

*ankyrin repeat domain 46* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.94× (z +16.0, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.579× (z -8.1, q 2e-13, down in 30 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.702× (z -5.3, q 1e-05, down in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (C32 0.115×, SW480 0.276×, LS 180 0.191×, NCI-H2030 0.240×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LoVo 0.0921×, KATO III 0.173×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SNU-423 0.0947×, SHP-77 0.127×; ⚠ toxic); [[Flumatinib (mesylate) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0671×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.106×); [[Imiquimod (maleate) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0961×).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GIN1]] (+0.56, fdr 6e-05), [[YAE1]] (+0.52, fdr 4e-05), [[KCTD18]] (+0.51, fdr 4e-05); moves opposite to [[SIK3]] (-0.49, fdr 3e-05), [[ADIPOR2]] (-0.47, fdr 1e-04), [[CAPZB]] (-0.46, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11778.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.94×** | +16.0 | 0e+00 | 45/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +14.0 | 4e-42 | 40/46 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +13.9 | 2e-41 | 39/47 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.45×** | +13.2 | 8e-38 | 44/48 (NCI-H2347, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.43×** | +13.2 | 2e-37 | 43/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +8.0 | 1e-13 | 38/48 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +7.8 | 5e-13 | 30/46 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.37×** | +6.5 | 5e-09 | 25/48 (KATO III, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +5.8 | 5e-07 | 25/48 (NCI-H2347, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +5.6 | 1e-06 | 25/44 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.90×** | +5.0 | 3e-05 | 20/48 (PANC-1, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +4.8 | 8e-05 | 27/48 (KATO III, HS-578T, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.6 | 2e-04 | 21/46 (A498, H4, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.32×** | +4.1 | 0.002 | 15/47 (HEC-1-A, BT-474, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.002 | 19/47 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.003 | 18/48 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.004 | 16/47 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.017 | 10/47 (NCI-H2347, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11778.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (C32 0.115×, SW480 0.276×, LS 180 0.191×, NCI-H2030 0.240×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LoVo 0.0921×, KATO III 0.173×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SNU-423 0.0947×, SHP-77 0.127×; ⚠ toxic); [[Flumatinib (mesylate) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0671×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.106×); [[Imiquimod (maleate) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0961×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.579×** | -8.1 | 2e-13 | 30/46 (RPMI-7951, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.627×** | -6.7 | 7e-09 | 26/44 (SNU-423, SHP-77, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.655×** | -6.3 | 6e-08 | 26/40 (Panc 03.27, SW48, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.673×** | -5.9 | 5e-07 | 26/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.672×** | -5.5 | 5e-06 | 17/35 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.702×** | -5.3 | 1e-05 | 27/47 (LoVo, SW48, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.702×** | -5.3 | 1e-05 | 24/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.722×** | -4.7 | 2e-04 | 16/33 (C32, SW480, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.752×** | -4.3 | 0.001 | 16/47 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.642×** | -3.4 | 0.032 | 16/48 (COLO 205, NCI-H2347, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.799×** | -3.4 | 0.040 | 12/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.800×** | -3.3 | 0.041 | 16/47 (LoVo, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11778. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.9 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.83× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -11.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A498 (line)]] | wt | 16.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +12.9) | — |
| [[AsPC-1 (line)]] | alt | 7.38 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.15× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.107× (z -9.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 24.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +23.9) | [[Dinaciclib (drug)]] 5 µM 0.115× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 21.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 23.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.52× (z +18.8) | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +14.2) | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0961× (z -9.0) |
| [[LoVo (line)]] | wt | 20.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +19.1) | [[Dinaciclib (drug)]] 0.05 µM 0.0921× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.348× (z -8.9) |
| [[BT-474 (line)]] | alt | 22.6 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 4.34× (z +8.9) | [[Budesonide (drug)]] 0.5 µM 0.241× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 16.6 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.53× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 21.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0816× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SHP-77 (line)]] | alt | 28.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.127× (z -12.1) ⚠ toxic |
| [[SW480 (line)]] | alt | 21.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.170× (z -8.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.0671× (z -11.3) |
| [[KATO III (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -11.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 17.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +12.4) | — |
| [[LS 180 (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.44× (z +15.0) | — |
| [[NCI-H2030 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H23 (line)]] | alt | 13.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0774× (z -11.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.106× (z -11.1) |
| [[SNU-423 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0947× (z -12.2) ⚠ toxic |
| [[SW48 (line)]] | wt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +9.8) | — |
| [[A-172 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11778), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GIN1]] | +0.56 | +0.70 / +0.38 | both halves | 6e-05 |  |
| [[YAE1]] | +0.52 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[KCTD18]] | +0.51 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[SPATA5L1]] | +0.50 | +0.37 / +0.47 | both halves | 8e-05 |  |
| [[THAP6]] | +0.49 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[TMEM186]] | +0.49 | +0.61 / +0.40 | both halves | 4e-05 |  |
| [[SBF2-AS1]] | +0.48 | +0.66 / +0.24 | both halves | 4e-04 |  |
| [[DCP1B]] | +0.48 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[PSMG4]] | +0.48 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[FRG1BP]] | +0.47 | +0.54 / +0.38 | both halves | 6e-05 |  |
| [[TMEM128]] | +0.47 | +0.68 / +0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[LINC01772]] | +0.47 | +0.52 / +0.36 | both halves | 9e-05 |  |
| [[PPP1R8]] | +0.47 | +0.52 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIK3]] | -0.49 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[ADIPOR2]] | -0.47 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[CAPZB]] | -0.46 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[PHTF2]] | -0.45 | -0.50 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[CRY1]] | -0.44 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[STK3]] | -0.44 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[VMP1]] | -0.42 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[ATF7]] | -0.42 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[NUP98]] | -0.41 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[ZSWIM6]] | -0.41 | -0.32 / -0.33 | both halves | 1e-04 |  |
| [[MRTFA]] | -0.40 | -0.29 / -0.35 | both halves | 2e-04 |  |
| [[UBE2M]] | -0.40 | -0.57 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[GALNS]] | -0.39 | -0.53 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANKRD46's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.313). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.0, 16.9); signed map (14.3, -19.7). **Vector** length 61.6, 10.4% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +13.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +14.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +4.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +1.7 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.9 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.6 | -5.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.2 | -8.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.2 | -5.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.2 | -0.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.2 | +0.4 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -1.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 46 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.3 — chr8:100,509,752-100,559,784 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q86W74](https://www.uniprot.org/uniprotkb/Q86W74) carries no function annotation.

**Summary**, from NCBI Gene [157567](https://www.ncbi.nlm.nih.gov/gene/157567):

> This gene encodes a protein containing multiple ankyrin repeats. Ankyrin domains function in protein-protein interactions in a variety of cellular processes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:27229](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27229) · Entrez [157567](https://www.ncbi.nlm.nih.gov/gene/157567) · UniProt [Q86W74](https://www.uniprot.org/uniprotkb/Q86W74) · Ensembl [ENSG00000186106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186106)

## Data

Gene col 11778: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11778); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11778, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11778]; `tensor/DDL_lfc|DDL_z.npy` [11778]; `embed/gene_vectors.npy` [11778]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11778 or target_col == 11778). Every well: [[ANKRD46 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD46.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

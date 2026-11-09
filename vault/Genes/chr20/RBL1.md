---
symbol: "RBL1"
type: "gene"
col: 1295
ensembl_id: "ENSG00000080839"
name: "RB transcriptional corepressor like 1"
location: "20q11.23"
module: 6
arm: "+"
pooled_cpm: 59.14
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 11
direction_downstream: 1
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RBL1

*RB transcriptional corepressor like 1* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.76× (z +11.2, q 2e-26, up in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~73% of this change. The strongest without an alert is [[Brivudine (drug)]] 5 µM: 1.48× (z +4.1, q 0.003, up in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (LOX-IMVI 4.24×, A549 2.84×; ⚠ cell-cycle shift, explains ~68% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (LOX-IMVI 3.60×, A549 2.75×; ⚠ cell-cycle shift, explains ~73% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 2.27×).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.413× (z -17.5, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BLM]] (+0.90, fdr 7e-06), [[EXO1]] (+0.86, fdr 7e-06), [[WDHD1]] (+0.86, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FANCM]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1295.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (LOX-IMVI 4.24×, A549 2.84×; ⚠ cell-cycle shift, explains ~68% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (LOX-IMVI 3.60×, A549 2.75×; ⚠ cell-cycle shift, explains ~73% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 2.27×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.76×** | +11.2 | 2e-26 | 39/48 (LOX-IMVI, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.68×** | +10.3 | 3e-22 | 37/48 (LOX-IMVI, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.64×** | +9.8 | 2e-20 | 37/48 (LOX-IMVI, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.37×** | +6.2 | 9e-08 | 30/48 (HT-29, PANC-1, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.21×** | +5.5 | 6e-06 | 21/48 (SW480, NCI-H23, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~85% of this change | **1.29×** | +4.8 | 2e-04 | 18/47 (SW480, HT-29, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.25×** | +4.4 | 8e-04 | 19/48 (LoVo, HT-29, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +4.1 | 0.003 | 17/48 (AsPC-1, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.037 | 13/48 (AsPC-1, C32, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.050 | 13/48 (HT-29, RPMI-7951, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.057 | 14/48 (SW48, NCI-H460, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.081 | 15/48 (HS-578T, NCI-H1573, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.099 | 13/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | 1.16× | +3.0 | 0.099 | 8/48 (HT-29, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1295.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.413×** | -17.5 | 0e+00 | 43/48 (SW480, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.541×** | -17.2 | 0e+00 | 38/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.537×** | -12.3 | 2e-32 | 35/48 (A-427, SNU-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.692×** | -10.3 | 1e-22 | 34/48 (HEC-1-A, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.590×** | -9.8 | 8e-21 | 35/48 (HEC-1-A, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.659×** | -5.9 | 4e-07 | 28/48 (SW480, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.566×** | -5.9 | 4e-07 | 26/48 (MIA PaCa-2, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.740×** | -5.7 | 8e-07 | 25/47 (HEC-1-A, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.835× | -5.0 | 3e-05 | 25/48 (A-427, SW48, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.768×** | -5.0 | 3e-05 | 25/48 (AN3 CA, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 0.840× | -4.8 | 7e-05 | 18/48 (NCI-H23, hTERT-HPNE, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.844× | -4.7 | 1e-04 | 21/48 (HCT15, SNU-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.634×** | -4.7 | 1e-04 | 18/49 (NCI-H23, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 5 µM |  | **0.638×** | -4.6 | 1e-04 | 20/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.684×** | -3.9 | 0.003 | 14/44 (SW48, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[crizotinib (drug)]] 5 µM |  | **0.816×** | -3.9 | 0.004 | 17/48 (PANC-1, SK-MEL-2, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.708×** | -3.6 | 0.012 | 17/46 (HCT15, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.838× | -3.5 | 0.016 | 16/47 (KATO III, AN3 CA, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.846× | -3.3 | 0.029 | 14/48 (A-427, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.65 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1295. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 117 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -19.2) |
| [[A-427 (line)]] | wt | 99.9 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0547× (z -30.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.305× (z -17.8) |
| [[NCI-H460 (line)]] | wt | 50.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -14.5) |
| [[C-33 A (line)]] | alt | 88.1 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.0994× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.337× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 73.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -21.2) |
| [[COLO 205 (line)]] | alt | 49.2 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.271× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 129 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.456× (z -12.1) |
| [[A-172 (line)]] | wt | 49.6 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.269× (z -10.9) |
| [[AN3 CA (line)]] | alt | 68.0 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.111× (z -11.2) |
| [[J82 (line)]] | alt | 187 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 66.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -14.5) |
| [[A498 (line)]] | wt | 43.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -18.8) |
| [[A549 (line)]] | wt | 35.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.84× (z +8.8) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[CFPAC-1 (line)]] | alt | 38.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -12.9) |
| [[H4 (line)]] | wt | 34.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.100× (z -12.8) |
| [[HCT15 (line)]] | alt | 63.5 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.270× (z -9.4) |
| [[HOP62 (line)]] | alt | 37.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.8) |
| [[KATO III (line)]] | alt | 79.4 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.291× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.444× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 30.7 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.24× (z +10.6) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[Panc 03.27 (line)]] | alt | 53.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.320× (z -9.9) |
| [[SHP-77 (line)]] | alt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0835× (z -25.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 65.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -13.2) |
| [[SNU-423 (line)]] | alt | 59.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -14.7) |
| [[SW48 (line)]] | wt | 50.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.390× (z -8.9) |
| [[SW480 (line)]] | alt | 96.1 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.256× (z -16.6) |
| [[Hs 766T (line)]] | wt | 65.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -12.7) |
| [[LS 180 (line)]] | wt | 31.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 63.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -14.3) |
| [[NCI-H2030 (line)]] | alt | 75.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.455× (z -8.5) |
| [[PANC-1 (line)]] | alt | 48.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.450× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 50.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -10.5) |
| [[SW 1088 (line)]] | alt | 76.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0638× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 91.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 76.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1295), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLM]] | +0.90 | +0.88 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[EXO1]] | +0.86 | +0.86 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[WDHD1]] | +0.86 | +0.83 / +0.86 | both halves | 7e-06 |  |
| [[RAD51]] | +0.85 | +0.85 / +0.80 | both halves | 7e-06 |  |
| [[DTL]] | +0.84 | +0.86 / +0.82 | both halves | 7e-06 |  |
| [[FANCB]] | +0.84 | +0.84 / +0.77 | both halves | 7e-06 |  |
| [[SPC24]] | +0.83 | +0.83 / +0.78 | both halves | 7e-06 |  |
| [[GINS1]] | +0.83 | +0.86 / +0.85 | both halves | 7e-06 |  |
| [[POLQ]] | +0.82 | +0.81 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[MCM10]] | +0.82 | +0.82 / +0.81 | both halves | 7e-06 | pathway: G1/S Transition |
| [[MMS22L]] | +0.81 | +0.82 / +0.80 | both halves | 7e-06 |  |
| [[MELK]] | +0.81 | +0.83 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises RBL1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.30× lower at baseline in the lines without E2F8 | 0.033 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers RBL1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CDC25A]] | B | CDC25A activity raises RBL1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.08× lower at baseline in the lines without CDC25A | 0.076 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises RBL1's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.84× lower at baseline in the lines without E2F2 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[BRME1]] | C | BRME1 activity strengthens RBL1's drug response | lines that do not express BRME1 (4) vs lines expressing it (44) | the lines without BRME1 respond 0.87× as strongly (z diff +0.63); strongest at Idarubicin (hydrochloride) 5 µM: 1.09x vs 0.67x (z diff +5.6) | 0.026 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[BRME1]] | C | BRME1 activity raises RBL1's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 2.27× lower at baseline in the lines without BRME1 | 0.040 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises RBL1's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.23× lower at baseline in the lines without DSCC1 | 0.057 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises RBL1's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.77× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[DIAPH3]], [[MELK]] | C | DIAPH3, MELK activity raises RBL1's level | lines that do not express DIAPH3, MELK (3) vs lines expressing them (47) | 2.61× lower at baseline in the lines without DIAPH3, MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CENPP]] | C | CENPP activity raises RBL1's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.21× lower at baseline in the lines without CENPP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[PBK]] | C | PBK activity raises RBL1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.10× lower at baseline in the lines without PBK | 0.092 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FANCM]] | C | RBL1's natural level strengthens FANCM's drug response | RBL1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse -0.04; direction not clear | 0.044 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.823). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.6, -46.5); signed map (-39.0, -42.6). **Vector** length 144, 47.0% of its response variance represented; |z| ≥ 3 in 1,284 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.61 to 65); *DNA strand elongation* (reactome, mean cos +0.67 to 28); *DNA Replication* (reactome, mean cos +0.66 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +6.5 | +6.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +6.1 | +11.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +6.0 | +9.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +5.9 | +10.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +1.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.4 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +1.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +2.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.4 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.4 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.0 | -17.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.8 | -12.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.8 | -17.2 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -5.2 | -5.9 |
|  | [[palbociclib (drug)]] 5 µM |  | -4.0 | -4.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.7 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -5.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -3.5 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | RB transcriptional corepressor like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:36,996,349-37,095,997 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p107, cp107, PRB1 |
| Gene groups (HGNC) | DREAM complex subunits |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 17 pathways, smallest: Transcription of E2F targets under negative control by p107 (RBL1) and p130 (RBL2) in complex with HDAC1; TP53 Regulates Transcription of Genes Involved in G2 Cell Cycle Arrest; Transcription of E2F targets under negative control by DREAM complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P28749](https://www.uniprot.org/uniprotkb/P28749) (Retinoblastoma-like protein 1):

> Key regulator of entry into cell division. Directly involved in heterochromatin formation by maintaining overall chromatin structure and, in particular, that of constitutive heterochromatin by stabilizing histone methylation (By similarity). Recruits and targets histone methyltransferases KMT5B and KMT5C, leading to epigenetic transcriptional repression (By similarity). Controls histone H4 'Lys-20' trimethylation (By similarity). Probably acts as a transcription repressor by recruiting …

**Summary**, from NCBI Gene [5933](https://www.ncbi.nlm.nih.gov/gene/5933):

> The protein encoded by this gene is similar in sequence and possibly function to the product of the retinoblastoma 1 (RB1) gene. The RB1 gene product is a tumor suppressor protein that appears to be involved in cell cycle regulation, as it is phosphorylated in the S to M phase transition and is dephosphorylated in the G1 phase of the cell cycle. Both the RB1 protein and the product of this gene can form a complex with adenovirus E1A protein and SV40 large T-antigen, with the SV40 large …

**Accessions** — [HGNC:9893](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9893) · Entrez [5933](https://www.ncbi.nlm.nih.gov/gene/5933) · UniProt [P28749](https://www.uniprot.org/uniprotkb/P28749) · Ensembl [ENSG00000080839](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080839)

## Data

Gene col 1295: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1295); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1295, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1295]; `tensor/DDL_lfc|DDL_z.npy` [1295]; `embed/gene_vectors.npy` [1295]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1295 or target_col == 1295). Every well: [[RBL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

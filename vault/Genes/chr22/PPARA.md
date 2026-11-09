---
symbol: "PPARA"
type: "gene"
col: 11871
ensembl_id: "ENSG00000186951"
name: "peroxisome proliferator activated receptor alpha"
location: "22q13.31"
module: 56
arm: "+"
pooled_cpm: 67.59
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 43
n_dd_up_clean: 2
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# PPARA

*peroxisome proliferator activated receptor alpha* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.28× (z +5.3, q 7e-05, up in 25 of 46 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.21× (z +4.3, q 0.004, up in 21 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW48 8.75×, PANC-1 2.29×, NCI-H460 2.02×; ⚠ cell-cycle shift, explains ~41% of this change).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.352× (z -23.0, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RASA4B]] (+0.67, fdr 8e-06), [[PDXDC2P-NPIPB14P]] (+0.66, fdr 7e-06), [[GOLGA2]] (+0.65, fdr 7e-06); moves opposite to [[RAB11FIP2]] (-0.62, fdr 2e-05), [[ZC3HAV1L]] (-0.59, fdr 5e-05), [[MTMR2]] (-0.58, fdr 4e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[BAZ2A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11871.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW48 8.75×, PANC-1 2.29×, NCI-H460 2.02×; ⚠ cell-cycle shift, explains ~41% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.28×** | +5.3 | 7e-05 | 25/46 (C32, A498, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +4.3 | 0.004 | 21/46 (NCI-H2030, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.026 | 15/47 (NCI-H1792, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.17× | +3.5 | 0.067 | 11/47 (KATO III, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 57 in all, 18 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11871.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.352×** | -23.0 | 0e+00 | 41/47 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.355×** | -22.8 | 0e+00 | 42/47 (COLO 205, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.394×** | -20.5 | 0e+00 | 45/47 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.395×** | -20.5 | 0e+00 | 43/47 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.430×** | -17.9 | 0e+00 | 40/46 (KATO III, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.430×** | -17.9 | 0e+00 | 40/47 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.431×** | -17.1 | 0e+00 | 34/42 (HOP62, HT-29, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.558×** | -12.8 | 8e-36 | 42/47 (LoVo, A549, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.561×** | -12.7 | 4e-35 | 34/48 (SK-MEL-2, SNU-1, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.551×** | -12.6 | 1e-34 | 33/49 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.338×** | -12.5 | 4e-34 | 38/47 (RKO, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.483×** | -12.3 | 5e-33 | 40/47 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.585×** | -11.3 | 4e-28 | 35/47 (HOP62, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.391×** | -10.8 | 1e-25 | 38/48 (LS 180, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.614×** | -10.7 | 3e-25 | 36/47 (CFPAC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.593×** | -8.8 | 3e-17 | 38/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.610×** | -8.3 | 2e-15 | 35/47 (CFPAC-1, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.735×** | -6.4 | 4e-09 | 33/47 (SW 900, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.769×** | -5.5 | 7e-07 | 24/47 (HS-578T, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11871. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 126 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -22.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -21.2) |
| [[SW 900 (line)]] | alt | 190 | 0 | 17 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.163× (z -18.4) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.182× (z -18.0) |
| [[CFPAC-1 (line)]] | alt | 67.0 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -17.7) |
| [[HOP62 (line)]] | alt | 103 | 0 | 13 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -15.8) |
| [[AsPC-1 (line)]] | alt | 104 | 0 | 12 (9 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.165× (z -20.4) |
| [[LoVo (line)]] | wt | 104 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -15.2) |
| [[LS 180 (line)]] | wt | 172 | 0 | 12 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.175× (z -21.8) |
| [[SNU-423 (line)]] | alt | 67.7 | 0 | 11 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.175× (z -17.1) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -13.9) |
| [[A-172 (line)]] | wt | 69.0 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -16.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.260× (z -14.0) |
| [[Hs 766T (line)]] | wt | 130 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -14.8) |
| [[HS-578T (line)]] | alt | 115 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -14.9) |
| [[HT-29 (line)]] | alt | 112 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -19.6) |
| [[COLO 205 (line)]] | alt | 120 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.154× (z -18.4) |
| [[H4 (line)]] | wt | 89.5 | 0 | 8 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.161× (z -15.1) |
| [[hTERT-HPNE (line)]] | wt | 83.5 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -14.9) |
| [[PANC-1 (line)]] | alt | 30.7 | 1 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.6) ⚠ cell-cycle shift, explains ~41% of this change | [[Digitoxin (drug)]] 5 µM 0.346× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.370× (z -10.7) |
| [[RKO (line)]] | wt | 72.3 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -18.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0599× (z -15.0) |
| [[HEC-1-A (line)]] | alt | 69.7 | 0 | 7 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 46.4 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.112× (z -18.1) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.255× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 50.0 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.109× (z -18.7) |
| [[NCI-H1792 (line)]] | alt | 63.5 | 0 | 7 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.218× (z -15.4) |
| [[Panc 03.27 (line)]] | alt | 54.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -13.1) |
| [[RPMI-7951 (line)]] | alt | 78.7 | 0 | 7 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -13.7) |
| [[C32 (line)]] | wt | 58.0 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.271× (z -11.9) |
| [[J82 (line)]] | alt | 50.1 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.344× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 39.0 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0796× (z -20.8) |
| [[SW480 (line)]] | alt | 37.0 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.207× (z -16.5) |
| [[A498 (line)]] | wt | 87.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.359× (z -12.2) |
| [[A549 (line)]] | wt | 25.1 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.164× (z -12.7) |
| [[NCI-H2030 (line)]] | alt | 39.6 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 25.0 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.7) ⚠ cell-cycle shift, explains ~41% of this change | [[Digitoxin (drug)]] 0.05 µM 0.253× (z -13.2) ⚠ cell-cycle shift, explains ~51% of this change |
| [[A-427 (line)]] | wt | 21.9 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.145× (z -13.5) |
| [[HCT15 (line)]] | alt | 118 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[LOX-IMVI (line)]] | wt | 25.4 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0443× (z -21.1) |
| [[SK-MEL-2 (line)]] | alt | 40.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -10.0) |
| [[SNU-1 (line)]] | wt | 72.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.329× (z -9.3) |
| [[SW1417 (line)]] | alt | 58.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -15.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.318× (z -12.0) |
| [[SW48 (line)]] | wt | 57.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.75× (z +20.5) ⚠ cell-cycle shift, explains ~41% of this change | [[Digitoxin (drug)]] 5 µM 0.155× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.244× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 49.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -8.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 77.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[AN3 CA (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11871), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASA4B]] | +0.67 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[PDXDC2P-NPIPB14P]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[GOLGA2]] | +0.65 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[PMM1]] | +0.64 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[WIPI1]] | +0.64 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[HORMAD2-AS1]] | +0.63 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[PHF1]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[INAFM1]] | +0.63 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[SLC25A42]] | +0.62 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[TBC1D10A]] | +0.62 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[PDXDC1]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[CLIP2]] | +0.61 | +0.56 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB11FIP2]] | -0.62 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[ZC3HAV1L]] | -0.59 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[MTMR2]] | -0.58 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[BMS1P2]] | -0.57 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[MGST1]] | -0.57 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[TAS2R30]] | -0.57 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[PRTFDC1]] | -0.56 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[EWSR1]] | -0.56 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[TADA2A]] | -0.56 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[ANGEL2]] | -0.56 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[SETMAR]] | -0.55 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[ZNF239]] | -0.55 | -0.47 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BAZ2A]] | C | PPARA's natural level weakens BAZ2A's drug response | PPARA's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.10; direction not clear | 0.057 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.541). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.6, -36.5); signed map (-19.4, 23.7). **Vector** length 101, 31.8% of its response variance represented; |z| ≥ 3 in 1,461 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +6.8 | -8.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.0 | +1.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.2 | -2.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.4 | -4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | -3.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.5 | +3.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.4 | +2.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +2.0 | +1.4 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.9 | +0.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.7 | -20.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.7 | -12.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -5.3 | -7.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.1 | -10.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.9 | -5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.8 | -4.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.4 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | peroxisome proliferator activated receptor alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:46,150,521-46,243,755 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hPPAR, NR1C1; previously PPAR |
| Gene groups (HGNC) | Peroxisome proliferator activated receptors |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 26 pathways, smallest: BMAL1:CLOCK,NPAS2 activates circadian expression; RORA,B,C and NR1D1 (REV-ERBA) regulate gene expression; Transcriptional regulation of brown and beige adipocyte differentiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07869](https://www.uniprot.org/uniprotkb/Q07869) (Peroxisome proliferator-activated receptor alpha):

> Ligand-activated transcription factor. Key regulator of lipid metabolism. Activated by the endogenous ligand 1-palmitoyl-2-oleoyl-sn-glycerol-3-phosphocholine (16:0/18:1-GPC). Activated by oleylethanolamide, a naturally occurring lipid that regulates satiety. Receptor for peroxisome proliferators such as hypolipidemic drugs and fatty acids. Regulates the peroxisomal beta-oxidation pathway of fatty acids. Functions as a transcription activator for the ACOX1 and P450 genes. Transactivation …

**Summary**, from NCBI Gene [5465](https://www.ncbi.nlm.nih.gov/gene/5465):

> Peroxisome proliferators include hypolipidemic drugs, herbicides, leukotriene antagonists, and plasticizers; this term arises because they induce an increase in the size and number of peroxisomes. Peroxisomes are subcellular organelles found in plants and animals that contain enzymes for respiration and for cholesterol and lipid metabolism. The action of peroxisome proliferators is thought to be mediated via specific receptors, called PPARs, which belong to the steroid hormone receptor …

**Accessions** — [HGNC:9232](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9232) · Entrez [5465](https://www.ncbi.nlm.nih.gov/gene/5465) · UniProt [Q07869](https://www.uniprot.org/uniprotkb/Q07869) · Ensembl [ENSG00000186951](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186951)

## Data

Gene col 11871: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11871); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11871, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11871]; `tensor/DDL_lfc|DDL_z.npy` [11871]; `embed/gene_vectors.npy` [11871]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11871 or target_col == 11871). Every well: [[PPARA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPARA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

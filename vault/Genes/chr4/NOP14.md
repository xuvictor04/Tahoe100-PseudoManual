---
symbol: "NOP14"
type: "gene"
col: 1496
ensembl_id: "ENSG00000087269"
name: "NOP14 nucleolar protein"
location: "4p16.3"
module: 1
arm: "+"
pooled_cpm: 43.13
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# NOP14

*NOP14 nucleolar protein* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.37× (z +21.5, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Anethole trithione (drug)]] 5 µM: 0.811× (z -5.2, q 1e-04, down in 27 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Minodronic acid (drug)]] 0.05 µM: 0.802× (z -3.7, q 0.036, down in 15 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 1 line (CHP-212 0.0770×; ⚠ transcription drop); [[Simotinib (drug)]] 5 µM in 1 line (AN3 CA 0.0890×; ⚠ toxic); [[Lonafarnib (drug)]] 5 µM in 1 line (HOP62 0.124×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPATCH4]] (+0.78, fdr 7e-06), [[MAK16]] (+0.74, fdr 7e-06), [[COA7]] (+0.74, fdr 7e-06); moves opposite to [[LAPTM4A]] (-0.64, fdr 9e-06), [[SEC11A]] (-0.64, fdr 7e-06), [[DPM1]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1496.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.37×** | +21.5 | 0e+00 | 46/48 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.96×** | +19.0 | 0e+00 | 46/48 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.76×** | +17.2 | 0e+00 | 46/48 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.57×** | +16.5 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.36×** | +15.1 | 0e+00 | 43/45 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.30×** | +14.0 | 8e-43 | 38/40 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.98×** | +12.0 | 4e-31 | 44/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +11.3 | 1e-27 | 37/45 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.52×** | +6.8 | 8e-10 | 33/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +6.3 | 2e-08 | 32/47 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +6.2 | 3e-08 | 31/47 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.42×** | +5.9 | 2e-07 | 27/47 (NCI-H1573, Panc 03.27, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.41×** | +5.8 | 3e-07 | 31/47 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.38×** | +5.6 | 7e-07 | 29/48 (NCI-H1573, Hs 766T, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +5.2 | 6e-06 | 27/47 (PANC-1, A-172, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.62×** | +4.4 | 3e-04 | 23/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.28×** | +4.3 | 4e-04 | 21/47 (HOP62, CFPAC-1, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.004 | 17/48 (CFPAC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.004 | 20/48 (NCI-H1573, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.006 | 19/47 (HT-29, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.006 | 16/47 (CFPAC-1, SW1417, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1496.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 1 line (CHP-212 0.0770×; ⚠ transcription drop); [[Simotinib (drug)]] 5 µM in 1 line (AN3 CA 0.0890×; ⚠ toxic); [[Lonafarnib (drug)]] 5 µM in 1 line (HOP62 0.124×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.811×** | -5.2 | 1e-04 | 27/48 (Hs 766T, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.852× | -4.0 | 0.020 | 20/48 (J82, LoVo, …) | top dose only | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -3.7 | 0.036 | 4/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Minodronic acid (drug)]] 0.05 µM |  | **0.802×** | -3.7 | 0.036 | 15/48 (NCI-H1792, J82, …) | inconsistent across doses | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 0.869× | -3.5 | 0.050 | 11/48 (NCI-H1573, SHP-77, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 0.828× | -3.2 | 0.12 | 15/47 (SK-MEL-2, C-33 A, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.829× | -3.2 | 0.12 | 13/47 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.836× | -3.1 | 0.12 | 13/47 (SW48, A-427, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1496. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 28.4 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +13.9) | — |
| [[HT-29 (line)]] | alt | 47.2 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +13.5) | — |
| [[LoVo (line)]] | wt | 48.2 | 6 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.43× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.21× (z +11.1) | — |
| [[NCI-H2347 (line)]] | alt | 38.4 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +15.2) | — |
| [[HOP62 (line)]] | alt | 31.5 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.18× (z +16.0) | [[Lonafarnib (drug)]] 5 µM 0.124× (z -9.6) ⚠ toxic |
| [[J82 (line)]] | alt | 80.5 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +16.1) | [[Selinexor (drug)]] 5 µM 0.559× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 41.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.74× (z +14.8) | — |
| [[Panc 03.27 (line)]] | alt | 38.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.19× (z +14.0) | — |
| [[PANC-1 (line)]] | alt | 49.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.3) | — |
| [[SW480 (line)]] | alt | 63.1 | 5 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.22× (z +13.4) | — |
| [[A498 (line)]] | wt | 39.0 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.77× (z +9.8) | — |
| [[A549 (line)]] | wt | 34.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +10.7) | — |
| [[KATO III (line)]] | alt | 40.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 50.7 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.30× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 27.5 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.45× (z +9.2) | — |
| [[A-172 (line)]] | wt | 31.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 30.8 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.40× (z +16.8) | — |
| [[H4 (line)]] | wt | 33.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +13.1) | — |
| [[HEC-1-A (line)]] | alt | 40.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +13.6) | — |
| [[Hs 766T (line)]] | wt | 37.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.49× (z +12.1) | — |
| [[LOX-IMVI (line)]] | wt | 46.8 | 3 | 0 | [[Harringtonine (drug)]] 0.5 µM 4.83× (z +12.4) | — |
| [[NCI-H460 (line)]] | wt | 40.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.94× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 2.62× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 32.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 33.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.38× (z +9.1) | — |
| [[COLO 205 (line)]] | alt | 26.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +12.0) | — |
| [[HS-578T (line)]] | alt | 23.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 53.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2030 (line)]] | alt | 27.3 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.03× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 44.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.38× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 33.1 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.80× (z +10.0) | — |
| [[AN3 CA (line)]] | alt | 68.9 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0890× (z -13.3) ⚠ toxic |
| [[C32 (line)]] | wt | 33.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.7) | — |
| [[CHP-212 (line)]] | wt | 60.4 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0770× (z -13.3) ⚠ transcription drop |
| [[HCT15 (line)]] | alt | 67.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HepG2_C3A (line)]] | wt | 36.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 34.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 100 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 69.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 93.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1496), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH4]] | +0.78 | +0.82 / +0.76 | both halves | 7e-06 | STRING 551 |
| [[MAK16]] | +0.74 | +0.80 / +0.68 | both halves | 7e-06 | STRING 880 |
| [[COA7]] | +0.74 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[MGA]] | +0.74 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[RBM28]] | +0.71 | +0.74 / +0.73 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 946 |
| [[UTP14A]] | +0.71 | +0.80 / +0.67 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 998 |
| [[DDX10]] | +0.71 | +0.71 / +0.76 | both halves | 7e-06 | same gene group; pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 952 |
| [[RAD50]] | +0.71 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[ABCE1]] | +0.71 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.71 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[LTV1]] | +0.70 | +0.73 / +0.67 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 976 |
| [[NOC3L]] | +0.70 | +0.72 / +0.70 | both halves | 7e-06 | STRING 874 |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAPTM4A]] | -0.64 | -0.69 / -0.57 | both halves | 9e-06 |  |
| [[SEC11A]] | -0.64 | -0.69 / -0.60 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[DPM1]] | -0.62 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[MOSPD3]] | -0.62 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | -0.61 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[ADIPOR1]] | -0.61 | -0.67 / -0.61 | both halves | 7e-06 |  |
| [[RAB6A]] | -0.60 | -0.67 / -0.56 | both halves | 1e-05 |  |
| [[GNB2]] | -0.60 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[CBFA2T2]] | -0.59 | -0.72 / -0.52 | both halves | 1e-05 |  |
| [[NENF]] | -0.59 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[NDUFA2]] | -0.59 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[SERF2]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.795). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.2, -37.1); signed map (0.9, -42.1). **Vector** length 101, 29.5% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.57 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.5 | +16.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.0 | +19.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.6 | +12.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.8 | +17.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +6.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.9 | +5.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.5 | +6.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +4.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +3.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.9 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | +0.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.8 | +2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -1.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.7 | -2.6 |
|  | [[Decitabine (drug)]] 0.05 µM |  | -1.6 | -0.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | NOP14 nucleolar protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:2,937,933-2,963,406 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RES4-25, UTP2; previously C4orf9, NOL14 |
| Gene groups (HGNC) | SSU processome |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [P78316](https://www.uniprot.org/uniprotkb/P78316) (Nucleolar protein 14):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome. Involved in nucleolar processing of pre-18S ribosomal RNA (By …

**Summary**, from NCBI Gene [8602](https://www.ncbi.nlm.nih.gov/gene/8602):

> This gene encodes a protein that plays a role in pre-18s rRNA processing and small ribosomal subunit assembly. The encoded protein may be involved in the regulation of pancreatic cancer cell proliferation and migration. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2014]

**Accessions** — [HGNC:16821](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16821) · Entrez [8602](https://www.ncbi.nlm.nih.gov/gene/8602) · UniProt [P78316](https://www.uniprot.org/uniprotkb/P78316) · Ensembl [ENSG00000087269](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087269)

## Data

Gene col 1496: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1496); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1496, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1496]; `tensor/DDL_lfc|DDL_z.npy` [1496]; `embed/gene_vectors.npy` [1496]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1496 or target_col == 1496). Every well: [[NOP14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOP14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

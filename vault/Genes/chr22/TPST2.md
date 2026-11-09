---
symbol: "TPST2"
type: "gene"
col: 4873
ensembl_id: "ENSG00000128294"
name: "tyrosylprotein sulfotransferase 2"
location: "22q12.1"
module: 2
arm: "+"
pooled_cpm: 20.5
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TPST2

*tyrosylprotein sulfotransferase 2* — 22q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.02× (z +24.9, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.381× (z -21.7, q 0e+00, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO9B]] (+0.73, fdr 1e-05), [[GNA12]] (+0.71, fdr 1e-05), [[LIMK1]] (+0.71, fdr 7e-06); moves opposite to [[CLK4]] (-0.72, fdr 7e-06), [[NFYC]] (-0.71, fdr 1e-05), [[LATS1]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4873.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.02×** | +24.9 | 0e+00 | 46/48 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.68×** | +22.2 | 0e+00 | 47/48 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.54×** | +21.0 | 0e+00 | 48/48 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +12.0 | 4e-31 | 39/48 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.60×** | +10.6 | 3e-24 | 32/46 (Panc 03.27, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +8.9 | 5e-17 | 25/48 (MIA PaCa-2, C32, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.96×** | +7.9 | 2e-13 | 26/48 (PANC-1, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.95×** | +7.9 | 3e-13 | 24/41 (Panc 03.27, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.38×** | +6.8 | 6e-10 | 21/47 (SW1417, KATO III, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +6.2 | 3e-08 | 16/48 (SW1417, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +5.6 | 9e-07 | 20/48 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +5.0 | 3e-05 | 18/48 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.24×** | +4.9 | 4e-05 | 14/47 (C32, KATO III, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | **1.22×** | +4.6 | 2e-04 | 11/48 (NCI-H23, A549, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.003 | 14/48 (C32, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.042 | 4/47 (SW1417, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4873.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.381×** | -21.7 | 0e+00 | 40/46 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.397×** | -20.0 | 0e+00 | 37/47 (RKO, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.558×** | -18.6 | 0e+00 | 37/47 (A498, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.476×** | -16.7 | 0e+00 | 35/48 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.342×** | -12.6 | 2e-34 | 32/48 (LS 180, NCI-H1792, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.599×** | -11.5 | 9e-29 | 30/48 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.564×** | -6.7 | 1e-09 | 20/46 (KATO III, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.828×** | -6.0 | 1e-07 | 21/48 (CFPAC-1, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.771×** | -5.4 | 4e-06 | 19/46 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.664×** | -4.8 | 8e-05 | 11/45 (A549, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.823×** | -4.4 | 6e-04 | 16/46 (KATO III, RPMI-7951, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 0.892× | -3.7 | 0.012 | 5/48 (HS-578T, hTERT-HPNE, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.5 µM |  | 0.855× | -3.5 | 0.019 | 11/48 (NCI-H1573, SW48, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.857× | -3.3 | 0.035 | 11/48 (NCI-H2347, CHP-212, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.867× | -3.2 | 0.049 | 12/47 (A498, HOP62, …) | inconsistent across doses |  |
| [[NVP-BHG712 (drug)]] 0.5 µM |  | **0.820×** | -3.2 | 0.051 | 7/48 (A498, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 0.05 µM |  | 0.862× | -3.2 | 0.054 | 5/48 (SW48, NCI-H460, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.906× | -3.1 | 0.054 | 13/48 (A-427, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4873. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 56.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -17.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.260× (z -16.3) |
| [[LOX-IMVI (line)]] | wt | 17.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -14.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.238× (z -9.3) |
| [[PANC-1 (line)]] | alt | 8.50 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.08× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -10.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.315× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 43.7 | 0 | 5 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.185× (z -11.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -10.9) |
| [[SW480 (line)]] | alt | 21.6 | 1 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.78× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -10.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.329× (z -9.5) |
| [[HOP62 (line)]] | alt | 26.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 8.32 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.66× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 34.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.95× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[HS-578T (line)]] | alt | 34.6 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.00× (z +8.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.221× (z -12.1) |
| [[KATO III (line)]] | alt | 20.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.268× (z -8.9) |
| [[SNU-423 (line)]] | alt | 22.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.15× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -8.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW1417 (line)]] | alt | 20.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.29× (z +12.5) | — |
| [[A549 (line)]] | wt | 15.4 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.191× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 6.33 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.51× (z +9.3) | — |
| [[LoVo (line)]] | wt | 20.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.230× (z -12.1) |
| [[LS 180 (line)]] | wt | 27.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.313× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 17.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -14.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.245× (z -10.5) |
| [[A-172 (line)]] | wt | 14.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -10.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 12.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -10.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HCT15 (line)]] | alt | 11.4 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.104× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 18.8 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.95× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.215× (z -9.0) |
| [[J82 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -10.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[MIA PaCa-2 (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 12.7 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.240× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -14.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[RKO (line)]] | wt | 19.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0335× (z -20.8) |
| [[SHP-77 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.130× (z -8.8) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[AN3 CA (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4873), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO9B]] | +0.73 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[GNA12]] | +0.71 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[LIMK1]] | +0.71 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[PRR5]] | +0.70 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[CYTH3]] | +0.70 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[CORO7]] | +0.70 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[TCF3]] | +0.69 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.68 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[PIP4K2A]] | +0.68 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[IGSF8]] | +0.68 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[TMEM184B]] | +0.67 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[FAM20B]] | +0.66 | +0.70 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*62 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLK4]] | -0.72 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[NFYC]] | -0.71 | -0.62 / -0.56 | both halves | 1e-05 | same gene group |
| [[LATS1]] | -0.70 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[ZNF518A]] | -0.69 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | -0.69 | -0.75 / -0.35 | both halves | 1e-04 |  |
| [[BCLAF1]] | -0.69 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[ZNF620]] | -0.68 | -0.74 / -0.53 | both halves | 1e-05 |  |
| [[PATL2]] | -0.67 | -0.65 / -0.46 | both halves | 2e-05 |  |
| [[LEKR1]] | -0.67 | -0.71 / -0.43 | both halves | 3e-05 |  |
| [[ANKRD26]] | -0.67 | -0.73 / -0.48 | both halves | 2e-05 |  |
| [[KRCC1]] | -0.67 | -0.72 / -0.41 | both halves | 4e-05 |  |
| [[WDR33]] | -0.67 | -0.58 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.650). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (2.3, 3.3); signed map (-42.5, -5.8). **Vector** length 106, 25.5% of its response variance represented; |z| ≥ 3 in 1,238 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.3 | +21.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.2 | +22.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.1 | +24.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.9 | +10.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +8.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +7.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.8 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.1 | -21.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.1 | -20.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -8.9 | -18.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.5 | -16.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.7 | -11.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -6.7 |

## What is on record

|  |  |
|---|---|
| Name | tyrosylprotein sulfotransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.1 — chr22:26,521,996-26,596,717 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TANGO13B |
| Gene groups (HGNC) | Sulfotransferases, membrane bound; MicroRNA protein coding host genes |
| Hallmark sets | HYPOXIA |
| Reactome | 10 pathways, smallest: Defective F8 sulfation at Y1699; Defective factor VIII causes hemophilia A; Differentiation of naive CD4+ T cells to T helper 1 cells (Th1 cells) |
| Matched by | ensembl_id |

**Function**, from UniProt [O60704](https://www.uniprot.org/uniprotkb/O60704) (Protein-tyrosine sulfotransferase 2):

> Catalyzes the O-sulfation of tyrosine residues within acidic motifs of polypeptides, using 3'-phosphoadenylyl sulfate (PAPS) as cosubstrate.

**Summary**, from NCBI Gene [8459](https://www.ncbi.nlm.nih.gov/gene/8459):

> The protein encoded by this gene catalyzes the O-sulfation of tyrosine residues within acidic regions of proteins. The encoded protein is a type II integral membrane protein found in the Golgi body. Alternative splicing produces multiple transcript variants encoding distinct isoforms. [provided by RefSeq, May 2018]

**Accessions** — [HGNC:12021](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12021) · Entrez [8459](https://www.ncbi.nlm.nih.gov/gene/8459) · UniProt [O60704](https://www.uniprot.org/uniprotkb/O60704) · Ensembl [ENSG00000128294](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128294)

## Data

Gene col 4873: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4873); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4873, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4873]; `tensor/DDL_lfc|DDL_z.npy` [4873]; `embed/gene_vectors.npy` [4873]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4873 or target_col == 4873). Every well: [[TPST2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPST2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

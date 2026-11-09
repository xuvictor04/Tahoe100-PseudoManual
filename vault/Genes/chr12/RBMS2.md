---
symbol: "RBMS2"
type: "gene"
col: 1143
ensembl_id: "ENSG00000076067"
name: "RNA binding motif single stranded interacting protein 2"
location: "12q13.3"
module: 120
arm: "+"
pooled_cpm: 81.39
n_lines_expressing: 47
n_dd_up: 2
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# RBMS2

*RNA binding motif single stranded interacting protein 2* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.31× (z +5.7, q 7e-06, up in 24 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 3.33×, MIA PaCa-2 2.78×; ⚠ cell-cycle shift, explains ~4% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 2.66×; ⚠ cell-cycle shift, explains ~0% of this change); [[Daptomycin (drug)]] 5 µM in 1 line (NCI-H1573 3.08×; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 2.21×).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.494× (z -20.9, q 0e+00, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP18]] (+0.61, fdr 1e-05), [[KRT80]] (+0.57, fdr 3e-05), [[LIMA1]] (+0.57, fdr 3e-05); moves opposite to [[FAM219A]] (-0.52, fdr 3e-05), [[C9orf24]] (-0.49, fdr 3e-05), [[KCNMA1]] (-0.47, fdr 8e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC01836]] → it (grade B ⚠); 3 go from it, the strongest it → [[LATS2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1143.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 3.33×, MIA PaCa-2 2.78×; ⚠ cell-cycle shift, explains ~4% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 2.66×; ⚠ cell-cycle shift, explains ~0% of this change); [[Daptomycin (drug)]] 5 µM in 1 line (NCI-H1573 3.08×; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 2.21×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +5.7 | 7e-06 | 24/46 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[NG25 (drug)]] 5 µM |  | **1.55×** | +4.8 | 5e-04 | 21/44 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.4 | 0.002 | 18/45 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.7 | 0.034 | 16/45 (AsPC-1, A-427, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.14 | 16/45 (A-172, A498, …) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | 1.17× | +3.1 | 0.14 | 6/45 (NCI-H460, C-33 A, …) | top dose only | plate-row cell shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.14 | 16/46 (SW 900, NCI-H2347, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.14 | 18/40 (A-427, NCI-H2347, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1143.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.494×** | -20.9 | 0e+00 | 42/46 (SW1417, RKO, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.561×** | -12.1 | 2e-31 | 41/45 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.556×** | -11.9 | 4e-30 | 35/45 (BT-474, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.601×** | -10.1 | 8e-22 | 33/45 (NCI-H460, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.625×** | -9.9 | 7e-21 | 32/45 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.643×** | -9.3 | 2e-18 | 31/45 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.707×** | -7.3 | 3e-11 | 30/45 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.548×** | -6.6 | 3e-09 | 22/41 (NCI-H460, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.557×** | -6.4 | 9e-09 | 33/45 (NCI-H460, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.751×** | -5.8 | 4e-07 | 28/47 (SNU-1, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.833×** | -5.4 | 3e-06 | 21/45 (NCI-H1573, AsPC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.773×** | -5.4 | 3e-06 | 24/45 (SNU-1, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.776×** | -5.3 | 5e-06 | 23/45 (SNU-1, NCI-H460, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.627×** | -5.1 | 1e-05 | 23/45 (NCI-H460, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.627×** | -5.1 | 1e-05 | 21/45 (NCI-H460, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.788×** | -5.0 | 2e-05 | 20/45 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.642×** | -4.9 | 4e-05 | 23/45 (SW1417, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.805×** | -4.4 | 4e-04 | 20/44 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.876× | -3.9 | 0.002 | 13/45 (SNU-1, SW 1271, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.807×** | -3.2 | 0.034 | 7/46 (A498, NCI-H460, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | 0.898× | -3.2 | 0.034 | 5/45 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1143. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 157 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -19.0) |
| [[SNU-1 (line)]] | wt | 238 | 0 | 8 (6 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.162× (z -22.0) |
| [[AsPC-1 (line)]] | alt | 97.5 | 0 | 7 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.284× (z -12.6) |
| [[A-427 (line)]] | wt | 99.3 | 4 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +19.0) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.21× (z +8.8) | [[Auranofin (drug)]] 5 µM 0.406× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 130 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -14.6) |
| [[NCI-H1573 (line)]] | alt | 78.7 | 2 (2 ⚠) | 3 (2 ⚠) | [[Daptomycin (drug)]] 5 µM 3.08× (z +9.6) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -14.9) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -13.3) |
| [[SW1417 (line)]] | alt | 148 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -19.5) |
| [[NCI-H2030 (line)]] | alt | 118 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -12.1) |
| [[CFPAC-1 (line)]] | alt | 128 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -15.8) |
| [[HT-29 (line)]] | alt | 136 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -16.9) |
| [[LoVo (line)]] | wt | 119 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -18.2) |
| [[HCT15 (line)]] | alt | 96.2 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.308× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 105 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -16.6) |
| [[LS 180 (line)]] | wt | 72.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -15.4) |
| [[Panc 03.27 (line)]] | alt | 195 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -11.7) |
| [[SW480 (line)]] | alt | 111 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -18.2) |
| [[A549 (line)]] | wt | 107 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -12.6) |
| [[BT-474 (line)]] | alt | 41.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -10.4) |
| [[KATO III (line)]] | alt | 52.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 33.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.8) ⚠ cell-cycle shift, explains ~4% of this change | — |
| [[NCI-H1792 (line)]] | alt | 29.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.2) |
| [[NCI-H661 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 71.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -19.3) |
| [[A-172 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.3 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 74.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 125 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.2 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1143), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP18]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[KRT80]] | +0.57 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[LIMA1]] | +0.57 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[IL18]] | +0.57 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[CCN2]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[LATS2]] | +0.56 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CCN1]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[NCEH1]] | +0.54 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[CRIM1]] | +0.54 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[AMOTL2]] | +0.54 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[DDAH1]] | +0.53 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[PICALM]] | +0.52 | +0.48 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM219A]] | -0.52 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[C9orf24]] | -0.49 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[KCNMA1]] | -0.47 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[ITPR1]] | -0.44 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[NRSN2-AS1]] | -0.44 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[ZFAND2A]] | -0.44 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[QPCTL]] | -0.43 | -0.29 / -0.50 | both halves | 3e-04 |  |
| [[DUSP28]] | -0.41 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[NPIPB12]] | -0.41 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[VEGFA]] | -0.40 | -0.20 / -0.46 | ⚠ not reproduced | 8e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01836]] | B | LINC01836 activity raises RBMS2's level | lines that do not express LINC01836 (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without LINC01836 | 0.002 | ⚠ within organs, on part of the lines; also absent: ANXA3, SLC9A2, SHROOM3 |
| [[ANXA3]] | B | ANXA3 activity raises RBMS2's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 1.82× lower at baseline in the lines without ANXA3 | 0.016 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[EDN1]] | B | EDN1 activity raises RBMS2's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 1.77× lower at baseline in the lines without EDN1 | 0.060 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[SH2D3A]] | B | SH2D3A activity raises RBMS2's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 1.68× lower at baseline in the lines without SH2D3A | 0.098 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[LRRC1]] | C | LRRC1 activity strengthens RBMS2's drug response | lines that do not express LRRC1 (3) vs lines expressing it (44) | the lines without LRRC1 respond 0.41× as strongly (z diff +2.98); strongest at Auranofin 5 µM: 0.74x vs 0.51x (z diff +4.7) | 0.081 | ⚠ few lines (3 vs 47); across organs; also absent: CYP2E1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LATS2]] | C | RBMS2 activity raises LATS2's level | lines that do not express RBMS2 (3) vs lines expressing it (47) | 3.97× lower at baseline in the lines without RBMS2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: HOMER3, ARHGAP10, TMEM144; maybe low, not absent; its own permutation p |
| [[AMOTL2]] | C | RBMS2 activity raises AMOTL2's level | lines that do not express RBMS2 (3) vs lines expressing it (47) | 2.82× lower at baseline in the lines without RBMS2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: HOMER3, ARHGAP10, TMEM144; maybe low, not absent; its own permutation p |
| [[ADGRG6]] | C | RBMS2 activity raises ADGRG6's level | lines that do not express RBMS2 (3) vs lines expressing it (47) | 5.00× lower at baseline in the lines without RBMS2 | 0.095 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: HOMER3, ARHGAP10, TMEM144; maybe low, not absent |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.572). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.0, 11.8); signed map (48.8, 15.8). **Vector** length 121, 34.0% of its response variance represented; |z| ≥ 3 in 1,210 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.7 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.0 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.9 | +0.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +5.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +0.6 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +1.7 | +1.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.0 | -9.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -20.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.4 | -9.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.3 | -10.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.9 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -12.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -7.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.2 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.4 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif single stranded interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:56,521,820-56,596,193 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SCR3 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

UniProt [Q15434](https://www.uniprot.org/uniprotkb/Q15434) carries no function annotation.

**Summary**, from NCBI Gene [5939](https://www.ncbi.nlm.nih.gov/gene/5939):

> The protein encoded by this gene is a member of a small family of proteins which bind single stranded DNA/RNA. These proteins are characterized by the presence of two sets of ribonucleoprotein consensus sequence (RNP-CS) that contain conserved motifs, RNP1 and RNP2, originally described in RNA binding proteins, and required for DNA binding. The RBMS proteins have been implicated in such diverse functions as DNA replication, gene transcription, cell cycle progression and apoptosis. This protein …

**Accessions** — [HGNC:9909](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9909) · Entrez [5939](https://www.ncbi.nlm.nih.gov/gene/5939) · UniProt [Q15434](https://www.uniprot.org/uniprotkb/Q15434) · Ensembl [ENSG00000076067](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076067)

## Data

Gene col 1143: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1143); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1143, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1143]; `tensor/DDL_lfc|DDL_z.npy` [1143]; `embed/gene_vectors.npy` [1143]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1143 or target_col == 1143). Every well: [[RBMS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBMS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

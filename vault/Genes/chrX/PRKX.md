---
symbol: "PRKX"
type: "gene"
col: 11473
ensembl_id: "ENSG00000183943"
name: "protein kinase cAMP-dependent X-linked catalytic subunit"
location: "Xp22.33"
module: 18
arm: "+"
pooled_cpm: 40.21
n_lines_expressing: 47
n_dd_up: 3
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PRKX

*protein kinase cAMP-dependent X-linked catalytic subunit* — Xp22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Lonafarnib (drug)]] 5 µM: 1.41× (z +5.3, q 2e-05, up in 10 of 31 measured lines) ⚠ toxic. The strongest without an alert is [[Betamethasone dipropionate (drug)]] 5 µM: 1.21× (z +5.3, q 2e-05, up in 17 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 5 lines (LS 180 9.01×, A-172 8.60×, NCI-H460 4.04×, A498 7.64×, …); [[PH-797804 (drug)]] 5 µM in 2 lines (LS 180 7.97×, SW48 5.95×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 3.15×, NCI-H460 1.96×; ⚠ cell-cycle shift, explains ~14% of this change); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 3.25×).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.268× (z -54.9, q 0e+00, down in 43 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PVT1]] (+0.61, fdr 1e-05), [[ANKRD13B]] (+0.61, fdr 1e-05), [[UCK2]] (+0.58, fdr 1e-05); moves opposite to [[SUB1]] (-0.51, fdr 3e-05), [[SGO1-AS1]] (-0.50, fdr 3e-05), [[ATXN1]] (-0.49, fdr 2e-04).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NCS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11473.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 5 lines (LS 180 9.01×, A-172 8.60×, NCI-H460 4.04×, A498 7.64×, …); [[PH-797804 (drug)]] 5 µM in 2 lines (LS 180 7.97×, SW48 5.95×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 3.15×, NCI-H460 1.96×; ⚠ cell-cycle shift, explains ~14% of this change); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 3.25×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +5.3 | 2e-05 | 10/31 (A549, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.21×** | +5.3 | 2e-05 | 17/45 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.20× | +5.3 | 2e-05 | 13/44 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +4.8 | 2e-04 | 17/45 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +4.4 | 0.001 | 8/45 (SHP-77, HT-29, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.15× | +4.1 | 0.003 | 16/44 (HS-578T, H4, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.14× | +3.8 | 0.012 | 15/44 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.14× | +3.8 | 0.012 | 4/45 (BT-474, RKO, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.039 | 5/44 (NCI-H1573, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 1.12× | +3.2 | 0.064 | 12/45 (H4, HS-578T, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.12× | +3.2 | 0.064 | 5/45 (A549, Panc 03.27, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.12× | +3.1 | 0.079 | 16/43 (HS-578T, H4, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.08× | +3.0 | 0.10 | 8/45 (H4, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11473.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.268×** | -54.9 | 0e+00 | 43/45 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.303×** | -33.8 | 0e+00 | 44/45 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.548×** | -25.0 | 0e+00 | 37/45 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.435×** | -22.8 | 0e+00 | 36/45 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.538×** | -18.2 | 0e+00 | 34/45 (MIA PaCa-2, SW48, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.547×** | -17.8 | 0e+00 | 35/45 (BT-474, SW48, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.638×** | -13.2 | 6e-38 | 31/45 (BT-474, SW48, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.670×** | -11.8 | 3e-30 | 28/45 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.696×** | -10.2 | 9e-23 | 25/44 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.719×** | -9.7 | 2e-20 | 26/45 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.752×** | -8.4 | 3e-15 | 21/45 (NCI-H23, SNU-423, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.921× | -8.0 | 4e-14 | 4/46 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.776×** | -7.5 | 4e-12 | 19/43 (KATO III, BT-474, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.785×** | -6.8 | 3e-10 | 22/43 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.795×** | -6.7 | 6e-10 | 18/45 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.826×** | -5.4 | 2e-06 | 16/45 (LS 180, SNU-423, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.708×** | -5.3 | 3e-06 | 15/46 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.855× | -4.6 | 1e-04 | 13/45 (RKO, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11473. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 83.7 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0919× (z -26.2) |
| [[HEC-1-A (line)]] | alt | 54.4 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -28.0) |
| [[NCI-H460 (line)]] | wt | 66.1 | 4 (2 ⚠) | 6 | [[TAK-901 (drug)]] 5 µM 4.04× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -24.1) |
| [[SW48 (line)]] | wt | 126 | 3 | 7 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.25× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -20.9) |
| [[BT-474 (line)]] | alt | 56.4 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -28.2) |
| [[SNU-423 (line)]] | alt | 52.0 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -21.7) |
| [[KATO III (line)]] | alt | 67.2 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -20.9) |
| [[RKO (line)]] | wt | 110 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -33.2) |
| [[A549 (line)]] | wt | 50.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -21.4) |
| [[SW480 (line)]] | alt | 69.1 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -20.3) |
| [[A-172 (line)]] | wt | 54.3 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 8.60× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -22.8) |
| [[A-427 (line)]] | wt | 40.7 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.308× (z -11.4) |
| [[A498 (line)]] | wt | 22.6 | 2 (1 ⚠) | 3 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +10.0) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.64× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -15.4) |
| [[C-33 A (line)]] | alt | 87.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -11.1) |
| [[LoVo (line)]] | wt | 57.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -17.9) |
| [[LS 180 (line)]] | wt | 59.4 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 9.01× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -10.8) |
| [[PANC-1 (line)]] | alt | 24.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -32.4) |
| [[J82 (line)]] | alt | 40.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -23.7) |
| [[HOP62 (line)]] | alt | 15.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -16.8) |
| [[Hs 766T (line)]] | wt | 60.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -24.9) |
| [[LOX-IMVI (line)]] | wt | 25.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -19.0) |
| [[NCI-H23 (line)]] | alt | 31.4 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.180× (z -14.7) |
| [[NCI-H2347 (line)]] | alt | 26.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 35.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -15.6) |
| [[SW1417 (line)]] | alt | 32.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -19.0) |
| [[AsPC-1 (line)]] | alt | 15.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -12.1) |
| [[COLO 205 (line)]] | alt | 27.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.122× (z -13.0) |
| [[H4 (line)]] | wt | 41.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -12.2) |
| [[HS-578T (line)]] | alt | 19.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -15.6) |
| [[NCI-H1573 (line)]] | alt | 16.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 31.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -20.0) |
| [[AN3 CA (line)]] | alt | 88.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 17.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -10.5) |
| [[CHP-212 (line)]] | wt | 80.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0864× (z -17.8) |
| [[HCT15 (line)]] | alt | 37.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -12.6) |
| [[HT-29 (line)]] | alt | 23.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -16.1) |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -10.0) |
| [[C32 (line)]] | wt | 3.44 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.68 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11473), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PVT1]] | +0.61 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[ANKRD13B]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[UCK2]] | +0.58 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[PARD6G]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[WDR43]] | +0.57 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[RCL1]] | +0.55 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ADAMTS7]] | +0.55 | +0.31 / +0.61 | both halves | 2e-04 |  |
| [[GARNL3]] | +0.54 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[EI24]] | +0.54 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[EBPL]] | +0.53 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[USP31]] | +0.53 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[NTPCR]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUB1]] | -0.51 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[SGO1-AS1]] | -0.50 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[ATXN1]] | -0.49 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[CGGBP1]] | -0.44 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[SMIM14]] | -0.44 | -0.51 / -0.37 | both halves | 9e-05 |  |
| [[TLR6]] | -0.44 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[MED29]] | -0.44 | -0.46 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCS1]] | B | NCS1 activity strengthens PRKX's drug response | lines that do not express NCS1 (5) vs lines expressing it (40) | the lines without NCS1 respond 0.56× as strongly (z diff +2.56); strongest at Panobinostat 5 µM: 0.94x vs 0.51x (z diff +5.3) | 0.096 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.561). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-2.4, -1.3); signed map (-4.9, -55.2). **Vector** length 106, 27.1% of its response variance represented; |z| ≥ 3 in 1,181 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.5 | -1.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +1.2 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.7 | +5.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +4.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.1 | +1.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.9 | +3.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +2.7 | +2.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.8 | -33.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -11.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.4 | -54.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -22.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.3 | -25.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -6.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.4 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | -8.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase cAMP-dependent X-linked catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.33 — chrX:3,604,340-3,713,649 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PKX1 |
| Gene groups (HGNC) | Protein kinase A family |
| Reactome | 24 pathways, smallest: CREB1 phosphorylation through the activation of Adenylate Cyclase; PKA-mediated phosphorylation of CREB; FCGR3A-mediated IL10 synthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P51817](https://www.uniprot.org/uniprotkb/P51817) (cAMP-dependent protein kinase catalytic subunit PRKX):

> Serine/threonine protein kinase regulated by and mediating cAMP signaling in cells. Acts through phosphorylation of downstream targets that may include CREB, SMAD6 and PKD1 and has multiple functions in cellular differentiation and epithelial morphogenesis. Regulates myeloid cell differentiation through SMAD6 phosphorylation. Involved in nephrogenesis by stimulating renal epithelial cell migration and tubulogenesis. Also involved in angiogenesis through stimulation of endothelial cell …

**Summary**, from NCBI Gene [5613](https://www.ncbi.nlm.nih.gov/gene/5613):

> This gene encodes a serine threonine protein kinase that has similarity to the catalytic subunit of cyclic AMP dependent protein kinases. The encoded protein is developmentally regulated and may be involved in renal epithelial morphogenesis. This protein may also be involved in macrophage and granulocyte maturation. Abnormal recombination between this gene and a related pseudogene on chromosome Y is a frequent cause of sex reversal disorder in XX males and XY females. Pseudogenes of this gene …

**Accessions** — [HGNC:9441](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9441) · Entrez [5613](https://www.ncbi.nlm.nih.gov/gene/5613) · UniProt [P51817](https://www.uniprot.org/uniprotkb/P51817) · Ensembl [ENSG00000183943](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183943)

## Data

Gene col 11473: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11473); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11473, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11473]; `tensor/DDL_lfc|DDL_z.npy` [11473]; `embed/gene_vectors.npy` [11473]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11473 or target_col == 11473). Every well: [[PRKX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

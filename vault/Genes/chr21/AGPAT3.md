---
symbol: "AGPAT3"
type: "gene"
col: 8323
ensembl_id: "ENSG00000160216"
name: "1-acylglycerol-3-phosphate O-acyltransferase 3"
location: "21q22.3"
module: 18
arm: "+"
pooled_cpm: 81.97
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 23
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# AGPAT3

*1-acylglycerol-3-phosphate O-acyltransferase 3* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.27× (z +20.2, q 0e+00, up in 37 of 50 measured lines) ⚠ position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 13 lines (A498 1.34×, PANC-1 1.30×, A-172 1.31×, SW480 1.31×, …; ⚠ position not correctable); [[Citalopram (hydrobromide) (drug)]] 0.05 µM in 1 line (NCI-H596 2.65×); [[Harringtonine (drug)]] 5 µM in 1 line (HOP62 2.31×); [[Salicylic acid (drug)]] 0.5 µM in 1 line (NCI-H596 2.04×).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.422× (z -21.3, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTA1]] (+0.64, fdr 1e-05), [[ABCC4]] (+0.64, fdr 7e-06), [[TMEM33]] (+0.62, fdr 1e-05); moves opposite to [[IFI27L2]] (-0.59, fdr 3e-05), [[NOSIP]] (-0.57, fdr 2e-05), [[SIRT2]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8323.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 13 lines (A498 1.34×, PANC-1 1.30×, A-172 1.31×, SW480 1.31×, …; ⚠ position not correctable); [[Citalopram (hydrobromide) (drug)]] 0.05 µM in 1 line (NCI-H596 2.65×); [[Harringtonine (drug)]] 5 µM in 1 line (HOP62 2.31×); [[Salicylic acid (drug)]] 0.5 µM in 1 line (NCI-H596 2.04×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.27×** | +20.2 | 0e+00 | 37/50 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +8.4 | 1e-14 | 28/43 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +7.5 | 8e-12 | 29/49 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.23×** | +5.0 | 7e-05 | 25/49 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Rimonabant (Hydrochloride) (drug)]] 0.05 µM | ⚠ unreliable plate only; position correction uncertain | **1.21×** | +4.8 | 2e-04 | 24/49 (SNU-423, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.006 | 19/45 (BT-474, CFPAC-1, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8323.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.422×** | -21.3 | 0e+00 | 45/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.560×** | -20.2 | 0e+00 | 35/48 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.441×** | -20.2 | 0e+00 | 45/48 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.481×** | -18.0 | 0e+00 | 46/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.484×** | -17.2 | 0e+00 | 37/48 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.574×** | -13.2 | 1e-37 | 39/50 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -12.5 | 3e-34 | 34/49 (RKO, CHP-212, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.622×** | -11.7 | 6e-30 | 30/48 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.639×** | -11.1 | 1e-26 | 36/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.638×** | -10.7 | 7e-25 | 37/47 (HepG2/C3A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.696×** | -8.9 | 2e-17 | 34/48 (SW48, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.518×** | -8.5 | 1e-15 | 33/49 (NCI-H23, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.708×** | -8.2 | 1e-14 | 34/48 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.718×** | -8.2 | 1e-14 | 33/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.720×** | -8.1 | 2e-14 | 34/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.726×** | -7.9 | 8e-14 | 36/48 (BT-474, SW 1271, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.810×** | -5.2 | 7e-06 | 22/48 (PANC-1, SW480, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.678×** | -5.0 | 1e-05 | 28/48 (SW480, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.875× | -4.7 | 8e-05 | 17/48 (RKO, SK-MEL-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.710×** | -4.4 | 2e-04 | 20/49 (RKO, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8323. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 52.7 | 0 | 13 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.175× (z -18.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.177× (z -18.6) |
| [[RKO (line)]] | wt | 133 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -31.8) |
| [[MIA PaCa-2 (line)]] | alt | 138 | 0 | 11 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.126× (z -24.6) |
| [[PANC-1 (line)]] | alt | 55.4 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -17.5) |
| [[NCI-H460 (line)]] | wt | 67.0 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -21.5) |
| [[A-172 (line)]] | wt | 160 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -28.8) |
| [[A-427 (line)]] | wt | 84.5 | 0 | 8 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.217× (z -16.8) |
| [[HEC-1-A (line)]] | alt | 147 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -23.2) |
| [[SW480 (line)]] | alt | 85.4 | 0 | 8 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.278× (z -19.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.412× (z -19.1) |
| [[A498 (line)]] | wt | 95.6 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.91× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -19.2) |
| [[HOP62 (line)]] | alt | 75.3 | 2 | 5 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.31× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.422× (z -12.0) |
| [[LoVo (line)]] | wt | 106 | 1 (1 ⚠) | 6 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.01× (z +9.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.370× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.473× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 67.2 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -21.8) |
| [[NCI-H2030 (line)]] | alt | 89.2 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -12.5) |
| [[SW48 (line)]] | wt | 161 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -16.4) |
| [[A549 (line)]] | wt | 61.4 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.349× (z -11.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.350× (z -11.2) |
| [[J82 (line)]] | alt | 71.2 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -16.3) |
| [[NCI-H1792 (line)]] | alt | 70.1 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +11.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.316× (z -14.2) |
| [[SK-MEL-2 (line)]] | alt | 79.1 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -17.5) |
| [[C-33 A (line)]] | alt | 104 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -10.6) |
| [[C32 (line)]] | wt | 80.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -24.0) |
| [[NCI-H2347 (line)]] | alt | 66.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -17.0) |
| [[NCI-H596 (line)]] | alt | 70.1 | 2 | 3 | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 2.65× (z +14.4) | [[Fulvestrant (drug)]] 5 µM 0.206× (z -24.4) |
| [[BT-474 (line)]] | alt | 104 | 2 (2 ⚠) | 2 | [[Lonafarnib (drug)]] 5 µM 6.39× (z +9.9) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -13.1) |
| [[Hs 766T (line)]] | wt | 55.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.332× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 78.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.354× (z -11.5) |
| [[SW1417 (line)]] | alt | 84.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.423× (z -10.8) |
| [[HS-578T (line)]] | alt | 74.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.422× (z -10.4) |
| [[LS 180 (line)]] | wt | 107 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.424× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.502× (z -8.8) |
| [[SNU-423 (line)]] | alt | 61.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.293× (z -12.7) |
| [[SW 900 (line)]] | alt | 62.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 79.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -8.9) |
| [[H4 (line)]] | wt | 127 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -9.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.410× (z -8.7) |
| [[HT-29 (line)]] | alt | 59.9 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.373× (z -10.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.471× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 66.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 23.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.238× (z -10.6) |
| [[SNU-1 (line)]] | wt | 132 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.447× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.387× (z -8.7) |
| [[SW 1271 (line)]] | alt | 66.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Silodosin (drug)]] 5 µM 0.109× (z -8.9) |
| [[CHP-212 (line)]] | wt | 84.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -13.2) |
| [[COLO 205 (line)]] | alt | 66.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 79.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.153× (z -16.0) ⚠ toxic |
| [[KATO III (line)]] | alt | 52.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 87.5 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0851× (z -9.4) |
| [[AN3 CA (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8323), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTA1]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[ABCC4]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[TMEM33]] | +0.62 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[SCRIB]] | +0.61 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[LARP1]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[GSPT1]] | +0.60 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[DOCK1]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[UBQLN4]] | +0.59 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[G3BP1]] | +0.59 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[LETM1]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[WDR77]] | +0.58 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[TMEM138]] | +0.58 | +0.37 / +0.60 | both halves | 8e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFI27L2]] | -0.59 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[NOSIP]] | -0.57 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[SIRT2]] | -0.57 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[RNF181]] | -0.55 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[TRIM7-AS2]] | -0.55 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[ING2]] | -0.55 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[CCS]] | -0.54 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[POLD4]] | -0.54 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[KLHL28]] | -0.54 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[EXOC1]] | -0.53 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[NDUFA7]] | -0.53 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[NDUFA2]] | -0.53 | -0.21 / -0.53 | both halves | 6e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.566). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.0, -35.5); signed map (-9.1, -43.8). **Vector** length 90.0, 23.0% of its response variance represented; |z| ≥ 3 in 1,282 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.2 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.3 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +8.1 | +4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.1 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.0 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | -0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +1.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.4 | +0.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -17.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.3 | -8.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.2 | -13.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.0 | -10.7 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.8 | -2.0 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.7 | -0.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Omeprazole (sodium) (drug)]] 5 µM |  | -1.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | 1-acylglycerol-3-phosphate O-acyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:43,865,223-43,987,592 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LPAAT-gamma, LPAAT3, LPLAT3 |
| Gene groups (HGNC) | 1-acylglycerol-3-phosphate O-acyltransferases; Lysophospholipid acyltransferases |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 9 pathways, smallest: Synthesis of PA; COPI-independent Golgi-to-ER retrograde traffic; Glycerophospholipid biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRZ7](https://www.uniprot.org/uniprotkb/Q9NRZ7) (1-acyl-sn-glycerol-3-phosphate acyltransferase gamma):

> Converts 1-acyl-sn-glycerol-3-phosphate (lysophosphatidic acid or LPA) into 1,2-diacyl-sn-glycerol-3-phosphate (phosphatidic acid or PA) by incorporating an acyl moiety at the sn-2 position of the glycerol backbone. Acts on LPA containing saturated or unsaturated fatty acids C16:0-C20:4 at the sn-1 position using C18:1, C20:4 or C18:2-CoA as the acyl donor. Also acts on lysophosphatidylcholine, lysophosphatidylinositol and lysophosphatidylserine using C18:1 or C20:4-CoA. Has a preference for …

**Summary**, from NCBI Gene [56894](https://www.ncbi.nlm.nih.gov/gene/56894):

> The protein encoded by this gene is an acyltransferase that converts lysophosphatidic acid into phosphatidic acid, which is the second step in the de novo phospholipid biosynthetic pathway. The encoded protein may be an integral membrane protein. Two transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:326](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:326) · Entrez [56894](https://www.ncbi.nlm.nih.gov/gene/56894) · UniProt [Q9NRZ7](https://www.uniprot.org/uniprotkb/Q9NRZ7) · Ensembl [ENSG00000160216](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160216)

## Data

Gene col 8323: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8323); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8323, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8323]; `tensor/DDL_lfc|DDL_z.npy` [8323]; `embed/gene_vectors.npy` [8323]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8323 or target_col == 8323). Every well: [[AGPAT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGPAT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

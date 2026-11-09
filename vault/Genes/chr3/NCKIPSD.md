---
symbol: "NCKIPSD"
type: "gene"
col: 13125
ensembl_id: "ENSG00000213672"
name: "NCK interacting protein with SH3 domain"
location: "3p21.31"
module: 180
arm: "+"
pooled_cpm: 31.27
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 29
n_dd_up_clean: 0
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# NCKIPSD

*NCK interacting protein with SH3 domain* — 3p21.31

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.346× (z -23.6, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CABIN1]] (+0.72, fdr 1e-05), [[SLC26A6]] (+0.71, fdr 1e-05, ⚠ same locus), [[EFNA3]] (+0.71, fdr 1e-05), [[ENO2]] (+0.69, fdr 1e-05); moves opposite to [[HCG17]] (-0.59, fdr 6e-05), [[GNG12-AS1]] (-0.59, fdr 6e-05), [[AP4S1]] (-0.57, fdr 2e-04).
> It is in [[Module 180]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[KDM4B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13125.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +5.6 | 2e-05 | 2/48 (HOP62, NCI-H2030) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.25× | +3.4 | 0.14 | 11/48 (NCI-H2347, HT-29, …) | top dose only | plate-row cell shift |
| [[Fumaric acid (drug)]] 5 µM |  | 1.25× | +3.3 | 0.14 | 9/48 (HEC-1-A, SNU-1, …) | top dose only | plate-row cell shift; position effect removed |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.23× | +3.2 | 0.14 | 10/48 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Roxadustat (drug)]] 5 µM |  | 1.24× | +3.2 | 0.14 | 17/47 (LS 180, A-427, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.15× | +3.0 | 0.24 | 6/48 (SW480, HS-578T, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13125.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.346×** | -23.6 | 0e+00 | 47/48 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.394×** | -20.7 | 0e+00 | 42/47 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.374×** | -14.9 | 0e+00 | 34/38 (HCT15, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.436×** | -13.1 | 6e-37 | 39/47 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.463×** | -11.7 | 2e-29 | 42/47 (SW480, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.491×** | -10.8 | 5e-25 | 38/48 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.511×** | -10.6 | 3e-24 | 37/44 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.544×** | -9.2 | 2e-18 | 39/48 (C32, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.546×** | -9.2 | 3e-18 | 39/47 (HepG2/C3A, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.545×** | -8.8 | 5e-17 | 29/42 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.697×** | -8.0 | 4e-14 | 35/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.735×** | -6.9 | 3e-10 | 31/48 (J82, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.701×** | -5.6 | 9e-07 | 30/48 (NCI-H23, HEC-1-A, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.513×** | -5.5 | 1e-06 | 28/48 (C32, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.704×** | -5.3 | 4e-06 | 25/46 (MIA PaCa-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.718×** | -5.0 | 2e-05 | 26/47 (A498, NCI-H460, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.766×** | -4.2 | 8e-04 | 23/48 (HEC-1-A, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.769×** | -4.1 | 0.001 | 21/48 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.610×** | -4.1 | 0.001 | 17/47 (LOX-IMVI, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.778×** | -4.0 | 0.002 | 23/48 (SNU-423, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Allantoin (drug)]] 5 µM |  | 0.839× | -3.9 | 0.002 | 19/48 (HEC-1-A, PANC-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13125. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 56.5 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -21.3) |
| [[SNU-423 (line)]] | alt | 42.3 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -22.8) |
| [[HOP62 (line)]] | alt | 37.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -19.9) |
| [[LOX-IMVI (line)]] | wt | 29.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 26.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -17.7) |
| [[C32 (line)]] | wt | 44.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -15.8) |
| [[CFPAC-1 (line)]] | alt | 28.6 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -17.4) |
| [[LS 180 (line)]] | wt | 32.3 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 29.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0918× (z -24.9) |
| [[NCI-H2347 (line)]] | alt | 42.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -13.0) |
| [[RPMI-7951 (line)]] | alt | 60.2 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -18.8) |
| [[NCI-H1573 (line)]] | alt | 19.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 28.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -12.3) |
| [[SW 900 (line)]] | alt | 22.9 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.218× (z -9.7) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -9.1) |
| [[SW480 (line)]] | alt | 34.7 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -20.9) |
| [[A-172 (line)]] | wt | 35.0 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -12.3) |
| [[H4 (line)]] | wt | 24.8 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0757× (z -18.7) |
| [[HCT15 (line)]] | alt | 59.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0982× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -12.6) |
| [[HS-578T (line)]] | alt | 38.1 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 26.4 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -12.1) |
| [[J82 (line)]] | alt | 42.7 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.484× (z -9.0) |
| [[KATO III (line)]] | alt | 23.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -11.5) |
| [[LoVo (line)]] | wt | 28.3 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -12.2) |
| [[RKO (line)]] | wt | 28.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 44.9 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -14.2) |
| [[SNU-1 (line)]] | wt | 48.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -10.6) |
| [[C-33 A (line)]] | alt | 59.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -8.6) |
| [[COLO 205 (line)]] | alt | 21.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -12.6) |
| [[HepG2_C3A (line)]] | wt | 23.5 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0790× (z -13.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -9.5) |
| [[Hs 766T (line)]] | wt | 30.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -13.9) |
| [[HT-29 (line)]] | alt | 22.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -14.1) |
| [[NCI-H2030 (line)]] | alt | 28.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -11.4) |
| [[PANC-1 (line)]] | alt | 19.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -12.7) |
| [[SW1417 (line)]] | alt | 44.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -16.6) |
| [[A549 (line)]] | wt | 19.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -11.5) |
| [[AN3 CA (line)]] | alt | 29.4 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0984× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 33.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -12.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 35.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -10.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13125), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CABIN1]] | +0.72 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[SLC26A6]] | +0.71 | +0.69 / +0.52 | both halves | 1e-05 | ⚠ same locus (38.4 kb, same strand: neighbours can correlate without regulation) |
| [[EFNA3]] | +0.71 | +0.76 / +0.52 | both halves | 1e-05 |  |
| [[ENO2]] | +0.69 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[HILPDA]] | +0.67 | +0.73 / +0.46 | both halves | 2e-05 |  |
| [[PDK3]] | +0.66 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[ALDOA]] | +0.66 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[YEATS2]] | +0.65 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[PPFIA4]] | +0.64 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[ALDOC]] | +0.63 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[FAM162A]] | +0.62 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[ARRB2]] | +0.62 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[PFKFB4]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCG17]] | -0.59 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[GNG12-AS1]] | -0.59 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[AP4S1]] | -0.57 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[DNAJB14]] | -0.56 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[PPP3CB-AS1]] | -0.56 | -0.58 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[ACADM]] | -0.54 | -0.65 / -0.33 | both halves | 1e-04 |  |
| [[PBLD]] | -0.54 | -0.56 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[ZNF407-AS1]] | -0.53 | -0.65 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[PPP1R12A-AS2]] | -0.52 | -0.61 / -0.11 | ⚠ one half (not replicated) | 0.002 |  |
| [[AP5M1]] | -0.52 | -0.55 / -0.20 | ⚠ one half (not replicated) | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NCKIPSD's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ENO2]] | C | ENO2 activity strengthens NCKIPSD's drug response | lines that do not express ENO2 (3) vs lines expressing it (45) | the lines without ENO2 respond 0.36× as strongly (z diff +3.13); strongest at Dinaciclib 0.05 µM: 1.33x vs 0.52x (z diff +7.1) | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: NMB; target measured in part of the lines; the reference differs; artifact flags |
| [[YEATS2]] | C | YEATS2's natural level strengthens NCKIPSD's drug response | YEATS2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.40; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KDM4B]] | C | NCKIPSD's natural level strengthens KDM4B's drug response | NCKIPSD's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.25; direction not clear | 0.046 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.2, -14.4); signed map (-34.5, 21.6). **Vector** length 103, 26.8% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.2 | -2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.1 | -1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +5.9 | -3.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +5.8 | +0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +2.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +0.3 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.5 | -20.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -23.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -11.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -13.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -9.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -8.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.6 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.5 | -3.7 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -2.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | NCK interacting protein with SH3 domain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:48,673,844-48,686,364 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AF3P21, SPIN90, ORF1, WISH, WASLBP, DIP1 |
| Gene groups (HGNC) | SH3 domain containing |
| Reactome | 12 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; FCGR3A-mediated phagocytosis; Leishmania phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZQ3](https://www.uniprot.org/uniprotkb/Q9NZQ3) (NCK-interacting protein with SH3 domain):

> Has an important role in stress fiber formation induced by active diaphanous protein homolog 1 (DRF1). Induces microspike formation, in vivo (By similarity). In vitro, stimulates N-WASP-induced ARP2/3 complex activation in the absence of CDC42 (By similarity). May play an important role in the maintenance of sarcomeres and/or in the assembly of myofibrils into sarcomeres. Implicated in regulation of actin polymerization and cell adhesion. Plays a role in angiogenesis.

**Summary**, from NCBI Gene [51517](https://www.ncbi.nlm.nih.gov/gene/51517):

> The protein encoded by this gene contains a nuclear localization signal. It plays a role in signal transduction, and may function in the maintenance of sarcomeres and in the assembly of myofibrils into sarcomeres. It also plays an important role in stress fiber formation This protein is involved in the formation and maintenance of dendritic spines, and modulates synaptic activity in neurons. The gene is involved in therapy-related leukemia by a chromosomal translocation t(3;11)(p21;q23) that …

**Accessions** — [HGNC:15486](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15486) · Entrez [51517](https://www.ncbi.nlm.nih.gov/gene/51517) · UniProt [Q9NZQ3](https://www.uniprot.org/uniprotkb/Q9NZQ3) · Ensembl [ENSG00000213672](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213672)

## Data

Gene col 13125: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13125); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13125, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13125]; `tensor/DDL_lfc|DDL_z.npy` [13125]; `embed/gene_vectors.npy` [13125]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13125 or target_col == 13125). Every well: [[NCKIPSD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCKIPSD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

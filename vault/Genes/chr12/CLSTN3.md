---
symbol: "CLSTN3"
type: "gene"
col: 6274
ensembl_id: "ENSG00000139182"
name: "calsyntenin 3"
location: "12p13.31"
module: 2
arm: "+"
pooled_cpm: 19.63
n_lines_expressing: 47
n_dd_up: 0
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CLSTN3

*calsyntenin 3* — 12p13.31

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW48 5.00×; ⚠ cell-cycle shift, explains ~52% of this change).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.416× (z -16.1, q 0e+00, down in 31 of 44 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.481× (z -9.5, q 5e-19, down in 32 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1RL-AS1]] (+0.58, fdr 7e-06, ⚠ same locus), [[BCAM]] (+0.53, fdr 2e-05), [[CYB5R3]] (+0.51, fdr 4e-05), [[MAPK11]] (+0.50, fdr 3e-05); moves opposite to [[AGO4]] (-0.51, fdr 8e-05), [[EXOC1]] (-0.45, fdr 6e-05), [[TGDS]] (-0.45, fdr 6e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C1RL-AS1]] → it (grade B ⚠); 3 go from it, the strongest it → [[C1RL-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6274.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW48 5.00×; ⚠ cell-cycle shift, explains ~52% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 1.35× | +3.6 | 0.15 | 21/44 (HOP62, NCI-H2030, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 1.22× | +3.5 | 0.15 | 10/45 (Hs 766T, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6274.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.416×** | -16.1 | 0e+00 | 31/44 (MIA PaCa-2, RKO, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.481×** | -9.5 | 5e-19 | 32/42 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -7.7 | 2e-12 | 31/42 (A-427, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.543×** | -7.5 | 1e-11 | 27/44 (NCI-H2030, KATO III, …) | rises with dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.585×** | -7.0 | 4e-10 | 27/44 (A-172, RPMI-7951, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.597×** | -6.7 | 2e-09 | 26/45 (KATO III, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.619×** | -6.3 | 3e-08 | 28/45 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.625×** | -6.1 | 7e-08 | 25/44 (SNU-423, A-427, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.656×** | -5.5 | 2e-06 | 26/44 (NCI-H2030, A-427, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.678×** | -4.8 | 1e-04 | 23/40 (HT-29, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.697×** | -4.7 | 1e-04 | 22/44 (A-427, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.688×** | -4.6 | 2e-04 | 20/40 (H4, SNU-423, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.528×** | -4.3 | 6e-04 | 20/45 (NCI-H23, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.720×** | -4.3 | 8e-04 | 17/45 (H4, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.682×** | -4.2 | 1e-03 | 20/45 (SW 900, NCI-H2030, …) | rises with dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.726×** | -3.9 | 0.003 | 17/45 (SW480, AN3 CA, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.738×** | -3.7 | 0.006 | 17/45 (SW48, A549, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.782×** | -3.0 | 0.078 | 15/44 (NCI-H1573, SW 1271, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.852× | -3.0 | 0.088 | 14/45 (CFPAC-1, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6274. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 26.3 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0607× (z -22.1) |
| [[A549 (line)]] | wt | 28.5 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0782× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.136× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 58.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 19.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 19.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -11.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -8.6) |
| [[HCT15 (line)]] | alt | 29.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -10.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[hTERT-HPNE (line)]] | wt | 22.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 11.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -13.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[Panc 03.27 (line)]] | alt | 34.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -12.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.236× (z -9.8) |
| [[SNU-423 (line)]] | alt | 15.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -9.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW48 (line)]] | wt | 37.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.00× (z +8.6) ⚠ cell-cycle shift, explains ~52% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 30.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -12.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.409× (z -8.8) |
| [[BT-474 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -11.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[COLO 205 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -9.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[H4 (line)]] | wt | 42.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -10.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HOP62 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -10.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[J82 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.278× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0543× (z -24.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1573 (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -15.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1792 (line)]] | alt | 22.7 | 0 | 1 | — | [[Pralsetinib (drug)]] 5 µM 0.0595× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -10.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H460 (line)]] | wt | 8.06 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 5.15 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -9.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[RKO (line)]] | wt | 35.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -20.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SHP-77 (line)]] | alt | 9.33 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.116× (z -9.0) |
| [[SW 900 (line)]] | alt | 38.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -16.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6274), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1RL-AS1]] | +0.58 | +0.61 / +0.74 | both halves | 7e-06 | ⚠ same locus (7.2 kb, same strand: neighbours can correlate without regulation) |
| [[BCAM]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[CYB5R3]] | +0.51 | +0.51 / +0.40 | both halves | 4e-05 |  |
| [[MAPK11]] | +0.50 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[SSPOP]] | +0.50 | +0.42 / +0.38 | both halves | 7e-05 |  |
| [[JMJD7]] | +0.49 | +0.43 / +0.33 | both halves | 1e-04 |  |
| [[ARF3]] | +0.49 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[REC8]] | +0.48 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[SIPA1]] | +0.48 | +0.47 / +0.36 | both halves | 1e-04 |  |
| [[RMRP]] | +0.48 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[C3]] | +0.48 | +0.32 / +0.44 | both halves | 2e-04 |  |
| [[SRRT]] | +0.48 | +0.40 / +0.45 | both halves | 4e-05 |  |
| [[ABCD1]] | +0.47 | +0.30 / +0.39 | both halves | 2e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGO4]] | -0.51 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[EXOC1]] | -0.45 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[TGDS]] | -0.45 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[RP9P]] | -0.45 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[MRPS31]] | -0.44 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[PURA]] | -0.44 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[AKAP10]] | -0.44 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[ASTE1]] | -0.44 | -0.41 / -0.37 | both halves | 7e-05 |  |
| [[TMED8]] | -0.44 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[TRAPPC13]] | -0.44 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[LSM8]] | -0.44 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[FBXL4]] | -0.44 | -0.30 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1RL-AS1]] | B | C1RL-AS1 activity raises CLSTN3's level | lines that do not express C1RL-AS1 (7) vs lines expressing it (43) | 2.90× lower at baseline in the lines without C1RL-AS1 | 0.085 | ⚠ within organs, on part of the lines; also absent: EGFR, HFE, SH2D4A |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1RL-AS1]] | C | CLSTN3 activity raises C1RL-AS1's level | lines that do not express CLSTN3 (3) vs lines expressing it (47) | 7.35× lower at baseline in the lines without CLSTN3 | 0.010 | ⚠ few lines (3 vs 47); across organs; also absent: PIM1, HACD1, ENSG00000286782 |
| [[TATDN3]] | C | CLSTN3 activity strengthens TATDN3's drug response | lines that do not express CLSTN3 (3) vs lines expressing it (45) | the lines without CLSTN3 respond 0.40× as strongly (z diff +1.56); strongest at Homoharringtonine 5 µM: 0.63x vs 1.35x (z diff +5.9) | 0.061 | ⚠ few lines (3 vs 47); across organs; also absent: PIM1, HACD1, ENSG00000286782; target measured in part of the lines; artifact flags |
| [[YWHAG]] | C | CLSTN3 activity lowers YWHAG's level | lines that do not express CLSTN3 (3) vs lines expressing it (47) | 1.70× higher at baseline in the lines without CLSTN3 | 0.092 | ⚠ few lines (3 vs 47); across organs; also absent: PIM1, HACD1, ENSG00000286782 |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.366). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (11.5, -5.7); signed map (-10.8, 28.9). **Vector** length 69.5, 12.6% of its response variance represented; |z| ≥ 3 in 900 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.6 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.0 | -0.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.3 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | +2.5 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.1 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | -2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.8 | -16.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -4.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -7.0 |

## What is on record

|  |  |
|---|---|
| Name | calsyntenin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:7,129,698-7,158,945 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CSTN3, KIAA0726, CDHR14 |
| Gene groups (HGNC) | Cadherin related |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQT9](https://www.uniprot.org/uniprotkb/Q9BQT9) (Calsyntenin-3):

> Postsynaptic adhesion molecule that binds to presynaptic neurexins to mediate both excitatory and inhibitory synapse formation. Promotes synapse development by acting as a cell adhesion molecule at the postsynaptic membrane, which associates with both neurexin-alpha and neurexin-beta proteins at the presynaptic membrane. Regulates the balance between excitatory and inhibitory synapses by inhibiting formation of excitatory parallel-fiber synapses and promoting formation of inhibitory synapses in …

**Summary**, from NCBI Gene [9746](https://www.ncbi.nlm.nih.gov/gene/9746):

> Enables cell-cell adhesion mediator activity and neurexin family protein binding activity. Involved in L-ascorbic acid metabolic process and regulation of synapse assembly. Predicted to be located in several cellular components, including Golgi membrane; postsynaptic density; and postsynaptic membrane. Predicted to be part of protein-containing complex. Predicted to be active in several cellular components, including endoplasmic reticulum membrane; lipid droplet; and postsynaptic density …

**Accessions** — [HGNC:18371](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18371) · Entrez [9746](https://www.ncbi.nlm.nih.gov/gene/9746) · UniProt [Q9BQT9](https://www.uniprot.org/uniprotkb/Q9BQT9) · Ensembl [ENSG00000139182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139182)

## Data

Gene col 6274: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6274); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6274, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6274]; `tensor/DDL_lfc|DDL_z.npy` [6274]; `embed/gene_vectors.npy` [6274]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6274 or target_col == 6274). Every well: [[CLSTN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLSTN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

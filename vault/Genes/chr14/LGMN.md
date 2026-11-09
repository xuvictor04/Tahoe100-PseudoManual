---
symbol: "LGMN"
type: "gene"
col: 1997
ensembl_id: "ENSG00000100600"
name: "legumain"
location: "14q32.12"
module: 93
arm: "+"
pooled_cpm: 45.71
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# LGMN

*legumain* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.14× (z +16.4, q 0e+00, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 0.0909×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.275×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.319×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL15]] (+0.66, fdr 7e-06), [[POR]] (+0.64, fdr 1e-05), [[TENT5C]] (+0.63, fdr 1e-05); moves opposite to [[RRP36]] (-0.54, fdr 1e-05), [[LSM14A]] (-0.52, fdr 3e-05), [[AP4E1]] (-0.52, fdr 3e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1997.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.14×** | +16.4 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.96×** | +12.2 | 1e-31 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.22×** | +11.4 | 7e-28 | 46/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +7.7 | 2e-12 | 38/48 (SW480, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.37×** | +6.4 | 2e-08 | 32/47 (MIA PaCa-2, NCI-H1792, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +6.0 | 2e-07 | 31/48 (SW480, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +5.9 | 2e-07 | 33/48 (SW 900, SW480, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.50×** | +5.6 | 2e-06 | 27/46 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.45×** | +5.3 | 6e-06 | 33/48 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +5.2 | 1e-05 | 35/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.37×** | +4.5 | 4e-04 | 26/47 (J82, NCI-H2347, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.37×** | +4.4 | 6e-04 | 27/48 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.77×** | +4.3 | 9e-04 | 25/43 (NCI-H23, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.002 | 22/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +3.9 | 0.003 | 23/48 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.004 | 24/48 (A549, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.012 | 20/48 (SK-MEL-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.016 | 20/48 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.028 | 19/48 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.029 | 18/48 (Panc 03.27, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1997.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 0.0909×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.275×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.319×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | 0.777× | -3.7 | 0.14 | 20/48 (RKO, LoVo, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.764× | -3.1 | 0.45 | 16/48 (SW 900, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 0.805× | -3.0 | 0.45 | 20/48 (KATO III, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1997. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 25.2 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.92× (z +12.8) | — |
| [[SW480 (line)]] | alt | 34.1 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.88× (z +16.8) | — |
| [[AsPC-1 (line)]] | alt | 39.7 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.34× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 25.1 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.94× (z +11.3) | — |
| [[A-427 (line)]] | wt | 33.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.20× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -15.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 59.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +10.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.76× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 48.1 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +9.7) | — |
| [[A498 (line)]] | wt | 27.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.22× (z +9.5) | — |
| [[A549 (line)]] | wt | 32.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.43× (z +10.6) | — |
| [[HCT15 (line)]] | alt | 32.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.77× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[HEC-1-A (line)]] | alt | 30.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.09× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 34.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.63× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 32.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.64× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 51.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 44.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +10.2) | — |
| [[KATO III (line)]] | alt | 56.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.95× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 28.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.97× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 30.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.34× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 94.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.01× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 24.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.84× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 69.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0909× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 42.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 26.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.70× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 90.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.05× (z +11.1) | — |
| [[SW1417 (line)]] | alt | 47.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.59× (z +9.1) | — |
| [[A-172 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 62.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 47.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1997), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL15]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[POR]] | +0.64 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[TENT5C]] | +0.63 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[SNAI1]] | +0.62 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[TNFSF9]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[MYO7A]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[FAM222A]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[OAT]] | +0.61 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[FAM53C]] | +0.61 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[HAP1]] | +0.60 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[GTF2B]] | +0.60 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[HSPA2]] | +0.60 | +0.48 / +0.63 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP36]] | -0.54 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[LSM14A]] | -0.52 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[AP4E1]] | -0.52 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[NHLRC2]] | -0.50 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[TADA2A]] | -0.49 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[MDC1]] | -0.49 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[JPX]] | -0.49 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[ENTPD3-AS1]] | -0.49 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[TRMT61B]] | -0.49 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[NDUFS1]] | -0.48 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ZNF282]] | -0.48 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[FAM86HP]] | -0.48 | -0.43 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.747). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.3, -27.4); signed map (1.9, 17.9). **Vector** length 112, 32.2% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.6 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +3.5 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.0 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +3.8 | +3.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +3.8 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +2.5 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.1 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.6 | -3.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.5 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | legumain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:92,703,807-92,748,679 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LGMN1; previously PRSC1 |
| Gene groups (HGNC) | Cysteine endopeptidases |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, COAGULATION, COMPLEMENT, MTORC1_SIGNALING |
| Reactome | 8 pathways, smallest: Trafficking and processing of endosomal TLR; Vitamin D (calciferol) metabolism; MHC class II antigen presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99538](https://www.uniprot.org/uniprotkb/Q99538) (Legumain):

> Has a strict specificity for hydrolysis of asparaginyl bonds. Can also cleave aspartyl bonds slowly, especially under acidic conditions. Involved in the processing of proteins for MHC class II antigen presentation in the lysosomal/endosomal system. Also involved in MHC class I antigen presentation in cross-presenting dendritic cells by mediating cleavage and maturation of Perforin-2 (MPEG1), thereby promoting antigen translocation in the cytosol (By similarity). Required for normal lysosomal …

**Summary**, from NCBI Gene [5641](https://www.ncbi.nlm.nih.gov/gene/5641):

> This gene encodes a cysteine protease that has a strict specificity for hydrolysis of asparaginyl bonds. This enzyme may be involved in the processing of bacterial peptides and endogenous proteins for MHC class II presentation in the lysosomal/endosomal systems. Enzyme activation is triggered by acidic pH and appears to be autocatalytic. Protein expression occurs after monocytes differentiate into dendritic cells. A fully mature, active enzyme is produced following lipopolysaccharide expression …

**Accessions** — [HGNC:9472](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9472) · Entrez [5641](https://www.ncbi.nlm.nih.gov/gene/5641) · UniProt [Q99538](https://www.uniprot.org/uniprotkb/Q99538) · Ensembl [ENSG00000100600](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100600)

## Data

Gene col 1997: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1997); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1997, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1997]; `tensor/DDL_lfc|DDL_z.npy` [1997]; `embed/gene_vectors.npy` [1997]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1997 or target_col == 1997). Every well: [[LGMN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LGMN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

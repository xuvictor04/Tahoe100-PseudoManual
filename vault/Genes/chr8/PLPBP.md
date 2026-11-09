---
symbol: "PLPBP"
type: "gene"
col: 7188
ensembl_id: "ENSG00000147471"
name: "pyridoxal phosphate binding protein"
location: "8p11.23"
module: 122
arm: "+"
pooled_cpm: 19.73
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# PLPBP

*pyridoxal phosphate binding protein* — 8p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.89× (z +16.6, q 0e+00, up in 30 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.44× (z +8.4, q 6e-15, up in 34 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.223×); [[Irinotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (C32 0.0680×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (RKO 0.282×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF6]] (+0.64, fdr 1e-05), [[DVL3]] (+0.60, fdr 4e-05), [[BOD1]] (+0.60, fdr 1e-05); moves opposite to [[HMGB1P5]] (-0.54, fdr 7e-05, ⚠ HMGB1P5 in the vector space only through flagged drug-doses), [[CDCA4]] (-0.53, fdr 3e-05), [[CENPW]] (-0.52, fdr 6e-05), [[EML4]] (-0.50, fdr 2e-04).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7188.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +16.6 | 0e+00 | 30/32 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.40×** | +14.2 | 1e-43 | 35/42 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +10.2 | 4e-22 | 29/35 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +9.2 | 5e-18 | 32/44 (MIA PaCa-2, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +8.4 | 6e-15 | 34/48 (CFPAC-1, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +7.1 | 1e-10 | 30/46 (SW480, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.4 | 4e-06 | 21/47 (A549, SW48, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +4.8 | 9e-05 | 21/47 (HOP62, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.7 | 1e-04 | 16/48 (SW480, A549, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.3 | 1e-03 | 16/44 (C-33 A, A549, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.20× | +4.1 | 0.002 | 17/48 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **1.27×** | +3.8 | 0.007 | 18/43 (KATO III, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.016 | 16/47 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.4 | 0.030 | 14/48 (NCI-H2347, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.22×** | +3.3 | 0.038 | 16/47 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.038 | 18/47 (HOP62, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7188.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.223×); [[Irinotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (C32 0.0680×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (RKO 0.282×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | 0.667× | -3.5 | 0.29 | 9/45 (A549, NCI-H460, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7188. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 27.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.36× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 29.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.86× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 19.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 21.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +11.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 26.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 10.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +9.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 6.32 | 0 | 1 | — | [[Irinotecan (hydrochloride) (drug)]] 0.05 µM 0.0680× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 13.7 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.223× (z -9.4) |
| [[HCT15 (line)]] | alt | 30.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.92× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 17.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +8.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 40.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 22.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.45× (z +10.2) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 29.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 14.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +10.0) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[NCI-H2030 (line)]] | alt | 14.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.6) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[Panc 03.27 (line)]] | alt | 26.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.91× (z +11.2) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 9.61 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +10.3) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 29.6 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.282× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7188), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF6]] | +0.64 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[DVL3]] | +0.60 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[BOD1]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ACTR8]] | +0.59 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[MRPL9]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[POLR2M]] | +0.58 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[EAF1]] | +0.58 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[SBDSP1]] | +0.58 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[UNC50]] | +0.57 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[BROX]] | +0.57 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[COPS2]] | +0.55 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[EIF2D]] | +0.55 | +0.31 / +0.54 | both halves | 2e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGB1P5]] ⚠ | -0.54 | -0.50 / -0.37 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CDCA4]] | -0.53 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[CENPW]] | -0.52 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[EML4]] | -0.50 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[JPT1]] | -0.50 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[STIL]] | -0.50 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[NUDT1]] | -0.49 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[CHTF18]] | -0.49 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[BARD1]] | -0.48 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[NUP98]] | -0.48 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[DNAJC1]] | -0.48 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[RTTN]] | -0.47 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[RBM6]] | -0.47 | -0.37 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.477). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-18.6, 12.0); signed map (6.1, -33.4). **Vector** length 59.0, 8.89% of its response variance represented; |z| ≥ 3 in 750 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.7 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +16.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.2 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +14.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +7.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +3.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.5 | -0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.4 | -1.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.9 | -1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -1.5 | +3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.1 | -0.4 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.0 | -0.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.0 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | pyridoxal phosphate binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.23 — chr8:37,762,595-37,779,768 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PROSC |
| Matched by | ensembl_id |

**Function**, from UniProt [O94903](https://www.uniprot.org/uniprotkb/O94903) (Pyridoxal phosphate homeostasis protein):

> Pyridoxal 5'-phosphate (PLP)-binding protein, which may be involved in intracellular homeostatic regulation of pyridoxal 5'-phosphate (PLP), the active form of vitamin B6.

**Summary**, from NCBI Gene [11212](https://www.ncbi.nlm.nih.gov/gene/11212):

> This gene encodes a pyridoxal 5'-phosphate binding protein involved in the homeostatic regulation of intracellular pyridoxal 5'-phosphate. This gene has a tumor suppressive effect on hepatocellular carcinoma and other solid tumors of epithelial origin. Naturally occurring mutations in this gene are associated with a pyridoxine-dependent epilepsy. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:9457](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9457) · Entrez [11212](https://www.ncbi.nlm.nih.gov/gene/11212) · UniProt [O94903](https://www.uniprot.org/uniprotkb/O94903) · Ensembl [ENSG00000147471](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147471)

## Data

Gene col 7188: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7188); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7188, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7188]; `tensor/DDL_lfc|DDL_z.npy` [7188]; `embed/gene_vectors.npy` [7188]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7188 or target_col == 7188). Every well: [[PLPBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLPBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

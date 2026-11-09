---
symbol: "TFAP2A"
type: "gene"
col: 5985
ensembl_id: "ENSG00000137203"
name: "transcription factor AP-2 alpha"
location: "6p24.3"
module: 68
arm: "+"
pooled_cpm: 36.91
n_lines_expressing: 45
n_dd_up: 18
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# TFAP2A

*transcription factor AP-2 alpha* — 6p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.90× (z +13.6, q 3e-39, up in 33 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.550× (z -9.0, q 2e-16, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFAP2A-AS1]] (+0.62, fdr 1e-05, ⚠ same locus), [[SIX5]] (+0.60, fdr 4e-05), [[CPEB2]] (+0.60, fdr 4e-05), [[BAZ2B]] (+0.58, fdr 5e-05); moves opposite to [[CTNNBL1]] (-0.53, fdr 2e-04), [[TPD52L2]] (-0.53, fdr 5e-05), [[ZDHHC9]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PCDH18]] → it (grade B ⚠); 2 go from it, the strongest it → [[FAM200B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5985.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +13.6 | 3e-39 | 33/40 (RKO, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.55×** | +9.3 | 4e-18 | 27/43 (J82, HS-578T, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +7.1 | 2e-10 | 28/41 (HS-578T, LS 180, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +6.6 | 6e-09 | 21/38 (J82, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.52×** | +6.1 | 2e-07 | 28/43 (HS-578T, J82, …) | top dose only | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.8 | 1e-04 | 17/43 (NCI-H2347, PANC-1, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +4.8 | 2e-04 | 17/36 (J82, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.002 | 18/41 (RKO, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD-7648 (drug)]] 5 µM |  | **1.60×** | +3.7 | 0.014 | 15/40 (C32, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.28×** | +3.7 | 0.014 | 13/39 (HCT15, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.6 | 0.020 | 16/38 (NCI-H23, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +3.5 | 0.022 | 14/33 (J82, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.4 | 0.026 | 13/41 (J82, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +3.4 | 0.029 | 13/38 (KATO III, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.029 | 15/43 (C32, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.053 | 5/42 (NCI-H23, AsPC-1, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.074 | 13/42 (BT-474, LOX-IMVI, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.097 | 12/42 (C32, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5985.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.550×** | -9.0 | 2e-16 | 31/43 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.626×** | -7.0 | 6e-10 | 29/43 (Panc 03.27, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.697×** | -5.4 | 1e-05 | 21/42 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.722×** | -4.9 | 1e-04 | 23/43 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.733×** | -4.4 | 0.001 | 23/42 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.759×** | -4.1 | 0.003 | 22/43 (LoVo, AsPC-1, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.786×** | -3.6 | 0.024 | 17/43 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.789×** | -3.4 | 0.039 | 18/42 (J82, A498, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.647×** | -3.4 | 0.039 | 15/41 (COLO 205, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.798×** | -3.4 | 0.039 | 12/42 (LOX-IMVI, HCT15, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Retinoic acid (drug)]] 5 µM |  | 0.857× | -3.3 | 0.051 | 12/43 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.862× | -3.2 | 0.071 | 13/43 (NCI-H460, A-427, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **0.811×** | -3.1 | 0.071 | 14/43 (NCI-H1573, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.807×** | -3.1 | 0.079 | 12/43 (RPMI-7951, HOP62, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5985. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 59.7 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.272× (z -12.7) |
| [[J82 (line)]] | alt | 56.0 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +18.5) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 45.6 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +17.8) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[LoVo (line)]] | wt | 67.3 | 2 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.1) ⚠ cell-cycle shift, explains ~51% of this change | [[Panobinostat (drug)]] 5 µM 0.185× (z -16.2) |
| [[LS 180 (line)]] | wt | 71.0 | 3 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +13.8) ⚠ cell-cycle shift, explains ~51% of this change | [[Panobinostat (drug)]] 5 µM 0.245× (z -13.8) |
| [[AsPC-1 (line)]] | alt | 71.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -15.7) |
| [[NCI-H23 (line)]] | alt | 76.8 | 1 (1 ⚠) | 2 | [[Adagrasib (drug)]] 0.05 µM 1.77× (z +14.2) ⚠ position not correctable | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 92.5 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.179× (z -14.6) |
| [[C32 (line)]] | wt | 58.9 | 2 | 0 | [[Cobimetinib (drug)]] 0.5 µM 4.82× (z +10.4) | — |
| [[KATO III (line)]] | alt | 37.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +14.2) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 49.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -11.0) |
| [[PANC-1 (line)]] | alt | 40.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.368× (z -9.2) |
| [[SNU-1 (line)]] | wt | 62.2 | 0 | 2 (1 ⚠) | — | [[vincristine (drug)]] 5 µM 0.0737× (z -8.9) |
| [[SNU-423 (line)]] | alt | 34.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.3) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[SW48 (line)]] | wt | 66.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -11.1) |
| [[A498 (line)]] | wt | 16.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 54.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +15.0) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[COLO 205 (line)]] | alt | 13.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 18.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 12.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +11.6) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[Hs 766T (line)]] | wt | 38.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +12.3) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[LOX-IMVI (line)]] | wt | 46.8 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.330× (z -8.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2030 (line)]] | alt | 28.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +10.5) | — |
| [[RKO (line)]] | wt | 13.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +11.3) | — |
| [[A-172 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.56 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.75 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.80 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5985), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFAP2A-AS1]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SIX5]] | +0.60 | +0.61 / +0.42 | both halves | 4e-05 | STRING 532 |
| [[CPEB2]] | +0.60 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[BAZ2B]] | +0.58 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[CYP1B1-AS1]] | +0.58 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[ZNF827]] | +0.58 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[FOXC1]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 | pathway: Gastrulation; STRING 652 |
| [[CDKN1B]] | +0.58 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[FOXA1]] | +0.57 | +0.54 / +0.49 | both halves | 1e-05 | pathway: Gastrulation; STRING 716 |
| [[ZSCAN31]] | +0.57 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[TRIM69]] | +0.56 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[GATA3]] | +0.56 | +0.47 / +0.50 | both halves | 2e-05 | STRING 693 |
| [[RARG]] | +0.56 | +0.61 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTNNBL1]] | -0.53 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[TPD52L2]] | -0.53 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[ZDHHC9]] | -0.53 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[SPTLC2]] | -0.53 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[MTG1]] | -0.52 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[STK4]] | -0.52 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[AP1M1]] | -0.51 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[TREX2]] | -0.51 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[DCAF13]] | -0.50 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[TMEM241]] | -0.50 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[HERC2P2]] | -0.50 | -0.44 / -0.37 | both halves | 9e-05 |  |
| [[WRN]] | -0.50 | -0.54 / -0.24 | both halves | 4e-04 | pathway: SUMO E3 ligases SUMOylate target proteins |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDH18]] | B | PCDH18 activity lowers TFAP2A's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 1.30× higher at baseline in the lines without PCDH18 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677 |
| [[PCDH7]] | B | PCDH7 activity raises TFAP2A's level | lines that do not express PCDH7 (18) vs lines expressing it (32) | 1.75× lower at baseline in the lines without PCDH7 | 0.073 | ⚠ within organs, on part of the lines; also absent: ADGRL4, KCNQ5, ST8SIA4 |
| [[EFNA1]] | B | EFNA1 activity raises TFAP2A's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 1.85× lower at baseline in the lines without EFNA1 | 0.074 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM200B]] | B | TFAP2A activity raises FAM200B's level | lines that do not express TFAP2A (5) vs lines expressing it (45) | 1.35× lower at baseline in the lines without TFAP2A | 0.015 | ⚠ within organs, on part of the lines; also absent: FAM111A, PRNP, TRIM34 |
| [[RARG]] | B | TFAP2A activity raises RARG's level | lines that do not express TFAP2A (5) vs lines expressing it (45) | 2.35× lower at baseline in the lines without TFAP2A | 0.040 | ⚠ within organs, on part of the lines; also absent: FAM111A, PRNP, TRIM34 |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (18.9, 12.3); signed map (18.5, -10.9). **Vector** length 107, 26.4% of its response variance represented; |z| ≥ 3 in 1,006 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +7.9 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +13.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +6.0 | +6.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.5 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | +3.5 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.8 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +1.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.6 | +1.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.1 | -7.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -9.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -3.7 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.4 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -4.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.9 | -3.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.2 | -2.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor AP-2 alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.3 — chr6:10,393,186-10,419,659 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AP-2, AP-2alpha; previously TFAP2, AP2TF |
| Gene groups (HGNC) | Transcription factor AP-2 family |
| Reactome | 24 pathways, smallest: TFAP2 (AP-2) family regulates transcription of other transcription factors; TFAP2 (AP-2) family regulates transcription of cell cycle factors; TFAP2A acts as a transcriptional repressor during retinoic acid induced cell differentiation |
| Matched by | ensembl_id |

**Function**, from UniProt [P05549](https://www.uniprot.org/uniprotkb/P05549) (Transcription factor AP-2-alpha):

> Sequence-specific DNA-binding protein that interacts with inducible viral and cellular enhancer elements to regulate transcription of selected genes. AP-2 factors bind to the consensus sequence 5'-GCCNNNGGC-3' and activate genes involved in a large spectrum of important biological functions including proper eye, face, body wall, limb and neural tube development. They can also suppress a number of genes including MCAM/MUC18 and C/EBP alpha. Is involved in the negative regulation of Wnt canonical …

**Summary**, from NCBI Gene [7020](https://www.ncbi.nlm.nih.gov/gene/7020):

> The protein encoded by this gene is a transcription factor that binds the consensus sequence 5'-GCCNNNGGC-3'. The encoded protein functions as either a homodimer or as a heterodimer with similar family members. This protein activates the transcription of some genes while inhibiting the transcription of others. Defects in this gene are a cause of branchiooculofacial syndrome (BOFS). Three transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Dec 2009]

**Accessions** — [HGNC:11742](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11742) · Entrez [7020](https://www.ncbi.nlm.nih.gov/gene/7020) · UniProt [P05549](https://www.uniprot.org/uniprotkb/P05549) · Ensembl [ENSG00000137203](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137203)

## Data

Gene col 5985: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5985); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5985, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5985]; `tensor/DDL_lfc|DDL_z.npy` [5985]; `embed/gene_vectors.npy` [5985]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5985 or target_col == 5985). Every well: [[TFAP2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFAP2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

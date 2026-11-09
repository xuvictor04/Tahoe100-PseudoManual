---
symbol: "SCGB2B2"
type: "gene"
col: 12957
ensembl_id: "ENSG00000205209"
name: "secretoglobin family 2B member 2"
location: "19q13.12"
module: 10
arm: "+"
pooled_cpm: 32.7
n_lines_expressing: 46
n_dd_up: 7
n_dd_down: 40
n_dd_up_clean: 5
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# SCGB2B2

*secretoglobin family 2B member 2* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.46× (z +8.3, q 6e-14, up in 26 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (22 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.284× (z -19.3, q 0e+00, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF689]] (+0.68, fdr 4e-05), [[THBS4]] (+0.66, fdr 3e-05), [[ZNF407-AS1]] (+0.66, fdr 1e-05); moves opposite to [[MGAT4A]] (-0.62, fdr 3e-05), [[TCF3]] (-0.61, fdr 2e-04), [[PRKCI]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[INHA]] → it (grade B ⚠); 2 go from it, the strongest it → [[KANK2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12957.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +8.3 | 6e-14 | 26/44 (SHP-77, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.39×** | +7.2 | 2e-10 | 30/44 (RKO, A549, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +4.5 | 0.001 | 21/44 (KATO III, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.32×** | +4.3 | 0.003 | 17/44 (A-427, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.8 | 0.014 | 18/44 (A498, HS-578T, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.017 | 18/44 (KATO III, SW48, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.024 | 11/44 (C32, NCI-H1792, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.042 | 18/43 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.23× | +3.1 | 0.12 | 16/43 (SW480, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.21× | +3.0 | 0.14 | 8/44 (LS 180, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 22 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12957.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.284×** | -19.3 | 0e+00 | 42/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.329×** | -17.0 | 0e+00 | 42/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.337×** | -16.7 | 0e+00 | 42/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.398×** | -14.1 | 3e-43 | 40/44 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.427×** | -13.0 | 7e-37 | 40/43 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.414×** | -13.0 | 1e-36 | 38/42 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.498×** | -10.7 | 1e-24 | 36/44 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.542×** | -9.4 | 4e-19 | 29/41 (SNU-1, NCI-H23, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.560×** | -8.9 | 4e-17 | 35/44 (LoVo, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.550×** | -8.7 | 3e-16 | 30/44 (PANC-1, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.579×** | -8.1 | 4e-14 | 29/43 (NCI-H1792, RPMI-7951, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.596×** | -7.9 | 1e-13 | 32/44 (NCI-H1792, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.622×** | -7.3 | 2e-11 | 31/44 (NCI-H1792, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.726×** | -6.9 | 2e-10 | 27/43 (C32, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.636×** | -6.7 | 1e-09 | 26/43 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.490×** | -5.7 | 3e-07 | 30/44 (MIA PaCa-2, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.495×** | -5.6 | 5e-07 | 24/43 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.790×** | -5.1 | 9e-06 | 23/44 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.806×** | -4.7 | 8e-05 | 21/44 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.754×** | -4.3 | 3e-04 | 15/44 (PANC-1, SW1417, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.765×** | -4.1 | 9e-04 | 19/43 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.604×** | -4.0 | 0.001 | 20/44 (KATO III, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.726×** | -3.5 | 0.008 | 13/44 (PANC-1, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.796×** | -3.5 | 0.009 | 18/43 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12957. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 55.6 | 0 | 13 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0531× (z -24.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -12.6) |
| [[C32 (line)]] | wt | 75.9 | 0 | 11 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -15.4) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.339× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 61.5 | 0 | 11 (8 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0881× (z -18.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -12.7) |
| [[PANC-1 (line)]] | alt | 39.9 | 0 | 10 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0924× (z -23.9) |
| [[LoVo (line)]] | wt | 58.8 | 0 | 9 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.320× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 25.5 | 0 | 9 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -16.6) |
| [[SW480 (line)]] | alt | 40.9 | 0 | 9 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.115× (z -22.9) |
| [[A549 (line)]] | wt | 41.6 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0986× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 41.6 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.109× (z -19.3) |
| [[NCI-H23 (line)]] | alt | 39.1 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.244× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 55.0 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.203× (z -11.5) |
| [[J82 (line)]] | alt | 29.4 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.166× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.213× (z -11.9) |
| [[SK-MEL-2 (line)]] | alt | 49.5 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.170× (z -13.7) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 67.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -11.3) |
| [[H4 (line)]] | wt | 32.3 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0872× (z -12.2) |
| [[HOP62 (line)]] | alt | 30.8 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.147× (z -13.4) |
| [[SW 900 (line)]] | alt | 36.9 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.179× (z -12.3) |
| [[A498 (line)]] | wt | 41.3 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.209× (z -11.4) ⚠ cell-cycle shift, explains ~40% of this change |
| [[LS 180 (line)]] | wt | 28.0 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.147× (z -13.5) |
| [[SHP-77 (line)]] | alt | 52.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[AsPC-1 (line)]] | alt | 9.48 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0842× (z -11.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 18.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[SW1417 (line)]] | alt | 17.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -10.5) |
| [[BT-474 (line)]] | alt | 26.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.202× (z -9.4) |
| [[CHP-212 (line)]] | wt | 67.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0885× (z -11.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 50.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0812× (z -17.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 22.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.219× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 15.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.119× (z -9.0) |
| [[KATO III (line)]] | alt | 30.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -15.2) |
| [[NCI-H2030 (line)]] | alt | 47.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.292× (z -9.6) ⚠ toxic |
| [[RKO (line)]] | wt | 31.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.213× (z -10.3) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 88.5 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0809× (z -9.7) |
| [[SW48 (line)]] | wt | 28.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0985× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.05 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.78 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12957), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF689]] | +0.68 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[THBS4]] | +0.66 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[ZNF407-AS1]] | +0.66 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[ZNF101]] | +0.66 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[MFF-DT]] | +0.66 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[ZNF830]] | +0.65 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[DNAJC30]] | +0.65 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[SMIM19]] | +0.64 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[C2orf49-DT]] | +0.64 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[MAD2L1-DT]] | +0.64 | +0.61 / +0.31 | both halves | 2e-04 |  |
| [[PPCS]] | +0.64 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[EMSY-DT]] | +0.63 | +0.56 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGAT4A]] | -0.62 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[TCF3]] | -0.61 | -0.60 / -0.31 | both halves | 2e-04 |  |
| [[PRKCI]] | -0.60 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ARHGAP8]] | -0.58 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[PIP4K2A]] | -0.58 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[KIF21B]] | -0.57 | -0.51 / -0.23 | both halves | 5e-04 |  |
| [[GPRIN1]] | -0.56 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[EDA]] | -0.56 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[KANK2]] | -0.56 | -0.43 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INHA]] | B | INHA activity raises SCGB2B2's level | lines that do not express INHA (11) vs lines expressing it (39) | 1.45× lower at baseline in the lines without INHA | 0.044 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13 |
| [[HOXA10-AS]] | B | HOXA10-AS activity lowers SCGB2B2's level | lines that do not express HOXA10-AS (21) vs lines expressing it (29) | 1.33× higher at baseline in the lines without HOXA10-AS | 0.096 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA11, HOXA10; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KANK2]] | C | SCGB2B2 activity lowers KANK2's level | lines that do not express SCGB2B2 (4) vs lines expressing it (46) | 1.99× higher at baseline in the lines without SCGB2B2 | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; its own permutation p |
| [[C11orf71]] | C | SCGB2B2 activity raises C11orf71's level | lines that do not express SCGB2B2 (4) vs lines expressing it (46) | 1.30× lower at baseline in the lines without SCGB2B2 | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; its own permutation p |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.618). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (3.3, 14.8); signed map (27.0, -14.0). **Vector** length 71.5, 16.2% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +8.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +5.1 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.9 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | -1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | -5.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -4.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.9 | -10.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.5 | -7.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.4 | -7.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.3 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -8.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -5.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | secretoglobin family 2B member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:34,590,644-34,677,159 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCGB4A2; previously SCGBL |
| Gene groups (HGNC) | Secretoglobins |
| Matched by | ensembl_id |

UniProt [Q4G0G5](https://www.uniprot.org/uniprotkb/Q4G0G5) carries no function annotation.

**Summary**, from NCBI Gene [284402](https://www.ncbi.nlm.nih.gov/gene/284402):

> Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27616](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27616) · Entrez [284402](https://www.ncbi.nlm.nih.gov/gene/284402) · UniProt [Q4G0G5](https://www.uniprot.org/uniprotkb/Q4G0G5) · Ensembl [ENSG00000205209](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205209)

## Data

Gene col 12957: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12957); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12957, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12957]; `tensor/DDL_lfc|DDL_z.npy` [12957]; `embed/gene_vectors.npy` [12957]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12957 or target_col == 12957). Every well: [[SCGB2B2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCGB2B2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

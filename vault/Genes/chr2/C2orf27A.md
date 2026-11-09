---
symbol: "C2orf27A"
type: "gene"
col: 16285
ensembl_id: "ENSG00000287151"
name: "long independently transcribed non-coding RNA 3124"
location: "2q21.2"
module: 40
arm: "+"
pooled_cpm: 20.88
n_lines_expressing: 45
n_dd_up: 8
n_dd_down: 26
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 8
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# C2orf27A

*long independently transcribed non-coding RNA 3124* — 2q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.28× (z +5.9, q 2e-06, up in 21 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.326× (z -19.0, q 0e+00, down in 36 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.452× (z -13.5, q 2e-39, down in 38 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUXAP10]] (+0.65, fdr 7e-06), [[NBEAP2]] (+0.63, fdr 7e-06, ⚠ same locus), [[TFB2M]] (+0.62, fdr 2e-05), [[ELP2]] (+0.58, fdr 1e-05); moves opposite to [[CHD4]] (-0.52, fdr 3e-05), [[SKIL]] (-0.45, fdr 9e-05), [[SLK]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 8 go from it, the strongest it → [[HEATR6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16285.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +5.9 | 2e-06 | 21/43 (NCI-H460, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +5.3 | 2e-05 | 22/43 (BT-474, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +5.3 | 2e-05 | 20/43 (NCI-H2347, A498, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.007 | 15/43 (SW 900, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.007 | 12/43 (HOP62, RKO, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.021 | 6/43 (HOP62, BT-474, …) | rises with dose |  |
| [[Tadalafil (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.031 | 6/43 (A-172, A-427, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.15× | +3.4 | 0.048 | 13/43 (NCI-H1792, A498, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.058 | 9/43 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16285.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.326×** | -19.0 | 0e+00 | 36/42 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.533×** | -15.1 | 0e+00 | 34/42 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.452×** | -13.5 | 2e-39 | 38/43 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.447×** | -13.2 | 2e-37 | 36/43 (PANC-1, A498, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.479×** | -12.5 | 8e-34 | 24/36 (SW480, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.505×** | -11.6 | 3e-29 | 36/43 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.558×** | -9.9 | 3e-21 | 30/43 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.591×** | -8.3 | 1e-14 | 22/31 (NCI-H2030, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.608×** | -8.1 | 2e-14 | 20/28 (SW 900, PANC-1, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.609×** | -8.1 | 3e-14 | 21/42 (NCI-H23, H4, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.644×** | -7.5 | 4e-12 | 28/42 (HEC-1-A, A-427, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.669×** | -6.8 | 4e-10 | 24/43 (H4, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.672×** | -6.8 | 6e-10 | 25/43 (HCT15, J82, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.723×** | -5.5 | 1e-06 | 20/43 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.796×** | -5.5 | 2e-06 | 23/43 (LOX-IMVI, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.725×** | -5.5 | 2e-06 | 18/43 (HEC-1-A, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.580×** | -4.8 | 4e-05 | 18/42 (hTERT-HPNE, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.769×** | -4.5 | 2e-04 | 19/43 (SW 1271, SW 1088, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.768×** | -4.2 | 6e-04 | 16/43 (AN3 CA, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.652×** | -3.8 | 0.004 | 19/43 (NCI-H1792, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.652×** | -3.8 | 0.004 | 14/43 (A498, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.674×** | -3.5 | 0.011 | 13/43 (A-172, A498, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.826×** | -3.1 | 0.039 | 14/43 (PANC-1, HS-578T, …) | top dose only |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **0.832×** | -3.1 | 0.039 | 10/43 (C-33 A, Panc 03.27, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16285. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 31.9 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -13.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.380× (z -8.7) |
| [[PANC-1 (line)]] | alt | 27.9 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.125× (z -17.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.380× (z -8.5) |
| [[SW 900 (line)]] | alt | 34.0 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LOX-IMVI (line)]] | wt | 64.3 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -15.6) |
| [[NCI-H460 (line)]] | wt | 8.09 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0720× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.116× (z -12.4) |
| [[CHP-212 (line)]] | wt | 40.2 | 0 | 3 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.102× (z -9.5) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 28.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.294× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -9.2) |
| [[SW480 (line)]] | alt | 14.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.300× (z -9.6) |
| [[A-427 (line)]] | wt | 21.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A498 (line)]] | wt | 35.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -16.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[H4 (line)]] | wt | 63.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.205× (z -10.3) |
| [[J82 (line)]] | alt | 33.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -9.5) |
| [[KATO III (line)]] | alt | 15.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.121× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 28.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -17.4) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H1792 (line)]] | alt | 20.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -11.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 24.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -16.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 18.0 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.116× (z -12.8) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.247× (z -8.7) |
| [[RKO (line)]] | wt | 30.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.214× (z -9.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 33.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -11.3) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.217× (z -10.3) |
| [[A-172 (line)]] | wt | 40.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A549 (line)]] | wt | 8.01 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0661× (z -10.7) |
| [[AN3 CA (line)]] | alt | 37.1 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0568× (z -9.1) |
| [[BT-474 (line)]] | alt | 40.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -10.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 8.25 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -10.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 1 | — | [[Triclosan (drug)]] 0.5 µM 0.0750× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0936× (z -8.9) |
| [[SHP-77 (line)]] | alt | 14.0 | 0 | 1 | — | [[9-ING-41 (drug)]] 0.5 µM 0.0781× (z -8.9) |
| [[SNU-1 (line)]] | wt | 20.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0746× (z -12.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 27.4 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0863× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.34 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.96 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16285), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUXAP10]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[NBEAP2]] | +0.63 | +0.65 / +0.65 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TFB2M]] | +0.62 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ELP2]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[DUXAP9]] | +0.54 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[COQ8A]] | +0.54 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[SNU13]] | +0.52 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[DUSP11]] | +0.52 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[EDRF1]] | +0.51 | +0.46 / +0.38 | both halves | 7e-05 |  |
| [[THOC3]] | +0.50 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[FBXL4]] | +0.50 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[ABHD10]] | +0.49 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[AFMID]] | +0.49 | +0.42 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHD4]] | -0.52 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[SKIL]] | -0.45 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[SLK]] | -0.45 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[KLF3]] | -0.44 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[TRIP12]] | -0.44 | -0.24 / -0.49 | both halves | 4e-04 |  |
| [[SCYL2]] | -0.43 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[PLEKHG2]] | -0.42 | -0.22 / -0.45 | both halves | 6e-04 |  |
| [[CUX1]] | -0.42 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[STX4]] | -0.42 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[ATP9A]] | -0.42 | -0.14 / -0.51 | ⚠ one half (not replicated) | 0.002 |  |
| [[PEPD]] | -0.42 | -0.38 / -0.24 | both halves | 5e-04 |  |
| [[AKT1S1]] | -0.42 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[VPS18]] | -0.41 | -0.36 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers C2orf27A's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[NBEAP2]] | C | NBEAP2 activity raises C2orf27A's level | lines that do not express NBEAP2 (5) vs lines expressing it (45) | 5.62× lower at baseline in the lines without NBEAP2 | 0.006 | ⚠ within organs, on part of the lines; also absent: C2orf27A, ROPN1L, ENSG00000287621; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HEATR6]] | B | C2orf27A activity raises HEATR6's level | lines that do not express C2orf27A (5) vs lines expressing it (45) | 1.92× lower at baseline in the lines without C2orf27A | 0.014 | ⚠ within organs, on part of the lines; also absent: NBEAP2, UBA6-DT, ENSG00000287621; maybe low, not absent |
| [[CSNK2A1]] | B | C2orf27A activity raises CSNK2A1's level | lines that do not express C2orf27A (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without C2orf27A | 0.039 | ⚠ within organs, on part of the lines; also absent: NBEAP2, UBA6-DT, ENSG00000287621; maybe low, not absent |
| [[ZNF565]] | B | C2orf27A activity raises ZNF565's level | lines that do not express C2orf27A (5) vs lines expressing it (45) | 1.39× lower at baseline in the lines without C2orf27A | 0.043 | ⚠ within organs, on part of the lines; also absent: NBEAP2, UBA6-DT, ENSG00000287621; maybe low, not absent |
| [[MRPS26]] | B | C2orf27A activity raises MRPS26's level | lines that do not express C2orf27A (5) vs lines expressing it (45) | 1.60× lower at baseline in the lines without C2orf27A | 0.078 | ⚠ within organs, on part of the lines; also absent: NBEAP2, UBA6-DT, ENSG00000287621; maybe low, not absent |
| [[SLK]] | B | C2orf27A activity lowers SLK's level | lines that do not express C2orf27A (5) vs lines expressing it (45) | 1.92× higher at baseline in the lines without C2orf27A | 0.085 | ⚠ within organs, on part of the lines; also absent: NBEAP2, UBA6-DT, ENSG00000287621; maybe low, not absent |
| [[COQ8A]] | B | C2orf27A activity raises COQ8A's level | lines that do not express C2orf27A (5) vs lines expressing it (45) | 1.57× lower at baseline in the lines without C2orf27A | 0.088 | ⚠ within organs, on part of the lines; also absent: NBEAP2, UBA6-DT, ENSG00000287621; maybe low, not absent |
| [[AFMID]] | B | C2orf27A activity raises AFMID's level | lines that do not express C2orf27A (5) vs lines expressing it (45) | 1.39× lower at baseline in the lines without C2orf27A | 0.091 | ⚠ within organs, on part of the lines; also absent: NBEAP2, UBA6-DT, ENSG00000287621; maybe low, not absent |
| [[NBEAP2]] | C | C2orf27A activity raises NBEAP2's level | lines that do not express C2orf27A (5) vs lines expressing it (45) | 5.90× lower at baseline in the lines without C2orf27A | 0.002 | ⚠ within organs, on part of the lines; also absent: NBEAP2, UBA6-DT, ENSG00000287621; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.454). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (0.6, -19.2); signed map (-53.8, -1.2). **Vector** length 67.9, 11.7% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.0 | +0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.0 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +5.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.4 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | -2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -5.1 | -15.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.4 | -13.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -4.3 | -8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -4.0 | -12.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -5.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.0 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -6.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.4 | -4.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.4 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | long independently transcribed non-coding RNA 3124 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q21.2 — chr2:131,647,990-131,767,404 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C2orf27, C2orf27A |
| Gene groups (HGNC) | Long independently transcribed non-coding RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25077](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25077) · Entrez [29798](https://www.ncbi.nlm.nih.gov/gene/29798) · Ensembl [ENSG00000287151](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000287151)

## Data

Gene col 16285: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16285); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16285, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16285]; `tensor/DDL_lfc|DDL_z.npy` [16285]; `embed/gene_vectors.npy` [16285]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16285 or target_col == 16285). Every well: [[C2orf27A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C2orf27A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

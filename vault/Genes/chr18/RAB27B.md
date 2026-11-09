---
symbol: "RAB27B"
type: "gene"
col: 474
ensembl_id: "ENSG00000041353"
name: "RAB27B, member RAS oncogene family"
location: "18q21.2"
module: 19
arm: "+"
pooled_cpm: 68.23
n_lines_expressing: 35
n_dd_up: 14
n_dd_down: 34
n_dd_up_clean: 10
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 5
direction_downstream: 19
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# RAB27B

*RAB27B, member RAS oncogene family* — 18q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.51× (z +8.7, q 2e-15, up in 23 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.354× (z -21.7, q 0e+00, down in 30 of 33 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC68]] (+0.62, fdr 1e-05, ⚠ same locus), [[CYP24A1]] (+0.58, fdr 1e-05), [[RAB31]] (+0.58, fdr 1e-05), [[CD55]] (+0.57, fdr 1e-05); moves opposite to [[FAM156A]] (-0.50, fdr 3e-05), [[RECQL5]] (-0.45, fdr 5e-05), [[POLR1HASP]] (-0.43, fdr 5e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PTGES]] → it (grade B ⚠); 19 go from it, the strongest it → [[RBM47]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 474.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +8.7 | 2e-15 | 23/33 (KATO III, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +7.1 | 3e-10 | 15/28 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +6.7 | 5e-09 | 16/34 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +4.7 | 4e-04 | 12/33 (J82, HT-29, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +4.6 | 4e-04 | 14/33 (MIA PaCa-2, COLO 205, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +4.6 | 4e-04 | 17/33 (hTERT-HPNE, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +4.5 | 5e-04 | 14/34 (KATO III, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.30×** | +3.9 | 0.006 | 18/33 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.20×** | +3.9 | 0.006 | 12/33 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +3.7 | 0.013 | 12/30 (RPMI-7951, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.054 | 7/33 (AsPC-1, A-172, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.065 | 7/33 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.065 | 3/34 (HS-578T, HCT15, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.099 | 8/34 (HS-578T, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 474.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.354×** | -21.7 | 0e+00 | 30/33 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.408×** | -18.8 | 0e+00 | 32/34 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.437×** | -11.8 | 1e-29 | 26/33 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.502×** | -10.2 | 3e-22 | 23/33 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.525×** | -9.5 | 2e-19 | 28/33 (SNU-1, NCI-H2347, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.594×** | -7.4 | 1e-11 | 24/33 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.607×** | -7.4 | 1e-11 | 21/33 (SNU-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.607×** | -7.1 | 9e-11 | 24/35 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.639×** | -6.6 | 2e-09 | 24/32 (SW 900, NCI-H1792, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.663×** | -6.1 | 7e-08 | 20/33 (LoVo, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.673×** | -5.5 | 2e-06 | 21/33 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.694×** | -5.4 | 3e-06 | 20/33 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.702×** | -5.2 | 7e-06 | 19/33 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.729×** | -4.7 | 1e-04 | 18/33 (NCI-H1573, NCI-H460, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.730×** | -4.6 | 1e-04 | 18/33 (NCI-H23, NCI-H1573, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.719×** | -4.6 | 1e-04 | 16/33 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.583×** | -4.2 | 1e-03 | 19/34 (LS 180, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.831×** | -3.9 | 0.004 | 15/33 (NCI-H1573, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 474. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 374 | 0 | 20 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0837× (z -31.1) |
| [[NCI-H1792 (line)]] | alt | 354 | 0 | 16 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0878× (z -20.7) |
| [[NCI-H460 (line)]] | wt | 154 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0813× (z -39.2) |
| [[SNU-1 (line)]] | wt | 293 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -24.5) |
| [[A549 (line)]] | wt | 123 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0780× (z -18.6) |
| [[LoVo (line)]] | wt | 33.1 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -21.4) |
| [[BT-474 (line)]] | alt | 176 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -18.5) |
| [[KATO III (line)]] | alt | 24.1 | 4 (2 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 3.16× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 438 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0615× (z -31.8) |
| [[NCI-H2347 (line)]] | alt | 120 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -18.4) |
| [[Panc 03.27 (line)]] | alt | 39.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -9.9) |
| [[SW 900 (line)]] | alt | 48.4 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0914× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.197× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 56.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -16.5) |
| [[AsPC-1 (line)]] | alt | 31.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -14.6) |
| [[Hs 766T (line)]] | wt | 47.1 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -14.6) |
| [[NCI-H2030 (line)]] | alt | 52.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -16.2) |
| [[NCI-H23 (line)]] | alt | 30.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -12.8) |
| [[SW48 (line)]] | wt | 61.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -11.8) |
| [[A498 (line)]] | wt | 28.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -11.8) |
| [[SNU-423 (line)]] | alt | 54.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -15.1) |
| [[SW 1271 (line)]] | alt | 76.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0961× (z -10.8) |
| [[COLO 205 (line)]] | alt | 36.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -11.6) |
| [[HCT15 (line)]] | alt | 24.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 39.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -15.9) |
| [[LS 180 (line)]] | wt | 60.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 21.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.05× (z +9.6) | — |
| [[A-172 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.89 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.77 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.43 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 13.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.01 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.37 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.04 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.75 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.86 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.35 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.46 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.91 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 474), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC68]] | +0.62 | +0.68 / +0.57 | both halves | 1e-05 | STRING 437; ⚠ same locus (6.0 kb: neighbours can correlate without regulation) |
| [[CYP24A1]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[RAB31]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 | same gene group; pathway: RAB GEFs exchange GTP for GDP on RABs |
| [[CD55]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[EDIL3]] | +0.55 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[SMOC1]] | +0.53 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[AHR]] | +0.53 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[NHS]] | +0.53 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[CRLF2]] | +0.51 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ANKRD29]] | +0.51 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[RSPO3]] | +0.51 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[IGFBP1]] | +0.50 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[RDH10]] | +0.48 | +0.41 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM156A]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[RECQL5]] | -0.45 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[POLR1HASP]] | -0.43 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[TTC28-AS1]] | -0.43 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[NPHP3]] | -0.42 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[MRPL23]] | -0.40 | -0.40 / -0.37 | both halves | 7e-05 |  |
| [[RPAP1]] | -0.40 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[PAAF1]] | -0.40 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[PGAP2]] | -0.40 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[ZNF717]] | -0.40 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[ZNF248]] | -0.39 | -0.20 / -0.36 | ⚠ not reproduced | 8e-04 |  |
| [[ZNG1E]] | -0.39 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[PYY]] | -0.39 | -0.35 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTGES]] | B | PTGES activity raises RAB27B's level | lines that do not express PTGES (17) vs lines expressing it (33) | 2.57× lower at baseline in the lines without PTGES | 0.061 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[LIPH]] | B | LIPH activity raises RAB27B's level | lines that do not express LIPH (27) vs lines expressing it (23) | 3.04× lower at baseline in the lines without LIPH | 0.062 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[XDH]] | B | XDH activity raises RAB27B's level | lines that do not express XDH (22) vs lines expressing it (28) | 2.79× lower at baseline in the lines without XDH | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564 |
| [[RIN2]] | B | RIN2 activity raises RAB27B's level | lines that do not express RIN2 (9) vs lines expressing it (41) | 3.28× lower at baseline in the lines without RIN2 | 0.095 | ⚠ within organs, on part of the lines; also absent: ANTXR2; maybe low, not absent |
| [[CCDC68]] | C | CCDC68 activity raises RAB27B's level | lines that do not express CCDC68 (25) vs lines expressing it (25) | 3.78× lower at baseline in the lines without CCDC68 | 0.004 | ⚠ within organs, on part of the lines; also absent: GRB7, SH2D3A, GOLT1A; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 17, C 2. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBM47]] | B | RAB27B activity raises RBM47's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 3.71× lower at baseline in the lines without RAB27B | 0.005 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[NHS]] | B | RAB27B activity raises NHS's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 4.40× lower at baseline in the lines without RAB27B | 0.010 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[LIPH]] | B | RAB27B activity raises LIPH's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 3.51× lower at baseline in the lines without RAB27B | 0.025 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[CD55]] | B | RAB27B activity raises CD55's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 2.78× lower at baseline in the lines without RAB27B | 0.034 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[PTGES]] | B | RAB27B activity raises PTGES's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 2.31× lower at baseline in the lines without RAB27B | 0.038 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[XDH]] | B | RAB27B activity raises XDH's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 2.91× lower at baseline in the lines without RAB27B | 0.039 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| cells under [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM | B | RAB27B activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 5 µM (protects the cells) | lines that do not express RAB27B (15) vs lines expressing it (33) | the lines without RAB27B: 0.88× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[CAB39]] | B | RAB27B activity raises CAB39's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 1.42× lower at baseline in the lines without RAB27B | 0.049 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[ATP2B1]] | B | RAB27B activity raises ATP2B1's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 1.41× lower at baseline in the lines without RAB27B | 0.069 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[RIN2]] | B | RAB27B activity raises RIN2's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 2.85× lower at baseline in the lines without RAB27B | 0.070 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[RSPO3]] | B | RAB27B activity raises RSPO3's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 2.16× lower at baseline in the lines without RAB27B | 0.071 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| cells under [[MK-3903 (drug)]] 0.05 µM | B | RAB27B activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express RAB27B (15) vs lines expressing it (33) | the lines without RAB27B: 0.88× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.334). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.1, 27.2); signed map (37.3, 46.8). **Vector** length 104, 26.8% of its response variance represented; |z| ≥ 3 in 1,114 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +2.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.8 | +2.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.1 | -2.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.9 | -3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -18.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -3.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.3 | -2.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.3 | -1.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | RAB27B, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.2 — chr18:54,717,860-54,895,516 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 9 pathways, smallest: RAB geranylgeranylation; RAB GEFs exchange GTP for GDP on RABs; Platelet degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [O00194](https://www.uniprot.org/uniprotkb/O00194) (Ras-related protein Rab-27B):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB27B regulates homeostasis of late endocytic pathway, including endosomal positioning, maturation and secretion. …

**Summary**, from NCBI Gene [5874](https://www.ncbi.nlm.nih.gov/gene/5874):

> Enables guanyl ribonucleotide binding activity; myosin V binding activity; and protein domain specific binding activity. Involved in multivesicular body sorting pathway and positive regulation of exocytosis. Located in Golgi stack and cytoplasmic vesicle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9767](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9767) · Entrez [5874](https://www.ncbi.nlm.nih.gov/gene/5874) · UniProt [O00194](https://www.uniprot.org/uniprotkb/O00194) · Ensembl [ENSG00000041353](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000041353)

## Data

Gene col 474: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 474); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 474, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 474]; `tensor/DDL_lfc|DDL_z.npy` [474]; `embed/gene_vectors.npy` [474]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 474 or target_col == 474). Every well: [[RAB27B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB27B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

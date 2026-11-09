---
symbol: "MTO1"
type: "gene"
col: 5675
ensembl_id: "ENSG00000135297"
name: "mitochondrial tRNA translation optimization 1"
location: "6q13"
module: 133
arm: "+"
pooled_cpm: 25.32
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# MTO1

*mitochondrial tRNA translation optimization 1* — 6q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.54× (z +11.3, q 6e-27, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.749× (z -5.4, q 2e-05, down in 23 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.815× (z -5.4, q 2e-05, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MORN4]] (+0.71, fdr 7e-06), [[TIMM44]] (+0.67, fdr 7e-06), [[ZBED3]] (+0.62, fdr 1e-05); moves opposite to [[DIAPH1]] (-0.62, fdr 1e-05), [[PKM]] (-0.54, fdr 1e-05), [[EPB41L2]] (-0.54, fdr 1e-05).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NIBAN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5675.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +11.3 | 6e-27 | 36/47 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +10.3 | 3e-22 | 36/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +7.2 | 1e-10 | 33/48 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +7.1 | 2e-10 | 27/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +6.0 | 2e-07 | 21/47 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +5.9 | 3e-07 | 21/43 (LOX-IMVI, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +5.6 | 2e-06 | 20/48 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +5.2 | 2e-05 | 18/48 (C-33 A, NCI-H2030, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.17× | +4.2 | 0.002 | 15/48 (A-427, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.002 | 13/48 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +3.8 | 0.007 | 16/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +3.8 | 0.007 | 16/46 (COLO 205, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.007 | 12/48 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.023 | 14/46 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.038 | 10/48 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.13× | +3.1 | 0.067 | 5/48 (SW48, A549, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.0 | 0.085 | 11/48 (LoVo, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5675.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.749×** | -5.4 | 2e-05 | 23/48 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.815×** | -5.4 | 2e-05 | 21/48 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.733×** | -5.3 | 2e-05 | 19/38 (SHP-77, PANC-1, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.773×** | -4.8 | 2e-04 | 21/48 (PANC-1, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.805×** | -4.0 | 0.006 | 13/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.808×** | -3.7 | 0.024 | 15/47 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.826×** | -3.6 | 0.028 | 13/48 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.875× | -3.5 | 0.028 | 16/48 (PANC-1, SNU-1, …) | top dose only |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.828×** | -3.5 | 0.028 | 11/48 (A498, SW 1271, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.823×** | -3.5 | 0.028 | 13/48 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.833×** | -3.4 | 0.031 | 14/48 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.833×** | -3.4 | 0.031 | 6/48 (LS 180, NCI-H23, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.837× | -3.3 | 0.039 | 10/48 (HT-29, A549, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | 0.838× | -3.3 | 0.039 | 19/43 (LoVo, PANC-1, …) | inconsistent across doses | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.840× | -3.2 | 0.044 | 12/47 (PANC-1, SW480, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.784×** | -3.2 | 0.044 | 14/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | 0.848× | -3.1 | 0.070 | 12/48 (A549, LS 180, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.850× | -3.0 | 0.072 | 10/47 (HT-29, SW480, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.855× | -2.9 | 0.095 | 10/48 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.855× | -2.9 | 0.095 | 4/48 (NCI-H1792, HT-29, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5675. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 24.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0494× (z -24.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[PANC-1 (line)]] | alt | 64.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C-33 A (line)]] | alt | 22.7 | 1 | 1 | [[5-Azacytidine (drug)]] 5 µM 4.39× (z +8.7) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.111× (z -11.9) |
| [[SW48 (line)]] | wt | 26.0 | 0 | 2 (1 ⚠) | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.125× (z -12.1) |
| [[SW480 (line)]] | alt | 27.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.3) | — |
| [[A549 (line)]] | wt | 12.2 | 0 | 1 | — | [[Belzutifan (drug)]] 5 µM 0.0605× (z -9.2) |
| [[AN3 CA (line)]] | alt | 25.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0870× (z -9.4) |
| [[Hs 766T (line)]] | wt | 18.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.272× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 26.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.49× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 21.1 | 0 | 1 | — | [[vincristine (drug)]] 5 µM 0.0673× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 42.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 33.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.345× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 20.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW 900 (line)]] | alt | 22.4 | 0 | 1 | — | [[OTS514 (drug)]] 5 µM 0.0651× (z -9.2) |
| [[A-172 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5675), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MORN4]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[TIMM44]] | +0.67 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ZBED3]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[TMEM267]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[EIF2S2]] | +0.60 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[PYROXD1]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 | same gene group |
| [[ASTE1]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[BRAP]] | +0.59 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[SLC35B1]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ZNF383]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[PGLS-DT]] | +0.58 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[TMEM216]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIAPH1]] | -0.62 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[PKM]] | -0.54 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[EPB41L2]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[CORO1C]] | -0.54 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[USP9X]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[HPSE]] | -0.53 | -0.57 / -0.32 | both halves | 2e-04 |  |
| [[CD59]] | -0.53 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[ITGB1]] | -0.52 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[YWHAZ]] | -0.52 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[NEDD4L]] | -0.52 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[RCOR1]] | -0.51 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[KLF12]] | -0.51 | -0.52 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NIBAN1]] | B | NIBAN1 activity raises MTO1's level | lines that do not express NIBAN1 (11) vs lines expressing it (39) | 1.21× lower at baseline in the lines without NIBAN1 | 0.056 | ⚠ within organs, on part of the lines; also absent: CAV1, FGF2, PCOLCE2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-24.5, 21.7); signed map (-6.0, -8.4). **Vector** length 89.7, 18.3% of its response variance represented; |z| ≥ 3 in 916 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.9 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +10.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +3.8 | +4.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.1 | +7.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.1 | +0.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +1.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -5.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | -0.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | -2.7 | -3.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.7 | -5.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.4 | -3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -3.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.0 | -3.1 |
|  | [[Thymol (drug)]] 5 µM |  | -1.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial tRNA translation optimization 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q13 — chr6:73,461,578-73,509,236 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Flavoproteins |
| Reactome | 3 pathways, smallest: tRNA modification in the mitochondrion; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2Z2](https://www.uniprot.org/uniprotkb/Q9Y2Z2) (5-taurinomethyluridine-[tRNA] synthase subunit MTO1, mitochondrial):

> Component of the GTPBP3-MTO1 complex that catalyzes the 5-taurinomethyluridine (taum(5)U) modification at the 34th wobble position (U34) of mitochondrial tRNAs (mt-tRNAs), which plays a role in mt-tRNA decoding and mitochondrial translation. Taum(5)U formation on mammalian mt-tRNA requires the presence of both GTPBP3-mediated GTPase activity and MTO1 catalytic activity.

**Summary**, from NCBI Gene [25821](https://www.ncbi.nlm.nih.gov/gene/25821):

> This gene encodes a mitochondrial protein thought to be involved in mitochondrial tRNA modification. The encoded protein may also play a role in the expression of the non-syndromic and aminoglycoside-induced deafness phenotypes associated with a specific mutation in the mitochondrial 12S rRNA gene. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19261](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19261) · Entrez [25821](https://www.ncbi.nlm.nih.gov/gene/25821) · UniProt [Q9Y2Z2](https://www.uniprot.org/uniprotkb/Q9Y2Z2) · Ensembl [ENSG00000135297](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135297)

## Data

Gene col 5675: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5675); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5675, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5675]; `tensor/DDL_lfc|DDL_z.npy` [5675]; `embed/gene_vectors.npy` [5675]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5675 or target_col == 5675). Every well: [[MTO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

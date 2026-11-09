---
symbol: "PRDM1"
type: "gene"
col: 649
ensembl_id: "ENSG00000057657"
name: "PR/SET domain 1"
location: "6q21"
module: 34
arm: "+"
pooled_cpm: 25.8
n_lines_expressing: 35
n_dd_up: 8
n_dd_down: 41
n_dd_up_clean: 8
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 12
direction_downstream: 5
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PRDM1

*PR/SET domain 1* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.87× (z +10.2, q 1e-21, up in 23 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.336× (z -16.3, q 0e+00, down in 25 of 33 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKN1A]] (+0.54, fdr 5e-05), [[LAMB3]] (+0.52, fdr 2e-05), [[MAST4]] (+0.52, fdr 3e-05); moves opposite to [[EEF2K]] (-0.42, fdr 1e-04), [[CEP20]] (-0.41, fdr 7e-05), [[ZC3H14]] (-0.40, fdr 9e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[IL1R2]] → it (grade B ⚠); 5 go from it, the strongest it → [[KANK3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 649.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.87×** | +10.2 | 1e-21 | 23/34 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +6.5 | 2e-08 | 17/33 (PANC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +5.3 | 3e-05 | 18/34 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +4.4 | 0.001 | 14/33 (HOP62, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 0.001 | 10/33 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 0.002 | 10/33 (NCI-H460, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.2 | 0.002 | 1/34 (NCI-H2030) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.65×** | +3.8 | 0.011 | 14/32 (HOP62, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.19× | +3.7 | 0.011 | 7/33 (A498, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.082 | 11/32 (NCI-H460, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Amsacrine (drug)]] 0.5 µM |  | 1.23× | +3.1 | 0.11 | 9/34 (SW48, NCI-H460, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM |  | 1.24× | +3.1 | 0.11 | 6/33 (LoVo, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 649.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.336×** | -16.3 | 0e+00 | 25/33 (hTERT-HPNE, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.457×** | -11.7 | 2e-29 | 23/33 (hTERT-HPNE, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.465×** | -11.5 | 3e-28 | 24/33 (hTERT-HPNE, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.524×** | -9.7 | 6e-20 | 23/30 (NCI-H2347, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.533×** | -9.4 | 4e-19 | 22/33 (NCI-H23, SW48, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.525×** | -9.3 | 1e-18 | 20/27 (NCI-H2347, CFPAC-1, …) | rises with dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.575×** | -8.3 | 8e-15 | 21/34 (NCI-H23, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.582×** | -8.1 | 4e-14 | 22/33 (KATO III, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.574×** | -8.0 | 8e-14 | 21/32 (hTERT-HPNE, NCI-H23, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.712×** | -7.2 | 4e-11 | 20/33 (AsPC-1, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.625×** | -7.1 | 9e-11 | 18/32 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.732×** | -6.6 | 2e-09 | 19/33 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.704×** | -5.3 | 6e-06 | 15/33 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~19% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.690×** | -5.3 | 6e-06 | 17/33 (HS-578T, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.696×** | -5.2 | 6e-06 | 16/32 (NCI-H23, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.707×** | -5.2 | 7e-06 | 13/33 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.504×** | -5.2 | 8e-06 | 18/30 (SW48, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **0.700×** | -5.0 | 2e-05 | 19/34 (CFPAC-1, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.547×** | -4.5 | 2e-04 | 16/32 (NCI-H2347, AsPC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 649. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 68.5 | 0 | 14 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0790× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.164× (z -13.9) |
| [[CFPAC-1 (line)]] | alt | 48.6 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0647× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.107× (z -14.4) |
| [[hTERT-HPNE (line)]] | wt | 132 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0464× (z -20.0) |
| [[NCI-H460 (line)]] | wt | 38.1 | 7 (3 ⚠) | 2 | [[Harringtonine (drug)]] 0.5 µM 5.65× (z +13.4) | [[Auranofin (drug)]] 5 µM 0.261× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 66.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0677× (z -22.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0700× (z -15.4) |
| [[NCI-H1792 (line)]] | alt | 50.1 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -11.3) |
| [[SW48 (line)]] | wt | 117 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0646× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.141× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 60.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.303× (z -9.3) |
| [[HOP62 (line)]] | alt | 44.9 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -12.6) |
| [[KATO III (line)]] | alt | 45.8 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.296× (z -8.9) |
| [[LoVo (line)]] | wt | 46.5 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 17.3× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.172× (z -14.6) |
| [[RPMI-7951 (line)]] | alt | 33.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0608× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -9.7) |
| [[A498 (line)]] | wt | 7.89 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +12.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.207× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[Panc 03.27 (line)]] | alt | 33.8 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -10.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.182× (z -9.8) |
| [[A549 (line)]] | wt | 36.4 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 15.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 34.5 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[H4 (line)]] | wt | 22.5 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0625× (z -9.3) |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0232× (z -16.5) |
| [[LOX-IMVI (line)]] | wt | 48.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 34.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.231× (z -10.7) |
| [[PANC-1 (line)]] | alt | 14.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.1× (z +8.6) | — |
| [[SW480 (line)]] | alt | 17.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.227× (z -9.7) |
| [[A-172 (line)]] | wt | 4.18 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.97 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.27 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.09 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 649), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN1A]] | +0.54 | +0.39 / +0.60 | both halves | 5e-05 | pathway: Affinity selection of immunoglobulins |
| [[LAMB3]] | +0.52 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[MAST4]] | +0.52 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[IL1R2]] | +0.52 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[GRHL3]] | +0.51 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[DHRS9]] | +0.51 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[PLEK2]] | +0.51 | +0.55 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[PTK2B]] | +0.51 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[ABTB2]] | +0.50 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[KDM7A-DT]] | +0.50 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[GJB3]] | +0.50 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[HS3ST1]] | +0.50 | +0.51 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF2K]] | -0.42 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[CEP20]] | -0.41 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[ZC3H14]] | -0.40 | -0.45 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL1R2]] | B | IL1R2 activity raises PRDM1's level | lines that do not express IL1R2 (23) vs lines expressing it (27) | 2.60× lower at baseline in the lines without IL1R2 | 0.008 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[FOXL1]] | B | FOXL1 activity raises PRDM1's level | lines that do not express FOXL1 (25) vs lines expressing it (25) | 2.72× lower at baseline in the lines without FOXL1 | 0.025 | ⚠ within organs, on part of the lines; also absent: SIRLNT, PTHLH, WNT5A |
| [[F3]] | B | F3 activity raises PRDM1's level | lines that do not express F3 (24) vs lines expressing it (26) | 2.60× lower at baseline in the lines without F3 | 0.034 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[PKP1]] | B | PKP1 activity raises PRDM1's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 2.81× lower at baseline in the lines without PKP1 | 0.035 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[DSG3]] | B | DSG3 activity raises PRDM1's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 3.94× lower at baseline in the lines without DSG3 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1 |
| [[G0S2]] | B | G0S2 activity raises PRDM1's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 2.41× lower at baseline in the lines without G0S2 | 0.043 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD |
| [[LAMB3]] | B | LAMB3 activity raises PRDM1's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 2.86× lower at baseline in the lines without LAMB3 | 0.048 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[EFNB2]] | B | EFNB2 activity raises PRDM1's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 2.67× lower at baseline in the lines without EFNB2 | 0.049 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[HSD11B1]] | B | HSD11B1 activity raises PRDM1's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 2.52× lower at baseline in the lines without HSD11B1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA |
| [[KLK11]] | B | KLK11 activity raises PRDM1's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 3.48× lower at baseline in the lines without KLK11 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ |
| [[IL1RL1]] | B | IL1RL1 activity raises PRDM1's level | lines that do not express IL1RL1 (32) vs lines expressing it (18) | 2.18× lower at baseline in the lines without IL1RL1 | 0.098 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, IGFBP1 |
| [[VGLL3]] | C | VGLL3 activity raises PRDM1's level | lines that do not express VGLL3 (30) vs lines expressing it (20) | 3.24× lower at baseline in the lines without VGLL3 | 0.004 | ⚠ within organs, on part of the lines; also absent: EDNRA, APBB1IP, LINC02882; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KANK3]] | B | PRDM1 activity lowers KANK3's level | lines that do not express PRDM1 (15) vs lines expressing it (35) | 1.34× higher at baseline in the lines without PRDM1 | 0.040 | ⚠ within organs, on part of the lines; also absent: PCED1B, AMIGO2, NRP1 |
| [[LAMB3]] | B | PRDM1 activity raises LAMB3's level | lines that do not express PRDM1 (15) vs lines expressing it (35) | 2.78× lower at baseline in the lines without PRDM1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PCED1B, AMIGO2, NRP1 |
| [[IL1R2]] | B | PRDM1 activity raises IL1R2's level | lines that do not express PRDM1 (15) vs lines expressing it (35) | 1.63× lower at baseline in the lines without PRDM1 | 0.088 | ⚠ within organs, on part of the lines; also absent: PCED1B, AMIGO2, NRP1 |
| [[EFNB2]] | B | PRDM1 activity raises EFNB2's level | lines that do not express PRDM1 (15) vs lines expressing it (35) | 2.61× lower at baseline in the lines without PRDM1 | 0.095 | ⚠ within organs, on part of the lines; also absent: PCED1B, AMIGO2, NRP1 |
| [[VGLL3]] | C | PRDM1 activity raises VGLL3's level | lines that do not express PRDM1 (15) vs lines expressing it (35) | 4.13× lower at baseline in the lines without PRDM1 | 0.022 | ⚠ within organs, on part of the lines; also absent: PCED1B, AMIGO2, NRP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.464). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.1, 52.8); signed map (3.0, 35.4). **Vector** length 108, 28.0% of its response variance represented; |z| ≥ 3 in 1,157 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.9 | +0.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +10.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.6 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | -1.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.5 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +3.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -8.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -7.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -4.5 |
|  | [[NG25 (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.6 | -3.5 |
|  | [[Afatinib (drug)]] 5 µM |  | -2.5 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | PR/SET domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:105,993,463-106,109,939 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRDI-BF1, Blimp-1; previously BLIMP1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; PR/SET domain family; Putative lysine methyltransferases |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 12 pathways, smallest: Specification of primordial germ cells; STAT3 nuclear events downstream of ALK signaling; Signaling by ALK |
| Matched by | ensembl_id |

**Function**, from UniProt [O75626](https://www.uniprot.org/uniprotkb/O75626) (PR domain zinc finger protein 1):

> Transcription factor that mediates a transcriptional program in various innate and adaptive immune tissue-resident lymphocyte T cell types such as tissue-resident memory T (Trm), natural killer (trNK) and natural killer T (NKT) cells and negatively regulates gene expression of proteins that promote the egress of tissue-resident T-cell populations from non-lymphoid organs. Plays a role in the development, retention and long-term establishment of adaptive and innate tissue-resident lymphocyte T …

**Summary**, from NCBI Gene [639](https://www.ncbi.nlm.nih.gov/gene/639):

> This gene encodes a protein that acts as a repressor of beta-interferon gene expression. The protein binds specifically to the PRDI (positive regulatory domain I element) of the beta-IFN gene promoter. Transcription of this gene increases upon virus induction. Two alternatively spliced transcript variants that encode different isoforms have been reported. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9346](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9346) · Entrez [639](https://www.ncbi.nlm.nih.gov/gene/639) · UniProt [O75626](https://www.uniprot.org/uniprotkb/O75626) · Ensembl [ENSG00000057657](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000057657)

## Data

Gene col 649: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 649); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 649, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 649]; `tensor/DDL_lfc|DDL_z.npy` [649]; `embed/gene_vectors.npy` [649]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 649 or target_col == 649). Every well: [[PRDM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRDM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

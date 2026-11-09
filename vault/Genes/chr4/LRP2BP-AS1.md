---
symbol: "LRP2BP-AS1"
type: "gene"
col: 14692
ensembl_id: "ENSG00000250410"
name: ""
location: ""
module: 38
arm: "+"
pooled_cpm: 15.87
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 31
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# LRP2BP-AS1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Filgotinib (drug)]] 5 µM: 1.43× (z +4.4, q 0.006, up in 18 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (16 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.203× (z -10.3, q 6e-22, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02798]] (+0.68, fdr 7e-06), [[CDKL4]] (+0.65, fdr 7e-06), [[APRG1]] (+0.64, fdr 7e-06); moves opposite to [[SLC25A12]] (-0.57, fdr 1e-05), [[TM7SF3]] (-0.54, fdr 1e-05), [[WDR17]] (-0.52, fdr 3e-05).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14692.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | **1.43×** | +4.4 | 0.006 | 18/48 (CFPAC-1, RKO, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.68× | +3.4 | 0.23 | 6/43 (SW480, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 16 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14692.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.203×** | -10.3 | 6e-22 | 41/48 (LoVo, CFPAC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.408×** | -9.3 | 3e-18 | 31/42 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.440×** | -8.6 | 2e-15 | 31/47 (SNU-423, A-172, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.524×** | -7.9 | 3e-13 | 31/45 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.541×** | -7.5 | 5e-12 | 30/47 (C32, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.580×** | -6.7 | 2e-09 | 27/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **0.596×** | -6.3 | 2e-08 | 24/36 (NCI-H1573, LS 180, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.598×** | -6.3 | 2e-08 | 27/47 (SW48, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.608×** | -6.1 | 7e-08 | 23/47 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.619×** | -5.9 | 2e-07 | 27/48 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.620×** | -5.9 | 2e-07 | 29/48 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.720×** | -5.7 | 6e-07 | 24/46 (NCI-H23, A-172, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.647×** | -5.3 | 4e-06 | 29/47 (C32, NCI-H1573, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.603×** | -5.3 | 5e-06 | 21/40 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.684×** | -4.6 | 1e-04 | 22/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.492×** | -4.6 | 2e-04 | 21/43 (Panc 03.27, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.769×** | -4.5 | 2e-04 | 25/48 (SNU-1, C32, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.652×** | -4.5 | 3e-04 | 20/46 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.783×** | -4.2 | 7e-04 | 20/48 (RKO, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.742×** | -3.7 | 0.007 | 14/47 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.605×** | -3.2 | 0.028 | 15/41 (SW48, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.630×** | -3.0 | 0.062 | 12/43 (A549, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.638×** | -2.9 | 0.077 | 11/43 (CFPAC-1, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.642×** | -2.8 | 0.084 | 9/41 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.785×** | -2.8 | 0.093 | 14/45 (CFPAC-1, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14692. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 36.3 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0559× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.119× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 35.6 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -9.6) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.256× (z -9.4) |
| [[A-172 (line)]] | wt | 23.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -13.6) ⚠ cell-cycle shift, explains ~72% of this change |
| [[J82 (line)]] | alt | 23.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0676× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[PANC-1 (line)]] | alt | 10.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0561× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[LoVo (line)]] | wt | 19.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.104× (z -8.8) |
| [[SW480 (line)]] | alt | 23.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[HepG2_C3A (line)]] | wt | 28.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.184× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 21.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0765× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.101× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 19.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -10.8) ⚠ cell-cycle shift, explains ~72% of this change |
| [[NCI-H23 (line)]] | alt | 14.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -16.6) ⚠ cell-cycle shift, explains ~72% of this change |
| [[RKO (line)]] | wt | 18.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -9.2) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.307× (z -8.8) |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0524× (z -13.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW48 (line)]] | wt | 16.7 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0710× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0594× (z -11.8) ⚠ toxic |
| [[C32 (line)]] | wt | 25.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.183× (z -9.8) |
| [[COLO 205 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0804× (z -9.9) ⚠ toxic |
| [[HCT15 (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[HOP62 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -9.4) ⚠ cell-cycle shift, explains ~54% of this change |
| [[KATO III (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -9.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[LOX-IMVI (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.173× (z -9.2) ⚠ cell-cycle shift, explains ~99% of this change |
| [[LS 180 (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0729× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[Panc 03.27 (line)]] | alt | 14.3 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0377× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0771× (z -10.8) ⚠ toxic |
| [[A-427 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14692), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02798]] | +0.68 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.65 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[APRG1]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[LINC01619]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.63 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[SLC22A14]] | +0.63 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[BLZF2P]] | +0.62 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[LINC02804]] | +0.62 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[WNT2B]] | +0.61 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ORAI2]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SLC23A3]] | +0.60 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[TEX29]] | +0.60 | +0.51 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A12]] | -0.57 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[TM7SF3]] | -0.54 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[WDR17]] | -0.52 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[NDUFA9]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[FBXO7]] | -0.52 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[JKAMP]] | -0.51 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[HSF2]] | -0.51 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[C2CD5]] | -0.51 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[METTL14]] | -0.51 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[TADA1]] | -0.51 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[TRAPPC11]] | -0.50 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[HEATR6]] | -0.50 | -0.52 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.2, -17.0); signed map (14.7, 8.2). **Vector** length 83.3, 17.8% of its response variance represented; |z| ≥ 3 in 1,154 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.6 | -0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +4.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | -0.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -4.3 | -3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.7 | -4.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.6 | -4.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.6 | -10.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.5 | -9.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -3.2 | -3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -4.6 |

## What is on record

> [!warning] No registry record
> LRP2BP-AS1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 14692: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14692); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14692, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14692]; `tensor/DDL_lfc|DDL_z.npy` [14692]; `embed/gene_vectors.npy` [14692]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14692 or target_col == 14692). Every well: [[LRP2BP-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRP2BP-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

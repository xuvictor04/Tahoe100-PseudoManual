---
symbol: "RNF2"
type: "gene"
col: 4277
ensembl_id: "ENSG00000121481"
name: "ring finger protein 2"
location: "1q25.3"
module: 188
arm: "+"
pooled_cpm: 38.2
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/188"]
generated_by: "tahoemap"
---

# RNF2

*ring finger protein 2* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 5 µM: 1.47× (z +4.7, q 0.002, up in 16 of 43 measured lines) ⚠ toxic.
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.580× (z -17.6, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[REPS1]] (+0.63, fdr 1e-05), [[MCUR1]] (+0.62, fdr 1e-05, ⚠ MCUR1 in the vector space only through flagged drug-doses), [[TMOD2]] (+0.61, fdr 2e-05), [[RFXAP]] (+0.60, fdr 2e-05); moves opposite to [[TTC41P]] (-0.59, fdr 1e-04), [[ASH1L]] (-0.51, fdr 3e-05), [[LINC00910]] (-0.50, fdr 8e-05).
> It is in [[Module 188]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4277.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.7 | 0.002 | 16/43 (A498, HT-29, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Roxadustat (drug)]] 5 µM |  | 1.17× | +3.5 | 0.13 | 10/47 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.10× | +3.2 | 0.21 | 6/48 (hTERT-HPNE, Hs 766T, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.2 | 0.21 | 14/47 (COLO 205, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.14× | +3.1 | 0.21 | 11/47 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.1 | 0.21 | 9/48 (CFPAC-1, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4277.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.580×** | -17.6 | 0e+00 | 42/48 (AsPC-1, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.620×** | -10.9 | 3e-25 | 37/48 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.615×** | -10.7 | 2e-24 | 37/48 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.635×** | -10.4 | 4e-23 | 36/48 (LOX-IMVI, AsPC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.707×** | -7.6 | 3e-12 | 26/47 (C32, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.739×** | -6.4 | 2e-08 | 24/44 (SK-MEL-2, HT-29, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.841× | -5.6 | 2e-06 | 23/47 (HS-578T, LOX-IMVI, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.784×** | -5.5 | 2e-06 | 24/48 (AsPC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.788×** | -5.2 | 1e-05 | 22/48 (NCI-H1573, AsPC-1, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.801×** | -5.0 | 2e-05 | 21/46 (AsPC-1, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **0.801×** | -5.0 | 2e-05 | 20/44 (AsPC-1, A-172, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.820×** | -4.5 | 3e-04 | 16/48 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.869× | -4.5 | 3e-04 | 18/48 (A-172, SW1417, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.948× | -4.3 | 9e-04 | 2/48 (CHP-212, SW 1088) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.721×** | -3.9 | 0.004 | 14/46 (HT-29, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.854× | -3.5 | 0.019 | 13/47 (hTERT-HPNE, RKO, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.856× | -3.4 | 0.023 | 9/47 (NCI-H1573, C32, …) | top dose only |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | 0.871× | -3.1 | 0.048 | 11/47 (SNU-1, SW 1271, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.873× | -3.1 | 0.057 | 7/48 (NCI-H2347, RKO, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | 0.877× | -3.0 | 0.076 | 8/48 (NCI-H2030, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4277. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 64.0 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -17.8) |
| [[LOX-IMVI (line)]] | wt | 51.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -14.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -12.7) |
| [[C32 (line)]] | wt | 81.6 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -16.4) |
| [[HEC-1-A (line)]] | alt | 51.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 62.7 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -13.4) |
| [[A-172 (line)]] | wt | 44.5 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -12.5) |
| [[HS-578T (line)]] | alt | 30.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -19.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -10.1) |
| [[C-33 A (line)]] | alt | 73.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 47.1 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.134× (z -9.5) |
| [[HT-29 (line)]] | alt | 52.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 32.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 49.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A549 (line)]] | wt | 33.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -10.2) |
| [[LoVo (line)]] | wt | 42.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 37.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.398× (z -8.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 33.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 21.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -11.4) |
| [[PANC-1 (line)]] | alt | 34.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.584× (z -9.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[RKO (line)]] | wt | 47.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -11.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SHP-77 (line)]] | alt | 43.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -10.9) |
| [[SW 900 (line)]] | alt | 29.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -8.8) |
| [[SW48 (line)]] | wt | 33.3 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -8.6) |
| [[SW480 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.459× (z -8.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4277), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REPS1]] | +0.63 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[MCUR1]] ⚠ | +0.62 | +0.53 / +0.55 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMOD2]] | +0.61 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[RFXAP]] | +0.60 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[AADAT]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[CSNK1G3]] | +0.59 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[KIF2A]] | +0.59 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[SMIM13]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SERAC1]] | +0.58 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[SNPH]] | +0.58 | +0.52 / +0.40 | both halves | 4e-05 |  |
| [[ZFAND4]] | +0.57 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[MBD2]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[USP46]] | +0.57 | +0.57 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC41P]] | -0.59 | -0.62 / -0.35 | both halves | 1e-04 |  |
| [[ASH1L]] | -0.51 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[LINC00910]] | -0.50 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[RFX1]] | -0.50 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[DYNC2I1]] | -0.49 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[UBAP2]] | -0.49 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[ZNF335]] | -0.49 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[ANKHD1-EIF4EBP3]] | -0.48 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[MZF1]] | -0.48 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[LINC01004]] | -0.48 | -0.55 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RNF2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TMSB15B]] | B | TMSB15B activity lowers RNF2's level | lines that do not express TMSB15B (11) vs lines expressing it (39) | 1.27× higher at baseline in the lines without TMSB15B | 0.0997 | ⚠ within organs, on part of the lines; also absent: ENSG00000288597, PRKD1, GRIK4 |
| [[FSD1L]] | C | FSD1L activity raises RNF2's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 1.92× lower at baseline in the lines without FSD1L | 0.064 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 188]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.677). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.2, -3.6); signed map (-36.6, -18.1). **Vector** length 85.1, 16.9% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.8 | +3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.9 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.8 | +0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +2.8 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -10.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.0 | -7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.9 | -5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -17.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -4.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Thymol (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:185,045,497-185,102,603 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BAP-1, BAP1, DING, HIPI3, RING1B, RING2 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 20 pathways, smallest: SUMOylation of DNA methylation proteins; Transcriptional Regulation by E2F6; RUNX1 interacts with co-factors whose precise effect on RUNX1 targets is not known |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99496](https://www.uniprot.org/uniprotkb/Q99496) (E3 ubiquitin-protein ligase RING2):

> E3 ubiquitin-protein ligase that mediates monoubiquitination of 'Lys-119' of histone H2A (H2AK119Ub), thereby playing a central role in histone code and gene regulation. H2AK119Ub gives a specific tag for epigenetic transcriptional repression and participates in X chromosome inactivation of female mammals. May be involved in the initiation of both imprinted and random X inactivation (By similarity). Essential component of a Polycomb group (PcG) multiprotein PRC1-like complex, a complex class …

**Summary**, from NCBI Gene [6045](https://www.ncbi.nlm.nih.gov/gene/6045):

> Polycomb group (PcG) of proteins form the multiprotein complexes that are important for the transcription repression of various genes involved in development and cell proliferation. The protein encoded by this gene is one of the PcG proteins. It has been shown to interact with, and suppress the activity of, transcription factor CP2 (TFCP2/CP2). Studies of the mouse counterpart suggested the involvement of this gene in the specification of anterior-posterior axis, as well as in cell …

**Accessions** — [HGNC:10061](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10061) · Entrez [6045](https://www.ncbi.nlm.nih.gov/gene/6045) · UniProt [Q99496](https://www.uniprot.org/uniprotkb/Q99496) · Ensembl [ENSG00000121481](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121481)

## Data

Gene col 4277: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4277); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4277, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4277]; `tensor/DDL_lfc|DDL_z.npy` [4277]; `embed/gene_vectors.npy` [4277]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4277 or target_col == 4277). Every well: [[RNF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

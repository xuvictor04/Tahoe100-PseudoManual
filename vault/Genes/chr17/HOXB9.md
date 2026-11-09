---
symbol: "HOXB9"
type: "gene"
col: 9996
ensembl_id: "ENSG00000170689"
name: "homeobox B9"
location: "17q21.32"
module: 133
arm: "+"
pooled_cpm: 22.56
n_lines_expressing: 33
n_dd_up: 28
n_dd_down: 14
n_dd_up_clean: 20
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 5
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# HOXB9

*homeobox B9* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.96× (z +10.8, q 3e-24, up in 22 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.424× (z -13.8, q 2e-40, down in 28 of 31 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCK2]] (+0.68, fdr 7e-06), [[YARS1]] (+0.67, fdr 7e-06), [[CEBPG]] (+0.65, fdr 7e-06); moves opposite to [[POMP]] (-0.46, fdr 1e-04), [[RTTN]] (-0.43, fdr 2e-04), [[DCTN4]] (-0.43, fdr 7e-05).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 5 go from it, the strongest it → [[ZBED3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9996.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.96×** | +10.8 | 3e-24 | 22/31 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.94×** | +10.6 | 9e-24 | 23/31 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.86×** | +9.9 | 7e-21 | 19/28 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +9.2 | 4e-18 | 15/30 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +7.7 | 1e-12 | 14/26 (PANC-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +7.3 | 3e-11 | 17/31 (Panc 03.27, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.35×** | +6.8 | 1e-09 | 15/31 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.49×** | +6.3 | 2e-08 | 17/31 (BT-474, NCI-H460, …) | top dose only | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **2.08×** | +6.1 | 6e-08 | 19/30 (A498, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +5.9 | 2e-07 | 10/22 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.45×** | +5.9 | 2e-07 | 17/31 (NCI-H460, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.28×** | +5.6 | 1e-06 | 16/31 (BT-474, SHP-77, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.89×** | +5.3 | 5e-06 | 15/31 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.39×** | +5.2 | 7e-06 | 11/31 (BT-474, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.37×** | +4.8 | 5e-05 | 10/31 (MIA PaCa-2, BT-474, …) | rises with dose | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.77×** | +4.8 | 7e-05 | 15/30 (LOX-IMVI, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +4.3 | 6e-04 | 10/31 (NCI-H460, SHP-77, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.66×** | +4.2 | 6e-04 | 10/30 (MIA PaCa-2, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.002 | 11/31 (A-172, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.005 | 12/31 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.014 | 5/31 (MIA PaCa-2, BT-474, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, none with an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9996.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.424×** | -13.8 | 2e-40 | 28/31 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.465×** | -12.3 | 3e-32 | 28/31 (HT-29, PANC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.469×** | -12.1 | 1e-31 | 26/31 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.431×** | -7.1 | 2e-10 | 18/30 (PANC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.692×** | -5.9 | 3e-07 | 19/31 (PANC-1, KATO III, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.509×** | -5.7 | 1e-06 | 17/31 (SW480, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.534×** | -5.3 | 1e-05 | 16/31 (H4, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.732×** | -5.0 | 4e-05 | 15/31 (KATO III, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.721×** | -5.0 | 4e-05 | 17/31 (HT-29, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.736×** | -4.9 | 5e-05 | 15/31 (PANC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.766×** | -4.1 | 0.003 | 12/30 (SW48, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **0.814×** | -3.3 | 0.041 | 4/31 (LOX-IMVI, SW48, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.682×** | -3.2 | 0.055 | 9/31 (HCT15, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.874× | -3.1 | 0.081 | 6/31 (HS-578T, PANC-1, …) | rises with dose | position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM |  | **0.820×** | -3.0 | 0.089 | 5/31 (A498, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9996. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 119 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.117× (z -24.1) |
| [[PANC-1 (line)]] | alt | 50.2 | 1 (1 ⚠) | 8 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.256× (z -16.9) |
| [[HCT15 (line)]] | alt | 137 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.152× (z -15.7) |
| [[SW48 (line)]] | wt | 103 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -15.8) |
| [[RKO (line)]] | wt | 32.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -21.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.140× (z -14.0) |
| [[LoVo (line)]] | wt | 36.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -16.7) |
| [[SW1417 (line)]] | alt | 86.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -18.0) |
| [[AN3 CA (line)]] | alt | 39.1 | 0 | 2 | — | [[Pemigatinib (drug)]] 0.05 µM 0.0777× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 8.32 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +11.5) | — |
| [[A-172 (line)]] | wt | 18.9 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.15× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 11.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 6.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.91× (z +9.4) | — |
| [[J82 (line)]] | alt | 9.56 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 44.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.188× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0950× (z -19.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 34.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.51× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 17.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW480 (line)]] | alt | 31.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.385× (z -9.8) |
| [[A-427 (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.27 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.16 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.25 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.33 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9996), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCK2]] | +0.68 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[YARS1]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CEBPG]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[DMGDH]] | +0.61 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ERICH2]] | +0.59 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[NIBAN1]] | +0.58 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[TARS1]] | +0.58 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[JDP2]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SLC3A2]] | +0.57 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[DLGAP1-AS2]] | +0.57 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[AARS1]] | +0.56 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[ADM2]] | +0.56 | +0.54 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POMP]] | -0.46 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[RTTN]] | -0.43 | -0.40 / -0.29 | both halves | 2e-04 |  |
| [[DCTN4]] | -0.43 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[TFPI]] | -0.43 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[SNRPD3]] | -0.43 | -0.44 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZBED3]] | B | HOXB9 activity raises ZBED3's level | lines that do not express HOXB9 (17) vs lines expressing it (33) | 1.27× lower at baseline in the lines without HOXB9 | 0.067 | ⚠ within organs, on part of the lines; also absent: LINC02086, HOXB8; maybe low, not absent |
| cells under [[Abemaciclib (drug)]] 5 µM | B | HOXB9 activity lowers the cells' numbers under Abemaciclib 5 µM (makes them more sensitive) | lines that do not express HOXB9 (17) vs lines expressing it (31) | the lines without HOXB9: 1.29× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: LINC02086, HOXB8; maybe low, not absent |
| [[SLC43A1]] | B | HOXB9 activity raises SLC43A1's level | lines that do not express HOXB9 (17) vs lines expressing it (33) | 1.56× lower at baseline in the lines without HOXB9 | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC02086, HOXB8; maybe low, not absent |
| cells under [[Elimusertib hydrochloride (drug)]] 0.5 µM | B | HOXB9 activity raises the cells' numbers under Elimusertib hydrochloride 0.5 µM (protects the cells) | lines that do not express HOXB9 (17) vs lines expressing it (31) | the lines without HOXB9: 0.83× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: LINC02086, HOXB8; maybe low, not absent |
| [[SLC3A2]] | B | HOXB9 activity raises SLC3A2's level | lines that do not express HOXB9 (17) vs lines expressing it (33) | 1.35× lower at baseline in the lines without HOXB9 | 0.099 | ⚠ within organs, on part of the lines; also absent: LINC02086, HOXB8; maybe low, not absent |

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.8, 47.6); signed map (-12.7, 23.0). **Vector** length 90.8, 22.8% of its response variance represented; |z| ≥ 3 in 818 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.0 | +10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +10.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.9 | +4.5 |
|  | [[Artesunate (drug)]] 5 µM |  | +3.5 | +5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +4.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.3 | +4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.3 | +5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +6.8 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -7.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.4 | -4.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.3 | -13.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -12.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -5.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -4.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.0 | -2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | homeobox B9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:48,621,156-48,626,358 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX2E, HOX2 |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Hallmark sets | HYPOXIA |
| Matched by | ensembl_id |

**Function**, from UniProt [P17482](https://www.uniprot.org/uniprotkb/P17482) (Homeobox protein Hox-B9):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3219](https://www.ncbi.nlm.nih.gov/gene/3219):

> This gene is a member of the Abd-B homeobox family and encodes a protein with a homeobox DNA-binding domain. It is included in a cluster of homeobox B genes located on chromosome 17. The encoded nuclear protein functions as a sequence-specific transcription factor that is involved in cell proliferation and differentiation. Increased expression of this gene is associated with some cases of leukemia, prostate cancer and lung cancer. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5120](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5120) · Entrez [3219](https://www.ncbi.nlm.nih.gov/gene/3219) · UniProt [P17482](https://www.uniprot.org/uniprotkb/P17482) · Ensembl [ENSG00000170689](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170689)

## Data

Gene col 9996: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9996); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9996, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9996]; `tensor/DDL_lfc|DDL_z.npy` [9996]; `embed/gene_vectors.npy` [9996]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9996 or target_col == 9996). Every well: [[HOXB9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXB9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

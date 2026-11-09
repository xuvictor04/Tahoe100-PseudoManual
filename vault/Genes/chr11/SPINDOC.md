---
symbol: "SPINDOC"
type: "gene"
col: 9579
ensembl_id: "ENSG00000168005"
name: "spindlin interactor and repressor of chromatin binding"
location: "11q13.1"
module: 72
arm: "+"
pooled_cpm: 12.0
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# SPINDOC

*spindlin interactor and repressor of chromatin binding* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.96× (z +20.3, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.786× (z -4.4, q 0.007, down in 16 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MBOAT7]] (+0.67, fdr 1e-05), [[AHSA1]] (+0.66, fdr 1e-05), [[KLHL25]] (+0.66, fdr 1e-05); moves opposite to [[TMEM265]] (-0.57, fdr 2e-05), [[ZC3H6]] (-0.54, fdr 1e-05), [[CEP63]] (-0.54, fdr 1e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[WNK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9579.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.96×** | +20.3 | 0e+00 | 43/47 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +18.4 | 0e+00 | 36/45 (A549, LoVo, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.02×** | +13.2 | 2e-37 | 36/47 (LoVo, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.00×** | +12.9 | 5e-36 | 32/47 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.95×** | +12.5 | 1e-33 | 33/47 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.83×** | +10.7 | 8e-25 | 32/46 (AsPC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.75×** | +10.4 | 1e-23 | 30/47 (HEC-1-A, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.55×** | +8.2 | 3e-14 | 27/47 (A498, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.54×** | +7.7 | 6e-13 | 10/21 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +7.5 | 4e-12 | 23/46 (A-172, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.95×** | +6.6 | 3e-09 | 20/35 (Panc 03.27, J82, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +6.2 | 3e-08 | 19/47 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +6.1 | 6e-08 | 18/47 (NCI-H460, A-427, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +6.0 | 9e-08 | 15/47 (A-427, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.56×** | +5.9 | 1e-07 | 20/47 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.0 | 1e-05 | 12/48 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.64×** | +4.8 | 4e-05 | 5/45 (J82, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.13× | +3.3 | 0.022 | 4/48 (LS 180, HEC-1-A, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.036 | 7/43 (BT-474, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pentoxifylline (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.061 | 3/47 (PANC-1, SW1417, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9579.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.786×** | -4.4 | 0.007 | 16/45 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.860× | -4.0 | 0.015 | 8/48 (BT-474, SW480, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.819×** | -3.6 | 0.053 | 15/45 (RPMI-7951, SW48, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.830×** | -3.5 | 0.055 | 11/47 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.831×** | -3.5 | 0.055 | 10/47 (SK-MEL-2, SW 1271, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.838× | -3.3 | 0.070 | 14/45 (A-427, A-172, …) | inconsistent across doses |  |
| [[AZD-7648 (drug)]] 5 µM |  | **0.713×** | -3.3 | 0.070 | 11/41 (SW48, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.959× | -3.1 | 0.14 | 2/48 (CHP-212, SW48) | inconsistent across doses |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | 0.800× | -3.0 | 0.15 | 7/46 (SHP-77, SW480, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9579. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 21.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -12.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HEC-1-A (line)]] | alt | 11.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 6.12× (z +11.5) | — |
| [[SW480 (line)]] | alt | 17.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.91× (z +12.0) | — |
| [[A549 (line)]] | wt | 8.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.73× (z +12.7) | — |
| [[HOP62 (line)]] | alt | 12.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.18× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 12.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.66× (z +8.5) | — |
| [[LoVo (line)]] | wt | 8.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 4.57 | 0 | 1 | — | [[Mifepristone (drug)]] 0.05 µM 0.0812× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 13.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.54× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 8.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 5.53 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0936× (z -8.6) |
| [[SNU-423 (line)]] | alt | 11.0 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.177× (z -8.6) |
| [[SW 900 (line)]] | alt | 10.0 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0931× (z -10.1) |
| [[SW48 (line)]] | wt | 11.2 | 0 | 1 | — | [[Lactate (calcium) (drug)]] 0.5 µM 0.0689× (z -9.5) |
| [[A-172 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9579), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBOAT7]] | +0.67 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[AHSA1]] | +0.66 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[KLHL25]] | +0.66 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[UFD1]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[CTDP1]] | +0.62 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[NECAB3]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ZNF731P]] | +0.59 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[TESK1]] | +0.58 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[CHRNA5]] | +0.58 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CACYBP]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SERPINH1]] | +0.57 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[TRRAP]] | +0.56 | +0.59 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM265]] | -0.57 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ZC3H6]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[CEP63]] | -0.54 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[TMEM42]] | -0.54 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[HHLA3]] | -0.54 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[LINC01473]] | -0.54 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[NFKBIA]] | -0.53 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[PPP4R2]] | -0.53 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[CLK4]] | -0.53 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[DOP1A]] | -0.53 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[NDUFA5]] | -0.52 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[MIER1]] | -0.52 | -0.37 / -0.51 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNK2]] | B | WNK2 activity raises SPINDOC's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.52× lower at baseline in the lines without WNK2 | 0.022 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[TOP2A]] | B | TOP2A activity lowers SPINDOC's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.559). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.5, -7.1); signed map (-27.9, -30.8). **Vector** length 74.0, 12.4% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.0 | +20.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.0 | +12.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.5 | +10.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.3 | +6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +18.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +8.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.6 | +5.9 |
|  | [[Infigratinib (drug)]] 5 µM |  | +1.5 | +4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.3 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.7 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.5 | -4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.4 | -0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -1.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -1.3 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.0 | -0.8 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | spindlin interactor and repressor of chromatin binding |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:63,813,456-63,827,716 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPIN-DOC; previously C11orf84 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUA3](https://www.uniprot.org/uniprotkb/Q9BUA3) (Spindlin interactor and repressor of chromatin-binding protein):

> Chromatin protein that stabilizes SPIN1 and enhances its association with histone H3 trimethylated at both 'Lys-4' and 'Lys-9' (H3K4me3K9me3). Positively regulates poly-ADP-ribosylation in response to DNA damage; acts by facilitating PARP1 ADP-ribosyltransferase activity.

**Summary**, from NCBI Gene [144097](https://www.ncbi.nlm.nih.gov/gene/144097):

> Involved in DNA damage response and negative regulation of DNA-templated transcription. Is active in nucleus and site of DNA damage. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25115](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25115) · Entrez [144097](https://www.ncbi.nlm.nih.gov/gene/144097) · UniProt [Q9BUA3](https://www.uniprot.org/uniprotkb/Q9BUA3) · Ensembl [ENSG00000168005](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168005)

## Data

Gene col 9579: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9579); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9579, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9579]; `tensor/DDL_lfc|DDL_z.npy` [9579]; `embed/gene_vectors.npy` [9579]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9579 or target_col == 9579). Every well: [[SPINDOC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPINDOC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

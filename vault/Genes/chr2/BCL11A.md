---
symbol: "BCL11A"
type: "gene"
col: 4128
ensembl_id: "ENSG00000119866"
name: "BCL11 transcription factor A"
location: "2p16.1"
module: 9
arm: "+"
pooled_cpm: 18.96
n_lines_expressing: 30
n_dd_up: 12
n_dd_down: 49
n_dd_up_clean: 12
n_dd_down_clean: 41
in_vector_space: true
direction_upstream: 12
direction_downstream: 1
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# BCL11A

*BCL11 transcription factor A* — 2p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.00× (z +14.4, q 2e-44, up in 20 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 49 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.401× (z -18.9, q 0e+00, down in 26 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGAT4C]] (+0.59, fdr 2e-05), [[SFMBT2]] (+0.58, fdr 1e-05), [[RBM20]] (+0.58, fdr 2e-05); moves opposite to [[CC2D1B]] (-0.50, fdr 3e-05), [[ERVK13-1]] (-0.48, fdr 9e-05), [[RABL2B]] (-0.44, fdr 9e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[ADAM22]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RNASEH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4128.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.00×** | +14.4 | 2e-44 | 20/28 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.30×** | +12.3 | 4e-32 | 22/28 (NCI-H460, C-33 A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.09×** | +10.8 | 5e-25 | 20/28 (NCI-H460, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.72×** | +8.0 | 1e-13 | 19/27 (NCI-H460, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.69×** | +7.6 | 3e-12 | 15/28 (NCI-H1792, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.60×** | +6.9 | 5e-10 | 20/28 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +5.8 | 5e-07 | 12/28 (NCI-H2030, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.48×** | +5.8 | 6e-07 | 13/28 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.46×** | +5.4 | 5e-06 | 12/28 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.53×** | +4.5 | 5e-04 | 5/28 (NCI-H460, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.077 | 7/28 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.079 | 7/26 (A549, NCI-H1792, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.081 | 7/28 (SW480, SHP-77, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.081 | 6/28 (SW480, CFPAC-1, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.081 | 7/28 (NCI-H23, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 49 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4128.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.401×** | -18.9 | 0e+00 | 26/28 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.373×** | -14.4 | 8e-45 | 24/28 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.411×** | -13.0 | 2e-36 | 24/28 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.426×** | -12.5 | 1e-33 | 25/28 (LOX-IMVI, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.433×** | -12.2 | 3e-32 | 22/27 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.456×** | -11.5 | 2e-28 | 22/28 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.457×** | -11.4 | 2e-28 | 23/28 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.463×** | -11.3 | 2e-27 | 23/27 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.463×** | -11.2 | 2e-27 | 23/28 (LOX-IMVI, SW48, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.512×** | -9.4 | 3e-19 | 22/28 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.658×** | -8.6 | 3e-16 | 20/28 (A-427, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.549×** | -8.1 | 3e-14 | 15/19 (A-427, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.585×** | -7.4 | 6e-12 | 18/27 (SW48, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.649×** | -6.2 | 3e-08 | 17/28 (H4, LS 180, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.657×** | -6.1 | 3e-08 | 18/27 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.449×** | -6.1 | 3e-08 | 19/27 (NCI-H1792, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.747×** | -6.0 | 7e-08 | 15/28 (CHP-212, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.459×** | -6.0 | 8e-08 | 19/27 (SW48, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.659×** | -5.9 | 1e-07 | 13/28 (NCI-H23, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4128. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 80.4 | 0 | 16 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.231× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.279× (z -13.7) |
| [[NCI-H460 (line)]] | wt | 25.8 | 0 | 13 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.132× (z -17.7) |
| [[NCI-H1573 (line)]] | alt | 43.2 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -20.8) |
| [[NCI-H2030 (line)]] | alt | 24.3 | 3 (1 ⚠) | 9 (4 ⚠) | [[Belinostat (drug)]] 5 µM 3.85× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -19.1) |
| [[SW480 (line)]] | alt | 39.4 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -15.3) |
| [[NCI-H1792 (line)]] | alt | 93.0 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.220× (z -13.4) |
| [[SW48 (line)]] | wt | 35.1 | 0 | 7 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0723× (z -13.0) |
| [[A-427 (line)]] | wt | 66.7 | 0 | 5 (4 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.196× (z -22.1) |
| [[COLO 205 (line)]] | alt | 16.6 | 0 | 5 | — | [[Harringtonine (drug)]] 5 µM 0.0913× (z -10.4) |
| [[HCT15 (line)]] | alt | 48.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -11.3) |
| [[LoVo (line)]] | wt | 47.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 62.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -23.4) |
| [[SHP-77 (line)]] | alt | 79.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -12.3) |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 2 | — | [[Auranofin (drug)]] 0.05 µM 0.0516× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 11.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -9.9) |
| [[H4 (line)]] | wt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0861× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 7.52 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0767× (z -10.3) ⚠ toxic |
| [[SW 900 (line)]] | alt | 10.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.106× (z -9.6) |
| [[A-172 (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.16 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4128), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGAT4C]] | +0.59 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[SFMBT2]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[RBM20]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ERBB4]] | +0.57 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[SLITRK6]] | +0.55 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[SLITRK5]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[POU3F2]] | +0.54 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[NELL2]] | +0.54 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[ST8SIA4]] | +0.52 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[PTCH1]] | +0.51 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[FAM117B]] | +0.50 | +0.36 / +0.53 | both halves | 9e-05 |  |
| [[GATA4]] | +0.50 | +0.48 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CC2D1B]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[ERVK13-1]] | -0.48 | -0.50 / -0.37 | both halves | 9e-05 |  |
| [[RABL2B]] | -0.44 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[RNF14]] | -0.42 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[IKBKG]] | -0.42 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[RNASEH1]] | -0.42 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[AVEN]] | -0.41 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[DESI1]] | -0.40 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[ERMAP]] | -0.40 | -0.41 / -0.26 | both halves | 4e-04 |  |
| [[EXOC7]] | -0.40 | -0.29 / -0.41 | both halves | 2e-04 |  |
| [[SZT2]] | -0.40 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[CEP170B]] | -0.40 | -0.40 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM22]] | B | ADAM22 activity raises BCL11A's level | lines that do not express ADAM22 (12) vs lines expressing it (38) | 2.84× lower at baseline in the lines without ADAM22 | 0.028 | ⚠ within organs, on part of the lines; also absent: ASGR1; maybe low, not absent |
| [[PRKAR2B]] | B | PRKAR2B activity raises BCL11A's level | lines that do not express PRKAR2B (12) vs lines expressing it (38) | 2.09× lower at baseline in the lines without PRKAR2B | 0.040 | ⚠ within organs, on part of the lines; also absent: EML1, GALNT16, KATNAL2 |
| [[POU3F3]] | B | POU3F3 activity raises BCL11A's level | lines that do not express POU3F3 (34) vs lines expressing it (16) | 2.25× lower at baseline in the lines without POU3F3 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PANTR1, EPGN, ENSG00000244468 |
| [[EPHA3]] | B | EPHA3 activity raises BCL11A's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 2.20× lower at baseline in the lines without EPHA3 | 0.061 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491 |
| [[MIR2052HG]] | B | MIR2052HG activity raises BCL11A's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 2.14× lower at baseline in the lines without MIR2052HG | 0.062 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent |
| [[NETO1]] | B | NETO1 activity raises BCL11A's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 4.71× lower at baseline in the lines without NETO1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4 |
| [[BCHE]] | B | BCHE activity raises BCL11A's level | lines that do not express BCHE (35) vs lines expressing it (15) | 2.38× lower at baseline in the lines without BCHE | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2 |
| [[TOP2A]] | B | TOP2A activity raises BCL11A's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDH12]] | B | CDH12 activity raises BCL11A's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 2.74× lower at baseline in the lines without CDH12 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers BCL11A's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers BCL11A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FAM133A]] | B | FAM133A activity raises BCL11A's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 1.76× lower at baseline in the lines without FAM133A | 0.097 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNASEH1]] | B | BCL11A activity lowers RNASEH1's level | lines that do not express BCL11A (20) vs lines expressing it (30) | 1.15× higher at baseline in the lines without BCL11A | 0.094 | ⚠ within organs, on part of the lines; also absent: VWDE, HEYL, HS6ST2 |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.474). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.9, 35.7); signed map (39.9, 38.3). **Vector** length 80.5, 19.1% of its response variance represented; |z| ≥ 3 in 974 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +14.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +12.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | +3.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.6 | +10.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.6 | +8.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | -1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -12.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.3 | -4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | BCL11 transcription factor A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.1 — chr2:60,450,520-60,554,467 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BCL11A-XL, BCL11A-L, BCL11A-S, CTIP1, HBFQTL5, ZNF856, SMARCM1; previously EVI9 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BAF complex subunits |
| Reactome | 9 pathways, smallest: ALK mutants bind TKIs; Formation of the embryonic stem cell BAF (esBAF) complex; Formation of neuronal progenitor and neuronal BAF (npBAF and nBAF) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H165](https://www.uniprot.org/uniprotkb/Q9H165) (BCL11 transcription factor A):

> Transcription factor. Associated with the BAF SWI/SNF chromatin remodeling complex. Binds to the 5'-TGACCA-3' sequence motif in regulatory regions of target genes, including a distal promoter of the HBG1 hemoglobin subunit gamma-1 gene. Involved in regulation of the developmental switch from gamma- to beta-globin, probably via direct repression of HBG1; hence indirectly repressing fetal hemoglobin (HbF) level. Involved in brain development. May play a role in hematopoiesis (By similarity). …

**Summary**, from NCBI Gene [53335](https://www.ncbi.nlm.nih.gov/gene/53335):

> This gene encodes a C2H2 type zinc-finger protein by its similarity to the mouse Bcl11a/Evi9 protein. The corresponding mouse gene is a common site of retroviral integration in myeloid leukemia, and may function as a leukemia disease gene, in part, through its interaction with BCL6. During hematopoietic cell differentiation, this gene is down-regulated. It is possibly involved in lymphoma pathogenesis since translocations associated with B-cell malignancies also deregulates its expression. …

**Accessions** — [HGNC:13221](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13221) · Entrez [53335](https://www.ncbi.nlm.nih.gov/gene/53335) · UniProt [Q9H165](https://www.uniprot.org/uniprotkb/Q9H165) · Ensembl [ENSG00000119866](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119866)

## Data

Gene col 4128: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4128); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4128, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4128]; `tensor/DDL_lfc|DDL_z.npy` [4128]; `embed/gene_vectors.npy` [4128]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4128 or target_col == 4128). Every well: [[BCL11A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL11A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

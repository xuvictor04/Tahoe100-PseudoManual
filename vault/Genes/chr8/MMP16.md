---
symbol: "MMP16"
type: "gene"
col: 7947
ensembl_id: "ENSG00000156103"
name: "matrix metallopeptidase 16"
location: "8q21.3"
module: 9
arm: "+"
pooled_cpm: 39.75
n_lines_expressing: 27
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 16
direction_downstream: 5
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# MMP16

*matrix metallopeptidase 16* — 8q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.91× (z +13.9, q 7e-41, up in 24 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 0.5 µM: 0.697× (z -5.5, q 2e-05, down in 9 of 24 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.784× (z -5.3, q 4e-05, down in 14 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMPRSS15]] (+0.62, fdr 1e-05), [[ADAMTS1]] (+0.61, fdr 1e-05), [[ST6GALNAC3]] (+0.61, fdr 1e-05); moves opposite to [[MMUT]] (-0.50, fdr 1e-05), [[HERPUD2]] (-0.50, fdr 4e-05), [[ARHGAP1]] (-0.47, fdr 4e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[XKR6]] → it (grade B ⚠); 5 go from it, the strongest it → [[CARD18]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7947.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.91×** | +13.9 | 7e-41 | 24/25 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +10.1 | 1e-21 | 8/22 (HEC-1-A, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.91×** | +9.9 | 1e-20 | 20/25 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +9.4 | 1e-18 | 19/24 (HOP62, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +8.1 | 9e-14 | 9/23 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +7.2 | 6e-11 | 19/24 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +7.1 | 1e-10 | 19/24 (NCI-H460, HOP62, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.26×** | +6.5 | 7e-09 | 16/22 (RPMI-7951, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +6.0 | 1e-07 | 17/25 (HOP62, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.92×** | +5.2 | 1e-05 | 18/25 (NCI-H460, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.41×** | +5.2 | 1e-05 | 14/24 (NCI-H460, NCI-H23, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +4.3 | 9e-04 | 12/24 (HOP62, PANC-1, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.2 | 0.001 | 17/24 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.32×** | +3.8 | 0.005 | 5/22 (A-172, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.26×** | +3.5 | 0.017 | 11/24 (HOP62, J82, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.55×** | +3.5 | 0.018 | 11/24 (HS-578T, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.048 | 3/25 (HS-578T, SHP-77, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.073 | 10/24 (SW 900, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +2.9 | 0.081 | 7/24 (AN3 CA, SHP-77, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.081 | 3/24 (HOP62, SNU-423, …) | top dose only |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.23×** | +2.9 | 0.084 | 6/24 (CHP-212, LOX-IMVI, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7947.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.697×** | -5.5 | 2e-05 | 9/24 (SK-MEL-2, PANC-1, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.784×** | -5.3 | 4e-05 | 14/25 (PANC-1, CHP-212, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.783×** | -3.6 | 0.040 | 9/24 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.791×** | -3.6 | 0.040 | 8/24 (SK-MEL-2, PANC-1, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.784×** | -3.6 | 0.040 | 12/24 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.766×** | -3.5 | 0.048 | 8/25 (A-427, AN3 CA, …) | two highest doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.804×** | -3.3 | 0.070 | 10/24 (SK-MEL-2, NCI-H1792, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.670×** | -3.2 | 0.097 | 8/24 (RPMI-7951, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.813×** | -3.2 | 0.097 | 12/24 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.815× | -3.1 | 0.10 | 0/25 | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.869× | -3.0 | 0.12 | 9/25 (H4, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7947. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 144 | 0 | 9 (8 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -17.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.505× (z -9.3) |
| [[AN3 CA (line)]] | alt | 293 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0401× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HOP62 (line)]] | alt | 28.7 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.08× (z +12.4) | — |
| [[NCI-H23 (line)]] | alt | 14.4 | 2 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.09× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.182× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 78.5 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.42× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 56.5 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.58× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 58.3 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.358× (z -9.3) ⚠ cell-cycle shift, explains ~83% of this change |
| [[SHP-77 (line)]] | alt | 92.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -12.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 92.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.33× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -10.3) ⚠ cell-cycle shift, explains ~62% of this change |
| [[A-172 (line)]] | wt | 29.8 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.95× (z +9.1) | — |
| [[C32 (line)]] | wt | 351 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -14.4) ⚠ cell-cycle shift, explains ~62% of this change |
| [[CHP-212 (line)]] | wt | 194 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0567× (z -20.1) ⚠ cell-cycle shift, explains ~62% of this change |
| [[NCI-H2347 (line)]] | alt | 12.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 7.13× (z +13.8) | — |
| [[NCI-H460 (line)]] | wt | 75.3 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.17× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 11.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.07× (z +11.1) | — |
| [[hTERT-HPNE (line)]] | wt | 45.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LOX-IMVI (line)]] | wt | 238 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -16.1) ⚠ cell-cycle shift, explains ~62% of this change |
| [[RPMI-7951 (line)]] | alt | 65.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.43× (z +8.6) | — |
| [[SW 1271 (line)]] | alt | 64.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0653× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -10.9) ⚠ cell-cycle shift, explains ~62% of this change |
| [[A498 (line)]] | wt | 3.08 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.74 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 73.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.06 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.20 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.65 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.83 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.91 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.11 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7947), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMPRSS15]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ADAMTS1]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 | pathway: Degradation of the extracellular matrix |
| [[ST6GALNAC3]] | +0.61 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[PDGFD]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[HMCN1]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[FMN2]] | +0.60 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ATRNL1]] | +0.60 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[ANGPT1]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[NCAM2]] | +0.60 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[EDNRB]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[DZIP1]] | +0.58 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[SOX5]] | +0.58 | +0.59 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMUT]] | -0.50 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[HERPUD2]] | -0.50 | -0.43 / -0.54 | both halves | 4e-05 |  |
| [[ARHGAP1]] | -0.47 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[SIRT3]] | -0.46 | -0.37 / -0.42 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 2, C 14. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XKR6]] | B | XKR6 activity raises MMP16's level | lines that do not express XKR6 (18) vs lines expressing it (32) | 2.14× lower at baseline in the lines without XKR6 | 0.096 | ⚠ within organs, on part of the lines; also absent: CIART, RNF182, LINC00702 |
| [[CARD18]] | B | CARD18 activity raises MMP16's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 2.41× lower at baseline in the lines without CARD18 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10 |
| [[KCNQ5]] | C | KCNQ5 activity raises MMP16's level | lines that do not express KCNQ5 (25) vs lines expressing it (25) | 7.71× lower at baseline in the lines without KCNQ5 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000253553, PRR16, FAP; co-absent with the target |
| [[NEGR1]] | C | NEGR1 activity raises MMP16's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 5.67× lower at baseline in the lines without NEGR1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[DZIP1]] | C | DZIP1 activity raises MMP16's level | lines that do not express DZIP1 (23) vs lines expressing it (27) | 5.58× lower at baseline in the lines without DZIP1 | 0.014 | ⚠ within organs, on part of the lines; also absent: BVES, LAYN, GLIS1; co-absent with the target |
| [[ANGPT1]] | C | ANGPT1 activity raises MMP16's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 4.59× lower at baseline in the lines without ANGPT1 | 0.039 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5; co-absent with the target |
| [[B3GALT1]] | C | B3GALT1 activity raises MMP16's level | lines that do not express B3GALT1 (20) vs lines expressing it (30) | 5.73× lower at baseline in the lines without B3GALT1 | 0.042 | ⚠ within organs, on part of the lines; also absent: ANTXR1, LINC00882, LINC01695; maybe low, not absent; co-absent with the target |
| [[NCAM2]] | C | NCAM2 activity raises MMP16's level | lines that do not express NCAM2 (24) vs lines expressing it (26) | 6.21× lower at baseline in the lines without NCAM2 | 0.045 | ⚠ within organs, on part of the lines; also absent: MMP16, ADGRB3, FAP; co-absent with the target |
| [[ST6GALNAC3]] | C | ST6GALNAC3 activity raises MMP16's level | lines that do not express ST6GALNAC3 (18) vs lines expressing it (32) | 4.63× lower at baseline in the lines without ST6GALNAC3 | 0.046 | ⚠ within organs, on part of the lines; also absent: TRIM9, GHR, OSBPL6; maybe low, not absent; co-absent with the target |
| [[PCDH18]] | C | PCDH18 activity raises MMP16's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 4.73× lower at baseline in the lines without PCDH18 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677; co-absent with the target |
| [[EPHA5]] | C | EPHA5 activity raises MMP16's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 4.90× lower at baseline in the lines without EPHA5 | 0.052 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[ATRNL1]] | C | ATRNL1 activity raises MMP16's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 4.20× lower at baseline in the lines without ATRNL1 | 0.052 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD18]] | B | MMP16 activity raises CARD18's level | lines that do not express MMP16 (23) vs lines expressing it (27) | 1.49× lower at baseline in the lines without MMP16 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000253553, NCAM2, KCNQ5 |
| [[KCNQ5]] | C | MMP16 activity raises KCNQ5's level | lines that do not express MMP16 (23) vs lines expressing it (27) | 7.15× lower at baseline in the lines without MMP16 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000253553, NCAM2, KCNQ5; co-absent with the target |
| [[B3GALT1]] | C | MMP16 activity raises B3GALT1's level | lines that do not express MMP16 (23) vs lines expressing it (27) | 2.95× lower at baseline in the lines without MMP16 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000253553, NCAM2, KCNQ5; co-absent with the target |
| [[DZIP1]] | C | MMP16 activity raises DZIP1's level | lines that do not express MMP16 (23) vs lines expressing it (27) | 4.84× lower at baseline in the lines without MMP16 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000253553, NCAM2, KCNQ5; co-absent with the target |
| [[EGFEM1P]] | C | MMP16 activity raises EGFEM1P's level | lines that do not express MMP16 (23) vs lines expressing it (27) | 3.83× lower at baseline in the lines without MMP16 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000253553, NCAM2, KCNQ5; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.644). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.2, 29.9); signed map (37.1, 32.9). **Vector** length 91.7, 28.9% of its response variance represented; |z| ≥ 3 in 715 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +8.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +10.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +5.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +3.5 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -2.6 | -3.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -0.3 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | matrix metallopeptidase 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.3 — chr8:88,032,011-88,328,025 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MT3-MMP, DKFZp761D112; previously C8orf57 |
| Gene groups (HGNC) | M10 matrix metallopeptidases |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 6 pathways, smallest: TGFBR3 PTM regulation; Activation of Matrix Metalloproteinases; Signaling by TGFBR3 |
| Matched by | ensembl_id |

**Function**, from UniProt [P51512](https://www.uniprot.org/uniprotkb/P51512) (Matrix metalloproteinase-16):

> Endopeptidase that degrades various components of the extracellular matrix, such as collagen type III and fibronectin. Activates progelatinase A. Involved in the matrix remodeling of blood vessels. Isoform short cleaves fibronectin and also collagen type III, but at lower rate. It has no effect on type I, II, IV and V collagen. However, upon interaction with CSPG4, it may be involved in degradation and invasion of type I collagen by melanoma cells.

**Summary**, from NCBI Gene [4325](https://www.ncbi.nlm.nih.gov/gene/4325):

> Proteins of the matrix metalloproteinase (MMP) family are involved in the breakdown of extracellular matrix in normal physiological processes, such as embryonic development, reproduction, and tissue remodeling, as well as in disease processes, such as arthritis and metastasis. Most MMP's are secreted as inactive proproteins which are activated when cleaved by extracellular proteinases. The encoded protein activates MMP2 by cleavage. This gene was once referred to as MT-MMP2, but was renamed as …

**Accessions** — [HGNC:7162](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7162) · Entrez [4325](https://www.ncbi.nlm.nih.gov/gene/4325) · UniProt [P51512](https://www.uniprot.org/uniprotkb/P51512) · Ensembl [ENSG00000156103](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156103)

## Data

Gene col 7947: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7947); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7947, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7947]; `tensor/DDL_lfc|DDL_z.npy` [7947]; `embed/gene_vectors.npy` [7947]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7947 or target_col == 7947). Every well: [[MMP16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMP16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

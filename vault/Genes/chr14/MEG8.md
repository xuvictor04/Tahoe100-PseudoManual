---
symbol: "MEG8"
type: "gene"
col: 13481
ensembl_id: "ENSG00000225746"
name: "maternally expressed 8, small nucleolar RNA host gene"
location: "14q32.31"
module: 13
arm: "+"
pooled_cpm: 40.76
n_lines_expressing: 18
n_dd_up: 21
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 19
direction_downstream: 7
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# MEG8

*maternally expressed 8, small nucleolar RNA host gene* — 14q32.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.12× (z +16.8, q 0e+00, up in 5 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.09× (z +12.3, q 1e-32, up in 5 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 0.661× (z -4.7, q 0.002, down in 5 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MEG3]] (+0.91, fdr 7e-06, ⚠ same locus), [[MIR493HG]] (+0.81, fdr 7e-06, ⚠ same locus), [[LINC01060]] (+0.65, fdr 1e-05), [[AGPAT4]] (+0.64, fdr 1e-05), [[PLEKHG4B]] (+0.64, fdr 1e-05); moves opposite to [[ARMC8]] (-0.49, fdr 2e-05), [[SRGN]] (-0.49, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[EPHB1]] → it (grade B ⚠); 7 go from it, the strongest it → [[SHANK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13481.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.12×** | +16.8 | 0e+00 | 5/17 (SHP-77, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.28×** | +13.1 | 2e-36 | 2/12 (NCI-H1573, CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +12.3 | 1e-32 | 5/15 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.08×** | +12.3 | 1e-32 | 13/16 (HOP62, SNU-423, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +11.9 | 1e-30 | 2/15 (CFPAC-1, NCI-H1573) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.64×** | +11.1 | 1e-26 | 2/11 (NCI-H23, PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +8.4 | 5e-15 | 4/15 (NCI-H1573, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +5.6 | 1e-06 | 8/16 (HOP62, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +5.5 | 2e-06 | 8/16 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +5.2 | 1e-05 | 9/16 (SNU-423, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +4.9 | 4e-05 | 8/16 (HOP62, SNU-423, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.20×** | +4.9 | 5e-05 | 4/13 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.5 | 2e-04 | 1/18 (CFPAC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +4.2 | 0.001 | 3/16 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.002 | 7/15 (CHP-212, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.013 | 2/16 (NCI-H1573, NCI-H661) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.015 | 2/15 (CFPAC-1, SHP-77) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.50×** | +3.4 | 0.017 | 1/15 (SNU-423) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.019 | 7/15 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13481.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.661×** | -4.7 | 0.002 | 5/16 (A549, HOP62, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.698×** | -4.3 | 0.004 | 3/16 (HOP62, A549, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.703×** | -4.2 | 0.004 | 4/16 (A549, SHP-77, …) | all doses, flat | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.720×** | -4.0 | 0.011 | 5/16 (HOP62, A549, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.729×** | -3.8 | 0.016 | 9/16 (A549, HOP62, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.734×** | -3.5 | 0.041 | 6/16 (A549, HOP62, …) | all doses, flat |  |
| [[Lopinavir (drug)]] 5 µM |  | 0.754× | -3.2 | 0.11 | 1/15 (CFPAC-1) | top dose only |  |
| [[Menadione (drug)]] 5 µM |  | 0.767× | -3.1 | 0.13 | 2/15 (CHP-212, AN3 CA) | top dose only | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.761× | -3.0 | 0.13 | 1/16 (HepG2/C3A) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.838× | -3.0 | 0.13 | 7/16 (A549, HOP62, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.779× | -3.0 | 0.13 | 6/15 (HS-578T, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13481. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 47.8 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0964× (z -13.8) |
| [[CFPAC-1 (line)]] | alt | 21.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.56× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 11.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.16× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 39.5 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.68× (z +12.5) | — |
| [[hTERT-HPNE (line)]] | wt | 731 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.166× (z -11.1) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 23.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +9.9) | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0779× (z -8.6) |
| [[PANC-1 (line)]] | alt | 344 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -14.6) |
| [[SNU-423 (line)]] | alt | 27.5 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 6.35× (z +12.3) | — |
| [[A549 (line)]] | wt | 112 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.263× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 59.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -11.3) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 656 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0553× (z -12.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.51 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.88 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.24 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.31 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.65 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.44 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.86 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.63 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.30 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.39 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13481), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEG3]] | +0.91 | +0.88 / +0.90 | both halves | 7e-06 | same gene group; ⚠ same locus (22.0 kb, same strand: neighbours can correlate without regulation) |
| [[MIR493HG]] | +0.81 | +0.73 / +0.83 | both halves | 7e-06 | same gene group; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[LINC01060]] | +0.65 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[AGPAT4]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[PLEKHG4B]] | +0.64 | +0.54 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[FZD8]] | +0.62 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[VSTM4]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[INHBA]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ADAMTS16]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[LINC01411]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[EVC]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[KCNMA1]] | +0.60 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[SLIT3]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[MYO10]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC8]] | -0.49 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[SRGN]] | -0.49 | -0.43 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 2, C 17. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHB1]] | B | EPHB1 activity raises MEG8's level | lines that do not express EPHB1 (16) vs lines expressing it (34) | 2.56× lower at baseline in the lines without EPHB1 | 0.028 | ⚠ within organs, on part of the lines; also absent: KCNG1, DOCK2, GLIS1; maybe low, not absent |
| [[GLIS3]] | B | GLIS3 activity raises MEG8's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 3.16× lower at baseline in the lines without GLIS3 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| [[MIR493HG]] | C | MIR493HG activity raises MEG8's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 10.43× lower at baseline in the lines without MIR493HG | 3e-04 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252; co-absent with the target |
| [[MEG3]] | C | MEG3 activity raises MEG8's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 10.13× lower at baseline in the lines without MEG3 | 8e-04 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8; co-absent with the target |
| [[GDNF]] | C | GDNF activity raises MEG8's level | lines that do not express GDNF (38) vs lines expressing it (12) | 3.88× lower at baseline in the lines without GDNF | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[SLC8A1]] | C | SLC8A1 activity raises MEG8's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 3.74× lower at baseline in the lines without SLC8A1 | 0.026 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3; co-absent with the target |
| [[CRMP1]] | C | CRMP1 activity raises MEG8's level | lines that do not express CRMP1 (19) vs lines expressing it (31) | 3.31× lower at baseline in the lines without CRMP1 | 0.032 | ⚠ within organs, on part of the lines; also absent: JAM3, NHSL2, ENSG00000286033; maybe low, not absent; co-absent with the target |
| [[HGF]] | C | HGF activity raises MEG8's level | lines that do not express HGF (38) vs lines expressing it (12) | 4.54× lower at baseline in the lines without HGF | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; co-absent with the target |
| [[SYNDIG1]] | C | SYNDIG1 activity raises MEG8's level | lines that do not express SYNDIG1 (32) vs lines expressing it (18) | 3.18× lower at baseline in the lines without SYNDIG1 | 0.036 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1; co-absent with the target |
| [[PTPRN]] | C | PTPRN activity raises MEG8's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 2.48× lower at baseline in the lines without PTPRN | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1; co-absent with the target |
| [[CARMN]] | C | CARMN activity raises MEG8's level | lines that do not express CARMN (40) vs lines expressing it (10) | 5.47× lower at baseline in the lines without CARMN | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |
| [[EVC2]] | C | EVC2 activity raises MEG8's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 4.16× lower at baseline in the lines without EVC2 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SHANK1]] | B | MEG8 activity raises SHANK1's level | lines that do not express MEG8 (32) vs lines expressing it (18) | 1.35× lower at baseline in the lines without MEG8 | 0.089 | ⚠ within organs, on part of the lines; also absent: MEG3, MIR493HG, MXRA8 |
| [[MEG3]] | C | MEG8 activity raises MEG3's level | lines that do not express MEG8 (32) vs lines expressing it (18) | 8.07× lower at baseline in the lines without MEG8 | 0.001 | ⚠ within organs, on part of the lines; also absent: MEG3, MIR493HG, MXRA8; co-absent with the target |
| [[MIR493HG]] | C | MEG8 activity raises MIR493HG's level | lines that do not express MEG8 (32) vs lines expressing it (18) | 4.53× lower at baseline in the lines without MEG8 | 0.003 | ⚠ within organs, on part of the lines; also absent: MEG3, MIR493HG, MXRA8; co-absent with the target |
| [[HGF]] | C | MEG8 activity raises HGF's level | lines that do not express MEG8 (32) vs lines expressing it (18) | 2.62× lower at baseline in the lines without MEG8 | 0.048 | ⚠ within organs, on part of the lines; also absent: MEG3, MIR493HG, MXRA8; co-absent with the target |
| [[SLC8A1]] | C | MEG8 activity raises SLC8A1's level | lines that do not express MEG8 (32) vs lines expressing it (18) | 2.77× lower at baseline in the lines without MEG8 | 0.066 | ⚠ within organs, on part of the lines; also absent: MEG3, MIR493HG, MXRA8; co-absent with the target |
| [[EVC2]] | C | MEG8 activity raises EVC2's level | lines that do not express MEG8 (32) vs lines expressing it (18) | 2.95× lower at baseline in the lines without MEG8 | 0.081 | ⚠ within organs, on part of the lines; also absent: MEG3, MIR493HG, MXRA8; co-absent with the target |
| [[GDNF]] | C | MEG8 activity raises GDNF's level | lines that do not express MEG8 (32) vs lines expressing it (18) | 2.16× lower at baseline in the lines without MEG8 | 0.091 | ⚠ within organs, on part of the lines; also absent: MEG3, MIR493HG, MXRA8; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.3, 16.0); signed map (22.6, 48.5). **Vector** length 48.2, 12.4% of its response variance represented; |z| ≥ 3 in 432 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +16.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +13.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +2.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.2 | +3.4 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -4.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.6 | -4.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | -4.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | maternally expressed 8, small nucleolar RNA host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q32.31 — chr14:100,883,057-101,038,859 (+) |
| Ensembl biotype | lncRNA |
| Also known as | NCRNA00024, Irm, Rian, Bsr, LINC00024, AL132709.8, lnc-MGC; previously SNHG23, SNHG24 |
| Gene groups (HGNC) | MicroRNA non-coding host genes; Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [79104](https://www.ncbi.nlm.nih.gov/gene/79104):

> This gene is located in a cluster of imprinted genes on chromosome 14q32.3. It encodes a a non-protein coding transcript that is preferentially expressed from the maternal allele in skeletal muscle, and appears to be coordinately regulated with other imprinted genes in this region. [provided by RefSeq, Oct 2010]

**Accessions** — [HGNC:14574](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14574) · Entrez [79104](https://www.ncbi.nlm.nih.gov/gene/79104) · Ensembl [ENSG00000225746](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225746)

## Data

Gene col 13481: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13481); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13481, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13481]; `tensor/DDL_lfc|DDL_z.npy` [13481]; `embed/gene_vectors.npy` [13481]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13481 or target_col == 13481). Every well: [[MEG8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEG8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "NPTX1"
type: "gene"
col: 10081
ensembl_id: "ENSG00000171246"
name: "neuronal pentraxin 1"
location: "17q25.3"
module: 112
arm: "+"
pooled_cpm: 9.43
n_lines_expressing: 25
n_dd_up: 18
n_dd_down: 22
n_dd_up_clean: 11
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# NPTX1

*neuronal pentraxin 1* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.66× (z +8.5, q 7e-15, up in 7 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.08× (z +7.1, q 2e-10, up in 7 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.05 µM: 0.437× (z -5.7, q 8e-06, down in 13 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTGS2]] (+0.62, fdr 1e-05), [[INHBA]] (+0.62, fdr 1e-05), [[IER3]] (+0.60, fdr 7e-06); moves opposite to [[ADGRG2]] (-0.63, fdr 1e-05), [[ARMC8]] (-0.58, fdr 1e-05), [[CLASP1]] (-0.51, fdr 2e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SLC24A3]] → it (grade B ⚠); 5 go from it, the strongest it → [[ADRA2C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10081.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.66×** | +8.5 | 7e-15 | 7/10 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.32×** | +8.2 | 6e-14 | 9/15 (A549, SW 900, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +7.1 | 2e-10 | 7/18 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.68×** | +6.2 | 6e-08 | 8/12 (A549, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.08×** | +5.0 | 6e-05 | 7/18 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.56×** | +4.3 | 0.002 | 8/18 (HOP62, NCI-H460, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +4.2 | 0.002 | 9/23 (A-427, NCI-H460, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.16×** | +3.8 | 0.011 | 1/17 (HOP62) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +3.7 | 0.011 | 6/21 (SHP-77, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.5 | 0.030 | 5/14 (J82, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **2.00×** | +3.4 | 0.034 | 3/19 (SW 900, NCI-H2030, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +3.4 | 0.034 | 3/17 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[AZD-7648 (drug)]] 5 µM |  | **2.51×** | +3.3 | 0.040 | 1/15 (hTERT-HPNE) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.62×** | +3.3 | 0.040 | 6/23 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | **1.57×** | +3.1 | 0.069 | 9/23 (hTERT-HPNE, H4, …) | top dose only |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **1.40×** | +3.1 | 0.069 | 6/23 (hTERT-HPNE, SW 900, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +3.1 | 0.074 | 3/20 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.094 | 2/23 (AN3 CA, A549) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, none with an alert; shown: the 15 strongest. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10081.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.437×** | -5.7 | 8e-06 | 13/21 (NCI-H1573, NCI-H2030, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.493×** | -4.8 | 3e-04 | 12/21 (NCI-H1573, PANC-1, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.468×** | -4.8 | 3e-04 | 11/19 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.516×** | -4.5 | 8e-04 | 13/22 (NCI-H1573, PANC-1, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.522×** | -4.4 | 1e-03 | 11/22 (NCI-H1573, PANC-1, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.530×** | -4.3 | 0.001 | 13/20 (NCI-H1573, RPMI-7951, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.537×** | -4.3 | 0.002 | 14/21 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.557×** | -4.0 | 0.004 | 13/23 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.670×** | -3.9 | 0.006 | 12/23 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.569×** | -3.9 | 0.006 | 10/21 (NCI-H1573, SW 900, …) | all doses, flat | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.672×** | -3.8 | 0.006 | 9/23 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.571×** | -3.8 | 0.006 | 13/21 (NCI-H1573, PANC-1, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.574×** | -3.8 | 0.006 | 9/23 (NCI-H1573, SW 900, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.557×** | -3.7 | 0.008 | 2/22 (NCI-H1573, CHP-212) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.685×** | -3.7 | 0.009 | 9/23 (NCI-H1573, SW 900, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10081. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 74.2 | 0 | 21 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0473× (z -14.0) |
| [[hTERT-HPNE (line)]] | wt | 220 | 0 | 3 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.106× (z -10.2) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.159× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 9.92 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +9.7) ⚠ cell-cycle shift, explains ~94% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 4.21 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +10.9) ⚠ cell-cycle shift, explains ~94% of this change | — |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0339× (z -12.1) |
| [[A-172 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.08 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10081), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTGS2]] | +0.62 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[INHBA]] | +0.62 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[IER3]] | +0.60 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[GEM]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[FGFR1]] | +0.60 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[C15orf48]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[SYNJ2]] | +0.59 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[MRPS6]] | +0.58 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[BCL11B]] | +0.58 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[FAM107B]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[FZD8]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[GATM]] | +0.57 | +0.50 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRG2]] | -0.63 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[ARMC8]] | -0.58 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[CLASP1]] | -0.51 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[MAOA]] | -0.51 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[COBLL1]] | -0.50 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[STXBP5]] | -0.50 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[MAP2]] | -0.50 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[LARP4]] | -0.50 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[ATL3]] | -0.49 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[ACSL1]] | -0.49 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[SLC15A5]] | -0.48 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[MGST1]] | -0.48 | -0.36 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC24A3]] | B | SLC24A3 activity raises NPTX1's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 1.88× lower at baseline in the lines without SLC24A3 | 0.024 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers NPTX1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[MEG3]] | C | MEG3 activity raises NPTX1's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 3.43× lower at baseline in the lines without MEG3 | 0.075 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8; co-absent with the target |
| [[MAPK4]] | C | MAPK4 activity raises NPTX1's level | lines that do not express MAPK4 (35) vs lines expressing it (15) | 2.72× lower at baseline in the lines without MAPK4 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000289418, SLC15A5, LHFPL3-AS1; co-absent with the target |
| [[SLC15A5]] | C | SLC15A5 activity raises NPTX1's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 3.80× lower at baseline in the lines without SLC15A5 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADRA2C]] | B | NPTX1 activity raises ADRA2C's level | lines that do not express NPTX1 (25) vs lines expressing it (25) | 1.46× lower at baseline in the lines without NPTX1 | 0.064 | ⚠ within organs, on part of the lines; also absent: JAM3, SNAP91, CECR2 |
| [[CD47]] | B | NPTX1 activity lowers CD47's level | lines that do not express NPTX1 (25) vs lines expressing it (25) | 1.59× higher at baseline in the lines without NPTX1 | 0.073 | ⚠ within organs, on part of the lines; also absent: JAM3, SNAP91, CECR2 |
| [[NR4A3]] | B | NPTX1 activity raises NR4A3's level | lines that do not express NPTX1 (25) vs lines expressing it (25) | 2.67× lower at baseline in the lines without NPTX1 | 0.091 | ⚠ within organs, on part of the lines; also absent: JAM3, SNAP91, CECR2 |
| [[TNFRSF11A]] | B | NPTX1 activity lowers TNFRSF11A's level | lines that do not express NPTX1 (25) vs lines expressing it (25) | 1.57× higher at baseline in the lines without NPTX1 | 0.094 | ⚠ within organs, on part of the lines; also absent: JAM3, SNAP91, CECR2 |
| [[OLFM1]] | C | NPTX1 activity raises OLFM1's level | lines that do not express NPTX1 (25) vs lines expressing it (25) | 3.01× lower at baseline in the lines without NPTX1 | 0.034 | ⚠ within organs, on part of the lines; also absent: JAM3, SNAP91, CECR2; co-absent with the target |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.2, -3.3); signed map (19.2, 50.6). **Vector** length 57.2, 13.6% of its response variance represented; |z| ≥ 3 in 612 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.54 to 11); *Interleukin-10 signaling* (reactome, mean cos +0.52 to 5); *KRAS signaling up* (hallmark, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +3.7 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +7.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +1.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.2 | +2.5 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -2.9 | -4.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.8 | -4.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.6 | -4.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.3 | -4.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.3 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | neuronal pentraxin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:80,466,834-80,477,843 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Long pentraxins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15818](https://www.uniprot.org/uniprotkb/Q15818) (Neuronal pentraxin-1):

> May be involved in mediating uptake of synaptic material during synapse remodeling or in mediating the synaptic clustering of AMPA glutamate receptors at a subset of excitatory synapses.

**Summary**, from NCBI Gene [4884](https://www.ncbi.nlm.nih.gov/gene/4884):

> NPTX1 is a member of the neuronal pentraxin gene family. Neuronal pentraxin 1 is similar to the rat NP1 gene which encodes a binding protein for the snake venom toxin taipoxin. Human NPTX1 mRNA is exclusively localized to the nervous system. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7952](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7952) · Entrez [4884](https://www.ncbi.nlm.nih.gov/gene/4884) · UniProt [Q15818](https://www.uniprot.org/uniprotkb/Q15818) · Ensembl [ENSG00000171246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171246)

## Data

Gene col 10081: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10081); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10081, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10081]; `tensor/DDL_lfc|DDL_z.npy` [10081]; `embed/gene_vectors.npy` [10081]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10081 or target_col == 10081). Every well: [[NPTX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPTX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "PRKG1-AS1"
type: "gene"
col: 14089
ensembl_id: "ENSG00000236671"
name: "PRKG1 antisense RNA 1"
location: "10q21.1"
module: 120
arm: "+"
pooled_cpm: 5.48
n_lines_expressing: 35
n_dd_up: 22
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# PRKG1-AS1

*PRKG1 antisense RNA 1* — 10q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.71× (z +13.8, q 2e-40, up in 16 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.591× (z -5.2, q 1e-04, down in 14 of 26 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DKK1]] (+0.64, fdr 7e-06, ⚠ same locus), [[MIR1915HG]] (+0.58, fdr 3e-05), [[SRGAP1]] (+0.58, fdr 3e-05), [[GREB1L]] (+0.57, fdr 1e-05); moves opposite to [[EMC2]] (-0.54, fdr 2e-05), [[TBC1D17]] (-0.52, fdr 5e-05), [[CRY2]] (-0.50, fdr 4e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[THSD4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14089.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.71×** | +13.8 | 2e-40 | 16/24 (LoVo, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.05×** | +10.5 | 3e-23 | 3/5 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.02×** | +9.7 | 6e-20 | 17/31 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +7.5 | 6e-12 | 3/16 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +6.2 | 6e-08 | 9/30 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +5.4 | 8e-06 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +4.9 | 9e-05 | 11/22 (LoVo, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.7 | 2e-04 | 3/14 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +4.3 | 1e-03 | 8/25 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +4.2 | 0.001 | 9/31 (HOP62, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Demeclocycline (drug)]] 5 µM |  | **1.36×** | +4.2 | 0.001 | 4/30 (Hs 766T, LoVo, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +4.1 | 0.002 | 8/28 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.45×** | +3.6 | 0.012 | 3/22 (SNU-423, LOX-IMVI, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.015 | 7/25 (LoVo, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.019 | 5/22 (LoVo, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.032 | 5/31 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.033 | 4/31 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.2 | 0.044 | 5/17 (LoVo, NCI-H460, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.56×** | +3.1 | 0.050 | 2/18 (NCI-H460, BT-474) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Canagliflozin (drug)]] 5 µM |  | **1.37×** | +2.9 | 0.084 | 1/22 (NCI-H2030) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14089.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.591×** | -5.2 | 1e-04 | 14/26 (LoVo, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.652×** | -4.2 | 0.007 | 15/30 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **0.754×** | -3.9 | 0.015 | 9/31 (A-172, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Fumaric acid (drug)]] 5 µM |  | **0.695×** | -3.4 | 0.074 | 1/31 (PANC-1) | top dose only | plate-row cell shift |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **0.708×** | -3.4 | 0.074 | 3/31 (NCI-H2347, HCT15, …) | inconsistent across doses |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.787×** | -3.4 | 0.074 | 8/31 (PANC-1, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14089. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 78.2 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -11.6) |
| [[LoVo (line)]] | wt | 9.39 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.16× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -9.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 9.96 | 0 | 2 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0632× (z -10.1) |
| [[A-172 (line)]] | wt | 9.93 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0753× (z -9.3) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 3.86 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -11.8) |
| [[A498 (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.671 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.758 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.991 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.586 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.802 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.549 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.000 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14089), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DKK1]] | +0.64 | +0.65 / +0.70 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[MIR1915HG]] | +0.58 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[SRGAP1]] | +0.58 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[GREB1L]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[SATB2]] | +0.56 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[LINC00707]] | +0.56 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[DAW1]] | +0.56 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[EGFR]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | +0.53 | +0.53 / +0.50 | both halves | 1e-05 | same gene group |
| [[NEMP2]] | +0.53 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[DDAH1]] | +0.53 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[CASC19]] | +0.52 | +0.49 / +0.55 | both halves | 2e-05 |  |
| [[C10orf88B]] | +0.51 | +0.51 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMC2]] | -0.54 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[TBC1D17]] | -0.52 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[CRY2]] | -0.50 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[IFT52]] | -0.49 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[USP2]] | -0.49 | -0.40 / -0.29 | both halves | 2e-04 |  |
| [[GALM]] | -0.49 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[CFAP36]] | -0.49 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[SREBF1]] | -0.48 | -0.47 / -0.37 | both halves | 7e-05 |  |
| [[YPEL2]] | -0.48 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[PLD3]] | -0.48 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[SCPEP1]] | -0.48 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[MAPK3]] | -0.48 | -0.51 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PRKG1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MIR1915HG]] | B | MIR1915HG activity raises PRKG1-AS1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.61× lower at baseline in the lines without MIR1915HG | 0.087 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[DKK1]] | C | DKK1 activity raises PRKG1-AS1's level | lines that do not express DKK1 (20) vs lines expressing it (30) | 2.55× lower at baseline in the lines without DKK1 | 0.019 | ⚠ within organs, on part of the lines; also absent: CACNG4, PALM, CRIP1; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THSD4]] | B | PRKG1-AS1 activity raises THSD4's level | lines that do not express PRKG1-AS1 (15) vs lines expressing it (35) | 3.54× lower at baseline in the lines without PRKG1-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: HERC5, RAB31, GALC |
| [[ARHGEF10L]] | B | PRKG1-AS1 activity lowers ARHGEF10L's level | lines that do not express PRKG1-AS1 (15) vs lines expressing it (35) | 2.07× higher at baseline in the lines without PRKG1-AS1 | 0.067 | ⚠ within organs, on part of the lines; also absent: HERC5, RAB31, GALC |
| [[ASIC2]] | B | PRKG1-AS1 activity lowers ASIC2's level | lines that do not express PRKG1-AS1 (15) vs lines expressing it (35) | 1.07× higher at baseline in the lines without PRKG1-AS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: HERC5, RAB31, GALC |
| [[CALCOCO2]] | B | PRKG1-AS1 activity raises CALCOCO2's level | lines that do not express PRKG1-AS1 (15) vs lines expressing it (35) | 1.15× lower at baseline in the lines without PRKG1-AS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: HERC5, RAB31, GALC |
| [[DKK1]] | C | PRKG1-AS1 activity raises DKK1's level | lines that do not express PRKG1-AS1 (15) vs lines expressing it (35) | 3.92× lower at baseline in the lines without PRKG1-AS1 | 0.046 | ⚠ within organs, on part of the lines; also absent: HERC5, RAB31, GALC; co-absent with the target |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.623). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.3, 11.4); signed map (13.6, 39.7). **Vector** length 52.4, 9.33% of its response variance represented; |z| ≥ 3 in 746 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +13.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +6.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.8 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.6 | +2.2 |
| fall | [[Artesunate (drug)]] 5 µM |  | -2.4 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.8 | -4.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -2.8 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | PRKG1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10q21.1 — chr10:52,230,398-52,314,507 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-573I11.2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:45029](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:45029) · Entrez [100506939](https://www.ncbi.nlm.nih.gov/gene/100506939) · Ensembl [ENSG00000236671](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236671)

## Data

Gene col 14089: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14089); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14089, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14089]; `tensor/DDL_lfc|DDL_z.npy` [14089]; `embed/gene_vectors.npy` [14089]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14089 or target_col == 14089). Every well: [[PRKG1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKG1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

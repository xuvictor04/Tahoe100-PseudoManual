---
symbol: "ERG"
type: "gene"
col: 8083
ensembl_id: "ENSG00000157554"
name: "ETS transcription factor ERG"
location: "21q22.2"
module: 73
arm: "+"
pooled_cpm: 4.2
n_lines_expressing: 20
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 8
direction_downstream: 18
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# ERG

*ETS transcription factor ERG* — 21q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.79× (z +20.4, q 0e+00, up in 3 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[5-Azacytidine (drug)]] 5 µM: 0.648× (z -4.0, q 0.032, down in 3 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LoVo 0.0710×, Hs 766T 0.0687×, LS 180 0.103×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (NCI-H23 0.0524×, LS 180 0.0948×, Hs 766T 0.166×); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (Hs 766T 0.0898×, LS 180 0.0922×, LoVo 0.237×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMP28]] (+0.63, fdr 3e-05), [[DOK5]] (+0.57, fdr 1e-05), [[ILDR2]] (+0.56, fdr 1e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 18 go from it, the strongest it → [[TLN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8083.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.79×** | +20.4 | 0e+00 | 3/12 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.26×** | +13.4 | 2e-38 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.45×** | +11.7 | 4e-29 | 11/15 (NCI-H1573, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.42×** | +10.9 | 2e-25 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.69×** | +8.4 | 4e-15 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.40×** | +8.1 | 7e-14 | 3/14 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.6 | 3e-09 | 0/15 | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.95×** | +6.2 | 5e-08 | 8/14 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +5.7 | 1e-06 | 3/13 (HOP62, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +5.0 | 3e-05 | 1/13 (RPMI-7951) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +4.6 | 2e-04 | 1/12 (HOP62) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +4.6 | 2e-04 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.21×** | +3.8 | 0.006 | 0/4 | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.77×** | +3.8 | 0.007 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +3.5 | 0.020 | 0/6 | top dose only | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.47×** | +3.3 | 0.040 | 2/10 (NCI-H1573, Hs 766T) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +3.2 | 0.053 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.062 | 1/14 (BT-474) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8083.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LoVo 0.0710×, Hs 766T 0.0687×, LS 180 0.103×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (NCI-H23 0.0524×, LS 180 0.0948×, Hs 766T 0.166×); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (Hs 766T 0.0898×, LS 180 0.0922×, LoVo 0.237×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **0.648×** | -4.0 | 0.032 | 3/14 (LS 180, LoVo, …) | top dose only |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.665× | -3.5 | 0.13 | 3/15 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.706× | -3.2 | 0.23 | 8/14 (NCI-H23, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8083. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 36.2 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0687× (z -18.5) |
| [[LoVo (line)]] | wt | 32.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0710× (z -24.5) |
| [[NCI-H23 (line)]] | alt | 21.8 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0781× (z -18.5) |
| [[HS-578T (line)]] | alt | 29.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -9.4) |
| [[LS 180 (line)]] | wt | 9.40 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 5.78 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.32× (z +8.8) | — |
| [[A-172 (line)]] | wt | 0.847 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.712 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.981 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.951 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.940 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.857 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.754 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.714 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.961 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.675 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.753 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.777 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.908 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.648 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.786 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.883 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.804 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.983 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.768 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.803 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.691 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8083), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMP28]] | +0.63 | +0.69 / +0.45 | both halves | 3e-05 | **novel candidate** |
| [[DOK5]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[ILDR2]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[TLL1]] | +0.56 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CFTR]] | +0.56 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[FREM2]] | +0.55 | +0.36 / +0.58 | both halves | 9e-05 |  |
| [[NEURL1]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[KCND3]] | +0.54 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[P2RY1]] | +0.53 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[LINC00457]] | +0.53 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[UGT1A1]] | +0.53 | +0.56 / +0.36 | both halves | 9e-05 |  |
| [[LINC00937]] | +0.53 | +0.42 / +0.44 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ERG's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[XACT]] | C | XACT activity raises ERG's level | lines that do not express XACT (30) vs lines expressing it (20) | 2.01× lower at baseline in the lines without XACT | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438; co-absent with the target |
| [[MIR646HG]] | C | MIR646HG activity raises ERG's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 2.02× lower at baseline in the lines without MIR646HG | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211; co-absent with the target |
| [[CALB1]] | C | CALB1 activity raises ERG's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 2.49× lower at baseline in the lines without CALB1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[LINC02582]] | C | LINC02582 activity raises ERG's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 2.21× lower at baseline in the lines without LINC02582 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |
| [[CFTR]] | C | CFTR activity raises ERG's level | lines that do not express CFTR (39) vs lines expressing it (11) | 1.93× lower at baseline in the lines without CFTR | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent; co-absent with the target |
| [[MMP28]] | C | MMP28 activity raises ERG's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.53× lower at baseline in the lines without MMP28 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent; co-absent with the target |
| [[IL33]] | C | IL33 activity raises ERG's level | lines that do not express IL33 (35) vs lines expressing it (15) | 2.12× lower at baseline in the lines without IL33 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01133, MUC2, LINC01411; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 5, C 13. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLN2]] | B | ERG activity raises TLN2's level | lines that do not express ERG (30) vs lines expressing it (20) | 1.76× lower at baseline in the lines without ERG | 0.005 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent |
| [[NEURL1]] | B | ERG activity raises NEURL1's level | lines that do not express ERG (30) vs lines expressing it (20) | 1.61× lower at baseline in the lines without ERG | 0.055 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent |
| [[LRP4]] | B | ERG activity raises LRP4's level | lines that do not express ERG (30) vs lines expressing it (20) | 1.59× lower at baseline in the lines without ERG | 0.075 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent |
| [[ATP8A1]] | B | ERG activity weakens ATP8A1's drug response | lines that do not express ERG (23) vs lines expressing it (12) | the lines without ERG respond 1.31× as strongly (z diff -1.45); strongest at Tucidinostat 5 µM: 2.57x vs 1.95x (z diff -2.4) | 0.076 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[KCNN3]] | B | ERG activity raises KCNN3's level | lines that do not express ERG (30) vs lines expressing it (20) | 1.72× lower at baseline in the lines without ERG | 0.092 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent |
| [[TPTEP1-1]] | C | ERG activity raises TPTEP1-1's level | lines that do not express ERG (30) vs lines expressing it (20) | 2.64× lower at baseline in the lines without ERG | 0.003 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent; co-absent with the target |
| [[CALB1]] | C | ERG activity raises CALB1's level | lines that do not express ERG (30) vs lines expressing it (20) | 1.95× lower at baseline in the lines without ERG | 0.004 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent; co-absent with the target |
| [[REG4]] | C | ERG activity raises REG4's level | lines that do not express ERG (30) vs lines expressing it (20) | 1.49× lower at baseline in the lines without ERG | 0.013 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent; co-absent with the target |
| [[SLITRK6]] | C | ERG activity raises SLITRK6's level | lines that do not express ERG (30) vs lines expressing it (20) | 2.86× lower at baseline in the lines without ERG | 0.019 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent; co-absent with the target |
| [[HEPH]] | C | ERG activity raises HEPH's level | lines that do not express ERG (30) vs lines expressing it (20) | 1.56× lower at baseline in the lines without ERG | 0.024 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent; co-absent with the target |
| [[TLL1]] | C | ERG activity raises TLL1's level | lines that do not express ERG (30) vs lines expressing it (20) | 2.08× lower at baseline in the lines without ERG | 0.025 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent; co-absent with the target |
| [[XACT]] | C | ERG activity raises XACT's level | lines that do not express ERG (30) vs lines expressing it (20) | 1.53× lower at baseline in the lines without ERG | 0.026 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.1, 47.3); signed map (45.2, 28.3). **Vector** length 39.3, 9.03% of its response variance represented; |z| ≥ 3 in 433 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +10.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +13.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +2.3 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -0.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -0.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.8 | -1.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ETS transcription factor ERG |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.2 — chr21:38,380,027-38,661,780 (-) |
| Ensembl biotype | protein_coding |
| Also known as | erg-3, p55 |
| Gene groups (HGNC) | ETS transcription factor family |
| Reactome | 1 pathways, smallest: Sprouting angiogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P11308](https://www.uniprot.org/uniprotkb/P11308) (Transcriptional regulator ERG):

> Transcriptional regulator. May participate in transcriptional regulation through the recruitment of SETDB1 histone methyltransferase and subsequent modification of local chromatin structure.

**Summary**, from NCBI Gene [2078](https://www.ncbi.nlm.nih.gov/gene/2078):

> This gene encodes a member of the erythroblast transformation-specific (ETS) family of transcriptions factors. All members of this family are key regulators of embryonic development, cell proliferation, differentiation, angiogenesis, inflammation, and apoptosis. The protein encoded by this gene is mainly expressed in the nucleus. It contains an ETS DNA-binding domain and a PNT (pointed) domain which is implicated in the self-association of chimeric oncoproteins. This protein is required for …

**Accessions** — [HGNC:3446](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3446) · Entrez [2078](https://www.ncbi.nlm.nih.gov/gene/2078) · UniProt [P11308](https://www.uniprot.org/uniprotkb/P11308) · Ensembl [ENSG00000157554](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157554)

## Data

Gene col 8083: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8083); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8083, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8083]; `tensor/DDL_lfc|DDL_z.npy` [8083]; `embed/gene_vectors.npy` [8083]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8083 or target_col == 8083). Every well: [[ERG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

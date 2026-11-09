---
symbol: "MACC1"
type: "gene"
col: 11447
ensembl_id: "ENSG00000183742"
name: "MET transcriptional regulator MACC1"
location: "7p21.1"
module: 8
arm: "+"
pooled_cpm: 131.6
n_lines_expressing: 18
n_dd_up: 9
n_dd_down: 23
n_dd_up_clean: 5
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 75
direction_downstream: 82
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# MACC1

*MET transcriptional regulator MACC1* — 7p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.08× (z +13.2, q 3e-37, up in 0 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Docetaxel (Trihydrate) (drug)]] 0.5 µM: 1.42× (z +4.1, q 0.005, up in 0 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.483× (z -8.6, q 6e-15, down in 15 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGEF38]] (+0.73, fdr 7e-06), [[ST14]] (+0.68, fdr 7e-06), [[POF1B]] (+0.66, fdr 7e-06); moves opposite to [[ITGB1BP1]] (-0.50, fdr 8e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 75 arrows point to it, the strongest [[ITGB8]] → it (grade B ⚠); 82 go from it, the strongest it → [[MUC20]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11447.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.08×** | +13.2 | 3e-37 | 0/17 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +10.5 | 2e-23 | 0/15 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +7.0 | 5e-10 | 0/15 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.42×** | +4.1 | 0.005 | 0/16 | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.27×** | +4.0 | 0.008 | 5/16 (BT-474, CFPAC-1, …) | top dose only | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.65×** | +3.9 | 0.008 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.015 | 9/16 (KATO III, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.015 | 0/16 | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.077 | 0/18 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sulfatinib (drug)]] 5 µM |  | 1.32× | +3.1 | 0.10 | 1/17 (KATO III) | top dose only |  |
| [[Erythromycin (drug)]] 5 µM |  | 1.30× | +3.1 | 0.10 | 0/16 | top dose only |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | 1.30× | +3.1 | 0.10 | 0/17 | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | 1.73× | +3.0 | 0.11 | 12/16 (LoVo, HT-29, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11447.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.483×** | -8.6 | 6e-15 | 15/16 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.506×** | -8.0 | 3e-13 | 14/16 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.559×** | -6.8 | 1e-09 | 15/16 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.645×** | -5.2 | 4e-05 | 12/16 (COLO 205, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.653×** | -5.0 | 6e-05 | 16/16 (SW480, SW1417, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.663×** | -4.8 | 1e-04 | 12/16 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.692×** | -4.3 | 0.001 | 7/16 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.712×** | -4.0 | 0.005 | 0/16 | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.718×** | -3.9 | 0.006 | 9/16 (LS 180, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.704×** | -3.8 | 0.008 | 0/16 | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -3.7 | 0.010 | 0/18 | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.811×** | -3.5 | 0.023 | 5/16 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Lapatinib ditosylate (drug)]] 0.5 µM |  | **0.649×** | -3.4 | 0.031 | 0/16 | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.738×** | -3.3 | 0.035 | 0/16 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.755×** | -3.3 | 0.035 | 9/16 (NCI-H460, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.759×** | -3.2 | 0.043 | 0/16 | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11447. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 359 | 0 | 13 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -19.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.152× (z -15.6) |
| [[COLO 205 (line)]] | alt | 927 | 0 | 11 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0844× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 64.8 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -16.0) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -11.6) |
| [[SW1417 (line)]] | alt | 892 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -17.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.141× (z -15.4) |
| [[CFPAC-1 (line)]] | alt | 466 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -16.5) |
| [[HEC-1-A (line)]] | alt | 360 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -14.1) |
| [[KATO III (line)]] | alt | 421 | 0 | 5 (3 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.106× (z -14.2) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.213× (z -10.3) |
| [[LoVo (line)]] | wt | 124 | 1 (1 ⚠) | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.15× (z +9.3) ⚠ cell-cycle shift, explains ~54% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.169× (z -12.1) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.270× (z -8.9) |
| [[LS 180 (line)]] | wt | 175 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.198× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 277 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 374 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.183× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 210 | 4 (2 ⚠) | 0 | [[Peretinoin (drug)]] 5 µM 4.07× (z +10.2) | — |
| [[SW48 (line)]] | wt | 120 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.207× (z -9.6) |
| [[BT-474 (line)]] | alt | 104 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +12.9) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[HT-29 (line)]] | alt | 241 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.161× (z -9.7) |
| [[A-172 (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.98 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 8.53 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.21 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 21.8 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.9 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.82 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.4 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.82 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.08 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.78 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.89 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.47 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.07 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 22.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 16.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11447), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF38]] | +0.73 | +0.78 / +0.68 | both halves | 7e-06 | same gene group |
| [[ST14]] | +0.68 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[POF1B]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[OCLN]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[FRK]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 | same gene group |
| [[TOX3]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[DAPP1]] | +0.64 | +0.59 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS2]] | +0.64 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[EXPH5]] | +0.63 | +0.70 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[ADGRF1]] | +0.63 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ANXA3]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ST6GALNAC5]] | +0.60 | +0.63 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB1BP1]] | -0.50 | -0.52 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*75 arrows, 75 of them with an alert ⚠; grade A 0, B 8, C 67. Shown: the 12 strongest; 63 more arrows (63 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB8]] | B | ITGB8 activity raises MACC1's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 3.93× lower at baseline in the lines without ITGB8 | 0.014 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises MACC1's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 4.51× lower at baseline in the lines without ELF3-AS1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[MUC20]] | B | MUC20 activity raises MACC1's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 4.02× lower at baseline in the lines without MUC20 | 0.031 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[SLC44A3]] | B | SLC44A3 activity raises MACC1's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.89× lower at baseline in the lines without SLC44A3 | 0.043 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[STS]] | B | STS activity raises MACC1's level | lines that do not express STS (11) vs lines expressing it (39) | 3.13× lower at baseline in the lines without STS | 0.086 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[HNF4G]] | B | HNF4G activity raises MACC1's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 3.89× lower at baseline in the lines without HNF4G | 0.088 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[SPATA6L]] | B | SPATA6L activity raises MACC1's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 4.14× lower at baseline in the lines without SPATA6L | 0.094 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[SH3RF2]] | B | SH3RF2 activity raises MACC1's level | lines that do not express SH3RF2 (16) vs lines expressing it (34) | 3.67× lower at baseline in the lines without SH3RF2 | 0.096 | ⚠ within organs, on part of the lines; also absent: LINC01564, CAPG, LINC00857; maybe low, not absent |
| [[ITGB6]] | C | ITGB6 activity raises MACC1's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 14.33× lower at baseline in the lines without ITGB6 | 1e-05 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4; co-absent with the target |
| [[ST14]] | C | ST14 activity raises MACC1's level | lines that do not express ST14 (32) vs lines expressing it (18) | 16.14× lower at baseline in the lines without ST14 | 1e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1; co-absent with the target |
| [[ARHGEF38]] | C | ARHGEF38 activity raises MACC1's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 18.20× lower at baseline in the lines without ARHGEF38 | 1e-05 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1; co-absent with the target |
| [[CDH1]] | C | CDH1 activity raises MACC1's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 13.90× lower at baseline in the lines without CDH1 | 2e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1; co-absent with the target |

### Downstream of this gene

*82 arrows, 82 of them with an alert ⚠; grade A 0, B 20, C 62. Shown: the 12 strongest; 70 more arrows (70 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC20]] | B | MACC1 activity raises MUC20's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 4.38× lower at baseline in the lines without MACC1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2 |
| [[TMEM184A]] | B | MACC1 activity raises TMEM184A's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 2.91× lower at baseline in the lines without MACC1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2 |
| [[SLC44A3]] | B | MACC1 activity raises SLC44A3's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 3.46× lower at baseline in the lines without MACC1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2 |
| [[SLC12A2]] | B | MACC1 activity raises SLC12A2's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 2.89× lower at baseline in the lines without MACC1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2 |
| [[ELF3-AS1]] | B | MACC1 activity raises ELF3-AS1's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 3.86× lower at baseline in the lines without MACC1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2 |
| [[SH3RF2]] | B | MACC1 activity raises SH3RF2's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 3.31× lower at baseline in the lines without MACC1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2 |
| [[STX19]] | B | MACC1 activity raises STX19's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 2.35× lower at baseline in the lines without MACC1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2 |
| [[STS]] | B | MACC1 activity raises STS's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 2.92× lower at baseline in the lines without MACC1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2 |
| [[LINC00857]] | B | MACC1 activity raises LINC00857's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 3.13× lower at baseline in the lines without MACC1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2 |
| [[OCLN]] | B | MACC1 activity strengthens OCLN's drug response | lines that do not express MACC1 (14) vs lines expressing it (16) | the lines without MACC1 respond 0.17× as strongly (z diff +4.88); strongest at Homoharringtonine 5 µM: 1.12x vs 0.42x (z diff +8.2) | 0.016 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2; target measured in part of the lines; artifact flags |
| [[ITGB8]] | B | MACC1 activity raises ITGB8's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 2.76× lower at baseline in the lines without MACC1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2 |
| [[TNFRSF21]] | B | MACC1 activity raises TNFRSF21's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 3.56× lower at baseline in the lines without MACC1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.1, 53.6); signed map (56.4, 5.7). **Vector** length 100, 44.6% of its response variance represented; |z| ≥ 3 in 617 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +13.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +2.8 | +4.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.4 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +1.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +2.9 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -5.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.8 | -4.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -3.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | MET transcriptional regulator MACC1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.1 — chr7:20,134,655-20,217,404 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 7A5, SH3BP4L |
| Gene groups (HGNC) | ZU5 domain containing ; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZN28](https://www.uniprot.org/uniprotkb/Q6ZN28) (Metastasis-associated in colon cancer protein 1):

> Acts as a transcription activator for MET and as a key regulator of HGF-MET signaling. Promotes cell motility, proliferation and hepatocyte growth factor (HGF)-dependent scattering in vitro and tumor growth and metastasis in vivo.

**Summary**, from NCBI Gene [346389](https://www.ncbi.nlm.nih.gov/gene/346389):

> MACC1 is a key regulator of the hepatocyte growth factor (HGF; MIM 142409)-HGF receptor (HGFR, or MET; MIM 164860) pathway, which is involved in cellular growth, epithelial-mesenchymal transition, angiogenesis, cell motility, invasiveness, and metastasis. Expression of MACC1 in colon cancer (MIM 114500) specimens is an independent prognostic indicator for metastasis formation and metastasis-free survival (Stein et al., 2009 [PubMed 19098908]).[supplied by OMIM, Mar 2009]

**Accessions** — [HGNC:30215](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30215) · Entrez [346389](https://www.ncbi.nlm.nih.gov/gene/346389) · UniProt [Q6ZN28](https://www.uniprot.org/uniprotkb/Q6ZN28) · Ensembl [ENSG00000183742](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183742)

## Data

Gene col 11447: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11447); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11447, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11447]; `tensor/DDL_lfc|DDL_z.npy` [11447]; `embed/gene_vectors.npy` [11447]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11447 or target_col == 11447). Every well: [[MACC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MACC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "SMOX"
type: "gene"
col: 1545
ensembl_id: "ENSG00000088826"
name: "spermine oxidase"
location: "20p13"
module: 136
arm: "+"
pooled_cpm: 71.14
n_lines_expressing: 44
n_dd_up: 3
n_dd_down: 51
n_dd_up_clean: 3
n_dd_down_clean: 37
in_vector_space: true
direction_upstream: 30
direction_downstream: 45
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# SMOX

*spermine oxidase* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.32× (z +4.1, q 0.027, up in 18 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 51 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.492× (z -9.5, q 2e-18, down in 25 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.634× (z -7.9, q 4e-13, down in 33 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX1A]] (+0.67, fdr 7e-06), [[BMERB1]] (+0.65, fdr 7e-06), [[SHB]] (+0.64, fdr 7e-06); moves opposite to [[TBC1D5]] (-0.54, fdr 2e-05), [[RAB11FIP2]] (-0.52, fdr 4e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[ITGB3]] → it (grade B ⚠); 45 go from it, the strongest it → [[PLAUR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1545.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.32×** | +4.1 | 0.027 | 18/41 (NCI-H460, LOX-IMVI, …) | two highest doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.027 | 16/42 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.073 | 15/43 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | 1.23× | +3.1 | 0.29 | 8/42 (SW 1088, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 51 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1545.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.492×** | -9.5 | 2e-18 | 25/35 (Panc 03.27, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.561×** | -8.0 | 3e-13 | 24/34 (RPMI-7951, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.634×** | -7.9 | 4e-13 | 33/42 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.612×** | -7.5 | 9e-12 | 30/44 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.598×** | -7.4 | 2e-11 | 31/42 (HepG2/C3A, SW 900, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.607×** | -6.9 | 5e-10 | 29/42 (NCI-H460, HS-578T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.623×** | -6.8 | 8e-10 | 32/43 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.616×** | -6.7 | 2e-09 | 31/41 (NCI-H460, HepG2/C3A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.625×** | -6.5 | 5e-09 | 26/41 (SW 900, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.618×** | -6.4 | 8e-09 | 28/42 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -6.3 | 1e-08 | 27/42 (SW 900, A498, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.681×** | -6.0 | 7e-08 | 28/43 (NCI-H460, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.724×** | -5.5 | 1e-06 | 28/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.672×** | -5.5 | 2e-06 | 23/41 (SW 900, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.769×** | -5.3 | 4e-06 | 20/41 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.690×** | -5.1 | 1e-05 | 24/44 (SW 900, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.792×** | -4.7 | 8e-05 | 22/42 (HT-29, SW 900, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.720×** | -4.7 | 8e-05 | 20/41 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.793×** | -4.6 | 1e-04 | 23/42 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1545. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 279 | 0 | 26 (17 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -15.1) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.207× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 139 | 0 | 16 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -18.5) |
| [[hTERT-HPNE (line)]] | wt | 142 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.146× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 194 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -14.5) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -10.9) |
| [[A498 (line)]] | wt | 69.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -10.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 209 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.214× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 46.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 29.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -10.5) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.459× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 170 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -14.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 270 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -12.1) |
| [[HepG2_C3A (line)]] | wt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0850× (z -19.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 99.0 | 0 | 2 | — | [[Osimertinib (mesylate) (drug)]] 5 µM 0.0649× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 20.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +10.4) | — |
| [[CHP-212 (line)]] | wt | 33.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0780× (z -12.3) |
| [[COLO 205 (line)]] | alt | 48.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -9.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 51.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -8.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 58.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -11.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 45.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -8.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 29.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.191× (z -10.5) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -9.6) ⚠ cell-cycle shift, explains ~8% of this change |
| [[A-172 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.60 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.97 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.1 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.8 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 49.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1545), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX1A]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[BMERB1]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[SHB]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[DUSP5]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[STC1]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[RAC2]] | +0.63 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[SLC25A51]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[WWTR1]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[RGS17]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[PC]] | +0.61 | +0.52 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[CRLF2]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D5]] | -0.54 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[RAB11FIP2]] | -0.52 | -0.43 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 29, C 1. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB3]] | B | ITGB3 activity raises SMOX's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 2.54× lower at baseline in the lines without ITGB3 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[PTGS2]] | B | PTGS2 activity raises SMOX's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.86× lower at baseline in the lines without PTGS2 | 0.003 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[MTSS1]] | B | MTSS1 activity raises SMOX's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without MTSS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[TREM1]] | B | TREM1 activity raises SMOX's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 2.88× lower at baseline in the lines without TREM1 | 0.006 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[VEGFC]] | B | VEGFC activity raises SMOX's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 2.46× lower at baseline in the lines without VEGFC | 0.008 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1 |
| [[FAM107B]] | B | FAM107B activity raises SMOX's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.72× lower at baseline in the lines without FAM107B | 0.015 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[DUSP5]] | B | DUSP5 activity raises SMOX's level | lines that do not express DUSP5 (7) vs lines expressing it (43) | 3.02× lower at baseline in the lines without DUSP5 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000236213, CA13, SLC2A1; maybe low, not absent |
| [[ELL2]] | B | ELL2 activity raises SMOX's level | lines that do not express ELL2 (12) vs lines expressing it (38) | 2.82× lower at baseline in the lines without ELL2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent |
| [[GFPT2]] | B | GFPT2 activity raises SMOX's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 2.23× lower at baseline in the lines without GFPT2 | 0.018 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[CRLF2]] | B | CRLF2 activity raises SMOX's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 2.76× lower at baseline in the lines without CRLF2 | 0.022 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR |
| [[HTR7]] | B | HTR7 activity raises SMOX's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 2.44× lower at baseline in the lines without HTR7 | 0.025 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[IL33]] | B | IL33 activity raises SMOX's level | lines that do not express IL33 (35) vs lines expressing it (15) | 1.92× lower at baseline in the lines without IL33 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01133, MUC2, LINC01411 |

### Downstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 40, C 5. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAUR]] | B | SMOX activity raises PLAUR's level | lines that do not express SMOX (6) vs lines expressing it (44) | 4.89× lower at baseline in the lines without SMOX | 0.005 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[STX1A]] | B | SMOX activity raises STX1A's level | lines that do not express SMOX (6) vs lines expressing it (44) | 2.66× lower at baseline in the lines without SMOX | 0.009 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[IGFBP3]] | B | SMOX activity raises IGFBP3's level | lines that do not express SMOX (6) vs lines expressing it (44) | 6.71× lower at baseline in the lines without SMOX | 0.010 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[STK17A]] | B | SMOX activity raises STK17A's level | lines that do not express SMOX (6) vs lines expressing it (44) | 2.62× lower at baseline in the lines without SMOX | 0.011 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[FAM107B]] | B | SMOX activity raises FAM107B's level | lines that do not express SMOX (6) vs lines expressing it (44) | 5.90× lower at baseline in the lines without SMOX | 0.012 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[VEGFC]] | B | SMOX activity raises VEGFC's level | lines that do not express SMOX (6) vs lines expressing it (44) | 2.60× lower at baseline in the lines without SMOX | 0.012 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[CDCP1]] | B | SMOX activity raises CDCP1's level | lines that do not express SMOX (6) vs lines expressing it (44) | 3.65× lower at baseline in the lines without SMOX | 0.018 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[HPCAL1]] | B | SMOX activity raises HPCAL1's level | lines that do not express SMOX (6) vs lines expressing it (44) | 2.85× lower at baseline in the lines without SMOX | 0.021 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[TIMP1]] | B | SMOX activity raises TIMP1's level | lines that do not express SMOX (6) vs lines expressing it (44) | 3.24× lower at baseline in the lines without SMOX | 0.024 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[ELL2]] | B | SMOX activity raises ELL2's level | lines that do not express SMOX (6) vs lines expressing it (44) | 2.43× lower at baseline in the lines without SMOX | 0.026 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[ITGA2]] | B | SMOX activity raises ITGA2's level | lines that do not express SMOX (6) vs lines expressing it (44) | 4.81× lower at baseline in the lines without SMOX | 0.027 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[CD82]] | B | SMOX activity raises CD82's level | lines that do not express SMOX (6) vs lines expressing it (44) | 4.26× lower at baseline in the lines without SMOX | 0.041 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.0, 2.7); signed map (4.2, 49.1). **Vector** length 129, 38.8% of its response variance represented; |z| ≥ 3 in 1,307 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +0.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.9 | +0.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.4 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +1.9 | +1.9 |
|  | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +1.8 | +1.9 |
| fall | [[Trametinib (drug)]] 5 µM |  | -7.3 | -7.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.8 | -7.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.5 | -6.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.2 | -6.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.8 | -6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.8 | -6.9 |

## What is on record

|  |  |
|---|---|
| Name | spermine oxidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:4,120,980-4,187,747 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20746, dJ779E11.1, PAO, PAOh1, MGC1010, SMO; previously C20orf16 |
| Gene groups (HGNC) | Flavoproteins; Polyamine oxidases |
| Hallmark sets | XENOBIOTIC_METABOLISM, HEME_METABOLISM |
| Reactome | 6 pathways, smallest: Interconversion of polyamines; Amine Oxidase reactions; Metabolism of polyamines |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWM0](https://www.uniprot.org/uniprotkb/Q9NWM0) (Spermine oxidase):

> Flavoenzyme which catalyzes the oxidation of spermine to spermidine. Can also use N(1)-acetylspermine and spermidine as substrates, with different affinity depending on the isoform (isozyme) and on the experimental conditions. Plays an important role in the regulation of polyamine intracellular concentration and has the potential to act as a determinant of cellular sensitivity to the antitumor polyamine analogs. May contribute to beta-alanine production via aldehyde dehydrogenase conversion of …

**Summary**, from NCBI Gene [54498](https://www.ncbi.nlm.nih.gov/gene/54498):

> Polyamines are ubiquitous polycationic alkylamines which include spermine, spermidine, putrescine, and agmatine. These molecules participate in a broad range of cellular functions which include cell cycle modulation, scavenging reactive oxygen species, and the control of gene expression. These molecules also play important roles in neurotransmission through their regulation of cell-surface receptor activity, involvement in intracellular signalling pathways, and their putative roles as …

**Accessions** — [HGNC:15862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15862) · Entrez [54498](https://www.ncbi.nlm.nih.gov/gene/54498) · UniProt [Q9NWM0](https://www.uniprot.org/uniprotkb/Q9NWM0) · Ensembl [ENSG00000088826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088826)

## Data

Gene col 1545: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1545); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1545, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1545]; `tensor/DDL_lfc|DDL_z.npy` [1545]; `embed/gene_vectors.npy` [1545]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1545 or target_col == 1545). Every well: [[SMOX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMOX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

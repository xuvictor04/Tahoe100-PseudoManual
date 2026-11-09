---
symbol: "RMDN2-AS1"
type: "gene"
col: 14042
ensembl_id: "ENSG00000235848"
name: "RMDN2 antisense RNA 1"
location: "2p22.2"
module: 19
arm: "+"
pooled_cpm: 4.59
n_lines_expressing: 36
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 4
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# RMDN2-AS1

*RMDN2 antisense RNA 1* — 2p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.75× (z +17.9, q 0e+00, up in 18 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (SW 900 0.0583×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (SW 900 0.0645×; ⚠ cell-cycle shift, explains ~44% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.0372×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SW 900 0.101×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (HT-29 0.0448×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYP1B1]] (+0.78, fdr 7e-06, ⚠ read-through risk), [[CYP1B1-AS1]] (+0.76, fdr 7e-06, ⚠ same locus), [[NOVA1]] (+0.66, fdr 7e-06), [[ARHGAP15]] (+0.65, fdr 1e-05), [[RIMS1]] (+0.62, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CYP1B1]] → it (grade B ⚠); 4 go from it, the strongest it → [[CYP1B1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14042.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.75×** | +17.9 | 0e+00 | 18/21 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.81×** | +10.6 | 1e-23 | 16/25 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.77×** | +9.6 | 2e-19 | 2/13 (HOP62, PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.83×** | +9.0 | 4e-17 | 2/9 (PANC-1, CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.81×** | +7.5 | 1e-11 | 12/25 (A-172, CFPAC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.49×** | +6.3 | 2e-08 | 2/9 (PANC-1, A498) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.81×** | +6.1 | 1e-07 | 9/30 (PANC-1, HS-578T, …) | top dose only |  |
| [[Menadione (drug)]] 5 µM |  | **2.18×** | +5.4 | 4e-06 | 18/24 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **1.75×** | +5.4 | 4e-06 | 16/29 (PANC-1, CFPAC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.97×** | +4.9 | 6e-05 | 9/24 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.47×** | +4.7 | 1e-04 | 3/7 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 5 µM |  | **3.36×** | +4.6 | 2e-04 | 13/16 (PANC-1, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.79×** | +4.2 | 0.001 | 14/34 (NCI-H460, SW 900, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **2.76×** | +3.8 | 0.005 | 5/10 (PANC-1, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +3.8 | 0.006 | 5/17 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.73×** | +3.7 | 0.006 | 14/27 (SW 900, NCI-H460, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +3.7 | 0.008 | 4/21 (hTERT-HPNE, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD-7648 (drug)]] 0.5 µM |  | **2.64×** | +3.6 | 0.010 | 9/22 (PANC-1, HT-29, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 5 µM |  | **1.94×** | +3.5 | 0.011 | 5/22 (CFPAC-1, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **2.55×** | +3.5 | 0.015 | 3/20 (PANC-1, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14042.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (SW 900 0.0583×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (SW 900 0.0645×; ⚠ cell-cycle shift, explains ~44% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.0372×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SW 900 0.101×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (HT-29 0.0448×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.721× | -3.3 | 0.27 | 12/32 (H4, AN3 CA, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.639× | -3.2 | 0.27 | 8/28 (NCI-H2030, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.644× | -3.2 | 0.27 | 6/29 (NCI-H1792, Hs 766T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14042. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 52.9 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0583× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.101× (z -9.0) |
| [[HS-578T (line)]] | alt | 3.64 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.8× (z +12.1) | — |
| [[HT-29 (line)]] | alt | 8.65 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0372× (z -9.1) |
| [[A498 (line)]] | wt | 1.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.9× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 1.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 2.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.0× (z +12.1) | — |
| [[A-172 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.941 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.897 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.980 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.948 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.864 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.994 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.972 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.999 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.996 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14042), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP1B1]] | +0.78 | +0.84 / +0.73 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of CYP1B1 on the same strand (can correlate by spillover, not regulation) |
| [[CYP1B1-AS1]] | +0.76 | +0.72 / +0.72 | both halves | 7e-06 | same gene group; ⚠ same locus (6.4 kb: neighbours can correlate without regulation) |
| [[NOVA1]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[ARHGAP15]] | +0.65 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[RIMS1]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[LINC02363]] | +0.60 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[IL34]] | +0.60 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[PRRT3]] | +0.60 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[AQP4-AS1]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 | same gene group |
| [[FAM151B]] | +0.59 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[GUCY1A2]] | +0.58 | +0.65 / +0.37 | both halves | 7e-05 |  |
| [[TENM3-AS1]] | +0.58 | +0.52 / +0.45 | both halves | 3e-05 | same gene group |
| [[TNFRSF11B]] | +0.58 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[RDH10]] | +0.57 | +0.61 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP1B1]] | B | CYP1B1 activity raises RMDN2-AS1's level | lines that do not express CYP1B1 (29) vs lines expressing it (21) | 2.76× lower at baseline in the lines without CYP1B1 | 0.001 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849 |
| [[STEAP1B-AS1]] | B | STEAP1B-AS1 activity raises RMDN2-AS1's level | lines that do not express STEAP1B-AS1 (30) vs lines expressing it (20) | 2.13× lower at baseline in the lines without STEAP1B-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, IL6, EFEMP1 |
| [[IL6]] | B | IL6 activity raises RMDN2-AS1's level | lines that do not express IL6 (32) vs lines expressing it (18) | 2.28× lower at baseline in the lines without IL6 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[NOVA1]] | B | NOVA1 activity raises RMDN2-AS1's level | lines that do not express NOVA1 (27) vs lines expressing it (23) | 2.03× lower at baseline in the lines without NOVA1 | 0.057 | ⚠ within organs, on part of the lines; also absent: EPHA6, ZYG11A, GALNT13 |
| [[BASP1-AS1]] | B | BASP1-AS1 activity raises RMDN2-AS1's level | lines that do not express BASP1-AS1 (28) vs lines expressing it (22) | 2.05× lower at baseline in the lines without BASP1-AS1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LRRC63, FGF14 |
| [[EBF1]] | B | EBF1 activity raises RMDN2-AS1's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 2.10× lower at baseline in the lines without EBF1 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4 |
| [[TOP2A]] | B | TOP2A activity lowers RMDN2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CYP1B1-AS1]] | B | CYP1B1-AS1 activity raises RMDN2-AS1's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 1.94× lower at baseline in the lines without CYP1B1-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP1B1-AS1]] | B | RMDN2-AS1 activity raises CYP1B1-AS1's level | lines that do not express RMDN2-AS1 (14) vs lines expressing it (36) | 2.58× lower at baseline in the lines without RMDN2-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: EHD3, PLOD2, ZNF43; maybe low, not absent |
| [[CYP1B1]] | B | RMDN2-AS1 activity raises CYP1B1's level | lines that do not express RMDN2-AS1 (14) vs lines expressing it (36) | 4.12× lower at baseline in the lines without RMDN2-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: EHD3, PLOD2, ZNF43; maybe low, not absent |
| [[ZMIZ1-AS1]] | B | RMDN2-AS1 activity raises ZMIZ1-AS1's level | lines that do not express RMDN2-AS1 (14) vs lines expressing it (36) | 1.49× lower at baseline in the lines without RMDN2-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: EHD3, PLOD2, ZNF43; maybe low, not absent |
| [[ARHGAP15]] | B | RMDN2-AS1 activity raises ARHGAP15's level | lines that do not express RMDN2-AS1 (14) vs lines expressing it (36) | 1.16× lower at baseline in the lines without RMDN2-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: EHD3, PLOD2, ZNF43; maybe low, not absent |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.484). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.4, 23.5); signed map (48.2, 24.7). **Vector** length 57.6, 11.9% of its response variance represented; |z| ≥ 3 in 662 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +17.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +7.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +3.7 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -3.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | RMDN2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p22.2 — chr2:37,949,911-38,067,041 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41150](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41150) · Entrez [101410544](https://www.ncbi.nlm.nih.gov/gene/101410544) · Ensembl [ENSG00000235848](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235848)

## Data

Gene col 14042: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14042); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14042, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14042]; `tensor/DDL_lfc|DDL_z.npy` [14042]; `embed/gene_vectors.npy` [14042]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14042 or target_col == 14042). Every well: [[RMDN2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RMDN2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

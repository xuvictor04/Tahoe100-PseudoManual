---
symbol: "HMCN1"
type: "gene"
col: 6718
ensembl_id: "ENSG00000143341"
name: "hemicentin 1"
location: "1q25.3-q31.1"
module: 9
arm: "+"
pooled_cpm: 19.73
n_lines_expressing: 24
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 17
direction_downstream: 20
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# HMCN1

*hemicentin 1* — 1q25.3-q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.82× (z +16.7, q 0e+00, up in 12 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Artesunate (drug)]] 5 µM: 0.747× (z -4.7, q 0.002, down in 8 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (CHP-212 0.0927×, SW1417 0.0654×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.0860×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.338×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIEZO2]] (+0.73, fdr 7e-06), [[ATRNL1]] (+0.70, fdr 7e-06), [[UNC5C]] (+0.68, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 20 go from it, the strongest it → [[LDB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6718.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.82×** | +16.7 | 0e+00 | 12/21 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.12×** | +12.2 | 1e-31 | 12/22 (NCI-H460, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +11.2 | 8e-27 | 7/17 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +9.3 | 3e-18 | 6/15 (SW 900, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.12×** | +8.8 | 1e-16 | 13/22 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +8.1 | 7e-14 | 10/20 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.85×** | +7.2 | 5e-11 | 7/22 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.73×** | +6.4 | 1e-08 | 10/22 (H4, A498, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +6.2 | 5e-08 | 11/22 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +5.9 | 2e-07 | 9/19 (H4, HOP62, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +4.3 | 0.001 | 4/17 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.2 | 0.001 | 2/22 (HOP62, LOX-IMVI) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.43×** | +4.2 | 0.001 | 11/22 (H4, HOP62, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.6 | 0.012 | 4/19 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +3.3 | 0.033 | 11/21 (HOP62, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.079 | 9/22 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.098 | 11/22 (NCI-H1792, SW 900, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6718.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (CHP-212 0.0927×, SW1417 0.0654×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.0860×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.338×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **0.747×** | -4.7 | 0.002 | 8/22 (HS-578T, CHP-212, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.759×** | -4.4 | 0.002 | 12/22 (CHP-212, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.754× | -3.3 | 0.14 | 10/20 (NCI-H2030, HS-578T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.756× | -3.3 | 0.14 | 9/21 (NCI-H460, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.759× | -3.2 | 0.14 | 5/21 (SK-MEL-2, CHP-212, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.758× | -3.1 | 0.17 | 9/21 (SW 900, hTERT-HPNE, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | 0.607× | -3.1 | 0.18 | 5/22 (NCI-H1792, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Menadione (drug)]] 5 µM |  | 0.765× | -3.0 | 0.18 | 4/20 (NCI-H23, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6718. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 69.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0927× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 105 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.71× (z +11.0) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 7.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 8.17 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.42× (z +10.4) | — |
| [[SW1417 (line)]] | alt | 9.25 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0654× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.04 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 332 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 88.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 170 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.75 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.54 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.88 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6718), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIEZO2]] | +0.73 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[ATRNL1]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[UNC5C]] | +0.68 | +0.54 / +0.71 | both halves | 1e-05 | same gene group |
| [[GRIK2]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[CDH18]] | +0.65 | +0.65 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[DMD]] | +0.65 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[ANGPT1]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[EPHA7]] | +0.63 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[NREP]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[PPP2R2B]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[MOXD1]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[NKAIN3]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 1, C 16. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HMCN1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EPHA5]] | C | EPHA5 activity raises HMCN1's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 5.58× lower at baseline in the lines without EPHA5 | 0.007 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[LINC01687]] | C | LINC01687 activity raises HMCN1's level | lines that do not express LINC01687 (31) vs lines expressing it (19) | 4.55× lower at baseline in the lines without LINC01687 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC02616, TPTE; co-absent with the target |
| [[SOX5]] | C | SOX5 activity raises HMCN1's level | lines that do not express SOX5 (24) vs lines expressing it (26) | 4.14× lower at baseline in the lines without SOX5 | 0.016 | ⚠ within organs, on part of the lines; also absent: CTHRC1, MOXD1, AK5; co-absent with the target |
| [[COL8A1]] | C | COL8A1 activity raises HMCN1's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 4.00× lower at baseline in the lines without COL8A1 | 0.037 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |
| [[ENPP2]] | C | ENPP2 activity raises HMCN1's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 3.83× lower at baseline in the lines without ENPP2 | 0.050 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent; co-absent with the target |
| [[MAP1A]] | C | MAP1A activity raises HMCN1's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 4.02× lower at baseline in the lines without MAP1A | 0.054 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent; co-absent with the target |
| [[GRIK2]] | C | GRIK2 activity raises HMCN1's level | lines that do not express GRIK2 (19) vs lines expressing it (31) | 3.57× lower at baseline in the lines without GRIK2 | 0.061 | ⚠ within organs, on part of the lines; also absent: MIR9-3HG, PCDH10, PLEKHG4B; co-absent with the target |
| [[ANGPT1]] | C | ANGPT1 activity raises HMCN1's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 3.71× lower at baseline in the lines without ANGPT1 | 0.061 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5; co-absent with the target |
| [[TMEM108]] | C | TMEM108 activity raises HMCN1's level | lines that do not express TMEM108 (23) vs lines expressing it (27) | 3.66× lower at baseline in the lines without TMEM108 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: TWIST1, FYB1, GATA3; maybe low, not absent; co-absent with the target |
| [[FBN1]] | C | FBN1 activity raises HMCN1's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 3.23× lower at baseline in the lines without FBN1 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; co-absent with the target |
| [[GLIS1]] | C | GLIS1 activity raises HMCN1's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 3.31× lower at baseline in the lines without GLIS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 5, C 15. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LDB2]] | B | HMCN1 activity raises LDB2's level | lines that do not express HMCN1 (26) vs lines expressing it (24) | 2.40× lower at baseline in the lines without HMCN1 | 0.020 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent |
| [[NREP]] | B | HMCN1 activity raises NREP's level | lines that do not express HMCN1 (26) vs lines expressing it (24) | 3.84× lower at baseline in the lines without HMCN1 | 0.087 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent |
| cells under [[5-Azacytidine (drug)]] 5 µM | B | HMCN1 activity lowers the cells' numbers under 5-Azacytidine 5 µM (makes them more sensitive) | lines that do not express HMCN1 (26) vs lines expressing it (22) | the lines without HMCN1: 1.27× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent |
| [[LINC01013]] | B | HMCN1 activity raises LINC01013's level | lines that do not express HMCN1 (26) vs lines expressing it (24) | 2.62× lower at baseline in the lines without HMCN1 | 0.096 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent |
| [[LINC02882]] | B | HMCN1 activity raises LINC02882's level | lines that do not express HMCN1 (26) vs lines expressing it (24) | 2.62× lower at baseline in the lines without HMCN1 | 0.098 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent |
| [[EPHA5]] | C | HMCN1 activity raises EPHA5's level | lines that do not express HMCN1 (26) vs lines expressing it (24) | 5.38× lower at baseline in the lines without HMCN1 | 0.004 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent; co-absent with the target |
| [[LINC01687]] | C | HMCN1 activity raises LINC01687's level | lines that do not express HMCN1 (26) vs lines expressing it (24) | 3.91× lower at baseline in the lines without HMCN1 | 0.011 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent; co-absent with the target |
| [[GLIS1]] | C | HMCN1 activity raises GLIS1's level | lines that do not express HMCN1 (26) vs lines expressing it (24) | 3.76× lower at baseline in the lines without HMCN1 | 0.012 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent; co-absent with the target |
| [[IGFBP7]] | C | HMCN1 activity raises IGFBP7's level | lines that do not express HMCN1 (26) vs lines expressing it (24) | 5.15× lower at baseline in the lines without HMCN1 | 0.023 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent; co-absent with the target |
| [[ITGA4]] | C | HMCN1 activity raises ITGA4's level | lines that do not express HMCN1 (26) vs lines expressing it (24) | 5.35× lower at baseline in the lines without HMCN1 | 0.026 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent; co-absent with the target |
| [[ENPP2]] | C | HMCN1 activity raises ENPP2's level | lines that do not express HMCN1 (26) vs lines expressing it (24) | 3.02× lower at baseline in the lines without HMCN1 | 0.048 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent; co-absent with the target |
| [[ANGPT1]] | C | HMCN1 activity raises ANGPT1's level | lines that do not express HMCN1 (26) vs lines expressing it (24) | 4.35× lower at baseline in the lines without HMCN1 | 0.055 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.6, 30.3); signed map (37.6, 33.3). **Vector** length 49.7, 11.7% of its response variance represented; |z| ≥ 3 in 497 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +12.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +16.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +1.0 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +1.2 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -2.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.8 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.6 | -4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | hemicentin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3-q31.1 — chr1:185,734,391-186,190,949 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBLN6, FIBL6, FIBL-6; previously ARMD1 |
| Gene groups (HGNC) | Fibulins; I-set domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RW7](https://www.uniprot.org/uniprotkb/Q96RW7) (Hemicentin-1):

> Involved in transforming growth factor beta-mediated rearrangement of the podocyte cytoskeleton which includes reduction of F-actin fibers and broadening, flattening and elongation of podocytes. Plays a role in basement membrane organization (By similarity). May promote cleavage furrow maturation during cytokinesis in preimplantation embryos (By similarity). May play a role in the architecture of adhesive and flexible epithelial cell junctions (By similarity). May play a role during myocardial …

**Summary**, from NCBI Gene [83872](https://www.ncbi.nlm.nih.gov/gene/83872):

> This gene encodes a large extracellular member of the immunoglobulin superfamily. A similar protein in C. elegans forms long, fine tracks at specific extracellular sites that are involved in many processes such as stabilization of the germline syncytium, anchorage of mechanosensory neurons to the epidermis, and organization of hemidesmosomes in the epidermis. Mutations in this gene may be associated with age-related macular degeneration. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19194](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19194) · Entrez [83872](https://www.ncbi.nlm.nih.gov/gene/83872) · UniProt [Q96RW7](https://www.uniprot.org/uniprotkb/Q96RW7) · Ensembl [ENSG00000143341](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143341)

## Data

Gene col 6718: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6718); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6718, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6718]; `tensor/DDL_lfc|DDL_z.npy` [6718]; `embed/gene_vectors.npy` [6718]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6718 or target_col == 6718). Every well: [[HMCN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMCN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

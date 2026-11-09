---
symbol: "PDZRN3"
type: "gene"
col: 4275
ensembl_id: "ENSG00000121440"
name: "PDZ domain containing ring finger 3"
location: "3p13"
module: 9
arm: "+"
pooled_cpm: 12.82
n_lines_expressing: 20
n_dd_up: 35
n_dd_down: 3
n_dd_up_clean: 27
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 22
direction_downstream: 28
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PDZRN3

*PDZ domain containing ring finger 3* — 3p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.02× (z +17.5, q 0e+00, up in 12 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Artesunate (drug)]] 5 µM: 0.753× (z -4.5, q 0.004, down in 10 of 18 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAALC]] (+0.56, fdr 3e-05), [[GPNMB]] (+0.55, fdr 2e-05), [[SGCD]] (+0.54, fdr 6e-05); moves opposite to [[ERI1]] (-0.41, fdr 1e-04), [[ANKRD20A1]] (-0.40, fdr 6e-04), [[IL19]] (-0.39, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[RALYL]] → it (grade B ⚠); 28 go from it, the strongest it → [[SEMA6D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4275.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.02×** | +17.5 | 0e+00 | 12/17 (SW1417, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.79×** | +16.2 | 0e+00 | 18/18 (SW1417, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +12.0 | 9e-31 | 7/17 (SW1417, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.07×** | +11.5 | 1e-28 | 15/18 (SW1417, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.77×** | +10.6 | 5e-24 | 0/13 | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.17×** | +8.6 | 5e-16 | 14/18 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.03×** | +7.9 | 2e-13 | 1/15 (HEC-1-A) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.90×** | +7.2 | 4e-11 | 16/18 (SW1417, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +6.3 | 1e-08 | 0/13 | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.77×** | +6.1 | 5e-08 | 4/15 (SK-MEL-2, SNU-423, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +6.0 | 9e-08 | 14/17 (H4, SW1417, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.75×** | +5.9 | 2e-07 | 6/17 (SK-MEL-2, SW1417, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.69×** | +5.9 | 2e-07 | 9/18 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.67×** | +5.7 | 4e-07 | 14/18 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.6 | 8e-07 | 4/17 (SW1417, HT-29, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.61×** | +5.3 | 3e-06 | 14/18 (SW480, HT-29, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **2.17×** | +4.5 | 2e-04 | 7/17 (RPMI-7951, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.001 | 7/18 (BT-474, RPMI-7951, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.42×** | +3.9 | 0.003 | 5/17 (BT-474, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4275.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **0.753×** | -4.5 | 0.004 | 10/18 (SHP-77, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.709×** | -3.9 | 0.033 | 9/17 (SHP-77, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.726×** | -3.6 | 0.061 | 7/18 (HS-578T, H4, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.740× | -3.4 | 0.11 | 5/16 (HT-29, CHP-212, …) | rises with dose |  |
| [[Futibatinib (drug)]] 0.05 µM |  | 0.749× | -3.1 | 0.23 | 1/17 (H4) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.763× | -3.0 | 0.23 | 9/18 (SHP-77, CHP-212, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4275. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 17.2 | 7 (2 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 16.5× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.130× (z -9.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 80.3 | 4 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.92× (z +10.6) | — |
| [[SW480 (line)]] | alt | 8.70 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 9.75× (z +17.8) | — |
| [[SNU-1 (line)]] | wt | 26.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0636× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.0743× (z -9.3) |
| [[SNU-423 (line)]] | alt | 8.47 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 14.7× (z +13.6) | — |
| [[BT-474 (line)]] | alt | 46.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +9.6) | — |
| [[C32 (line)]] | wt | 113 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.35× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 53.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 10.1× (z +12.2) ⚠ unreliable plate only | — |
| [[HT-29 (line)]] | alt | 27.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.44× (z +8.6) | — |
| [[A-172 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 231 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 128 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.05 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4275), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAALC]] | +0.56 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[GPNMB]] | +0.55 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[SGCD]] | +0.54 | +0.56 / +0.39 | both halves | 6e-05 |  |
| [[OFCC1]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[LDB2]] | +0.54 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[CASC15]] | +0.53 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[LINC01695]] | +0.52 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[CACNB2]] | +0.52 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[RALYL]] | +0.51 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[DMD]] | +0.51 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[DCT]] | +0.51 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[KCNE4]] | +0.50 | +0.44 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERI1]] | -0.41 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[ANKRD20A1]] | -0.40 | -0.22 / -0.27 | both halves | 6e-04 | STRING 601 |
| [[IL19]] | -0.39 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[PPP1R16A]] | -0.38 | -0.31 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 5, C 17. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RALYL]] | B | RALYL activity raises PDZRN3's level | lines that do not express RALYL (17) vs lines expressing it (33) | 3.50× lower at baseline in the lines without RALYL | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |
| [[TEX41]] | B | TEX41 activity raises PDZRN3's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 2.03× lower at baseline in the lines without TEX41 | 0.031 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12 |
| [[TOP2A]] | B | TOP2A activity lowers PDZRN3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SOX5]] | B | SOX5 activity raises PDZRN3's level | lines that do not express SOX5 (24) vs lines expressing it (26) | 2.61× lower at baseline in the lines without SOX5 | 0.089 | ⚠ within organs, on part of the lines; also absent: CTHRC1, MOXD1, AK5 |
| [[PLXDC2]] | B | PLXDC2 activity raises PDZRN3's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 2.39× lower at baseline in the lines without PLXDC2 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent |
| [[HGF]] | C | HGF activity raises PDZRN3's level | lines that do not express HGF (38) vs lines expressing it (12) | 5.11× lower at baseline in the lines without HGF | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; co-absent with the target |
| [[PRUNE2]] | C | PRUNE2 activity raises PDZRN3's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 5.10× lower at baseline in the lines without PRUNE2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY; co-absent with the target |
| [[BAALC]] | C | BAALC activity raises PDZRN3's level | lines that do not express BAALC (32) vs lines expressing it (18) | 3.55× lower at baseline in the lines without BAALC | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent; co-absent with the target |
| [[GPNMB]] | C | GPNMB activity raises PDZRN3's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 4.04× lower at baseline in the lines without GPNMB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6; co-absent with the target |
| [[DCT]] | C | DCT activity raises PDZRN3's level | lines that do not express DCT (42) vs lines expressing it (8) | 5.35× lower at baseline in the lines without DCT | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1; co-absent with the target |
| [[PGR]] | C | PGR activity raises PDZRN3's level | lines that do not express PGR (36) vs lines expressing it (14) | 4.28× lower at baseline in the lines without PGR | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises PDZRN3's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 4.57× lower at baseline in the lines without KCNE4 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 13, C 15. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6D]] | B | PDZRN3 activity raises SEMA6D's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 2.18× lower at baseline in the lines without PDZRN3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[CFAP20DC-DT]] | B | PDZRN3 activity raises CFAP20DC-DT's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 1.67× lower at baseline in the lines without PDZRN3 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[GNG2]] | B | PDZRN3 activity raises GNG2's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 3.60× lower at baseline in the lines without PDZRN3 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[OFCC1]] | B | PDZRN3 activity raises OFCC1's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 1.96× lower at baseline in the lines without PDZRN3 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[RALYL]] | B | PDZRN3 activity raises RALYL's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 1.75× lower at baseline in the lines without PDZRN3 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[LDB2]] | B | PDZRN3 activity raises LDB2's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 2.54× lower at baseline in the lines without PDZRN3 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[VENTXP1]] | B | PDZRN3 activity raises VENTXP1's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 1.61× lower at baseline in the lines without PDZRN3 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[MAP1A]] | B | PDZRN3 activity raises MAP1A's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 1.89× lower at baseline in the lines without PDZRN3 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[PKNOX2]] | B | PDZRN3 activity raises PKNOX2's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 1.83× lower at baseline in the lines without PDZRN3 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[ANO3]] | B | PDZRN3 activity raises ANO3's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 1.63× lower at baseline in the lines without PDZRN3 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[RFTN2]] | B | PDZRN3 activity raises RFTN2's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 1.45× lower at baseline in the lines without PDZRN3 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| cells under [[Ixazomib citrate (drug)]] 5 µM | B | PDZRN3 activity lowers the cells' numbers under Ixazomib citrate 5 µM (makes them more sensitive) | lines that do not express PDZRN3 (30) vs lines expressing it (18) | the lines without PDZRN3: 1.32× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.484). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.1, 31.3); signed map (46.0, 29.6). **Vector** length 55.7, 14.6% of its response variance represented; |z| ≥ 3 in 534 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +16.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.7 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +17.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +8.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +3.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | +1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | PDZ domain containing ring finger 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p13 — chr3:73,382,431-73,624,941 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1095, SEMACAP3, LNX3, SEMCAP3 |
| Gene groups (HGNC) | Ring finger proteins; PDZ domain containing; Zinc fingers TRAF-type; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPQ7](https://www.uniprot.org/uniprotkb/Q9UPQ7) (E3 ubiquitin-protein ligase PDZRN3):

> E3 ubiquitin-protein ligase. Plays an important role in regulating the surface level of MUSK on myotubes. Mediates the ubiquitination of MUSK, promoting its endocytosis and lysosomal degradation. Might contribute to terminal myogenic differentiation.

**Summary**, from NCBI Gene [23024](https://www.ncbi.nlm.nih.gov/gene/23024):

> This gene encodes a member of the LNX (Ligand of Numb Protein-X) family of RING-type ubiquitin E3 ligases. This protein may function in vascular morphogenesis and the differentiation of adipocytes, osteoblasts and myoblasts. This protein may be targeted for degradation by the human papilloma virus E6 protein. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:17704](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17704) · Entrez [23024](https://www.ncbi.nlm.nih.gov/gene/23024) · UniProt [Q9UPQ7](https://www.uniprot.org/uniprotkb/Q9UPQ7) · Ensembl [ENSG00000121440](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121440)

## Data

Gene col 4275: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4275); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4275, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4275]; `tensor/DDL_lfc|DDL_z.npy` [4275]; `embed/gene_vectors.npy` [4275]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4275 or target_col == 4275). Every well: [[PDZRN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDZRN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

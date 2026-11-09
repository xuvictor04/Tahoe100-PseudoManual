---
symbol: "KCNK2"
type: "gene"
col: 1348
ensembl_id: "ENSG00000082482"
name: "potassium two pore domain channel subfamily K member 2"
location: "1q41"
module: 19
arm: "+"
pooled_cpm: 3.63
n_lines_expressing: 23
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 31
direction_downstream: 10
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# KCNK2

*potassium two pore domain channel subfamily K member 2* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.94× (z +17.8, q 0e+00, up in 7 of 12 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.105×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.117×); [[Daptomycin (drug)]] 5 µM in 1 line (CHP-212 0.0457×; ⚠ unreliable plate only); [[Trametinib (drug)]] 5 µM in 1 line (NCI-H460 0.142×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GREM2]] (+0.88, fdr 7e-06), [[FENDRR]] (+0.84, fdr 7e-06), [[CHL1]] (+0.83, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 31 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 10 go from it, the strongest it → [[LINC00922]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1348.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.94×** | +17.8 | 0e+00 | 7/12 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.83×** | +11.6 | 1e-28 | 8/14 (J82, C32, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.02×** | +11.0 | 9e-26 | 1/5 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.92×** | +10.4 | 5e-23 | 1/3 (hTERT-HPNE) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.11×** | +8.3 | 1e-14 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.73×** | +7.9 | 2e-13 | 7/17 (NCI-H1792, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +5.9 | 3e-07 | 3/14 (SNU-423, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.10×** | +5.9 | 3e-07 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.65×** | +5.6 | 1e-06 | 3/18 (hTERT-HPNE, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +5.2 | 1e-05 | 4/13 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +4.9 | 4e-05 | 1/9 (NCI-H1792) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +4.9 | 5e-05 | 3/16 (SW 900, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +4.6 | 2e-04 | 8/17 (C32, NCI-H1573, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +4.5 | 3e-04 | 2/7 (A-427, SK-MEL-2) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.73×** | +4.1 | 0.001 | 0/4 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1348.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.105×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.117×); [[Daptomycin (drug)]] 5 µM in 1 line (CHP-212 0.0457×; ⚠ unreliable plate only); [[Trametinib (drug)]] 5 µM in 1 line (NCI-H460 0.142×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | 0.653× | -3.2 | 0.73 | 7/18 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1348. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 43.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -15.6) |
| [[CHP-212 (line)]] | wt | 52.6 | 0 | 3 (3 ⚠) | — | [[Daptomycin (drug)]] 5 µM 0.0457× (z -10.5) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0727× (z -8.6) ⚠ cell-cycle shift, explains ~22% of this change |
| [[A-172 (line)]] | wt | 0.779 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.579 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.819 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.931 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.843 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.735 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.780 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.779 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.993 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.597 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.961 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.724 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.770 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.648 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.560 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.642 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.661 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.835 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.624 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1348), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GREM2]] | +0.88 | +0.86 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[FENDRR]] | +0.84 | +0.73 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[CHL1]] | +0.83 | +0.74 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[LINC03000]] | +0.81 | +0.80 / +0.74 | both halves | 7e-06 |  |
| [[COL4A6]] | +0.80 | +0.81 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[DPP10]] | +0.80 | +0.74 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[ADGRD1]] | +0.80 | +0.76 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[LINC01035]] | +0.80 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[SCARA5]] | +0.79 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[CTNND2]] | +0.78 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[NCKAP5-AS2]] | +0.77 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[LIN7A]] | +0.77 | +0.71 / +0.73 | both halves | 7e-06 | pathway: Neuronal System |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 6, C 25. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KCNK2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TTTY14]] | B | TTTY14 activity raises KCNK2's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 1.74× lower at baseline in the lines without TTTY14 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY |
| [[TTTY10]] | B | TTTY10 activity raises KCNK2's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 1.87× lower at baseline in the lines without TTTY10 | 0.052 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY |
| [[UTY]] | B | UTY activity raises KCNK2's level | lines that do not express UTY (31) vs lines expressing it (19) | 1.90× lower at baseline in the lines without UTY | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY |
| [[TXLNGY]] | B | TXLNGY activity raises KCNK2's level | lines that do not express TXLNGY (30) vs lines expressing it (20) | 1.82× lower at baseline in the lines without TXLNGY | 0.065 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |
| [[SOX6]] | B | SOX6 activity raises KCNK2's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 1.70× lower at baseline in the lines without SOX6 | 0.075 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[PAPPA2]] | C | PAPPA2 activity raises KCNK2's level | lines that do not express PAPPA2 (28) vs lines expressing it (22) | 2.32× lower at baseline in the lines without PAPPA2 | 0.006 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises KCNK2's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 2.36× lower at baseline in the lines without KCNE4 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[GREM2]] | C | GREM2 activity raises KCNK2's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 3.07× lower at baseline in the lines without GREM2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[SLC7A2]] | C | SLC7A2 activity raises KCNK2's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 2.00× lower at baseline in the lines without SLC7A2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D; co-absent with the target |
| [[PDE1A]] | C | PDE1A activity raises KCNK2's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 2.10× lower at baseline in the lines without PDE1A | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |
| [[GSG1L2]] | C | GSG1L2 activity raises KCNK2's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 2.73× lower at baseline in the lines without GSG1L2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00922]] | B | KCNK2 activity raises LINC00922's level | lines that do not express KCNK2 (27) vs lines expressing it (23) | 1.89× lower at baseline in the lines without KCNK2 | 0.054 | ⚠ within organs, on part of the lines; also absent: KC6, EDNRB, PAPPA2; maybe low, not absent |
| [[KIAA0825]] | B | KCNK2 activity raises KIAA0825's level | lines that do not express KCNK2 (27) vs lines expressing it (23) | 2.15× lower at baseline in the lines without KCNK2 | 0.080 | ⚠ within organs, on part of the lines; also absent: KC6, EDNRB, PAPPA2; maybe low, not absent |
| [[ANO3]] | B | KCNK2 activity weakens ANO3's drug response | lines that do not express KCNK2 (25) vs lines expressing it (18) | the lines without KCNK2 respond 3.77× as strongly (z diff -1.30); strongest at Homoharringtonine 5 µM: 2.55x vs 0.70x (z diff -5.5) | 0.081 | ⚠ within organs, on part of the lines; also absent: KC6, EDNRB, PAPPA2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CACNB2]] | C | KCNK2 activity raises CACNB2's level | lines that do not express KCNK2 (27) vs lines expressing it (23) | 2.53× lower at baseline in the lines without KCNK2 | 0.013 | ⚠ within organs, on part of the lines; also absent: KC6, EDNRB, PAPPA2; maybe low, not absent; co-absent with the target |
| [[LSAMP]] | C | KCNK2 activity raises LSAMP's level | lines that do not express KCNK2 (27) vs lines expressing it (23) | 3.31× lower at baseline in the lines without KCNK2 | 0.015 | ⚠ within organs, on part of the lines; also absent: KC6, EDNRB, PAPPA2; maybe low, not absent; co-absent with the target |
| [[KCNE4]] | C | KCNK2 activity raises KCNE4's level | lines that do not express KCNK2 (27) vs lines expressing it (23) | 3.78× lower at baseline in the lines without KCNK2 | 0.015 | ⚠ within organs, on part of the lines; also absent: KC6, EDNRB, PAPPA2; maybe low, not absent; co-absent with the target |
| [[PAK3]] | C | KCNK2 activity raises PAK3's level | lines that do not express KCNK2 (27) vs lines expressing it (23) | 2.86× lower at baseline in the lines without KCNK2 | 0.018 | ⚠ within organs, on part of the lines; also absent: KC6, EDNRB, PAPPA2; maybe low, not absent; co-absent with the target |
| [[TCF4]] | C | KCNK2 activity raises TCF4's level | lines that do not express KCNK2 (27) vs lines expressing it (23) | 4.49× lower at baseline in the lines without KCNK2 | 0.019 | ⚠ within organs, on part of the lines; also absent: KC6, EDNRB, PAPPA2; maybe low, not absent; co-absent with the target |
| [[CDH11]] | C | KCNK2 activity raises CDH11's level | lines that do not express KCNK2 (27) vs lines expressing it (23) | 2.19× lower at baseline in the lines without KCNK2 | 0.060 | ⚠ within organs, on part of the lines; also absent: KC6, EDNRB, PAPPA2; maybe low, not absent; co-absent with the target |
| [[RTN1]] | C | KCNK2 activity raises RTN1's level | lines that do not express KCNK2 (27) vs lines expressing it (23) | 2.20× lower at baseline in the lines without KCNK2 | 0.098 | ⚠ within organs, on part of the lines; also absent: KC6, EDNRB, PAPPA2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.849). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.3, 36.1); signed map (42.8, 44.2). **Vector** length 44.5, 11.2% of its response variance represented; |z| ≥ 3 in 457 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +11.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +17.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +5.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +1.7 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -1.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -3.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -1.2 | -1.2 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | potassium two pore domain channel subfamily K member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:215,005,775-215,237,090 (+) |
| Ensembl biotype | protein_coding |
| Also known as | K2p2.1, TREK-1 |
| Gene groups (HGNC) | Potassium two pore domain channel subfamily K |
| Reactome | 6 pathways, smallest: Tandem pore domain potassium channels; Phase 4 - resting membrane potential; Potassium Channels |
| Matched by | ensembl_id |

**Function**, from UniProt [O95069](https://www.uniprot.org/uniprotkb/O95069) (Potassium channel subfamily K member 2):

> K(+) channel that conducts voltage-dependent outward rectifying currents upon membrane depolarization. Voltage sensing is coupled to K(+) electrochemical gradient in an 'ion flux gating' mode where outward but not inward ion flow opens the gate. Converts to voltage-independent 'leak' conductance mode upon stimulation by various stimuli including mechanical membrane stretch, acidic pH, heat and lipids. Reversibly converts between a voltage-insensitive K(+) 'leak' channel and a voltage-dependent …

**Summary**, from NCBI Gene [3776](https://www.ncbi.nlm.nih.gov/gene/3776):

> This gene encodes one of the members of the two-pore-domain background potassium channel protein family. This type of potassium channel is formed by two homodimers that create a channel that leaks potassium out of the cell to control resting membrane potential. The channel can be opened, however, by certain anesthetics, membrane stretching, intracellular acidosis, and heat. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6277](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6277) · Entrez [3776](https://www.ncbi.nlm.nih.gov/gene/3776) · UniProt [O95069](https://www.uniprot.org/uniprotkb/O95069) · Ensembl [ENSG00000082482](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082482)

## Data

Gene col 1348: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1348); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1348, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1348]; `tensor/DDL_lfc|DDL_z.npy` [1348]; `embed/gene_vectors.npy` [1348]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1348 or target_col == 1348). Every well: [[KCNK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

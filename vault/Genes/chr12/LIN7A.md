---
symbol: "LIN7A"
type: "gene"
col: 3189
ensembl_id: "ENSG00000111052"
name: "lin-7 cell polarity scaffold A"
location: "12q21.31"
module: 19
arm: "+"
pooled_cpm: 12.64
n_lines_expressing: 16
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 10
direction_downstream: 22
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# LIN7A

*lin-7 cell polarity scaffold A* — 12q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.96× (z +12.4, q 2e-32, up in 2 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.03× (z +11.4, q 8e-28, up in 5 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.688× (z -3.9, q 0.047, down in 1 of 13 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 9 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (SHP-77 0.133×, NCI-H460 0.186×; ⚠ cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.143×, NCI-H460 0.226×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.202×, A-427 0.114×; ⚠ cell-cycle shift, explains ~32% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.0701×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.136×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.167×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01035]] (+0.81, fdr 7e-06), [[GREM2]] (+0.79, fdr 7e-06), [[PAX7]] (+0.78, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 22 go from it, the strongest it → [[MTMR7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3189.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.96×** | +12.4 | 2e-32 | 2/9 (A549, A-427) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +11.4 | 8e-28 | 5/10 (A549, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.82×** | +11.4 | 9e-28 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.92×** | +10.6 | 6e-24 | 6/13 (HEC-1-A, C32, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +7.6 | 4e-12 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +6.7 | 3e-09 | 5/11 (BT-474, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +6.2 | 5e-08 | 4/9 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +5.5 | 2e-06 | 5/11 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +4.5 | 5e-04 | 1/12 (C32) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +4.1 | 0.002 | 5/12 (hTERT-HPNE, C32, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +4.0 | 0.003 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.0 | 0.003 | 1/12 (BT-474) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.38×** | +3.6 | 0.011 | 5/13 (BT-474, HepG2/C3A, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.011 | 4/14 (hTERT-HPNE, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.25×** | +3.6 | 0.012 | 2/11 (BT-474, HepG2/C3A) | top dose only | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.012 | 2/11 (hTERT-HPNE, HEC-1-A) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.014 | 2/12 (HEC-1-A, A549) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.014 | 0/12 | top dose only | cell-cycle shift (explains ~10% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.54×** | +3.5 | 0.014 | 1/11 (C32) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.076 | 2/11 (A-427, BT-474) | inconsistent across doses |  |
| [[Silodosin (drug)]] 5 µM |  | **1.30×** | +2.9 | 0.099 | 1/11 (A549) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3189.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 9 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (SHP-77 0.133×, NCI-H460 0.186×; ⚠ cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.143×, NCI-H460 0.226×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.202×, A-427 0.114×; ⚠ cell-cycle shift, explains ~32% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.0701×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.136×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.167×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.688×** | -3.9 | 0.047 | 1/13 (AN3 CA) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.729×** | -3.6 | 0.068 | 7/13 (BT-474, NCI-H460, …) | rises with dose | position effect removed |
| [[Ivermectin (drug)]] 5 µM |  | **0.731×** | -3.6 | 0.068 | 1/13 (AN3 CA) | rises with dose |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.726× | -3.4 | 0.11 | 0/12 | inconsistent across doses |  |
| [[Volasertib (drug)]] 0.5 µM |  | 0.671× | -3.2 | 0.13 | 0/14 | inconsistent across doses | noisy plate (z scaled) |
| [[Delamanid (drug)]] 5 µM |  | 0.758× | -3.1 | 0.15 | 1/13 (AN3 CA) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | 0.765× | -3.0 | 0.19 | 0/13 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3189. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 119 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -17.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H460 (line)]] | wt | 109 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -13.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 21.4 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0701× (z -14.7) |
| [[HepG2_C3A (line)]] | wt | 40.5 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.167× (z -9.3) |
| [[A-172 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.88 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3189), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01035]] | +0.81 | +0.71 / +0.82 | both halves | 7e-06 |  |
| [[GREM2]] | +0.79 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[PAX7]] | +0.78 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[CHL1]] | +0.78 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[LINC03000]] | +0.78 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[ADGRD1]] | +0.77 | +0.64 / +0.79 | both halves | 7e-06 |  |
| [[KCNK2]] | +0.77 | +0.71 / +0.73 | both halves | 7e-06 | pathway: Neuronal System |
| [[RTN1]] | +0.76 | +0.67 / +0.76 | both halves | 7e-06 | same gene group |
| [[NCKAP5-AS2]] | +0.75 | +0.72 / +0.58 | both halves | 8e-06 |  |
| [[SCARA5]] | +0.74 | +0.71 / +0.69 | both halves | 7e-06 | same gene group |
| [[SLC15A5]] | +0.73 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[DPP10]] | +0.73 | +0.56 / +0.81 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LIN7A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01508]] | C | LINC01508 activity raises LIN7A's level | lines that do not express LINC01508 (42) vs lines expressing it (8) | 3.47× lower at baseline in the lines without LINC01508 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SPINK13, RHEX; co-absent with the target |
| [[NRCAM]] | C | NRCAM activity raises LIN7A's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 3.65× lower at baseline in the lines without NRCAM | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG; co-absent with the target |
| [[TTTY10]] | C | TTTY10 activity raises LIN7A's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 1.97× lower at baseline in the lines without TTTY10 | 0.046 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |
| [[GASK1B]] | C | GASK1B activity raises LIN7A's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 2.06× lower at baseline in the lines without GASK1B | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054; co-absent with the target |
| [[SMOC1]] | C | SMOC1 activity raises LIN7A's level | lines that do not express SMOC1 (34) vs lines expressing it (16) | 2.55× lower at baseline in the lines without SMOC1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CPLX2, LGSN, CYP24A1; co-absent with the target |
| [[SLC7A2]] | C | SLC7A2 activity raises LIN7A's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 3.20× lower at baseline in the lines without SLC7A2 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D; co-absent with the target |
| [[ACSS3]] | C | ACSS3 activity raises LIN7A's level | lines that do not express ACSS3 (31) vs lines expressing it (19) | 2.74× lower at baseline in the lines without ACSS3 | 0.074 | ⚠ within organs, on part of the lines; also absent: NTNG1, ENSG00000289884, HOPX; co-absent with the target |
| [[SOX6]] | C | SOX6 activity raises LIN7A's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 1.98× lower at baseline in the lines without SOX6 | 0.079 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises LIN7A's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 4.24× lower at baseline in the lines without DPP10 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 3, C 19. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTMR7]] | B | LIN7A activity raises MTMR7's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 2.33× lower at baseline in the lines without LIN7A | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1 |
| [[ELMO1]] | B | LIN7A activity raises ELMO1's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 3.13× lower at baseline in the lines without LIN7A | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1 |
| cells under [[Glycyrrhizic acid (drug)]] 0.05 µM | B | LIN7A activity lowers the cells' numbers under Glycyrrhizic acid 0.05 µM (makes them more sensitive) | lines that do not express LIN7A (34) vs lines expressing it (14) | the lines without LIN7A: 1.16× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1 |
| [[SLC7A2]] | C | LIN7A activity raises SLC7A2's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 4.71× lower at baseline in the lines without LIN7A | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |
| [[GABBR2]] | C | LIN7A activity raises GABBR2's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 2.35× lower at baseline in the lines without LIN7A | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |
| [[TTTY10]] | C | LIN7A activity raises TTTY10's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 3.28× lower at baseline in the lines without LIN7A | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |
| [[NCKAP5-AS2]] | C | LIN7A activity raises NCKAP5-AS2's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 1.93× lower at baseline in the lines without LIN7A | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |
| [[CDH19]] | C | LIN7A activity raises CDH19's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 2.61× lower at baseline in the lines without LIN7A | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |
| [[KCNK2]] | C | LIN7A activity raises KCNK2's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 2.28× lower at baseline in the lines without LIN7A | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |
| [[GPRIN3]] | C | LIN7A activity raises GPRIN3's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 2.59× lower at baseline in the lines without LIN7A | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |
| [[NRCAM]] | C | LIN7A activity raises NRCAM's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 2.98× lower at baseline in the lines without LIN7A | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |
| [[LAMB4]] | C | LIN7A activity raises LAMB4's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 1.73× lower at baseline in the lines without LIN7A | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.785). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.0, 36.5); signed map (43.3, 44.1). **Vector** length 43.0, 13.8% of its response variance represented; |z| ≥ 3 in 303 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +12.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +10.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +4.5 |
| fall | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -2.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -3.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | lin-7 cell polarity scaffold A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.31 — chr12:80,792,520-80,937,934 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MALS-1, TIP-33, LIN-7A, VELI1 |
| Gene groups (HGNC) | PDZ domain containing; Crumbs complex components; MicroRNA protein coding host genes |
| Reactome | 9 pathways, smallest: Dopamine Neurotransmitter Release Cycle; Assembly and cell surface presentation of NMDA receptors; Neurotransmitter release cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O14910](https://www.uniprot.org/uniprotkb/O14910) (Protein lin-7 homolog A):

> Plays a role in establishing and maintaining the asymmetric distribution of channels and receptors at the plasma membrane of polarized cells. Forms membrane-associated multiprotein complexes that may regulate delivery and recycling of proteins to the correct membrane domains. The tripartite complex composed of LIN7 (LIN7A, LIN7B or LIN7C), CASK and APBA1 associates with the motor protein KIF17 to transport vesicles containing N-methyl-D-aspartate (NMDA) receptor subunit NR2B along microtubules …

**Summary**, from NCBI Gene [8825](https://www.ncbi.nlm.nih.gov/gene/8825):

> The protein encoded by this gene is involved in generating and maintaining the asymmetric distribution of channels and receptors at the cell membrane. The encoded protein also is required for the localization of some specific channels and can be part of a protein complex that couples synaptic vesicle exocytosis to cell adhesion in the brain. [provided by RefSeq, May 2016]

**Accessions** — [HGNC:17787](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17787) · Entrez [8825](https://www.ncbi.nlm.nih.gov/gene/8825) · UniProt [O14910](https://www.uniprot.org/uniprotkb/O14910) · Ensembl [ENSG00000111052](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111052)

## Data

Gene col 3189: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3189); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3189, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3189]; `tensor/DDL_lfc|DDL_z.npy` [3189]; `embed/gene_vectors.npy` [3189]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3189 or target_col == 3189). Every well: [[LIN7A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIN7A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

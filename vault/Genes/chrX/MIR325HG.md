---
symbol: "MIR325HG"
type: "gene"
col: 15970
ensembl_id: "ENSG00000280870"
name: "MIR325 host gene"
location: "Xq13.3-q21.1"
module: 90
arm: "+"
pooled_cpm: 2.29
n_lines_expressing: 48
n_dd_up: 40
n_dd_down: 0
n_dd_up_clean: 31
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# MIR325HG

*MIR325 host gene* — Xq13.3-q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.24× (z +14.9, q 0e+00, up in 28 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[EX229 (drug)]] 0.05 µM in 1 line (SHP-77 0.118×); [[Ipatasertib (drug)]] 0.05 µM in 1 line (Hs 766T 0.0377×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.144×; ⚠ cell-cycle shift, explains ~3% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XKR4]] (+0.74, fdr 7e-06), [[UNC80]] (+0.71, fdr 7e-06), [[LUZP2]] (+0.70, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15970.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.24×** | +14.9 | 0e+00 | 28/36 (SW480, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.22×** | +14.9 | 0e+00 | 21/23 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.05×** | +12.7 | 1e-34 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.29×** | +12.3 | 1e-32 | 11/18 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.12×** | +12.0 | 7e-31 | 5/9 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.64×** | +10.4 | 2e-23 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.86×** | +7.7 | 1e-12 | 16/33 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.83×** | +7.6 | 2e-12 | 17/23 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.26×** | +5.8 | 5e-07 | 13/39 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.18×** | +5.7 | 7e-07 | 8/18 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +5.6 | 1e-06 | 1/10 (PANC-1) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.70×** | +5.5 | 2e-06 | 4/36 (SW480, NCI-H460, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.89×** | +4.5 | 4e-04 | 7/15 (SW480, Hs 766T, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.83×** | +4.4 | 4e-04 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.80×** | +4.3 | 7e-04 | 12/21 (Hs 766T, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +4.3 | 8e-04 | 7/20 (HT-29, MIA PaCa-2, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.75×** | +4.1 | 0.002 | 6/39 (SHP-77, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.76×** | +4.0 | 0.002 | 7/28 (NCI-H1573, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +3.7 | 0.006 | 5/15 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.46×** | +3.7 | 0.006 | 8/38 (SW480, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15970.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[EX229 (drug)]] 0.05 µM in 1 line (SHP-77 0.118×); [[Ipatasertib (drug)]] 0.05 µM in 1 line (Hs 766T 0.0377×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.144×; ⚠ cell-cycle shift, explains ~3% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.648× | -3.2 | 0.77 | 7/31 (Hs 766T, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15970. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 43.9 | 0 | 2 (1 ⚠) | — | [[EX229 (drug)]] 0.05 µM 0.118× (z -9.8) |
| [[BT-474 (line)]] | alt | 0.928 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.5× (z +8.5) | — |
| [[C32 (line)]] | wt | 0.779 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.5× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 0.941 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.0× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 12.6 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.05 µM 0.0377× (z -9.7) |
| [[HT-29 (line)]] | alt | 2.79 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.0× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 0.876 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 15.1× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 5.65 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.0× (z +10.7) | — |
| [[SW480 (line)]] | alt | 4.14 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 13.4× (z +11.4) | — |
| [[A-172 (line)]] | wt | 0.615 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.569 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.584 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.600 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.753 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.759 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.903 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.839 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.824 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.761 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.582 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.632 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.802 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.647 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.780 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.587 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.773 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.569 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.938 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.579 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.636 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.664 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.924 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.874 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.695 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.789 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.719 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15970), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XKR4]] | +0.74 | +0.62 / +0.81 | both halves | 7e-06 |  |
| [[UNC80]] | +0.71 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[LUZP2]] | +0.70 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[LINC02208]] | +0.70 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[COL21A1]] | +0.69 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[SORCS1]] | +0.69 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[LINC00298]] | +0.69 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[CNTNAP2]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[PLCL1]] | +0.67 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[SLC9C1]] | +0.67 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[SPOCK3]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[LINC02306]] | +0.66 | +0.68 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MIR325HG's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.0% of all compounds | 0.009 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[AGMO]] | B | AGMO activity raises MIR325HG's level | lines that do not express AGMO (30) vs lines expressing it (20) | 1.68× lower at baseline in the lines without AGMO | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657 |
| [[STXBP5L]] | B | STXBP5L activity raises MIR325HG's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 1.63× lower at baseline in the lines without STXBP5L | 0.031 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent |
| [[NRXN1]] | B | NRXN1 activity raises MIR325HG's level | lines that do not express NRXN1 (19) vs lines expressing it (31) | 1.57× lower at baseline in the lines without NRXN1 | 0.044 | ⚠ within organs, on part of the lines; also absent: CHRM3, MIR2052HG, ENSG00000265994; maybe low, not absent |
| [[DACH1]] | B | DACH1 activity raises MIR325HG's level | lines that do not express DACH1 (30) vs lines expressing it (20) | 1.63× lower at baseline in the lines without DACH1 | 0.044 | ⚠ within organs, on part of the lines; also absent: FGF20, CSMD3, XKR7 |
| [[LINC02466]] | B | LINC02466 activity raises MIR325HG's level | lines that do not express LINC02466 (21) vs lines expressing it (29) | 1.62× lower at baseline in the lines without LINC02466 | 0.050 | ⚠ within organs, on part of the lines; also absent: MME, ENSG00000227088, GABRA3; maybe low, not absent |
| [[CDH6]] | B | CDH6 activity raises MIR325HG's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 1.49× lower at baseline in the lines without CDH6 | 0.053 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC |
| [[AFF2]] | B | AFF2 activity raises MIR325HG's level | lines that do not express AFF2 (25) vs lines expressing it (25) | 1.56× lower at baseline in the lines without AFF2 | 0.054 | ⚠ within organs, on part of the lines; also absent: KIF1A, TMEM163, LINC02315; maybe low, not absent |
| [[SIM1]] | B | SIM1 activity raises MIR325HG's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 1.90× lower at baseline in the lines without SIM1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5 |
| [[HTR2C]] | B | HTR2C activity raises MIR325HG's level | lines that do not express HTR2C (22) vs lines expressing it (28) | 1.54× lower at baseline in the lines without HTR2C | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, KCNJ6, PTPRN; maybe low, not absent |
| [[PRUNE2]] | B | PRUNE2 activity raises MIR325HG's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 1.38× lower at baseline in the lines without PRUNE2 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY |
| [[GPR158]] | B | GPR158 activity raises MIR325HG's level | lines that do not express GPR158 (20) vs lines expressing it (30) | 1.55× lower at baseline in the lines without GPR158 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000259929, P2RX7, LINC02968 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.756). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.5, 30.0); signed map (34.6, 17.4). **Vector** length 46.9, 7.75% of its response variance represented; |z| ≥ 3 in 841 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +14.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +7.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +14.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +12.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +5.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +3.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -3.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.1 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.1 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | MIR325 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xq13.3-q21.1 — chrX:76,656,866-77,014,532 (-) |
| Ensembl biotype | lncRNA |
| Also known as | MIR384HG |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50346](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50346) · Entrez [101928469](https://www.ncbi.nlm.nih.gov/gene/101928469) · Ensembl [ENSG00000280870](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000280870)

## Data

Gene col 15970: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15970); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15970, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15970]; `tensor/DDL_lfc|DDL_z.npy` [15970]; `embed/gene_vectors.npy` [15970]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15970 or target_col == 15970). Every well: [[MIR325HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR325HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "BASP1-AS1"
type: "gene"
col: 13252
ensembl_id: "ENSG00000215196"
name: "BASP1 antisense RNA 1"
location: "5p15.1"
module: 19
arm: "+"
pooled_cpm: 12.72
n_lines_expressing: 22
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 18
direction_downstream: 8
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# BASP1-AS1

*BASP1 antisense RNA 1* — 5p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.64× (z +15.8, q 0e+00, up in 12 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.626× (z -5.4, q 3e-05, down in 12 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LGSN]] (+0.66, fdr 1e-05), [[P3H2-AS1]] (+0.61, fdr 1e-05), [[HORMAD1]] (+0.61, fdr 2e-05); moves opposite to [[ATP10B]] (-0.45, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[CYP1B1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13252.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +15.8 | 0e+00 | 12/19 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.29×** | +12.7 | 2e-34 | 1/12 (CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.01×** | +12.2 | 4e-32 | 1/11 (NCI-H1792) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +10.8 | 5e-25 | 3/13 (CFPAC-1, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +7.3 | 4e-11 | 11/20 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.4 | 1e-08 | 12/20 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +5.3 | 1e-05 | 12/19 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +4.3 | 0.001 | 1/20 (NCI-H460) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +3.9 | 0.006 | 0/15 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.006 | 8/18 (H4, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.039 | 1/18 (SW 900) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13252.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.626×** | -5.4 | 3e-05 | 12/19 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.635×** | -5.3 | 4e-05 | 14/19 (A549, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.695×** | -4.2 | 0.005 | 8/19 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.698×** | -4.1 | 0.006 | 8/19 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.731×** | -3.6 | 0.030 | 13/19 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.715×** | -3.6 | 0.030 | 6/18 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.743×** | -3.5 | 0.044 | 13/19 (PANC-1, HOP62, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.754×** | -3.3 | 0.072 | 8/19 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.762× | -3.2 | 0.10 | 11/19 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.830× | -3.1 | 0.12 | 9/20 (NCI-H23, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13252. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 50.2 | 0 | 12 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0533× (z -23.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 59.4 | 1 (1 ⚠) | 8 (6 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.78× (z +13.3) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.255× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 76.3 | 0 | 8 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -18.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 15.4 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.224× (z -10.5) |
| [[HOP62 (line)]] | alt | 31.6 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.162× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0328× (z -15.2) |
| [[NCI-H1792 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0521× (z -13.5) ⚠ cell-cycle shift, explains ~10% of this change |
| [[NCI-H2030 (line)]] | alt | 53.1 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.75× (z +9.2) ⚠ position not correctable | — |
| [[SW 900 (line)]] | alt | 9.44 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0956× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.72 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.59 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13252), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LGSN]] | +0.66 | +0.57 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[P3H2-AS1]] | +0.61 | +0.49 / +0.67 | both halves | 1e-05 | same gene group |
| [[HORMAD1]] | +0.61 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[PPEF1]] | +0.60 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[RASSF8-AS1]] | +0.59 | +0.57 / +0.45 | both halves | 3e-05 | same gene group |
| [[CYP1B1-AS1]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 | same gene group |
| [[UBE2Q2P13]] | +0.58 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[PDE1A]] | +0.57 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[FBXO15]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[BVES-AS1]] | +0.56 | +0.57 / +0.44 | both halves | 3e-05 | same gene group |
| [[EYA2]] | +0.56 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[SLITRK5]] | +0.55 | +0.49 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP10B]] | -0.45 | -0.42 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 5, C 13. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BASP1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LRRC36]] | B | LRRC36 activity raises BASP1-AS1's level | lines that do not express LRRC36 (16) vs lines expressing it (34) | 2.09× lower at baseline in the lines without LRRC36 | 0.052 | ⚠ within organs, on part of the lines; also absent: DANT2, ANKRD20A21P, MTMR8; maybe low, not absent |
| [[CYP1B1-AS1]] | B | CYP1B1-AS1 activity raises BASP1-AS1's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 2.13× lower at baseline in the lines without CYP1B1-AS1 | 0.061 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises BASP1-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers BASP1-AS1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[PAPPA]] | C | PAPPA activity raises BASP1-AS1's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 3.63× lower at baseline in the lines without PAPPA | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[P3H2]] | C | P3H2 activity raises BASP1-AS1's level | lines that do not express P3H2 (28) vs lines expressing it (22) | 2.53× lower at baseline in the lines without P3H2 | 0.037 | ⚠ within organs, on part of the lines; also absent: P3H2-AS1, SRGN, SPOCK1; co-absent with the target |
| [[ODAD2]] | C | ODAD2 activity raises BASP1-AS1's level | lines that do not express ODAD2 (27) vs lines expressing it (23) | 2.65× lower at baseline in the lines without ODAD2 | 0.038 | ⚠ within organs, on part of the lines; also absent: FBN2, NDNF, EPHA5; co-absent with the target |
| [[LRRC63]] | C | LRRC63 activity raises BASP1-AS1's level | lines that do not express LRRC63 (25) vs lines expressing it (25) | 3.37× lower at baseline in the lines without LRRC63 | 0.046 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, STAC, CRLF2; co-absent with the target |
| [[RSPO3]] | C | RSPO3 activity raises BASP1-AS1's level | lines that do not express RSPO3 (39) vs lines expressing it (11) | 4.68× lower at baseline in the lines without RSPO3 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2; co-absent with the target |
| [[BNC2]] | C | BNC2 activity raises BASP1-AS1's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 2.47× lower at baseline in the lines without BNC2 | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182; co-absent with the target |
| [[P3H2-AS1]] | C | P3H2-AS1 activity raises BASP1-AS1's level | lines that do not express P3H2-AS1 (30) vs lines expressing it (20) | 2.55× lower at baseline in the lines without P3H2-AS1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: P3H2, SRGN, KIRREL3; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP1B1-AS1]] | B | BASP1-AS1 activity raises CYP1B1-AS1's level | lines that do not express BASP1-AS1 (28) vs lines expressing it (22) | 2.14× lower at baseline in the lines without BASP1-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LRRC63, FGF14 |
| [[HHAT]] | B | BASP1-AS1 activity raises HHAT's level | lines that do not express BASP1-AS1 (28) vs lines expressing it (22) | 2.07× lower at baseline in the lines without BASP1-AS1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LRRC63, FGF14 |
| [[RMDN2-AS1]] | B | BASP1-AS1 activity raises RMDN2-AS1's level | lines that do not express BASP1-AS1 (28) vs lines expressing it (22) | 2.05× lower at baseline in the lines without BASP1-AS1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LRRC63, FGF14 |
| [[APH1B]] | B | BASP1-AS1 activity raises APH1B's level | lines that do not express BASP1-AS1 (28) vs lines expressing it (22) | 2.40× lower at baseline in the lines without BASP1-AS1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LRRC63, FGF14 |
| [[RASSF8-AS1]] | B | BASP1-AS1 activity raises RASSF8-AS1's level | lines that do not express BASP1-AS1 (28) vs lines expressing it (22) | 2.99× lower at baseline in the lines without BASP1-AS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LRRC63, FGF14 |
| [[GCAWKR]] | C | BASP1-AS1 activity raises GCAWKR's level | lines that do not express BASP1-AS1 (28) vs lines expressing it (22) | 1.83× lower at baseline in the lines without BASP1-AS1 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LRRC63, FGF14; co-absent with the target |
| [[FLRT2]] | C | BASP1-AS1 activity raises FLRT2's level | lines that do not express BASP1-AS1 (28) vs lines expressing it (22) | 5.79× lower at baseline in the lines without BASP1-AS1 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LRRC63, FGF14; co-absent with the target |
| [[PAPPA]] | C | BASP1-AS1 activity raises PAPPA's level | lines that do not express BASP1-AS1 (28) vs lines expressing it (22) | 4.37× lower at baseline in the lines without BASP1-AS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LRRC63, FGF14; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.561). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.7, 37.6); signed map (39.5, 41.9). **Vector** length 70.4, 22.3% of its response variance represented; |z| ≥ 3 in 588 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +15.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +12.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +10.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +1.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +1.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.1 | -5.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -2.0 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -3.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -5.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | +1.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | BASP1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5p15.1 — chr5:17,089,296-17,217,047 (-) |
| Ensembl biotype | lncRNA |
| Also known as | LOC285696 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26609](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26609) · Entrez [285696](https://www.ncbi.nlm.nih.gov/gene/285696) · Ensembl [ENSG00000215196](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215196)

## Data

Gene col 13252: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13252); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13252, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13252]; `tensor/DDL_lfc|DDL_z.npy` [13252]; `embed/gene_vectors.npy` [13252]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13252 or target_col == 13252). Every well: [[BASP1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BASP1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

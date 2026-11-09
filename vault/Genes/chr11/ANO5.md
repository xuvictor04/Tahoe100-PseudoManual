---
symbol: "ANO5"
type: "gene"
col: 10150
ensembl_id: "ENSG00000171714"
name: "anoctamin 5"
location: "11p14.3"
module: 19
arm: "+"
pooled_cpm: 8.68
n_lines_expressing: 25
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 5
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# ANO5

*anoctamin 5* — 11p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.25× (z +21.2, q 0e+00, up in 15 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.681× (z -4.9, q 6e-04, down in 11 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (NCI-H1573 0.126×, NCI-H2030 0.153×, PANC-1 0.243×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A549 0.224×, NCI-H1573 0.332×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0934×); [[Harringtonine (drug)]] 0.5 µM in 1 line (A549 0.182×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LGSN]] (+0.59, fdr 2e-05), [[CHMP1B2P]] (+0.58, fdr 2e-05), [[PDGFD]] (+0.58, fdr 1e-05); moves opposite to [[LINC00412]] (-0.42, fdr 3e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PCDHA6]] → it (grade B ⚠); 5 go from it, the strongest it → [[VAV3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10150.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.25×** | +21.2 | 0e+00 | 15/21 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +13.0 | 4e-36 | 5/17 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.06×** | +12.9 | 6e-36 | 18/22 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.29×** | +9.7 | 4e-20 | 3/14 (NCI-H2030, J82, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +9.4 | 9e-19 | 6/11 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.99×** | +8.7 | 2e-16 | 18/23 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +7.3 | 2e-11 | 15/22 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +7.2 | 3e-11 | 6/21 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.61×** | +6.0 | 1e-07 | 13/22 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +5.9 | 2e-07 | 15/22 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +5.5 | 2e-06 | 9/21 (BT-474, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +5.5 | 2e-06 | 16/23 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.1 | 2e-05 | 3/22 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +4.9 | 3e-05 | 15/22 (NCI-H1792, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +4.9 | 4e-05 | 16/22 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +4.3 | 7e-04 | 4/22 (A-427, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +3.2 | 0.048 | 14/22 (PANC-1, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.18× | +3.0 | 0.077 | 9/22 (H4, J82, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10150.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (NCI-H1573 0.126×, NCI-H2030 0.153×, PANC-1 0.243×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A549 0.224×, NCI-H1573 0.332×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0934×); [[Harringtonine (drug)]] 0.5 µM in 1 line (A549 0.182×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.681×** | -4.9 | 6e-04 | 11/23 (A549, PANC-1, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.698×** | -4.6 | 0.001 | 14/22 (PANC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -4.0 | 0.012 | 4/23 (LS 180, SK-MEL-2, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.768× | -3.4 | 0.11 | 7/22 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.780× | -3.2 | 0.18 | 13/22 (A549, NCI-H1573, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.785× | -3.1 | 0.19 | 15/23 (NCI-H460, PANC-1, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.787× | -3.0 | 0.19 | 15/22 (NCI-H1573, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10150. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.65 | 5 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.88× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.171× (z -11.1) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.229× (z -9.3) |
| [[A549 (line)]] | wt | 62.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 19.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.332× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 6.01 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -9.2) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.195× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 3.02 | 0 | 1 | — | [[Meloxicam (drug)]] 0.5 µM 0.0658× (z -8.7) |
| [[H4 (line)]] | wt | 55.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 2.59 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.05 µM 0.0608× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0934× (z -12.1) |
| [[A-172 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.25 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10150), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LGSN]] | +0.59 | +0.60 / +0.47 | both halves | 2e-05 | **novel candidate** |
| [[CHMP1B2P]] | +0.58 | +0.56 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[PDGFD]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[VAV3]] | +0.58 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[PRKD1]] | +0.57 | +0.57 / +0.58 | both halves | 8e-06 |  |
| [[ASXL3]] | +0.56 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[ADD2]] | +0.56 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[NKAIN3]] | +0.56 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[CNKSR2]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[EBF2]] | +0.55 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[GUCY1B1]] | +0.54 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[NOVA1]] | +0.54 | +0.60 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00412]] | -0.42 | -0.26 / -0.34 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDHA6]] | B | PCDHA6 activity raises ANO5's level | lines that do not express PCDHA6 (17) vs lines expressing it (33) | 2.58× lower at baseline in the lines without PCDHA6 | 0.032 | ⚠ within organs, on part of the lines; also absent: RAB39A, PHF21B, LONRF2 |
| [[TOP2A]] | B | TOP2A activity lowers ANO5's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GUCY1B1]] | B | GUCY1B1 activity raises ANO5's level | lines that do not express GUCY1B1 (25) vs lines expressing it (25) | 1.51× lower at baseline in the lines without GUCY1B1 | 0.093 | ⚠ within organs, on part of the lines; also absent: FAP, STAC, SALL1 |
| [[EBF2]] | B | EBF2 activity raises ANO5's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 1.75× lower at baseline in the lines without EBF2 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[CNKSR2]] | C | CNKSR2 activity raises ANO5's level | lines that do not express CNKSR2 (32) vs lines expressing it (18) | 5.81× lower at baseline in the lines without CNKSR2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CDH10, CDH19; maybe low, not absent; co-absent with the target |
| [[CTNNA2]] | C | CTNNA2 activity raises ANO5's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.55× lower at baseline in the lines without CTNNA2 | 0.061 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7; co-absent with the target |
| [[LINC03046]] | C | LINC03046 activity raises ANO5's level | lines that do not express LINC03046 (38) vs lines expressing it (12) | 3.20× lower at baseline in the lines without LINC03046 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, LINC00824, LINC01205; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VAV3]] | B | ANO5 activity raises VAV3's level | lines that do not express ANO5 (25) vs lines expressing it (25) | 2.49× lower at baseline in the lines without ANO5 | 0.087 | ⚠ within organs, on part of the lines; also absent: CNKSR2, SLC6A15, CNTN1; maybe low, not absent |
| [[KLHL13]] | C | ANO5 activity raises KLHL13's level | lines that do not express ANO5 (25) vs lines expressing it (25) | 2.09× lower at baseline in the lines without ANO5 | 0.049 | ⚠ within organs, on part of the lines; also absent: CNKSR2, SLC6A15, CNTN1; maybe low, not absent; co-absent with the target |
| [[CTNNA2]] | C | ANO5 activity raises CTNNA2's level | lines that do not express ANO5 (25) vs lines expressing it (25) | 2.35× lower at baseline in the lines without ANO5 | 0.049 | ⚠ within organs, on part of the lines; also absent: CNKSR2, SLC6A15, CNTN1; maybe low, not absent; co-absent with the target |
| [[SNCA]] | C | ANO5 activity raises SNCA's level | lines that do not express ANO5 (25) vs lines expressing it (25) | 3.34× lower at baseline in the lines without ANO5 | 0.057 | ⚠ within organs, on part of the lines; also absent: CNKSR2, SLC6A15, CNTN1; maybe low, not absent; co-absent with the target |
| [[CNKSR2]] | C | ANO5 activity raises CNKSR2's level | lines that do not express ANO5 (25) vs lines expressing it (25) | 3.67× lower at baseline in the lines without ANO5 | 0.072 | ⚠ within organs, on part of the lines; also absent: CNKSR2, SLC6A15, CNTN1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.412). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.2, 36.4); signed map (38.6, 36.9). **Vector** length 50.2, 11.4% of its response variance represented; |z| ≥ 3 in 569 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.8 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +12.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +21.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +4.9 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -4.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -4.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | anoctamin 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p14.3 — chr11:21,782,659-22,283,567 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GDD1; previously TMEM16E, LGMD2L |
| Gene groups (HGNC) | Anoctamins |
| Reactome | 11 pathways, smallest: Induction of Cell-Cell Fusion; Regulation of clotting cascade; Coagulation pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q75V66](https://www.uniprot.org/uniprotkb/Q75V66) (Anoctamin-5):

> Plays a role in plasma membrane repair in a process involving annexins. Does not exhibit calcium-activated chloride channel (CaCC) activity.

**Summary**, from NCBI Gene [203859](https://www.ncbi.nlm.nih.gov/gene/203859):

> This gene encodes a member of the anoctamin family of transmembrane proteins. The encoded protein is likely a calcium activated chloride channel. Mutations in this gene have been associated with gnathodiaphyseal dysplasia. Alternatively spliced transcript variants have been described. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:27337](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27337) · Entrez [203859](https://www.ncbi.nlm.nih.gov/gene/203859) · UniProt [Q75V66](https://www.uniprot.org/uniprotkb/Q75V66) · Ensembl [ENSG00000171714](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171714)

## Data

Gene col 10150: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10150); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10150, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10150]; `tensor/DDL_lfc|DDL_z.npy` [10150]; `embed/gene_vectors.npy` [10150]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10150 or target_col == 10150). Every well: [[ANO5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANO5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

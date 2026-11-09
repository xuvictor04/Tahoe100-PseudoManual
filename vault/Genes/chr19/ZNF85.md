---
symbol: "ZNF85"
type: "gene"
col: 2660
ensembl_id: "ENSG00000105750"
name: "zinc finger protein 85"
location: "19p12"
module: 91
arm: "+"
pooled_cpm: 4.01
n_lines_expressing: 33
n_dd_up: 22
n_dd_down: 7
n_dd_up_clean: 19
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 12
direction_downstream: 24
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# ZNF85

*zinc finger protein 85* — 19p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.63× (z +16.7, q 0e+00, up in 23 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.648× (z -5.3, q 6e-05, down in 11 of 30 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C5orf34]] (+0.83, fdr 7e-06), [[ZNF100]] (+0.78, fdr 7e-06), [[ZNF101]] (+0.75, fdr 7e-06); moves opposite to [[ST6GALNAC4]] (-0.65, fdr 3e-05), [[STRAP]] (-0.63, fdr 1e-05), [[SCART1]] (-0.59, fdr 5e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[ZNF681]] → it (grade B ⚠); 24 go from it, the strongest it → [[ZNF442]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2660.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.63×** | +16.7 | 0e+00 | 23/27 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.19×** | +13.6 | 2e-39 | 21/26 (J82, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.32×** | +9.9 | 9e-21 | 19/29 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.73×** | +9.5 | 4e-19 | 15/30 (PANC-1, SNU-423, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +7.9 | 4e-13 | 16/27 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +7.4 | 1e-11 | 10/31 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +7.4 | 1e-11 | 13/22 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +7.2 | 5e-11 | 7/17 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.68×** | +6.4 | 1e-08 | 13/29 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +6.2 | 3e-08 | 9/27 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.51×** | +5.0 | 2e-05 | 7/28 (SHP-77, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.48×** | +4.8 | 8e-05 | 9/31 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +4.6 | 2e-04 | 4/30 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.46×** | +4.6 | 2e-04 | 6/30 (HOP62, HEC-1-A, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +4.3 | 7e-04 | 8/30 (SNU-423, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +4.1 | 0.002 | 8/30 (CFPAC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2660.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.648×** | -5.3 | 6e-05 | 11/30 (PANC-1, C32, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.651×** | -5.1 | 1e-04 | 8/20 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.499×** | -4.5 | 0.002 | 9/29 (SNU-423, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.717×** | -4.1 | 0.006 | 10/30 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.748×** | -3.4 | 0.084 | 10/27 (A-172, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[crizotinib (drug)]] 5 µM |  | **0.755×** | -3.3 | 0.085 | 5/30 (SK-MEL-2, RKO, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.766×** | -3.3 | 0.086 | 4/30 (PANC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~14% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2660. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0698× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.178× (z -9.3) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 4.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.69× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 5.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +9.4) | — |
| [[RKO (line)]] | wt | 6.11 | 0 | 1 | — | [[Sulfatinib (drug)]] 0.05 µM 0.0597× (z -8.6) |
| [[SNU-423 (line)]] | alt | 9.96 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.112× (z -10.0) ⚠ toxic |
| [[A-427 (line)]] | wt | 0.238 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.272 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.287 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.382 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.380 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.412 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.305 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2660), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C5orf34]] | +0.83 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[ZNF100]] | +0.78 | +0.81 / +0.64 | both halves | 7e-06 | same gene group |
| [[ZNF101]] | +0.75 | +0.67 / +0.62 | both halves | 7e-06 | same gene group |
| [[ZNF253]] | +0.74 | +0.75 / +0.57 | both halves | 9e-06 | same gene group |
| [[CENPL]] | +0.68 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[ZNF563]] | +0.68 | +0.63 / +0.53 | both halves | 1e-05 | same gene group |
| [[ZNF682]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 | same gene group |
| [[ZNF714]] | +0.67 | +0.57 / +0.66 | both halves | 8e-06 | same gene group |
| [[ZNF66]] | +0.67 | +0.76 / +0.59 | both halves | 7e-06 | same gene group |
| [[ZNF724]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 | same gene group |
| [[ZNF700]] | +0.67 | +0.46 / +0.64 | both halves | 3e-05 | same gene group |
| [[ZNF442]] | +0.66 | +0.56 / +0.53 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC4]] | -0.65 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[STRAP]] | -0.63 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[SCART1]] | -0.59 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[RSU1]] | -0.59 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[SND1]] | -0.56 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[HSPA5]] | -0.56 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[NOMO1]] | -0.56 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[ATRN]] | -0.55 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[GNB1L]] | -0.55 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[GALNS]] | -0.55 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[CALU]] | -0.55 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[P4HB]] | -0.54 | -0.52 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 9, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF681]] | B | ZNF681 activity raises ZNF85's level | lines that do not express ZNF681 (16) vs lines expressing it (34) | 2.23× lower at baseline in the lines without ZNF681 | 0.016 | ⚠ within organs, on part of the lines; also absent: RPSAP58, ZNF649, ZNF793 |
| [[ZNF724]] | B | ZNF724 activity raises ZNF85's level | lines that do not express ZNF724 (8) vs lines expressing it (42) | 3.27× lower at baseline in the lines without ZNF724 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000283201, ENSG00000269237, ZNF577 |
| [[TOP2A]] | B | TOP2A activity lowers ZNF85's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF844]] | B | ZNF844 activity raises ZNF85's level | lines that do not express ZNF844 (23) vs lines expressing it (27) | 1.92× lower at baseline in the lines without ZNF844 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000286132, ENSG00000267383, ZNF486 |
| [[ZNF525]] | B | ZNF525 activity raises ZNF85's level | lines that do not express ZNF525 (10) vs lines expressing it (40) | 3.18× lower at baseline in the lines without ZNF525 | 0.044 | ⚠ within organs, on part of the lines; also absent: ZNF331, ZNF577, ZNF83 |
| [[ZNF442]] | B | ZNF442 activity raises ZNF85's level | lines that do not express ZNF442 (7) vs lines expressing it (43) | 1.89× lower at baseline in the lines without ZNF442 | 0.062 | ⚠ within organs, on part of the lines; also absent: ZNF563, ENSG00000286098, ENSG00000268870 |
| [[ZNF433]] | B | ZNF433 activity raises ZNF85's level | lines that do not express ZNF433 (8) vs lines expressing it (42) | 1.83× lower at baseline in the lines without ZNF433 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF563, ZNF442 |
| [[ZNF675]] | B | ZNF675 activity raises ZNF85's level | lines that do not express ZNF675 (5) vs lines expressing it (45) | 3.24× lower at baseline in the lines without ZNF675 | 0.079 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF573, ZNF420 |
| [[ZNF563]] | B | ZNF563 activity raises ZNF85's level | lines that do not express ZNF563 (9) vs lines expressing it (41) | 1.66× lower at baseline in the lines without ZNF563 | 0.084 | ⚠ within organs, on part of the lines; also absent: ZNF442, ZNF433, ENSG00000269755 |
| [[ZNF66]] | C | ZNF66 activity raises ZNF85's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 3.82× lower at baseline in the lines without ZNF66 | 0.008 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85; co-absent with the target |
| [[ZNF726]] | C | ZNF726 activity raises ZNF85's level | lines that do not express ZNF726 (20) vs lines expressing it (30) | 3.03× lower at baseline in the lines without ZNF726 | 0.018 | ⚠ within organs, on part of the lines; also absent: SUSD5, RNF150, BVES; co-absent with the target |
| [[ZNF682]] | C | ZNF682 activity raises ZNF85's level | lines that do not express ZNF682 (20) vs lines expressing it (30) | 2.79× lower at baseline in the lines without ZNF682 | 0.027 | ⚠ within organs, on part of the lines; also absent: ZNF93, ZNF90, SCUBE3; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 19, C 5. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF442]] | B | ZNF85 activity raises ZNF442's level | lines that do not express ZNF85 (17) vs lines expressing it (33) | 2.04× lower at baseline in the lines without ZNF85 | 0.003 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF66, ZNF726 |
| [[ZNF253]] | B | ZNF85 activity raises ZNF253's level | lines that do not express ZNF85 (17) vs lines expressing it (33) | 2.02× lower at baseline in the lines without ZNF85 | 0.007 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF66, ZNF726 |
| [[ZNF563]] | B | ZNF85 activity raises ZNF563's level | lines that do not express ZNF85 (17) vs lines expressing it (33) | 1.65× lower at baseline in the lines without ZNF85 | 0.008 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF66, ZNF726 |
| [[ZNF433]] | B | ZNF85 activity raises ZNF433's level | lines that do not express ZNF85 (17) vs lines expressing it (33) | 2.23× lower at baseline in the lines without ZNF85 | 0.008 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF66, ZNF726 |
| [[ZNF675]] | B | ZNF85 activity raises ZNF675's level | lines that do not express ZNF85 (17) vs lines expressing it (33) | 2.36× lower at baseline in the lines without ZNF85 | 0.008 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF66, ZNF726 |
| [[ZNF20]] | B | ZNF85 activity raises ZNF20's level | lines that do not express ZNF85 (17) vs lines expressing it (33) | 1.53× lower at baseline in the lines without ZNF85 | 0.024 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF66, ZNF726 |
| [[ZNF100]] | B | ZNF85 activity raises ZNF100's level | lines that do not express ZNF85 (17) vs lines expressing it (33) | 2.36× lower at baseline in the lines without ZNF85 | 0.025 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF66, ZNF726 |
| [[ZNF441]] | B | ZNF85 activity raises ZNF441's level | lines that do not express ZNF85 (17) vs lines expressing it (33) | 1.97× lower at baseline in the lines without ZNF85 | 0.027 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF66, ZNF726 |
| [[ZNF724]] | B | ZNF85 activity raises ZNF724's level | lines that do not express ZNF85 (17) vs lines expressing it (33) | 2.12× lower at baseline in the lines without ZNF85 | 0.045 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF66, ZNF726 |
| [[ZNF525]] | B | ZNF85 activity raises ZNF525's level | lines that do not express ZNF85 (17) vs lines expressing it (33) | 2.27× lower at baseline in the lines without ZNF85 | 0.052 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF66, ZNF726 |
| [[HSPA5]] | B | ZNF85 activity raises HSPA5's level | lines that do not express ZNF85 (17) vs lines expressing it (33) | 1.51× lower at baseline in the lines without ZNF85 | 0.052 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF66, ZNF726 |
| [[ZNF844]] | B | ZNF85 activity raises ZNF844's level | lines that do not express ZNF85 (17) vs lines expressing it (33) | 2.71× lower at baseline in the lines without ZNF85 | 0.054 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF66, ZNF726 |

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.800). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-44.9, -46.6); signed map (16.8, -18.4). **Vector** length 48.3, 8.12% of its response variance represented; |z| ≥ 3 in 667 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.59 to 5); *Resolution of D-loop Structures through Holliday Junction Intermediates* (reactome, mean cos +0.58 to 4); *Resolution of D-Loop Structures* (reactome, mean cos +0.58 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +16.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.7 | +9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +13.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +9.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +1.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +4.6 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +0.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -0.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -0.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 85 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p12 — chr19:20,923,222-20,950,697 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HPF4, HTF1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03923](https://www.uniprot.org/uniprotkb/Q03923) (Zinc finger protein 85):

> May be a transcriptional repressor.

**Summary**, from NCBI Gene [7639](https://www.ncbi.nlm.nih.gov/gene/7639):

> Enables DNA-binding transcription repressor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of DNA-templated transcription. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13160](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13160) · Entrez [7639](https://www.ncbi.nlm.nih.gov/gene/7639) · UniProt [Q03923](https://www.uniprot.org/uniprotkb/Q03923) · Ensembl [ENSG00000105750](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105750)

## Data

Gene col 2660: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2660); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2660, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2660]; `tensor/DDL_lfc|DDL_z.npy` [2660]; `embed/gene_vectors.npy` [2660]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2660 or target_col == 2660). Every well: [[ZNF85 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF85.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

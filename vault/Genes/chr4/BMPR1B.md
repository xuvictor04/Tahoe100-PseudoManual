---
symbol: "BMPR1B"
type: "gene"
col: 6217
ensembl_id: "ENSG00000138696"
name: "bone morphogenetic protein receptor type 1B"
location: "4q22.3"
module: 202
arm: "+"
pooled_cpm: 31.9
n_lines_expressing: 22
n_dd_up: 35
n_dd_down: 5
n_dd_up_clean: 27
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 8
tags: ["gene", "module/202"]
generated_by: "tahoemap"
---

# BMPR1B

*bone morphogenetic protein receptor type 1B* — 4q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.74× (z +34.9, q 0e+00, up in 10 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.535× (z -9.9, q 2e-20, down in 18 of 20 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02516]] (+0.64, fdr 2e-05), [[CACNA2D1]] (+0.62, fdr 1e-04), [[TRHDE]] (+0.62, fdr 4e-05); moves opposite to [[HSPB11]] (-0.65, fdr 1e-05), [[SDHAP1]] (-0.62, fdr 2e-05), [[RAB3A]] (-0.61, fdr 8e-05).
> It is in [[Module 202]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 8 go from it, the strongest it → [[MIGA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6217.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.74×** | +34.9 | 0e+00 | 10/19 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.45×** | +33.5 | 0e+00 | 19/20 (A549, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.40×** | +19.4 | 0e+00 | 18/20 (C32, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.96×** | +16.1 | 0e+00 | 8/20 (HS-578T, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.68×** | +15.6 | 0e+00 | 10/20 (SW 900, C32, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.78×** | +15.2 | 0e+00 | 8/20 (HS-578T, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.76×** | +15.1 | 0e+00 | 20/20 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.78×** | +12.9 | 4e-36 | 8/20 (HS-578T, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +9.8 | 5e-21 | 8/20 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +9.0 | 1e-17 | 13/20 (C32, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.65×** | +7.9 | 2e-13 | 14/20 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +7.6 | 2e-12 | 8/20 (C32, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +7.2 | 3e-11 | 13/20 (NCI-H2030, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.63×** | +7.1 | 4e-11 | 6/17 (SW 900, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.8 | 3e-10 | 0/18 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.54×** | +6.5 | 4e-09 | 13/19 (NCI-H1573, LoVo, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +6.3 | 9e-09 | 5/20 (HS-578T, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +6.3 | 1e-08 | 11/20 (C32, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6217.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.535×** | -9.9 | 2e-20 | 18/20 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.579×** | -8.6 | 2e-15 | 16/20 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | **0.789×** | -3.5 | 0.080 | 4/20 (hTERT-HPNE, CHP-212, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.809×** | -3.4 | 0.088 | 9/20 (BT-474, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.809×** | -3.4 | 0.088 | 13/20 (LoVo, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 0.659× | -3.1 | 0.16 | 11/20 (A-427, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6217. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 107 | 5 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +20.6) | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -14.1) |
| [[NCI-H2030 (line)]] | alt | 239 | 2 | 6 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 3.28× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.127× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.174× (z -15.8) |
| [[A498 (line)]] | wt | 8.77 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.59× (z +17.9) | — |
| [[LoVo (line)]] | wt | 155 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.0803× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.207× (z -16.3) |
| [[A-427 (line)]] | wt | 164 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.289× (z -12.1) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.312× (z -11.3) |
| [[HS-578T (line)]] | alt | 20.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +12.6) | — |
| [[NCI-H1792 (line)]] | alt | 100 | 3 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.45× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.369× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 19.3 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 8.98× (z +10.3) | — |
| [[C32 (line)]] | wt | 39.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +18.4) | — |
| [[CFPAC-1 (line)]] | alt | 54.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 62.6 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.256× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 9.65 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.58× (z +11.6) | — |
| [[H4 (line)]] | wt | 35.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +11.1) | — |
| [[hTERT-HPNE (line)]] | wt | 16.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 85.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 25.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +8.7) | — |
| [[NCI-H661 (line)]] | alt | 42.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0431× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.72 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.29 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.04 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.70 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.78 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.87 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.37 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.97 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.61 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.53 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.36 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.90 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.48 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.71 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.22 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6217), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02516]] | +0.64 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[CACNA2D1]] | +0.62 | +0.58 / +0.33 | both halves | 1e-04 |  |
| [[TRHDE]] | +0.62 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[FGF2]] | +0.62 | +0.58 / +0.44 | both halves | 3e-05 | pathway: Signaling by TGFB family members |
| [[TENM3-AS1]] | +0.62 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[ARAP2]] | +0.61 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[CARD6]] | +0.61 | +0.36 / +0.48 | both halves | 9e-05 |  |
| [[ANKRD18B]] | +0.61 | +0.54 / +0.31 | both halves | 2e-04 |  |
| [[PTPRK]] | +0.61 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[WARS2-AS1]] | +0.61 | +0.58 / +0.28 | both halves | 3e-04 |  |
| [[CCDC90B-AS1]] | +0.60 | +0.58 / +0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[RIPK2-DT]] | +0.60 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[VPS35L]] | +0.59 | +0.53 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPB11]] | -0.65 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.62 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[RAB3A]] | -0.61 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[GMCL1]] | -0.61 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[RNF168]] | -0.61 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[LCMT1]] | -0.61 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[SNAPC3]] | -0.60 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[UBE2O]] | -0.59 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[SLC31A1]] | -0.59 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[OXNAD1]] | -0.59 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[NPRL2]] | -0.59 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[DHTKD1]] | -0.58 | -0.35 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises BMPR1B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers BMPR1B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZFY]] | C | ZFY activity raises BMPR1B's level | lines that do not express ZFY (29) vs lines expressing it (21) | 2.78× lower at baseline in the lines without ZFY | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PRKY, RPS4Y1, LINC00278; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIGA2]] | B | BMPR1B activity lowers MIGA2's level | lines that do not express BMPR1B (28) vs lines expressing it (22) | 1.32× higher at baseline in the lines without BMPR1B | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, SLC6A17, EPHA5-AS1 |
| [[CABLES2]] | B | BMPR1B activity lowers CABLES2's level | lines that do not express BMPR1B (28) vs lines expressing it (22) | 1.42× higher at baseline in the lines without BMPR1B | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, SLC6A17, EPHA5-AS1 |
| [[ITPA]] | B | BMPR1B activity lowers ITPA's level | lines that do not express BMPR1B (28) vs lines expressing it (22) | 1.39× higher at baseline in the lines without BMPR1B | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, SLC6A17, EPHA5-AS1 |
| [[GRIP1]] | B | BMPR1B activity raises GRIP1's level | lines that do not express BMPR1B (28) vs lines expressing it (22) | 2.10× lower at baseline in the lines without BMPR1B | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, SLC6A17, EPHA5-AS1 |
| [[RIPK2-DT]] | B | BMPR1B activity raises RIPK2-DT's level | lines that do not express BMPR1B (28) vs lines expressing it (22) | 1.60× lower at baseline in the lines without BMPR1B | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, SLC6A17, EPHA5-AS1 |
| [[SYNPO2]] | B | BMPR1B activity raises SYNPO2's level | lines that do not express BMPR1B (28) vs lines expressing it (22) | 2.34× lower at baseline in the lines without BMPR1B | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, SLC6A17, EPHA5-AS1 |
| [[GNAI2]] | B | BMPR1B activity lowers GNAI2's level | lines that do not express BMPR1B (28) vs lines expressing it (22) | 1.20× higher at baseline in the lines without BMPR1B | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, SLC6A17, EPHA5-AS1 |
| [[ZFY]] | C | BMPR1B activity raises ZFY's level | lines that do not express BMPR1B (28) vs lines expressing it (22) | 1.94× lower at baseline in the lines without BMPR1B | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, SLC6A17, EPHA5-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 202]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.749). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.2, 15.3); signed map (44.2, 24.0). **Vector** length 67.3, 18.4% of its response variance represented; |z| ≥ 3 in 578 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +34.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +33.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +12.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +15.6 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.6 | -8.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -9.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -2.7 | -3.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -1.7 | -3.4 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | bone morphogenetic protein receptor type 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.3 — chr4:94,757,955-95,158,448 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ALK6, CDw293 |
| Gene groups (HGNC) | Type 1 receptor serine/threonine kinases; CD molecules; BMP receptors |
| Hallmark sets | ANDROGEN_RESPONSE, KRAS_SIGNALING_DN, FATTY_ACID_METABOLISM |
| Reactome | 2 pathways, smallest: Signaling by BMP; Signaling by TGFB family members |
| Matched by | ensembl_id |

**Function**, from UniProt [O00238](https://www.uniprot.org/uniprotkb/O00238) (Bone morphogenetic protein receptor type-1B):

> On ligand binding, forms a receptor complex consisting of two type II and two type I transmembrane serine/threonine kinases. Type II receptors phosphorylate and activate type I receptors which autophosphorylate, then bind and activate SMAD transcriptional regulators. Receptor for BMP7/OP-1 and GDF5. Positively regulates chondrocyte differentiation through GDF5 interaction.

**Summary**, from NCBI Gene [658](https://www.ncbi.nlm.nih.gov/gene/658):

> This gene encodes a member of the bone morphogenetic protein (BMP) receptor family of transmembrane serine/threonine kinases. The ligands of this receptor are BMPs, which are members of the TGF-beta superfamily. BMPs are involved in endochondral bone formation and embryogenesis. These proteins transduce their signals through the formation of heteromeric complexes of 2 different types of serine (threonine) kinase receptors: type I receptors of about 50-55 kD and type II receptors of about 70-80 …

**Accessions** — [HGNC:1077](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1077) · Entrez [658](https://www.ncbi.nlm.nih.gov/gene/658) · UniProt [O00238](https://www.uniprot.org/uniprotkb/O00238) · Ensembl [ENSG00000138696](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138696)

## Data

Gene col 6217: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6217); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6217, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6217]; `tensor/DDL_lfc|DDL_z.npy` [6217]; `embed/gene_vectors.npy` [6217]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6217 or target_col == 6217). Every well: [[BMPR1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMPR1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

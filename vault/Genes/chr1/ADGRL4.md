---
symbol: "ADGRL4"
type: "gene"
col: 8545
ensembl_id: "ENSG00000162618"
name: "adhesion G protein-coupled receptor L4"
location: "1p31.1"
module: 92
arm: "+"
pooled_cpm: 3.57
n_lines_expressing: 33
n_dd_up: 26
n_dd_down: 10
n_dd_up_clean: 20
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 4
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# ADGRL4

*adhesion G protein-coupled receptor L4* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.52× (z +15.1, q 0e+00, up in 13 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.494× (z -5.5, q 2e-05, down in 10 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RASGRF1]] (+0.70, fdr 7e-06), [[RASGRF2]] (+0.69, fdr 7e-06), [[PPP1R1C]] (+0.68, fdr 7e-06); moves opposite to [[HTT]] (-0.53, fdr 4e-05), [[SLC25A1]] (-0.51, fdr 8e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[LINC01138]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8545.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.52×** | +15.1 | 0e+00 | 13/23 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.90×** | +11.1 | 4e-26 | 2/7 (hTERT-HPNE, RPMI-7951) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.64×** | +10.9 | 1e-25 | 6/14 (LOX-IMVI, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.44×** | +10.7 | 2e-24 | 11/23 (LOX-IMVI, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.93×** | +8.4 | 4e-15 | 4/8 (RPMI-7951, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.28×** | +7.0 | 3e-10 | 13/26 (HEC-1-A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +6.5 | 7e-09 | 12/27 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.15×** | +6.5 | 7e-09 | 11/23 (HT-29, SW 900, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +5.4 | 5e-06 | 6/22 (AsPC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.1 | 2e-05 | 4/29 (HS-578T, NCI-H2030, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.81×** | +5.0 | 3e-05 | 9/26 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.85×** | +5.0 | 3e-05 | 12/25 (HT-29, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.77×** | +4.8 | 6e-05 | 11/27 (HS-578T, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +4.5 | 3e-04 | 9/26 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +4.1 | 0.002 | 4/23 (AsPC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.005 | 5/27 (LS 180, NCI-H1792, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[DTP3 (drug)]] 5 µM |  | **2.13×** | +3.3 | 0.027 | 3/18 (LS 180, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.043 | 6/30 (NCI-H1792, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8545.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.494×** | -5.5 | 2e-05 | 10/28 (LS 180, SHP-77, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.589×** | -4.2 | 0.007 | 16/28 (SHP-77, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.641×** | -3.6 | 0.046 | 10/25 (HT-29, SK-MEL-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.660×** | -3.5 | 0.046 | 14/28 (SHP-77, SW 1271, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.663×** | -3.5 | 0.046 | 11/28 (LS 180, NCI-H2030, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.664×** | -3.5 | 0.046 | 15/28 (HT-29, SNU-423, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.725×** | -3.4 | 0.053 | 16/28 (HT-29, NCI-H2030, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.480×** | -3.3 | 0.075 | 10/27 (SHP-77, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.718×** | -3.2 | 0.075 | 11/28 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.676×** | -3.2 | 0.077 | 13/25 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.697× | -3.1 | 0.11 | 13/28 (AsPC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8545. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 15.6 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0404× (z -10.3) ⚠ cell-cycle shift, explains ~7% of this change |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0581× (z -9.1) |
| [[HT-29 (line)]] | alt | 8.63 | 0 | 1 | — | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.0437× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.358× (z -10.8) ⚠ position not correctable |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -10.6) |
| [[A-172 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.689 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.788 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.993 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.716 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.862 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.830 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.754 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.712 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.827 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.730 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.757 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.809 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.816 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8545), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASGRF1]] | +0.70 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[RASGRF2]] | +0.69 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[PPP1R1C]] | +0.68 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ZFPM2-AS1]] | +0.67 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[SPRY2]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[B4GALT6]] | +0.66 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[SPRED1]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[AGO2]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[BFSP1]] | +0.63 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ETV4]] | +0.63 | +0.59 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[DUSP4]] | +0.62 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[MSRA]] | +0.62 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HTT]] | -0.53 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[SLC25A1]] | -0.51 | -0.37 / -0.41 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ADGRL4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SERPINE2]] | B | SERPINE2 activity raises ADGRL4's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 2.03× lower at baseline in the lines without SERPINE2 | 0.048 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[MBP]] | B | MBP activity lowers ADGRL4's level | lines that do not express MBP (9) vs lines expressing it (41) | 1.53× higher at baseline in the lines without MBP | 0.078 | ⚠ within organs, on part of the lines; co-occurs with PTEN; also absent: RHPN1, CHMP4C, EVPL |
| [[HDAC6]] | B | HDAC6 activity raises ADGRL4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity raises ADGRL4's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets |
| [[LINC02930]] | B | LINC02930 activity raises ADGRL4's level | lines that do not express LINC02930 (33) vs lines expressing it (17) | 2.21× lower at baseline in the lines without LINC02930 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000232053, GYPC, PLPP4 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01138]] | B | ADGRL4 activity raises LINC01138's level | lines that do not express ADGRL4 (17) vs lines expressing it (33) | 1.71× lower at baseline in the lines without ADGRL4 | 0.033 | ⚠ within organs, on part of the lines; also absent: PCDH7, MEF2C-AS1, FAP; maybe low, not absent |
| [[LINC00623]] | B | ADGRL4 activity raises LINC00623's level | lines that do not express ADGRL4 (17) vs lines expressing it (33) | 1.45× lower at baseline in the lines without ADGRL4 | 0.066 | ⚠ within organs, on part of the lines; also absent: PCDH7, MEF2C-AS1, FAP; maybe low, not absent |
| [[LINC01145-1]] | B | ADGRL4 activity raises LINC01145-1's level | lines that do not express ADGRL4 (17) vs lines expressing it (33) | 1.45× lower at baseline in the lines without ADGRL4 | 0.072 | ⚠ within organs, on part of the lines; also absent: PCDH7, MEF2C-AS1, FAP; maybe low, not absent |
| [[LINC01204]] | B | ADGRL4 activity lowers LINC01204's level | lines that do not express ADGRL4 (17) vs lines expressing it (33) | 1.74× higher at baseline in the lines without ADGRL4 | 0.085 | ⚠ within organs, on part of the lines; also absent: PCDH7, MEF2C-AS1, FAP; maybe low, not absent |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.804). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.9, 9.7); signed map (11.3, 43.8). **Vector** length 53.6, 10.1% of its response variance represented; |z| ≥ 3 in 740 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MAPK output* (control, mean cos +0.58 to 8); *Pre-NOTCH Expression and Processing* (reactome, mean cos +0.53 to 5); *MAPK family signaling cascades* (reactome, mean cos +0.61 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +11.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +5.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +2.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.1 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -5.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor L4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:78,889,764-79,282,124 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ETL; previously ELTD1 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily L |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBW9](https://www.uniprot.org/uniprotkb/Q9HBW9) (Adhesion G protein-coupled receptor L4):

> Endothelial orphan receptor that acts as a key regulator of angiogenesis.

**Summary**, from NCBI Gene [64123](https://www.ncbi.nlm.nih.gov/gene/64123):

> Predicted to enable G protein-coupled receptor activity. Predicted to be involved in G protein-coupled receptor signaling pathway. Predicted to be located in cytoplasmic vesicle. Predicted to be active in plasma membrane. Biomarker of glioblastoma and hypertrophic cardiomyopathy. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20822](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20822) · Entrez [64123](https://www.ncbi.nlm.nih.gov/gene/64123) · UniProt [Q9HBW9](https://www.uniprot.org/uniprotkb/Q9HBW9) · Ensembl [ENSG00000162618](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162618)

## Data

Gene col 8545: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8545); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8545, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8545]; `tensor/DDL_lfc|DDL_z.npy` [8545]; `embed/gene_vectors.npy` [8545]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8545 or target_col == 8545). Every well: [[ADGRL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

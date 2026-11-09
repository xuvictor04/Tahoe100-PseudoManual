---
symbol: "MMP7"
type: "gene"
col: 6046
ensembl_id: "ENSG00000137673"
name: "matrix metallopeptidase 7"
location: "11q22.2"
module: 8
arm: "+"
pooled_cpm: 29.86
n_lines_expressing: 11
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 69
direction_downstream: 102
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# MMP7

*matrix metallopeptidase 7* — 11q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.69× (z +12.3, q 3e-32, up in 5 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.95× (z +7.5, q 7e-12, up in 4 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.537× (z -5.0, q 3e-04, down in 8 of 8 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDZK1IP1]] (+0.80, fdr 7e-06), [[MUC4]] (+0.77, fdr 7e-06), [[TRIM31]] (+0.73, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 69 arrows point to it, the strongest [[CTSS]] → it (grade B ⚠); 102 go from it, the strongest it → [[CTSS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6046.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.69×** | +12.3 | 3e-32 | 5/8 (A549, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.27×** | +11.2 | 2e-26 | 2/6 (AsPC-1, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.45×** | +9.1 | 1e-17 | 1/7 (A549) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +7.5 | 7e-12 | 4/9 (AsPC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +6.2 | 6e-08 | 5/9 (A498, A549, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **2.16×** | +5.9 | 3e-07 | 6/8 (AsPC-1, A498, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.72×** | +5.0 | 5e-05 | 7/9 (AsPC-1, A498, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +4.5 | 6e-04 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.65×** | +4.2 | 0.001 | 8/9 (AsPC-1, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.08×** | +4.2 | 0.002 | 3/8 (AsPC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +3.9 | 0.004 | 4/8 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.52×** | +3.9 | 0.005 | 7/9 (AsPC-1, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +3.7 | 0.010 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.55×** | +3.5 | 0.021 | 6/8 (AsPC-1, A498, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.3 | 0.039 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.063 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.69×** | +3.0 | 0.085 | 0/8 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +2.9 | 0.099 | 7/8 (A498, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6046.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.537×** | -5.0 | 3e-04 | 8/8 (AsPC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.656×** | -4.8 | 5e-04 | 8/9 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.558×** | -4.7 | 5e-04 | 7/8 (A498, HT-29, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.584×** | -4.3 | 0.002 | 6/8 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.606×** | -3.9 | 0.013 | 6/8 (AsPC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.625×** | -3.8 | 0.015 | 6/8 (HT-29, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.734×** | -3.5 | 0.035 | 3/9 (CFPAC-1, A498, …) | top dose only |  |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.646×** | -3.3 | 0.065 | 0/9 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.672×** | -3.2 | 0.089 | 6/8 (HT-29, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6046. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 133 | 0 | 5 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0367× (z -15.1) |
| [[A498 (line)]] | wt | 112 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.168× (z -10.4) |
| [[COLO 205 (line)]] | alt | 34.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0629× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 49.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.0797× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 660 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 52.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -9.4) |
| [[A-172 (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.05 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.23 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.12 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.40 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.11 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.08 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6046), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDZK1IP1]] | +0.80 | +0.82 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[MUC4]] | +0.77 | +0.69 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[TRIM31]] | +0.73 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[TM4SF4]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[SAMD12-AS1]] | +0.71 | +0.65 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[BCL2L15]] | +0.71 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[WFDC2]] | +0.71 | +0.76 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[DPP4]] | +0.68 | +0.72 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_COAGULATION |
| [[ALOX5]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[RBM47]] | +0.68 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[SLC34A2]] | +0.68 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[FRK]] | +0.67 | +0.65 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*69 arrows, 69 of them with an alert ⚠; grade A 0, B 9, C 60. Shown: the 12 strongest; 57 more arrows (57 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSS]] | B | CTSS activity raises MMP7's level | lines that do not express CTSS (15) vs lines expressing it (35) | 2.56× lower at baseline in the lines without CTSS | 0.040 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[HNF4G]] | B | HNF4G activity raises MMP7's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 2.41× lower at baseline in the lines without HNF4G | 0.044 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[SAMD12-AS1]] | B | SAMD12-AS1 activity raises MMP7's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 1.88× lower at baseline in the lines without SAMD12-AS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[MTUS1]] | B | MTUS1 activity raises MMP7's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.43× lower at baseline in the lines without MTUS1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[MAP2K1]] | B | MAP2K1 activity lowers MMP7's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[HDAC6]] | B | HDAC6 activity raises MMP7's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises MMP7's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.15× lower at baseline in the lines without SLC44A3-AS1 | 0.094 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[PLEKHS1]] | B | PLEKHS1 activity raises MMP7's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 2.19× lower at baseline in the lines without PLEKHS1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[RBPMS]] | B | RBPMS activity raises MMP7's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 2.33× lower at baseline in the lines without RBPMS | 0.094 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[WFDC2]] | C | WFDC2 activity raises MMP7's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 5.34× lower at baseline in the lines without WFDC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises MMP7's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.97× lower at baseline in the lines without ADGRF1 | 0.003 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[CLIC5]] | C | CLIC5 activity raises MMP7's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 4.25× lower at baseline in the lines without CLIC5 | 0.004 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3; co-absent with the target |

### Downstream of this gene

*102 arrows, 102 of them with an alert ⚠; grade A 0, B 39, C 63. Shown: the 12 strongest; 90 more arrows (90 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSS]] | B | MMP7 activity raises CTSS's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 4.01× lower at baseline in the lines without MMP7 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[SAMD12-AS1]] | B | MMP7 activity raises SAMD12-AS1's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 2.78× lower at baseline in the lines without MMP7 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[FMO5]] | B | MMP7 activity raises FMO5's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 2.08× lower at baseline in the lines without MMP7 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[MUC20]] | B | MMP7 activity raises MUC20's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 3.24× lower at baseline in the lines without MMP7 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[BCL2L15]] | B | MMP7 activity raises BCL2L15's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 2.01× lower at baseline in the lines without MMP7 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[LGALS9]] | B | MMP7 activity raises LGALS9's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 2.73× lower at baseline in the lines without MMP7 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[LINC01504]] | B | MMP7 activity raises LINC01504's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 2.00× lower at baseline in the lines without MMP7 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[SPATA6L]] | B | MMP7 activity raises SPATA6L's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 2.67× lower at baseline in the lines without MMP7 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[FMO5]] | B | MMP7 activity strengthens FMO5's drug response | lines that do not express MMP7 (38) vs lines expressing it (8) | the lines without MMP7 respond 0.78× as strongly (z diff +0.66); strongest at Digitoxin 5 µM: 0.55x vs 0.26x (z diff +3.5) | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP; target measured in part of the lines; both ways; artifact flags |
| [[B4GALT5]] | B | MMP7 activity raises B4GALT5's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 1.86× lower at baseline in the lines without MMP7 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[RBM47]] | B | MMP7 activity raises RBM47's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 4.23× lower at baseline in the lines without MMP7 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[CGN]] | B | MMP7 activity raises CGN's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 3.21× lower at baseline in the lines without MMP7 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.764). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.4, 54.5); signed map (60.0, 2.0). **Vector** length 47.6, 21.2% of its response variance represented; |z| ≥ 3 in 307 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.59 to 5); *O-linked glycosylation of mucins* (reactome, mean cos +0.56 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +12.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +11.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +6.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.7 | +4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +2.9 |
| fall | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.0 | -3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.9 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | matrix metallopeptidase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.2 — chr11:102,520,508-102,530,750 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PUMP-1; previously MPSL1 |
| Gene groups (HGNC) | M10 matrix metallopeptidases; Elastases |
| Hallmark sets | COAGULATION |
| Reactome | 9 pathways, smallest: Activation of Matrix Metalloproteinases; Collagen degradation; Assembly of collagen fibrils and other multimeric structures |
| Matched by | ensembl_id |

**Function**, from UniProt [P09237](https://www.uniprot.org/uniprotkb/P09237) (Matrilysin):

> Degrades casein, gelatins of types I, III, IV, and V, and fibronectin. Activates procollagenase.

**Summary**, from NCBI Gene [4316](https://www.ncbi.nlm.nih.gov/gene/4316):

> This gene encodes a member of the peptidase M10 family of matrix metalloproteinases (MMPs). Proteins in this family are involved in the breakdown of extracellular matrix in normal physiological processes, such as embryonic development, reproduction, and tissue remodeling, as well as in disease processes, such as arthritis and metastasis. The encoded preproprotein is proteolytically processed to generate the mature protease. This secreted protease breaks down proteoglycans, fibronectin, elastin …

**Accessions** — [HGNC:7174](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7174) · Entrez [4316](https://www.ncbi.nlm.nih.gov/gene/4316) · UniProt [P09237](https://www.uniprot.org/uniprotkb/P09237) · Ensembl [ENSG00000137673](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137673)

## Data

Gene col 6046: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6046); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6046, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6046]; `tensor/DDL_lfc|DDL_z.npy` [6046]; `embed/gene_vectors.npy` [6046]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6046 or target_col == 6046). Every well: [[MMP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

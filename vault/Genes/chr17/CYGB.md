---
symbol: "CYGB"
type: "gene"
col: 8438
ensembl_id: "ENSG00000161544"
name: "cytoglobin"
location: "17q25.1"
module: 13
arm: "+"
pooled_cpm: 4.57
n_lines_expressing: 30
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 14
direction_downstream: 19
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# CYGB

*cytoglobin* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.74× (z +12.5, q 7e-33, up in 7 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.490× (z -6.3, q 2e-07, down in 10 of 22 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTHRC1]] (+0.62, fdr 1e-05), [[LINC02813]] (+0.58, fdr 1e-05), [[ZNF385D]] (+0.56, fdr 1e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[GDNF]] → it (grade B ⚠); 19 go from it, the strongest it → [[SLC16A6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8438.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.74×** | +12.5 | 7e-33 | 7/21 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.41×** | +10.3 | 2e-22 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.96×** | +8.8 | 3e-16 | 1/6 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.51×** | +7.7 | 1e-12 | 4/12 (A498, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +6.7 | 2e-09 | 3/10 (HepG2/C3A, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.87×** | +5.5 | 4e-06 | 8/26 (A-427, SNU-1, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.0 | 0.006 | 2/19 (A-427, HS-578T) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.70×** | +3.3 | 0.069 | 2/18 (PANC-1, HS-578T) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.49×** | +3.2 | 0.084 | 2/15 (SW480, PANC-1) | inconsistent across doses | low cells (technical?) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 1.63× | +3.0 | 0.13 | 1/8 (HepG2/C3A) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8438.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.490×** | -6.3 | 2e-07 | 10/22 (PANC-1, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.516×** | -5.8 | 2e-06 | 13/26 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.547×** | -5.3 | 2e-05 | 13/24 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.554×** | -5.2 | 3e-05 | 12/25 (HOP62, SW 900, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.568×** | -5.0 | 7e-05 | 15/25 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.665×** | -3.6 | 0.030 | 2/24 (SW480, C-33 A) | inconsistent across doses | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.688×** | -3.3 | 0.077 | 2/27 (SNU-1, RPMI-7951) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8438. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 31.0 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0858× (z -15.2) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0625× (z -12.2) |
| [[C32 (line)]] | wt | 83.0 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0623× (z -15.3) |
| [[HepG2_C3A (line)]] | wt | 7.67 | 1 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 22.1× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 0.5 µM 0.0327× (z -10.4) |
| [[SW 900 (line)]] | alt | 13.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -9.4) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0756× (z -9.0) |
| [[PANC-1 (line)]] | alt | 4.18 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0464× (z -12.5) |
| [[SNU-423 (line)]] | alt | 18.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0953× (z -8.9) |
| [[A-172 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.877 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.963 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.706 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.598 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.860 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.970 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.894 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.959 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.685 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.750 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.586 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8438), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTHRC1]] | +0.62 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[LINC02813]] | +0.58 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ZNF385D]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[GDNF-AS1]] | +0.55 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[CNIH3]] | +0.55 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[MIR34AHG]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[C10orf90]] | +0.54 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[RUNX3]] | +0.53 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[SETBP1]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[ITGA11]] | +0.51 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ITGB3]] | +0.51 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[FAM20C]] | +0.50 | +0.54 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 10, C 4. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GDNF]] | B | GDNF activity raises CYGB's level | lines that do not express GDNF (38) vs lines expressing it (12) | 3.14× lower at baseline in the lines without GDNF | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9 |
| [[C10orf90]] | B | C10orf90 activity raises CYGB's level | lines that do not express C10orf90 (35) vs lines expressing it (15) | 2.40× lower at baseline in the lines without C10orf90 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GRIN2A, LINC01242, ADGRG7; maybe low, not absent |
| [[SLC16A6]] | B | SLC16A6 activity raises CYGB's level | lines that do not express SLC16A6 (27) vs lines expressing it (23) | 2.44× lower at baseline in the lines without SLC16A6 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7 |
| [[FRMD4A]] | B | FRMD4A activity raises CYGB's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.10× lower at baseline in the lines without FRMD4A | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[DENND2A]] | B | DENND2A activity raises CYGB's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 1.85× lower at baseline in the lines without DENND2A | 0.053 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[GYPC]] | B | GYPC activity raises CYGB's level | lines that do not express GYPC (35) vs lines expressing it (15) | 2.20× lower at baseline in the lines without GYPC | 0.067 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[CTHRC1]] | B | CTHRC1 activity raises CYGB's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 2.71× lower at baseline in the lines without CTHRC1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent |
| [[FLT1]] | B | FLT1 activity raises CYGB's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 1.95× lower at baseline in the lines without FLT1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB |
| [[HDAC6]] | B | HDAC6 activity raises CYGB's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MRC2]] | B | MRC2 activity raises CYGB's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 2.05× lower at baseline in the lines without MRC2 | 0.087 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[INSYN2B]] | C | INSYN2B activity raises CYGB's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 2.78× lower at baseline in the lines without INSYN2B | 0.030 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[LINC02813]] | C | LINC02813 activity raises CYGB's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 2.30× lower at baseline in the lines without LINC02813 | 0.057 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 12, C 7. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A6]] | B | CYGB activity raises SLC16A6's level | lines that do not express CYGB (20) vs lines expressing it (30) | 2.43× lower at baseline in the lines without CYGB | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[EFCAB13-DT]] | B | CYGB activity raises EFCAB13-DT's level | lines that do not express CYGB (20) vs lines expressing it (30) | 1.47× lower at baseline in the lines without CYGB | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[CNIH3]] | B | CYGB activity raises CNIH3's level | lines that do not express CYGB (20) vs lines expressing it (30) | 2.51× lower at baseline in the lines without CYGB | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[ITGB3]] | B | CYGB activity raises ITGB3's level | lines that do not express CYGB (20) vs lines expressing it (30) | 3.34× lower at baseline in the lines without CYGB | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[ZNF404]] | B | CYGB activity raises ZNF404's level | lines that do not express CYGB (20) vs lines expressing it (30) | 2.35× lower at baseline in the lines without CYGB | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[FRMD4A]] | B | CYGB activity raises FRMD4A's level | lines that do not express CYGB (20) vs lines expressing it (30) | 2.78× lower at baseline in the lines without CYGB | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[BOC]] | B | CYGB activity raises BOC's level | lines that do not express CYGB (20) vs lines expressing it (30) | 2.49× lower at baseline in the lines without CYGB | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[C2orf92]] | B | CYGB activity raises C2orf92's level | lines that do not express CYGB (20) vs lines expressing it (30) | 1.74× lower at baseline in the lines without CYGB | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[SHC4]] | B | CYGB activity raises SHC4's level | lines that do not express CYGB (20) vs lines expressing it (30) | 2.30× lower at baseline in the lines without CYGB | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[DENND2A]] | B | CYGB activity raises DENND2A's level | lines that do not express CYGB (20) vs lines expressing it (30) | 2.15× lower at baseline in the lines without CYGB | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[DPY19L2P2]] | B | CYGB activity raises DPY19L2P2's level | lines that do not express CYGB (20) vs lines expressing it (30) | 1.48× lower at baseline in the lines without CYGB | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[GDNF]] | B | CYGB activity raises GDNF's level | lines that do not express CYGB (20) vs lines expressing it (30) | 2.56× lower at baseline in the lines without CYGB | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.469). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.4, 9.3); signed map (11.6, 50.9). **Vector** length 57.1, 12.9% of its response variance represented; |z| ≥ 3 in 652 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +12.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.4 | +8.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +0.9 | +1.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.7 | +2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.7 | +3.2 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.5 | -5.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.0 | -1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -0.9 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | cytoglobin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:76,527,356-76,551,175 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HGB, STAP |
| Gene groups (HGNC) | Oxygenases; Globin family |
| Reactome | 3 pathways, smallest: eNOS activation; Metabolism of nitric oxide: NOS3 activation and regulation; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWM9](https://www.uniprot.org/uniprotkb/Q8WWM9) (Cytoglobin):

> Probable multifunctional globin with a hexacoordinated heme iron required for the catalysis of various reactions depending on redox condition of the cell as well as oxygen availability. Has a nitric oxide dioxygenase (NOD) activity and is most probably involved in cell-mediated and oxygen-dependent nitric oxide consumption. By scavenging this second messenger may regulate several biological processes including endothelium-mediated vasodilation and vascular tone. Under normoxic conditions …

**Summary**, from NCBI Gene [114757](https://www.ncbi.nlm.nih.gov/gene/114757):

> This gene encodes a globin protein found in vertebrate cells. The encoded protein is described as a hexacoordinate hemoglobin which binds ligand differently from the pentacoordinate hemoglobins involved in oxygen transport, and may be involved in protection during oxidative stress. This gene is located on chromosome 17 in the same region as a retinal gene which is mutated in progressive rod-cone degeneration, but in the opposite orientation. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:16505](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16505) · Entrez [114757](https://www.ncbi.nlm.nih.gov/gene/114757) · UniProt [Q8WWM9](https://www.uniprot.org/uniprotkb/Q8WWM9) · Ensembl [ENSG00000161544](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161544)

## Data

Gene col 8438: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8438); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8438, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8438]; `tensor/DDL_lfc|DDL_z.npy` [8438]; `embed/gene_vectors.npy` [8438]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8438 or target_col == 8438). Every well: [[CYGB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYGB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

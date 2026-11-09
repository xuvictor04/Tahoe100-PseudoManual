---
symbol: "PITRM1-AS1"
type: "gene"
col: 14130
ensembl_id: "ENSG00000237399"
name: "PITRM1 antisense RNA 1"
location: "10p15.2"
module: 47
arm: "+"
pooled_cpm: 6.91
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# PITRM1-AS1

*PITRM1 antisense RNA 1* — 10p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.23× (z +7.2, q 3e-10, up in 7 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.55× (z +5.8, q 2e-06, up in 20 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.580× (z -5.1, q 2e-04, down in 19 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM72]] (+0.86, fdr 7e-06), [[FNDC7]] (+0.85, fdr 7e-06), [[USP50]] (+0.84, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[LINC01291]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14130.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +7.2 | 3e-10 | 7/15 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +5.8 | 2e-06 | 20/41 (SW48, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +5.2 | 3e-05 | 11/30 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +4.7 | 4e-04 | 8/23 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +4.0 | 0.006 | 18/39 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.008 | 18/44 (HEC-1-A, SW480, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.032 | 9/46 (NCI-H1792, NCI-H2030, …) | rises with dose | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.032 | 13/48 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +3.2 | 0.075 | 11/45 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.27× | +3.1 | 0.10 | 12/42 (MIA PaCa-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14130.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.580×** | -5.1 | 2e-04 | 19/44 (H4, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.592×** | -4.9 | 2e-04 | 25/46 (HT-29, LOX-IMVI, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.634×** | -4.3 | 0.003 | 19/44 (NCI-H1792, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.669×** | -3.8 | 0.023 | 17/46 (J82, H4, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Amsacrine (drug)]] 5 µM |  | **0.775×** | -3.4 | 0.078 | 13/45 (HEC-1-A, BT-474, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.704×** | -3.3 | 0.089 | 10/47 (BT-474, NCI-H460, …) | top dose only |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM |  | 0.716× | -3.1 | 0.14 | 9/42 (NCI-H1792, SHP-77, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | 0.721× | -3.1 | 0.15 | 7/44 (COLO 205, SW1417, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.707× | -3.0 | 0.15 | 13/45 (C-33 A, RPMI-7951, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.727× | -3.0 | 0.15 | 11/46 (BT-474, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14130. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.10 | 0 | 2 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.102× (z -9.7) |
| [[SW 900 (line)]] | alt | 7.51 | 0 | 2 | — | [[Radotinib (drug)]] 0.5 µM 0.0706× (z -9.8) |
| [[A498 (line)]] | wt | 6.74 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0785× (z -10.0) |
| [[A549 (line)]] | wt | 7.81 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0889× (z -9.0) |
| [[HOP62 (line)]] | alt | 4.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 6.31 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0735× (z -9.4) |
| [[LS 180 (line)]] | wt | 5.52 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0670× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 9.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 6.74 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.87× (z +8.9) | — |
| [[SW48 (line)]] | wt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.00× (z +10.4) | — |
| [[A-172 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14130), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM72]] | +0.86 | +0.85 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[FNDC7]] | +0.85 | +0.83 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[USP50]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 |  |
| [[C19orf38]] | +0.84 | +0.82 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[MPP4]] | +0.84 | +0.80 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[PILRA]] | +0.82 | +0.80 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[ALDH8A1]] | +0.82 | +0.78 / +0.81 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.82 | +0.84 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[MYOCOS]] | +0.81 | +0.82 / +0.80 | both halves | 7e-06 |  |
| [[LINC02236]] | +0.80 | +0.78 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[SH2D4B]] | +0.80 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[TMEM25]] | +0.80 | +0.78 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01291]] | B | LINC01291 activity raises PITRM1-AS1's level | lines that do not express LINC01291 (10) vs lines expressing it (40) | 1.64× lower at baseline in the lines without LINC01291 | 0.025 | ⚠ within organs, on part of the lines; also absent: ANTXR2, ENSG00000230479, PROCR; maybe low, not absent |
| [[SEMA4A]] | B | SEMA4A activity raises PITRM1-AS1's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.69× lower at baseline in the lines without SEMA4A | 0.035 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[FBXW10B]] | B | FBXW10B activity raises PITRM1-AS1's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without FBXW10B | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[FER1L4]] | B | FER1L4 activity raises PITRM1-AS1's level | lines that do not express FER1L4 (7) vs lines expressing it (43) | 1.35× lower at baseline in the lines without FER1L4 | 0.049 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, STEAP2, OSR2; maybe low, not absent |
| [[SLC2A9]] | B | SLC2A9 activity raises PITRM1-AS1's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 1.60× lower at baseline in the lines without SLC2A9 | 0.062 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[IMPA1P1]] | B | IMPA1P1 activity raises PITRM1-AS1's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.45× lower at baseline in the lines without IMPA1P1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[TRIM72]] | C | TRIM72 activity raises PITRM1-AS1's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 2.00× lower at baseline in the lines without TRIM72 | 0.013 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |
| [[LINC02133]] | C | LINC02133 activity raises PITRM1-AS1's level | lines that do not express LINC02133 (4) vs lines expressing it (46) | 1.69× lower at baseline in the lines without LINC02133 | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LYG1, RBM44, TRIM72; maybe low, not absent |
| [[PDE2A]] | C | PDE2A activity raises PITRM1-AS1's level | lines that do not express PDE2A (4) vs lines expressing it (46) | 1.77× lower at baseline in the lines without PDE2A | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GOLGA8N, TMEFF1, LUCAT1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.884). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.0, -15.1); signed map (17.4, 11.3). **Vector** length 84.8, 16.1% of its response variance represented; |z| ≥ 3 in 948 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.9 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.8 | +3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.4 |
| fall | [[Radotinib (drug)]] 5 µM |  | -3.7 | -2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -5.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.9 | -2.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.6 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | PITRM1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10p15.2 — chr10:3,141,632-3,167,972 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44675](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44675) · Entrez [100507034](https://www.ncbi.nlm.nih.gov/gene/100507034) · Ensembl [ENSG00000237399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237399)

## Data

Gene col 14130: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14130); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14130, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14130]; `tensor/DDL_lfc|DDL_z.npy` [14130]; `embed/gene_vectors.npy` [14130]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14130 or target_col == 14130). Every well: [[PITRM1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PITRM1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

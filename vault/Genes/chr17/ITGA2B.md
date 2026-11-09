---
symbol: "ITGA2B"
type: "gene"
col: 94
ensembl_id: "ENSG00000005961"
name: "integrin subunit alpha 2b"
location: "17q21.31"
module: 38
arm: "+"
pooled_cpm: 5.65
n_lines_expressing: 47
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 8
direction_downstream: 3
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# ITGA2B

*integrin subunit alpha 2b* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.91× (z +14.6, q 3e-45, up in 33 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.443× (z -7.9, q 2e-12, down in 23 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.496× (z -6.8, q 3e-09, down in 28 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HVCN1]] (+0.76, fdr 7e-06), [[MYOCOS]] (+0.70, fdr 7e-06), [[EPHX3]] (+0.68, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[COL4A3]] → it (grade B ⚠); 3 go from it, the strongest it → [[STRADA]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 94.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.91×** | +14.6 | 3e-45 | 33/37 (MIA PaCa-2, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.28×** | +11.3 | 6e-27 | 22/36 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +9.6 | 1e-19 | 7/9 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +7.4 | 2e-11 | 12/21 (SW 900, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +4.6 | 4e-04 | 11/43 (HOP62, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.015 | 10/38 (C-33 A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.015 | 9/44 (HepG2/C3A, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.030 | 9/45 (HOP62, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.038 | 6/41 (CFPAC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.40× | +3.0 | 0.15 | 4/12 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 94.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.443×** | -7.9 | 2e-12 | 23/33 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.496×** | -6.8 | 3e-09 | 28/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.506×** | -6.6 | 7e-09 | 23/43 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.551×** | -5.8 | 1e-06 | 20/43 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.587×** | -5.2 | 3e-05 | 19/44 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.629×** | -4.5 | 6e-04 | 17/43 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.712×** | -3.3 | 0.078 | 14/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.705×** | -3.2 | 0.094 | 10/40 (HEC-1-A, J82, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 94. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 25.4 | 0 | 16 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0281× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0972× (z -15.0) |
| [[A549 (line)]] | wt | 5.62 | 0 | 2 (1 ⚠) | — | [[Oxaprozin (drug)]] 0.5 µM 0.0799× (z -9.3) |
| [[PANC-1 (line)]] | alt | 3.80 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0416× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.139× (z -9.2) |
| [[A-427 (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.106× (z -11.4) ⚠ cell-cycle shift, explains ~43% of this change |
| [[HEC-1-A (line)]] | alt | 11.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.124× (z -10.3) |
| [[LoVo (line)]] | wt | 5.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 7.14 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0998× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 5.35 | 0 | 1 | — | [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.0641× (z -9.1) |
| [[A-172 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.906 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 94), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HVCN1]] | +0.76 | +0.76 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[MYOCOS]] | +0.70 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[EPHX3]] | +0.68 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[SPOCK2]] | +0.68 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.68 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[ARL9]] | +0.67 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[HCLS1]] | +0.67 | +0.69 / +0.62 | both halves | 7e-06 | STRING 446 |
| [[CPT1C]] | +0.67 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[AZU1]] | +0.66 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[USP50]] | +0.65 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.65 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[LAT2]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL4A3]] | B | COL4A3 activity raises ITGA2B's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 1.66× lower at baseline in the lines without COL4A3 | 0.015 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4 |
| [[LINC00334]] | B | LINC00334 activity raises ITGA2B's level | lines that do not express LINC00334 (10) vs lines expressing it (40) | 1.67× lower at baseline in the lines without LINC00334 | 0.046 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ITGA2B's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ISM2]] | B | ISM2 activity raises ITGA2B's level | lines that do not express ISM2 (9) vs lines expressing it (41) | 1.83× lower at baseline in the lines without ISM2 | 0.065 | ⚠ within organs, on part of the lines; also absent: DYSF, CSRP2, LINC02609; maybe low, not absent |
| [[SPOCK2]] | B | SPOCK2 activity raises ITGA2B's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.56× lower at baseline in the lines without SPOCK2 | 0.080 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |
| [[PRRX2]] | B | PRRX2 activity raises ITGA2B's level | lines that do not express PRRX2 (24) vs lines expressing it (26) | 1.42× lower at baseline in the lines without PRRX2 | 0.082 | ⚠ within organs, on part of the lines; also absent: PTCHD1, CYP27C1, STOX2 |
| [[KIF17]] | C | KIF17 activity raises ITGA2B's level | lines that do not express KIF17 (3) vs lines expressing it (47) | 2.56× lower at baseline in the lines without KIF17 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DPF1, CNTNAP1, CFL2; maybe low, not absent; co-absent with the target; its own permutation p |
| [[IMPG2]] | C | IMPG2 activity raises ITGA2B's level | lines that do not express IMPG2 (4) vs lines expressing it (46) | 2.21× lower at baseline in the lines without IMPG2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, CLEC2D, LINC01341; maybe low, not absent; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STRADA]] | C | ITGA2B activity raises STRADA's level | lines that do not express ITGA2B (3) vs lines expressing it (47) | 1.59× lower at baseline in the lines without ITGA2B | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PHC1, CFL2, HECTD2; maybe low, not absent; its own permutation p |
| [[MFSD2B]] | C | ITGA2B activity raises MFSD2B's level | lines that do not express ITGA2B (3) vs lines expressing it (47) | 1.53× lower at baseline in the lines without ITGA2B | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PHC1, CFL2, HECTD2; maybe low, not absent |
| [[PILRA]] | C | ITGA2B activity raises PILRA's level | lines that do not express ITGA2B (3) vs lines expressing it (47) | 2.12× lower at baseline in the lines without ITGA2B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PHC1, CFL2, HECTD2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.678). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.8, -17.1); signed map (16.2, 10.0). **Vector** length 74.5, 13.0% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +14.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +11.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +1.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.4 | -6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | -6.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -5.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.1 | -4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.0 | -3.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit alpha 2b |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:44,372,180-44,389,649 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD41B, CD41, PPP1R93, GPIIb; previously GP2B |
| Gene groups (HGNC) | CD molecules; Protein phosphatase 1 regulatory subunits; Integrin alpha subunits; Human platelet antigens |
| Reactome | 32 pathways, smallest: Fibrin formation; GRB2:SOS provides linkage to MAPK signaling for Integrins; p130Cas linkage to MAPK signaling for integrins |
| Matched by | ensembl_id |

**Function**, from UniProt [P08514](https://www.uniprot.org/uniprotkb/P08514) (Integrin alpha-IIb):

> Integrin alpha-IIb/beta-3 (ITGA2B:ITGB3) is a receptor for fibronectin, fibrinogen, plasminogen, prothrombin, thrombospondin and vitronectin. It recognizes the sequence R-G-D in a wide array of ligands. It recognizes the sequence H-H-L-G-G-G-A-K-Q-A-G-D-V in fibrinogen gamma chain (By similarity). Following activation integrin alpha-IIb/beta-3 brings about platelet/platelet interaction through binding of soluble fibrinogen. This step leads to rapid platelet aggregation which physically plugs …

**Summary**, from NCBI Gene [3674](https://www.ncbi.nlm.nih.gov/gene/3674):

> This gene encodes a member of the integrin alpha chain family of proteins. The encoded preproprotein is proteolytically processed to generate light and heavy chains that associate through disulfide linkages to form a subunit of the alpha-IIb/beta-3 integrin cell adhesion receptor. This receptor plays a crucial role in the blood coagulation system, by mediating platelet aggregation. Mutations in this gene are associated with platelet-type bleeding disorders, which are characterized by a failure …

**Accessions** — [HGNC:6138](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6138) · Entrez [3674](https://www.ncbi.nlm.nih.gov/gene/3674) · UniProt [P08514](https://www.uniprot.org/uniprotkb/P08514) · Ensembl [ENSG00000005961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005961)

## Data

Gene col 94: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 94); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 94, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 94]; `tensor/DDL_lfc|DDL_z.npy` [94]; `embed/gene_vectors.npy` [94]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 94 or target_col == 94). Every well: [[ITGA2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGA2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

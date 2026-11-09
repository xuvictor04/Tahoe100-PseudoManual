---
symbol: "GARIN1B"
type: "gene"
col: 5669
ensembl_id: "ENSG00000135248"
name: "golgi associated RAB2 interactor 1B"
location: "7q32.1"
module: 39
arm: "+"
pooled_cpm: 2.13
n_lines_expressing: 46
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 10
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# GARIN1B

*golgi associated RAB2 interactor 1B* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.63× (z +11.3, q 7e-27, up in 25 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Dexamethasone (drug)]] 5 µM: 0.401× (z -4.3, q 0.011, down in 18 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPYS]] (+0.89, fdr 7e-06), [[SLC6A13]] (+0.86, fdr 7e-06), [[USP50]] (+0.86, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 10 go from it, the strongest it → [[GARIN1A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5669.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.63×** | +11.3 | 7e-27 | 25/27 (SW1417, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.63×** | +10.0 | 3e-21 | 21/29 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.84×** | +8.6 | 2e-15 | 1/4 (HS-578T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.47×** | +8.0 | 2e-13 | 3/5 (CFPAC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.26×** | +7.7 | 2e-12 | 4/12 (NCI-H2030, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.26×** | +6.7 | 2e-09 | 18/28 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.34×** | +5.4 | 7e-06 | 8/22 (LOX-IMVI, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **3.09×** | +5.2 | 1e-05 | 23/41 (A498, J82, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.04×** | +4.6 | 2e-04 | 7/38 (A498, CFPAC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **2.53×** | +4.3 | 0.001 | 13/35 (LoVo, SW48, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +4.3 | 0.001 | 11/30 (C32, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.81×** | +3.9 | 0.005 | 9/38 (HEC-1-A, SW1417, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.34×** | +3.8 | 0.007 | 12/33 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lactate (calcium) (drug)]] 5 µM |  | **2.09×** | +3.4 | 0.027 | 7/39 (RPMI-7951, NCI-H1573, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.18×** | +3.4 | 0.027 | 8/34 (A498, A549, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM |  | **2.08×** | +3.4 | 0.027 | 5/39 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **2.02×** | +3.2 | 0.040 | 4/33 (HEC-1-A, SW1417, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.93×** | +3.0 | 0.079 | 7/40 (J82, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5669.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 5 µM |  | **0.401×** | -4.3 | 0.011 | 18/39 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Tirabrutinib (drug)]] 5 µM |  | 0.480× | -3.3 | 0.16 | 12/40 (SW 900, hTERT-HPNE, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | 0.504× | -3.2 | 0.16 | 11/38 (SW 900, HS-578T, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Anethole trithione (drug)]] 5 µM |  | 0.620× | -3.2 | 0.16 | 7/39 (J82, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.621× | -3.2 | 0.16 | 16/35 (BT-474, SNU-423, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.494× | -3.1 | 0.16 | 8/28 (NCI-H460, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM |  | 0.282× | -3.1 | 0.16 | 9/18 (HEC-1-A, J82, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5669. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.884 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.983 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.833 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.722 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.775 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.521 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.782 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.682 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.683 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.330 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.439 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5669), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPYS]] | +0.89 | +0.87 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[SLC6A13]] | +0.86 | +0.87 / +0.80 | both halves | 7e-06 |  |
| [[USP50]] | +0.86 | +0.84 / +0.83 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.84 | +0.81 / +0.81 | both halves | 7e-06 | ⚠ same locus (21.2 kb, same strand: neighbours can correlate without regulation) |
| [[MYOCOS]] | +0.84 | +0.80 / +0.79 | both halves | 7e-06 |  |
| [[MPP4]] | +0.83 | +0.85 / +0.73 | both halves | 7e-06 |  |
| [[AXDND1]] | +0.82 | +0.81 / +0.69 | both halves | 7e-06 |  |
| [[OIT3]] | +0.81 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.81 | +0.81 / +0.72 | both halves | 7e-06 |  |
| [[LINC01934]] | +0.80 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[SGSM3-AS1]] | +0.80 | +0.80 / +0.80 | both halves | 7e-06 |  |
| [[SLC7A9]] | +0.79 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[SLC22A1]] | +0.79 | +0.76 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GARIN1B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01252]] | B | LINC01252 activity raises GARIN1B's level | lines that do not express LINC01252 (17) vs lines expressing it (33) | 1.54× lower at baseline in the lines without LINC01252 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000275119, EPHB6, ABCC2; maybe low, not absent |
| [[FBXW10B]] | B | FBXW10B activity raises GARIN1B's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 1.47× lower at baseline in the lines without FBXW10B | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GARIN1A]] | C | GARIN1B activity raises GARIN1A's level | lines that do not express GARIN1B (4) vs lines expressing it (46) | 2.37× lower at baseline in the lines without GARIN1B | 0.001 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PGGHG, ALPK1; maybe low, not absent |
| [[RIMS2]] | C | GARIN1B activity lowers RIMS2's level | lines that do not express GARIN1B (4) vs lines expressing it (46) | 2.57× higher at baseline in the lines without GARIN1B | 0.035 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PGGHG, ALPK1; maybe low, not absent |
| [[TBX15]] | C | GARIN1B activity lowers TBX15's level | lines that do not express GARIN1B (4) vs lines expressing it (46) | 2.04× higher at baseline in the lines without GARIN1B | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PGGHG, ALPK1; maybe low, not absent |
| [[SLC6A13]] | C | GARIN1B activity raises SLC6A13's level | lines that do not express GARIN1B (4) vs lines expressing it (46) | 2.41× lower at baseline in the lines without GARIN1B | 0.059 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PGGHG, ALPK1; maybe low, not absent |
| [[FAM24B]] | C | GARIN1B activity lowers FAM24B's level | lines that do not express GARIN1B (4) vs lines expressing it (46) | 2.26× higher at baseline in the lines without GARIN1B | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PGGHG, ALPK1; maybe low, not absent |
| [[SLC35A1]] | C | GARIN1B activity weakens SLC35A1's drug response | lines that do not express GARIN1B (4) vs lines expressing it (44) | the lines without GARIN1B respond 1.88× as strongly (z diff -2.24); strongest at Digitoxin 5 µM: 0.32x vs 0.61x (z diff -5.6) | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PGGHG, ALPK1; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |
| [[BTBD16]] | C | GARIN1B activity lowers BTBD16's level | lines that do not express GARIN1B (4) vs lines expressing it (46) | 2.04× higher at baseline in the lines without GARIN1B | 0.077 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PGGHG, ALPK1; maybe low, not absent |
| [[LYRM7]] | C | GARIN1B activity lowers LYRM7's level | lines that do not express GARIN1B (4) vs lines expressing it (46) | 1.58× higher at baseline in the lines without GARIN1B | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PGGHG, ALPK1; maybe low, not absent |
| [[SLC35A1]] | C | GARIN1B activity lowers SLC35A1's level | lines that do not express GARIN1B (4) vs lines expressing it (46) | 1.73× higher at baseline in the lines without GARIN1B | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PGGHG, ALPK1; maybe low, not absent |
| [[USP50]] | C | GARIN1B activity raises USP50's level | lines that do not express GARIN1B (4) vs lines expressing it (46) | 1.69× lower at baseline in the lines without GARIN1B | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PGGHG, ALPK1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.876). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.8, -13.5); signed map (18.4, 9.2). **Vector** length 69.2, 13.6% of its response variance represented; |z| ≥ 3 in 778 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.5 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.3 | +5.2 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.9 | +3.4 |
| fall | [[Radotinib (drug)]] 5 µM |  | -3.3 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.6 | -3.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -1.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.0 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | golgi associated RAB2 interactor 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.1 — chr7:128,709,061-128,731,743 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NYD-SP18, GARI-L1; previously FAM137A, FAM71F1 |
| Gene groups (HGNC) | Golgi associated RAB2 interactor family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96KD3](https://www.uniprot.org/uniprotkb/Q96KD3) (Golgi-associated RAB2 interactor protein 1B):

> RAB2B effector protein required for accurate acrosome formation and normal male fertility. In complex with RAB2A/RAB2B, seems to suppress excessive vesicle trafficking during acrosome formation.

**Summary**, from NCBI Gene [84691](https://www.ncbi.nlm.nih.gov/gene/84691):

> Predicted to be involved in acrosome assembly and acrosome reaction. Predicted to be located in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30704](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30704) · Entrez [84691](https://www.ncbi.nlm.nih.gov/gene/84691) · UniProt [Q96KD3](https://www.uniprot.org/uniprotkb/Q96KD3) · Ensembl [ENSG00000135248](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135248)

## Data

Gene col 5669: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5669); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5669, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5669]; `tensor/DDL_lfc|DDL_z.npy` [5669]; `embed/gene_vectors.npy` [5669]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5669 or target_col == 5669). Every well: [[GARIN1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GARIN1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

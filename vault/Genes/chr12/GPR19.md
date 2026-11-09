---
symbol: "GPR19"
type: "gene"
col: 11374
ensembl_id: "ENSG00000183150"
name: "G protein-coupled receptor 19"
location: "12p13.1"
module: 71
arm: "+"
pooled_cpm: 3.75
n_lines_expressing: 44
n_dd_up: 14
n_dd_down: 18
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# GPR19

*G protein-coupled receptor 19* — 12p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.02× (z +15.4, q 0e+00, up in 29 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.427× (z -8.4, q 3e-14, down in 27 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLCD3B]] (+0.82, fdr 7e-06), [[E2F8]] (+0.78, fdr 7e-06), [[CENPH]] (+0.78, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[ZGRF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11374.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.02×** | +15.4 | 0e+00 | 29/34 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.52×** | +8.4 | 1e-14 | 1/5 (HOP62) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.93×** | +6.2 | 1e-07 | 2/4 (A498, CFPAC-1) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **1.68×** | +5.1 | 5e-05 | 5/17 (SW1417, NCI-H2347, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.65×** | +4.7 | 2e-04 | 14/34 (SW480, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.61×** | +4.5 | 7e-04 | 13/31 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.36×** | +4.3 | 0.001 | 9/39 (LOX-IMVI, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.53×** | +4.2 | 0.002 | 10/40 (HT-29, SW480, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.35×** | +4.2 | 0.002 | 7/39 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.004 | 8/39 (HOP62, SW480, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.46×** | +3.7 | 0.011 | 11/40 (SW480, NCI-H23, …) | two highest doses |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.41×** | +3.4 | 0.033 | 4/39 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.41×** | +3.3 | 0.049 | 3/37 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.083 | 4/38 (C32, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11374.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.427×** | -8.4 | 3e-14 | 27/40 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.484×** | -7.2 | 2e-10 | 22/38 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.464×** | -7.2 | 2e-10 | 21/36 (NCI-H23, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.593×** | -5.2 | 3e-05 | 12/33 (A498, Hs 766T, …) | two highest doses |  |
| [[palbociclib (drug)]] 0.5 µM |  | **0.483×** | -5.1 | 3e-05 | 12/41 (HEC-1-A, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.616×** | -4.8 | 2e-04 | 16/37 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.720×** | -4.6 | 4e-04 | 18/39 (SW 1271, NCI-H1792, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.636×** | -4.5 | 5e-04 | 12/40 (LS 180, PANC-1, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.736×** | -4.3 | 0.001 | 15/41 (SHP-77, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.650×** | -4.3 | 0.001 | 16/39 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.661×** | -4.1 | 0.002 | 14/38 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.679×** | -3.8 | 0.006 | 17/28 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.772×** | -3.6 | 0.012 | 10/39 (SK-MEL-2, RPMI-7951, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.498×** | -3.6 | 0.013 | 9/31 (C-33 A, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.792×** | -3.3 | 0.041 | 12/35 (Panc 03.27, A498, …) | two highest doses | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.732×** | -3.0 | 0.094 | 8/37 (NCI-H1792, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.81 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11374. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 20.4 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.165× (z -10.4) |
| [[A-427 (line)]] | wt | 10.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -9.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 9.71 | 0 | 1 | — | [[Verapamil (drug)]] 0.05 µM 0.0725× (z -9.2) |
| [[PANC-1 (line)]] | alt | 4.81 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.148× (z -9.9) |
| [[SW480 (line)]] | alt | 4.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +10.2) | — |
| [[A-172 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.956 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.842 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.671 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.581 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.758 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.945 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11374), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLCD3B]] | +0.82 | +0.80 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[E2F8]] | +0.78 | +0.75 / +0.80 | both halves | 7e-06 |  |
| [[CENPH]] | +0.78 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[ESCO2]] | +0.78 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[C21orf58]] | +0.77 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[DMC1]] | +0.76 | +0.70 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[RAD51AP1]] | +0.76 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[E2F2]] | +0.75 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[RMI2]] | +0.74 | +0.69 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ATAD5]] | +0.74 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[ZGRF1]] | +0.73 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[ZNF367]] | +0.73 | +0.65 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GPR19's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TLCD3B]] | B | TLCD3B activity raises GPR19's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 1.88× lower at baseline in the lines without TLCD3B | 0.097 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZGRF1]] | B | GPR19 activity raises ZGRF1's level | lines that do not express GPR19 (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without GPR19 | 0.060 | ⚠ within organs, on part of the lines; also absent: DBNDD1, GPR137B, ERO1B; maybe low, not absent; its own permutation p |
| [[C1orf112]] | B | GPR19 activity raises C1orf112's level | lines that do not express GPR19 (6) vs lines expressing it (44) | 1.50× lower at baseline in the lines without GPR19 | 0.060 | ⚠ within organs, on part of the lines; also absent: DBNDD1, GPR137B, ERO1B; maybe low, not absent; its own permutation p |
| [[MGME1]] | B | GPR19 activity raises MGME1's level | lines that do not express GPR19 (6) vs lines expressing it (44) | 1.31× lower at baseline in the lines without GPR19 | 0.060 | ⚠ within organs, on part of the lines; also absent: DBNDD1, GPR137B, ERO1B; maybe low, not absent; its own permutation p |
| [[MCM8]] | B | GPR19 activity raises MCM8's level | lines that do not express GPR19 (6) vs lines expressing it (44) | 1.52× lower at baseline in the lines without GPR19 | 0.091 | ⚠ within organs, on part of the lines; also absent: DBNDD1, GPR137B, ERO1B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.740). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.5, -46.9); signed map (-41.0, -46.9). **Vector** length 62.0, 10.4% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.55 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +15.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +2.9 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +2.8 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | +2.4 | +6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +2.4 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +1.6 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +1.6 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.1 | +2.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -3.2 | -7.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.2 | -7.2 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.1 | -3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -4.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -1.8 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -4.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.1 — chr12:12,660,890-12,696,207 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | G protein-coupled receptors, Class A orphans |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15760](https://www.uniprot.org/uniprotkb/Q15760) (Probable G protein-coupled receptor 19):

> G protein-coupled receptor that plays a role in the regulation of circadian rhythms and energy metabolism. Participates in maintaining proper circadian gene expression in the suprachiasmatic nucleus (SCN), the locus of the master circadian clock in the brain (By similarity). May function as a coordinator of aging-associated metabolic dysfunction, stress response, DNA integrity management, and eventual senescence. Upon binding to adropin, modulates mitochondrial energy metabolism via the …

**Summary**, from NCBI Gene [2842](https://www.ncbi.nlm.nih.gov/gene/2842):

> Enables G protein-coupled receptor activity. Involved in G protein-coupled receptor signaling pathway. Located in cilium. Is active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:4473](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4473) · Entrez [2842](https://www.ncbi.nlm.nih.gov/gene/2842) · UniProt [Q15760](https://www.uniprot.org/uniprotkb/Q15760) · Ensembl [ENSG00000183150](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183150)

## Data

Gene col 11374: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11374); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11374, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11374]; `tensor/DDL_lfc|DDL_z.npy` [11374]; `embed/gene_vectors.npy` [11374]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11374 or target_col == 11374). Every well: [[GPR19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPR19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "PYGM"
type: "gene"
col: 907
ensembl_id: "ENSG00000068976"
name: "glycogen phosphorylase, muscle associated"
location: "11q13.1"
module: 38
arm: "+"
pooled_cpm: 7.2
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/038", "written"]
generated_by: "tahoemap"
---

# PYGM

*glycogen phosphorylase, muscle associated* — 11q13.1

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> PYGM encodes muscle glycogen phosphorylase, the enzyme that releases glucose-1-phosphate from glycogen in skeletal muscle; its loss causes McArdle disease.

## What it is

One of the classical allosteric enzymes: a pyridoxal-phosphate-dependent homodimer, switched on covalently by phosphorylase kinase downstream of calcium and adrenergic signalling, and tuned allosterically by AMP and ATP. It is the muscle-specific member of a three-gene family, with liver PYGL and brain PYGB, and supplies the glycolytic flux that powers burst exercise. Recessive loss of function causes glycogen storage disease type V, McArdle disease: exercise intolerance, cramps, rhabdomyolysis, and the characteristic "second wind" as the body switches to oxidative fuel. The biochemistry is unusually well settled for a gene this specialised; the gene's own transcriptional control outside muscle differentiation has had little attention.

## What is uncertain

PYGM is a muscle transcript detected at a trickle in non-muscle lines, so almost anything that shifts detection of lowly expressed genes shifts it: sequencing depth, ambient RNA, drug-induced changes in total RNA content. PYGM also carries the readthrough-geometry flag — it sits a short distance 3' of a much higher-expressed same-strand gene, so part of what is counted as PYGM may be its neighbour's transcription ([[Readthrough spillover]]). In the earlier MG53/p53 study it tracked measured MG53, a trace muscle transcript with the same vulnerabilities, so nothing there separated co-regulation from co-measurement.

## References

- Tsujino et al., 1993, New England Journal of Medicine — identified mutations in muscle glycogen phosphorylase as the cause of McArdle disease.
- Nogales-Gadea et al., 2015, Human Mutation — curated the reported PYGM mutation spectrum in McArdle disease.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.44× (z +11.7, q 8e-29, up in 37 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.373× (z -6.6, q 2e-08, down in 26 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.454× (z -5.1, q 1e-04, down in 26 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VWCE]] (+0.88, fdr 7e-06), [[TRIM72]] (+0.87, fdr 7e-06), [[FNDC7]] (+0.85, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[MYOM1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 907.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.44×** | +11.7 | 8e-29 | 37/41 (PANC-1, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.56×** | +6.0 | 4e-07 | 26/42 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.29×** | +5.5 | 6e-06 | 26/47 (A549, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +5.0 | 9e-05 | 20/42 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +4.8 | 2e-04 | 21/39 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +4.3 | 0.002 | 16/35 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.86×** | +4.1 | 0.003 | 19/48 (SW480, SW 900, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.006 | 18/45 (C32, HT-29, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +3.5 | 0.027 | 20/46 (J82, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[DTP3 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.60×** | +3.1 | 0.093 | 8/47 (HEC-1-A, C32, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.38× | +3.1 | 0.11 | 12/48 (C32, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 907.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.373×** | -6.6 | 2e-08 | 26/42 (LOX-IMVI, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.454×** | -5.1 | 1e-04 | 26/45 (NCI-H1573, BT-474, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.403×** | -4.7 | 5e-04 | 26/45 (J82, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.548×** | -4.0 | 0.008 | 21/46 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.474×** | -3.9 | 0.012 | 20/46 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.565×** | -3.5 | 0.029 | 16/47 (AsPC-1, HepG2/C3A, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.591×** | -3.5 | 0.029 | 16/47 (HEC-1-A, BT-474, …) | top dose only | position effect removed |
| [[Erlotinib (drug)]] 5 µM |  | **0.580×** | -3.5 | 0.029 | 20/45 (CFPAC-1, BT-474, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.581×** | -3.5 | 0.029 | 22/43 (J82, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.605×** | -3.4 | 0.042 | 19/47 (KATO III, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.613×** | -3.3 | 0.052 | 13/47 (LOX-IMVI, A-427, …) | top dose only | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.608×** | -3.2 | 0.055 | 16/44 (HepG2/C3A, Panc 03.27, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM |  | **0.713×** | -3.2 | 0.055 | 13/48 (SW 900, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.597×** | -3.2 | 0.055 | 18/42 (NCI-H460, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.627×** | -3.1 | 0.065 | 18/46 (NCI-H2030, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.425×** | -3.0 | 0.094 | 13/32 (A-427, C32, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 907. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 18.8 | 0 | 3 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.0547× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 20.9 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.166× (z -10.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 8.13 | 0 | 3 (2 ⚠) | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0679× (z -10.7) |
| [[A498 (line)]] | wt | 3.14 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.87× (z +8.6) | [[Mozavaptan (drug)]] 0.5 µM 0.0728× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 10.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.55× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.0540× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 14.0 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0652× (z -11.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0921× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 2 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0459× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 4.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 8.28 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0714× (z -9.9) |
| [[KATO III (line)]] | alt | 6.73 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0427× (z -11.3) |
| [[LoVo (line)]] | wt | 9.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 9.86 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0620× (z -9.8) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 4.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.92× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 5.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.65× (z +9.6) | — |
| [[A-172 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 907), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VWCE]] | +0.88 | +0.87 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[TRIM72]] | +0.87 | +0.89 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[FNDC7]] | +0.85 | +0.86 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[PILRA]] | +0.83 | +0.79 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[LRRC23]] | +0.83 | +0.83 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[SMIM41]] | +0.82 | +0.80 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[ARL9]] | +0.82 | +0.80 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[PPIEL]] | +0.81 | +0.83 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[CPT1C]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[RFPL3S]] | +0.79 | +0.78 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[IDI2-AS1]] | +0.79 | +0.80 / +0.81 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.79 | +0.82 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 9, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYOM1]] | B | MYOM1 activity raises PYGM's level | lines that do not express MYOM1 (9) vs lines expressing it (41) | 1.50× lower at baseline in the lines without MYOM1 | 0.005 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[F2]] | B | F2 activity raises PYGM's level | lines that do not express F2 (11) vs lines expressing it (39) | 1.69× lower at baseline in the lines without F2 | 0.016 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LSMEM2]] | B | LSMEM2 activity raises PYGM's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 1.63× lower at baseline in the lines without LSMEM2 | 0.019 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[PTPN6]] | B | PTPN6 activity raises PYGM's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.78× lower at baseline in the lines without PTPN6 | 0.053 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |
| [[C21orf91-OT1]] | B | C21orf91-OT1 activity raises PYGM's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 1.37× lower at baseline in the lines without C21orf91-OT1 | 0.061 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[TOP2A]] | B | TOP2A activity lowers PYGM's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LMO7DN]] | B | LMO7DN activity raises PYGM's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.38× lower at baseline in the lines without LMO7DN | 0.078 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[HAP1]] | B | HAP1 activity raises PYGM's level | lines that do not express HAP1 (12) vs lines expressing it (38) | 1.54× lower at baseline in the lines without HAP1 | 0.081 | ⚠ within organs, on part of the lines; also absent: HID1, NRARP, PDE9A |
| [[HPN]] | B | HPN activity raises PYGM's level | lines that do not express HPN (6) vs lines expressing it (44) | 1.58× lower at baseline in the lines without HPN | 0.096 | ⚠ within organs, on part of the lines; also absent: NAT14, APBA1; maybe low, not absent |
| [[SLC16A1]] | C | SLC16A1 activity lowers PYGM's level | lines that do not express SLC16A1 (3) vs lines expressing it (47) | 2.19× higher at baseline in the lines without SLC16A1 | 0.047 | ⚠ few lines (3 vs 47); across organs; co-occurs with ERBB2; also absent: SLC16A1-AS1, SLC4A7, PALS2 |
| [[NECAB2]] | C | NECAB2 activity raises PYGM's level | lines that do not express NECAB2 (3) vs lines expressing it (47) | 2.09× lower at baseline in the lines without NECAB2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, PARP11, DLG4; maybe low, not absent; its own permutation p |
| [[C5AR1]] | C | C5AR1 activity raises PYGM's level | lines that do not express C5AR1 (3) vs lines expressing it (47) | 2.04× lower at baseline in the lines without C5AR1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FARP1, PER3, NECAB2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.877). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.3, -16.9); signed map (15.5, 11.6). **Vector** length 116, 29.5% of its response variance represented; |z| ≥ 3 in 1,180 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +11.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.6 | +4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.3 | +2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.8 | +2.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.4 | +1.0 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +3.0 | +2.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.8 | +3.1 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.8 | -4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.0 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.6 | -3.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -4.2 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.7 | -5.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -3.5 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.3 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | glycogen phosphorylase, muscle associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,746,389-64,759,974 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GSD5 |
| Gene groups (HGNC) | Glycogen phosphorylases |
| Hallmark sets | MYOGENESIS, HYPOXIA |
| Reactome | 3 pathways, smallest: Glycogen breakdown (glycogenolysis); Glycogen metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P11217](https://www.uniprot.org/uniprotkb/P11217) (Glycogen phosphorylase, muscle form):

> Allosteric enzyme that catalyzes the rate-limiting step in glycogen catabolism, the phosphorolytic cleavage of glycogen to produce glucose-1-phosphate, and plays a central role in maintaining cellular and organismal glucose homeostasis.

**Summary**, from NCBI Gene [5837](https://www.ncbi.nlm.nih.gov/gene/5837):

> This gene encodes a muscle enzyme involved in glycogenolysis. Highly similar enzymes encoded by different genes are found in liver and brain. Mutations in this gene are associated with McArdle disease (myophosphorylase deficiency), a glycogen storage disease of muscle. Alternative splicing results in multiple transcript variants.[provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:9726](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9726) · Entrez [5837](https://www.ncbi.nlm.nih.gov/gene/5837) · UniProt [P11217](https://www.uniprot.org/uniprotkb/P11217) · Ensembl [ENSG00000068976](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068976)

## Data

Gene col 907: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 907); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 907, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 907]; `tensor/DDL_lfc|DDL_z.npy` [907]; `embed/gene_vectors.npy` [907]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 907 or target_col == 907). Every well: [[PYGM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/PYGM.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

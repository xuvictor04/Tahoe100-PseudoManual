---
symbol: "ROPN1L"
type: "gene"
col: 6997
ensembl_id: "ENSG00000145491"
name: "rhophilin associated tail protein 1 like"
location: "5p15.2"
module: 38
arm: "+"
pooled_cpm: 3.81
n_lines_expressing: 47
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# ROPN1L

*rhophilin associated tail protein 1 like* — 5p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.73× (z +16.6, q 0e+00, up in 33 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.598× (z -4.6, q 0.002, down in 17 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FNDC7]] (+0.82, fdr 7e-06), [[USP50]] (+0.81, fdr 7e-06), [[HCLS1]] (+0.81, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[COQ3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6997.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.73×** | +16.6 | 0e+00 | 33/37 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.62×** | +16.2 | 0e+00 | 32/35 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.37×** | +13.2 | 2e-37 | 35/44 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.35×** | +10.8 | 5e-25 | 33/43 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.99×** | +9.8 | 2e-20 | 30/43 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.93×** | +9.6 | 9e-20 | 25/34 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.59×** | +8.5 | 2e-15 | 24/40 (A-172, LoVo, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +8.1 | 3e-14 | 19/32 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Filgotinib (drug)]] 5 µM |  | **2.19×** | +7.0 | 2e-10 | 24/45 (A498, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +5.7 | 6e-07 | 17/33 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +5.5 | 3e-06 | 13/43 (PANC-1, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +5.4 | 4e-06 | 0/10 | inconsistent across doses | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +5.3 | 5e-06 | 5/11 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.82×** | +5.0 | 2e-05 | 15/40 (SW480, A498, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.0 | 2e-05 | 15/43 (PANC-1, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +4.9 | 3e-05 | 21/41 (HS-578T, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +3.8 | 0.005 | 12/41 (A549, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~18% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6997.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.598×** | -4.6 | 0.002 | 17/42 (LOX-IMVI, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.606×** | -4.5 | 0.002 | 17/40 (LOX-IMVI, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.652×** | -3.8 | 0.022 | 15/42 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.640×** | -3.8 | 0.022 | 10/39 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.709× | -3.1 | 0.23 | 16/43 (NCI-H23, H4, …) | two highest doses | cell-cycle shift (explains ~1% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6997. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.96 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 8.76× (z +10.4) | — |
| [[J82 (line)]] | alt | 5.00 | 0 | 3 (1 ⚠) | — | [[Erlotinib (drug)]] 5 µM 0.0786× (z -8.8) |
| [[A498 (line)]] | wt | 2.56 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.45× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 8.34 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0750× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 3.15 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +9.6) | — |
| [[A549 (line)]] | wt | 2.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.95× (z +8.7) | — |
| [[C32 (line)]] | wt | 5.31 | 0 | 1 | — | [[Asciminib (drug)]] 5 µM 0.0617× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 4.10 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0881× (z -8.7) |
| [[HOP62 (line)]] | alt | 4.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +9.0) | — |
| [[KATO III (line)]] | alt | 3.98 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM 0.0534× (z -8.7) |
| [[LoVo (line)]] | wt | 3.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +11.5) | — |
| [[NCI-H2030 (line)]] | alt | 6.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.56× (z +8.8) | — |
| [[SW480 (line)]] | alt | 2.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +9.4) | — |
| [[A-172 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.897 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6997), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FNDC7]] | +0.82 | +0.86 / +0.77 | both halves | 7e-06 |  |
| [[USP50]] | +0.81 | +0.86 / +0.76 | both halves | 7e-06 |  |
| [[HCLS1]] | +0.81 | +0.81 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[LDHC]] | +0.81 | +0.81 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[MYOCOS]] | +0.80 | +0.84 / +0.74 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.80 | +0.81 / +0.76 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.79 | +0.87 / +0.69 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.78 | +0.81 / +0.70 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.76 | +0.84 / +0.66 | both halves | 7e-06 |  |
| [[ARL9]] | +0.76 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.76 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.75 | +0.78 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ROPN1L's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00334]] | B | LINC00334 activity raises ROPN1L's level | lines that do not express LINC00334 (10) vs lines expressing it (40) | 1.71× lower at baseline in the lines without LINC00334 | 0.036 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent |
| [[ADORA1]] | B | ADORA1 activity raises ROPN1L's level | lines that do not express ADORA1 (7) vs lines expressing it (43) | 1.76× lower at baseline in the lines without ADORA1 | 0.071 | ⚠ within organs, on part of the lines; also absent: DRAM1, HHAT, SUGCT; maybe low, not absent |
| [[MPP4]] | C | MPP4 activity raises ROPN1L's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 1.75× lower at baseline in the lines without MPP4 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COQ3]] | C | ROPN1L activity raises COQ3's level | lines that do not express ROPN1L (3) vs lines expressing it (47) | 1.77× lower at baseline in the lines without ROPN1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NBEAP2, FAM229B, SPDL1; maybe low, not absent; its own permutation p |
| [[BMP8A]] | C | ROPN1L activity raises BMP8A's level | lines that do not express ROPN1L (3) vs lines expressing it (47) | 2.36× lower at baseline in the lines without ROPN1L | 0.069 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NBEAP2, FAM229B, SPDL1; maybe low, not absent; co-absent with the target |
| [[CENPBD2P]] | C | ROPN1L activity raises CENPBD2P's level | lines that do not express ROPN1L (3) vs lines expressing it (47) | 1.74× lower at baseline in the lines without ROPN1L | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NBEAP2, FAM229B, SPDL1; maybe low, not absent; its own permutation p |
| [[POLG2]] | C | ROPN1L activity raises POLG2's level | lines that do not express ROPN1L (3) vs lines expressing it (47) | 1.69× lower at baseline in the lines without ROPN1L | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NBEAP2, FAM229B, SPDL1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.7, -15.9); signed map (16.5, 11.2). **Vector** length 72.7, 12.3% of its response variance represented; |z| ≥ 3 in 1,177 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +16.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +16.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +5.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +7.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +5.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.0 | +2.3 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | +1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.4 | -4.5 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.2 | -3.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | rhophilin associated tail protein 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.2 — chr5:10,441,524-10,472,029 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ASP, FLJ25776, RSPH11, RP11-1C1.7, TCONS_00009352; previously LINC01513 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96C74](https://www.uniprot.org/uniprotkb/Q96C74) (Ropporin-1-like protein):

> Functions as part of axonemal radial spoke complexes that play an important part in the motility of sperm and cilia. Important for male fertility. With ROPN1, involved in fibrous sheath integrity and sperm motility, plays a role in PKA-dependent signaling processes required for spermatozoa capacitation.

**Summary**, from NCBI Gene [83853](https://www.ncbi.nlm.nih.gov/gene/83853):

> This gene encodes a member of the ropporin family. The encoded protein is present in sperm and interacts with A-kinase anchoring protein, AKAP3, through the amphipathic helix region of AKAP3. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Oct 2014]

**Accessions** — [HGNC:24060](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24060) · Entrez [83853](https://www.ncbi.nlm.nih.gov/gene/83853) · UniProt [Q96C74](https://www.uniprot.org/uniprotkb/Q96C74) · Ensembl [ENSG00000145491](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145491)

## Data

Gene col 6997: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6997); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6997, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6997]; `tensor/DDL_lfc|DDL_z.npy` [6997]; `embed/gene_vectors.npy` [6997]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6997 or target_col == 6997). Every well: [[ROPN1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ROPN1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

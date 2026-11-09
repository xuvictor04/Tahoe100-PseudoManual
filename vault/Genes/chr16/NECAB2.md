---
symbol: "NECAB2"
type: "gene"
col: 2327
ensembl_id: "ENSG00000103154"
name: "N-terminal EF-hand calcium binding protein 2"
location: "16q23.3"
module: 47
arm: "+"
pooled_cpm: 2.42
n_lines_expressing: 47
n_dd_up: 27
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/047", "written"]
generated_by: "tahoemap"
---

# NECAB2

*N-terminal EF-hand calcium binding protein 2* — 16q23.3

> [!summary] In one line
> NECAB2 encodes a neuronal EF-hand calcium-binding protein studied almost exclusively as a modulator of striatal G-protein-coupled receptors.

## What it is

NECAB2 is a roughly 43 kDa cytosolic protein with two EF-hand calcium-binding motifs, a NECAB homology region and a C-terminal antibiotic-monooxygenase (ABM) domain of unknown function — an odd pairing, since the ABM fold is otherwise a bacterial oxidoreductase module. Expression is narrow, enriched in striatum and hippocampal CA2. What functional work exists concerns receptor trafficking. A yeast two-hybrid screen identified NECAB2 as a partner of the adenosine A2A receptor C-terminus, and the interaction was reported to alter the receptor's surface expression, internalisation and downstream MAPK activation; an interaction with mGluR5 has also been described. The evidence is from transfected cells and rodent brain. The gene lies at 16q23.3.

## What is uncertain

A neuron-restricted transcript in pooled cancer cell lines should sit close to the detection floor, and at that abundance an apparent correlation is as readily produced by ambient RNA or a few lines of unusual lineage as by regulated expression. No link between NECAB2 and p53 or calcium-dependent membrane repair has been reported, so there is no mechanism against which an association can be judged. The receptor-modulation findings come from a small literature and, as far as I can establish, are unreplicated.

## References

- Canela et al., 2007 — a yeast two-hybrid screen identified NECAB2 as an adenosine A2A receptor interactor and showed it modulates receptor surface expression and internalisation (journal not verified).

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 4.19× (z +11.1, q 6e-26, up in 21 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.364× (z -4.1, q 0.018, down in 8 of 18 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Dexamethasone (drug)]] 5 µM: 0.600× (z -4.0, q 0.018, down in 10 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPP4]] (+0.72, fdr 7e-06), [[PITRM1-AS1]] (+0.70, fdr 7e-06), [[OIT3]] (+0.70, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01564]] → it (grade B ⚠); 5 go from it, the strongest it → [[PILRA]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2327.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **4.19×** | +11.1 | 6e-26 | 21/30 (A-172, SW480, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **4.12×** | +10.4 | 8e-23 | 21/26 (COLO 205, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.54×** | +10.2 | 2e-22 | 16/29 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; position correction uncertain | **3.03×** | +8.3 | 2e-14 | 0/2 | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; position correction uncertain | **3.01×** | +7.9 | 3e-13 | 2/5 (MIA PaCa-2, NCI-H2030) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.35×** | +6.6 | 3e-09 | 13/26 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; position correction uncertain | **2.30×** | +6.5 | 9e-09 | 3/10 (A498, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.92×** | +5.0 | 3e-05 | 10/40 (J82, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.8 | 1e-04 | 8/26 (A549, J82, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.71×** | +4.2 | 0.002 | 1/19 (LOX-IMVI) | inconsistent across doses | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.002 | 3/37 (KATO III, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.67×** | +4.0 | 0.003 | 2/8 (BT-474, A-172) | all doses, flat | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.65×** | +3.9 | 0.004 | 11/41 (A498, NCI-H460, …) | top dose only |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.66×** | +3.8 | 0.007 | 1/15 (A-172) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.64×** | +3.7 | 0.008 | 3/13 (A549, A-172, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.64×** | +3.5 | 0.013 | 3/15 (HEC-1-A, LoVo, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.015 | 5/38 (A498, A-172, …) | rises with dose | position effect removed |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.62×** | +3.4 | 0.017 | 1/17 (A-427) | inconsistent across doses | position effect removed |
| [[SBI-0640756 (drug)]] 5 µM |  | **2.28×** | +3.3 | 0.023 | 0/13 | top dose only | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.83×** | +3.3 | 0.023 | 2/36 (COLO 205, A-172) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.14×** | +3.1 | 0.050 | 1/20 (LOX-IMVI) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +2.9 | 0.092 | 9/32 (COLO 205, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2327.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.364×** | -4.1 | 0.018 | 8/18 (HEC-1-A, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **0.600×** | -4.0 | 0.018 | 10/39 (H4, NCI-H2030, …) | rises with dose |  |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **0.607×** | -3.9 | 0.018 | 11/40 (BT-474, NCI-H2030, …) | top dose only |  |
| [[Econazole (drug)]] 5 µM |  | **0.638×** | -3.5 | 0.063 | 5/40 (Panc 03.27, SW1417, …) | rises with dose |  |
| [[Megestrol (drug)]] 5 µM |  | **0.734×** | -3.4 | 0.067 | 9/39 (Hs 766T, H4, …) | top dose only |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.653×** | -3.3 | 0.080 | 9/40 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Sinomenine (drug)]] 0.5 µM |  | **0.659×** | -3.3 | 0.089 | 2/36 (Panc 03.27, MIA PaCa-2) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2327. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 8.76 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0502× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[A-427 (line)]] | wt | 2.90 | 0 | 1 | — | [[Indacaterol (maleate) (drug)]] 5 µM 0.0483× (z -8.9) |
| [[H4 (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0257× (z -10.1) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.795 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.831 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.766 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.697 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.647 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.869 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.291 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.539 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.598 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.829 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.704 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.691 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.714 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.966 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2327), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP4]] | +0.72 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[OIT3]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[EPHX3]] | +0.70 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[FBXW10B]] | +0.68 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[SCUBE2]] | +0.68 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[ALPK3]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[KIF17]] | +0.65 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[CHRNA10]] | +0.65 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[MIR9-1HG]] | +0.65 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ARL9]] | +0.65 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[MMP25]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01564]] | B | LINC01564 activity raises NECAB2's level | lines that do not express LINC01564 (24) vs lines expressing it (26) | 1.48× lower at baseline in the lines without LINC01564 | 0.069 | ⚠ within organs, on part of the lines; also absent: LINC03040, INAVA, CYP4F11; maybe low, not absent |
| [[SLC7A11]] | B | SLC7A11 activity raises NECAB2's level | lines that do not express SLC7A11 (6) vs lines expressing it (44) | 1.46× lower at baseline in the lines without SLC7A11 | 0.094 | ⚠ within organs, on part of the lines; also absent: CD68; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PILRA]] | C | NECAB2 activity raises PILRA's level | lines that do not express NECAB2 (3) vs lines expressing it (47) | 2.65× lower at baseline in the lines without NECAB2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, PARP11, DLG4; maybe low, not absent; its own permutation p |
| [[COL20A1]] | C | NECAB2 activity raises COL20A1's level | lines that do not express NECAB2 (3) vs lines expressing it (47) | 2.10× lower at baseline in the lines without NECAB2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, PARP11, DLG4; maybe low, not absent; its own permutation p |
| [[PYGM]] | C | NECAB2 activity raises PYGM's level | lines that do not express NECAB2 (3) vs lines expressing it (47) | 2.09× lower at baseline in the lines without NECAB2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, PARP11, DLG4; maybe low, not absent; its own permutation p |
| [[MYO15A]] | C | NECAB2 activity raises MYO15A's level | lines that do not express NECAB2 (3) vs lines expressing it (47) | 1.89× lower at baseline in the lines without NECAB2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, PARP11, DLG4; maybe low, not absent; its own permutation p |
| [[ZDHHC11]] | C | NECAB2 activity raises ZDHHC11's level | lines that do not express NECAB2 (3) vs lines expressing it (47) | 2.14× lower at baseline in the lines without NECAB2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, PARP11, DLG4; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.737). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.6, -14.2); signed map (18.2, 10.5). **Vector** length 57.7, 9.51% of its response variance represented; |z| ≥ 3 in 835 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; position correction uncertain | +5.4 | +8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; position correction uncertain | +4.4 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; position correction uncertain | +4.4 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +10.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +3.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -2.5 | -2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -1.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | N-terminal EF-hand calcium binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.3 — chr16:83,968,244-84,002,776 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously EFCBP2 |
| Gene groups (HGNC) | N-terminal EF-hand calcium binding proteins; EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6G3](https://www.uniprot.org/uniprotkb/Q7Z6G3) (N-terminal EF-hand calcium-binding protein 2):

> May act as a signaling scaffold protein that senses intracellular calcium. Can modulate ligand-induced internalization of ADORA2A and coupling efficiency of mGluR5/GRM5; for both receptors may regulate signaling activity such as promoting MAPK1/3 (ERK1/2) activation.

**Summary**, from NCBI Gene [54550](https://www.ncbi.nlm.nih.gov/gene/54550):

> The protein encoded by this gene is a neuronal calcium-binding protein that binds to and modulates the function of at least two receptors, adenosine A(2A) receptor and metabotropic glutamate receptor type 5. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:23746](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23746) · Entrez [54550](https://www.ncbi.nlm.nih.gov/gene/54550) · UniProt [Q7Z6G3](https://www.uniprot.org/uniprotkb/Q7Z6G3) · Ensembl [ENSG00000103154](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103154)

## Data

Gene col 2327: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2327); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2327, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2327]; `tensor/DDL_lfc|DDL_z.npy` [2327]; `embed/gene_vectors.npy` [2327]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2327 or target_col == 2327). Every well: [[NECAB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/NECAB2.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "ARHGAP11B"
type: "gene"
col: 16087
ensembl_id: "ENSG00000285077"
name: "Rho GTPase activating protein 11B"
location: "15q13.2"
module: 67
arm: "+"
pooled_cpm: 4.01
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# ARHGAP11B

*Rho GTPase activating protein 11B* — 15q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.93× (z +6.1, q 8e-07, up in 2 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.59× (z +4.4, q 9e-04, up in 11 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.655× (z -5.7, q 5e-06, down in 24 of 45 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 0.560× (z -5.6, q 8e-06, down in 19 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BUB1B]] (+0.90, fdr 7e-06), [[INCENP]] (+0.87, fdr 7e-06), [[ARHGAP11A]] (+0.87, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16087.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +6.1 | 8e-07 | 2/6 (PANC-1, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.69×** | +5.0 | 1e-04 | 15/35 (SW1417, HT-29, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +4.9 | 2e-04 | 5/11 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.61×** | +4.6 | 8e-04 | 6/24 (SW1417, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +4.4 | 9e-04 | 11/43 (KATO III, A549, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +4.4 | 9e-04 | 6/20 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +4.0 | 0.006 | 15/46 (CFPAC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.48×** | +3.7 | 0.013 | 9/44 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.42×** | +3.3 | 0.057 | 9/46 (KATO III, LS 180, …) | two highest doses | composition shift |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.43×** | +3.2 | 0.073 | 11/42 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.89×** | +3.2 | 0.073 | 0/9 | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16087.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.655×** | -5.7 | 5e-06 | 24/45 (SW48, SNU-1, …) | rises with dose | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.560×** | -5.6 | 8e-06 | 19/44 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.568×** | -5.4 | 1e-05 | 18/45 (A498, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.584×** | -5.2 | 4e-05 | 15/44 (SW480, H4, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.626×** | -4.5 | 8e-04 | 13/44 (H4, C-33 A, …) | two highest doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.661×** | -3.8 | 0.012 | 16/43 (NCI-H1792, BT-474, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.700×** | -3.4 | 0.050 | 12/44 (LOX-IMVI, NCI-H2030, …) | rises with dose | position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | **0.782×** | -3.3 | 0.059 | 11/44 (SNU-423, COLO 205, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.712×** | -3.3 | 0.070 | 10/37 (LoVo, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.705×** | -3.2 | 0.079 | 14/43 (HOP62, LS 180, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | **0.710×** | -3.2 | 0.079 | 7/42 (SNU-1, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16087. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.57 | 0 | 1 (1 ⚠) | — | [[Ornidazole (drug)]] 0.5 µM 0.0581× (z -8.7) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 3.87 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0946× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 2.93 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0709× (z -10.0) |
| [[SHP-77 (line)]] | alt | 7.52 | 0 | 1 | — | [[Busulfan (drug)]] 0.5 µM 0.0756× (z -8.5) |
| [[A-427 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16087), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BUB1B]] | +0.90 | +0.89 / +0.89 | both halves | 7e-06 | STRING 608 |
| [[INCENP]] | +0.87 | +0.86 / +0.86 | both halves | 7e-06 |  |
| [[ARHGAP11A]] | +0.87 | +0.85 / +0.86 | both halves | 7e-06 | same gene group; pathway: RHOA GTPase cycle |
| [[TROAP]] | +0.87 | +0.84 / +0.86 | both halves | 7e-06 |  |
| [[TACC3]] | +0.87 | +0.88 / +0.84 | both halves | 7e-06 |  |
| [[KIF4A]] | +0.87 | +0.84 / +0.86 | both halves | 7e-06 |  |
| [[DEPDC1B]] | +0.87 | +0.84 / +0.84 | both halves | 7e-06 | pathway: CDC42 GTPase cycle |
| [[CIT]] | +0.86 | +0.85 / +0.88 | both halves | 7e-06 | pathway: RHOA GTPase cycle |
| [[PRC1]] | +0.85 | +0.81 / +0.84 | both halves | 7e-06 |  |
| [[KIF23]] | +0.85 | +0.83 / +0.83 | both halves | 7e-06 |  |
| [[SPAG5]] | +0.85 | +0.84 / +0.83 | both halves | 7e-06 | STRING 590 |
| [[KIFC1]] | +0.85 | +0.84 / +0.83 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises ARHGAP11B's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without PIMREG | 0.044 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[FAM72B]] | B | FAM72B activity raises ARHGAP11B's level | lines that do not express FAM72B (6) vs lines expressing it (44) | 1.21× lower at baseline in the lines without FAM72B | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC02798, SRGAP2C, ZNF512B; its own permutation p |
| [[NDC80]] | C | NDC80 activity raises ARHGAP11B's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 1.77× lower at baseline in the lines without NDC80 | 0.033 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[PBK]] | C | PBK activity raises ARHGAP11B's level | lines that do not express PBK (4) vs lines expressing it (46) | 1.78× lower at baseline in the lines without PBK | 0.044 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises ARHGAP11B's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.74× lower at baseline in the lines without AURKB | 0.072 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CDCA3]] | C | CDCA3 activity raises ARHGAP11B's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 1.91× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.812). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-36.2, -54.8); signed map (-48.2, -42.2). **Vector** length 66.9, 10.6% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.73 to 12); *G2/M checkpoint* (hallmark, mean cos +0.73 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.69 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.3 | +3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +1.9 | +4.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +1.7 | +4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +1.5 | +3.3 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.3 | +1.1 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.1 | +1.5 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +0.9 | +3.2 |
|  | [[Pentagastrin (drug)]] 5 µM |  | +0.8 | +1.5 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +0.7 | +1.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.0 | -5.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -3.0 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -5.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 11B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q13.2 — chr15:30,624,494-30,649,529 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B'-T; previously FAM7B1 |
| Gene groups (HGNC) | Rho GTPase activating proteins |
| Reactome | 5 pathways, smallest: RHOA GTPase cycle; CDC42 GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3KRB8](https://www.uniprot.org/uniprotkb/Q3KRB8) (Inactive Rho GTPase-activating protein 11B):

> Hominin-specific protein that promotes development and evolutionary expansion of the brain neocortex. Able to promote amplification of basal progenitors in the subventricular zone, producing more neurons during fetal corticogenesis, thereby playing a key role in neocortex expansion. Promotes the proliferation of basal progenitors by inhibiting the mitochondrial permeability transition pore (mPTP): delays the opening of the mPTP via interaction with ADP:ATP translocase, thereby increasing …

**Summary**, from NCBI Gene [89839](https://www.ncbi.nlm.nih.gov/gene/89839):

> Predicted to enable GTPase activator activity. Involved in cerebral cortex development and negative regulation of mitochondrial membrane permeability. Acts upstream of with a positive effect on L-glutamine catabolic process. Located in mitochondrial matrix. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15782) · Entrez [89839](https://www.ncbi.nlm.nih.gov/gene/89839) · UniProt [Q3KRB8](https://www.uniprot.org/uniprotkb/Q3KRB8) · Ensembl [ENSG00000285077](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000285077)

## Data

Gene col 16087: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16087); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16087, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16087]; `tensor/DDL_lfc|DDL_z.npy` [16087]; `embed/gene_vectors.npy` [16087]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16087 or target_col == 16087). Every well: [[ARHGAP11B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP11B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

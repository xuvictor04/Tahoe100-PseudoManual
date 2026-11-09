---
symbol: "SDF2"
type: "gene"
col: 5341
ensembl_id: "ENSG00000132581"
name: "stromal cell derived factor 2"
location: "17q11.2"
module: 212
arm: "+"
pooled_cpm: 27.11
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/212"]
generated_by: "tahoemap"
---

# SDF2

*stromal cell derived factor 2* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.66× (z +7.6, q 2e-11, up in 35 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 1.28× (z +3.7, q 0.014, up in 15 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.712× (z -5.1, q 2e-04, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATAT1]] (+0.68, fdr 7e-06), [[MED31]] (+0.66, fdr 1e-05), [[GP6-AS1]] (+0.66, fdr 7e-06); moves opposite to [[THOC7]] (-0.67, fdr 1e-05), [[POGLUT1]] (-0.62, fdr 2e-05), [[PARD3B]] (-0.61, fdr 1e-05).
> It is in [[Module 212]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TMEM92-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5341.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +7.6 | 2e-11 | 35/45 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.60×** | +7.3 | 7e-11 | 34/46 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.64×** | +7.2 | 2e-10 | 24/38 (NCI-H460, C32, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.47×** | +6.0 | 2e-07 | 29/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.47×** | +6.0 | 3e-07 | 31/48 (SW480, HEC-1-A, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.35×** | +4.7 | 2e-04 | 23/48 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.35×** | +4.7 | 2e-04 | 24/48 (HEC-1-A, SW480, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.29×** | +4.0 | 0.005 | 21/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.8 | 0.009 | 16/48 (J82, HEC-1-A, …) | top dose only | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.014 | 15/48 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.017 | 16/48 (NCI-H2030, SW48, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.036 | 22/48 (HT-29, NCI-H23, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.3 | 0.039 | 0/48 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.22×** | +3.1 | 0.076 | 17/48 (NCI-H460, BT-474, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5341.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.712×** | -5.1 | 2e-04 | 21/47 (Panc 03.27, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.819×** | -4.4 | 0.002 | 23/47 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.764×** | -4.1 | 0.009 | 20/34 (SW 900, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.773×** | -3.9 | 0.014 | 20/47 (RPMI-7951, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.774×** | -3.8 | 0.014 | 20/48 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.840× | -3.8 | 0.014 | 19/48 (SW 1088, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.794×** | -3.5 | 0.035 | 16/48 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.787×** | -3.5 | 0.035 | 17/48 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.803×** | -3.4 | 0.035 | 18/47 (A-427, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.806×** | -3.4 | 0.040 | 11/48 (COLO 205, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5341. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 25.8 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 30.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.325× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.488× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 32.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.9) |
| [[A-427 (line)]] | wt | 17.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -9.5) |
| [[A498 (line)]] | wt | 38.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.413× (z -8.5) |
| [[A549 (line)]] | wt | 31.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -8.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.146× (z -12.2) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.276× (z -8.6) ⚠ toxic |
| [[SW 900 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -11.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 25.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.38× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[A-172 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5341), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATAT1]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[MED31]] | +0.66 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[GP6-AS1]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[BIN3]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[CCDC32]] | +0.65 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[ZNHIT1]] | +0.65 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[ADIPOR1]] | +0.65 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[INTS4]] | +0.65 | +0.59 / +0.57 | both halves | 8e-06 |  |
| [[FBXL12]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[OGG1]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[SEZ6L2]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[AP1S1]] | +0.63 | +0.54 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC7]] | -0.67 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[POGLUT1]] | -0.62 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[PARD3B]] | -0.61 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[AASDHPPT]] | -0.58 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[U2SURP]] | -0.58 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[OTUD4]] | -0.58 | -0.58 / -0.43 | both halves | 4e-05 |  |
| [[CFL2]] | -0.58 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[HNRNPU]] | -0.57 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.57 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[DST]] | -0.57 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[DPH5]] | -0.57 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[ZNF252P-1]] | -0.56 | -0.57 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity raises SDF2's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 1.24× lower at baseline in the lines without TMEM92-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[CIB1]] | C | CIB1 activity raises SDF2's level | lines that do not express CIB1 (4) vs lines expressing it (46) | 1.48× lower at baseline in the lines without CIB1 | 0.061 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 212]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.816). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.9, -25.0); signed map (-43.0, 9.5). **Vector** length 93.6, 21.8% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.3 | +6.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.8 | +3.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +2.8 | +7.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.6 | +6.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.4 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.5 | +0.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.4 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +3.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.9 | -5.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.8 | -3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.5 | -3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.9 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.5 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.3 | -1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | stromal cell derived factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,648,346-28,662,189 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [Q99470](https://www.uniprot.org/uniprotkb/Q99470) carries no function annotation.

**Summary**, from NCBI Gene [6388](https://www.ncbi.nlm.nih.gov/gene/6388):

> The protein encoded by this gene is believed to be a secretory protein. It has regions of similarity to hydrophilic segments of yeast mannosyltransferases. Its expression is ubiquitous and the gene appears to be relatively conserved among mammals. Alternate splicing results in both coding and non-coding variants. A pseudogene of this gene is located on chromosome 15. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:10675](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10675) · Entrez [6388](https://www.ncbi.nlm.nih.gov/gene/6388) · UniProt [Q99470](https://www.uniprot.org/uniprotkb/Q99470) · Ensembl [ENSG00000132581](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132581)

## Data

Gene col 5341: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5341); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5341, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5341]; `tensor/DDL_lfc|DDL_z.npy` [5341]; `embed/gene_vectors.npy` [5341]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5341 or target_col == 5341). Every well: [[SDF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "STAC3"
type: "gene"
col: 11684
ensembl_id: "ENSG00000185482"
name: "SH3 and cysteine rich domain 3"
location: "12q13.3"
module: 47
arm: "+"
pooled_cpm: 3.44
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 14
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# STAC3

*SH3 and cysteine rich domain 3* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.43× (z +7.8, q 4e-12, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.68× (z +6.7, q 4e-09, up in 20 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.287× (z -11.5, q 7e-28, down in 36 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFAP161]] (+0.72, fdr 7e-06), [[ZDHHC11]] (+0.71, fdr 7e-06), [[SCUBE2]] (+0.70, fdr 8e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SPOCK2]] → it (grade B ⚠); 2 go from it, the strongest it → [[GARIN1A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11684.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.43×** | +7.8 | 4e-12 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +6.7 | 4e-09 | 20/35 (C32, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +5.6 | 4e-06 | 9/18 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +5.0 | 7e-05 | 2/4 (PANC-1, MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | 1.44× | +3.3 | 0.10 | 3/43 (AsPC-1, SNU-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.41× | +3.1 | 0.13 | 5/46 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.1 | 0.13 | 3/47 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11684.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.287×** | -11.5 | 7e-28 | 36/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.378×** | -8.9 | 1e-16 | 24/31 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.387×** | -8.7 | 5e-16 | 30/42 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.470×** | -6.9 | 5e-10 | 26/42 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.328×** | -5.4 | 9e-06 | 21/40 (BT-474, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.593×** | -4.8 | 1e-04 | 19/43 (J82, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.622×** | -4.2 | 0.003 | 11/19 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.655×** | -3.9 | 0.007 | 13/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.667×** | -3.6 | 0.023 | 10/43 (Panc 03.27, NCI-H1573, …) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.681×** | -3.5 | 0.023 | 9/44 (A-427, A498, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.673×** | -3.5 | 0.026 | 14/39 (SW1417, SW480, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.768×** | -3.4 | 0.027 | 10/43 (SW480, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.693×** | -3.4 | 0.032 | 18/43 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.526×** | -3.1 | 0.081 | 11/34 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11684. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 6.76 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0727× (z -13.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 6.71 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0651× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.119× (z -8.6) |
| [[PANC-1 (line)]] | alt | 2.73 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0460× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 5.43 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0871× (z -9.7) ⚠ toxic |
| [[KATO III (line)]] | alt | 4.26 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0750× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 3.93 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0489× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 4.70 | 0 | 1 | — | [[Aliskiren (drug)]] 0.5 µM 0.0628× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 5.05 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0927× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.103× (z -10.3) ⚠ toxic |
| [[A-172 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11684), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP161]] | +0.72 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[ZDHHC11]] | +0.71 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[SCUBE2]] | +0.70 | +0.72 / +0.58 | both halves | 8e-06 |  |
| [[C3orf20]] | +0.67 | +0.76 / +0.51 | both halves | 1e-05 |  |
| [[ITPR2-AS1]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[PPIEL-1]] | +0.67 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[EPHX3]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[SLC2A9]] | +0.65 | +0.80 / +0.43 | both halves | 3e-05 |  |
| [[GAL3ST2]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[C19orf18]] | +0.65 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[NLGN3]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[R3HDM2]] | +0.65 | +0.73 / +0.44 | both halves | 3e-05 | ⚠ **readthrough risk**: this gene lies 2.6 kb 3′ of R3HDM2 on the same strand (can correlate by spillover, not regulation) |
| [[GARIN1A]] | +0.64 | +0.67 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPOCK2]] | B | SPOCK2 activity raises STAC3's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.67× lower at baseline in the lines without SPOCK2 | 0.022 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |
| [[FAM66C]] | B | FAM66C activity raises STAC3's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.31× lower at baseline in the lines without FAM66C | 0.058 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[NEK10]] | B | NEK10 activity raises STAC3's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without NEK10 | 0.062 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[ITPR2-AS1]] | C | ITPR2-AS1 activity raises STAC3's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 1.73× lower at baseline in the lines without ITPR2-AS1 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GARIN1A]] | C | STAC3's natural level strengthens GARIN1A's drug response | STAC3's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.12; direction not clear | 0.029 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | STAC3's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | STAC3's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.57 | 0.519 over the table, 0.094 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.0, -11.8); signed map (19.5, 7.2). **Vector** length 55.0, 7.11% of its response variance represented; |z| ≥ 3 in 1,173 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +7.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.0 | +1.0 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +0.9 | +1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +0.9 | +0.6 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +0.9 | +2.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -8.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.6 | -6.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -11.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.1 | -8.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -3.5 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | SH3 and cysteine rich domain 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:57,243,453-57,251,188 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2793 |
| Gene groups (HGNC) | SH3 and cysteine rich domain family; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MF2](https://www.uniprot.org/uniprotkb/Q96MF2) (SH3 and cysteine-rich domain-containing protein 3):

> Required for normal excitation-contraction coupling in skeletal muscle and for normal muscle contraction in response to membrane depolarization. Required for normal Ca(2+) release from the sarcplasmic reticulum, which ultimately leads to muscle contraction. Probably functions via its effects on muscle calcium channels. Increases CACNA1S channel activity, in addition to its role in enhancing the expression of CACNA1S at the cell membrane. Has a redundant role in promoting the expression of the …

**Summary**, from NCBI Gene [246329](https://www.ncbi.nlm.nih.gov/gene/246329):

> The protein encoded by this gene is a component of the excitation-contraction coupling machinery of muscles. This protein is a member of the Stac gene family and contains an N-terminal cysteine-rich domain and two SH3 domains. Mutations in this gene are a cause of Native American myopathy. [provided by RefSeq, Nov 2013]

**Accessions** — [HGNC:28423](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28423) · Entrez [246329](https://www.ncbi.nlm.nih.gov/gene/246329) · UniProt [Q96MF2](https://www.uniprot.org/uniprotkb/Q96MF2) · Ensembl [ENSG00000185482](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185482)

## Data

Gene col 11684: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11684); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11684, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11684]; `tensor/DDL_lfc|DDL_z.npy` [11684]; `embed/gene_vectors.npy` [11684]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11684 or target_col == 11684). Every well: [[STAC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

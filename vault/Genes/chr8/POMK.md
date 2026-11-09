---
symbol: "POMK"
type: "gene"
col: 11750
ensembl_id: "ENSG00000185900"
name: "protein O-mannose kinase"
location: "8p11.21"
module: 153
arm: "+"
pooled_cpm: 22.19
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# POMK

*protein O-mannose kinase* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.40× (z +6.9, q 4e-09, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.549× (z -8.7, q 2e-15, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SF3B4]] (+0.68, fdr 1e-05), [[TRUB1]] (+0.68, fdr 7e-06), [[ATP13A1]] (+0.66, fdr 1e-05); moves opposite to [[RABGEF1]] (-0.63, fdr 7e-06), [[MYO9B]] (-0.61, fdr 3e-05), [[TPT1]] (-0.60, fdr 1e-05).
> It is in [[Module 153]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ZNF618]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11750.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +6.9 | 4e-09 | 30/48 (Hs 766T, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +5.9 | 1e-06 | 29/47 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +5.6 | 5e-06 | 30/48 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +4.4 | 0.001 | 22/46 (HOP62, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.4 | 0.001 | 21/48 (LOX-IMVI, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +3.8 | 0.014 | 17/46 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.7 | 0.015 | 19/48 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.017 | 12/48 (HepG2/C3A, CFPAC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.5 | 0.025 | 14/47 (RKO, SW48, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.035 | 20/46 (HS-578T, PANC-1, …) | all doses, flat | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.035 | 12/46 (MIA PaCa-2, C32, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.036 | 8/47 (LOX-IMVI, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11750.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.549×** | -8.7 | 2e-15 | 35/48 (HEC-1-A, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.567×** | -8.3 | 4e-14 | 41/48 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.574×** | -8.1 | 1e-13 | 36/47 (HEC-1-A, SW48, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -4.7 | 5e-04 | 21/46 (HEC-1-A, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.730×** | -4.6 | 5e-04 | 21/48 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.732×** | -4.5 | 6e-04 | 24/46 (A-172, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.832×** | -3.8 | 0.013 | 22/48 (HOP62, HCT15, …) | top dose only | position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **0.798×** | -3.3 | 0.075 | 14/46 (hTERT-HPNE, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.813× | -3.0 | 0.16 | 16/47 (NCI-H460, NCI-H23, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11750. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 14.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -12.2) ⚠ cell-cycle shift, explains ~11% of this change |
| [[HCT15 (line)]] | alt | 41.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 37.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0902× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 25.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.377× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 34.0 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0822× (z -9.8) |
| [[SNU-423 (line)]] | alt | 12.1 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.179× (z -9.5) |
| [[SW48 (line)]] | wt | 36.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0482× (z -16.6) ⚠ cell-cycle shift, explains ~24% of this change |
| [[A-172 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11750), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SF3B4]] | +0.68 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[TRUB1]] | +0.68 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[ATP13A1]] | +0.66 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[ALG10B]] | +0.65 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[U2AF2]] | +0.65 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TARBP2]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[MANEA]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[EWSR1]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[RBBP9]] | +0.63 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[EXOSC10]] | +0.63 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[MTA2]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[FECH]] | +0.62 | +0.50 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGEF1]] | -0.63 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[MYO9B]] | -0.61 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[TPT1]] | -0.60 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[WDR44]] | -0.60 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[LRRFIP1]] | -0.57 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[DDT]] | -0.56 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[PLIN3]] | -0.55 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[PNPLA8]] | -0.55 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[RPL28]] | -0.55 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[TPT1-AS1]] | -0.55 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[COX6A1]] | -0.55 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[NPC1]] | -0.55 | -0.52 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF618]] | B | ZNF618 activity raises POMK's level | lines that do not express ZNF618 (9) vs lines expressing it (41) | 1.64× lower at baseline in the lines without ZNF618 | 0.026 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63 |
| [[HDAC6]] | B | HDAC6 activity raises POMK's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MYO1E]] | B | MYO1E activity lowers POMK's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 1.65× higher at baseline in the lines without MYO1E | 0.079 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[ZNF618]] | B | ZNF618 activity strengthens POMK's drug response | lines that do not express ZNF618 (9) vs lines expressing it (39) | the lines without ZNF618 respond 0.75× as strongly (z diff +0.82); strongest at Belinostat 5 µM: 0.67x vs 0.55x (z diff +1.7) | 0.099 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.0, 1.4); signed map (-10.6, -36.2). **Vector** length 89.3, 18.7% of its response variance represented; |z| ≥ 3 in 832 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.2 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.8 | +2.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +5.2 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.7 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.6 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +3.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.0 | -8.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.6 | -4.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -4.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.3 | -8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -1.5 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.5 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | protein O-mannose kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:43,093,498-43,131,180 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23356, SgK196 |
| Gene groups (HGNC) | Carbohydrate kinases |
| Reactome | 3 pathways, smallest: DAG1 core M3 glycosylations; DAG1 glycosylations; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H5K3](https://www.uniprot.org/uniprotkb/Q9H5K3) (Protein O-mannose kinase):

> Protein O-mannose kinase that specifically mediates phosphorylation at the 6-position of an O-mannose of the trisaccharide (N-acetylgalactosamine (GalNAc)-beta-1,3-N-acetylglucosamine (GlcNAc)-beta-1,4-mannose) to generate phosphorylated O-mannosyl trisaccharide (N-acetylgalactosamine-beta-1,3-N-acetylglucosamine-beta-1,4-(phosphate-6-)mannose). Phosphorylated O-mannosyl trisaccharide is a carbohydrate structure present in alpha-dystroglycan (DAG1), which is required for binding laminin G-like …

**Summary**, from NCBI Gene [84197](https://www.ncbi.nlm.nih.gov/gene/84197):

> This gene encodes a protein that may be involved in the presentation of the laminin-binding O-linked carbohydrate chain of alpha-dystroglycan (a-DG), which forms transmembrane linkages between the extracellular matrix and the exoskeleton. Some pathogens use this O-linked carbohydrate unit for host entry. Loss of function compound heterozygous mutations in this gene were found in a human patient affected by the Walker-Warburg syndrome (WWS) phenotype. Mice lacking this gene contain misplaced …

**Accessions** — [HGNC:26267](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26267) · Entrez [84197](https://www.ncbi.nlm.nih.gov/gene/84197) · UniProt [Q9H5K3](https://www.uniprot.org/uniprotkb/Q9H5K3) · Ensembl [ENSG00000185900](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185900)

## Data

Gene col 11750: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11750); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11750, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11750]; `tensor/DDL_lfc|DDL_z.npy` [11750]; `embed/gene_vectors.npy` [11750]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11750 or target_col == 11750). Every well: [[POMK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POMK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

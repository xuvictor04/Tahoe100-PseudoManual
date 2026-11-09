---
symbol: "ARSK"
type: "gene"
col: 8918
ensembl_id: "ENSG00000164291"
name: "arylsulfatase family member K"
location: "5q15"
module: 79
arm: "+"
pooled_cpm: 22.43
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 14
n_dd_up_clean: 21
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# ARSK

*arylsulfatase family member K* — 5q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.31× (z +13.4, q 4e-38, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.686× (z -6.0, q 1e-06, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM193B]] (+0.67, fdr 7e-06), [[SAP30-DT]] (+0.66, fdr 7e-06), [[PRKRA]] (+0.65, fdr 7e-06); moves opposite to [[CHMP6]] (-0.62, fdr 7e-06), [[ZNF655]] (-0.57, fdr 3e-05), [[RNF32-AS1]] (-0.57, fdr 2e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[STARD9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8918.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.31×** | +13.4 | 4e-38 | 42/47 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.28×** | +13.2 | 3e-37 | 42/47 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.90×** | +10.3 | 2e-22 | 37/47 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +8.1 | 8e-14 | 27/45 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +7.3 | 3e-11 | 30/47 (NCI-H2347, J82, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +7.2 | 4e-11 | 30/47 (HOP62, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +6.5 | 6e-09 | 30/47 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +6.2 | 3e-08 | 32/47 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +6.2 | 4e-08 | 22/42 (NCI-H2030, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.8 | 3e-07 | 28/47 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.97×** | +5.7 | 7e-07 | 27/47 (LoVo, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +5.0 | 3e-05 | 19/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.32×** | +4.5 | 3e-04 | 15/47 (NCI-H2347, A-172, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.31×** | +4.3 | 8e-04 | 17/47 (HS-578T, Hs 766T, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.64×** | +4.1 | 0.001 | 14/45 (PANC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.002 | 14/47 (HS-578T, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8918.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.686×** | -6.0 | 1e-06 | 26/47 (A-172, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.716×** | -5.3 | 2e-05 | 22/45 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.704×** | -5.3 | 2e-05 | 23/47 (H4, C32, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.802×** | -5.0 | 9e-05 | 21/46 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.720×** | -4.8 | 1e-04 | 21/38 (H4, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.732×** | -4.7 | 3e-04 | 19/47 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **0.752×** | -4.2 | 0.002 | 18/45 (SNU-1, LS 180, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.776×** | -4.0 | 0.003 | 16/47 (PANC-1, A-172, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -4.0 | 0.003 | 2/47 (SW 1271, SNU-1) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.779×** | -4.0 | 0.004 | 16/45 (hTERT-HPNE, SW480, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.772×** | -3.9 | 0.005 | 15/31 (LS 180, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.793×** | -3.7 | 0.010 | 20/47 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ivermectin (drug)]] 5 µM |  | **0.804×** | -3.5 | 0.022 | 11/47 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.805×** | -3.1 | 0.079 | 17/47 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.825×** | -3.1 | 0.079 | 17/42 (LS 180, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8918. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 43.8 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.74× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -13.2) |
| [[A498 (line)]] | wt | 22.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -12.5) |
| [[PANC-1 (line)]] | alt | 49.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 22.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.45× (z +9.1) | — |
| [[A-427 (line)]] | wt | 22.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.5) |
| [[H4 (line)]] | wt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -11.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 31.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.357× (z -9.2) |
| [[Hs 766T (line)]] | wt | 26.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -9.1) |
| [[HS-578T (line)]] | alt | 38.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -13.2) |
| [[LoVo (line)]] | wt | 12.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.26× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -11.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 31.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -9.4) |
| [[A549 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8918), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM193B]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[SAP30-DT]] | +0.66 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[PRKRA]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.64 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[PEX3]] | +0.64 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[FAM13A]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[SPATA7]] | +0.61 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[SNAPC3]] | +0.61 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[UBE2O]] | +0.61 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[MALSU1]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[SAP30]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[VKORC1]] | +0.59 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP6]] | -0.62 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[ZNF655]] | -0.57 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[RNF32-AS1]] | -0.57 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[ITPR2-AS1]] | -0.57 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[ALOX12P2-1]] | -0.55 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[FAM83H]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[RBM12]] | -0.54 | -0.37 / -0.57 | both halves | 8e-05 |  |
| [[CUEDC1]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[PSMD11]] | -0.53 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[DDX5]] | -0.53 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[MTNR1A]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[RFFL]] | -0.52 | -0.58 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD9]] | B | STARD9 activity raises ARSK's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.98× lower at baseline in the lines without STARD9 | 0.082 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[GPR155]] | B | GPR155 activity raises ARSK's level | lines that do not express GPR155 (6) vs lines expressing it (44) | 1.69× lower at baseline in the lines without GPR155 | 0.096 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PKIG, TBC1D19; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.7, -16.1); signed map (-36.5, 20.8). **Vector** length 104, 24.9% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *glycolysis* (hallmark, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +3.7 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +7.3 |
|  | [[NG25 (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.9 | +3.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.2 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.2 | -5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.1 | -4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.2 | -3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | -3.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.9 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | arylsulfatase family member K |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q15 — chr5:95,555,101-95,605,102 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp313G1735, TSULF |
| Gene groups (HGNC) | Sulfatases |
| Reactome | 6 pathways, smallest: The activation of arylsulfatases; Glycosphingolipid catabolism; Glycosphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UWY0](https://www.uniprot.org/uniprotkb/Q6UWY0) (Arylsulfatase K):

> Lysosomal sulfatase involved in the degradation of heparan sulfate (also known as heparitin sulfate), and probably other 2-O-sulfoglucuronate-containing glycosaminoglycans. Catalyzes the hydrolysis of the 2-sulfate groups of 2-O-sulfo-D-glucuronate residues. Acts selectively on 2-sulfoglucuronate and lacks activity against 2-sulfoiduronate, which is found in dermatan sulfate. In vitro, it catalyzes with low efficiency the hydrolysis of small sulfated aromatic compounds such as p-nitrocatechol …

**Summary**, from NCBI Gene [153642](https://www.ncbi.nlm.nih.gov/gene/153642):

> Sulfatases (EC 3.1.5.6), such as ARSK, hydrolyze sulfate esters from sulfated steroids, carbohydrates, proteoglycans, and glycolipids. They are involved in hormone biosynthesis, modulation of cell signaling, and degradation of macromolecules (Sardiello et al., 2005 [PubMed 16174644]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:25239](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25239) · Entrez [153642](https://www.ncbi.nlm.nih.gov/gene/153642) · UniProt [Q6UWY0](https://www.uniprot.org/uniprotkb/Q6UWY0) · Ensembl [ENSG00000164291](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164291)

## Data

Gene col 8918: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8918); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8918, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8918]; `tensor/DDL_lfc|DDL_z.npy` [8918]; `embed/gene_vectors.npy` [8918]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8918 or target_col == 8918). Every well: [[ARSK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARSK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

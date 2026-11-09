---
symbol: "RCBTB2"
type: "gene"
col: 5829
ensembl_id: "ENSG00000136161"
name: "RCC1 and BTB domain containing protein 2"
location: "13q14.2"
module: 137
arm: "+"
pooled_cpm: 5.53
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# RCBTB2

*RCC1 and BTB domain containing protein 2* — 13q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.61× (z +4.5, q 0.003, up in 1 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.55× (z +3.5, q 0.097, up in 4 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.175× (z -17.3, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LANCL2]] (+0.71, fdr 2e-05), [[PBLD]] (+0.70, fdr 1e-04), [[AVEN]] (+0.70, fdr 1e-05); moves opposite to [[DNAAF3]] (-0.67, fdr 4e-05), [[TMEM256]] (-0.63, fdr 7e-05), [[SBF2]] (-0.62, fdr 2e-04).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ABCA10]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5829.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +4.5 | 0.003 | 1/11 (C32) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +3.9 | 0.028 | 7/18 (Hs 766T, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +3.5 | 0.097 | 4/47 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.097 | 5/48 (A498, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5829.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.175×** | -17.3 | 0e+00 | 44/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.203×** | -15.8 | 0e+00 | 42/46 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.206×** | -15.7 | 0e+00 | 41/47 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.342×** | -10.7 | 2e-24 | 38/47 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.365×** | -10.0 | 2e-21 | 30/39 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.339×** | -5.6 | 2e-06 | 24/46 (SK-MEL-2, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.597×** | -5.1 | 2e-05 | 20/39 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.396×** | -4.8 | 1e-04 | 12/44 (A498, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.619×** | -4.8 | 1e-04 | 19/44 (A-172, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.655×** | -4.2 | 0.001 | 17/48 (SW 900, PANC-1, …) | rises with dose | composition shift |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.650×** | -4.1 | 0.002 | 18/40 (NCI-H2030, A-172, …) | rises with dose |  |
| [[Silodosin (drug)]] 5 µM |  | **0.661×** | -4.0 | 0.004 | 11/40 (NCI-H1573, COLO 205, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.717×** | -3.3 | 0.040 | 12/42 (HOP62, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5829. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 6.24 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0470× (z -13.2) |
| [[SW480 (line)]] | alt | 7.79 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0711× (z -15.3) |
| [[J82 (line)]] | alt | 7.12 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0694× (z -11.1) |
| [[KATO III (line)]] | alt | 6.39 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0602× (z -10.6) |
| [[A498 (line)]] | wt | 8.31 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0607× (z -13.8) |
| [[AsPC-1 (line)]] | alt | 7.05 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0946× (z -9.4) |
| [[COLO 205 (line)]] | alt | 6.88 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0390× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0885× (z -8.9) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0894× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 6.37 | 0 | 2 | — | [[Panobinostat (drug)]] 0.05 µM 0.0192× (z -15.0) |
| [[NCI-H2030 (line)]] | alt | 4.71 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.0733× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 6.67 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.157× (z -9.5) |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0463× (z -10.5) |
| [[H4 (line)]] | wt | 10.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0457× (z -10.4) |
| [[HCT15 (line)]] | alt | 4.42 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0332× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 5.62 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0702× (z -11.7) |
| [[LoVo (line)]] | wt | 2.73 | 0 | 1 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 0.05 µM 0.0664× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 4.26 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0792× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 6.47 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0603× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 5.14 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0734× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 7.69 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0834× (z -9.6) |
| [[SW 900 (line)]] | alt | 8.52 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0506× (z -11.5) |
| [[A-172 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5829), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LANCL2]] | +0.71 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[PBLD]] | +0.70 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[AVEN]] | +0.70 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[ERMAP]] | +0.69 | +0.60 / +0.38 | both halves | 7e-05 |  |
| [[PRDM11]] | +0.68 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[ARSB]] | +0.67 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[SPRY3]] | +0.67 | +0.59 / +0.22 | both halves | 6e-04 |  |
| [[PCBD2]] | +0.66 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[FIZ1]] | +0.66 | +0.54 / +0.33 | both halves | 1e-04 |  |
| [[FAIM]] | +0.66 | +0.53 / +0.29 | both halves | 2e-04 |  |
| [[EIF5]] | +0.66 | +0.58 / +0.38 | both halves | 7e-05 |  |
| [[PCBP1-AS1]] | +0.66 | +0.52 / +0.29 | both halves | 2e-04 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF3]] | -0.67 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[TMEM256]] | -0.63 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[SBF2]] | -0.62 | -0.55 / -0.29 | both halves | 2e-04 |  |
| [[GMCL1]] | -0.62 | -0.53 / -0.43 | both halves | 3e-05 | same gene group |
| [[HEBP1]] | -0.61 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[KYAT1]] | -0.60 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[ELOB]] | -0.60 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[TSEN54]] | -0.60 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[RRAS]] | -0.60 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[MAST3]] | -0.60 | -0.46 / -0.20 | ⚠ not reproduced | 7e-04 |  |
| [[PLEKHH3]] | -0.59 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[YIF1B]] | -0.59 | -0.34 / -0.24 | both halves | 5e-04 |  |
| [[ARL3]] | -0.59 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA10]] | B | ABCA10 activity raises RCBTB2's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.35× lower at baseline in the lines without ABCA10 | 0.022 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[GRB7]] | B | GRB7 activity lowers RCBTB2's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 1.47× higher at baseline in the lines without GRB7 | 0.039 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[CDS1]] | B | CDS1 activity lowers RCBTB2's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 1.44× higher at baseline in the lines without CDS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[PRSS8]] | B | PRSS8 activity lowers RCBTB2's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 1.46× higher at baseline in the lines without PRSS8 | 0.098 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | RCBTB2's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | RCBTB2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.68 | 0.285 over the table, 0.021 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.750). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-5.8, 8.0); signed map (23.1, -27.6). **Vector** length 77.8, 13.8% of its response variance represented; |z| ≥ 3 in 1,075 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.4 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +2.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.8 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +0.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.5 | +2.3 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.6 | -10.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.3 | -17.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.6 | -10.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.1 | -15.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.6 | -15.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -5.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -2.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.2 | -4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.8 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | RCC1 and BTB domain containing protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.2 — chr13:48,488,963-48,533,256 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CHC1L |
| Gene groups (HGNC) | BTB domain containing |
| Matched by | ensembl_id |

UniProt [O95199](https://www.uniprot.org/uniprotkb/O95199) carries no function annotation.

**Summary**, from NCBI Gene [1102](https://www.ncbi.nlm.nih.gov/gene/1102):

> This gene encodes a protein containing two C-terminal BTB/POZ domains that is related to regulator of chromosome condensation (RCC). The encoded protein may act as a guanine nucleotide exchange factor. This gene is observed to be lost or underexpressed in prostate cancers. There is a pseudogene of this gene on chromosome 10. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2013]

**Accessions** — [HGNC:1914](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1914) · Entrez [1102](https://www.ncbi.nlm.nih.gov/gene/1102) · UniProt [O95199](https://www.uniprot.org/uniprotkb/O95199) · Ensembl [ENSG00000136161](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136161)

## Data

Gene col 5829: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5829); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5829, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5829]; `tensor/DDL_lfc|DDL_z.npy` [5829]; `embed/gene_vectors.npy` [5829]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5829 or target_col == 5829). Every well: [[RCBTB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RCBTB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

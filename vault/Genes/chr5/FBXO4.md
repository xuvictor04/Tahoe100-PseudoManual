---
symbol: "FBXO4"
type: "gene"
col: 7573
ensembl_id: "ENSG00000151876"
name: "F-box protein 4"
location: "5p13.1"
module: 10
arm: "+"
pooled_cpm: 7.38
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 16
n_dd_up_clean: 8
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# FBXO4

*F-box protein 4* — 5p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.84× (z +10.9, q 8e-25, up in 25 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.407× (z -11.2, q 1e-26, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM26-AS1]] (+0.74, fdr 1e-05), [[NEPRO-AS1]] (+0.70, fdr 5e-05), [[PPP1R3F]] (+0.68, fdr 3e-05); moves opposite to [[GNB2]] (-0.66, fdr 5e-05), [[TRIM62]] (-0.60, fdr 6e-05), [[TRAPPC1]] (-0.60, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DNAH5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7573.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +10.9 | 8e-25 | 25/43 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +10.5 | 2e-23 | 14/20 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +9.9 | 5e-21 | 6/13 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +9.7 | 3e-20 | 17/27 (LoVo, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.9 | 1e-04 | 16/42 (BT-474, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +4.6 | 3e-04 | 17/41 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.40×** | +4.2 | 0.002 | 13/45 (NCI-H460, A-172, …) | all doses, flat |  |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.049 | 6/45 (LOX-IMVI, HEC-1-A, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.056 | 6/42 (HEC-1-A, AsPC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.058 | 7/45 (KATO III, SW480, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.099 | 4/48 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7573.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.407×** | -11.2 | 1e-26 | 35/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.435×** | -10.4 | 7e-23 | 36/46 (SW480, KATO III, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.449×** | -10.0 | 2e-21 | 34/47 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.449×** | -10.0 | 2e-21 | 32/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.459×** | -9.7 | 3e-20 | 26/41 (J82, PANC-1, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.482×** | -9.1 | 6e-18 | 28/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.497×** | -8.7 | 2e-16 | 27/46 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.521×** | -8.1 | 3e-14 | 32/45 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.589×** | -6.2 | 3e-08 | 19/43 (SW1417, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.649×** | -5.4 | 4e-06 | 22/45 (A-427, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.667×** | -5.0 | 2e-05 | 17/48 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.530×** | -4.1 | 0.002 | 11/44 (RKO, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.812×** | -3.7 | 0.011 | 12/46 (HEC-1-A, SW480, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.601×** | -3.3 | 0.036 | 14/41 (HS-578T, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.769×** | -3.3 | 0.042 | 10/47 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 0.836× | -3.1 | 0.060 | 5/48 (Hs 766T, BT-474, …) | top dose only | position effect removed |
| [[Acetazolamide (drug)]] 0.05 µM |  | **0.784×** | -3.0 | 0.086 | 5/46 (RKO, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7573. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.9 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -13.6) |
| [[PANC-1 (line)]] | alt | 7.90 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -10.0) |
| [[A498 (line)]] | wt | 13.7 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0864× (z -9.0) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.292× (z -8.6) |
| [[J82 (line)]] | alt | 17.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.252× (z -8.9) |
| [[KATO III (line)]] | alt | 6.83 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0931× (z -10.6) |
| [[LoVo (line)]] | wt | 9.72 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.0× (z +14.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 5.74 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +20.8) | — |
| [[RKO (line)]] | wt | 8.64 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -8.8) |
| [[A-427 (line)]] | wt | 10.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.144× (z -9.4) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 8.86 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.92× (z +8.8) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 6.45 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0559× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 5.62 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -8.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 9.37 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.109× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 5.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.38× (z +12.1) | — |
| [[NCI-H1792 (line)]] | alt | 5.64 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0834× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 8.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.19× (z +12.8) | — |
| [[RPMI-7951 (line)]] | alt | 7.42 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.102× (z -8.5) |
| [[SNU-423 (line)]] | alt | 5.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +8.6) | — |
| [[A-172 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7573), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM26-AS1]] | +0.74 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | +0.70 | +0.75 / +0.40 | both halves | 5e-05 |  |
| [[PPP1R3F]] | +0.68 | +0.72 / +0.43 | both halves | 3e-05 |  |
| [[RFX3-DT]] | +0.68 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[C19orf54]] | +0.68 | +0.75 / +0.30 | both halves | 2e-04 |  |
| [[LEKR1]] | +0.66 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[ZCWPW1]] | +0.66 | +0.69 / +0.39 | both halves | 6e-05 |  |
| [[MAGOHB]] | +0.66 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[KICS2]] | +0.66 | +0.71 / +0.35 | both halves | 1e-04 |  |
| [[PPP3CB-AS1]] | +0.65 | +0.69 / +0.29 | both halves | 2e-04 |  |
| [[SEPTIN7-DT]] | +0.65 | +0.71 / +0.33 | both halves | 1e-04 |  |
| [[ZNF621]] | +0.65 | +0.67 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNB2]] | -0.66 | -0.66 / -0.39 | both halves | 5e-05 | pathway: Chaperonin-mediated protein folding |
| [[TRIM62]] | -0.60 | -0.60 / -0.39 | both halves | 6e-05 |  |
| [[TRAPPC1]] | -0.60 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[ALDOA]] | -0.60 | -0.60 / -0.36 | both halves | 1e-04 |  |
| [[COX6A1]] | -0.58 | -0.52 / -0.25 | both halves | 4e-04 |  |
| [[CARHSP1]] | -0.57 | -0.56 / -0.29 | both halves | 2e-04 |  |
| [[TSPAN17]] | -0.57 | -0.62 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAH5]] | B | DNAH5 activity strengthens FBXO4's drug response | lines that do not express DNAH5 (10) vs lines expressing it (38) | the lines without DNAH5 respond 0.84× as strongly (z diff +0.29); strongest at Digitoxin 5 µM: 0.99x vs 0.38x (z diff +3.8) | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC02966; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.4, 9.0); signed map (16.2, -25.1). **Vector** length 81.1, 15.0% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.9 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +2.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.6 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.2 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +3.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.3 | -10.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.3 | -10.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.2 | -11.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.1 | -9.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.6 | -10.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -5.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.1 — chr5:41,925,254-41,941,743 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBX4 |
| Gene groups (HGNC) | F-boxes other |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 7 pathways, smallest: Association of TriC/CCT with target proteins during biosynthesis; Chaperonin-mediated protein folding; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKT5](https://www.uniprot.org/uniprotkb/Q9UKT5) (F-box only protein 4):

> Substrate recognition component of a SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex that mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Promotes ubiquitination of cyclin-D1 (CCND1) and its subsequent proteasomal degradation. However, it does not act as a major regulator of CCND1 stability during the G1/S transition (By similarity). Recognizes TERF1 and promotes its ubiquitination together with UBE2D1. Promotes ubiquitination of FXR1 …

**Summary**, from NCBI Gene [26272](https://www.ncbi.nlm.nih.gov/gene/26272):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of the ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:13583](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13583) · Entrez [26272](https://www.ncbi.nlm.nih.gov/gene/26272) · UniProt [Q9UKT5](https://www.uniprot.org/uniprotkb/Q9UKT5) · Ensembl [ENSG00000151876](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151876)

## Data

Gene col 7573: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7573); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7573, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7573]; `tensor/DDL_lfc|DDL_z.npy` [7573]; `embed/gene_vectors.npy` [7573]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7573 or target_col == 7573). Every well: [[FBXO4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

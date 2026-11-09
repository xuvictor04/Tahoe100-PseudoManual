---
symbol: "WNK4"
type: "gene"
col: 4745
ensembl_id: "ENSG00000126562"
name: "WNK lysine deficient protein kinase 4"
location: "17q21.2"
module: 38
arm: "+"
pooled_cpm: 9.28
n_lines_expressing: 45
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# WNK4

*WNK lysine deficient protein kinase 4* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.01× (z +17.3, q 0e+00, up in 27 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.618× (z -4.9, q 5e-04, down in 14 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C2orf92]] (+0.73, fdr 7e-06), [[ASGR1]] (+0.66, fdr 1e-05), [[NLGN3]] (+0.66, fdr 7e-06); moves opposite to [[PRDX3]] (-0.59, fdr 1e-05), [[GSTA4]] (-0.57, fdr 2e-05), [[KDM1A]] (-0.56, fdr 2e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC26A4]] → it (grade B ⚠); 3 go from it, the strongest it → [[CYB5R4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4745.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.01×** | +17.3 | 0e+00 | 27/36 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +12.4 | 4e-33 | 28/37 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.81×** | +11.4 | 5e-28 | 27/36 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +5.5 | 4e-06 | 19/40 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.64×** | +5.5 | 4e-06 | 16/38 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.1 | 3e-05 | 14/30 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.6 | 4e-04 | 14/41 (A549, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +4.5 | 6e-04 | 14/35 (A-427, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.51×** | +4.4 | 7e-04 | 4/14 (HEC-1-A, C32, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +4.2 | 0.002 | 14/42 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.39×** | +3.7 | 0.013 | 9/26 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.014 | 8/42 (A498, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.020 | 14/41 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.044 | 6/37 (COLO 205, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4745.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.618×** | -4.9 | 5e-04 | 14/41 (SK-MEL-2, HepG2/C3A, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.662×** | -4.6 | 0.001 | 19/41 (J82, RPMI-7951, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.670×** | -4.3 | 0.004 | 12/38 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.726×** | -3.5 | 0.056 | 10/42 (A498, SNU-423, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.765×** | -3.3 | 0.099 | 15/42 (HepG2/C3A, C32, …) | all doses, flat | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4745. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 37.9 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.250× (z -8.9) |
| [[C32 (line)]] | wt | 13.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.68× (z +12.1) | — |
| [[NCI-H460 (line)]] | wt | 3.62 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +12.3) | — |
| [[A-172 (line)]] | wt | 12.4 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0964× (z -11.7) |
| [[J82 (line)]] | alt | 3.50 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0527× (z -10.1) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 9.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 5.08 | 0 | 1 | — | [[Ranolazine (drug)]] 0.05 µM 0.0640× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +11.0) | — |
| [[A-427 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4745), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2orf92]] | +0.73 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[ASGR1]] | +0.66 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[NLGN3]] | +0.66 | +0.65 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[LCAT]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[CEACAM19]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[MIRLET7IHG]] | +0.63 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[RPSAP52]] | +0.63 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[PPIEL-1]] | +0.63 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[CFAP251]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ORAI2]] | +0.63 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[C3orf20]] | +0.62 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[MMP25]] | +0.62 | +0.68 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDX3]] | -0.59 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[GSTA4]] | -0.57 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[KDM1A]] | -0.56 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[TMEM9]] | -0.56 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[PPT1]] | -0.56 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[BCL9]] | -0.55 | -0.60 / -0.46 | both halves | 2e-05 |  |
| [[C20orf96]] | -0.55 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[CYB5R4]] | -0.54 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[FAM210B]] | -0.54 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[LANCL1]] | -0.54 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[NXPE3]] | -0.53 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[SCCPDH]] | -0.53 | -0.59 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC26A4]] | B | SLC26A4 activity raises WNK4's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 2.46× lower at baseline in the lines without SLC26A4 | 0.017 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[MIR4280HG]] | B | MIR4280HG activity raises WNK4's level | lines that do not express MIR4280HG (21) vs lines expressing it (29) | 2.02× lower at baseline in the lines without MIR4280HG | 0.096 | ⚠ within organs, on part of the lines; also absent: EVA1A, MILR1, LNX1; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYB5R4]] | B | WNK4 activity lowers CYB5R4's level | lines that do not express WNK4 (5) vs lines expressing it (45) | 1.38× higher at baseline in the lines without WNK4 | 0.060 | ⚠ within organs, on part of the lines; also absent: TEX14, TMEM144, NEO1; maybe low, not absent |
| [[NLGN3]] | B | WNK4 activity raises NLGN3's level | lines that do not express WNK4 (5) vs lines expressing it (45) | 1.87× lower at baseline in the lines without WNK4 | 0.065 | ⚠ within organs, on part of the lines; also absent: TEX14, TMEM144, NEO1; maybe low, not absent |
| [[PILRA]] | B | WNK4 activity raises PILRA's level | lines that do not express WNK4 (5) vs lines expressing it (45) | 2.20× lower at baseline in the lines without WNK4 | 0.098 | ⚠ within organs, on part of the lines; also absent: TEX14, TMEM144, NEO1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.0, -6.8); signed map (17.9, 5.4). **Vector** length 84.0, 17.1% of its response variance represented; |z| ≥ 3 in 916 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +17.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +12.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.4 | +5.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.7 | +1.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.2 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -2.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | WNK lysine deficient protein kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,780,610-42,797,066 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PRKWNK4 |
| Gene groups (HGNC) | WNK lysine deficient protein kinases |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96J92](https://www.uniprot.org/uniprotkb/Q96J92) (Serine/threonine-protein kinase WNK4):

> Serine/threonine-protein kinase component of the WNK4-SPAK/OSR1 kinase cascade, which acts as a key regulator of ion transport in the distal nephron and blood pressure (By similarity). The WNK4-SPAK/OSR1 kinase cascade is composed of WNK4, which mediates phosphorylation and activation of downstream kinases OXSR1/OSR1 and STK39/SPAK. Following activation, OXSR1/OSR1 and STK39/SPAK catalyze phosphorylation of ion cotransporters, such as SLC12A1/NKCC2, SLC12A2/NKCC1, SLC12A3/NCC, SLC12A5/KCC2 or …

**Summary**, from NCBI Gene [65266](https://www.ncbi.nlm.nih.gov/gene/65266):

> This gene encodes a member of the WNK family of serine-threonine protein kinases. The kinase is part of the tight junction complex in kidney cells, and regulates the balance between NaCl reabsorption and K(+) secretion. The kinase regulates the activities of several types of ion channels, cotransporters, and exchangers involved in electrolyte flux in epithelial cells. Mutations in this gene result in pseudohypoaldosteronism type IIB.[provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:14544](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14544) · Entrez [65266](https://www.ncbi.nlm.nih.gov/gene/65266) · UniProt [Q96J92](https://www.uniprot.org/uniprotkb/Q96J92) · Ensembl [ENSG00000126562](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126562)

## Data

Gene col 4745: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4745); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4745, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4745]; `tensor/DDL_lfc|DDL_z.npy` [4745]; `embed/gene_vectors.npy` [4745]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4745 or target_col == 4745). Every well: [[WNK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WNK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

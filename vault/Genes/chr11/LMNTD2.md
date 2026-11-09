---
symbol: "LMNTD2"
type: "gene"
col: 11693
ensembl_id: "ENSG00000185522"
name: "lamin tail domain containing 2"
location: "11p15.5"
module: 157
arm: "+"
pooled_cpm: 2.35
n_lines_expressing: 47
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# LMNTD2

*lamin tail domain containing 2* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.26× (z +9.4, q 2e-18, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.41× (z +4.0, q 0.008, up in 6 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.450× (z -9.4, q 4e-18, down in 27 of 27 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.394× (z -7.7, q 4e-12, down in 23 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM198B]] (+0.65, fdr 1e-05), [[PPM1M]] (+0.59, fdr 2e-05), [[EME2]] (+0.59, fdr 1e-05); moves opposite to [[MTMR9]] (-0.49, fdr 3e-05), [[ZMYM1]] (-0.49, fdr 5e-05), [[MAP7D3]] (-0.45, fdr 5e-05).
> It is in [[Module 157]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → cells under [[IQ 1 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11693.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.26×** | +9.4 | 2e-18 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.59×** | +7.9 | 8e-13 | 4/10 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +5.9 | 9e-07 | 1/5 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.008 | 6/25 (AsPC-1, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +3.6 | 0.034 | 6/21 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.18×** | +3.4 | 0.068 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.52×** | +3.2 | 0.100 | 3/16 (LS 180, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.46× | +3.2 | 0.11 | 0/11 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 11 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11693.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.450×** | -9.4 | 4e-18 | 27/27 (LoVo, A549, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.381×** | -7.7 | 4e-12 | 21/34 (LoVo, HT-29, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.394×** | -7.7 | 4e-12 | 23/26 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.477×** | -6.1 | 1e-07 | 20/35 (MIA PaCa-2, HCT15, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.493×** | -5.9 | 5e-07 | 18/38 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.526×** | -5.3 | 9e-06 | 19/42 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.539×** | -5.1 | 2e-05 | 19/31 (KATO III, Hs 766T, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.583×** | -4.5 | 5e-04 | 13/41 (NCI-H1573, SK-MEL-2, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.593×** | -4.3 | 9e-04 | 16/40 (LOX-IMVI, NCI-H23, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.615×** | -4.0 | 0.003 | 12/23 (NCI-H2030, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.645×** | -3.6 | 0.014 | 15/34 (LoVo, A-172, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.643×** | -3.5 | 0.018 | 7/32 (C32, J82, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.656×** | -3.5 | 0.020 | 8/39 (A-172, A-427, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.660×** | -3.4 | 0.023 | 11/39 (A549, SK-MEL-2, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.675×** | -3.3 | 0.041 | 12/40 (A-427, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.670×** | -3.2 | 0.049 | 5/40 (RKO, HT-29, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11693. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 8.98 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -14.6) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -8.9) |
| [[A549 (line)]] | wt | 2.80 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0731× (z -10.5) ⚠ cell-cycle shift, explains ~49% of this change |
| [[AsPC-1 (line)]] | alt | 2.57 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0950× (z -8.9) ⚠ cell-cycle shift, explains ~49% of this change |
| [[HT-29 (line)]] | alt | 2.41 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0829× (z -9.9) ⚠ cell-cycle shift, explains ~49% of this change |
| [[PANC-1 (line)]] | alt | 3.40 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -9.9) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SW480 (line)]] | alt | 2.48 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -8.9) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A-172 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.752 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.928 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.679 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11693), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM198B]] | +0.65 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[PPM1M]] | +0.59 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[EME2]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[CDK5RAP3]] | +0.59 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[IL11RA]] | +0.59 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[SLC9A3-AS1]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[CFAP410]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[INPPL1]] | +0.57 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[AKT2]] | +0.57 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[PBXIP1]] | +0.55 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[GSTM2]] | +0.55 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[LENG8]] | +0.55 | +0.50 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTMR9]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[ZMYM1]] | -0.49 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[MAP7D3]] | -0.45 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[METTL2A]] | -0.45 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[MPHOSPH6]] | -0.45 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[AGGF1]] | -0.44 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[TIPRL]] | -0.44 | -0.37 / -0.42 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[IQ 1 (drug)]] 5 µM | C | LMNTD2 activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express LMNTD2 (3) vs lines expressing it (45) | the lines without LMNTD2: 0.72× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGAP27, MMP25, RBMS2; maybe low, not absent |
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.05 µM | C | LMNTD2 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express LMNTD2 (3) vs lines expressing it (45) | the lines without LMNTD2: 0.74× the cells of the other lines | 0.080 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGAP27, MMP25, RBMS2; maybe low, not absent |
| [[DTX2P1]] | C | LMNTD2 activity raises DTX2P1's level | lines that do not express LMNTD2 (3) vs lines expressing it (47) | 1.97× lower at baseline in the lines without LMNTD2 | 0.095 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGAP27, MMP25, RBMS2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.749). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.2, -24.2); signed map (-0.3, 5.4). **Vector** length 44.0, 5.51% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +1.6 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +0.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.1 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.1 | +2.7 |
|  | [[Saquinavir (drug)]] 0.5 µM |  | +1.1 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.9 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -2.1 | -9.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.9 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.2 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.4 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -2.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.1 | -1.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | lamin tail domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:554,850-560,738 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC35138; previously C11orf35 |
| Matched by | ensembl_id |

UniProt [Q8IXW0](https://www.uniprot.org/uniprotkb/Q8IXW0) carries no function annotation.

**Summary**, from NCBI Gene [256329](https://www.ncbi.nlm.nih.gov/gene/256329):

> Predicted to be a structural constituent of chromatin. Predicted to act upstream of or within positive regulation of mRNA splicing, via spliceosome. Predicted to be active in lamin filament. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28561](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28561) · Entrez [256329](https://www.ncbi.nlm.nih.gov/gene/256329) · UniProt [Q8IXW0](https://www.uniprot.org/uniprotkb/Q8IXW0) · Ensembl [ENSG00000185522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185522)

## Data

Gene col 11693: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11693); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11693, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11693]; `tensor/DDL_lfc|DDL_z.npy` [11693]; `embed/gene_vectors.npy` [11693]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11693 or target_col == 11693). Every well: [[LMNTD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMNTD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

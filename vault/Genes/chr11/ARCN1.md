---
symbol: "ARCN1"
type: "gene"
col: 1736
ensembl_id: "ENSG00000095139"
name: "archain 1 coat protein complex I subunit delta"
location: "11q23.3"
module: 42
arm: "+"
pooled_cpm: 128.81
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# ARCN1

*archain 1 coat protein complex I subunit delta* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.50× (z +11.8, q 4e-29, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.552× (z -12.1, q 3e-31, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3H11A]] (+0.73, fdr 7e-06), [[USO1]] (+0.72, fdr 7e-06), [[LYSMD3]] (+0.69, fdr 7e-06); moves opposite to [[MFSD14CP]] (-0.66, fdr 1e-05), [[RNF38]] (-0.65, fdr 1e-05), [[SEC11A]] (-0.65, fdr 7e-06).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 2 go from it, the strongest it → [[PPP1R15B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1736.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +11.8 | 4e-29 | 41/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +11.7 | 4e-29 | 43/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +9.3 | 4e-18 | 41/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +8.7 | 4e-16 | 39/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +5.5 | 4e-06 | 33/48 (LOX-IMVI, SK-MEL-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +5.0 | 6e-05 | 31/48 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +4.9 | 8e-05 | 32/48 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.5 | 5e-04 | 0/50 | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.16× | +3.0 | 0.16 | 6/49 (C32, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1736.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.552×** | -12.1 | 3e-31 | 44/48 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.567×** | -11.6 | 1e-28 | 44/48 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.590×** | -10.8 | 6e-25 | 44/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.768×** | -7.7 | 3e-12 | 35/49 (HT-29, A498, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.702×** | -7.0 | 4e-10 | 36/47 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.754×** | -5.8 | 7e-07 | 31/48 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.760×** | -5.6 | 2e-06 | 30/48 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.763×** | -5.3 | 7e-06 | 31/48 (RKO, HT-29, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Rapamycin (drug)]] 5 µM |  | 0.864× | -4.2 | 0.001 | 12/48 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.818×** | -4.1 | 0.002 | 25/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.847× | -3.4 | 0.035 | 20/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.849× | -3.4 | 0.035 | 19/48 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.798×** | -3.3 | 0.042 | 18/48 (SW 1271, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.861× | -3.1 | 0.086 | 15/48 (C32, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.862× | -3.1 | 0.086 | 16/48 (C32, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1736. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 157 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +15.8) | [[Panobinostat (drug)]] 5 µM 0.346× (z -13.9) |
| [[NCI-H1573 (line)]] | alt | 231 | 4 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.21× (z +18.1) | [[Panobinostat (drug)]] 5 µM 0.369× (z -12.5) |
| [[HT-29 (line)]] | alt | 188 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -14.5) |
| [[RKO (line)]] | wt | 140 | 4 | 2 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.75× (z +11.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -8.8) |
| [[SW480 (line)]] | alt | 166 | 4 | 2 | [[Harringtonine (drug)]] 0.5 µM 2.05× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.453× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 84.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +19.7) | — |
| [[NCI-H1792 (line)]] | alt | 117 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.396× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 107 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 102 | 2 | 2 | [[Harringtonine (drug)]] 5 µM 2.49× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.485× (z -9.6) |
| [[PANC-1 (line)]] | alt | 146 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +25.1) | — |
| [[CFPAC-1 (line)]] | alt | 133 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.547× (z -8.7) |
| [[KATO III (line)]] | alt | 318 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.377× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 75.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 139 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.435× (z -10.9) |
| [[SW48 (line)]] | wt | 131 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.84× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.385× (z -8.8) |
| [[A-172 (line)]] | wt | 89.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.15× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.459× (z -10.0) |
| [[A498 (line)]] | wt | 113 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -9.6) |
| [[COLO 205 (line)]] | alt | 130 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +13.2) | — |
| [[Hs 766T (line)]] | wt | 200 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.440× (z -10.0) |
| [[HS-578T (line)]] | alt | 136 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.453× (z -9.5) |
| [[LS 180 (line)]] | wt | 106 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.15× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 105 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.61× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 130 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.396× (z -10.4) |
| [[A549 (line)]] | wt | 85.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.1) | — |
| [[AN3 CA (line)]] | alt | 109 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 135 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 140 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.469× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 158 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.495× (z -8.5) |
| [[A-427 (line)]] | wt | 55.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 160 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 101 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 148 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 179 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1736), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H11A]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[USO1]] | +0.72 | +0.65 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 721 |
| [[LYSMD3]] | +0.69 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[THAP5]] | +0.67 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[YIPF6]] | +0.66 | +0.63 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[ANAPC13]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[TRIP11]] | +0.66 | +0.68 / +0.56 | both halves | 1e-05 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[ZNF460]] | +0.65 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[SF3B1]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 | STRING 509 |
| [[CNOT3]] | +0.65 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[SRP68]] | +0.63 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[LIG4]] | +0.63 | +0.53 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD14CP]] | -0.66 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[RNF38]] | -0.65 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[SEC11A]] | -0.65 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[SMG1P5]] | -0.64 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[SRPK2]] | -0.63 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[UBE2G1]] | -0.62 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[EIF3CL]] | -0.62 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[SSBP4]] | -0.61 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[NENF]] | -0.61 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[SNX1]] | -0.60 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[ATOX1]] | -0.58 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[NDUFAF7]] | -0.58 | -0.53 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ARCN1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R15B]] | C | ARCN1's natural level weakens PPP1R15B's drug response | ARCN1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.16; direction not clear | 0.070 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Belzutifan (drug)]] 5 µM | C | ARCN1's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | ARCN1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64 | 0.390 over the table, 0.041 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.138). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.6, -16.8); signed map (13.5, -27.7). **Vector** length 143, 47.5% of its response variance represented; |z| ≥ 3 in 1,004 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.7 | +9.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +11.4 | +11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +11.0 | +11.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +10.2 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.0 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.6 | +2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.8 | +2.2 |
|  | [[EX229 (drug)]] 0.05 µM |  | +2.5 | +2.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -6.0 | -5.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.7 | -11.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.6 | -3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.2 | -3.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.8 | -12.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.7 | -2.8 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -3.1 | -2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | archain 1 coat protein complex I subunit delta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:118,572,390-118,603,033 (+) |
| Ensembl biotype | protein_coding |
| Also known as | delta-COP; previously COPD |
| Gene groups (HGNC) | Coat protein complex I |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 9 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; COPI-mediated anterograde transport; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P48444](https://www.uniprot.org/uniprotkb/P48444) (Coatomer subunit delta):

> Component of the coatomer, a cytosolic protein complex that binds to dilysine motifs and reversibly associates with Golgi non-clathrin-coated vesicles, which further mediate biosynthetic protein transport from the ER, via the Golgi up to the trans Golgi network. The coatomer complex is required for budding from Golgi membranes, and is essential for the retrograde Golgi-to-ER transport of dilysine-tagged proteins. In mammals, the coatomer can only be recruited by membranes associated to …

**Summary**, from NCBI Gene [372](https://www.ncbi.nlm.nih.gov/gene/372):

> This gene maps in a region, which include the mixed lineage leukemia and Friend leukemia virus integration 1 genes, where multiple disease-associated chromosome translocations occur. It is an intracellular protein. Archain sequences are well conserved among eukaryotes and this protein may play a fundamental role in eukaryotic cell biology. It has similarities to heat shock proteins and clathrin-associated proteins, and may be involved in vesicle structure or trafficking. [provided by RefSeq, …

**Accessions** — [HGNC:649](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:649) · Entrez [372](https://www.ncbi.nlm.nih.gov/gene/372) · UniProt [P48444](https://www.uniprot.org/uniprotkb/P48444) · Ensembl [ENSG00000095139](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095139)

## Data

Gene col 1736: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1736); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1736, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1736]; `tensor/DDL_lfc|DDL_z.npy` [1736]; `embed/gene_vectors.npy` [1736]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1736 or target_col == 1736). Every well: [[ARCN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARCN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

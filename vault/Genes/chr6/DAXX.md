---
symbol: "DAXX"
type: "gene"
col: 12829
ensembl_id: "ENSG00000204209"
name: "death domain associated protein"
location: "6p21.32"
module: 11
arm: "+"
pooled_cpm: 39.36
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# DAXX

*death domain associated protein* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.05 µM: 1.75× (z +6.6, q 2e-08, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.608× (z -6.4, q 1e-07, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RDH14]] (+0.72, fdr 4e-05), [[PHAX]] (+0.71, fdr 7e-06), [[MRPL46]] (+0.70, fdr 3e-05); moves opposite to [[TXNDC5]] (-0.63, fdr 3e-05), [[SUMF2]] (-0.62, fdr 1e-05), [[FKBP1A]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12829.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.05 µM |  | **1.75×** | +6.6 | 2e-08 | 42/47 (PANC-1, LoVo, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +6.3 | 6e-08 | 41/48 (HS-578T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.63×** | +6.3 | 6e-08 | 38/48 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.66×** | +6.2 | 8e-08 | 31/48 (SNU-423, HS-578T, …) | all doses, flat | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.55×** | +5.6 | 3e-06 | 32/46 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.57×** | +5.4 | 8e-06 | 40/48 (A-172, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +5.1 | 3e-05 | 29/47 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.35×** | +3.9 | 0.008 | 24/48 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.024 | 23/48 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.044 | 17/47 (A-172, NCI-H460, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.049 | 23/48 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.28×** | +3.2 | 0.062 | 23/47 (SW1417, CHP-212, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | 1.28× | +3.0 | 0.10 | 20/47 (PANC-1, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12829.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.608×** | -6.4 | 1e-07 | 34/48 (NCI-H23, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.638×** | -5.7 | 3e-06 | 33/48 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.675×** | -5.0 | 1e-04 | 29/48 (KATO III, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.805×** | -3.9 | 0.012 | 18/48 (SW480, LS 180, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.770× | -3.2 | 0.14 | 19/39 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.838× | -3.2 | 0.14 | 11/48 (A498, SHP-77, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12829. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 60.7 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +12.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.94× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 40.1 | 4 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.18× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 88.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -10.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 41.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 53.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.338× (z -9.1) |
| [[SNU-423 (line)]] | alt | 59.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +12.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 42.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -11.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 31.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.325× (z -8.6) |
| [[BT-474 (line)]] | alt | 30.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -9.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 45.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -8.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[KATO III (line)]] | alt | 42.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.363× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 62.4 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.60× (z +8.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[RKO (line)]] | wt | 44.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 30.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.76× (z +8.7) ⚠ toxic | — |
| [[A549 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12829), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RDH14]] | +0.72 | +0.42 / +0.76 | both halves | 4e-05 |  |
| [[PHAX]] | +0.71 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[MRPL46]] | +0.70 | +0.45 / +0.73 | both halves | 3e-05 |  |
| [[CCDC137]] | +0.69 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[NSMCE3]] | +0.69 | +0.50 / +0.64 | both halves | 1e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[SNW1]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions |
| [[CCDC174]] | +0.69 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[FDX2]] | +0.67 | +0.40 / +0.72 | both halves | 5e-05 |  |
| [[C1orf131]] | +0.67 | +0.48 / +0.73 | both halves | 2e-05 |  |
| [[FAM32A]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[TBCC]] | +0.65 | +0.43 / +0.70 | both halves | 3e-05 |  |
| [[ZNF593]] | +0.64 | +0.43 / +0.71 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC5]] | -0.63 | -0.44 / -0.68 | both halves | 3e-05 |  |
| [[SUMF2]] | -0.62 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[FKBP1A]] | -0.60 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[CPSF6]] | -0.58 | -0.41 / -0.61 | both halves | 4e-05 | pathway: Dengue Virus-Host Interactions |
| [[TMEM30A]] | -0.58 | -0.39 / -0.61 | both halves | 5e-05 |  |
| [[RCN2]] | -0.57 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[SELENON]] | -0.57 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[PIGK]] | -0.56 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[PDIA6]] | -0.56 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[RPN2]] | -0.56 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[CRTAP]] | -0.56 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[MAPK1]] | -0.56 | -0.56 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DAXX's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises DAXX's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.699). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.6, 3.6); signed map (0.4, -18.4). **Vector** length 94.2, 24.4% of its response variance represented; |z| ≥ 3 in 759 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +5.8 | +6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.8 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.7 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.6 | +3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.7 | +6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +1.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.4 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -7.3 | -1.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -7.1 | -1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -2.6 | +0.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | death domain associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:33,318,558-33,323,016 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DAP6 |
| Reactome | 18 pathways, smallest: Dengue virus modulates apoptosis; Inhibition of DNA recombination at telomere; Regulation of TP53 Degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UER7](https://www.uniprot.org/uniprotkb/Q9UER7) (Death domain-associated protein 6):

> Transcription corepressor known to repress transcriptional potential of several sumoylated transcription factors. Down-regulates basal and activated transcription. Its transcription repressor activity is modulated by recruiting it to subnuclear compartments like the nucleolus or PML/POD/ND10 nuclear bodies through interactions with MCSR1 and PML, respectively. Seems to regulate transcription in PML/POD/ND10 nuclear bodies together with PML and may influence TNFRSF6-dependent apoptosis thereby. …

**Summary**, from NCBI Gene [1616](https://www.ncbi.nlm.nih.gov/gene/1616):

> This gene encodes a multifunctional protein that resides in multiple locations in the nucleus and in the cytoplasm. It interacts with a wide variety of proteins, such as apoptosis antigen Fas, centromere protein C, and transcription factor erythroblastosis virus E26 oncogene homolog 1. In the nucleus, the encoded protein functions as a potent transcription repressor that binds to sumoylated transcription factors. Its repression can be relieved by the sequestration of this protein into …

**Accessions** — [HGNC:2681](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2681) · Entrez [1616](https://www.ncbi.nlm.nih.gov/gene/1616) · UniProt [Q9UER7](https://www.uniprot.org/uniprotkb/Q9UER7) · Ensembl [ENSG00000204209](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204209)

## Data

Gene col 12829: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12829); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12829, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12829]; `tensor/DDL_lfc|DDL_z.npy` [12829]; `embed/gene_vectors.npy` [12829]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12829 or target_col == 12829). Every well: [[DAXX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DAXX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

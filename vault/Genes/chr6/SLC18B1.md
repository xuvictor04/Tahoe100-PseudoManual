---
symbol: "SLC18B1"
type: "gene"
col: 7089
ensembl_id: "ENSG00000146409"
name: "solute carrier family 18 member B1"
location: "6q23.2"
module: 190
arm: "+"
pooled_cpm: 12.39
n_lines_expressing: 45
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/190"]
generated_by: "tahoemap"
---

# SLC18B1

*solute carrier family 18 member B1* — 6q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.72× (z +7.5, q 4e-11, up in 20 of 35 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.44× (z +7.3, q 7e-11, up in 25 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.550× (z -12.1, q 6e-31, down in 30 of 41 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.510× (z -9.6, q 2e-19, down in 29 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPD52L1]] (+0.67, fdr 7e-06), [[NAPB]] (+0.61, fdr 1e-05), [[MRPS30-DT]] (+0.61, fdr 2e-05); moves opposite to [[CYTH2]] (-0.58, fdr 1e-05), [[KPNA4]] (-0.56, fdr 1e-05), [[ARHGAP39]] (-0.55, fdr 3e-05).
> It is in [[Module 190]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TPD52L1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PGAP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7089.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +7.5 | 4e-11 | 20/35 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +7.3 | 7e-11 | 25/43 (LOX-IMVI, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.39×** | +6.6 | 6e-09 | 22/42 (NCI-H1792, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +6.3 | 4e-08 | 20/41 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.31×** | +5.5 | 5e-06 | 15/42 (SHP-77, SW480, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +5.0 | 5e-05 | 14/42 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.39×** | +4.7 | 2e-04 | 15/41 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.32×** | +3.9 | 0.006 | 11/42 (LoVo, A-427, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.009 | 12/42 (C32, Panc 03.27, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.009 | 12/42 (SW480, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +3.6 | 0.018 | 13/42 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.018 | 9/43 (MIA PaCa-2, LS 180, …) | two highest doses | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.044 | 6/42 (KATO III, NCI-H1792, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.044 | 9/41 (J82, Panc 03.27, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.045 | 11/41 (C32, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7089.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.550×** | -12.1 | 6e-31 | 30/41 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.510×** | -9.6 | 2e-19 | 29/42 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.521×** | -9.3 | 2e-18 | 26/42 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.558×** | -8.0 | 1e-13 | 23/41 (NCI-H1573, NCI-H1792, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.589×** | -7.6 | 4e-12 | 28/42 (BT-474, SHP-77, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.735×** | -4.4 | 0.001 | 16/42 (BT-474, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.743×** | -4.2 | 0.002 | 17/40 (NCI-H1573, RKO, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.751×** | -4.1 | 0.003 | 14/42 (BT-474, CHP-212, …) | top dose only |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.776×** | -3.3 | 0.061 | 6/42 (A498, A-172, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.648×** | -3.2 | 0.066 | 12/41 (A498, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7089. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -15.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Palmatine (chloride) (drug)]] 0.5 µM 0.240× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0552× (z -16.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SHP-77 (line)]] | alt | 31.6 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.200× (z -11.2) |
| [[SW480 (line)]] | alt | 21.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -10.7) |
| [[BT-474 (line)]] | alt | 9.62 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0256× (z -14.7) |
| [[MIA PaCa-2 (line)]] | alt | 16.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0747× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 10.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -12.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HEC-1-A (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.238× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -10.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1792 (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.107× (z -11.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 7.72 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -10.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[RKO (line)]] | wt | 33.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -12.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -10.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SNU-423 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -9.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -10.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7089), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPD52L1]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[NAPB]] | +0.61 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[MRPS30-DT]] | +0.61 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[NDUFAF7]] | +0.59 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[CIAO2A]] | +0.58 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[PIGB]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[JKAMP]] | +0.57 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[STEAP2]] | +0.57 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[DRAM2]] | +0.57 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[EPHX2]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[UBA5]] | +0.56 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYTH2]] | -0.58 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[KPNA4]] | -0.56 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[ARHGAP39]] | -0.55 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[MYO1C]] | -0.54 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[CCDC57]] | -0.53 | -0.58 / -0.36 | both halves | 1e-04 |  |
| [[SETX]] | -0.52 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[LINC00205]] | -0.52 | -0.58 / -0.40 | both halves | 4e-05 |  |
| [[PPP1R10]] | -0.52 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[PDPK1]] | -0.52 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[SVIL]] | -0.52 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[RASAL2]] | -0.51 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[FER]] | -0.50 | -0.42 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPD52L1]] | B | TPD52L1 activity raises SLC18B1's level | lines that do not express TPD52L1 (12) vs lines expressing it (38) | 2.45× lower at baseline in the lines without TPD52L1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TNFRSF21, EML5 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGAP1]] | B | SLC18B1 activity lowers PGAP1's level | lines that do not express SLC18B1 (5) vs lines expressing it (45) | 1.79× higher at baseline in the lines without SLC18B1 | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: FHIP1A, NIPAL1, RALGPS2; its own permutation p |

## Where it sits

- **Module**: [[Module 190]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.8, 12.5); signed map (-30.1, -17.8). **Vector** length 87.8, 19.2% of its response variance represented; |z| ≥ 3 in 832 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +5.5 | +6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.4 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +6.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +3.9 | +4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +3.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.4 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.4 | -12.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.5 | -4.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.4 | -2.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 18 member B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.2 — chr6:132,769,370-132,813,339 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ55C23.6; previously C6orf192 |
| Gene groups (HGNC) | Solute carrier family 18 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NT16](https://www.uniprot.org/uniprotkb/Q6NT16) (MFS-type transporter SLC18B1):

> Proton-coupled polyamine antiporter involved in the translocation of polyamines from cytosol into secretory vesicles prior to their release via exocytosis. Uses the electrochemical proton gradient generated by a V-type proton-pumping ATPase to couple the efflux of protons with the uptake of a polyamine molecule. Facilitates vesicular storage of spermine and spermidine in astrocytes with an impact on glutamatergic neuronal transmission and memory formation (By similarity). Upon antigen …

**Summary**, from NCBI Gene [116843](https://www.ncbi.nlm.nih.gov/gene/116843):

> This gene encodes a protein, which has high sequence similarity to rat, xenopus and zebrafish proteins. The protein function is unknown. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:21573](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21573) · Entrez [116843](https://www.ncbi.nlm.nih.gov/gene/116843) · UniProt [Q6NT16](https://www.uniprot.org/uniprotkb/Q6NT16) · Ensembl [ENSG00000146409](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146409)

## Data

Gene col 7089: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7089); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7089, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7089]; `tensor/DDL_lfc|DDL_z.npy` [7089]; `embed/gene_vectors.npy` [7089]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7089 or target_col == 7089). Every well: [[SLC18B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC18B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "PGAP2"
type: "gene"
col: 7333
ensembl_id: "ENSG00000148985"
name: "post-GPI attachment to proteins 2"
location: "11p15.4"
module: 175
arm: "+"
pooled_cpm: 19.01
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 36
n_dd_up_clean: 4
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# PGAP2

*post-GPI attachment to proteins 2* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 0.5 µM: 1.34× (z +4.9, q 5e-04, up in 19 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.337× (z -25.8, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRMT7]] (+0.63, fdr 7e-06), [[GLMN]] (+0.59, fdr 1e-05), [[ZNF449]] (+0.59, fdr 1e-05); moves opposite to [[BACH1]] (-0.56, fdr 3e-05), [[LMO7DN]] (-0.55, fdr 1e-05), [[TBILA]] (-0.54, fdr 1e-05).
> It is in [[Module 175]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DSC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7333.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +4.9 | 5e-04 | 19/47 (A498, LS 180, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.8 | 5e-04 | 9/25 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Afatinib (drug)]] 5 µM |  | **1.31×** | +4.7 | 5e-04 | 14/47 (NCI-H23, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.38×** | +3.9 | 0.017 | 11/42 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.092 | 10/44 (Panc 03.27, A498, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.15 | 8/46 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7333.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.337×** | -25.8 | 0e+00 | 42/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.355×** | -17.4 | 0e+00 | 36/46 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.465×** | -12.9 | 1e-35 | 37/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.515×** | -10.7 | 1e-24 | 38/47 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.533×** | -10.6 | 5e-24 | 33/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.558×** | -9.8 | 1e-20 | 37/46 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.595×** | -8.4 | 4e-15 | 22/40 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.607×** | -8.4 | 4e-15 | 28/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.626×** | -7.9 | 3e-13 | 30/47 (RPMI-7951, A-172, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.429×** | -7.4 | 6e-12 | 25/48 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.643×** | -7.4 | 7e-12 | 28/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.670×** | -6.7 | 9e-10 | 21/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.687×** | -6.3 | 1e-08 | 23/48 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.799×** | -5.3 | 4e-06 | 17/48 (SW480, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.729×** | -5.3 | 4e-06 | 22/46 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.734×** | -5.2 | 7e-06 | 19/47 (PANC-1, HT-29, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.564×** | -5.0 | 2e-05 | 15/43 (HOP62, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.741×** | -5.0 | 2e-05 | 20/44 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7333. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 77.8 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -24.6) |
| [[SW480 (line)]] | alt | 29.6 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -17.6) |
| [[HOP62 (line)]] | alt | 15.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -18.6) |
| [[A498 (line)]] | wt | 21.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -23.0) |
| [[A549 (line)]] | wt | 15.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -18.1) |
| [[LOX-IMVI (line)]] | wt | 9.61 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0402× (z -16.5) |
| [[RPMI-7951 (line)]] | alt | 12.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -11.5) |
| [[A-427 (line)]] | wt | 22.1 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0516× (z -20.6) ⚠ cell-cycle shift, explains ~23% of this change |
| [[COLO 205 (line)]] | alt | 15.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 20.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -11.5) |
| [[J82 (line)]] | alt | 16.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -11.2) |
| [[LoVo (line)]] | wt | 12.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -18.2) |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -18.0) |
| [[NCI-H1573 (line)]] | alt | 13.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 13.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.403× (z -9.7) |
| [[A-172 (line)]] | wt | 16.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -10.9) ⚠ cell-cycle shift, explains ~23% of this change |
| [[H4 (line)]] | wt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0789× (z -10.0) |
| [[Hs 766T (line)]] | wt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -10.8) |
| [[HS-578T (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.146× (z -10.2) ⚠ toxic |
| [[HT-29 (line)]] | alt | 18.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -13.3) |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0904× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 12.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0909× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 25.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -14.1) |
| [[NCI-H2347 (line)]] | alt | 8.79 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -9.8) |
| [[RKO (line)]] | wt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -8.5) |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.182× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 9.66 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -9.6) |
| [[SNU-423 (line)]] | alt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -8.5) |
| [[SW1417 (line)]] | alt | 23.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -13.5) |
| [[AN3 CA (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7333), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRMT7]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[GLMN]] | +0.59 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[ZNF449]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[TMEM143]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[ZNF333]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[NT5M]] | +0.56 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[PIGU]] | +0.55 | +0.58 / +0.55 | both halves | 1e-05 | STRING 535 |
| [[TAFAZZIN]] | +0.54 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[PEMT]] | +0.52 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[CRYZL1]] | +0.52 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[ALG6]] | +0.52 | +0.63 / +0.33 | both halves | 1e-04 |  |
| [[NPRL3]] | +0.52 | +0.54 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BACH1]] | -0.56 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[LMO7DN]] | -0.55 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[TBILA]] | -0.54 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[RNF32-AS1]] | -0.50 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[NEK10]] | -0.48 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[SSUH2]] | -0.48 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[GUCY1A2]] | -0.47 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[AADAC]] | -0.46 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ESRRB]] | -0.46 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[TXK]] | -0.46 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[CDK14]] | -0.46 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[LMO7]] | -0.46 | -0.35 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSC2]] | B | DSC2 activity weakens PGAP2's drug response | lines that do not express DSC2 (22) vs lines expressing it (26) | the lines without DSC2 respond 1.35× as strongly (z diff -1.16); strongest at Homoharringtonine 0.5 µM: 0.21x vs 0.49x (z diff -2.8) | 0.068 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.6, -3.8); signed map (-39.7, -20.7). **Vector** length 67.7, 11.9% of its response variance represented; |z| ≥ 3 in 1,064 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +2.7 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +2.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.6 | +4.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -25.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -17.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | post-GPI attachment to proteins 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:3,797,724-3,826,371 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FRAG1, CWH43-N; previously MRT21, MRT17 |
| Gene groups (HGNC) | Acyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHJ9](https://www.uniprot.org/uniprotkb/Q9UHJ9) (Acyltransferase PGAP2):

> Involved in the fatty acid remodeling steps of GPI-anchor maturation where the unsaturated acyl chain at sn-2 of inositol phosphate is replaced by a saturated stearoyl chain. May catalyze the second step of the fatty acid remodeling, by reacylating a lyso-GPI intermediate at sn-2 of inositol phosphate by a saturated chain (By similarity). The fatty acid remodeling steps is critical for the integration of GPI-APs into lipid rafts.

**Summary**, from NCBI Gene [27315](https://www.ncbi.nlm.nih.gov/gene/27315):

> The protein encoded by this gene plays a role in the maturation of glycosylphosphatidylinositol (GPI) anchors on GPI-anchored proteins. Mutations in this gene are associated with an autosomal recessive syndrome characterized by hyperphosphatasia and intellectual disability. [provided by RefSeq, Jul 2017]

**Accessions** — [HGNC:17893](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17893) · Entrez [27315](https://www.ncbi.nlm.nih.gov/gene/27315) · UniProt [Q9UHJ9](https://www.uniprot.org/uniprotkb/Q9UHJ9) · Ensembl [ENSG00000148985](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148985)

## Data

Gene col 7333: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7333); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7333, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7333]; `tensor/DDL_lfc|DDL_z.npy` [7333]; `embed/gene_vectors.npy` [7333]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7333 or target_col == 7333). Every well: [[PGAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

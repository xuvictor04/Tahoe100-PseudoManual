---
symbol: "KCNIP2"
type: "gene"
col: 4151
ensembl_id: "ENSG00000120049"
name: "potassium voltage-gated channel interacting protein 2"
location: "10q24.32"
module: 126
arm: "+"
pooled_cpm: 7.09
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# KCNIP2

*potassium voltage-gated channel interacting protein 2* — 10q24.32

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.206× (z -12.2, q 2e-31, down in 39 of 44 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.218× (z -6.4, q 2e-08, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL18BP]] (+0.71, fdr 1e-05), [[MKRN5P]] (+0.65, fdr 1e-05), [[CYP2D7]] (+0.64, fdr 1e-05); moves opposite to [[MRPL57]] (-0.60, fdr 4e-05), [[COMMD3]] (-0.59, fdr 2e-05), [[NDUFA7]] (-0.56, fdr 1e-05).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EID2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4151.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +4.9 | 5e-04 | 15/47 (NCI-H23, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4151.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.206×** | -12.2 | 2e-31 | 39/44 (PANC-1, A-427, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.484×** | -8.2 | 6e-14 | 31/45 (CFPAC-1, HEC-1-A, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.394×** | -7.5 | 2e-11 | 33/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.445×** | -6.5 | 1e-08 | 29/43 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.218×** | -6.4 | 2e-08 | 32/45 (SNU-423, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.459×** | -6.1 | 1e-07 | 28/45 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.470×** | -6.0 | 1e-07 | 26/42 (PANC-1, hTERT-HPNE, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.515×** | -5.1 | 2e-05 | 23/35 (HS-578T, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.589×** | -4.2 | 0.001 | 20/45 (H4, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.594×** | -4.2 | 0.002 | 24/44 (NCI-H2030, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.634×** | -3.6 | 0.014 | 20/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.642×** | -3.5 | 0.019 | 17/44 (SW1417, KATO III, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.644×** | -3.5 | 0.019 | 16/45 (NCI-H1573, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~69% of this change | **0.638×** | -3.5 | 0.022 | 20/38 (SNU-423, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.672×** | -3.1 | 0.071 | 15/46 (MIA PaCa-2, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.67 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4151. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.04 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0671× (z -13.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 11.5 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0255× (z -17.4) |
| [[A549 (line)]] | wt | 6.49 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0483× (z -10.8) |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -9.8) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Raltitrexed (drug)]] 0.5 µM 0.0721× (z -8.9) |
| [[H4 (line)]] | wt | 8.85 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0421× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 8.97 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -12.2) ⚠ cell-cycle shift, explains ~75% of this change |
| [[MIA PaCa-2 (line)]] | alt | 13.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.139× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 6.31 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0741× (z -10.9) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.101× (z -9.6) |
| [[A-172 (line)]] | wt | 9.89 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -8.9) ⚠ cell-cycle shift, explains ~75% of this change |
| [[A498 (line)]] | wt | 4.73 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -8.5) ⚠ cell-cycle shift, explains ~75% of this change |
| [[AsPC-1 (line)]] | alt | 3.34 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0384× (z -9.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[CFPAC-1 (line)]] | alt | 5.70 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0992× (z -12.9) ⚠ cell-cycle shift, explains ~75% of this change |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0933× (z -9.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 8.49 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.137× (z -8.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HS-578T (line)]] | alt | 5.09 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0682× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[hTERT-HPNE (line)]] | wt | 6.65 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0312× (z -9.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[J82 (line)]] | alt | 4.33 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0815× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 7.68 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0653× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[LS 180 (line)]] | wt | 6.05 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0444× (z -11.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H1573 (line)]] | alt | 7.83 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0518× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[NCI-H460 (line)]] | wt | 6.62 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.131× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 6.88 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0553× (z -8.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW1417 (line)]] | alt | 3.95 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0741× (z -8.8) |
| [[AN3 CA (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4151), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL18BP]] | +0.71 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[MKRN5P]] | +0.65 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[CYP2D7]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[RNF32-AS1]] | +0.61 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[NPIPB11]] | +0.60 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[CERS2]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[LY6G5B]] | +0.58 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[EOLA2-DT]] | +0.58 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[SMG1P6]] | +0.57 | +0.36 / +0.63 | both halves | 1e-04 |  |
| [[EEF1A1]] | +0.56 | +0.37 / +0.58 | both halves | 8e-05 |  |
| [[MTA1]] | +0.56 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[LINC01355]] | +0.56 | +0.45 / +0.64 | both halves | 3e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL57]] | -0.60 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[COMMD3]] | -0.59 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[NDUFA7]] | -0.56 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[FOXA2]] | -0.55 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[MED19]] | -0.55 | -0.37 / -0.58 | both halves | 8e-05 |  |
| [[MRPS31]] | -0.55 | -0.39 / -0.62 | both halves | 6e-05 |  |
| [[METTL23]] | -0.53 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[HCFC2]] | -0.53 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[ATP5PO]] ⚠ | -0.53 | -0.39 / -0.55 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DMAC1]] | -0.53 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[EID2]] | -0.53 | -0.36 / -0.61 | both halves | 1e-04 |  |
| [[IFI27L2]] | -0.52 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[PITPNA-AS1]] | -0.52 | -0.37 / -0.51 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EID2]] | C | EID2 activity raises KCNIP2's level | lines that do not express EID2 (3) vs lines expressing it (47) | 1.91× lower at baseline in the lines without EID2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.578). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.4, -15.7); signed map (-9.3, -36.8). **Vector** length 58.2, 8.69% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.7 | +0.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | -1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.4 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.8 | -0.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.7 | +4.9 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | +1.1 | +1.1 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.1 | +1.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.0 | -12.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -2.5 | -8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | +0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.2 | -3.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.5 | -1.0 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:101,825,974-101,843,920 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KCHIP2 |
| Gene groups (HGNC) | Potassium voltage-gated channel regulatory subunits; EF-hand domain containing |
| Hallmark sets | COMPLEMENT |
| Reactome | 3 pathways, smallest: Phase 1 - inactivation of fast Na+ channels; Cardiac conduction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NS61](https://www.uniprot.org/uniprotkb/Q9NS61) (A-type potassium channel modulatory protein KCNIP2):

> Regulatory subunit of Kv4/D (Shal)-type voltage-gated rapidly inactivating A-type potassium channels. Modulates channel density, inactivation kinetics and rate of recovery from inactivation in a calcium-dependent and isoform-specific manner. Involved in KCND2 and KCND3 trafficking to the cell surface. May be required for the expression of I(To) currents in the heart (By similarity).

**Summary**, from NCBI Gene [30819](https://www.ncbi.nlm.nih.gov/gene/30819):

> This gene encodes a member of the family of voltage-gated potassium (Kv) channel-interacting proteins (KCNIPs), which belongs to the recoverin branch of the EF-hand superfamily. Members of the KCNIP family are small calcium binding proteins. They all have EF-hand-like domains, and differ from each other in the N-terminus. They are integral subunit components of native Kv4 channel complexes. They may regulate A-type currents, and hence neuronal excitability, in response to changes in …

**Accessions** — [HGNC:15522](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15522) · Entrez [30819](https://www.ncbi.nlm.nih.gov/gene/30819) · UniProt [Q9NS61](https://www.uniprot.org/uniprotkb/Q9NS61) · Ensembl [ENSG00000120049](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120049)

## Data

Gene col 4151: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4151); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4151, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4151]; `tensor/DDL_lfc|DDL_z.npy` [4151]; `embed/gene_vectors.npy` [4151]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4151 or target_col == 4151). Every well: [[KCNIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

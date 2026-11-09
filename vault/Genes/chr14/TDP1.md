---
symbol: "TDP1"
type: "gene"
col: 482
ensembl_id: "ENSG00000042088"
name: "tyrosyl-DNA phosphodiesterase 1"
location: "14q32.11"
module: 67
arm: "+"
pooled_cpm: 32.51
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# TDP1

*tyrosyl-DNA phosphodiesterase 1* — 14q32.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.05 µM: 1.33× (z +5.1, q 2e-04, up in 21 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.589× (z -13.5, q 1e-38, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POC1A]] (+0.71, fdr 7e-06), [[NSD2]] (+0.71, fdr 7e-06), [[SPAG5]] (+0.68, fdr 7e-06); moves opposite to [[ELF1]] (-0.54, fdr 3e-05), [[TICAM1]] (-0.53, fdr 4e-05), [[MAP3K2-DT]] (-0.53, fdr 1e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 482.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **1.33×** | +5.1 | 2e-04 | 21/46 (PANC-1, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.31×** | +4.8 | 4e-04 | 21/47 (SW480, A498, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +4.6 | 9e-04 | 16/36 (SHP-77, BT-474, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.29×** | +4.4 | 0.002 | 19/46 (LS 180, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.18× | +4.2 | 0.003 | 21/47 (LoVo, NCI-H1573, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.024 | 11/46 (SW480, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.21×** | +3.4 | 0.053 | 12/47 (SW48, HT-29, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.053 | 15/46 (NCI-H2030, SW 900, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 482.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.589×** | -13.5 | 1e-38 | 37/47 (RPMI-7951, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.507×** | -12.2 | 8e-32 | 41/47 (HCT15, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.544×** | -11.0 | 1e-25 | 36/47 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.544×** | -10.5 | 9e-24 | 40/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.740×** | -7.7 | 2e-12 | 33/47 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.686×** | -6.8 | 1e-09 | 27/46 (NCI-H460, SW48, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.748×** | -5.2 | 1e-05 | 25/47 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.759×** | -4.6 | 3e-04 | 21/41 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.615×** | -4.6 | 3e-04 | 21/47 (SNU-1, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.794×** | -4.2 | 0.002 | 20/47 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.789×** | -4.1 | 0.002 | 21/44 (NCI-H2030, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.789×** | -4.1 | 0.002 | 18/46 (HCT15, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.854× | -4.1 | 0.002 | 20/47 (A549, PANC-1, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.800×** | -4.0 | 0.002 | 19/47 (RPMI-7951, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.800×** | -4.0 | 0.002 | 22/47 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 0.5 µM |  | 0.841× | -3.1 | 0.055 | 7/47 (SW 1088, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 482. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.5 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.218× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.212× (z -15.1) |
| [[A-427 (line)]] | wt | 52.6 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -10.5) |
| [[SW480 (line)]] | alt | 42.3 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.396× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 50.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -13.2) |
| [[A-172 (line)]] | wt | 39.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -13.7) |
| [[AN3 CA (line)]] | alt | 52.6 | 0 | 2 | — | [[Tadalafil (drug)]] 0.05 µM 0.0415× (z -14.0) |
| [[HCT15 (line)]] | alt | 43.0 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.137× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 30.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 53.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 71.8 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.322× (z -10.2) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 36.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.344× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -20.5) |
| [[SK-MEL-2 (line)]] | alt | 35.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -16.5) |
| [[SW48 (line)]] | wt | 35.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0794× (z -14.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 22.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.354× (z -8.6) |
| [[C-33 A (line)]] | alt | 29.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -10.8) |
| [[C32 (line)]] | wt | 27.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.249× (z -9.0) |
| [[H4 (line)]] | wt | 48.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.238× (z -8.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 26.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -10.0) |
| [[HS-578T (line)]] | alt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -12.7) |
| [[J82 (line)]] | alt | 34.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -12.0) |
| [[LoVo (line)]] | wt | 28.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +10.7) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[NCI-H1573 (line)]] | alt | 25.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.314× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 43.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -15.7) |
| [[NCI-H23 (line)]] | alt | 39.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.314× (z -10.4) |
| [[RKO (line)]] | wt | 42.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.316× (z -8.9) |
| [[SNU-423 (line)]] | alt | 29.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.318× (z -8.5) |
| [[SW1417 (line)]] | alt | 21.7 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.292× (z -8.5) |
| [[A549 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 482), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POC1A]] | +0.71 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[NSD2]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair |
| [[SPAG5]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[DTYMK]] | +0.67 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[MPHOSPH9]] | +0.67 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[SUGP2]] | +0.67 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[TICRR]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[EFCAB11]] | +0.64 | +0.66 / +0.57 | both halves | 1e-05 | STRING 461; ⚠ same locus (0.2 kb: neighbours can correlate without regulation) |
| [[NDC1]] | +0.64 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[CIT]] | +0.63 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[BUB3]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[KIF22]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[CKS1B]] | +0.62 | +0.69 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELF1]] | -0.54 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[TICAM1]] | -0.53 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[MAP3K2-DT]] | -0.53 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ZNF579]] | -0.51 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[FMO4]] | -0.51 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[TUBB2A]] | -0.51 | -0.47 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TDP1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.645). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-34.8, -51.6); signed map (-44.2, -42.3). **Vector** length 97.9, 22.7% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.55 to 12); *G2/M checkpoint* (hallmark, mean cos +0.57 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.56 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM |  | +4.4 | +5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +1.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +3.0 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +2.9 | +4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +1.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.8 | +3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.7 | +1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.7 | +0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +0.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.3 | -12.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.1 | -7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.0 | -4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.4 | -13.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -10.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -1.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | tyrosyl-DNA phosphodiesterase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.11 — chr14:89,954,939-90,044,764 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11090, SCAN1 |
| Reactome | 3 pathways, smallest: Nonhomologous End-Joining (NHEJ); DNA Double-Strand Break Repair; DNA Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUW8](https://www.uniprot.org/uniprotkb/Q9NUW8) (Tyrosyl-DNA phosphodiesterase 1):

> DNA repair enzyme that can remove a variety of covalent adducts from DNA through hydrolysis of a 3'-phosphodiester bond, giving rise to DNA with a free 3' phosphate. Catalyzes the hydrolysis of dead-end complexes between DNA and the topoisomerase I active site tyrosine residue. Hydrolyzes 3'-phosphoglycolates on protruding 3' ends on DNA double-strand breaks due to DNA damage by radiation and free radicals. Acts on blunt-ended double-strand DNA breaks and on single-stranded DNA. Has low …

**Summary**, from NCBI Gene [55775](https://www.ncbi.nlm.nih.gov/gene/55775):

> The protein encoded by this gene is involved in repairing stalled topoisomerase I-DNA complexes by catalyzing the hydrolysis of the phosphodiester bond between the tyrosine residue of topoisomerase I and the 3-prime phosphate of DNA. This protein may also remove glycolate from single-stranded DNA containing 3-prime phosphoglycolate, suggesting a role in repair of free-radical mediated DNA double-strand breaks. This gene is a member of the phospholipase D family and contains two PLD …

**Accessions** — [HGNC:18884](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18884) · Entrez [55775](https://www.ncbi.nlm.nih.gov/gene/55775) · UniProt [Q9NUW8](https://www.uniprot.org/uniprotkb/Q9NUW8) · Ensembl [ENSG00000042088](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000042088)

## Data

Gene col 482: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 482); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 482, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 482]; `tensor/DDL_lfc|DDL_z.npy` [482]; `embed/gene_vectors.npy` [482]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 482 or target_col == 482). Every well: [[TDP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TDP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

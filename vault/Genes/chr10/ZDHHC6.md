---
symbol: "ZDHHC6"
type: "gene"
col: 338
ensembl_id: "ENSG00000023041"
name: "zDHHC palmitoyltransferase 6"
location: "10q25.2"
module: 65
arm: "+"
pooled_cpm: 24.04
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# ZDHHC6

*zDHHC palmitoyltransferase 6* — 10q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.67× (z +9.7, q 2e-19, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.554× (z -11.3, q 7e-27, down in 37 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.653× (z -8.1, q 7e-14, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELMOD2]] (+0.63, fdr 1e-05), [[DLST]] (+0.63, fdr 1e-05), [[NUP43]] (+0.59, fdr 3e-05); moves opposite to [[SIK3]] (-0.63, fdr 1e-05), [[NR2F1]] (-0.58, fdr 1e-05), [[HES1]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 338.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +9.7 | 2e-19 | 33/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.58×** | +8.7 | 8e-16 | 32/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +7.6 | 6e-12 | 25/48 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.26×** | +6.1 | 1e-07 | 22/48 (CFPAC-1, SW480, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +5.1 | 4e-05 | 24/48 (LoVo, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.30×** | +5.0 | 5e-05 | 17/48 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.8 | 1e-04 | 16/32 (A498, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.7 | 0.016 | 9/48 (SW1417, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.039 | 3/47 (A498, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 5 µM |  | 1.12× | +3.1 | 0.12 | 3/48 (LS 180, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 338.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.554×** | -11.3 | 7e-27 | 37/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.619×** | -9.2 | 1e-17 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.653×** | -8.1 | 7e-14 | 32/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.693×** | -7.0 | 3e-10 | 29/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.781×** | -6.7 | 2e-09 | 25/47 (H4, HEC-1-A, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.758×** | -4.9 | 9e-05 | 14/36 (Panc 03.27, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.804×** | -4.0 | 0.004 | 18/47 (HOP62, NCI-H1792, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.826×** | -3.7 | 0.017 | 18/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.830×** | -3.6 | 0.021 | 13/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Arbutin (drug)]] 5 µM |  | **0.828×** | -3.5 | 0.027 | 14/48 (HepG2/C3A, A-172, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.708×** | -3.5 | 0.029 | 9/48 (SW48, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 338. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 28.7 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.21× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.384× (z -10.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.443× (z -9.0) |
| [[PANC-1 (line)]] | alt | 36.6 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.277× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.383× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 19.2 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.222× (z -13.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.390× (z -8.7) |
| [[AN3 CA (line)]] | alt | 24.4 | 0 | 2 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0853× (z -9.4) |
| [[BT-474 (line)]] | alt | 7.50 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.103× (z -8.6) |
| [[LS 180 (line)]] | wt | 38.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.320× (z -10.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[MIA PaCa-2 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -13.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 35.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.326× (z -9.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 338), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELMOD2]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[DLST]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[NUP43]] | +0.59 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[RFT1]] | +0.58 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[SLC30A6]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[CDC16]] | +0.55 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[UCHL5]] | +0.55 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[DTD1]] | +0.55 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[EDEM2]] | +0.54 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[TRAK2]] | +0.54 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[ZNF273]] | +0.54 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[SPTLC1]] | +0.54 | +0.48 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIK3]] | -0.63 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[NR2F1]] | -0.58 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[HES1]] | -0.56 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[TLE4]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[TSC22D1]] | -0.53 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[FOXP1]] | -0.53 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[DENND5B]] | -0.52 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[LITAF]] | -0.52 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[TFAP2C]] | -0.51 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[FOXA2]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[CABLES1]] | -0.51 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[TGIF2]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ZDHHC6's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.311). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.5, -52.9); signed map (-34.9, -31.8). **Vector** length 76.4, 13.5% of its response variance represented; |z| ≥ 3 in 929 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +5.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +3.4 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.4 | -0.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.3 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | -0.2 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | -11.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.4 | -9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.1 | -6.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -8.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.0 | -7.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -0.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | +1.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.2 — chr10:112,424,428-112,447,572 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF376, FLJ21952 |
| Gene groups (HGNC) | Zinc fingers DHHC-type; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6R6](https://www.uniprot.org/uniprotkb/Q9H6R6) (Palmitoyltransferase ZDHHC6):

> Endoplasmic reticulum palmitoyl acyltransferase that mediates palmitoylation of proteins such as AMFR, CALX, ITPR1 and TFRC. Palmitoylates calnexin (CALX), which is required for its association with the ribosome-translocon complex and efficient folding of glycosylated proteins. Mediates palmitoylation of AMFR, promoting AMFR distribution to the peripheral endoplasmic reticulum. Together with SELENOK, palmitoylates ITPR1 in immune cells, leading to regulate ITPR1 stability and function. …

**Summary**, from NCBI Gene [64429](https://www.ncbi.nlm.nih.gov/gene/64429):

> Enables palmitoyltransferase activity and protein-cysteine S-stearoyltransferase activity. Involved in intracellular signal transduction. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19160](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19160) · Entrez [64429](https://www.ncbi.nlm.nih.gov/gene/64429) · UniProt [Q9H6R6](https://www.uniprot.org/uniprotkb/Q9H6R6) · Ensembl [ENSG00000023041](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000023041)

## Data

Gene col 338: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 338); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 338, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 338]; `tensor/DDL_lfc|DDL_z.npy` [338]; `embed/gene_vectors.npy` [338]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 338 or target_col == 338). Every well: [[ZDHHC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

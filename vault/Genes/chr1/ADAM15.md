---
symbol: "ADAM15"
type: "gene"
col: 6764
ensembl_id: "ENSG00000143537"
name: "ADAM metallopeptidase domain 15"
location: "1q21.3"
module: 50
arm: "+"
pooled_cpm: 17.47
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# ADAM15

*ADAM metallopeptidase domain 15* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.58× (z +12.5, q 4e-33, up in 27 of 29 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +12.0, q 7e-31, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.629× (z -9.1, q 8e-17, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAGA]] (+0.74, fdr 7e-06), [[COLGALT1]] (+0.72, fdr 7e-06), [[SLC25A39]] (+0.70, fdr 7e-06); moves opposite to [[MED18]] (-0.72, fdr 7e-06), [[CCDC174]] (-0.70, fdr 7e-06), [[WASHC1]] (-0.67, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CELSR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6764.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.58×** | +12.5 | 4e-33 | 27/29 (LoVo, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +12.0 | 7e-31 | 39/45 (A498, A549, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **2.31×** | +11.5 | 2e-28 | 44/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.26×** | +11.2 | 6e-27 | 34/37 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.15×** | +10.5 | 1e-23 | 43/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.92×** | +9.0 | 3e-17 | 43/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.95×** | +8.5 | 2e-15 | 25/32 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.69×** | +7.2 | 6e-11 | 33/45 (A-172, SW1417, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.57×** | +6.0 | 1e-07 | 26/46 (C32, A498, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +5.2 | 1e-05 | 21/42 (Hs 766T, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.47×** | +5.1 | 2e-05 | 23/47 (NCI-H2347, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.44×** | +5.0 | 3e-05 | 24/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.42×** | +4.8 | 7e-05 | 20/47 (HOP62, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.82×** | +4.3 | 7e-04 | 16/48 (NCI-H2030, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.31×** | +3.7 | 0.008 | 20/48 (NCI-H460, SW480, …) | rises with dose | composition shift; position effect removed |
| [[Olanzapine (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.012 | 9/47 (A-172, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Folic acid (drug)]] 5 µM |  | 1.19× | +3.3 | 0.029 | 8/48 (SNU-1, NCI-H2347, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.034 | 15/47 (HOP62, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.080 | 10/46 (H4, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6764.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.629×** | -9.1 | 8e-17 | 36/47 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.592×** | -7.2 | 1e-10 | 32/44 (SW48, C-33 A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.644×** | -6.1 | 2e-07 | 28/46 (hTERT-HPNE, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.662×** | -5.5 | 6e-06 | 24/47 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Pemetrexed (drug)]] 0.5 µM |  | **0.706×** | -4.8 | 2e-04 | 20/47 (PANC-1, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.804×** | -4.3 | 0.002 | 22/48 (A-172, H4, …) | two highest doses | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **0.782×** | -3.3 | 0.085 | 14/45 (H4, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.803× | -3.1 | 0.16 | 10/48 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.58 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6764. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 30.2 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +10.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.353× (z -8.5) |
| [[A-172 (line)]] | wt | 30.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -10.3) |
| [[A498 (line)]] | wt | 20.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +11.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.283× (z -10.1) |
| [[LoVo (line)]] | wt | 13.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW48 (line)]] | wt | 26.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0431× (z -15.7) |
| [[A549 (line)]] | wt | 8.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.90× (z +10.5) | — |
| [[C-33 A (line)]] | alt | 16.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0625× (z -12.5) |
| [[KATO III (line)]] | alt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 26.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -17.8) |
| [[SNU-1 (line)]] | wt | 21.6 | 0 | 1 | — | [[Berbamine (drug)]] 5 µM 0.272× (z -9.0) |
| [[SNU-423 (line)]] | alt | 8.77 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0610× (z -12.4) |
| [[A-427 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6764), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAGA]] | +0.74 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[COLGALT1]] | +0.72 | +0.66 / +0.69 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[SLC25A39]] | +0.70 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[RBBP7]] | +0.69 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[ZDHHC3]] | +0.68 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[CMPK1]] | +0.68 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[IMPA2]] | +0.67 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[CDK16]] | +0.67 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[NUTF2]] | +0.67 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[BSG]] | +0.66 | +0.66 / +0.53 | both halves | 1e-05 | pathway: Degradation of the extracellular matrix |
| [[ATP1A1]] | +0.66 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[SELENON]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED18]] | -0.72 | -0.68 / -0.66 | both halves | 7e-06 |  |
| [[CCDC174]] | -0.70 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[WASHC1]] | -0.67 | -0.71 / -0.57 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.66 | -0.67 / -0.56 | both halves | 1e-05 |  |
| [[GATAD1]] | -0.66 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[SEC62]] | -0.66 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | -0.65 | -0.66 / -0.66 | both halves | 7e-06 |  |
| [[PIGBOS1]] | -0.65 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[GORAB]] | -0.64 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[PPIG]] | -0.63 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[SNHG11]] | -0.63 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[ATF4]] | -0.62 | -0.63 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CELSR2]] | B | CELSR2 activity raises ADAM15's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 1.42× lower at baseline in the lines without CELSR2 | 0.042 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |
| [[IL23A]] | B | IL23A activity lowers ADAM15's level | lines that do not express IL23A (6) vs lines expressing it (44) | 1.50× higher at baseline in the lines without IL23A | 0.053 | ⚠ within organs, on part of the lines; also absent: MYRF; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.763). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.1, -25.3); signed map (-27.1, -41.5). **Vector** length 99.2, 22.5% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +3.3 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +3.2 | +12.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +12.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.0 | +9.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.0 | +11.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.5 | +2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.3 | +2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.2 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.6 | -7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.2 | -9.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.1 | -5.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.4 | -4.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.3 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.3 | -1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -1.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | -2.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase domain 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:155,050,566-155,062,775 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MDC15 |
| Gene groups (HGNC) | ADAM metallopeptidase domain containing |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 3 pathways, smallest: Invadopodia formation; Degradation of the extracellular matrix; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13444](https://www.uniprot.org/uniprotkb/Q13444) (Disintegrin and metalloproteinase domain-containing protein 15):

> Active metalloproteinase with gelatinolytic and collagenolytic activity. Plays a role in the wound healing process. Mediates both heterotypic intraepithelial cell/T-cell interactions and homotypic T-cell aggregation. Inhibits beta-1 integrin-mediated cell adhesion and migration of airway smooth muscle cells. Suppresses cell motility on or towards fibronectin possibly by driving alpha-v/beta-1 integrin (ITAGV-ITGB1) cell surface expression via ERK1/2 inactivation. Cleaves E-cadherin in response …

**Summary**, from NCBI Gene [8751](https://www.ncbi.nlm.nih.gov/gene/8751):

> The protein encoded by this gene is a member of the ADAM (a disintegrin and metalloproteinase) protein family. ADAM family members are type I transmembrane glycoproteins known to be involved in cell adhesion and proteolytic ectodomain processing of cytokines and adhesion molecules. This protein contains multiple functional domains including a zinc-binding metalloprotease domain, a disintegrin-like domain, as well as a EGF-like domain. Through its disintegrin-like domain, this protein …

**Accessions** — [HGNC:193](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:193) · Entrez [8751](https://www.ncbi.nlm.nih.gov/gene/8751) · UniProt [Q13444](https://www.uniprot.org/uniprotkb/Q13444) · Ensembl [ENSG00000143537](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143537)

## Data

Gene col 6764: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6764); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6764, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6764]; `tensor/DDL_lfc|DDL_z.npy` [6764]; `embed/gene_vectors.npy` [6764]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6764 or target_col == 6764). Every well: [[ADAM15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAM15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

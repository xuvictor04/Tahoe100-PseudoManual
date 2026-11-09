---
symbol: "TRAF5"
type: "gene"
col: 1350
ensembl_id: "ENSG00000082512"
name: "TNF receptor associated factor 5"
location: "1q32.3"
module: 18
arm: "+"
pooled_cpm: 35.57
n_lines_expressing: 48
n_dd_up: 0
n_dd_down: 25
n_dd_up_clean: 0
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# TRAF5

*TNF receptor associated factor 5* — 1q32.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.410× (z -17.8, q 0e+00, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AADAT]] (+0.58, fdr 1e-05), [[FAM136A]] (+0.57, fdr 1e-05), [[ADAT2]] (+0.56, fdr 3e-05); moves opposite to [[MTHFR]] (-0.53, fdr 1e-05), [[CCNI]] (-0.53, fdr 5e-05), [[RAB33B-AS1]] (-0.51, fdr 2e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[COLGALT2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1350.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | 1.16× | +3.0 | 0.62 | 17/46 (COLO 205, A-427, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1350.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.410×** | -17.8 | 0e+00 | 42/46 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.329×** | -15.7 | 0e+00 | 38/46 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.386×** | -13.4 | 1e-38 | 42/46 (LS 180, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.433×** | -11.8 | 6e-30 | 39/45 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.575×** | -7.5 | 8e-12 | 30/46 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.598×** | -7.3 | 4e-11 | 25/46 (MIA PaCa-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.624×** | -6.6 | 2e-09 | 31/46 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.649×** | -5.9 | 3e-07 | 22/36 (LoVo, SHP-77, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.754×** | -5.6 | 1e-06 | 27/46 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.652×** | -5.6 | 1e-06 | 26/40 (SW480, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.651×** | -5.5 | 2e-06 | 24/43 (AN3 CA, SW48, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.694×** | -5.0 | 3e-05 | 25/43 (J82, AsPC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.711×** | -4.8 | 6e-05 | 26/46 (A-172, Panc 03.27, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.701×** | -4.8 | 6e-05 | 24/44 (SW48, SW480, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -4.6 | 1e-04 | 23/45 (SK-MEL-2, A-172, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.739×** | -4.3 | 7e-04 | 23/44 (Panc 03.27, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.604×** | -3.7 | 0.006 | 15/44 (Panc 03.27, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **0.774×** | -3.6 | 0.008 | 18/44 (HCT15, NCI-H1792, …) | two highest doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.805×** | -2.9 | 0.078 | 10/45 (HOP62, AsPC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.864× | -2.9 | 0.083 | 17/46 (HS-578T, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1350. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 128 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.129× (z -15.5) |
| [[A-172 (line)]] | wt | 49.5 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 35.7 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -18.0) |
| [[LoVo (line)]] | wt | 42.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -17.9) |
| [[MIA PaCa-2 (line)]] | alt | 36.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0873× (z -17.5) |
| [[A549 (line)]] | wt | 27.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -16.3) |
| [[J82 (line)]] | alt | 40.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -15.5) |
| [[SW48 (line)]] | wt | 54.2 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.190× (z -10.3) |
| [[COLO 205 (line)]] | alt | 83.0 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.162× (z -11.0) |
| [[HS-578T (line)]] | alt | 32.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -13.6) |
| [[HT-29 (line)]] | alt | 28.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.232× (z -10.8) |
| [[LS 180 (line)]] | wt | 73.0 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.142× (z -17.0) |
| [[Panc 03.27 (line)]] | alt | 27.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -13.8) |
| [[PANC-1 (line)]] | alt | 27.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -25.6) |
| [[AN3 CA (line)]] | alt | 66.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0660× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.161× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 42.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -15.7) |
| [[SHP-77 (line)]] | alt | 33.4 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.111× (z -15.5) ⚠ toxic; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.253× (z -10.0) |
| [[SW1417 (line)]] | alt | 60.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -13.0) |
| [[A-427 (line)]] | wt | 23.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.238× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 14.6 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.128× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.255× (z -8.9) |
| [[KATO III (line)]] | alt | 23.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 38.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -12.1) |
| [[RKO (line)]] | wt | 47.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.221× (z -11.9) |
| [[A498 (line)]] | wt | 19.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 29.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.3) |
| [[HCT15 (line)]] | alt | 41.2 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0686× (z -17.4) |
| [[HOP62 (line)]] | alt | 33.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -18.2) |
| [[Hs 766T (line)]] | wt | 17.3 | 0 | 1 | — | [[Futibatinib (drug)]] 0.05 µM 0.124× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 19.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.283× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 18.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -8.7) |
| [[SW 900 (line)]] | alt | 22.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -10.5) |
| [[BT-474 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.74 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.12 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1350), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AADAT]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[FAM136A]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ADAT2]] | +0.56 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[PLCG1]] | +0.55 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ZC3HAV1L]] | +0.54 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ZFYVE9]] | +0.54 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[SLC25A15]] | +0.54 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[CSTF2]] | +0.53 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[AMER1]] | +0.53 | +0.43 / +0.43 | both halves | 4e-05 |  |
| [[USP46]] | +0.53 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[MVB12B]] | +0.53 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[ALDH5A1]] | +0.53 | +0.43 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTHFR]] | -0.53 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[CCNI]] | -0.53 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[RAB33B-AS1]] | -0.51 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[PRMT2]] | -0.50 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[JUND]] | -0.49 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[GLCCI1]] | -0.49 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[NBEAL1]] | -0.49 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[INAFM1]] | -0.49 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[STX12]] | -0.49 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[FAM177A1]] | -0.48 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[DLGAP4]] | -0.46 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[MFSD11]] | -0.46 | -0.54 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COLGALT2]] | B | COLGALT2 activity raises TRAF5's level | lines that do not express COLGALT2 (23) vs lines expressing it (27) | 1.62× lower at baseline in the lines without COLGALT2 | 0.054 | ⚠ within organs, on part of the lines; also absent: PRRX1, SYT11, GNAT3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.532). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-24.2, -29.4); signed map (-12.7, -42.1). **Vector** length 82.8, 18.5% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | +5.3 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +5.1 | -5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | -5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +4.1 | -5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +3.8 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.5 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | -2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -17.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.9 | -7.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -7.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.4 | -3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -3.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.9 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor associated factor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.3 — chr1:211,326,615-211,374,946 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RNF84 |
| Gene groups (HGNC) | Ring finger proteins; TNF receptor associated factors; Zinc fingers TRAF-type; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [O00463](https://www.uniprot.org/uniprotkb/O00463) (TNF receptor-associated factor 5):

> Adapter protein and signal transducer that links members of the tumor necrosis factor receptor family to different signaling pathways by association with the receptor cytoplasmic domain and kinases. Mediates activation of NF-kappa-B and probably JNK. Seems to be involved in apoptosis. Plays a role in mediating activation of NF-kappa-B by EIF2AK2/PKR.

**Summary**, from NCBI Gene [7188](https://www.ncbi.nlm.nih.gov/gene/7188):

> The scaffold protein encoded by this gene is a member of the tumor necrosis factor receptor-associated factor (TRAF) protein family and contains a meprin and TRAF homology (MATH) domain, a RING-type zinc finger, and two TRAF-type zinc fingers. TRAF proteins are associated with, and mediate signal transduction from members of the TNF receptor superfamily. This protein is one of the components of a multiple protein complex which binds to tumor necrosis factor (TNF) receptor cytoplasmic domains …

**Accessions** — [HGNC:12035](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12035) · Entrez [7188](https://www.ncbi.nlm.nih.gov/gene/7188) · UniProt [O00463](https://www.uniprot.org/uniprotkb/O00463) · Ensembl [ENSG00000082512](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082512)

## Data

Gene col 1350: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1350); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1350, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1350]; `tensor/DDL_lfc|DDL_z.npy` [1350]; `embed/gene_vectors.npy` [1350]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1350 or target_col == 1350). Every well: [[TRAF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAF5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

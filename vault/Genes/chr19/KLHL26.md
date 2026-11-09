---
symbol: "KLHL26"
type: "gene"
col: 9471
ensembl_id: "ENSG00000167487"
name: "kelch like family member 26"
location: "19p13.11"
module: 3
arm: "+"
pooled_cpm: 5.82
n_lines_expressing: 48
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# KLHL26

*kelch like family member 26* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 4.01× (z +17.6, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.454× (z -10.0, q 6e-21, down in 21 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.705× (z -4.3, q 0.003, down in 12 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H2347 0.0992×, SW480 0.124×, SW1417 0.106×, Panc 03.27 0.150×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (A498 0.0804×, NCI-H2347 0.0773×, CFPAC-1 0.0963×, HS-578T 0.147×, …; ⚠ toxic; transcription drop); [[Menadione (drug)]] 5 µM in 1 line (A-172 0.0820×); [[Busulfan (drug)]] 0.05 µM in 1 line (HCT15 0.0692×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RPMI-7951 0.0706×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC38]] (+0.75, fdr 7e-06), [[BAIAP3]] (+0.74, fdr 7e-06), [[MAST3]] (+0.71, fdr 2e-05); moves opposite to [[CRPPA]] (-0.67, fdr 6e-05), [[STMP1]] (-0.65, fdr 1e-05), [[ARSB]] (-0.63, fdr 4e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RGS14]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9471.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.01×** | +17.6 | 0e+00 | 44/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.61×** | +16.2 | 0e+00 | 42/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.62×** | +12.2 | 9e-32 | 40/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +10.6 | 3e-24 | 31/39 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +6.2 | 7e-08 | 20/40 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +5.5 | 3e-06 | 15/45 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +5.1 | 3e-05 | 14/45 (PANC-1, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +4.3 | 0.001 | 10/43 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.009 | 9/44 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +3.4 | 0.034 | 4/44 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.034 | 11/45 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.40× | +3.0 | 0.12 | 6/31 (SW 900, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9471.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H2347 0.0992×, SW480 0.124×, SW1417 0.106×, Panc 03.27 0.150×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (A498 0.0804×, NCI-H2347 0.0773×, CFPAC-1 0.0963×, HS-578T 0.147×, …; ⚠ toxic; transcription drop); [[Menadione (drug)]] 5 µM in 1 line (A-172 0.0820×); [[Busulfan (drug)]] 0.05 µM in 1 line (HCT15 0.0692×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RPMI-7951 0.0706×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.454×** | -10.0 | 6e-21 | 21/27 (NCI-H2347, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.683×** | -4.7 | 8e-04 | 8/11 (A498, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.705×** | -4.3 | 0.003 | 12/42 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | 0.783× | -3.1 | 0.25 | 7/45 (SW 1088, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.788× | -3.0 | 0.26 | 7/44 (LoVo, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9471. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 7.70 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0773× (z -13.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 5.37 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.66× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 5.46 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.92× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 7.87 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0706× (z -9.4) |
| [[A-172 (line)]] | wt | 5.49 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0820× (z -10.8) |
| [[A498 (line)]] | wt | 7.07 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0804× (z -14.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 7.30 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0963× (z -11.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 9.40 | 0 | 1 | — | [[Busulfan (drug)]] 0.05 µM 0.0692× (z -10.0) |
| [[HOP62 (line)]] | alt | 5.22 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -8.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 7.95 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -8.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 4.61 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -9.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 7.97 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -9.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -9.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 6.64 | 0 | 1 | — | [[Busulfan (drug)]] 5 µM 0.109× (z -8.6) |
| [[SW1417 (line)]] | alt | 6.81 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -10.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.537 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9471), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC38]] | +0.75 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[BAIAP3]] | +0.74 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[MAST3]] | +0.71 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[SLC26A6]] | +0.68 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[CAMSAP3]] | +0.68 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[CRTC1]] | +0.66 | +0.62 / +0.51 | both halves | 1e-05 | ⚠ same locus (12.0 kb, same strand: neighbours can correlate without regulation) |
| [[MPND]] | +0.65 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[EPHB3]] | +0.65 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[MIGA2]] | +0.65 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[AHDC1]] | +0.65 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[OSBPL7]] | +0.65 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[RAB3A]] | +0.64 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[PIGH]] | +0.64 | +0.42 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRPPA]] | -0.67 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[STMP1]] | -0.65 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ARSB]] | -0.63 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[AP5M1]] | -0.63 | -0.40 / -0.32 | both halves | 1e-04 |  |
| [[EPM2A]] | -0.62 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[DECR1]] | -0.60 | -0.36 / -0.29 | both halves | 2e-04 |  |
| [[VBP1]] | -0.60 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[ENOX2]] | -0.60 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[TCF12]] | -0.59 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[PSME3IP1]] | -0.58 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[CPSF2]] | -0.57 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[ATE1]] | -0.57 | -0.34 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS14]] | C | RGS14 activity lowers KLHL26's level | lines that do not express RGS14 (4) vs lines expressing it (46) | 1.45× higher at baseline in the lines without RGS14 | 0.080 | ⚠ few lines (4 vs 46); within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (10.3, -3.3); signed map (-27.0, 19.8). **Vector** length 56.9, 7.80% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.0 | +16.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +17.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.2 | +12.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.8 | +0.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | +0.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.2 | +0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.0 |
|  | [[Posaconazole (drug)]] 5 µM |  | +1.0 | +0.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.0 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -4.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,637,025-18,671,721 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53HC5](https://www.uniprot.org/uniprotkb/Q53HC5) (Kelch-like protein 26):

> May play a role in endo(sarco)plasmic reticulum (ER/SR) mitochondrial signaling. May be part of the ubiquitin-proteasome system (UPS) and affect ubiquitination and degradation of target substrates in cardiomyocytes.

**Summary**, from NCBI Gene [55295](https://www.ncbi.nlm.nih.gov/gene/55295):

> Predicted to enable ubiquitin-like ligase-substrate adaptor activity. Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process. Predicted to be part of Cul3-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25623](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25623) · Entrez [55295](https://www.ncbi.nlm.nih.gov/gene/55295) · UniProt [Q53HC5](https://www.uniprot.org/uniprotkb/Q53HC5) · Ensembl [ENSG00000167487](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167487)

## Data

Gene col 9471: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9471); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9471, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9471]; `tensor/DDL_lfc|DDL_z.npy` [9471]; `embed/gene_vectors.npy` [9471]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9471 or target_col == 9471). Every well: [[KLHL26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

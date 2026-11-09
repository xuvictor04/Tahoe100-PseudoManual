---
symbol: "PEF1"
type: "gene"
col: 8526
ensembl_id: "ENSG00000162517"
name: "penta-EF-hand domain containing 1"
location: "1p35.2"
module: 148
arm: "+"
pooled_cpm: 11.15
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# PEF1

*penta-EF-hand domain containing 1* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.78× (z +9.7, q 2e-19, up in 34 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.367× (z -16.9, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FIZ1]] (+0.81, fdr 7e-06), [[ARFGAP2]] (+0.79, fdr 7e-06), [[C19orf54]] (+0.79, fdr 7e-06); moves opposite to [[PCMT1]] (-0.68, fdr 1e-04), [[LPCAT4]] (-0.67, fdr 5e-05), [[STRN]] (-0.64, fdr 4e-04).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TRIP6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8526.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +9.7 | 2e-19 | 34/43 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +8.0 | 3e-13 | 18/36 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +6.7 | 4e-09 | 21/47 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +6.4 | 3e-08 | 23/46 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +6.3 | 3e-08 | 19/44 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +6.3 | 3e-08 | 11/23 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.5 | 3e-06 | 20/46 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +5.4 | 5e-06 | 20/46 (RKO, KATO III, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +5.1 | 2e-05 | 16/40 (KATO III, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +5.1 | 2e-05 | 17/47 (LS 180, SW48, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.1 | 0.002 | 12/48 (HOP62, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +4.0 | 0.002 | 12/28 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.5 | 0.022 | 0/48 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.039 | 7/43 (SW480, C32, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8526.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.367×** | -16.9 | 0e+00 | 45/48 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.370×** | -16.7 | 0e+00 | 42/47 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.416×** | -14.7 | 0e+00 | 44/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.635×** | -10.8 | 5e-25 | 39/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.530×** | -10.7 | 1e-24 | 38/48 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.698×** | -6.1 | 1e-07 | 20/45 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.738×** | -5.1 | 2e-05 | 18/43 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.742×** | -5.0 | 4e-05 | 20/45 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ritonavir (drug)]] 0.5 µM |  | **0.768×** | -4.4 | 5e-04 | 18/44 (Hs 766T, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.624×** | -4.1 | 0.002 | 16/47 (NCI-H23, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.785×** | -4.1 | 0.002 | 14/48 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.820×** | -3.2 | 0.062 | 14/45 (SNU-423, SW480, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.875× | -3.2 | 0.066 | 9/48 (H4, A-427, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.834× | -3.0 | 0.093 | 8/45 (A498, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8526. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 12.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -10.8) |
| [[C-33 A (line)]] | alt | 12.8 | 0 | 3 (1 ⚠) | — | [[Brimonidine (drug)]] 0.5 µM 0.0799× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 13.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 8.31 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.234× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.290× (z -8.5) |
| [[A-427 (line)]] | wt | 9.84 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.155× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~14% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.195× (z -8.5) |
| [[J82 (line)]] | alt | 11.9 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.152× (z -10.9) |
| [[LoVo (line)]] | wt | 12.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.234× (z -10.5) |
| [[LS 180 (line)]] | wt | 14.9 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.265× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 15.2 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.250× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 12.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.300× (z -8.5) |
| [[Hs 766T (line)]] | wt | 11.9 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0838× (z -12.4) |
| [[hTERT-HPNE (line)]] | wt | 8.82 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0911× (z -10.0) |
| [[KATO III (line)]] | alt | 11.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 12.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -11.3) |
| [[RKO (line)]] | wt | 10.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.174× (z -8.7) |
| [[SNU-423 (line)]] | alt | 10.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -8.5) |
| [[SW 900 (line)]] | alt | 7.32 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -9.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.169× (z -15.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8526), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FIZ1]] | +0.81 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[ARFGAP2]] | +0.79 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[C19orf54]] | +0.79 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[VPS52]] | +0.77 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[ZNF689]] | +0.76 | +0.78 / +0.45 | both halves | 3e-05 |  |
| [[UBE3B]] | +0.73 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[MTHFSD]] | +0.73 | +0.72 / +0.48 | both halves | 2e-05 |  |
| [[C8orf33]] | +0.73 | +0.76 / +0.38 | both halves | 6e-05 |  |
| [[SCAF1]] | +0.72 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[PBLD]] | +0.72 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[TMEM199]] | +0.72 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[DNAJB12]] | +0.71 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCMT1]] | -0.68 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[LPCAT4]] | -0.67 | -0.64 / -0.39 | both halves | 5e-05 |  |
| [[STRN]] | -0.64 | -0.69 / -0.26 | both halves | 4e-04 |  |
| [[FCHO1]] | -0.64 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[LPCAT2]] | -0.63 | -0.53 / -0.53 | both halves | 1e-05 | same gene group |
| [[COX6A1]] | -0.63 | -0.61 / -0.29 | both halves | 2e-04 |  |
| [[FAM102B]] | -0.62 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[MAST3]] | -0.62 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[CYTH3]] | -0.62 | -0.65 / -0.39 | both halves | 5e-05 |  |
| [[INPP5F]] | -0.62 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[METAP1]] | -0.62 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[FAM118A]] | -0.61 | -0.55 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIP6]] | B | TRIP6 activity lowers PEF1's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.14× higher at baseline in the lines without TRIP6 | 0.068 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[PBX4]] | C | PBX4 activity raises PEF1's level | lines that do not express PBX4 (3) vs lines expressing it (47) | 1.50× lower at baseline in the lines without PBX4 | 0.031 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561 |
| [[PBLD]] | C | PBLD's natural level strengthens PEF1's drug response | PBLD's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.21; direction not clear | 0.095 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.800). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-10.7, 6.8); signed map (14.8, -24.3). **Vector** length 83.2, 15.3% of its response variance represented; |z| ≥ 3 in 1,022 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +6.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.6 | +6.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.1 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +5.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +0.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -10.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.7 | -16.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.4 | -16.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.0 | -14.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.7 | -10.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -4.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.5 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | penta-EF-hand domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:31,629,866-31,644,896 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PEF1A |
| Gene groups (HGNC) | EF-hand domain containing |
| Hallmark sets | COAGULATION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBV8](https://www.uniprot.org/uniprotkb/Q9UBV8) (Peflin):

> Calcium-binding protein that acts as an adapter that bridges unrelated proteins or stabilizes weak protein-protein complexes in response to calcium. Together with PDCD6, acts as a calcium-dependent adapter for the BCR(KLHL12) complex, a complex involved in endoplasmic reticulum (ER)-Golgi transport by regulating the size of COPII coats. In response to cytosolic calcium increase, the heterodimer formed with PDCD6 interacts with, and bridges together the BCR(KLHL12) complex and SEC31 (SEC31A or …

**Summary**, from NCBI Gene [553115](https://www.ncbi.nlm.nih.gov/gene/553115):

> This gene encodes a calcium-binding protein belonging to the penta-EF-hand protein family. The encoded protein has been shown to form a heterodimer with the programmed cell death 6 gene product and may modulate its function in Ca(2+) signaling. Alternative splicing results in multiple transcript variants and a pseudogene has been identified on chromosome 1.[provided by RefSeq, May 2010]

**Accessions** — [HGNC:30009](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30009) · Entrez [553115](https://www.ncbi.nlm.nih.gov/gene/553115) · UniProt [Q9UBV8](https://www.uniprot.org/uniprotkb/Q9UBV8) · Ensembl [ENSG00000162517](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162517)

## Data

Gene col 8526: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8526); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8526, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8526]; `tensor/DDL_lfc|DDL_z.npy` [8526]; `embed/gene_vectors.npy` [8526]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8526 or target_col == 8526). Every well: [[PEF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

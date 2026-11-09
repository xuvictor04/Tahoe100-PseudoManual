---
symbol: "BPGM"
type: "gene"
col: 10240
ensembl_id: "ENSG00000172331"
name: "bisphosphoglycerate mutase"
location: "7q33"
module: 93
arm: "+"
pooled_cpm: 16.21
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# BPGM

*bisphosphoglycerate mutase* — 7q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.36× (z +10.2, q 1e-21, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.720× (z -3.9, q 0.057, down in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.105×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 0.340×); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.673×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.114×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0972×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TENT5C]] (+0.62, fdr 1e-05), [[FAM222A]] (+0.50, fdr 2e-05), [[BCL2A1]] (+0.48, fdr 9e-05); moves opposite to [[DGCR2]] (-0.50, fdr 6e-05), [[SUZ12P1]] (-0.43, fdr 9e-05), [[MRPS25]] (-0.43, fdr 2e-04).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[AGPAT4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10240.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.36×** | +10.2 | 1e-21 | 39/48 (SK-MEL-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +9.9 | 2e-20 | 29/45 (CFPAC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.22×** | +9.5 | 5e-19 | 38/48 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +8.2 | 2e-14 | 29/40 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.69×** | +8.1 | 7e-14 | 31/47 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +6.7 | 2e-09 | 27/48 (RKO, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.76×** | +6.7 | 2e-09 | 29/48 (SK-MEL-2, J82, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.79×** | +6.6 | 2e-09 | 27/47 (CFPAC-1, A549, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +6.1 | 7e-08 | 18/44 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.9 | 2e-07 | 27/46 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +4.9 | 6e-05 | 22/48 (LoVo, A-427, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +4.8 | 7e-05 | 23/48 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +4.7 | 1e-04 | 21/48 (LoVo, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +4.7 | 1e-04 | 20/47 (SW1417, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.5 | 2e-04 | 23/48 (A498, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.001 | 17/48 (LoVo, A-427, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +4.0 | 0.002 | 19/48 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10240.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.105×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 0.340×); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.673×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.114×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0972×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.720×** | -3.9 | 0.057 | 17/48 (HT-29, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Carbamazepine (drug)]] 0.5 µM |  | 0.764× | -3.2 | 0.41 | 11/47 (BT-474, CHP-212, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10240. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 20.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +12.2) | — |
| [[A498 (line)]] | wt | 39.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 16.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.8× (z +22.8) | — |
| [[NCI-H2347 (line)]] | alt | 11.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +9.8) | — |
| [[AN3 CA (line)]] | alt | 21.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0724× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0762× (z -8.7) |
| [[PANC-1 (line)]] | alt | 27.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 14.0× (z +9.4) | — |
| [[C32 (line)]] | wt | 27.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 7.56 | 0 | 1 | — | [[Dimethyl fumarate (drug)]] 0.05 µM 0.0642× (z -8.6) |
| [[HT-29 (line)]] | alt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.47× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 55.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -13.7) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +8.8) | — |
| [[RKO (line)]] | wt | 10.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0972× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 11.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.79× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 9.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +8.9) | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0651× (z -8.6) |
| [[A-172 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10240), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TENT5C]] | +0.62 | +0.57 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM; STRING 557 |
| [[FAM222A]] | +0.50 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[BCL2A1]] | +0.48 | +0.45 / +0.37 | both halves | 9e-05 |  |
| [[EHD1]] | +0.48 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[LGMN]] | +0.48 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[NFKBIZ]] | +0.47 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[TPBG]] | +0.47 | +0.47 / +0.39 | both halves | 6e-05 |  |
| [[SNAI1]] | +0.46 | +0.40 / +0.45 | both halves | 4e-05 |  |
| [[FSCN1]] | +0.46 | +0.43 / +0.43 | both halves | 4e-05 |  |
| [[PRKCG]] | +0.46 | +0.44 / +0.40 | both halves | 4e-05 |  |
| [[STARD5]] | +0.45 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[FAM107B]] | +0.45 | +0.44 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGCR2]] | -0.50 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[SUZ12P1]] | -0.43 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[MRPS25]] | -0.43 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[GTF2I]] | -0.40 | -0.38 / -0.37 | both halves | 7e-05 |  |
| [[SYMPK]] | -0.40 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[ARL17A]] | -0.39 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[SUGP2]] | -0.39 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[MLLT6]] | -0.38 | -0.32 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGPAT4]] | B | AGPAT4 activity lowers BPGM's level | lines that do not express AGPAT4 (6) vs lines expressing it (44) | 1.07× higher at baseline in the lines without AGPAT4 | 0.056 | ⚠ within organs, on part of the lines; also absent: SSBP2, ENSG00000236230, PTPN13; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.495). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.9, -7.9); signed map (2.6, 18.3). **Vector** length 82.7, 16.3% of its response variance represented; |z| ≥ 3 in 1,085 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.8 | +6.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.2 | +8.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.7 | +6.6 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +1.6 | +1.7 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | +1.6 | +2.1 |
|  | [[Uridine (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +3.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.8 | -3.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.2 | -0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -0.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +0.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.5 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.3 | -1.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | bisphosphoglycerate mutase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q33 — chr7:134,646,811-134,679,816 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phosphoglycerate mutases; Bisphosphoglycerate phosphatases |
| Hallmark sets | KRAS_SIGNALING_UP, INTERFERON_GAMMA_RESPONSE, HEME_METABOLISM |
| Reactome | 3 pathways, smallest: Glycolysis; Glucose metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P07738](https://www.uniprot.org/uniprotkb/P07738) (Bisphosphoglycerate mutase):

> Plays a major role in regulating hemoglobin oxygen affinity by controlling the levels of its allosteric effector 2,3-bisphosphoglycerate (2,3-BPG). Also exhibits mutase (EC 5.4.2.11) activity.

**Summary**, from NCBI Gene [669](https://www.ncbi.nlm.nih.gov/gene/669):

> 2,3-diphosphoglycerate (2,3-DPG) is a small molecule found at high concentrations in red blood cells where it binds to and decreases the oxygen affinity of hemoglobin. This gene encodes a multifunctional enzyme that catalyzes 2,3-DPG synthesis via its synthetase activity, and 2,3-DPG degradation via its phosphatase activity. The enzyme also has phosphoglycerate phosphomutase activity. Deficiency of this enzyme increases the affinity of cells for oxygen. Mutations in this gene result in …

**Accessions** — [HGNC:1093](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1093) · Entrez [669](https://www.ncbi.nlm.nih.gov/gene/669) · UniProt [P07738](https://www.uniprot.org/uniprotkb/P07738) · Ensembl [ENSG00000172331](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172331)

## Data

Gene col 10240: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10240); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10240, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10240]; `tensor/DDL_lfc|DDL_z.npy` [10240]; `embed/gene_vectors.npy` [10240]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10240 or target_col == 10240). Every well: [[BPGM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BPGM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

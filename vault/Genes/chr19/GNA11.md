---
symbol: "GNA11"
type: "gene"
col: 1524
ensembl_id: "ENSG00000088256"
name: "G protein subunit alpha 11"
location: "19p13.3"
module: 2
arm: "+"
pooled_cpm: 23.12
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# GNA11

*G protein subunit alpha 11* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.21× (z +13.5, q 1e-38, up in 43 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.105×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 0.169×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 0.393×; ⚠ cell-cycle shift, explains ~21% of this change).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIP5K1C]] (+0.62, fdr 1e-05), [[GNAI2]] (+0.60, fdr 3e-05), [[GAS2L1]] (+0.60, fdr 1e-05); moves opposite to [[METAP1D]] (-0.55, fdr 2e-04), [[CCDC169]] (-0.50, fdr 3e-04), [[GCFC2]] (-0.49, fdr 6e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SNTA1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1524.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.21×** | +13.5 | 1e-38 | 43/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +13.0 | 4e-36 | 35/47 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.11×** | +12.7 | 2e-34 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.01×** | +11.8 | 4e-30 | 43/48 (MIA PaCa-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.78×** | +9.8 | 1e-20 | 32/41 (C-33 A, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.65×** | +7.3 | 4e-11 | 25/36 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +5.7 | 9e-07 | 30/47 (A-172, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.34×** | +5.0 | 4e-05 | 23/48 (Hs 766T, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.31×** | +4.6 | 2e-04 | 21/44 (SW1417, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.32×** | +4.3 | 9e-04 | 17/39 (SNU-423, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.41×** | +4.0 | 0.004 | 14/44 (J82, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.010 | 8/48 (Hs 766T, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.022 | 12/48 (Hs 766T, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.022 | 10/48 (Hs 766T, HOP62, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.022 | 15/48 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[AZD-7648 (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.039 | 5/46 (LoVo, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.063 | 7/47 (Hs 766T, NCI-H2030, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.064 | 7/46 (NCI-H460, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[OTS514 (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.068 | 3/43 (A498, HCT15, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.0 | 0.080 | 14/48 (LoVo, SNU-423, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.105×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 0.169×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 0.393×; ⚠ cell-cycle shift, explains ~21% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1524. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 65.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.393× (z -9.3) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A498 (line)]] | wt | 31.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +16.6) | — |
| [[NCI-H460 (line)]] | wt | 15.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.55× (z +17.3) | [[Dinaciclib (drug)]] 5 µM 0.169× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-427 (line)]] | wt | 20.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -15.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.45× (z +14.6) | — |
| [[hTERT-HPNE (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.252× (z -8.8) ⚠ transcription drop; cell-cycle shift, explains ~34% of this change |
| [[LoVo (line)]] | wt | 22.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 22.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +10.4) | — |
| [[RKO (line)]] | wt | 23.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +13.6) | — |
| [[SHP-77 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[SW480 (line)]] | alt | 14.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.26× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1524), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIP5K1C]] | +0.62 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[GNAI2]] | +0.60 | +0.43 / +0.55 | both halves | 3e-05 | pathway: G alpha (i) signalling events; STRING 602 |
| [[GAS2L1]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[KIFC2]] | +0.59 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[ECE1]] | +0.59 | +0.40 / +0.52 | both halves | 4e-05 |  |
| [[PGAP6]] | +0.58 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[PITPNM1]] | +0.57 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[FAM89B]] | +0.56 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[SRGAP2C]] | +0.56 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[CDR2L]] | +0.54 | +0.40 / +0.53 | both halves | 4e-05 |  |
| [[ZCCHC24]] | +0.54 | +0.38 / +0.52 | both halves | 7e-05 |  |
| [[MLXIP]] | +0.54 | +0.48 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METAP1D]] | -0.55 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[CCDC169]] | -0.50 | -0.29 / -0.43 | both halves | 3e-04 |  |
| [[GCFC2]] | -0.49 | -0.22 / -0.46 | both halves | 6e-04 |  |
| [[GSTO2]] | -0.48 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[ENOSF1]] | -0.48 | -0.24 / -0.45 | both halves | 4e-04 |  |
| [[RRAGB]] | -0.46 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[AIMP1]] | -0.46 | -0.22 / -0.45 | both halves | 6e-04 |  |
| [[KICS2]] | -0.45 | -0.19 / -0.44 | ⚠ not reproduced | 8e-04 |  |
| [[NAALADL2-AS2]] | -0.45 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[YARS2]] | -0.45 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[SHLD1]] | -0.45 | -0.25 / -0.38 | both halves | 4e-04 |  |
| [[SLC16A9]] | -0.44 | -0.19 / -0.32 | ⚠ not reproduced | 8e-04 |  |
| [[SULT1C2]] | -0.44 | -0.34 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNTA1]] | B | SNTA1 activity raises GNA11's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.38× lower at baseline in the lines without SNTA1 | 0.083 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.529). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (12.1, -4.5); signed map (-26.6, 18.2). **Vector** length 69.8, 12.4% of its response variance represented; |z| ≥ 3 in 782 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +3.3 | +5.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.8 | +11.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.8 | +12.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.8 | +13.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +2.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.4 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +4.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.4 | +1.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | +0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[Hydroxyurea (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit alpha 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:3,094,362-3,123,999 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBH, FBH2, FHH2; previously HHC2 |
| Gene groups (HGNC) | G protein subunits alpha, group q |
| Reactome | 27 pathways, smallest: Fatty Acids bound to GPR40 (FFAR1) regulate insulin secretion; Acetylcholine regulates insulin secretion; Free fatty acids regulate insulin secretion |
| Matched by | ensembl_id |

**Function**, from UniProt [P29992](https://www.uniprot.org/uniprotkb/P29992) (Guanine nucleotide-binding protein subunit alpha-11):

> Guanine nucleotide-binding proteins (G proteins) function as transducers downstream of G protein-coupled receptors (GPCRs) in numerous signaling cascades. The alpha chain contains the guanine nucleotide binding site and alternates between an active, GTP-bound state and an inactive, GDP-bound state. Signaling by an activated GPCR promotes GDP release and GTP binding. The alpha subunit has a low GTPase activity that converts bound GTP to GDP, thereby terminating the signal. Both GDP release and …

**Summary**, from NCBI Gene [2767](https://www.ncbi.nlm.nih.gov/gene/2767):

> The protein encoded by this gene belongs to the family of guanine nucleotide-binding proteins (G proteins), which function as modulators or transducers in various transmembrane signaling systems. G proteins are composed of 3 units: alpha, beta and gamma. This gene encodes one of the alpha subunits (subunit alpha-11). Mutations in this gene have been associated with hypocalciuric hypercalcemia type II (HHC2) and hypocalcemia dominant 2 (HYPOC2). Patients with HHC2 and HYPOC2 exhibit decreased or …

**Accessions** — [HGNC:4379](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4379) · Entrez [2767](https://www.ncbi.nlm.nih.gov/gene/2767) · UniProt [P29992](https://www.uniprot.org/uniprotkb/P29992) · Ensembl [ENSG00000088256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088256)

## Data

Gene col 1524: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1524); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1524, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1524]; `tensor/DDL_lfc|DDL_z.npy` [1524]; `embed/gene_vectors.npy` [1524]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1524 or target_col == 1524). Every well: [[GNA11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNA11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

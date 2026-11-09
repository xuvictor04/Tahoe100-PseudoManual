---
symbol: "ZDHHC23"
type: "gene"
col: 11518
ensembl_id: "ENSG00000184307"
name: "zDHHC palmitoyltransferase 23"
location: "3q13.31"
module: 14
arm: "+"
pooled_cpm: 7.54
n_lines_expressing: 44
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# ZDHHC23

*zDHHC palmitoyltransferase 23* — 3q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.46× (z +18.7, q 0e+00, up in 24 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.708× (z -4.8, q 9e-04, down in 18 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD10]] (+0.66, fdr 1e-05), [[PAXIP1]] (+0.62, fdr 1e-05), [[SEPTIN8]] (+0.62, fdr 1e-05); moves opposite to [[PCYT1A]] (-0.54, fdr 2e-05), [[MRPL55]] (-0.53, fdr 5e-05), [[RAB2A]] (-0.53, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ISOC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11518.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.46×** | +18.7 | 0e+00 | 24/37 (HEC-1-A, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +13.3 | 5e-38 | 26/38 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +8.2 | 6e-14 | 22/40 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +7.3 | 3e-11 | 8/18 (Panc 03.27, SW480, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.61×** | +6.8 | 2e-09 | 14/34 (NCI-H2347, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.38×** | +6.6 | 3e-09 | 18/41 (COLO 205, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +6.4 | 2e-08 | 2/11 (SW480, SW1417) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +6.3 | 3e-08 | 13/40 (SW 900, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +6.2 | 4e-08 | 12/41 (A-172, PANC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.47×** | +5.6 | 1e-06 | 11/26 (LS 180, SW1417, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +5.3 | 7e-06 | 10/42 (HEC-1-A, A-427, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.42×** | +4.9 | 4e-05 | 11/38 (KATO III, SW 900, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +4.5 | 3e-04 | 9/42 (A498, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.2 | 0.001 | 1/42 (SNU-1) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.31×** | +4.0 | 0.003 | 8/40 (A498, NCI-H1573, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.018 | 11/42 (SHP-77, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.026 | 2/40 (NCI-H1573, NCI-H2347) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.0 | 0.070 | 4/41 (KATO III, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11518.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.708×** | -4.8 | 9e-04 | 18/38 (HEC-1-A, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.755×** | -4.2 | 0.009 | 13/39 (LoVo, HT-29, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.604×** | -3.9 | 0.019 | 11/35 (A549, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.791×** | -3.4 | 0.085 | 7/39 (NCI-H2030, SW 1271, …) | two highest doses | position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | 0.806× | -3.2 | 0.16 | 8/35 (SK-MEL-2, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11518. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 4.08 | 0 | 4 (1 ⚠) | — | [[Omeprazole (drug)]] 0.5 µM 0.0873× (z -10.1) |
| [[A-172 (line)]] | wt | 2.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +10.3) | — |
| [[A498 (line)]] | wt | 2.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 5.47 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0730× (z -9.2) |
| [[C-33 A (line)]] | alt | 22.2 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.120× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 18.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 6.85 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0464× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 12.8 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 5 µM 0.0463× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 5.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 14.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +8.9) | — |
| [[SW48 (line)]] | wt | 13.8 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.101× (z -8.7) |
| [[A-427 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.976 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.986 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11518), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD10]] | +0.66 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[PAXIP1]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[SEPTIN8]] | +0.62 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ISOC1]] | +0.60 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[FOXP4-AS1]] | +0.59 | +0.61 / +0.49 | both halves | 2e-05 |  |
| [[TIFA]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[NCR3LG1]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[CD83]] | +0.57 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[ABCG2]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[SEPTIN11]] | +0.55 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[OTUD4]] | +0.55 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[GATM]] | +0.54 | +0.41 / +0.62 | both halves | 4e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCYT1A]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[MRPL55]] | -0.53 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[RAB2A]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[KCTD21]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[POLR2J4]] | -0.50 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[VRK3]] | -0.50 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[TMEM208]] | -0.49 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[MED31]] | -0.49 | -0.52 / -0.40 | both halves | 4e-05 |  |
| [[MEF2B]] | -0.49 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[PPIL2]] | -0.48 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[PSMB1]] | -0.48 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[DRD4]] | -0.48 | -0.49 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises ZDHHC23's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ISOC1]] | B | ZDHHC23 activity raises ISOC1's level | lines that do not express ZDHHC23 (6) vs lines expressing it (44) | 1.85× lower at baseline in the lines without ZDHHC23 | 0.0998 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.545). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.9, 6.0); signed map (23.1, -34.5). **Vector** length 63.9, 10.2% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.2 | +8.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +2.9 | +6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +18.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +13.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +2.1 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +6.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.3 | +0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.2 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +3.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -3.5 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -1.6 | +4.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.31 — chr3:113,947,901-113,965,401 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC42530 |
| Gene groups (HGNC) | Zinc fingers DHHC-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYP9](https://www.uniprot.org/uniprotkb/Q8IYP9) (Palmitoyltransferase ZDHHC23):

> Palmitoyltransferase that could catalyze the addition of palmitate onto various protein substrates and be involved in a variety of cellular processes (Probable). Palmitoyltransferase that mediates palmitoylation of KCNMA1, regulating localization of KCNMA1 to the plasma membrane. May be involved in NOS1 regulation and targeting to the synaptic membrane.

**Summary**, from NCBI Gene [254887](https://www.ncbi.nlm.nih.gov/gene/254887):

> Predicted to enable protein-cysteine S-palmitoyltransferase activity. Involved in protein localization to plasma membrane and protein palmitoylation. Predicted to be located in Golgi membrane. Predicted to be active in Golgi apparatus and endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28654](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28654) · Entrez [254887](https://www.ncbi.nlm.nih.gov/gene/254887) · UniProt [Q8IYP9](https://www.uniprot.org/uniprotkb/Q8IYP9) · Ensembl [ENSG00000184307](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184307)

## Data

Gene col 11518: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11518); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11518, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11518]; `tensor/DDL_lfc|DDL_z.npy` [11518]; `embed/gene_vectors.npy` [11518]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11518 or target_col == 11518). Every well: [[ZDHHC23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "CKB"
type: "gene"
col: 9249
ensembl_id: "ENSG00000166165"
name: "creatine kinase B"
location: "14q32.33"
module: 123
arm: "+"
pooled_cpm: 17.34
n_lines_expressing: 39
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# CKB

*creatine kinase B* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.10× (z +9.8, q 6e-20, up in 30 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.527× (z -4.9, q 5e-04, down in 20 of 35 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 0.613× (z -4.3, q 0.006, down in 18 of 36 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPPP]] (+0.59, fdr 1e-05), [[USP2]] (+0.57, fdr 1e-04), [[SYNGR2]] (+0.57, fdr 2e-05); moves opposite to [[EPM2A]] (-0.54, fdr 2e-04), [[AIFM2]] (-0.52, fdr 4e-05), [[HSPA4]] (-0.51, fdr 1e-04).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[CFD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9249.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.10×** | +9.8 | 6e-20 | 30/36 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.73×** | +8.7 | 7e-16 | 22/27 (HT-29, SW480, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.70×** | +8.6 | 1e-15 | 28/36 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.79×** | +8.2 | 3e-14 | 19/25 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.62×** | +7.4 | 1e-11 | 15/23 (LoVo, SW480, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.93×** | +5.7 | 1e-06 | 25/36 (NCI-H2030, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +5.6 | 2e-06 | 19/32 (SW 900, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.46×** | +4.6 | 3e-04 | 16/35 (PANC-1, J82, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.67×** | +4.4 | 6e-04 | 18/35 (PANC-1, A-172, …) | two highest doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **1.63×** | +4.2 | 0.001 | 18/33 (NCI-H2030, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.005 | 16/35 (NCI-H2030, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.87×** | +3.9 | 0.005 | 17/31 (J82, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +3.7 | 0.009 | 16/36 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.61×** | +3.7 | 0.010 | 17/35 (PANC-1, J82, …) | two highest doses | composition shift; position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.014 | 14/37 (NCI-H460, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.021 | 15/37 (NCI-H2030, J82, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.74×** | +3.4 | 0.021 | 14/35 (LoVo, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.046 | 11/36 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9249.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.527×** | -4.9 | 5e-04 | 20/35 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.613×** | -4.3 | 0.006 | 18/36 (CHP-212, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.588×** | -4.1 | 0.008 | 18/34 (NCI-H2347, SK-MEL-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.650×** | -3.8 | 0.023 | 18/36 (HOP62, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.685× | -3.3 | 0.11 | 11/36 (AN3 CA, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9249. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 65.2 | 3 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.24× (z +10.6) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[SW480 (line)]] | alt | 10.5 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.86× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.15× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 11.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.73× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 14.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 9.95× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 20.2 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -11.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HT-29 (line)]] | alt | 38.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[J82 (line)]] | alt | 21.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 17.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.08× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[LS 180 (line)]] | wt | 38.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H1573 (line)]] | alt | 6.57 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 38.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +8.8) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H460 (line)]] | wt | 24.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.52× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9249), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPPP]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[USP2]] | +0.57 | +0.36 / +0.55 | both halves | 1e-04 |  |
| [[SYNGR2]] | +0.57 | +0.50 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_MYOGENESIS |
| [[TUBB2B]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[PNPLA2]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[CXADR]] | +0.54 | +0.34 / +0.44 | both halves | 1e-04 |  |
| [[CGN]] | +0.54 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[RHOB]] | +0.53 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[LMNA]] | +0.53 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[KLF2]] | +0.53 | +0.34 / +0.50 | both halves | 1e-04 |  |
| [[CRIP1]] | +0.52 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[NUDT14]] | +0.52 | +0.39 / +0.43 | both halves | 5e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPM2A]] | -0.54 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[AIFM2]] | -0.52 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[HSPA4]] | -0.51 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[MKRN5P]] | -0.51 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[NPAS2]] | -0.48 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[TMEM11-DT]] | -0.48 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[GLUD1P3]] | -0.48 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[NHSL1]] | -0.48 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[ZFYVE9]] | -0.47 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[CCT6A]] | -0.47 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[EXOSC3]] | -0.47 | -0.38 / -0.24 | both halves | 5e-04 |  |
| [[ANGEL2]] | -0.47 | -0.42 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFD]] | B | CKB activity raises CFD's level | lines that do not express CKB (11) vs lines expressing it (39) | 2.01× lower at baseline in the lines without CKB | 0.068 | ⚠ within organs, on part of the lines; also absent: BACH2, MAOA; maybe low, not absent |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.598). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-7.0, 32.6); signed map (-0.9, 21.5). **Vector** length 70.8, 16.0% of its response variance represented; |z| ≥ 3 in 700 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.5 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +3.1 | +3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | +9.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.4 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +2.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.5 | -4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | creatine kinase B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:103,519,667-103,522,833 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CKBB |
| Gene groups (HGNC) | Creatine kinase family |
| Hallmark sets | MYOGENESIS, ESTROGEN_RESPONSE_LATE |
| Reactome | 6 pathways, smallest: Creatine metabolism; RND3 GTPase cycle; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P12277](https://www.uniprot.org/uniprotkb/P12277) (Creatine kinase B-type):

> Reversibly catalyzes the transfer of phosphate between ATP and various phosphogens (e.g. creatine phosphate). Creatine kinase isoenzymes play a central role in energy transduction in tissues with large, fluctuating energy demands, such as skeletal muscle, heart, brain and spermatozoa (Probable). Acts as a key regulator of adaptive thermogenesis as part of the futile creatine cycle: localizes to the mitochondria of thermogenic fat cells and acts by mediating phosphorylation of creatine to …

**Summary**, from NCBI Gene [1152](https://www.ncbi.nlm.nih.gov/gene/1152):

> The protein encoded by this gene is a cytoplasmic enzyme involved in energy homeostasis. The encoded protein reversibly catalyzes the transfer of phosphate between ATP and various phosphogens such as creatine phosphate. It acts as a homodimer in brain as well as in other tissues, and as a heterodimer with a similar muscle isozyme in heart. The encoded protein is a member of the ATP:guanido phosphotransferase protein family. A pseudogene of this gene has been characterized. [provided by RefSeq, …

**Accessions** — [HGNC:1991](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1991) · Entrez [1152](https://www.ncbi.nlm.nih.gov/gene/1152) · UniProt [P12277](https://www.uniprot.org/uniprotkb/P12277) · Ensembl [ENSG00000166165](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166165)

## Data

Gene col 9249: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9249); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9249, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9249]; `tensor/DDL_lfc|DDL_z.npy` [9249]; `embed/gene_vectors.npy` [9249]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9249 or target_col == 9249). Every well: [[CKB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CKB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

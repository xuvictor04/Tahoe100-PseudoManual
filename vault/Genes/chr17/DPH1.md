---
symbol: "DPH1"
type: "gene"
col: 3015
ensembl_id: "ENSG00000108963"
name: "diphthamide biosynthesis 1"
location: "17p13.3"
module: 11
arm: "+"
pooled_cpm: 14.65
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# DPH1

*diphthamide biosynthesis 1* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.65× (z +7.3, q 1e-10, up in 29 of 42 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.39× (z +4.9, q 2e-04, up in 19 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.698× (z -5.4, q 3e-05, down in 21 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.801× (z -4.7, q 4e-04, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF579]] (+0.69, fdr 7e-06), [[SNHG11]] (+0.67, fdr 7e-06), [[ZNF282]] (+0.66, fdr 1e-05); moves opposite to [[TPM3]] (-0.59, fdr 1e-05), [[DIAPH1]] (-0.57, fdr 1e-05), [[PDIA6]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KDF1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3015.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +7.3 | 1e-10 | 29/42 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +6.1 | 3e-07 | 23/44 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +4.9 | 2e-04 | 19/46 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.61×** | +4.6 | 7e-04 | 16/45 (SW 900, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.22×** | +4.3 | 0.002 | 22/47 (A-172, A-427, …) | rises with dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +4.1 | 0.005 | 12/44 (NCI-H1573, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.52×** | +4.0 | 0.005 | 7/45 (LOX-IMVI, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.029 | 15/47 (LoVo, J82, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.037 | 6/45 (HEC-1-A, LS 180, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.037 | 4/45 (A549, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[DTP3 (drug)]] 5 µM |  | **1.63×** | +3.4 | 0.039 | 5/43 (LOX-IMVI, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.62×** | +3.3 | 0.039 | 7/45 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.24×** | +3.3 | 0.043 | 12/46 (A-172, A498, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.047 | 7/47 (SHP-77, PANC-1, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.070 | 8/45 (NCI-H460, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.070 | 8/46 (hTERT-HPNE, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3015.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.698×** | -5.4 | 3e-05 | 21/47 (KATO III, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.705×** | -5.3 | 4e-05 | 19/47 (SW 1271, SW48, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.801×** | -4.7 | 4e-04 | 23/48 (HCT15, SNU-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.736×** | -4.6 | 5e-04 | 17/47 (SW480, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.746×** | -4.4 | 0.001 | 17/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.538×** | -4.3 | 0.002 | 13/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.773×** | -3.9 | 0.008 | 12/48 (A498, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Hexylresorcinol (drug)]] 0.5 µM |  | **0.774×** | -3.9 | 0.008 | 8/48 (Hs 766T, PANC-1, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.781×** | -3.7 | 0.012 | 13/48 (HepG2/C3A, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.784×** | -3.7 | 0.014 | 11/47 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (drug)]] 5 µM |  | 0.851× | -3.4 | 0.030 | 9/48 (Hs 766T, LOX-IMVI, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **0.800×** | -3.4 | 0.036 | 14/46 (NCI-H1792, RKO, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3015. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 13.0 | 0 | 2 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0848× (z -9.8) ⚠ unreliable plate only · without an alert: [[Pyridoxine (drug)]] 0.5 µM 0.114× (z -8.6) |
| [[A549 (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.121× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 14.7 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.233× (z -9.1) |
| [[SW480 (line)]] | alt | 22.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.357× (z -9.5) |
| [[A-172 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3015), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF579]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[SNHG11]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ZNF282]] | +0.66 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[MRPL38]] | +0.65 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[NOL8]] | +0.65 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[DDX28]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[INTS14]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ZNF317]] | +0.63 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[RPP25L]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[RRN3]] | +0.62 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[ZNF691]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[RPP38]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPM3]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[DIAPH1]] | -0.57 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[PDIA6]] | -0.57 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[C12orf75]] | -0.54 | -0.56 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KDF1]] | B | KDF1 activity lowers DPH1's level | lines that do not express KDF1 (30) vs lines expressing it (20) | 1.22× higher at baseline in the lines without KDF1 | 0.013 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.8, 7.8); signed map (-2.5, -23.2). **Vector** length 70.9, 13.0% of its response variance represented; |z| ≥ 3 in 612 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.2 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +4.1 | +4.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.8 | +4.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.5 | +4.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.5 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.2 | +1.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.1 | +3.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.3 | -3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -4.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -4.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -2.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | diphthamide biosynthesis 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:2,030,137-2,043,898 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OVCA1; previously DPH2L, DPH2L1 |
| Gene groups (HGNC) | Minor histocompatibility antigens; Diphthamide biosynthesis genes |
| Reactome | 2 pathways, smallest: Synthesis of diphthamide-EEF2; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZG8](https://www.uniprot.org/uniprotkb/Q9BZG8) (2-(3-amino-3-carboxypropyl)histidine synthase subunit 1):

> Catalyzes the first step of diphthamide biosynthesis, a post-translational modification of histidine which occurs in elongation factor 2. DPH1 and DPH2 transfer a 3-amino-3-carboxypropyl (ACP) group from S-adenosyl-L-methionine (SAM) to a histidine residue, the reaction is assisted by a reduction system comprising DPH3 and a NADH-dependent reductase (By similarity). Acts as a tumor suppressor.

**Summary**, from NCBI Gene [1801](https://www.ncbi.nlm.nih.gov/gene/1801):

> The protein encoded by this gene is an enzyme involved in the biosynthesis of diphthamide, a modified histidine found only in elongation factor-2 (EEF2). Diphthamide residues in EEF2 are targeted for ADP-ribosylation by diphtheria toxin and Pseudomonas exotoxin A. Defects in this gene have been associated with both ovarian cancer and autosomal recessive intellectual disability with short stature, craniofacial, and ectodermal anomalies. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:3003](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3003) · Entrez [1801](https://www.ncbi.nlm.nih.gov/gene/1801) · UniProt [Q9BZG8](https://www.uniprot.org/uniprotkb/Q9BZG8) · Ensembl [ENSG00000108963](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108963)

## Data

Gene col 3015: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3015); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3015, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3015]; `tensor/DDL_lfc|DDL_z.npy` [3015]; `embed/gene_vectors.npy` [3015]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3015 or target_col == 3015). Every well: [[DPH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

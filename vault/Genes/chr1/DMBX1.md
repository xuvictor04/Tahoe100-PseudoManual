---
symbol: "DMBX1"
type: "gene"
col: 12427
ensembl_id: "ENSG00000197587"
name: "diencephalon/mesencephalon homeobox 1"
location: "1p33"
module: 124
arm: "-"
pooled_cpm: 2.97
n_lines_expressing: 39
n_dd_up: 18
n_dd_down: 17
n_dd_up_clean: 12
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# DMBX1

*diencephalon/mesencephalon homeobox 1* — 1p33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 4.24× (z +14.8, q 0e+00, up in 31 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.506× (z -6.9, q 2e-09, down in 19 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HAUS4]] (+0.57, fdr 2e-05), [[STIL]] (+0.56, fdr 4e-05), [[TLCD3B]] (+0.56, fdr 2e-05); moves opposite to [[ITPA]] (-0.62, fdr 5e-05), [[DPH5-DT]] (-0.56, fdr 5e-05), [[GATC]] (-0.55, fdr 3e-05).
> It sits in the **-** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SBK1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZYG11A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12427.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **4.24×** | +14.8 | 0e+00 | 31/34 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.46×** | +12.7 | 3e-34 | 30/35 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.48×** | +9.3 | 3e-18 | 24/35 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.53×** | +9.1 | 1e-17 | 0/3 | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.75×** | +8.1 | 5e-14 | 16/35 (J82, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.90×** | +6.6 | 5e-09 | 17/35 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.4 | 2e-08 | 14/26 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **1.49×** | +4.1 | 0.003 | 3/14 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.65×** | +3.7 | 0.016 | 2/15 (CFPAC-1, A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.033 | 6/25 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.89×** | +3.4 | 0.035 | 2/32 (PANC-1, SW480) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.05 µM |  | **1.39×** | +3.4 | 0.038 | 0/35 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.41×** | +3.3 | 0.042 | 0/4 | all doses, stronger at high dose | composition shift |
| [[Apalutamide (drug)]] 0.05 µM |  | **1.41×** | +3.3 | 0.042 | 1/26 (NCI-H460) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.042 | 6/33 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12427.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.506×** | -6.9 | 2e-09 | 19/32 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.525×** | -6.6 | 2e-08 | 13/35 (C32, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.564×** | -5.8 | 1e-06 | 12/23 (A-172, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.602×** | -5.2 | 4e-05 | 14/32 (A-172, A549, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.610×** | -5.0 | 6e-05 | 11/35 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.708×** | -5.0 | 7e-05 | 9/34 (A498, NCI-H2030, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.621×** | -4.8 | 1e-04 | 17/34 (A549, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.409×** | -4.8 | 1e-04 | 8/31 (A498, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.724×** | -4.6 | 2e-04 | 10/34 (A-172, NCI-H460, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.658×** | -4.3 | 0.001 | 10/35 (SW 900, HCT15, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.679×** | -3.9 | 0.004 | 10/33 (A-172, PANC-1, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.688×** | -3.8 | 0.007 | 14/31 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.693×** | -3.7 | 0.008 | 4/33 (KATO III, HEC-1-A, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.774×** | -3.7 | 0.010 | 11/35 (C32, HT-29, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.544×** | -3.2 | 0.045 | 7/23 (LoVo, A498, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.739×** | -3.1 | 0.070 | 8/31 (HCT15, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12427. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.37 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0581× (z -10.2) |
| [[A498 (line)]] | wt | 5.85 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0676× (z -12.3) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.196× (z -10.9) |
| [[A-427 (line)]] | wt | 9.26 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0866× (z -11.3) |
| [[A549 (line)]] | wt | 2.10 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0319× (z -8.8) |
| [[SW 1271 (line)]] | alt | 1.90 | 1 | 0 | [[Vemurafenib (drug)]] 0.5 µM 2.34× (z +42.5) | — |
| [[SW480 (line)]] | alt | 2.47 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0906× (z -9.2) |
| [[AN3 CA (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.337 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.487 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.293 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.289 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.291 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.783 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.793 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.904 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.209 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12427), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAUS4]] | +0.57 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[STIL]] | +0.56 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[TLCD3B]] | +0.56 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[RIMS3]] | +0.56 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[CHTF18]] | +0.56 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[NRTN]] | +0.55 | +0.32 / +0.56 | both halves | 2e-04 |  |
| [[DUSP9]] | +0.55 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[PRADC1]] | +0.55 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[FGFR3]] | +0.54 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[IDH2]] | +0.54 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[CEP131]] | +0.54 | +0.45 / +0.38 | both halves | 6e-05 |  |
| [[C1QL1]] | +0.54 | +0.45 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITPA]] | -0.62 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[DPH5-DT]] | -0.56 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[GATC]] | -0.55 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[RAB30-DT]] | -0.55 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[ENOX2]] | -0.54 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[CLHC1]] | -0.53 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[MTHFSD]] | -0.53 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[HDHD2]] | -0.52 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[LTO1]] | -0.51 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[GPATCH2]] | -0.50 | -0.41 / -0.29 | both halves | 3e-04 |  |
| [[DNAJC11]] | -0.50 | -0.37 / -0.43 | both halves | 7e-05 |  |
| [[ZNF91]] | -0.50 | -0.33 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SBK1]] | B | SBK1 activity raises DMBX1's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 1.99× lower at baseline in the lines without SBK1 | 0.067 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZYG11A]] | B | DMBX1 activity raises ZYG11A's level | lines that do not express DMBX1 (11) vs lines expressing it (39) | 2.96× lower at baseline in the lines without DMBX1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ERICH2, NTN1, KCNIP3 |

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **-** arm (projection on the module's main direction -0.511). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-26.3, -50.7); signed map (-44.9, -31.8). **Vector** length 53.9, 8.80% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +2.9 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | +2.5 | +4.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.5 | +12.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +3.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | -0.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -5.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -5.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.9 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -5.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | diencephalon/mesencephalon homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p33 — chr1:46,489,836-46,516,216 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAXB, MBX, Atx; previously OTX3 |
| Gene groups (HGNC) | PRD class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFW5](https://www.uniprot.org/uniprotkb/Q8NFW5) (Diencephalon/mesencephalon homeobox protein 1):

> Functions as a transcriptional repressor. May repress OTX2-mediated transactivation by forming a heterodimer with OTX2 on the P3C (5'-TAATCCGATTA-3') sequence. Required for brain development (By similarity).

**Summary**, from NCBI Gene [127343](https://www.ncbi.nlm.nih.gov/gene/127343):

> This gene encodes a member of the bicoid sub-family of homeodomain-containing transcription factors. The encoded protein acts as a transcription factor and may play a role in brain and sensory organ development. Two transcript variants encoding distinct isoforms have been identified for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19026](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19026) · Entrez [127343](https://www.ncbi.nlm.nih.gov/gene/127343) · UniProt [Q8NFW5](https://www.uniprot.org/uniprotkb/Q8NFW5) · Ensembl [ENSG00000197587](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197587)

## Data

Gene col 12427: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12427); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12427, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12427]; `tensor/DDL_lfc|DDL_z.npy` [12427]; `embed/gene_vectors.npy` [12427]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12427 or target_col == 12427). Every well: [[DMBX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DMBX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

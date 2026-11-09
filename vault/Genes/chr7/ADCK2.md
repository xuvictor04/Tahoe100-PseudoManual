---
symbol: "ADCK2"
type: "gene"
col: 5454
ensembl_id: "ENSG00000133597"
name: "aarF domain containing kinase 2"
location: "7q34"
module: 30
arm: "+"
pooled_cpm: 4.21
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# ADCK2

*aarF domain containing kinase 2* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.92× (z +7.8, q 4e-12, up in 2 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.42× (z +6.1, q 2e-07, up in 10 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.405× (z -11.2, q 4e-26, down in 32 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POMGNT2]] (+0.60, fdr 1e-05), [[OTX1]] (+0.59, fdr 2e-05), [[XKR8]] (+0.59, fdr 3e-05); moves opposite to [[RFX3]] (-0.53, fdr 4e-05), [[SECISBP2]] (-0.53, fdr 3e-05), [[SLIT2]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GNAZ]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5454.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +7.8 | 4e-12 | 2/7 (PANC-1, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +6.1 | 2e-07 | 10/46 (A498, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +5.2 | 5e-05 | 6/23 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +4.3 | 0.002 | 3/8 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.2 | 0.003 | 6/36 (NCI-H2030, HEC-1-A, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.8 | 0.012 | 5/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.53×** | +3.8 | 0.012 | 1/35 (KATO III) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.012 | 6/45 (LS 180, NCI-H23, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.021 | 5/26 (LoVo, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +3.4 | 0.035 | 5/26 (HT-29, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.063 | 8/38 (HT-29, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.097 | 5/43 (NCI-H1792, LoVo, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.097 | 2/30 (NCI-H460, LS 180) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.098 | 5/31 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.099 | 8/31 (A498, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5454.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.405×** | -11.2 | 4e-26 | 32/44 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.407×** | -11.1 | 4e-26 | 33/47 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.545×** | -10.6 | 7e-24 | 25/38 (A498, SNU-423, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.462×** | -9.5 | 3e-19 | 22/33 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.489×** | -8.5 | 3e-15 | 26/43 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.506×** | -8.4 | 4e-15 | 25/44 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.567×** | -7.0 | 2e-10 | 18/36 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.459×** | -5.0 | 4e-05 | 12/41 (RKO, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.687×** | -4.6 | 2e-04 | 13/44 (SNU-423, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.701×** | -4.4 | 7e-04 | 14/47 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.748×** | -3.6 | 0.019 | 10/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.581×** | -3.5 | 0.022 | 9/33 (HEC-1-A, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.763×** | -3.3 | 0.038 | 13/43 (LoVo, NCI-H1573, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5454. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 9.72 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -10.8) |
| [[A-172 (line)]] | wt | 6.29 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 3.37 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0385× (z -11.2) |
| [[C32 (line)]] | wt | 8.49 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0753× (z -10.7) ⚠ cell-cycle shift, explains ~1% of this change |
| [[LS 180 (line)]] | wt | 2.87 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.05 µM 0.0607× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 7.40 | 0 | 1 | — | [[Pasireotide (acetate) (drug)]] 5 µM 0.235× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 3.34 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0630× (z -11.7) |
| [[SNU-423 (line)]] | alt | 3.78 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -8.8) |
| [[A-427 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5454), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POMGNT2]] | +0.60 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[OTX1]] | +0.59 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[XKR8]] | +0.59 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[SLC15A4]] | +0.58 | +0.32 / +0.64 | both halves | 2e-04 |  |
| [[MKRN2]] | +0.58 | +0.32 / +0.60 | both halves | 2e-04 |  |
| [[TADA1]] | +0.57 | +0.38 / +0.47 | both halves | 7e-05 |  |
| [[SEMA4F]] | +0.56 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[IMPDH1]] | +0.56 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[TMEM185A]] | +0.55 | +0.38 / +0.43 | both halves | 6e-05 |  |
| [[GNPTAB]] | +0.55 | +0.30 / +0.47 | both halves | 2e-04 |  |
| [[EXD2]] | +0.54 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[ZNF74]] | +0.54 | +0.45 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFX3]] | -0.53 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[SECISBP2]] | -0.53 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[SLIT2]] | -0.50 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[LINC00641]] | -0.50 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[BAZ2B]] | -0.48 | -0.33 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAZ]] | B | GNAZ activity raises ADCK2's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.47× lower at baseline in the lines without GNAZ | 0.031 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[ULK2]] | B | ULK2 activity raises ADCK2's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 1.11× lower at baseline in the lines without ULK2 | 0.054 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[SNTA1]] | B | SNTA1 activity raises ADCK2's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.16× lower at baseline in the lines without SNTA1 | 0.064 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[BOLA3-DT]] | B | BOLA3-DT activity raises ADCK2's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 1.23× lower at baseline in the lines without BOLA3-DT | 0.089 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.617). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-0.3, -4.4); signed map (-35.8, -4.0). **Vector** length 43.6, 4.73% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.0 | +6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +1.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +1.7 | +3.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.5 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.4 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -11.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -11.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -8.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -0.9 | -2.8 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.8 | -2.0 |
|  | [[Pimozide (drug)]] 5 µM |  | -0.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | aarF domain containing kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:140,672,945-140,696,261 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC20727 |
| Gene groups (HGNC) | ADCK family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z695](https://www.uniprot.org/uniprotkb/Q7Z695) (Uncharacterized aarF domain-containing protein kinase 2):

> The function of this protein is not yet clear. It is not known if it has protein kinase activity and what type of substrate it would phosphorylate (Ser, Thr or Tyr) (Probable). Involved in the mitochondrial import of CoQ precursors, plays a role in muscle mitochondrial function and fatty acid beta-oxidation.

**Summary**, from NCBI Gene [90956](https://www.ncbi.nlm.nih.gov/gene/90956):

> Predicted to enable ATP binding activity and protein serine/threonine kinase activity. Involved in regulation of ubiquinone biosynthetic process. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19039](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19039) · Entrez [90956](https://www.ncbi.nlm.nih.gov/gene/90956) · UniProt [Q7Z695](https://www.uniprot.org/uniprotkb/Q7Z695) · Ensembl [ENSG00000133597](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133597)

## Data

Gene col 5454: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5454); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5454, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5454]; `tensor/DDL_lfc|DDL_z.npy` [5454]; `embed/gene_vectors.npy` [5454]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5454 or target_col == 5454). Every well: [[ADCK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADCK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

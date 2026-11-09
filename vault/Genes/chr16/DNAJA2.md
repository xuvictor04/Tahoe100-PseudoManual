---
symbol: "DNAJA2"
type: "gene"
col: 915
ensembl_id: "ENSG00000069345"
name: "DnaJ heat shock protein family (Hsp40) member A2"
location: "16q11.2"
module: 7
arm: "+"
pooled_cpm: 52.9
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# DNAJA2

*DnaJ heat shock protein family (Hsp40) member A2* — 16q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.08× (z +11.0, q 2e-25, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Rapamycin (drug)]] 5 µM: 0.860× (z -4.0, q 0.030, down in 14 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.220×, NCI-H460 0.416×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.472×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.373×; ⚠ toxic; cell-cycle shift, explains ~11% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL9]] (+0.67, fdr 7e-06), [[SMIM15]] (+0.66, fdr 7e-06), [[PUF60]] (+0.64, fdr 7e-06); moves opposite to [[GNRH1]] (-0.56, fdr 1e-05), [[PPP1R14B]] (-0.51, fdr 3e-05), [[STK32C]] (-0.49, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF518B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 915.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.08×** | +11.0 | 2e-25 | 44/49 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +10.2 | 8e-22 | 40/48 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +10.0 | 3e-21 | 37/48 (SW1417, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.67×** | +9.2 | 4e-18 | 42/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +7.7 | 2e-12 | 39/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +7.3 | 2e-11 | 36/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +7.1 | 1e-10 | 39/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +6.5 | 5e-09 | 34/48 (NCI-H2030, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +6.4 | 1e-08 | 35/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +5.9 | 2e-07 | 28/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.81×** | +5.8 | 3e-07 | 32/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +5.7 | 6e-07 | 31/48 (SW480, NCI-H460, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +5.6 | 1e-06 | 22/48 (PANC-1, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.31×** | +5.1 | 1e-05 | 27/46 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.30×** | +5.0 | 2e-05 | 25/48 (HOP62, NCI-H1792, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +4.8 | 7e-05 | 31/48 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.003 | 18/48 (NCI-H1573, SNU-423, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.5 | 0.015 | 15/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 915.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.220×, NCI-H460 0.416×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.472×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.373×; ⚠ toxic; cell-cycle shift, explains ~11% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rapamycin (drug)]] 5 µM |  | 0.860× | -4.0 | 0.030 | 14/48 (A-427, AsPC-1, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.751×** | -3.8 | 0.030 | 21/47 (COLO 205, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.819×** | -3.7 | 0.030 | 19/48 (HEC-1-A, AsPC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -3.7 | 0.030 | 1/49 (SW 1088) | inconsistent across doses |  |
| [[Sacubitril_Valsartan (drug)]] 5 µM |  | 0.837× | -3.2 | 0.16 | 15/48 (A-172, LoVo, …) | top dose only | position effect removed |
| [[Baicalin (drug)]] 5 µM |  | 0.887× | -3.1 | 0.16 | 6/48 (Panc 03.27, LOX-IMVI, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 915. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 70.8 | 6 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.48× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 46.0 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 54.1 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 1.98× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[A-427 (line)]] | wt | 49.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.01× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -11.2) |
| [[A549 (line)]] | wt | 50.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +12.1) | — |
| [[HEC-1-A (line)]] | alt | 43.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 56.4 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[NCI-H1573 (line)]] | alt | 46.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.29× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 65.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.8) | — |
| [[A-172 (line)]] | wt | 48.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 78.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.204× (z -9.0) ⚠ toxic |
| [[C32 (line)]] | wt | 40.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +8.8) | — |
| [[KATO III (line)]] | alt | 59.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.3) | — |
| [[LoVo (line)]] | wt | 53.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 79.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.38× (z +9.4) | — |
| [[RKO (line)]] | wt | 74.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.373× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~11% of this change |
| [[A498 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 86.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 90.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 915), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL9]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[SMIM15]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[PUF60]] | +0.64 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[PRELID3B]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ZNF845]] | +0.61 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[ZNF518B]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[C7orf25]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[C17orf80]] | +0.59 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[UBE2Q1]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ACTR8]] | +0.58 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[VCPIP1]] | +0.58 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[ZNF816]] | +0.58 | +0.53 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNRH1]] | -0.56 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[PPP1R14B]] | -0.51 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[STK32C]] | -0.49 | -0.50 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF518B]] | B | ZNF518B activity lowers DNAJA2's level | lines that do not express ZNF518B (16) vs lines expressing it (34) | 1.32× higher at baseline in the lines without ZNF518B | 0.034 | ⚠ within organs, on part of the lines; also absent: EHD3, KCNG1, TUB |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.547). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-32.1, 14.0); signed map (2.6, -31.4). **Vector** length 84.9, 19.4% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.7 | +5.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | +4.5 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +7.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.7 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Erlotinib (drug)]] 5 µM |  | +2.7 | +2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | -0.1 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -3.9 | -3.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -2.6 | +4.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.3 | -2.3 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -2.3 | -1.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.3 | -1.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q11.2 — chr16:46,955,362-46,973,674 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HIRIP4, DNAJ, CPR3, DNJ3 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Reactome | 6 pathways, smallest: HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; Dengue Virus Genome Translation and Replication; Dengue Virus Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [O60884](https://www.uniprot.org/uniprotkb/O60884) (DnaJ homolog subfamily A member 2):

> Co-chaperone of Hsc70. Stimulates ATP hydrolysis and the folding of unfolded proteins mediated by HSPA1A/B (in vitro).

**Summary**, from NCBI Gene [10294](https://www.ncbi.nlm.nih.gov/gene/10294):

> The protein encoded by this gene belongs to the evolutionarily conserved DNAJ/HSP40 family of proteins, which regulate molecular chaperone activity by stimulating ATPase activity. DNAJ proteins may have up to 3 distinct domains: a conserved 70-amino acid J domain, usually at the N terminus; a glycine/phenylalanine (G/F)-rich region; and a cysteine-rich domain containing 4 motifs resembling a zinc finger domain. The product of this gene works as a cochaperone of Hsp70s in protein folding and …

**Accessions** — [HGNC:14884](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14884) · Entrez [10294](https://www.ncbi.nlm.nih.gov/gene/10294) · UniProt [O60884](https://www.uniprot.org/uniprotkb/O60884) · Ensembl [ENSG00000069345](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069345)

## Data

Gene col 915: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 915); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 915, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 915]; `tensor/DDL_lfc|DDL_z.npy` [915]; `embed/gene_vectors.npy` [915]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 915 or target_col == 915). Every well: [[DNAJA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "ARL3"
type: "gene"
col: 6138
ensembl_id: "ENSG00000138175"
name: "ARF like GTPase 3"
location: "10q24.32"
module: 1
arm: "-"
pooled_cpm: 35.66
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ARL3

*ARF like GTPase 3* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.82× (z +10.7, q 1e-23, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.729× (z -4.6, q 0.003, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GMCL1]] (+0.77, fdr 7e-06), [[PJA2]] (+0.77, fdr 1e-05), [[PLEKHH3]] (+0.76, fdr 7e-06); moves opposite to [[UTP20]] (-0.74, fdr 7e-06), [[DPH5-DT]] (-0.74, fdr 1e-05), [[ST7L]] (-0.73, fdr 1e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GPR160]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6138.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.82×** | +10.7 | 1e-23 | 46/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.79×** | +10.5 | 2e-23 | 45/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.48×** | +9.3 | 2e-18 | 45/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.30×** | +7.7 | 2e-12 | 39/43 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.04×** | +7.0 | 2e-10 | 32/38 (A-172, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +5.3 | 1e-05 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +4.6 | 4e-04 | 39/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.002 | 26/48 (RKO, LS 180, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.50×** | +4.1 | 0.002 | 31/47 (A-427, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.46×** | +3.6 | 0.020 | 22/42 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +3.1 | 0.095 | 20/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.1 | 0.099 | 23/48 (PANC-1, Panc 03.27, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.23× | +3.0 | 0.12 | 25/48 (SW480, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6138.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.729×** | -4.6 | 0.003 | 25/48 (HOP62, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.670×** | -4.1 | 0.012 | 29/48 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.680×** | -3.9 | 0.015 | 25/48 (MIA PaCa-2, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.695×** | -3.7 | 0.027 | 27/48 (HEC-1-A, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.704×** | -3.6 | 0.036 | 26/48 (NCI-H1573, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.699×** | -3.5 | 0.051 | 29/47 (A-172, RPMI-7951, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.729×** | -3.2 | 0.097 | 27/48 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6138. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 66.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 38.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.289× (z -8.5) |
| [[SW480 (line)]] | alt | 31.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 25.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.49× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 26.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.83× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 33.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.35× (z +9.6) | — |
| [[A-172 (line)]] | wt | 56.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[AN3 CA (line)]] | alt | 55.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -8.6) |
| [[Hs 766T (line)]] | wt | 43.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -10.3) |
| [[HS-578T (line)]] | alt | 51.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -9.3) |
| [[KATO III (line)]] | alt | 24.9 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.61× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 29.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -8.8) |
| [[NCI-H661 (line)]] | alt | 34.0 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.05 µM 0.0721× (z -8.5) |
| [[PANC-1 (line)]] | alt | 50.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RKO (line)]] | wt | 23.9 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.06× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 32.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.22× (z +9.0) | — |
| [[A-427 (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6138), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMCL1]] | +0.77 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[PJA2]] | +0.77 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[PLEKHH3]] | +0.76 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[PPP1R2]] | +0.76 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.76 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[YIF1B]] | +0.74 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[TMEM256]] | +0.74 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ANG]] | +0.73 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[USP48]] | +0.72 | +0.77 / +0.53 | both halves | 1e-05 |  |
| [[RAP1A]] | +0.72 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[RRAS]] | +0.71 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[HEATR5B]] | +0.70 | +0.60 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP20]] | -0.74 | -0.70 / -0.62 | both halves | 7e-06 |  |
| [[DPH5-DT]] | -0.74 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[ST7L]] | -0.73 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[GPATCH4]] | -0.73 | -0.75 / -0.57 | both halves | 1e-05 |  |
| [[DNAJC11]] | -0.73 | -0.70 / -0.60 | both halves | 7e-06 | pathway: Organelle biogenesis and maintenance |
| [[AVEN]] | -0.71 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[ZNF124]] | -0.70 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[DHX37]] | -0.70 | -0.72 / -0.58 | both halves | 8e-06 |  |
| [[SNAPC5]] | -0.69 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[NIP7]] | -0.68 | -0.74 / -0.58 | both halves | 7e-06 |  |
| [[ITPA]] | -0.68 | -0.65 / -0.40 | both halves | 4e-05 |  |
| [[ZNF507]] | -0.67 | -0.56 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR160]] | B | GPR160 activity lowers ARL3's level | lines that do not express GPR160 (8) vs lines expressing it (42) | 1.35× higher at baseline in the lines without GPR160 | 0.052 | ⚠ within organs, on part of the lines; also absent: PNPLA4, PRKCZ; maybe low, not absent |
| [[C1QL1]] | B | C1QL1 activity raises ARL3's level | lines that do not express C1QL1 (22) vs lines expressing it (28) | 1.32× lower at baseline in the lines without C1QL1 | 0.089 | ⚠ within organs, on part of the lines; also absent: CPEB1, PDZD4, BARX1 |
| [[HDAC6]] | B | HDAC6 activity lowers ARL3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.583). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (4.0, -12.2); signed map (-33.1, 16.0). **Vector** length 101, 30.4% of its response variance represented; |z| ≥ 3 in 715 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.1 | +9.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +10.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.8 | +10.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.5 | +5.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -0.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.8 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.9 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -4.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:102,673,731-102,714,397 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARFL3 |
| Gene groups (HGNC) | ARF GTPase family |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 5 pathways, smallest: Trafficking of myristoylated proteins to the cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [P36405](https://www.uniprot.org/uniprotkb/P36405) (ADP-ribosylation factor-like protein 3):

> Small GTP-binding protein which cycles between an inactive GDP-bound and an active GTP-bound form, and the rate of cycling is regulated by guanine nucleotide exchange factors (GEF) and GTPase-activating proteins (GAP). Required for normal cytokinesis and cilia signaling. Required for targeting proteins to the cilium, including myristoylated NPHP3 and prenylated INPP5E. Targets NPHP3 to the ciliary membrane by releasing myristoylated NPHP3 from UNC119B cargo adapter into the cilium. Required for …

**Summary**, from NCBI Gene [403](https://www.ncbi.nlm.nih.gov/gene/403):

> Enables GDP binding activity; GTP binding activity; and microtubule binding activity. Involved in several processes, including cilium assembly; protein localization to cilium; and small GTPase-mediated signal transduction. Acts upstream of or within post-Golgi vesicle-mediated transport. Located in several cellular components, including microtubule cytoskeleton; midbody; and photoreceptor connecting cilium. Implicated in Joubert syndrome and retinitis pigmentosa 83. [provided by Alliance of …

**Accessions** — [HGNC:694](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:694) · Entrez [403](https://www.ncbi.nlm.nih.gov/gene/403) · UniProt [P36405](https://www.uniprot.org/uniprotkb/P36405) · Ensembl [ENSG00000138175](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138175)

## Data

Gene col 6138: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6138); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6138, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6138]; `tensor/DDL_lfc|DDL_z.npy` [6138]; `embed/gene_vectors.npy` [6138]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6138 or target_col == 6138). Every well: [[ARL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

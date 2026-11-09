---
symbol: "PPM1M"
type: "gene"
col: 8863
ensembl_id: "ENSG00000164088"
name: "protein phosphatase, Mg2+/Mn2+ dependent 1M"
location: "3p21.2"
module: 157
arm: "+"
pooled_cpm: 2.04
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 16
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# PPM1M

*protein phosphatase, Mg2+/Mn2+ dependent 1M* — 3p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.84× (z +11.2, q 2e-26, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 2.37× (z +5.3, q 1e-05, up in 4 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.347× (z -9.2, q 3e-17, down in 28 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA20]] (+0.65, fdr 1e-05), [[ACCS]] (+0.61, fdr 2e-05), [[LMNTD2]] (+0.59, fdr 2e-05); moves opposite to [[UBE2V2]] (-0.47, fdr 1e-04), [[NCBP2]] (-0.45, fdr 3e-04), [[METTL2B]] (-0.44, fdr 6e-04).
> It is in [[Module 157]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[REEP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8863.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.84×** | +11.2 | 2e-26 | 1/2 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.12×** | +9.8 | 2e-20 | 7/10 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.19×** | +9.3 | 3e-18 | 1/3 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.37×** | +5.3 | 1e-05 | 4/12 (PANC-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.74×** | +4.8 | 2e-04 | 7/42 (HEC-1-A, NCI-H2030, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.42×** | +4.3 | 0.001 | 3/41 (RKO, LoVo, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.64×** | +4.3 | 0.001 | 8/35 (A-427, SK-MEL-2, …) | rises with dose | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.52×** | +4.1 | 0.003 | 0/5 | rises with dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.88×** | +3.9 | 0.006 | 6/23 (A498, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +3.9 | 0.006 | 2/12 (SW480, KATO III) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.68×** | +3.2 | 0.073 | 2/22 (HOP62, LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.65×** | +3.1 | 0.091 | 1/18 (A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +3.1 | 0.091 | 3/28 (Panc 03.27, A498, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.091 | 4/35 (A-172, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8863.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.347×** | -9.2 | 3e-17 | 28/44 (A-427, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.407×** | -7.8 | 2e-12 | 19/28 (NCI-H2030, SW480, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.430×** | -7.3 | 5e-11 | 21/35 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.458×** | -6.8 | 2e-09 | 19/32 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.585×** | -6.6 | 6e-09 | 22/31 (A498, PANC-1, …) | two highest doses | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.520×** | -5.7 | 1e-06 | 9/16 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.508×** | -5.6 | 1e-06 | 14/37 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.548×** | -5.2 | 1e-05 | 16/43 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.641×** | -3.8 | 0.008 | 11/39 (LOX-IMVI, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.738×** | -3.7 | 0.012 | 8/27 (NCI-H2030, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.661×** | -3.6 | 0.018 | 11/33 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.663×** | -3.6 | 0.018 | 10/40 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.464×** | -3.4 | 0.026 | 9/24 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.674×** | -3.4 | 0.026 | 11/38 (Panc 03.27, A-427, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.682×** | -3.1 | 0.067 | 3/30 (J82, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | **0.697×** | -3.0 | 0.096 | 11/33 (hTERT-HPNE, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8863. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.54 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0402× (z -11.8) |
| [[A-427 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.742 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.742 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.716 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.966 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.964 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.903 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.750 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8863), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA20]] | +0.65 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ACCS]] | +0.61 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[LMNTD2]] | +0.59 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[IL11RA]] | +0.58 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[SLC37A4]] | +0.56 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SPIN2B]] | +0.55 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[ACBD4]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[GSTM4]] | +0.54 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[GHDC]] | +0.54 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[CACFD1]] | +0.53 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[GSTM2]] | +0.52 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[ROGDI]] | +0.52 | +0.55 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2V2]] | -0.47 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[NCBP2]] | -0.45 | -0.44 / -0.26 | both halves | 3e-04 |  |
| [[METTL2B]] | -0.44 | -0.48 / -0.22 | both halves | 6e-04 |  |
| [[PRR14L]] | -0.43 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[BZW1]] | -0.43 | -0.30 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[REEP2]] | B | REEP2 activity raises PPM1M's level | lines that do not express REEP2 (12) vs lines expressing it (38) | 1.26× lower at baseline in the lines without REEP2 | 0.097 | ⚠ within organs, on part of the lines; also absent: DLK2, ENSG00000234405, STARD9; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.515). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.4, 29.7); signed map (-0.5, 5.5). **Vector** length 35.1, 3.69% of its response variance represented; |z| ≥ 3 in 862 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +2.8 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +11.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.4 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +9.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +4.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -7.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.9 | -6.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -9.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.5 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.5 | -7.8 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.8 | -2.1 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -2.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -0.8 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -0.8 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase, Mg2+/Mn2+ dependent 1M |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.2 — chr3:52,245,759-52,250,599 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PP2Ceta, FLJ32332 |
| Gene groups (HGNC) | Protein phosphatases, Mg2+/Mn2+ dependent |
| Matched by | ensembl_id |

UniProt [Q96MI6](https://www.uniprot.org/uniprotkb/Q96MI6) carries no function annotation.

**Summary**, from NCBI Gene [132160](https://www.ncbi.nlm.nih.gov/gene/132160):

> Predicted to enable [pyruvate dehydrogenase (acetyl-transferring)]-phosphatase activity and manganese ion binding activity. Predicted to be involved in protein dephosphorylation. Predicted to be located in nucleus. Predicted to be active in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26506](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26506) · Entrez [132160](https://www.ncbi.nlm.nih.gov/gene/132160) · UniProt [Q96MI6](https://www.uniprot.org/uniprotkb/Q96MI6) · Ensembl [ENSG00000164088](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164088)

## Data

Gene col 8863: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8863); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8863, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8863]; `tensor/DDL_lfc|DDL_z.npy` [8863]; `embed/gene_vectors.npy` [8863]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8863 or target_col == 8863). Every well: [[PPM1M — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPM1M.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

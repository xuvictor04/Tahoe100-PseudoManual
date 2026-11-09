---
symbol: "TMEM187"
type: "gene"
col: 10870
ensembl_id: "ENSG00000177854"
name: "transmembrane protein 187"
location: "Xq28"
module: 15
arm: "+"
pooled_cpm: 3.29
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 20
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# TMEM187

*transmembrane protein 187* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.74× (z +15.4, q 0e+00, up in 29 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.349× (z -11.4, q 3e-27, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENDOG]] (+0.65, fdr 1e-04), [[SMIM12]] (+0.63, fdr 1e-05), [[ZNF862]] (+0.61, fdr 1e-05); moves opposite to [[MOCS2]] (-0.64, fdr 3e-05), [[RPAP3]] (-0.60, fdr 0.002, ⚠ one half only (not replicated)), [[SOAT1]] (-0.58, fdr 1e-04), [[NDRG3]] (-0.56, fdr 5e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MPP1]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10870.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.74×** | +15.4 | 0e+00 | 29/32 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +8.6 | 3e-15 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +5.2 | 4e-05 | 9/28 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +4.8 | 2e-04 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.77×** | +4.4 | 0.001 | 3/10 (A498, A-172, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +4.4 | 0.001 | 3/17 (A549, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.5 | 0.038 | 3/17 (PANC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.038 | 1/40 (HEC-1-A) | rises with dose |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.4 | 0.038 | 1/39 (A-427) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.050 | 1/47 (J82) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.050 | 2/24 (J82, HEC-1-A) | inconsistent across doses | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.32× | +3.0 | 0.12 | 3/38 (LS 180, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10870.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.349×** | -11.4 | 3e-27 | 31/43 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.471×** | -8.2 | 1e-13 | 20/43 (NCI-H2030, LoVo, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.507×** | -7.4 | 4e-11 | 23/46 (LoVo, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.522×** | -6.7 | 4e-09 | 20/37 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.655×** | -6.5 | 1e-08 | 22/34 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.574×** | -6.0 | 2e-07 | 18/45 (A-172, C-33 A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.578×** | -5.9 | 2e-07 | 21/41 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.422×** | -4.9 | 7e-05 | 13/37 (PANC-1, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.654×** | -4.4 | 6e-04 | 14/22 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.679×** | -4.2 | 0.002 | 9/45 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.683×** | -4.1 | 0.002 | 10/25 (HOP62, PANC-1, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.774×** | -3.9 | 0.004 | 12/43 (NCI-H1573, SW 900, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.501×** | -3.9 | 0.004 | 10/29 (A-172, J82, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.692×** | -3.7 | 0.009 | 7/42 (LOX-IMVI, C-33 A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.705×** | -3.6 | 0.010 | 12/39 (Panc 03.27, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.725×** | -3.5 | 0.016 | 15/41 (NCI-H1573, SHP-77, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Asciminib (drug)]] 0.05 µM |  | **0.734×** | -3.3 | 0.026 | 8/42 (RKO, HEC-1-A, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.756×** | -3.0 | 0.069 | 11/34 (A549, LS 180, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10870. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.46 | 0 | 6 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.134× (z -12.7) |
| [[A-172 (line)]] | wt | 5.98 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -8.6) |
| [[A-427 (line)]] | wt | 3.53 | 0 | 1 | — | [[Bestatin (drug)]] 5 µM 0.0602× (z -9.1) |
| [[A498 (line)]] | wt | 4.75 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -9.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 3.82 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0721× (z -9.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 4.01 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -9.7) |
| [[LoVo (line)]] | wt | 2.10 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0478× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 2.52 | 0 | 1 (1 ⚠) | — | [[Glasdegib (drug)]] 5 µM 0.0607× (z -8.5) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 3.11 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.127× (z -8.8) |
| [[SW1417 (line)]] | alt | 2.80 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0612× (z -8.8) |
| [[A549 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10870), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENDOG]] | +0.65 | +0.35 / +0.71 | both halves | 1e-04 |  |
| [[SMIM12]] | +0.63 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[ZNF862]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[ANKRD17-DT]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[KIAA2026]] | +0.60 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[DICER1-AS1]] | +0.60 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[NIFK-AS1]] | +0.59 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[DDX59-AS1]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[LINC01301]] | +0.58 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[PCMTD1-DT]] | +0.58 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[SPESP1]] | +0.58 | +0.56 / +0.40 | both halves | 4e-05 |  |
| [[TMEM186]] | +0.57 | +0.47 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOCS2]] | -0.64 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[RPAP3]] | -0.60 | -0.14 / -0.65 | ⚠ one half (not replicated) | 0.002 |  |
| [[SOAT1]] | -0.58 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[NDRG3]] | -0.56 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[HDAC1]] | -0.56 | -0.29 / -0.60 | both halves | 2e-04 |  |
| [[DLD]] | -0.55 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[VAMP7]] | -0.55 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[HSD17B4]] | -0.55 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[STARD3NL]] | -0.53 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[DNM1]] | -0.53 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[CYB5R1]] | -0.52 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[PRKCI]] | -0.52 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[API5]] | -0.52 | -0.28 / -0.59 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPP1]] | B | MPP1 activity lowers TMEM187's level | lines that do not express MPP1 (7) vs lines expressing it (43) | 1.17× higher at baseline in the lines without MPP1 | 0.087 | ⚠ within organs, on part of the lines; also absent: ZNF566, ELOVL5, PALM2AKAP2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | TMEM187's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | TMEM187's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.421 over the table, 0.043 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.561). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.3, 19.0); signed map (18.7, -6.8). **Vector** length 48.3, 5.86% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +15.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +5.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.9 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.7 | -3.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -11.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.8 | -6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.5 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -2.9 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -0.7 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 187 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:153,972,754-153,983,194 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ITBA1, DXS9878E; previously CXorf12 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q14656](https://www.uniprot.org/uniprotkb/Q14656) carries no function annotation.

**Summary**, from NCBI Gene [8269](https://www.ncbi.nlm.nih.gov/gene/8269):

> This gene consists of two exons and encodes a multi-pass membrane protein. An alternatively spliced transcript variant encoding the same protein has been found, but its biological validity is not determined. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:13705](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13705) · Entrez [8269](https://www.ncbi.nlm.nih.gov/gene/8269) · UniProt [Q14656](https://www.uniprot.org/uniprotkb/Q14656) · Ensembl [ENSG00000177854](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177854)

## Data

Gene col 10870: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10870); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10870, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10870]; `tensor/DDL_lfc|DDL_z.npy` [10870]; `embed/gene_vectors.npy` [10870]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10870 or target_col == 10870). Every well: [[TMEM187 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM187.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
